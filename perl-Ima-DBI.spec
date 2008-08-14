%define module	Ima-DBI
%define name	perl-%{module}
%define version 0.35
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Database connection caching and organization
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/%{module}-%{version}.tar.gz
Buildrequires:	perl-DBIx-ContextualFetch
Buildrequires:	perl-Class-Data-Inheritable
Buildrequires:  perl-DBI
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Ima::DBI attempts to organize and facilitate caching and more efficient use of
database connections and statement handles by storing DBI and SQL information
with your class (instead of as separate objects). This allows you to pass
around just one object without worrying about a trail of DBI handles behind it.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Ima
%{_mandir}/*/*

