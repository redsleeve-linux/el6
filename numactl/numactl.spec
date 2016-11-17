Name:		numactl
Summary:	Library for tuning for Non Uniform Memory Access machines
Version:	2.0.9
Release:	2%{?dist}.0
License:	LGPLv2/GPLv2
Group: 		System Environment/Base
URL:		ftp://oss.sgi.com/www/projects/libnuma/download
Source0:	ftp://oss.sgi.com/www/projects/libnuma/download/numactl-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-buildroot

Patch0: numactl-2.0.9-distance-parsing.patch
Patch1: numactl-2.0.9-nodes_allowed_list.patch
Patch2: numactl-2.0.9-localalloc-man-option.patch
Patch10001: numactl-2.0.9-arm_migrate_pages.patch

ExcludeArch: s390 s390x

%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy and a libnuma to do
allocations with NUMA policy in applications.

%package devel
Summary: Development package for building Applications that use numa
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Provides development headers for numa library calls

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10001 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -I."

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8

make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/%{_libdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libnuma.so.1
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/memhog
%{_bindir}/migspeed
%{_bindir}/migratepages
%{_mandir}/man8/*.8*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*.3*

%changelog
* Fri Aug 28 2015 Jacco Ligthart <jacco@redsleeve.org> - 2.0.9-2.0
- add patch for __NR_migrate_pages on arm, see:
- https://wiki.linaro.org/LEG/Engineering/Kernel/NUMA

* Thu May 22 2014 Petr Holasek <pholasek@redhat.com> - 2.0.9-2
- Respin due to regression caused by rebase (bz1100134)

* Wed May 21 2014 Petr Holasek <pholasek@redhat.com> - 2.0.9-1
- Rebase to the 2.0.9 release (bz1017048)

* Mon Aug 19 2013 Petr Holasek <pholasek@redhat.com> - 2.0.7-8
- localalloc description (bz881779)

* Wed Aug 14 2013 Anton Arapov <anton@redhat.com> - 2.0.7-7
- numastat.c: fix bug preventing correct static huge page quantities
- numastat.c: update version number
- numastat.8: remove redundant "interleave hit" description
- numastat.8: remove extraneous leading spaces and blank lines
- numastat.8: enhance explanation of correct placement for "-s" option
- Resolves: rhbz#987507

* Tue Oct 16 2012 Petr Holasek <pholasek@redhat.com> - 2.0.7-6
- Added new rewritten numastat utility (bz829896)

* Fri Oct 5 2012 Petr Holasek <pholasek@redhat.com> - 2.0.7-5
- Fixed %{?dist} in spec file (bz805965), it caused test fails

* Thu Oct 4 2012 Petr Holasek <pholasek@redhat.com> - 2.0.7-4
- Symbol numa_num_possible_cpus exported (bz804827)
- miscalculating of numa_num_configured_cpus was fixed (bz804480)

* Thu Mar 22 2012 Anton Arapov <anton@rehdat.com> - 2.0.7-3
- Bring back the legacy export to prevent the ABI change.

* Wed Feb 15 2012 Petr Holasek <pholasek@redhat.com> - 2.0.7-1
- Rebase to 2.0.7
- Fixes for numademo segfaults (bz 784501, bz 707138)

* Mon Jan 02 2012 Anton Arapov <aarapov@redhat.com> - 2.0.3-10
- Add missing manpages (bz 751764)

* Thu Jun 17 2010 Neil Horman <nhorman@redhat.com> - 2.0.3-9
- Fix dist tag (bz 604556)

* Thu Apr 29 2010 Neil Horman <nhorman@redhat.com> - 2.0.3-7.1
- fixed nodes_allowed.patch (bz 587211)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.3-7.1
- Rebuilt for RHEL 6

* Mon Aug 10 2009 Neil Horman <nhorman@redhat.com> - 2.0.3-7
- Add destructor to libnuma.so to free allocated memory (bz 516227)

* Mon Aug 10 2009 Neil Horman <nhorman@redhat.com> - 2.0.3-6
- Fix obo in nodes_allowed_list strncpy (bz 516223)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Neil Horman <nhorman@redhat.com>
- Update to full 2.0.3 version (bz 506795)

* Wed Jun 17 2009 Neil Horman <nhorman@redhat.com>
- Fix silly libnuma warnings again (bz 499633)

* Fri May 08 2009 Neil Horman <nhorman@redhat.com>
- Update to 2.0.3-rc3 (bz 499633)

* Wed Mar 25 2009 Mark McLoughlin <markmc@redhat.com> - 2.0.2-4
- Remove warning from libnuma (bz 484552)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 29 2008 Neil Horman <nhorman@redhat.com> - 2.0.2-2
- Fix build break due to register selection in asm

* Mon Sep 29 2008 Neil Horman <nhorman@redhat.com> - 2.0.2-1
- Update rawhide to version 2.0.2 of numactl

* Fri Apr 25 2008 Neil Horman <nhorman@redhat.com> - 1.0.2-6
- Fix buffer size passing and arg sanity check for physcpubind (bz 442521)

* Fri Mar 14 2008 Neil Horman <nhorman@redhat.com> - 1.0.2-5
- Fixing spec file to actually apply alpha patch :)

* Fri Mar 14 2008 Neil Horman <nhorman@redhat.com> - 1.0.2-4
- Add alpha syscalls (bz 396361)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-3
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Neil Horman <nhorman@redhat.com> - 1.0.2-1
- Update numactl to fix get_mempolicy signature (bz 418551)

* Fri Dec 14 2007 Neil Horman <nhorman@redhat.com> - 1.0.2-1
- Update numactl to latest version (bz 425281)

* Tue Aug 07 2007 Neil Horman <nhorman@redhat.com> - 0.9.8-4
- Fixing some remaining merge review issues (bz 226207)

* Fri Aug 03 2007 Neil Horman <nhorman@redhat.com> - 0.9.8-3
- fixing up merge review (bz 226207)

* Fri Jan 12 2007 Neil Horman <nhorman@redhat.com> - 0.9.8-2
- Properly fixed bz 221982
- Updated revision string to include %{dist}

* Thu Jan 11 2007 Neil Horman <nhorman@redhat.com> - 0.9.8-1.38
- Fixed -devel to depend on base package so libnuma.so resolves

* Thu Sep 21 2006 Neil Horman <nhorman@redhat.com> - 0.9.8-1.36
- adding nodebind patch for bz 207404

* Fri Aug 25 2006 Neil Horman <nhorman@redhat.com> - 0.9.8-1.35
- moving over libnuma.so to -devel package as well

* Fri Aug 25 2006 Neil Horman <nhorman@redhat.com> - 0.9.8-1.34
- split out headers/devel man pages to a devel subpackage

* Tue Aug 15 2006 Neil Horman <nhorman@redhat.com> - 0.9.8-1.32
- add patch for broken cpu/nodebind output (bz 201906)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8-1.31
- rebuild

* Tue Jun 13 2006 Neil Horman <nhorman@redhat.com>
- Rebased numactl to version 0.9.8 for FC6/RHEL5

* Wed Apr 26 2006 Neil Horman <nhorman@redhat.com>
- Added patches for 64 bit overflows and cpu mask problem

* Fri Mar 10 2006 Bill Nottingham <notting@redhat.com>
- rebuild for ppc TLS issue (#184446)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.6.4-1.25.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Jul  7 2005 Dave Jones <davej@redhat.com>
- numactl doesn't own the manpage dirs. (#161547)

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- rebuild with -D_FORTIFY_SOURCE=2

* Wed Nov 10 2004 David Woodhouse <dwmw2@redhat.com>
- Fix build on x86_64

* Thu Oct 21 2004 David Woodhouse <dwmw2@redhat.com>
- Add PPC support

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jun 05 2004 Warren Togami <wtogami@redhat.com> 
- spec cleanup

* Sat Jun 05 2004 Arjan van de Ven <arjanv@redhat.com>
- initial packaging

