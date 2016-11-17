Summary:     The mdadm program controls Linux md devices (software RAID arrays)
Name:        mdadm
Version:     3.3.4
Release:     1%{?dist}.5
Source:      http://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-%{version}.tar.xz
Source1:     mdmonitor.init
Source2:     raid-check
Source3:     mdadm.rules
Source4:     mdadm-raid-check-sysconfig
Source5:     mdadm-cron
Patch1:      mdadm-3.3.4-imsm-don-t-call-abort_reshape-in-imsm_manage_reshape.patch
Patch2:      mdadm-3.3.4-Grow-close-file-descriptor-earlier-to-avoid-still-in.patch
Patch3:      mdadm-3.3.4-imsm-abort-reshape-if-sync_action-is-not-reshape.patch
Patch4:      mdadm-3.3.4-imsm-use-timeout-when-waiting-for-reshape-progress.patch
Patch5:      mdadm-3.3.4-imsm-don-t-update-migration-record-when-reshape-is-i.patch
Patch6:      mdadm-3.3.4-Grow-Add-documentation-to-abort_reshape-for-suspend_.patch
Patch7:      mdadm-3.3.4-super-intel-ensure-suspended-region-is-removed-when-.patch
Patch8:      mdadm-3.3.4-Grow-close-fd-earlier-to-avoid-cannot-get-excl-acces.patch
Patch9:      mdadm-3.3.4-Introduce-stat2kname-and-fd2kname.patch
Patch10:     mdadm-3.3.4-IMSM-retry-reading-sync_completed-during-reshape.patch
Patch11:     mdadm-3.3.4-The-sys_name-array-in-the-mdinfo-structure-is-20-byt.patch
Patch12:     mdadm-3.3.4-imsm-add-handling-of-sync_action-is-equal-to-idle.patch
Patch13:     mdadm-3.3.4-imsm-properly-handle-values-of-sync_completed.patch
Patch97:     mdadm-3.3.2-disable-ddf.patch
Patch98:     mdadm-3.3.2-udev.patch
Patch99:     mdadm-3.3-makefile.patch
# Patches not upstream yet
URL:         http://www.kernel.org/pub/linux/utils/raid/mdadm/
License:     GPLv2+
Group:       System Environment/Base
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes:   mdctl,raidtools
BuildRequires: binutils-devel
Requires(post): /sbin/service, /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service
Requires: udev

%description 
The mdadm program is used to create, manage, and monitor Linux MD (software
RAID) devices.  As such, it provides similar functionality to the raidtools
package.  However, mdadm is a single program, and it can perform
almost all functions without a configuration file, though a configuration
file can be used to help with some common tasks.

%prep
%setup -q
%patch1 -p1 -b .abort
%patch2 -p1 -b .grow-close
%patch3 -p1 -b .sync_action
%patch4 -p1 -b .timeout
%patch5 -p1 -b .bother
%patch6 -p1 -b .doc
%patch7 -p1 -b .suspended-region
%patch8 -p1 -b .early
%patch9 -p1 -b .stat2kname
%patch10 -p1 -b .retry
%patch11 -p1 -b .sysname
%patch12 -p1 -b .syncidle
%patch13 -p1 -b .synccomplete
%patch97 -p1 -b .ddf
%patch98 -p1 -b .udev
%patch99 -p1 -b .static

%build
make %{?_smp_mflags} CXFLAGS="$RPM_OPT_FLAGS" SYSCONFDIR="%{_sysconfdir}" mdadm mdmon

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} MANDIR=%{_mandir} BINDIR=/sbin install
rm -f %{buildroot}/lib/udev/rules.d/6[34]*
install -Dp -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/mdmonitor
install -Dp -m 755 %{SOURCE2} %{buildroot}%{_sbindir}/raid-check
install -Dp -m 644 %{SOURCE3} %{buildroot}/lib/udev/rules.d/65-md-incremental.rules
install -Dp -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/raid-check
install -Dp -m 600 %{SOURCE5} %{buildroot}%{_sysconfdir}/cron.d/raid-check
mkdir -p -m 700 %{buildroot}/var/run/mdadm

%clean
rm -rf %{buildroot}

%post
if [ "$1" = 1 ]; then
    /sbin/chkconfig --add mdmonitor
fi

%preun
if [ "$1" = 0 ]; then
    service mdmonitor stop > /dev/null 2>&1 ||:
    /sbin/chkconfig --del mdmonitor
fi

%postun
if [ "$1" -ge "1" ]; then
    service mdmonitor condrestart > /dev/null 2>&1
fi

%files
%defattr(-,root,root,-)
%doc TODO ChangeLog mdadm.conf-example COPYING misc/*
/lib/udev/rules.d/*
/sbin/*
%{_sbindir}/raid-check
%{_initrddir}/*
%{_mandir}/man*/md*
%config(noreplace) %{_sysconfdir}/cron.d/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%attr(0700,root,root) %dir /var/run/mdadm

