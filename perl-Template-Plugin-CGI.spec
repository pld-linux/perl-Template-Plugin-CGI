#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Template
%define	pnam	Plugin-CGI
Summary:	Template::Plugin::CGI - interface to CGI.pm module
Summary(pl.UTF-8):	Template::Plugin::CGI - Interfejs do modułu CGI.pm
Name:		perl-Template-Plugin-CGI
Version:	3.101
Release:	1
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	97e4eea444df76ec6ba7b4fb3f2c6ba1
URL:		https://metacpan.org/dist/Template-Plugin-Autoformat
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-CGI >= 4.44
BuildRequires:	perl-Template-Toolkit >= 3.100
BuildRequires:	perl-Test-CPAN-Meta
#BuildRequires:	perl-Test2-Tools-Explain
%endif
Requires:	perl-CGI >= 4.44
Requires:	perl-Template-Toolkit >= 3.100
Provides:	perl-Template-Toolkit-Plugin-CGI = %{version}
Obsoletes:	perl-Template-Toolkit-Plugin-CGI < 3.100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple Template Toolkit Plugin interface to the CGI
module.

%description -l pl.UTF-8
Bardzo prosty interfejs wtyczki Template Toolkitu do modułu CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%{perl_vendorlib}/Template/Plugin/CGI.pm
%{_mandir}/man3/Template::Plugin::CGI.3pm*
