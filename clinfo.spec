%global gitcommit 7f44937169b1d7d0fb446cc0b1878cf0c09017f1

Summary: Enumerate OpenCL platforms and devices
Name:    clinfo
Version: 0.1
Release: 0.1%{?dist}
License: Public Domain
Group:   System Environment/Libraries
URL:     https://github.com/Oblomov/clinfo

%global tarball %{name}-20131001git%{gitcommit}.tar.gz
Source0: https://github.com/Oblomov/%{name}/archive/%{gitcommit}.tar.gz#/%{tarball}

BuildRequires: pkgconfig automake autoconf libtool
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
%setup -q -n %{name}-%{gitcommit}

# Hack:
# Create a dummy configure so we can later run configure
# which also sets C and LDFLAGS which are needed at build-time
touch configure ; chmod a+x configure


%build
# Hack:
# Run confiure to set env CFLAGS and LDFLAGS
%configure
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} clinfo %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_mandir}/man1
%{__cp} man/clinfo.1 %{buildroot}/%{_mandir}/man1/


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc README LICENSE
%{_bindir}/clinfo
%{_mandir}/man1/clinfo.1.gz

%changelog
* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.1
- Initial package