%changelog
* Tue Jun 21 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.el6_8.5
- Fix problem with reshaping IMSM arrays, where a new reshape could be
  launched before the first reshape had fully completed, leading to
  unpected results.
- Resolves bz1348544

* Fri Jun 17 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.el6_8.4
- Fix problem with mdadm large device names overflowing an internal buffer,
  potentially leading to segfaults.
- Resolves bz1347808

* Tue May 24 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.el6_8.3
- Retry reading sync_completed state to avoid a reshape not continuing after
  restarting a reshape
  This is an additional patch to resolve this bug.
- Resolves bz1331331

* Wed May 11 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.el6_8.2
- Fix problem with mdadm crashing during multi-volume reshape with NVMe drives
- Resolves bz1334956

* Tue May 10 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.el6_8.1
- Bump revision to be able to build
- Resolves bz1331331

* Thu Apr 28 2016 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.4-1.1
- Fix a number of issues with interrupting reshapes of IMSM RAID arrays
- Resolves bz1331331

* Wed Dec 9 2015 Xiao Ni <xni@redhat.com> - 3.3.4-1
- Update to mdadm-3.3.4
- Resolves bz1248989

* Tue May 19 2015 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.2-5
- Fix race condition when assembling IMSM volumes with mdadm -As
- Resolves bz1146994

* Fri Apr 17 2015 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.2-4
- Fix problem where mdadm allowed the creation of more arrays than
  supported by the BIOS.
- Resolves bz1211564

* Tue Apr 14 2015 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.2-3
- Add missing patches to support IMSM RAID spanning NVMe controllers
- Resolves bz1211500

* Wed Feb 11 2015 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3.2-2
- Do not install superfluous udev rule
- Resolves bz1146536

* Sat Nov 1 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-7
- Fix problem with mdadm.conf AUTO=-all not being handled correctly
- Resolves bz1159399

* Wed Sep 3 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-6
- Fix problem with reshape of IMSM RAID arrays failing to start
- Disallow IMSM arrays spanning multiple controllers
- Fix problem with reshape failing to restart when reassembling IMSM RAID
- Resolves bz1136880, bz1136891, bz1136903

* Wed Sep 3 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-5
- Fix problem with not being able to create IMSM arrays larger than 100GiB
- Resolves bz1136868

* Mon Jun 30 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-4
- Actually apply the patch introduced in 3.3-3
- Resolves bz1113871

* Mon Jun 30 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-3
- Disable DDF support as it is not supported in RHEL
- Resolves bz1113871

* Fri Apr 11 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-2
- Fix problem with path=* policy not working, due to lack of /dev/disk/by-path/
- Resolves bz1059193

* Wed Mar 19 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.3-1
- Update to mdadm-3.3
- Resolves bz1030606

* Mon Mar 17 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-11
- Fix problem where mdadm would crash if trying to create an IMSM array with
  missing drives.
- Resolves bz1059307

* Fri Mar 14 2014 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-10
- Fix problem of IMSM platform capabilities not being detected in UEFI
  mode when only the second SATA controller is enabled.
- Resolves bz1075529

* Thu Dec 12 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-9
- Change permissions of /etc/cron.d/raid-check to 600
- Resolves bz1012505
- Avoid double close() issue reported by Coverity
- Resolves bz991041

* Wed Dec 11 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-8
- Work around udev sporadically not updating ID_FS_TYPE field of block
  device entry in its database when array is being created.
- Resolves bz1040006

* Wed Oct 9 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-7
- Check for DM_UDEV_DISABLE_OTHER_RULES_FLAG instead of
  DM_UDEV_DISABLE_DISK_RULES_FLAG in 65-md-incremental.rules 
- Resolves bz1015514

* Mon Sep 30 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-6
- Fix problem with failed disks in failed RAID volume not being removed
- Resolves bz1010859

* Thu Sep 26 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-5
- Fix problem with rebuild not restarting on stopped RAID1/10 IMSM arrays
- Resolves bz1001627

* Fri Aug 23 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-4
- Fix problem with RAID10 resync failing to restart if it has been
  stopped after 50% completion.
- Resolves bz995105

* Thu Jul 18 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-3
- Fix problem where first stop command doesn't stop container during
  IMSM volume's reshape
- Fix annoying build noise caused by latest rpmbuild
- Resolves bz956016

* Fri May 3 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-2
- Enhance raid-check to allow the admin to specify the max number of
  concurrent arrays to be checked at any given time.
- Resolves bz819943

* Thu May 2 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.6-1
- Update mdadm to upstream release v3.2.6
  This includes all current patches, except for
  mdadm-3.2.5-imsm-Forbid-spanning-between-multiple-controllers.patch and
  mdadm-3.2.5-Create.c-check-if-freesize-is-equal-0.patch
