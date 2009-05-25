%define	upstream_name	 PathTools
%define upstream_version 3.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Tools for working with paths and file specs across platforms
URL:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRoot:	%{_tmppath}/%{upstream_name}-%{upstream_version}

%description
Tools for working with paths and file specs across platforms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

