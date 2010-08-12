Summary:	Lightweight data-interchange format
Name:		qjson
Version:	0.7.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Databases
URL:		http://qjson.sourceforge.net
Source:		http://sourceforge.net/projects/qjson/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	lib64qt4-devel >= 4.0
BuildRequires:	cmake >= 2.6
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It can represents integer, real number, string, an ordered sequence of value, and a collection of name/value pairs.

QJson is a qt-based library that maps JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances, while JSON objects will be mapped to QVariantMap.

%files
%defattr (-,root,root)
%doc COPYING README INSTALL
%{_includedir}/%{name}
%{_libdir}/lib*
%{_libdir}/pkgconfig/*
%{_kde_appsdir}/cmake/modules/FindQJSON.cmake

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