- Fix problem with arrays marked <ignored> in mdadm.conf still being
  auto-assembled
- Fix problem with it not being possible to use <ignore> more than
  once in mdadm.conf
- Resolves bz922971
- Resolves bz902142
- Resolves bz902137

* Thu May 2 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-6
- Fix problem with IMSM metadata where resync progress would be lost
  if an array was stopped during ongoing expansion of a RAID1/5 volume.
- Resolves bz903212

* Mon Apr 29 2013 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-5
- Fix problem with IMSM RAID5 not rebuilding after reboot
- Resolves bz955972

* Thu Dec 6 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-4
- Fix typo in error message in fix for 880208. No code functional change
- Resolves bz880208

* Wed Nov 28 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-3
- Avoid corruption by prohibiting an IMSM array from spanning multiple
  controllers (bz878810)
- Prevent creation of a second IMSM array of size 0 (bz880208)
- Avoid segfault when running mdadm --detail on an IMSM raid1 array
  where two drives have been disabled (bz880225)
- Resolves bz878810, bz880208, bz880225

* Thu Oct 4 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-2
- Resolve issue with ambiguous licenses
- Resolves bz862565

* Fri Aug 10 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.5-1
- Update mdadm to upstream release v3.2.5
  This includes all current patches, except for
  mdadm-3.2.3-imsm-fix-correct-checking-volume-s-degradation.patch
- Resolved bz812358

* Thu May 31 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-11
- Fix case where reshape of IMSM RAID fails because we don't check the
  return value when trying to read the word 'degraded' from sysfs,
  resulting in the use of random stack data.
- Resolves bz824815

* Thu May 10 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-10
- Fix man-page to state the correct location for the device-map file
- Resolves bz820643

* Thu Apr 26 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-9
- Correctly fix failure when trying to add internal bitmap to 1.0 arrays
- Resolves bz811282

* Mon Apr 23 2012 Doug Ledford <dledford@redhat.com> - 3.2.3-8
- The support for expanding imsm arrays/containers was accepted upstream,
  update to the official patches from there
- Fix for the issue of --add not being very smart
- Fix an issue causing rebuilds to fail to restart on reboot (data
  corrupter level problem)
- Reset the bad flag on map file updates
- bitmap_offset is signed, treat it as such
- Related: bz808475
- Resolves: bz808776, bz812001, bz814743, bz811282

* Sat Apr 07 2012 Doug Ledford <dledford@redhat.com> - 3.2.3-7
- Fix Monitor mode sometimes crashes when a resync completes
- Fix missing symlink for mdadm container device when incremental creates
  the array
- Make sure when creating a second array in a container that the second
  array uses all available space since leaving space for a third array
  is invalid
- Validate the number of imsm volumes per controller
- Fix issues with imsm arrays and disks larger than 2TB
- Add support for expanding imsm arrays/containers
- Resolves: bz808424, bz808519, bz808492, bz808438, bz808507,
	    bz808475

* Tue Feb 28 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-6
- Fix segfault if trying to write superblock to non existing device
- Resolves: bz795751

* Tue Feb 21 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-5
- Fix issue with devices failing to be added to a raid using bitmaps,
  due to trying to write the bitmap with mis-aligned buffers using
  O_DIRECT 
- Resolves: bz790394

* Mon Feb 20 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-4
- Fix bug where IMSM arrays stay inactive in case a reboot is
- performed during the reshape process.
- Resolves: bz730052

* Thu Feb 9 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-3
- Really enable fix for problem where a device fails to remove from
- an IMSM container
- Resolves: bz771332

* Thu Feb 2 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-2
- Fix problem where a device fails to remove from an IMSM container
- Resolves: bz771332

* Thu Jan 5 2012 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.3-1
- Update to latest upstream mdadm-3.2.3
- Resolves: bz745802

* Fri Nov 4 2011 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.2-9
- Fix problem where an IMSM RAID is rejected because of unexpected
  attribute settings. Additional fix being extra cautious from -8.
- Resolves: bz733153

* Thu Nov 3 2011 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.2-8
- Fix problem where an IMSM RAID is rejected because of unexpected
  attribute settings.
- Resolves: bz733153

* Mon Oct 24 2011 Jes Sorensen <Jes.Sorensen@redhat.com> - 3.2.2-7
- Fix problem where a dirty IMSM RAID isn't assembled correctly during
  boot, preventing booting from this RAID device.
- Resolves: bz692261

* Wed Aug 31 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-6
- Fix several new coverity issues introduced by changes between the rhel6.1
  and rhel6.2 mdadm package (this does not attempt to address coverity
  issues that also exist in rhel6.1)
- Resolves: bz734716

