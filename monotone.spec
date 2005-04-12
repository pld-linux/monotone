Summary:	A free distributed version control system
Summary(pl):	Wolnodostêpny rozproszony system kontroli wersji
Name:		monotone
Version:	0.18
Release:	2
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.venge.net/monotone/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	16a8f0cce9d219311d75e2b913d0fabc
URL:		http://www.venge.net/monotone/
BuildRequires:	boost-date_time-devel
BuildRequires:	boost-devel >= 1.32.0-3
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	boost-ref-devel
BuildRequires:	boost-test-devel
BuildRequires:	libidn-devel
BuildRequires:	lua50-devel
BuildRequires:	popt-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monotone is a free distributed version control system. It provides a
simple, single-file transactional version store, with fully
disconnected operation and an efficient peer-to-peer synchronization
protocol. It understands history-sensitive merging, lightweight
branches, integrated code review and 3rd party testing. It uses
cryptographic version naming and client-side RSA certificates. It has
good internationalization support, has no external dependencies, runs
on Linux, Solaris, MacOS X, and Windows, and is licensed under the GNU
GPL.

%description -l pl
monotone to wolnodostêpny, rozproszony system kontroli wersji.
Dostarcza proste, jednoplikowe, transakcyjne przechowywanie wersji, z
w pe³ni bezpo³±czeniow± prac± i wydajnym protoko³em synchronizacji
peer-to-peer. Obs³uguje ³±czenie z uwzglêdnieniem historii, lekkie
odga³êzienia, zintegrowany podgl±d kodu i testowanie przez osoby
trzecie. U¿ywa kryptograficznego nazywania wersji i certyfikatów RSA
po stronie klienta. Ma dobre umiêdzynarodowienie, nie ma zewnêtrznych
zale¿no¶ci, dzia³a na Linuksie, Solarisie, MacOS-ie X oraz Windows i
jest licencjonowany na GNU GPL.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/lua50"; export CPPFLAGS
%configure \
	--without-bundled-sqlite \
	--without-bundled-lua
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_infodir}/monotone*
%{_mandir}/man?/*
