Name:           mod_ical
Version:        1.0.0
Release:        %autorelease
Summary:        iCalendar/jCal/xCal filter for Apache httpd
License:        Apache-2.0
URL:            https://github.com/minfrin/%{name}
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  httpd-devel >= 2.4.0
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libxml-2.0)

# Tie the module directly to the host's specific Apache binary ABI
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       httpd >= 2.4.0

%description
iCalendar/jCal/xCal filter for Apache httpd. Allows iCal data to be
filtered and made available to client side web clients in iCal, xCal and
jCal formats.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_httpd_moddir}/mod_ical.so

%changelog
%autochangelog
