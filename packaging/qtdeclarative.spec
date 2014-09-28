# Package prefix
%define pkgname qt5-qtdeclarative

Name:       qtdeclarative
Summary:    Qt Declarative library
Version:    5.3.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.io
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qttest-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-qmake
BuildRequires:  fdupes
BuildRequires:  python
BuildRequires:  gdb

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Declarative library


%package -n qt5-qtdeclarative
Summary:    Qt Declarative library
Group:      Qt/Qt

%description -n qt5-qtdeclarative
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Declarative library


%package -n qt5-qtdeclarative-devel
Summary:    Qt Declarative - development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   qt5-qtsql-devel
Requires:   qt5-qtnetwork-devel

%description -n qt5-qtdeclarative-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the Declarative library development files


%package -n qt5-qtdeclarative-qtquicktest
Summary:    Qt Declarative QtQuickTest library
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtdeclarative-qtquicktest
This package contains the QtQuickTest library for QtDeclarative module


%package -n qt5-qtdeclarative-qtquicktest-devel
Summary:    Qt Declarative QtQuickTest - development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   %{pkgname}-devel = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquicktest = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquicktest-devel
This package contains the development headers for QtQuickTest library


%package -n qt5-qtdeclarative-qtquick
Summary:    Qt Declarative - QtQuick library
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquick
This package contains the QtQuick QML support library


%package -n qt5-qtdeclarative-qtquick-devel
Summary:    Qt Declarative - QtQuick development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquick = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquick-devel
This package contains the development headers for legacy QtQuick 1
QML support library


%package -n qt5-qtdeclarative-qtquickwidgets
Summary:    Qt Declarative - QtQuick Widgets library
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquickwidgets
This package contains the QtQuick Widgets support library


%package -n qt5-qtdeclarative-qtquickwidgets-devel
Summary:    Qt Declarative - QtQuick Widgets development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquickwidgets = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquickwidgets-devel
This package contains the development headers for QtQuickWidgets
QML support library


%package -n qt5-qtdeclarative-qtquickparticles
Summary:    Qt Declarative - QtQuick Particles library
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquickparticles
This package contains the QtQuick Particles support library


%package -n qt5-qtdeclarative-qtquickparticles-devel
Summary:    Qt Declarative - QtQuick Particles development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   qt5-qtdeclarative-qtquickparticles = %{version}-%{release}

%description -n qt5-qtdeclarative-qtquickparticles-devel
This package contains the development headers for QtQuickParticles
QML support library


%package -n qt5-qtdeclarative-qtdeclarativetools-devel
Summary:    Qt Declarative QtQmlDevTools - development files
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}
Requires:   %{pkgname}-devel = %{version}-%{release}
Requires:   qt5-qtdeclarative-devel = %{version}-%{release}

%description -n qt5-qtdeclarative-qtdeclarativetools-devel
This package contains the development headers for QtQmlDevTools


#### Small plugin and import packages


%package -n qt5-qtdeclarative-import-folderlistmodel
Summary:    Qt Declarative folderlistmodel plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-folderlistmodel
This package provides the QtQml folderlistmodel plugin


%package -n qt5-qtdeclarative-import-settings
Summary:    Qt Declarative settings plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-settings
This package provides the %{summary}


%package -n qt5-qtdeclarative-import-localstorageplugin
Summary:    Qt LocalStorage plugin
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-localstorageplugin
This package provided the Qt LocalStorage plugin


%package -n qt5-qtdeclarative-plugin-qmlinspector
Summary:    Qt Declarative QML inspector plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-plugin-qmlinspector
This package provides the QML inspector plugin


%package -n qt5-qtdeclarative-plugin-accessible
Summary:    Qt Declarative accessible plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-plugin-accessible
This package provides the QML accessible plugin


%package -n qt5-qtdeclarative-import-qtquick2plugin
Summary:    Qt Declarative QtQuick 2 support plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qtquick2plugin
This package provides the QtQuick 2 support plugin


%package -n qt5-qtdeclarative-import-qttest
Summary:    Qt Declarative QtTest plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-qttest
This package provides the QtQml QtTest plugin