* Thu Aug 25 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-5
- Fix multiple issues in the udev incremental assembly rules file.  We should
  now properly support:
  1) Nested md raid arrays
  2) md raid arrays built on top of dm device (like LUKS encrypted devices)
  3) md raid arrays build on top of dm multipath devices (we should no longer
    attempt to grab the path device instead of waiting for the logical
    multipath device to come live and grabbing it for our md raid usage)
- Resolves: bz598513, bz609122

* Thu Aug 11 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-4
- Minor tweaks to wording in the comments of the /etc/sysconfig/raid-check
  file
- Resolves: bz708280

* Mon Aug 01 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-3
- Be robust when running on a version 3.0 kernel
- Properly set the default chunk size on orom devices
- Fix getinfo_super_imsm so a hack in create.c can be dropped
- Make the output of --detail more accurately communicate the state of
  a device that is waiting on a resync because another resync is
  already running
- A few tweaks to the man page for mdadm to clarify usage in relation to
  imsm arrays
- Resolves: bz727216, bz727207, bz727210, bz727212, bz727203

* Wed Jul 27 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-2
- When using writemostly on a raid1 array, if you remove a device that
  is readwrite and then readd it, it can end up being listed as writemostly
  if the device used to pull the superblock info from was writemostly.
  Properly clear the writemostly bit when adding/readding a device.
- Related: bz706500

* Mon Jul 18 2011 Doug Ledford <dledford@redhat.com> - 3.2.2-1
- Update to latest upstream release (many bugfixes related to the new
  automatic rebuild support: bz716413, bz694083, bz694092, bz694103,
  bz694121, bz694779, bz695336, bz702270)
- Correct typo in /etc/sysconfig/raid-check file (bz708280)
- Fix a bug related to readding devices into an array (bz706500)
- Resolves: bz716413, bz694083, bz694092, bz694103, bz694121, bz694779
- Resolves: bz695336, bz702270, bz708280, bz706500

* Mon Mar 28 2011 Doug Ledford <dledford@redhat.com> - 3.2.1-1
- Update to latest upstream release
- Don't report mismatch counts on either raid1 or raid10 devices
- Check both active and idle arrays during raid check runs
- Move raid-check script to /usr/sbin, add a crontab entry to /etc/cron.d
  and mark it config(noreplace) so that users can select their own
  raid check frequency and it will be preserved across updates
- Allow the raid check script to set both the cpu and io priority on the
  raid check process in an effort to minimize the impact to users on the
  system
- Related: bz633306

* Fri Feb 04 2011 Doug Ledford <dledford@redhat.com> - 3.2-1
- Update to latest upstream release
- Related: bz633306, bz633667, bz633671, bz633688, bz633690, bz633692
- Fix mdadm udev rules file
- Resolves: bz605710
- Process the Y option
- Resolves: bz636883

* Wed Aug 11 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-1
- Update to official 3.1.3 release instead of a git snapshot
- Add patch for return code in the case that a container is not assembled
  due to insufficient drives (bz622408)
- Add patch to allow the deprecated --no-degraded option to be passed in,
  just not honored (bz622408)
- Resolves: bz622408

* Wed Aug 04 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-0.git20100804.1
- Update to latest upstream (new fix for racy lockfile handling issue)
- Related: bz616597

* Thu Jul 29 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-0.git20100722.2
- Update mdadm rules file to honor noiswmd command line option
- Resolves: bz605710

* Thu Jul 22 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-0.git20100722.1
- Change git date format to the correct format (YYYYMMDD)
- Update to latest upstream push (fixes bz604023)
- Resolves: bz604023

* Tue Jul 20 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-0.git07202010.2
- Fix racy locking of mapfile (bz616597)
- Resolves: bz616597

* Tue Jul 20 2010 Doug Ledford <dledford@redhat.com> - 3.1.3-0.git07202010.1
- Update to latest git repo (3.1.2 plus pending changes, bz617280)
- Remove mdadm.static as its no longer used in initrd creation
- Remove glibc-static buildreq
- Resolves: bz617280

* Tue Apr 13 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-10
- Minor update to mdadm.rules to make anaconda happy

* Thu Apr 08 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-9
- Slight fix on container patch

* Thu Apr 08 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-8
- Updated container patch that also enables mdadm -IRs for imsm devices

* Tue Apr 06 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-7
- Fix up directory in mdmonitor init script so that we restart mdmon like we
  are supposed to
- Add a rule to run incremental assembly on containers in case there are
  multiple volumes in a container and we only started some of them in the
  initramfs
- Make -If work with imsm arrays.  We had too restrictive of a test in
  sysfs_unique_holder.
- Make incremental assembly of containers act like incremental assembly of
  regular devices (aka, --run is needed to start a degraded array)

* Tue Apr 06 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-6
- Typo in new rules file

