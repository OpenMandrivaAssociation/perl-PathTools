%define	module	PathTools
%define	name	perl-%{module}
%define version 3.29
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Tools for working with paths and file specs across platforms
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Tools for working with paths and file specs across platforms.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/File
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/auto/Cwd
%{_mandir}/man3/*

