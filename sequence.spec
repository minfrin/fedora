# RPM Spec file for sequence

Name:      sequence
Version:   1.2.0
Release:   %autorelease
Summary:   Run all executables in a directory in sequence
License:   Apache-2.0

URL:       https://github.com/minfrin/%{name}
Source0:   %{URL}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires: clang
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
The sequence command runs all the executables in a specified directory,
running each one in sequence ordered alphabetically.

Each executable is named sensibly so it is clear which executable is
responsible for output in logfiles.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/sequence
%{_mandir}/man1/sequence.1*

%doc AUTHORS ChangeLog README
%license COPYING

%changelog
%autochangelog