%package -n qt5-qtdeclarative-import-particles2
Summary:    Qt Declarative Particles plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-particles2
This package provides the QtQml Particles.2 plugin


%package -n qt5-qtdeclarative-import-window2
Summary:    Qt Declarative Window plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-window2
This package provides the QtQml Window.2 plugin


%package -n qt5-qtdeclarative-import-models2
Summary:    Qt Declarative models plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-models2
This package provides the QtDeclarative models plugin for QtQuick 2.0


%package -n qt5-qtdeclarative-import-xmllistmodel
Summary:    Qt Declarative XmlListModel plugin
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-import-xmllistmodel
This package provides the QtDeclarative XmlListModel plugin for QtQuick 2.0


%package -n qt5-qtdeclarative-qmlscene
Summary:    QML scene viewer
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-qmlscene
This package contains the QML viewer for QtQuick 2.0 files.


%package -n qt5-qtdeclarative-tool-qml
Summary:    QML runtime binary
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-tool-qml
This package contains the %{summary} tool


%package -n qt5-qtdeclarative-tool-qmlimportscanner
Summary:    QML runtime binary
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-tool-qmlimportscanner
This package contains the %{summary} tool


%package -n qt5-qtdeclarative-devel-tools
Summary:    QML development tools
Group:      Qt/Qt
Requires:   %{pkgname} = %{version}-%{release}

%description -n qt5-qtdeclarative-devel-tools
This package contains QML debugging and development tools


%prep
%setup -q -n %{name}-%{version}/upstream

%build
export QTDIR=/usr/share/qt5
touch .git

#%ifarch armv8el
# to enable JIT, we need to enable thumb, as it is the only supported
# configuration for JIT on ARM. unfortunately, we are not currently in the right
# frame of mind to be able to deal with a full thumb transition, so we need to
# hack it in.
#
# OBS forces -mno-thumb, so first step, we need to remove that, and then add our
# own thumb argument. we can't do this in the .pro, as it won't propegate. we
# can't do it in .qmake.conf, because that's loaded too early. -after is *just*
# the right place: it's after everything has happened except for
# default_post.prf, which sets up the real QMAKE_C{XX}FLAGS, so brutally abuse
# it to acomplish our evil goals.
#%qmake5 -after \
#    QMAKE_CFLAGS_RELEASE-=-mno-thumb     QMAKE_CFLAGS_DEBUG-=-mno-thumb \
#    QMAKE_CXXFLAGS_RELEASE-=-mno-thumb   QMAKE_CXXFLAGS_DEBUG-=-mno-thumb \
#    QMAKE_CFLAGS_RELEASE+=-mthumb        QMAKE_CFLAGS_DEBUG+=-mthumb \
#    QMAKE_CXXFLAGS_RELEASE+=-mthumb      QMAKE_CXXFLAGS_DEBUG+=-mthumb
#%else
%qmake5
#%endif

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
    -exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
    -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Manually copy qmldevtools static library
cp lib/libQt5QmlDevTools.a %{buildroot}/%{_libdir}

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}


%post -n qt5-qtdeclarative
/sbin/ldconfig
%postun -n qt5-qtdeclarative
/sbin/ldconfig

%post -n qt5-qtdeclarative-qtquicktest
/sbin/ldconfig
%postun -n qt5-qtdeclarative-qtquicktest
/sbin/ldconfig

%post -n qt5-qtdeclarative-qtquick
/sbin/ldconfig
%postun -n qt5-qtdeclarative-qtquick
/sbin/ldconfig

%post -n qt5-qtdeclarative-qtquickwidgets
/sbin/ldconfig
%postun -n qt5-qtdeclarative-qtquickwidgets
/sbin/ldconfig

%post -n qt5-qtdeclarative-qtquickparticles
/sbin/ldconfig
%postun -n qt5-qtdeclarative-qtquickparticles
/sbin/ldconfig


%files -n qt5-qtdeclarative
%defattr(-,root,root,-)
%{_libdir}/libQt5Qml.so.5
%{_libdir}/libQt5Qml.so.5.*

