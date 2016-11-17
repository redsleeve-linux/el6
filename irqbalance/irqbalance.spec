Summary:        IRQ balancing daemon
Name:           irqbalance
Version:        1.0.7
Release:        8%{?dist}.0
Epoch:          2
Group:          System Environment/Base
License:        GPLv2
Url:            https://github.com/Irqbalance/irqbalance
Source0:        https://github.com/Irqbalance/irqbalance/archive/v%{version}.tar.gz
Source1:        irqbalance.init
Source2:        irqbalance.sysconfig
BuildRequires:  autoconf automake libtool libcap-ng numactl-devel
Requires(post): chkconfig
Requires(postun):chkconfig
Requires(preun):chkconfig

ExclusiveArch:  %{ix86} x86_64 ia64 ppc ppc64 %{arm}
Obsoletes:      kernel-utils
BuildRequires:  glib2-devel pkgconfig imake libcap-ng-devel
Requires:       kernel >= 2.6.32-358.2.1, glib2 >= 2.28

%global _hardened_build 1

Patch1: irqbalance-1.0.7-security-compile-flags.patch
Patch2: irqbalance-1.0.7-banned-cpus-fix.patch
Patch3: irqbalance-1.0.7-affinity_hint.patch
Patch4: irqbalance-1.0.7-debug_output.patch
Patch5: irqbalance-1.0.7-deepestcache_bits.patch
Patch6: irqbalance-1.0.8-removing-unused-variable-cache_stat.patch
Patch7: irqbalance-1.0.8-Manpage-note-about-ignoring-of-pid-in-some-cases.patch
Patch8: irqbalance-1.0.8-irqbalance-signal-handling-tuning.patch
Patch9: irqbalance-1.0.8-Warning-when-irqbalance-hasn-t-root-privileges.patch
Patch10: irqbalance-1.0.7-manpage-hostname.patch
Patch11: irqbalance-1.0.8-classify-mem-leak.patch
Patch12: irqbalance-1.0.8-polscript-doc.patch
Patch13: irqbalance-1.0.7-banscript-enable.patch
Patch14: irqbalance-1.0.7-banscript-docs.patch
Patch15: irqbalance-1.0.8-separate-banned-irqs.patch
Patch16: irqbalance-1.0.8-fix-cpulist_parse-definition-to-match-bitmap_parseli.patch
Patch17: irqbalance-1.0.8-import-__bitmap_parselist-from-Linux-kernel.patch
Patch18: irqbalance-1.0.8-parse-isolcpus-from-proc-cmdline-to-set-up-banned_cp.patch


%description
irqbalance is a daemon that evenly distributes IRQ load across
multiple CPUs for enhanced performance.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
sh ./autogen.sh
%{configure}
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
install -D -p -m 0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING AUTHORS
%{_sbindir}/irqbalance
%{_initrddir}/irqbalance
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/sysconfig/irqbalance

%preun
if [ "$1" = "0" ] ; then
 /sbin/chkconfig --del irqbalance
fi

%post
if [ "$1" = "1" ] ; then
 /sbin/chkconfig --add irqbalance
fi

%triggerpostun -- kernel-utils
/sbin/chkconfig --add irqbalance
exit 0


%changelog
* Tue Sep 06 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 2:1.0.7-8.0
- Added patch from Jacco
- add ARM architectures

* Tue Feb 02 2016 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-8
- Explicit dependency on newer glib2 added (bz 1302903)

* Wed Nov 18 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-7
- Irqbalance doesn't place irq on isolated cpus (bz 1244948)

* Wed Nov 18 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-6
- Unsolicited irqbalance re-enabling fixed (bz 1273505)

* Thu May 28 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-5
- Broken banirq handling after rebase fixed (bz 1181720)

* Tue Apr 07 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-4
- Banscript option docs renewed (bz 1181720)

* Wed Apr 01 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-3
- Banscript option re-enabled (bz 1178903)

