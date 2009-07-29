%define upstream_name	 Math-Roman
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Arbitrary sized Roman numbers and conversion from and to Arabic
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Well, it seems I have been infected by the Perligata-Virus, too. ;o)

This module lets you calculate with Roman numbers, as if they were big
integers. The numbers can have arbitrary length and all the usual functions
from Math::BigInt are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
