#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	LP-Solve
Summary:	Math::LP::Solve - perl wrapper for the lp_solve linear program solver
Summary(pl):	Math::LP::Solve - interfejs do biblioteki lp_solve, rozwi±zuj±cej problemy liniowe
Name:		perl-Math-LP-Solve
Version:	3.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-system-lpk.patch
# not ready for lp_solve 4.0
BuildRequires:	lp_solve-devel = 3.2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::LP::Solve is a wrapper around the freeware lp_solve library,
which solves linear and mixed linear/integer programs. Most functions
and data structures in the file lpkit.h of the lp_solve distribution
are made available in the Math::LP::Solve namespace.

%description -l pl
Math::LP::Solve to interfejs do darmowej biblioteki lp_solve,
rozwi±zuj±cej problemy programowania liniowego i mieszane liniowo-
ca³kowitoliczbowe. Wiêkszo¶æ funkcji i struktur danych z pliku lpkit.h
jest dostêpna w przestrzeni nazw Math::LP::Solve.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/Math/LP
%dir %{perl_sitearch}/Math/LP/Solve.pm
%dir %{perl_sitearch}/auto/Math/LP
%dir %{perl_sitearch}/auto/Math/LP/Solve
%{perl_sitearch}/auto/Math/LP/Solve/Solve.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/LP/Solve/Solve.so
%{_mandir}/man3/*