* Tue Apr 06 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-5
- Enable incremental support for imsm devices

* Tue Apr 06 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-4
- One line fix for ppc64 compiles

* Tue Apr 06 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-3
- Clean up directory mess once and for all
- Add incremental remove support

* Wed Mar 17 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-2
- Add a little more paranoia checking to the RebuildMap code to avoid ever
  having the same infinite loop as in bz569019 again even if we change file
  locations to somewhere where we can't create a mapfile

* Tue Mar 16 2010 Doug Ledford <dledford@redhat.com> - 3.1.2-1
- Grab latest upstream release instead of git repo snapshot (bz552344, bz572561)
- The lack of /dev/md is causing problems, so add code to mapfile.c to cause
  us to create /dev/md if it doesn't exist (bz569019)

* Tue Feb 23 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.6
- Newer version of imsm patch that leaves warning, but only when there
  actually are too many devices on the command line (bz554974)

* Sun Feb 21 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.5
- The uuid patch cause a different problem during assembly, so use a gross
  hack to work around the uuid issue that won't break assembly until fixed
  properly upstream (bz567132)

* Sun Feb 21 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.4
- Fix problem with booting multiple imsm containers when they aren't listed
  "just so" in the mdadm.conf file (bz554974)

* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.3
- Don't run the raid-check script if the kernel doesn't support
  md devices (bz557053)
- Don't report any mismatch_cnt issues on raid1 devices as there are
  legitimate reasons why the count may not be 0 and we are getting enough
  false positives that it renders the check useless (bz554217, bz547128)

* Thu Feb 18 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.2
- Fix s390/ppc64 UUID byte swap issue

* Wed Feb 17 2010 Doug Ledford <dledford@redhat.com> - 3.1.1-0.gcd9a8b5.1
- Update to head of upstream git repo, which contains a significant number
  of bug fixes we need (bz543746)

* Fri Jan 15 2010 Doug Ledford <dledford@redhat.com> - 3.0.3-3
- Fix crash when AUTO keyword is in mdadm.conf (bz552342)

* Tue Dec 01 2009 Doug Ledford <dledford@redhat.com> - 3.0.3-2
- Minor tweak to init script for LSB compliance (bz527957)

* Wed Nov 04 2009 Doug Ledford <dledford@redhat.com> - 3.0.3-1
- New upstream release 3.0.3 (bz523320, bz527281)
- Update a couple internal patches
- Drop a patch in that was in Neil's tree for 3.0.3 that we had pulled for
  immediate use to resolve a bug
- Drop the endian patch because it no longer applied cleanly and all attempts
  to reproduce the original problem as reported in bz510605 failed, even up
  to and including downloading the specific package that was reported as
  failing in that bug and trying to reproduce with it on both ppc and ppc64
  hardware and with both ppc and ppc64 versions on the 64bit hardware.
  Without a reproducer, it is impossible to determine if a rehashed patch
  to apply to this code would actually solve the problem, so remove the patch
  entirely since the original problem, as reported, was an easy to detect DOA
  issue where installing to a raid array was bound to fail on reboot and so
  we should be able to quickly and definitively tell if the problem resurfaces.
- Update the mdmonitor init script for LSB compliance (bz527957)
- Link from mdadm.static man page to mdadm man page (bz529314)
- Fix a problem in the raid-check script (bz523000)
- Fix the intel superblock handler so we can test on non-scsi block devices

* Fri Oct  2 2009 Hans de Goede <hdegoede@redhat.com> - 3.0.2-1
- New upstream release 3.0.2
- Add a patch fixing mdadm --detail -export segfaults (bz526761, bz523862)
- Add a patch making mdmon store its state under /dev/.mdadm for initrd
  mdmon, rootfs mdmon handover
- Restart mdmon from initscript (when running) for rootfs mdmon handover

* Thu Sep 17 2009 Doug Ledford <dledford@redhat.com> - 3.0-4
- Stop some mdmon segfaults (bz523860)

* Tue Sep 15 2009 Doug Ledford <dledford@redhat.com> - 3.0-3
- Update to current head of upstream git repo for various imsm related fixes
  (fixes bz523262)
- Fix display of metadata version in output of Detail mode
- Add UUID output to --detail --export (bz523314)

* Fri Jul 24 2009 Doug Ledford <dledford@redhat.com> - 3.0-2
- Improved raid-check script as well as the ability to configure what devices
  get checked
- Endian patch for uuid generation

* Mon Jun 29 2009 Doug Ledford <dledford@redhat.com> - 3.0-1
- Remove stale patches already accepted by upstream
- Fix the raid-check script to only try and check a device if it is
  checkable
- Update to official mdadm-3.0 version
- Resolves: bz505587, bz505552

* Tue May 19 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.7
- Move the mdadm.map file from /dev/md/ to /dev/ so the installer doesn't
  need to precreate the /dev/md/ directory in order for incremental
  assembly to work

