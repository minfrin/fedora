Name:           mod_contact
Version:        1.0.1
Release:        %autorelease
Summary:        Apache HTTPD contact MIME filter module
License:        Apache-2.0
URL:            https://github.com/minfrin/%{name}
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  httpd-devel >= 2.4.0
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  mod_multipart-devel

# Tie the module directly to the host's specific Apache binary ABI
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       httpd >= 2.4.0

%description
Apache httpd module that implements a contact us form with file upload.
Acts as a gateway between a form submission and email.

%package devel
Summary:        Development tools for the mod_contact filters
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       httpd-devel >= 2.4.0

%description devel
Header files for mod_contact filters implementing contact MIME parsing.

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
%{_httpd_moddir}/mod_contact.so

%files devel
%{_includedir}/httpd/mod_contact.h

%changelog
%autochangelog
