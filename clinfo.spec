%global commit 7f44937169b1d7d0fb446cc0b1878cf0c09017f1
%global commitdate 20130930
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitversion .git%{commitdate}.%{shortcommit}

Summary: Enumerate OpenCL platforms and devices
Name:    clinfo
Version: 0.1
Release: 0.1%{?gitversion}%{?dist}
License: Public Domain
Group:   System Environment/Libraries
URL:     https://github.com/Oblomov/clinfo

%global tarball %{name}-%{gitversion}.tar.gz
Source0: https://github.com/Oblomov/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: opencl-headers ocl-icd-devel

Requires: opencl-filesystem


%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).


%prep
%setup -q -n %{name}-%{commit}


%build
# configure doesn't exist, but we need the exported CFLAGS and friends
%configure || :
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m0755 clinfo %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_mandir}/man1
%{__cp} -a man/clinfo.1 %{buildroot}/%{_mandir}/man1/


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README LICENSE
%{_bindir}/clinfo
%{_mandir}/man1/clinfo.1.gz

%changelog
* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.1
- Initial package