* Tue Jan 20 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-2
- Unused variable removed (bz 1119404)
- Warning when started as non-root (bz 749651)
- More robust signal handling (bz 1158932)
- Fixed manpage hostname (bz 1162247)
- Fixed memleak (bz 1178247)
- Fixed help message typo (bz 1178903)

* Mon Jan 19 2015 Petr Holasek <pholasek@redhat.com> - 2:1.0.7-1
- Rebase to 1.0.7 (bz 1181720)

* Thu May 29 2014 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-10
- Minor source hardening (bz 878001)
- Migrating algorithm fix (bz 1031230)
- Introducing deepestcache option (bz 1052166)
- Debug option behavior fix (bz 1096392)

* Thu May 01 2014 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-9
- Fixed affinity hint default (bz 1079109)

* Mon Jan 20 2014 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-8
- Fixed kernel dependency (bz 987801)

* Thu Jan 16 2014 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-7
- Banned cpus awareness fix(bz 1039178)

* Thu Aug 22 2013 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-6
- Cpu hotplug segfault fixed (bz 991363)

* Wed Jun 26 2013 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-5
- Pidfile enabled (bz 975524)

* Tue Jun 25 2013 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-4
- Fixed kernel dependency (bz 951720)

* Fri Oct 12 2012 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-3
- Man page regression fix (bz 813078)

* Mon Oct 1 2012 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-2
- Correct security flags added
- Init file fixed (bz 860627)

* Tue Sep 25 2012 Petr Holasek <pholasek@redhat.com> - 2:1.0.4-1
- Rebase to 1.0.4 (bz 789946)

* Thu Aug 2 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-35
- Fix segfault (bz 843379)

* Thu May 3 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-34
- numactl* dependencies removed.

* Wed May 2 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-33
- Fix classifying net devices with biosdevname (bz 682211)