* Tue May 19 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.6
- Only check raid devices automatically, do not attempt to repair them
  during the weekly data scrubbing

* Fri Mar 20 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.5
- Fix a few issues with the new code to determine when a device gets to
  keep its name and when it doesn't

* Fri Mar 20 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.4
- Change the perms on the udev rules file, it doesn't need to be +x

* Fri Mar 20 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.3
- Slightly tweak the udev rules to make sure we don't start arrays
  while running in rc.sysinit...leave array starting to it instead
- Modify mdadm to put its mapfile in /dev/md instead of /var/run/mdadm
  since at startup /var/run/mdadm is read-only by default and this
  breaks incremental assembly
- Change how mdadm decides to assemble incremental devices using their 
  preferred name or a random name to avoid possible conflicts when plugging
  a foreign array into a host

* Wed Mar 18 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.2
- Change around the mdadm udev rules we ship to avoid a udev file conflict

* Tue Mar 17 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel3.1
- Update to latest devel release
- Remove the no longer necessary udev patch
- Remove the no longer necessary warn patch
- Remove the no longer necessary alias patch
- Update the mdadm.rules file to only pay attention to device adds, not
  changes and to enable incremental assembly
- Add a cron job to run a weekly repair of the array to correct bad sectors
- Resolves: bz474436, bz490972

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.devel2.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel2.2
- Readd our old mdadm rules file that does incremental assembly
- Remove the new mdadm rules file from upstream as we already have this in
  our udev package (and the one in the udev package already has a bug fixed)

* Thu Feb 12 2009 Doug Ledford <dledford@redhat.com> - 3.0-0.devel2.1
- Update to latest upstream devel release
- Use the udev rules file included with mdadm instead of our own
- Drop all the no longer relevant patches
- Fix a build error in mdopen.c
- Fix the udev rules path in Makefile
- Fix a compile issue with the __le32_to_cpu() macro usage (bad juju to
  to operations on the target of the macro as it could get executed
  multiple times, and gcc now throws an error on that)
- Add some casts to some print statements to keep gcc from complaining

