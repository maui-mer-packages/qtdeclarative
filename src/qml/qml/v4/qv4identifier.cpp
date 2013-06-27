/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the QtQml module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and Digia.  For licensing terms and
** conditions see http://qt.digia.com/licensing.  For further information
** use the contact form at http://qt.digia.com/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Digia gives you certain additional
** rights.  These rights are described in the Digia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3.0 as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU General Public License version 3.0 requirements will be
** met: http://www.gnu.org/copyleft/gpl.html.
**
**
** $QT_END_LICENSE$
**
****************************************************************************/
#include "qv4identifier_p.h"

QT_BEGIN_NAMESPACE

namespace QV4 {

static const uchar prime_deltas[] = {
    0,  0,  1,  3,  1,  5,  3,  3,  1,  9,  7,  5,  3,  9, 25,  3,
    1, 21,  3, 21,  7, 15,  9,  5,  3, 29, 15,  0,  0,  0,  0,  0
};

static inline int primeForNumBits(int numBits)
{
    return (1 << numBits) + prime_deltas[numBits];
}


IdentifierIntHashData::IdentifierIntHashData(int numBits)
    : refCount(Q_BASIC_ATOMIC_INITIALIZER(1))
    , numBits(numBits)
    , size(0)
{
    alloc = primeForNumBits(numBits);
    entries = (IdentifierIntHash::Entry *)malloc(alloc*sizeof(IdentifierIntHash::Entry));
    memset(entries, 0, alloc*sizeof(IdentifierIntHash::Entry));
}

IdentifierIntHash::IdentifierIntHash(ExecutionEngine *engine)
{
    d = new IdentifierIntHashData(3);
    d->identifierTable = engine->identifierTable;
}

void IdentifierIntHash::add(const QString &str, int value)
{
    Identifier *i = d->identifierTable->identifier(str);
    addEntry(i, value);
}

int IdentifierIntHash::value(const QString &str)
{
    return lookup(d->identifierTable->identifier(str));
}

int IdentifierIntHash::value(String *str)
{
    return lookup(d->identifierTable->identifier(str));
}

QString IdentifierIntHash::findId(int value) const
{
    Entry *e = d->entries;
    Entry *end = e + d->alloc;
    while (e < end) {
        if (e->value == value)
            return e->identifier->string;
    }
    return QString();
}


void IdentifierIntHash::addEntry(const Identifier *identifier, uint value)
{
    // fill up to max 50%
    bool grow = (d->alloc <= d->size*2);

    if (grow) {
        ++d->numBits;
        int newAlloc = primeForNumBits(d->numBits);
        Entry *newEntries = (Entry *)malloc(newAlloc * sizeof(Entry));
        memset(newEntries, 0, newAlloc*sizeof(Entry));
        for (uint i = 0; i < d->alloc; ++i) {
            const Entry &e = d->entries[i];
            if (!e.identifier)
                continue;
            uint idx = hash(e.identifier) % newAlloc;
            while (newEntries[idx].identifier) {
                ++idx;
                idx %= newAlloc;
            }
            newEntries[idx] = e;
        }
        free(d->entries);
        d->entries = newEntries;
        d->alloc = newAlloc;
    }

    uint idx = hash(identifier) % d->alloc;
    while (d->entries[idx].identifier) {
        Q_ASSERT(d->entries[idx].identifier != identifier);
        ++idx;
        idx %= d->alloc;
    }
    d->entries[idx].identifier = identifier;
    d->entries[idx].value = value;
    ++d->size;
}

int IdentifierIntHash::lookup(const Identifier *identifier) const
{
    assert(d->entries);

    uint idx = hash(identifier) % d->alloc;
    while (1) {
        if (d->entries[idx].identifier == identifier)
            return d->entries[idx].value;
        if (!d->entries[idx].identifier)
            return -1;
        ++idx;
        idx %= d->alloc;
    }
}



IdentifierTable::IdentifierTable(ExecutionEngine *engine)
    : engine(engine)
    , size(0)
    , numBits(8)
{
    alloc = primeForNumBits(numBits);
    entries = (String **)malloc(alloc*sizeof(String *));
    memset(entries, 0, alloc*sizeof(String *));
}

IdentifierTable::~IdentifierTable()
{
    free(entries);
}

void IdentifierTable::addEntry(String *str)
{
    uint hash = str->hashValue();

    if (str->subtype >= String::StringType_UInt)
        return;

    str->identifier = new Identifier;
    str->identifier->string = str->toQString();
    str->identifier->hashValue = hash;

    bool grow = (alloc <= size*2);

    if (grow) {
        ++numBits;
        int newAlloc = primeForNumBits(numBits);
        String **newEntries = (String **)malloc(newAlloc*sizeof(String *));
        memset(newEntries, 0, newAlloc*sizeof(String *));
        for (uint i = 0; i < alloc; ++i) {
            String *e = entries[i];
            if (!e)
                continue;
            uint idx = e->stringHash % newAlloc;
            while (newEntries[idx]) {
                ++idx;
                idx %= newAlloc;
            }
            newEntries[idx] = e;
        }
        free(entries);
        entries = newEntries;
        alloc = newAlloc;
    }

    uint idx = hash % alloc;
    while (entries[idx]) {
        ++idx;
        idx %= alloc;
    }
    entries[idx] = str;
    ++size;
}



String *IdentifierTable::insertString(const QString &s)
{
    uint hash = String::createHashValue(s.constData(), s.length());
    uint idx = hash % alloc;
    while (String *e = entries[idx]) {
        if (e->stringHash == hash && e->toQString() == s)
            return e;
        ++idx;
        idx %= alloc;
    }

    String *str = engine->newString(s);
    addEntry(str);
    return str;
}


Identifier *IdentifierTable::identifier(String *str)
{
    if (str->identifier)
        return str->identifier;
    uint hash = str->hashValue();
    if (str->subtype >= String::StringType_UInt)
        return 0;

    uint idx = hash % alloc;
    while (String *e = entries[idx]) {
        if (e->stringHash == hash && e->isEqualTo(str)) {
            str->identifier = e->identifier;
            return e->identifier;
        }
        ++idx;
        idx %= alloc;
    }

    addEntry(str);
    return str->identifier;
}

Identifier *IdentifierTable::identifier(const QString &s)
{
    return insertString(s)->identifier;
}

Identifier *IdentifierTable::identifier(const char *s, int len)
{
    uint hash = String::createHashValue(s, len);
    if (hash == UINT_MAX)
        return identifier(QString::fromUtf8(s, len));

    QLatin1String latin(s, len);
    uint idx = hash % alloc;
    while (String *e = entries[idx]) {
        if (e->stringHash == hash && e->toQString() == latin)
            return e->identifier;
        ++idx;
        idx %= alloc;
    }

    String *str = engine->newString(QString::fromLatin1(s, len));
    addEntry(str);
    return str->identifier;
}

}

QT_END_NAMESPACE
