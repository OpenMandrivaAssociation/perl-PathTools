%define	upstream_name	 PathTools
%define upstream_version 3.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Tools for working with paths and file specs across platforms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::CBuilder)

Patch0:		PathTools-3.33-no-crappy-OSes.patch

%description
Tools for working with paths and file specs across platforms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .noCrappyOS~
rm -f lib/File/Spec/Cygwin.pm \
      lib/File/Spec/Epoc.pm \
      lib/File/Spec/Mac.pm \
      lib/File/Spec/OS2.pm \
      lib/File/Spec/VMS.pm \
      lib/File/Spec/Win32.pm
sed -i -e '/Cygwin.pm/d;/Epoc.pm/d;/Mac.pm/d;/OS2.pm/d;/VMS.pm/d;/Win32.pm/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorarch}/File
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/auto/Cwd
%{_mandir}/man3/*
