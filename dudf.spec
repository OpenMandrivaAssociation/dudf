Name:		dudf
Summary:	Mandriva implementation of DUDF as part of the Mancoosi European Project
Version:	0.15
Release:	5
Group:		System/Base
License:	GPLv2+
URL:		http://www.mancoosi.org

Source0:	%{name}-%{version}.tar.xz
Patch0:		dudf-0.15-fix-test-linking.patch
BuildRequires:	swig
BuildRequires:	perl-devel
BuildRequires:	jsoncpp-devel >= 0.5.0-11
BuildRequires:	libxml2-devel
BuildRequires:	rpm-devel
BuildRequires:	ossp-uuid-devel
BuildRequires:	cppunit-devel

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

%define	major	1
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name} %{major}

%package -n	%{libname}
Summary:	Mandriva DUDF file generation library
Group:		System/Libraries

%description -n	%{libname}
Library used for generating the Mandriva DUDF file.

%package -n	%{devname}
Summary:	Development header & library for Mandriva DUDF library
Group:		Development/C++
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development header & library for Mandriva DUDF file generation library.

%package -n	perl-dudfrpmstatus
Summary:	Mandriva DUDF file generation library Perl wrapper
Group:		System/Libraries

%description -n	perl-dudfrpmstatus
Perl wrapper providing access to the Mandriva DUDF file generation
library.

%prep
%setup -q
%patch0 -p1 -b .libs~
%build
export LDFLAGS="%{ldflags}"
%define	_disable_ld_no_undefined 1
export PERL_LDFLAGS="%{ldflags}"
%make CXXFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std prefix=%{_prefix} libdir=%{_libdir}

%files -n %{libname}
%{_libdir}/libdudf.so.%{major}*

%files -n %{devname}
%{_libdir}/libdudf.so
%{_includedir}/dudf.h

%files -n perl-dudfrpmstatus
%{perl_sitearch}/dudfrpmstatus.pm
%{perl_sitearch}/auto/dudfrpmstatus/dudfrpmstatus.so
