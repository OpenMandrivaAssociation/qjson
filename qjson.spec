Name:		qjson
Version:	0.7.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Databases
URL:		http://qjson.sourceforge.net
Source:		http://sourceforge.net/projects/qjson/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	libqt4-devel >= 4.0
BuildRequires:	cmake >= 2.6
BuildRequires:	kde4-macros
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Summary:	Lightweight data-interchange format

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It can represents integer, real number, string, an ordered sequence of value, and a collection of name/value pairs.

QJson is a qt-based library that maps JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances, while JSON objects will be mapped to QVariantMap.

%package devel
Summary:	Lightweight data-interchange format - devel

%description -n %{name}-devel
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It can represents integer, real number, string, an ordered sequence of value, and a collection of name/value pairs.

QJson is a qt-based library that maps JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances, while JSON objects will be mapped to QVariantMap.

Devel package

%files
%defattr (-,root,root)
%doc COPYING README INSTALL
%{_libdir}/lib*

%files -n %{name}-devel
%defattr (-,root,root)
%doc COPYING README INSTALL
%{_includedir}/%{name}
%{_kde_appsdir}/cmake/modules/FindQJSON.cmake
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean 
rm -rf %{buildroot}
