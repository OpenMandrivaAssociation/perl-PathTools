%define	upstream_name	 PathTools
%define upstream_version 3.33

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

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
%__perl Makefile.PL INSTALLDIRS=vendor
make CFLAGS="%{optflags}"

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


%changelog
* Fri Jul 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 3.330.0-3
+ Revision: 810455
- Remove support for non-POSIX OSes and its dependencies

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.330.0-2
+ Revision: 766183
- rebuilt for perl-5.14.2

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.330.0-1mdv2011.0
+ Revision: 595981
- update to new version 3.33

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 3.310.0-3mdv2011.0
+ Revision: 566439
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.310.0-2mdv2011.0
+ Revision: 556070
- rebuild for perl 5.12

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 3.310.0-1mdv2010.1
+ Revision: 461777
- update to 3.31

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 3.300.0-2mdv2010.0
+ Revision: 408699
- force rebuild

* Mon May 25 2009 Jérôme Quelin <jquelin@mandriva.org> 3.300.0-1mdv2010.0
+ Revision: 379596
- using new %%perl_convert_version macro

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 3.30-1mdv2010.0
+ Revision: 374417
- update to new version 3.30

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.29-1mdv2009.1
+ Revision: 300672
- nouvelle version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 3.27-4mdv2009.0
+ Revision: 258194
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.27-3mdv2009.0
+ Revision: 246274
- rebuild

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.27-1mdv2008.1
+ Revision: 156180
- update to new version 3.27
- update to new version 3.27

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 3.25-2mdv2008.1
+ Revision: 152231
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.25-1mdv2008.0
+ Revision: 48706
- import perl-PathTools

