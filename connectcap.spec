# RPM Spec file for connectcap

Name:      connectcap
Version:   1.0.0
Release:   %autorelease
Summary:   Https connect proxy that captures outgoing network traffic
License:   Apache-2.0

URL:       https://github.com/minfrin/%{name}
Source0:   %{URL}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires: clang
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: systemd
BuildRequires: pkgconfig(apr-1)
BuildRequires: pkgconfig(apr-util-1)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libpcap)

%description
The connectcap daemon is an https CONNECT proxy that records all outgoing
connections for further analysis. Use this to debug connecion issues where
the people doing the troubleshooting and the place where the trouble is
occurring are not the same place.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%pre
getent group connectcap >/dev/null || groupadd -r connectcap

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/connectcap
%{_mandir}/man1/connectcap.1*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ccpasswd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(2750,root,connectcap) %{_localstatedir}/spool/%{name}
%{_unitdir}/%{name}.service

%doc AUTHORS ChangeLog
%license COPYING

%changelog
%autochangelog