* Wed Apr 25 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-32
- NUMA awareness bits were thrown away (from #673234 and #798648)
- Mistake in sysconfig documentation was fixed (bz 732435)

* Mon Mar 5 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-31
- Fix fclose call (bz 798648)

* Mon Feb 13 2012 Petr Holasek <pholasek@redhat.com> - 2:0.55-30
- NUMA awareness bits (bz 673234)
- network devices are classified more correctly

* Tue Sep 07 2010 Anton Arapov <aarapov@redhat.com> - 2:0.55-29
- Add -fPIE to build to enable execshield support (bz 630023)

* Mon Aug 09 2010 Neil Horman <nhorman@redhat.com> - 2:0.55-27
- Fix affinity hint initalization (bz 622560)

* Mon Aug 02 2010 Neil Horman <nhorman@redhat.com> - 2:0.55-26
- Bump NR_CPUS to 4096 for RHEL6 (bz 617705)
- Add affinity_hint support (bz 591515)

* Wed Sep 09 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-25
- Fixing BuildRequires

* Fri Sep 04 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-24
- Fixing irqbalance initscript (bz 521246)

* Wed Sep 02 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-23
- Fixing BuildRequires for new config script

* Tue Sep 01 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-22
- Fixing BuildRequires for new config script

* Tue Sep 01 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-21
- Fixing BuildRequires for new config script

* Tue Sep 01 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-20
- Fixing BuildRequires for new config script

* Tue Sep 01 2009 Neil Horman <nhorman@redhat.com> - 2:0.55-19
- Incorporate capng (bz 520699)

* Fri Jul 31 2009 Peter Lemenkov <lemenkov@gmail.com> - 2:0.55-18
- Added back accidentaly forgotten imake

* Fri Jul 31 2009 Peter Lemenkov <lemenkov@gmail.com> - 2:0.55-17
- Cosmetic fixes in spec-file
- Fixed rpmlint error in the init-script

* Tue Jul 28 2009 Peter Lemenkov <lemenkov@gmail.com> - 2:0.55-16
- Many imrovements in spec-file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.55-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 6 2009 Neil Horman <nhorman@redhat.com>
- Update spec file to build for i586 as per new build guidelines (bz 488849)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.55-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Neil Norman <nhorman@redhat.com> - 2:0.55-12
- Remove odd Netorking dependence from irqbalance (bz 476179)

* Fri Aug 01 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2:0.55-11
- fix license tag

* Wed Jun 04 2008 Neil Horman <nhorman@redhat.com> - 2:0.55-10
- Update man page to explain why irqbalance exits on single cache (bz 449949)

* Tue Mar 18 2008 Neil Horman <nhorman@redhat.com> - 2:0.55-9
- Rediff pid-file patch to not remove initial parse_cpu_tree (bz 433270)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2:0.55-8
- Autorebuild for GCC 4.3

* Thu Nov 01 2007 Neil Horman <nhorman@redhat.com> - 2:0.55-7
- Update to properly hadndle pid files (bz 355231)

* Thu Oct 04 2007 Neil Horman <nhorman@redhat.com> - 2:0.55-6
- Fix irqbalance init script (bz 317219)

* Fri Sep 28 2007 Neil Horman <nhorman@redhat.com> - 2:0.55-5
- Install pie patch
- Grab Ulis cpuparse cleanup (bz 310821)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 2:0.55-4
- Rebuild for selinux ppc32 issue.

* Thu Jul 05 2007 Neil Horman <nhorman@redhat.com> - 0.55.3
- Fixing LSB requirements (bz 246959)

* Tue Dec 12 2006 Neil Horman <nhorman@redhat.com> - 0.55-2
- Fixing typos in spec file (bz 219301)

* Tue Dec 12 2006 Neil Horman <nhorman@redhat.com> - 0.55-1
- Updating to version 0.55

* Mon Dec 11 2006 Neil Horman <nhorman@redhat.com> - 0.54-1
- Update irqbalance to new version released at www.irqbalance.org

* Wed Nov 15 2006 Neil Horman <nhorman@redhat.com> - 1.13-8
- Add ability to set default affinity mask (bz 211148)

* Wed Nov 08 2006 Neil Horman <nhorman@redhat.com> - 1.13-7
- fix up irqbalance to detect multicore (not ht) (bz 211183)

* Thu Nov 02 2006 Neil Horman <nhorman@redhat.com> - 1.13-6
- bumping up MAX_INTERRUPTS to support xen kernels
- rediffing patch1 and patch3 to remove fuzz

* Tue Oct 17 2006 Neil Horman <nhorman@redhat.com> - 1.13-5
- Making oneshot mean oneshot always (bz 211178)

* Wed Sep 13 2006 Peter Jones <pjones@redhat.com> - 1.13-4
- Fix subsystem locking

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 1.13-2
- rebuilt with latest binutils to pick up 64K -z commonpagesize on ppc*
  (#203001)
- Remove hack to use cvs checkin ID as release as it doesn't follow
  packaging guidelines

* Tue Aug 01 2006 Neil Horman <nhorman@redhat.com>
- Change license to GPL in version 0.13

* Sat Jul 29 2006 Dave Jones <davej@redhat.com>
- identify a bunch more classes.

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Tue Jul 11 2006 Dave Jones <davej@redhat.com>
- Further lazy rebalancing tweaks.

* Sun Feb 26 2006 Dave Jones <davej@redhat.com>
- Don't rebalance IRQs where no interrupts have occured.

* Sun Feb 12 2006 Dave Jones <davej@redhat.com>
- Build for ppc[64] too.

* Thu Feb 09 2006 Dave Jones <davej@redhat.com>
- rebuild.

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild with gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- Build as pie, also -D_FORTIFY_SOURCE=2

* Tue Jan 11 2005 Dave Jones <davej@redhat.com>
- Add missing Obsoletes: kernel-utils.

* Mon Jan 10 2005 Dave Jones <davej@redhat.com>
- Start irqbalance in runlevel 2 too. (#102064)

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based on kernel-utils.

