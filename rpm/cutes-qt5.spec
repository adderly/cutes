Name:    cutes-qt5
Summary: QtScript environment and "interpreter"
Version: 0.0.0
Release: 1

License: LGPLv2
Group:	 System/Shells
URL:     http://github.com/nemomobile/cutes
Source0: %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: cmake >= 2.8
BuildRequires: pkgconfig(tut) >= 0.0.1
BuildRequires: pkgconfig(cor) >= 0.1.6
Provides: cutes = %{version}
Obsoletes: cutes < 0.7.10

%description
QtScript environment and "interpreter"

%define qt_importdir %{_libdir}/qt5/qml

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DUSEQT=5
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/cutes
%{_libdir}/libcutescript-qt5.so
%{qt_importdir}/Mer/QtScript/libqtscript.so
%{qt_importdir}/Mer/QtScript/qmldir
%{_mandir}/man1/cutes.1.gz
