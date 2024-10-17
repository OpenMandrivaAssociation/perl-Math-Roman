%define upstream_name	 Math-Roman
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Arbitrary sized Roman numbers and conversion from and to Arabic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Well, it seems I have been infected by the Perligata-Virus, too. ;o)

This module lets you calculate with Roman numbers, as if they were big
integers. The numbers can have arbitrary length and all the usual functions
from Math::BigInt are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README INSTALL SIGNATURE
%{perl_vendorlib}/Math
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 403856
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.07-6mdv2009.0
+ Revision: 241725
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-4mdv2008.0
+ Revision: 86634
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-3mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.07-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdk
- first mdk release

