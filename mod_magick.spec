Name:           mod_magick
Version:        1.0.1
Release:        %autorelease
Summary:        Apache HTTPD image filtering
License:        Apache-2.0
URL:            https://github.com/minfrin/%{name}
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  httpd-devel >= 2.4.0
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(GraphicsMagick)

# Tie the module directly to the host's specific Apache binary ABI
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       httpd >= 2.4.0

%description
The Apache mod_magick filter provides image filtering for requests.

%package devel
Summary:        Development tools for the mod_magick filters
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       httpd-devel >= 2.4.0

%description devel
Header file for the mod_magick filter and magick bucket used to
manipulate image requests.

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
%{_httpd_moddir}/mod_magick*.so

%files devel
%{_includedir}/httpd/mod_magick.h

%changelog
%autochangelog
