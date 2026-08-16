# NOTE:
# - lua 5.1 is not a leftover: monotone uses lua_strlen and LUA_QL, both gone
#   in 5.2
# TODO:
# - subpackage with init-scripts
# - database format is changing - migrate and regenerate options has to be run.
Summary:	A free distributed version control system
Summary(pl.UTF-8):	Wolnodostępny rozproszony system kontroli wersji
Name:		monotone
Version:	1.1
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	df3f40ca22120aa142ac9becba9e1bf7
Patch0:		%{name}-botan2.patch
Patch1:		%{name}-boost-e-macro.patch
Patch2:		%{name}-pcre.patch
URL:		http://www.monotone.ca/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	botan2-devel
BuildRequires:	libidn-devel
BuildRequires:	lua51-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
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

%description -l pl.UTF-8
monotone to wolnodostępny, rozproszony system kontroli wersji.
Dostarcza proste, jednoplikowe, transakcyjne przechowywanie wersji, z
w pełni bezpołączeniową pracą i wydajnym protokołem synchronizacji
peer-to-peer. Obsługuje łączenie z uwzględnieniem historii, lekkie
odgałęzienia, zintegrowany podgląd kodu i testowanie przez osoby
trzecie. Używa kryptograficznego nazywania wersji i certyfikatów RSA
po stronie klienta. Ma dobre umiędzynarodowienie, nie ma zewnętrznych
zależności, działa na Linuksie, Solarisie, MacOS-ie X oraz Windows i
jest licencjonowany na GNU GPL.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# avoid hiding the interpreter dependency behind env
%{__sed} -i -e '1s,#! */usr/bin/env bash,#!/bin/bash,' extra/mtn-hooks/monotone-mail-notify
%{__sed} -i -e '1s,#!/usr/bin/env perl,#!%{__perl},' extra/bin/mtn-cleanup

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	lua_CFLAGS="$(pkg-config --cflags lua51)" \
	lua_LIBS="$(pkg-config --libs lua51)" \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

# upstream drops these into an unversioned docdir; ship them as %%doc instead
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# python2 notifier for cia.vc, a service shut down in 2011, and the hook
# that calls it
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/monotone-ciabot.py
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/hooks/monotone-ciabot.lua

install -d $RPM_BUILD_ROOT%{bash_compdir}
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/monotone.bash_completion \
	$RPM_BUILD_ROOT%{bash_compdir}/mtn
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%{__rm} $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README UPGRADE contrib examples
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/hooks
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/monotone-mail-notify
%{bash_compdir}/mtn
%{_infodir}/monotone*
%{_mandir}/man1/mtn.1*
%{_mandir}/man1/mtn-cleanup.1*
%{_mandir}/man1/mtnopt.1*
