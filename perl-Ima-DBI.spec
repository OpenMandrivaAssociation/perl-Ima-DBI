%define module	Ima-DBI
%define upstream_version 0.35

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Summary:	Database connection caching and organization
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{module}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBIx::ContextualFetch)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
Ima::DBI attempts to organize and facilitate caching and more efficient use of
database connections and statement handles by storing DBI and SQL information
with your class (instead of as separate objects). This allows you to pass
around just one object without worrying about a trail of DBI handles behind it.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Ima
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.35-2mdv2010.0
+ Revision: 430468
- rebuild

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.0
+ Revision: 271775
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.34-7mdv2009.0
+ Revision: 241484
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-5mdv2008.0
+ Revision: 86474
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-4mdv2007.0
- Rebuild

* Wed Dec 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.34-3mdk
- Add BuildRequires

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-2mdk
- fix buildrequires

* Mon Dec 05 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdk
- first mdk release