* Fri Oct 24 2008 Doug Ledford <dledford@redhat.com> - 2.6.7.1-1
- Updated to latest upstream stable release (#466803)
- Change udev rule to not assemble degraded arrays (#453314)
- Fix metadata matching in config file (#466078)
- Fix assembly of raid10 devices (#444237)
- Fix incremental assembly of partitioned raid devices (#447818)

* Thu Jun 26 2008 Doug Ledford <dledford@redhat.com> - 2.6.7-1
- Update to latest upstream version (should resolve #444237)
- Drop incremental patch as it's now part of upstream
- Clean up all the open() calls in the code (#437145)
- Fix the build process to actually generate mdassemble (#446988)
- Update the udev rules to get additional info about arrays being assembled
  from the /etc/mdadm.conf file (--scan option) (#447818)
- Update the udev rules to run degraded arrays (--run option) (#452459)

* Thu Apr 17 2008 Bill Nottingham <notting@redhat.com> - 2.6.4-4
- make /dev/md if necessary in incremental mode (#429604)
- open RAID devices with O_EXCL to avoid racing against other --incremental processes (#433932)
 
* Fri Feb  1 2008 Bill Nottingham <notting@redhat.com> - 2.6.4-3
- add a udev rules file for device assembly (#429604)

* Fri Jan 18 2008 Doug Ledford <dledford@redhat.com> - 2.6.4-2
- Bump version and rebuild

* Fri Oct 19 2007 Doug Ledford <dledford@redhat.com> - 2.6.4-1
- Update to latest upstream and remove patches upstream has taken

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2.6.2-5
- Rebuild for selinux ppc32 issue.

* Mon Jul 09 2007 Doug Ledford <dledford@redhat.com> - 2.6.2-4
- Oops, if we call -C -e1, minor_version is no longer properly set, fix that
  up
- Related: bz230207

* Fri Jul 06 2007 Doug Ledford <dledford@redhat.com> - 2.6.2-3
- Oops, had to update the file leak patch, missed one thing
- Minor tweak to return codes in init script and add LSB header
- Resolves: bz244582, bz246980

* Mon Jul 02 2007 Doug Ledford <dledford@redhat.com> - 2.6.2-2
- Fix a file leak issue when mdadm is in monitor mode
- Update mdadm init script so that status will always run and so
  return codes are standards compliant
- Fix assembly of version 1 superblock devices
- Make the attempt to create an already running device have a clearer
  error message
- Allow the creation of a degraded raid4 array like we allow for raid5
- Make mdadm actually pay attention to raid4 devices when in monitor mode
- Make the mdmonitor script use daemon() correctly
- Fix a bug where manage mode would not add disks correctly under certain
  conditions
- Resolves: bz244582, bz242688, bz230207, bz169516, bz171862, bz171938
- Resolves: bz174642, bz224272, bz186524

* Mon Jul 02 2007 Doug Ledford <dledford@redhat.com> - 2.6.2-1
- Update to latest upstream
- Remove requirement for /usr/sbin/sendmail - it's optional and not on by
  default, and sendmail isn't *required* for mdadm itself to work, and isn't
  even required for the monitoring capability to work, just if you want to
  have the monitoring capability do the automatic email thing instead of
  run your own program (and if you use the program option of the monitor
  capability, your program could email you in a different manner entirely)

* Mon Apr 16 2007 Doug Ledford <dledford@redhat.com> - 2.6.1-4
- More cleanups for merge review process
- Related: bz226134

* Wed Apr 11 2007 Doug Ledford <dledford@redhat.com> - 2.6.1-3
- Various cleanups as part of merge review process
- Related: bz226134

* Sat Mar 31 2007 Doug Ledford <dledford@redhat.com> - 2.6.1-2
- Oops, missing a dependency in the Makefile

* Sat Mar 31 2007 Doug Ledford <dledford@redhat.com> - 2.6.1-1
- Update to latest upstream version
- Resolves: bz233422

* Fri Jan 26 2007 Doug Ledford <dledford@redhat.com> - 2.6-1
- Update to latest upstream version
- Remove the mdmpd daemon entirely.  Now that multipath tools from the lvm/dm
  packages handles multipath devices well, this is no longer needed.
- Various cleanups in the spec file

* Thu Nov 09 2006 Doug Ledford <dledford@redhat.com> - 2.5.4-3
- Add a fix for the broken printout of array GUID when using the -E --brief
  flags

* Fri Oct 13 2006 Doug Ledford <dledford@redhat.com> - 2.5.4-2
- tag present on another branch and can't be forcibly moved
  required number bump

* Fri Oct 13 2006 Doug Ledford <dledford@redhat.com> - 2.5.4-1
- Update to 2.5.4 (listed as a bugfix update by upstream)
- Remove previous bitmap patch that's now part of 2.5.4

* Sun Oct  8 2006 Doug Ledford <dledford@redhat.com> - 2.5.3-2
- Fix a big-endian machine error in the bitmap code (Paul Clements)

* Mon Aug  7 2006 Doug Ledford <dledford@redhat.com> - 2.5.3-1
- Update to 2.5.3 which upstream calls a "bug fix" release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.5.2-1.1
- rebuild

* Fri Jul  7 2006 Doug Ledford <dledford@redhat.com> - 2.5.2-1
- Update to 2.5.2
- Remove auto default patch as upstream now has a preferred default auto method

* Wed Mar  8 2006 Peter Jones <pjones@redhat.com> - 2.3.1-3
- fix build on ppc64

* Wed Mar  8 2006 Jeremy Katz <katzj@redhat.com> - 2.3.1-2
- fix build on ppc

* Wed Mar  8 2006 Jeremy Katz <katzj@redhat.com> - 2.3.1-1
- update to 2.3.1 to fix raid5 (#184284)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2-1.fc5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2-1.fc5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec 05 2005 Warren Togami <wtogami@redhat.com> 2.2-1
- 2.2 upgrade (#167897)
- disable diet because we don't ship it anymore
  and we don't actually use mdassemble now

* Mon May 16 2005 Doug Ledford <dledford@redhat.com> 1.11.0-4.fc4
- Make the mdmonitor init script use the pid-file option, major cleanup
  of the script now possible (#134459)

* Mon May 16 2005 Doug Ledford <dledford@redhat.com> 1.11.0-3.fc4
- Put back the obsoletes: raidtools that was present in 1.11.0-1.fc4

* Mon May 16 2005 Doug Ledford <dledford@redhat.com> 1.11.0-2.fc4
- Change the default auto= mode so it need not be on the command line to
  work with udev, however it is still supported on the command line (#132706)
- Add a man page (from Luca Berra) for mdassemble

* Wed May 11 2005 Doug Ledford <dledford@redhat.com> - 1.11.0-1.fc4
- Upgrade to 1.11.0

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1.9.0-3.fc4
- fix mdmonitor initscript (#144717)

* Mon Mar 21 2005 Doug Ledford <dledford@redhat.com> 1.9.0-2
- Build mdadm.static and mdassemble (static as well) to be used in initrd
  images

* Wed Mar 09 2005 Doug Ledford <dledford@redhat.com> 1.9.0-1
- Initial upgrade to 1.9.0 and update of doc files
- Fix an s390 build error

* Mon Oct 04 2004 Doug Ledford <dledford@redhat.com> 1.6.0-2
- Remove /etc/mdadm.conf from the file list.  Anaconda will write one out
  if it's needed.

* Fri Oct 01 2004 Doug Ledford <dledford@redhat.com> 1.6.0-1
- Update to newer upstream version
- Make mdmpd work on kernels that don't have the event interface patch

* Fri Jul 30 2004 Dan Walsh <dwalsh@redhat.com> 1.5.0-11
- Create a directory /var/run/mdadm to contain mdadm.pid
- This cleans up SELinux problem

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 22 2004 Doug Ledford <dledford@redhat.com> - 1.5.0-9
- Fix Makefile and build method to satisfy bz #123769
- Add mdmpd man page, update mdmpd version to 0.3 - bz #117160
- Make sure mdadm --monitor closes all md device files so that md devices
  can be stopped while mdadm is still running - bz #119532

* Thu May 20 2004 Jeremy Katz <katzj@redhat.com> - 1.5.0-8
- remove unneeded patch, can use --run instead

* Wed May 19 2004 Jeremy Katz <katzj@redhat.com> - 1.5.0-7
- add patch with reallyforce mode on creation to be used by anaconda

* Wed May 12 2004 Doug Ledford <dledford@redhat.com> 2.5.0-6
- Fix a bug in the postun scriptlet related to downgrading to a version
  of mdadm that doesn't include the mdmpd daemon.

* Fri May 07 2004 Doug Ledford <dledford@redhat.com> 1.5.0-5
- Disable service mdmpd by default to avoid [Failed] messages on
  current 2.6 kernels.  Possibly re-enable it by default once the
  2.6 kernels have the md event interface.

* Thu Apr 22 2004 Doug Ledford <dledford@redhat.com> 1.5.0-4
- Update mdmonitor script to start daemon more cleanly
- Repackage mdmpd tarball to include gcc-3.4 changes and to make
  mdmpd properly daemonize at startup instead of forking and leaving
  the child attached to the terminal.

* Thu Mar  4 2004 Bill Nottingham <notting@redhat.com> 1.5.0-3
- ship /var/run/mpmpd (#117497)

* Thu Feb 26 2004 Doug Ledford <dledford@redhat.com> 1.5.0-2
- Add a default MAILADDR line to the mdadm.conf file installed by default
  (Bugzilla #92447)
- Make it build with gcc-3.4

* Mon Feb 23 2004 Doug Ledford <dledford@redhat.com> 1.5.0-1
- Update to 1.5.0 (from Matthew J. Galgoci <mgalgoci@redhat.com>)

* Sun Nov 16 2003 Doug Ledford <dledford@redhat.com> 1.4.0-1
- fix problem with recovery thread sleeping in mdmpd

* Fri Nov 14 2003 Doug Ledford <dledford@redhat.com>
- sync upstream
- add mdmpd package into mdadm package

* Wed Sep 10 2003 Michael K. Johnson <johnsonm@redhat.com> 1.3.0-1
- sync upstream

* Tue Mar 11 2003 Michael K. Johnson <johnsonm@redhat.com> 1.1.0-1
- sync upstream

* Tue Jan 28 2003 Michael K. Johnson <johnsonm@redhat.com> 1.0.1-1
- update for rebuild

* Wed Dec 25 2002 Tim Powers <timp@redhat.com> 1.0.0-8
- fix references to %%install in the changelog so that it will build

* Fri Dec 13 2002 Elliot Lee <sopwith@redhat.com> 1.0.0-7
- Rebuild

* Fri Jul 12 2002 Michael K. Johnson <johnsonm@redhat.com>
- Changed RPM Group to System Environment/Base

* Wed May 15 2002 Michael K. Johnson <johnsonm@redhat.com>
- minor cleanups to the text, conditionalize rm -rf
- added mdmonitor init script

* Fri May 10 2002  <neilb@cse.unsw.edu.au>
- update to 1.0.0
- Set CXFLAGS instead of CFLAGS

* Sat Apr  6 2002  <neilb@cse.unsw.edu.au>
- change %%install to use "make install"

* Fri Mar 15 2002  <gleblanc@localhost.localdomain>
- beautification
- made mdadm.conf non-replaceable config
- renamed Copyright to License in the header
- added missing license file
- used macros for file paths

* Fri Mar 15 2002 Luca Berra <bluca@comedia.it>
- Added Obsoletes: mdctl
- missingok for configfile

* Tue Mar 12 2002 NeilBrown <neilb@cse.unsw.edu.au>
- Add md.4 and mdadm.conf.5 man pages

* Fri Mar 08 2002 Chris Siebenmann <cks@cquest.utoronto.ca>
- builds properly as non-root.

* Fri Mar 08 2002 Derek Vadala <derek@cynicism.com>
- updated for 0.7, fixed /usr/share/doc and added manpage

* Tue Aug 07 2001 Danilo Godec <danci@agenda.si>
- initial RPM build
