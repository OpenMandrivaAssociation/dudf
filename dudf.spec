%if %{_use_internal_dependency_generator}
%define __noautoreq 'devel\\(libjsoncpp(.*)\\)'
%endif

Name:		dudf
Summary:	Mandriva implementation of DUDF as part of the Mancoosi European Project
Version:	0.15
Release:	6
Group:		System/Base
License:	GPLv2+
URL:		http://www.mancoosi.org

Source0:	%{name}-%{version}.tar.xz
BuildRequires:	swig
BuildRequires:	perl-devel
BuildRequires:	jsoncpp-devel >= 0.5.0-11
BuildRequires:	pkgconfig(libxml-2.0)
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

%build
export LDFLAGS="%{ldflags}"
%define	_disable_ld_no_undefined 1
export PERL_LDFLAGS="%{ldflags}"
%make CXXFLAGS="%{optflags}"

# %check
# make test

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


%changelog
* Tue Apr 26 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.15-3
+ Revision: 659398
- drop dependency filtering now that libjsoncpp has a proper soname
- rebuild against new libjsoncpp with SONAME

* Sun Apr 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.15-2
+ Revision: 658150
- add cppunit-devel to buildrequires so that test suite may build
- add %%check section
- update license tag
- filter out dependency on devel(libjsoncpp) for -devel package

* Sat Apr 23 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.15-1
+ Revision: 657379
- new version:
  	o fix remaining memleaks
  	o fix problem with parsing of dependency flags

* Fri Apr 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.14-1
+ Revision: 656743
- new version:
  	o fix some linking issues

* Fri Apr 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.13-1
+ Revision: 656716
- new version:
  	o use libossp-uuid rather than libuuid
- rebuild against new perl
- remove some obsolete rpm stuff

* Sat Feb 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.12-1
+ Revision: 636296
- add missing buildrequires
- update to latest code
- cleanup package
- bump major
- add -devel package

* Fri Jul 30 2010 Stéphane Laurière <slauriere@mandriva.com> 0.11-1mdv2011.0
+ Revision: 563738
- updated libopenssl-devel buildrequires
- v0.1 release

