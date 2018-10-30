%define major 1
%define upstreamver %(echo %{version} |sed -e 's,\\\.,_,g')
Summary:	QJson is a qt-based library that maps JSON data to QVariant objects
Name:		qjson
Version:	1.0.0
Release:	3
License:	GPLv2
Group:		Development/C
Url:		http://qjson.sourceforge.net/
Source0:	https://github.com/flavio/qjson/archive/%{upstreamver}.tar.gz
Patch0:		qjson-1.0.0-fix-pkgconfig.patch
BuildRequires:	cmake ninja
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format. 
It can represents integer, real number, string, an ordered sequence of value, 
and a collection of name/value pairs.
QJson is a qt-based library that maps JSON data to QVariant objects.
JSON arrays will be mapped to QVariantList instances, while JSON's objects 
will be mapped to QVariantMap.

#--------------------------------------------------------------------

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
%autosetup -n %{name}-%{upstreamver}

%build
%cmake \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
