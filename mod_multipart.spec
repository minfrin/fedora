Name:           mod_multipart
Version:        2.4.0
Release:        %autorelease
Summary:        Apache HTTPD multipart MIME filter module
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
The Apache mod_multipart module provides a set of filters that
can parse and interpret multipart MIME content.

%package devel
Summary:        Development tools for the mod_multipart filters
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       httpd-devel >= 2.4.0

%description devel
Header files for mod_multipart filters implementing multipart MIME parsing.

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
%{_httpd_moddir}/mod_multipart.so

%files devel
%{_includedir}/httpd/mod_multipart.h

%changelog
%autochangelog
