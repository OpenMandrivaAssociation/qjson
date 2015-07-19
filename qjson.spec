Summary:	QJson is a qt-based library that maps JSON data to QVariant objects
Name:		qjson
Version:	0.8.1
Release:	9
License:	GPLv2
Group:		Development/C
Url:		http://qjson.sourceforge.net/
Source0:	http://freefr.dl.sourceforge.net/project/qjson/qjson/%{version}/qjson-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel

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
Summary:	QJson is a qt-based library that maps JSON data to QVariant objects
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Obsoletes:	%{name} < %{EVRD}

%description -n   %{libname}
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs.
QJson is a qt-based library that maps JSON data to QVariant objects.
JSON arrays will be mapped to QVariantList instances, while JSON's objects
will be mapped to QVariantMap.

%files -n   %{libname}
%{_libdir}/libqjson.so.%{major}*

#--------------------------------------------------------------------

%define devname %mklibname -d qjson

%package -n %{devname}
Summary:	Development files for QJson
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}
Conflicts:	qjson < %{EVRD}

%description -n %{devname}
This package contains files for developing applications using 
QJson.

%files -n %{devname}
%{_libdir}/libqjson.so
%{_libdir}/pkgconfig/QJson.pc
%{_libdir}/cmake/%{name}
%{_includedir}/qjson

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

