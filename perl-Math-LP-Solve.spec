#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	LP-Solve
Summary:	Math::LP::Solve - Perl wrapper for the lp_solve linear program solver
Summary(pl.UTF-8):	Math::LP::Solve - interfejs perlowy do biblioteki lp_solve, rozwiązującej problemy liniowe
Name:		perl-Math-LP-Solve
Version:	3.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	358c56ca0d40a300cb5fd132c90fbd3e
Patch0:		%{name}-system-lpk.patch
Patch1:		%{name}-perl5.8.patch
URL:		http://search.cpan.org/dist/Math-LP-Solve/
# not ready for lp_solve 4.0
BuildRequires:	lp_solve3-devel >= 3.2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::LP::Solve is a wrapper around the freeware lp_solve library,
which solves linear and mixed linear/integer programs. Most functions
and data structures in the file lpkit.h of the lp_solve distribution
are made available in the Math::LP::Solve namespace.

%description -l pl.UTF-8
Math::LP::Solve to interfejs do darmowej biblioteki lp_solve,
rozwiązującej problemy programowania liniowego i mieszane liniowo-
całkowitoliczbowe. Większość funkcji i struktur danych z pliku lpkit.h
jest dostępna w przestrzeni nazw Math::LP::Solve.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Math/LP
%dir %{perl_vendorarch}/Math/LP/Solve.pm
%dir %{perl_vendorarch}/auto/Math/LP
%dir %{perl_vendorarch}/auto/Math/LP/Solve
%attr(755,root,root) %{perl_vendorarch}/auto/Math/LP/Solve/Solve.so
%{_mandir}/man3/*
