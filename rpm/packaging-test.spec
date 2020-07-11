Name:           packaging-test
Version:        0.2
Release:        1%{?dist}
Summary:        Packaging Test package

License:        GPLv3
URL:            https://gitlab.nic.cz/knot/packaging-test
Source0:        https://gitlab.labs.nic.cz/knot/packaging-test/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        demo-libuv.service

BuildRequires:  gcc
BuildRequires:  libuv-devel

Requires:       libuv

%description
This is a testing package to prove my mad packaging skills.

It contains demo_libuv binary and demo-libuv oneshot systemd service.


%prep
%setup -qn %{name}-v%{version}

%build
gcc -g -luv demo_libuv.c -o demo_libuv

%install
install -p -D -m 0755 demo_libuv %{buildroot}%{_bindir}/demo_libuv
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/demo-libuv.service

%post
%systemd_post demo-libuv.service

%preun
%systemd_preun demo-libuv.service


%files
%license LICENSE
%{_bindir}/demo_libuv
%{_unitdir}/demo-libuv.service


%changelog
* Sat Jul 11 2020 Jakub Ružička <voice@texnoforge.dev> - 0.2-1
- Initial Release
