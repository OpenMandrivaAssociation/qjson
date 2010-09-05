Name:           qjson
Summary:        QJson is a qt-based library that maps JSON data to QVariant objects
Version:        0.7.1
Release:        %mkrel 5
License:        GPLv2
Url:            http://qjson.sourceforge.net/
Group:          Development/C
BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://downloads.sourceforge.net/qjson/qjson-%{version}.tar.bz2

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
Provides:     %name = %version-%release
Obsoletes:    %name < 0.7.1-5

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
Requires:     %libname = %version-%release
Provides:     %name-devel = %version-%release
Obsoletes:    %{name}-devel < 0.7.1-5
Conflicts:    qjson < 0.7.1-5

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
%_datadir/apps/cmake/modules/FindQJSON.cmake
%_includedir/qjson

#--------------------------------------------------------------------

%prep
%setup -q -n qjson

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%clean
rm -rf %buildroot

