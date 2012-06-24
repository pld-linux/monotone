# NOTE:
# - bundled sqlite has local modifications to support large db
# - bundled lua is stripped, it doesn't contain some features
#   that create security holes in monotone enviroment
Summary:	A free distributed version control system
Summary(pl):	Wolnodost�pny rozproszony system kontroli wersji
Name:		monotone
Version:	0.27
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.venge.net/monotone/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	cf3d8f26b7570d0d65834c3949913e2d
URL:		http://www.venge.net/monotone/
BuildRequires:	boost-date_time-devel
BuildRequires:	boost-devel >= 1.32.0-3
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-mem_fn-devel
BuildRequires:	boost-ref-devel
BuildRequires:	boost-regex-devel
BuildRequires:	boost-test-devel
BuildRequires:	libidn-devel
BuildRequires:	popt-devel
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
monotone to wolnodost�pny, rozproszony system kontroli wersji.
Dostarcza proste, jednoplikowe, transakcyjne przechowywanie wersji, z
w pe�ni bezpo��czeniow� prac� i wydajnym protoko�em synchronizacji
peer-to-peer. Obs�uguje ��czenie z uwzgl�dnieniem historii, lekkie
odga��zienia, zintegrowany podgl�d kodu i testowanie przez osoby
trzecie. U�ywa kryptograficznego nazywania wersji i certyfikat�w RSA
po stronie klienta. Ma dobre umi�dzynarodowienie, nie ma zewn�trznych
zale�no�ci, dzia�a na Linuksie, Solarisie, MacOS-ie X oraz Windows i
jest licencjonowany na GNU GPL.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/lua50"; export CPPFLAGS
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}/monotone.html \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS ChangeLog UPGRADE monotone.html
%attr(755,root,root) %{_bindir}/*
%{_infodir}/monotone*
%{_mandir}/man?/*
