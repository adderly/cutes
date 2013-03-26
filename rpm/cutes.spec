
Name:    cutes
Summary: QtScript environment and "interpreter"
Version: 0.7.7
Release: 1

License: LGPLv2
Group:	 System/Shells
URL:     http://github.com/deztructor/cutes
Source0: %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtScript)
BuildRequires: cmake

%description
QtScript environment and "interpreter"

%if %{?_qt4_importdir:1}%{!?_qt4_importdir:0}
%define _qt_importdir %{_qt4_importdir}
%endif

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_libdir}/libcutescript.so
%{_qt_importdir}/Mer/QtScript/libqtscript.so
%{_qt_importdir}/Mer/QtScript/qmldir
%{_mandir}/man1/%{name}.1.gz
