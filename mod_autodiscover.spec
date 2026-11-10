Name:           mod_autodiscover
Version:        1.0.0
Release:        %autorelease
Summary:        Apache HTTPD input filter for parsing an Autodiscover request
License:        Apache-2.0
URL:            https://github.com/minfrin/%{name}
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  httpd-devel >= 2.4.0
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel

# Tie the module directly to the host's specific Apache binary ABI
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       httpd >= 2.4.0

%description
The Apache mod_autodiscover module allows parsing of a Microsoft Autodiscover
POST request.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog
%{_httpd_moddir}/mod_autodiscover.so

%changelog
%autochangelog
