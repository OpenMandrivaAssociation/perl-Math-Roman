%define module	Math-Roman
%define name	perl-%{module}
%define version 1.07
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Arbitrary sized Roman numbers and conversion from and to Arabic
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp.perl.org/pub/CPAN/modules/by-module/Math/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Well, it seems I have been infected by the Perligata-Virus, too. ;o)

This module lets you calculate with Roman numbers, as if they were big
integers. The numbers can have arbitrary length and all the usual functions
from Math::BigInt are available.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README INSTALL SIGNATURE
%{perl_vendorlib}/Math
%{_mandir}/*/*