# FIXME: the provided .pc file is empty!
# Find out what gives and find a clean resolution
%files -n qt5-qtdeclarative-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Qml.so
%{_libdir}/libQt5Qml.prl
%{_libdir}/pkgconfig/Qt5Qml.pc
%{_includedir}/qt5/QtQml/
%{_datadir}/qt5/mkspecs/modules/qt_lib_qml.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qml_private.pri
%{_libdir}/cmake/

%files -n qt5-qtdeclarative-qtquick
%defattr(-,root,root,-)
%{_libdir}/libQt5Quick.so.5
%{_libdir}/libQt5Quick.so.5.*

%files -n qt5-qtdeclarative-qtquick-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Quick.so
%{_libdir}/libQt5Quick.prl
%{_libdir}/pkgconfig/Qt5Quick.pc
%{_includedir}/qt5/QtQuick/
%{_datadir}/qt5/mkspecs/modules/qt_lib_quick.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_quick_private.pri

%files -n qt5-qtdeclarative-qmlscene
%defattr(-,root,root,-)
%{_qt5_bindir}/qmlscene

%files -n qt5-qtdeclarative-tool-qml
%defattr(-,root,root,-)
%{_qt5_bindir}/qml

%files -n qt5-qtdeclarative-tool-qmlimportscanner
%defattr(-,root,root,-)
%{_qt5_bindir}/qmlimportscanner

%files -n qt5-qtdeclarative-devel-tools
%defattr(-,root,root,-)
%{_qt5_bindir}/qmlplugindump
%{_qt5_bindir}/qmlprofiler
%{_qt5_bindir}/qmltestrunner
%{_qt5_bindir}/qmlmin
%{_qt5_bindir}/qmlbundle
%{_qt5_bindir}/qmljs

%files -n qt5-qtdeclarative-import-folderlistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt/labs/folderlistmodel/*

%files -n qt5-qtdeclarative-import-settings
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/Qt/labs/settings/*

%files -n qt5-qtdeclarative-import-localstorageplugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/LocalStorage/

%files -n qt5-qtdeclarative-plugin-qmlinspector
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/qmltooling/*

%files -n qt5-qtdeclarative-plugin-accessible
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/accessible/libqtaccessiblequick.so

%files -n qt5-qtdeclarative-import-qttest
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtTest/

%files -n qt5-qtdeclarative-import-qtquick2plugin
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick.2/

%files -n qt5-qtdeclarative-import-particles2
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Particles.2/

%files -n qt5-qtdeclarative-import-window2
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Window.2/

%files -n qt5-qtdeclarative-import-models2
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQml/Models.2/

%files -n qt5-qtdeclarative-import-xmllistmodel
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/XmlListModel/

%files -n qt5-qtdeclarative-qtquicktest
%defattr(-,root,root,-)
%{_libdir}/libQt5QuickTest.so.5
%{_libdir}/libQt5QuickTest.so.5.*

%files -n qt5-qtdeclarative-qtquicktest-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtQuickTest/
%{_libdir}/libQt5QuickTest.so
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/pkgconfig/Qt5QuickTest.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmltest.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmltest_private.pri

%files -n qt5-qtdeclarative-qtquickwidgets
%defattr(-,root,root,-)
%{_libdir}/libQt5QuickWidgets.so.5
%{_libdir}/libQt5QuickWidgets.so.5.*

%files -n qt5-qtdeclarative-qtquickwidgets-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtQuickWidgets/
%{_libdir}/libQt5QuickWidgets.so
%{_libdir}/libQt5QuickWidgets.prl
%{_libdir}/pkgconfig/Qt5QuickWidgets.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri

%files -n qt5-qtdeclarative-qtquickparticles
%defattr(-,root,root,-)
%{_libdir}/libQt5QuickParticles.so.5
%{_libdir}/libQt5QuickParticles.so.5.*

%files -n qt5-qtdeclarative-qtquickparticles-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtQuickParticles/
%{_libdir}/libQt5QuickParticles.so
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/pkgconfig/Qt5QuickParticles.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri

%files -n qt5-qtdeclarative-qtdeclarativetools-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5QmlDevTools.a
%{_libdir}/libQt5QmlDevTools.prl
%{_libdir}/pkgconfig/Qt5QmlDevTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri
