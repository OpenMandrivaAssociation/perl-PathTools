%define	modname	PathTools
%define modver	3.33

Summary:	Tools for working with paths and file specs across platforms
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{modname}-%{modver}.tar.gz
Patch0:		PathTools-3.33-no-crappy-OSes.patch
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::CBuilder)

%description
Tools for working with paths and file specs across platforms.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches
rm -f lib/File/Spec/Cygwin.pm \
      lib/File/Spec/Epoc.pm \
      lib/File/Spec/Mac.pm \
      lib/File/Spec/OS2.pm \
      lib/File/Spec/VMS.pm \
      lib/File/Spec/Win32.pm
sed -i -e '/Cygwin.pm/d;/Epoc.pm/d;/Mac.pm/d;/OS2.pm/d;/VMS.pm/d;/Win32.pm/d' MANIFEST

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorarch}/File
%{perl_vendorarch}/Cwd.pm
%{perl_vendorarch}/auto/Cwd
%{_mandir}/man3/*

