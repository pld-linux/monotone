Summary:	A free distributed version control system
Name:		monotone
Version:	0.13
Release:	1
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.venge.net/monotone/%{name}-%{version}.tar.gz
# Source0-md5:	19a9cc07058aba5ab41e0d3264d2a601
URL:		http://www.venge.net/monotone/
BuildRequires:	boost-devel
BuildRequires:	boost-test-devel
BuildRequires:	lua-devel
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
monotone is a free distributed version control system. it provides a
simple, single-file transactional version store, with fully
disconnected operation and an efficient peer-to-peer synchronization
protocol. it understands history-sensitive merging, lightweight
branches, integrated code review and 3rd party testing. it uses
cryptographic version naming and client-side RSA certificates. it has
good internationalization support, has no external dependencies, runs
on linux, solaris, OSX, and windows, and is licensed under the GNU
GPL.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html ps texi
%attr(755,root,root) %{_bindir}/*
