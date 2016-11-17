Name: libnes
Version: 1.1.4
Release: 2%{?dist}.0
Summary: NetEffect RNIC Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/nes/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel > 1.1.4
%ifnarch ia64
BuildRequires: valgrind-devel
%endif
ExclusiveArch: %{ix86} x86_64 ia64 ppc ppc64 %{arm}
Provides: libibverbs-driver.%{_arch}
Obsoletes: %{name}-devel
%description
Userspace hardware driver for use with the libibverbs InfiniBand/iWARP verbs
library.  This driver enables NetEffect iWARP capable ethernet devices.

%package static
Summary: Static version of the libnes driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libnes that may be linked directly to an application.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ifnarch ia64
%configure --with-valgrind
%else
%configure
%endif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%doc AUTHORS COPYING

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Thu Aug 27 2015 Jacco Ligthart <jacco@redsleeve.org> - 1.1.4-2.0
- Add ARM architectures

* Wed Mar 11 2015 Doug Ledford <dledford@redhat.com> - 1.1.4-2
- Bump and rebuild against updated valgrind-devel
- Resolves: bz1142165

* Wed Jun 18 2014 Doug Ledford <dledford@redhat.com> - 1.1.4-1
- Update to latest upstream and build against new libibverbs
- Related: bz854655

* Mon Jan 23 2012 Doug Ledford <dledford@redhat.com> - 1.1.3-1
- Update to latest upstream release
- Rebuild against latest libibverbs (native FDR/IBoE enabled)
- Related: bz750609

* Mon Jul 25 2011 Doug Ledford <dledford@redhat.com> - 1.1.1-2
- Rebuild against latest libibverbs
- Add psuedo provide of libibverbs-driver.%%{_arch}
- Fix exclusivearch to work on i686
- Related: bz725016, bz724900

* Mon Jan 17 2011 Doug Ledford <dledford@redhat.com> - 1.1.1-1.el6
- Update to latest upstream release
- Related: bz664801

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 0.9.0-2.el6
- Correct license tag
- Related: bz543948

* Mon Dec 21 2009 Doug Ledford <dledford@redhat.com> - 0.9.0-1.el5
- Update to latest upstream source
- Build against new libibverbs API
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 0.6-2.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 0.6-1.el5
- Build against non-XRC libibverbs
- Update to ofed 1.4.1 final bits
- Remove no longer needed memleak patch
- Related: bz506258, bz506097

* Fri Apr 17 2009 Doug Ledford <dledford@redhat.com> - 0.5-5.el5
- Fix a minor memleak (from upstream)
- Rebuild against libibverbs that has xrc support
- Related: bz459652

* Thu Sep 18 2008 Doug Ledford <dledford@redhat.com> - 0.5-4
- Add a build flag to silence some compile warnings

* Tue Sep 16 2008 Doug Ledford <dledford@redhat.com> - 0.5-3
- Upstream has updated the libnes tarball without changing the version.  Pick
  up the libnes-0.5.tar.gz tarball that's dated 13-Jun-2008
- Resolves: bz451470

* Thu Feb 14 2008 Doug Ledford <dledford@redhat.com> - 0.5-2
- Obsolete the old -devel package
- Related: bz432765

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 0.5-1
- Initial driver import
- Related: bz428197

