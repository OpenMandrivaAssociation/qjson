Name:           qjson
Summary:        QJson is a qt-based library that maps JSON data to QVariant objects
Version:        0.8.1
Release:        2
License:        GPLv2
Url:            http://qjson.sourceforge.net/
Group:          Development/C
BuildRequires:  cmake
BuildRequires:  qt4-devel
Source0:        http://freefr.dl.sourceforge.net/project/qjson/qjson/%version/qjson-%version.tar.bz2

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format. 
It can represents integer, real number, string, an ordered sequence of value, 
and a collection of name/value pairs.
QJson is a qt-based library that maps JSON data to QVariant objects.
JSON arrays will be mapped to QVariantList instances, while JSON's objects 
will be mapped to QVariantMap.

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname qjson %{major}

%package -n   %{libname}
Summary:      QJson is a qt-based library that maps JSON data to QVariant objects
Group:        System/Libraries
Provides:     %name = %EVRD
Obsoletes:    %name < %EVRD

%description -n   %{libname}
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs.
QJson is a qt-based library that maps JSON data to QVariant objects.
JSON arrays will be mapped to QVariantList instances, while JSON's objects
will be mapped to QVariantMap.

%files -n   %{libname}
%defattr(-,root,root)
%_libdir/libqjson.so.%{major}*

#--------------------------------------------------------------------

%define develname %mklibname -d qjson

%package -n %{develname}
Summary:      Development files for QJson
Group:        Development/C
Requires:     %libname = %EVRD
Provides:     %name-devel = %EVRD
Obsoletes:    %{name}-devel < %EVRD
Conflicts:    qjson < %EVRD

%description -n %{develname}
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs.
QJson is a qt-based library that maps JSON data to QVariant objects.
JSON arrays will be mapped to QVariantList instances, while JSON's objects
will be mapped to QVariantMap.

This package contains files for developing applications using 
QJson.

%files -n %{develname}
%defattr(-,root,root)
%_libdir/libqjson.so
%_libdir/pkgconfig/QJson.pc
%_libdir/cmake/%name
%_includedir/qjson

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-6mdv2011.0
+ Revision: 669381
- mass rebuild

* Sun Sep 05 2010 Funda Wang <fwang@mandriva.org> 0.7.1-5mdv2011.0
+ Revision: 576084
- correct package name

* Fri Aug 13 2010 Bruno Cornec <bcornec@mandriva.org> 0.7.1-4mdv2011.0
+ Revision: 569402
- Add Group for package devel which prevents upload
- And bump release tag :-(
- Adds missing deps for chroot build) - rpm macros for cmake
- Split in 2 packages for correct dependencies management (main and devel)
- Addition of the qjson package to improve support of tellico
- create qjson

