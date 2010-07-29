Name:		dudf
Summary:	Mandriva implementation of DUDF as part of the Mancoosi European Project
Version:	0.1
Release:	%mkrel 1
Group:		System/Base
License:	GPL
URL:		http://git.mandriva.com/?p=projects/dudf.git

Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl

%description
Mancoosi aims at achieving better management of software upgrades.
As part of this European project, urpmi can generate information about
installation failure when it arises and provide it to Mandriva engineers
and Mancoosi project members to help solving the issue. This is achieved
via a DUDF file, where DUDF stands for Distribution Upgradeability 
Description Format. 
The current package provides libdudf, a C++ library aiming at generating
this DUDF file, together with a Perl wrapper, perl-dudfrpmstatus, which is
used by urpmi.

#### Each generated package follows

#--- The libdudf package
%define dudf_major 0
%define libdudf %mklibname dudf %{dudf_major}

%package -n %{libdudf}
Summary:	Mandriva DUDF file generation library
Group:		System/Libraries
BuildRequires:	gcc-cpp
BuildRequires:	jsoncpp-devel
BuildRequires:	libxml2-devel
BuildRequires:	librpm-devel
BuildRequires:	libopenssl1.0.0-devel
Requires:	libxml2
Requires:	jsoncpp
Requires:	librpm
Requires:	openssl
Provides:	libdudf
Provides:	libdudf.so

%description -n %{libdudf}
Library used for generating the Mandriva DUDF file.

%files -n %{libdudf}
%defattr(-,root,root,-)
%{_libdir}/libdudf.so

#--- The perl-dudfrpmstatus package

%package -n perl-dudfrpmstatus
Summary:	Mandriva DUDF file generation library Perl wrapper
Group:		System/Libraries
BuildRequires:	swig
BuildRequires:	perl-devel
Requires:	libdudf
Provides:	perl-dudfrpmstatus
Provides:	dudfrpmstatus.so
Provides:	dudfrpmstatus.pm

%description -n perl-dudfrpmstatus
Perl wrapper providing access to the Mandriva DUDF file generation
library.

%files -n perl-dudfrpmstatus
%defattr(-,root,root,-)
%{perl_sitearch}/dudfrpmstatus.pm
%{perl_sitearch}/auto/dudfrpmstatus/dudfrpmstatus.so

########### Now compile code!
%prep
%setup -q

%build
%make

%install
%{__rm} -rf %buildroot
%{__mkdir_p} %buildroot/%{_libdir}
%{__make} DESTDIR=%buildroot LIBDIR=%{_libdir} install

%clean
%{__rm} -rf %buildroot
