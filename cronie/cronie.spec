%bcond_without selinux
%bcond_without pam
%bcond_without audit
%bcond_without inotify

Summary: Cron daemon for executing programs at set times
Name: cronie
Version: 1.4.4
Release: 16%{?dist}.2
License: MIT and BSD and ISC and GPLv2
Group: System Environment/Base
URL: https://fedorahosted.org/cronie
Source0: https://fedorahosted.org/releases/c/r/cronie/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch1:   cronie-anacron-close-624043.patch
Patch2:   cronie-crontab-permission-676081.patch
Patch3:   cronie-init-615107.patch
Patch4:   cronie-commoncriteria-677364.patch
Patch5:   cronie-675077.patch
Patch6:   cronie-dst_61run.patch
Patch7:   cronie-1.4.4-popen697485.patch
Patch8:   cronie-1.4.4-orphan738232.patch
Patch9:   cronie-1.4.4-init_restart.patch
Patch10:  cronie-1.4.4-comments_in_script.patch
Patch11:  cronie-1.4.4-man_typo.patch
Patch12:  cronie-1.4.4-PATH_via_pam.patch
Patch13:  cronie-1.4.4-lang.patch
Patch14:  cronie-1.4.4-random.patch
Patch15:  cronie-1.4.4-mail.patch
Patch16:  cronie-1.4.4-two_instances_run.patch
Patch17:  cronie-1.4.4-null-deref.patch
Patch18:  cronie-1.4.4-sigterm-child.patch
Patch19:  cronie-1.4.4-shutdown-msg.patch
Patch20:  cronie-1.4.4-getpwnam-error.patch
Patch21:  cronie-1.4.4-temp-name.patch
Patch22:  cronie-1.4.4-refresh-users.patch
Patch23:  cronie-1.4.4-syslog-output.patch

Requires: syslog, bash >= 2.0
Requires: /usr/sbin/sendmail
Conflicts: sysklogd < 1.4.1
Provides: vixie-cron = 4:4.4
Obsoletes: vixie-cron <= 4:4.3
Requires: dailyjobs

%if %{with selinux}
Requires: libselinux >= 2.0.64
Buildrequires: libselinux-devel >= 2.0.64
%endif
%if %{with pam}
Requires: pam >= 1.0.1
Buildrequires: pam-devel >= 1.0.1
%endif
%if %{with audit}
Buildrequires: audit-libs-devel >= 1.4.1
%endif

Requires(post): /sbin/chkconfig coreutils sed
Requires(postun): /sbin/chkconfig
Requires(postun): /sbin/service 
Requires(preun): /sbin/chkconfig 
Requires(preun): /sbin/service

%description
Cronie contains the standard UNIX daemon crond that runs specified programs at
scheduled times and related tools. It is a fork of the original vixie-cron and
has security and configuration enhancements like the ability to use pam and
SELinux.

%package anacron
Summary: Utility for running regular jobs
Requires: crontabs
Group: System Environment/Base
Provides: dailyjobs
Provides: anacron = 2.4
Obsoletes: anacron <= 2.3
Requires(post): coreutils
Requires: %{name} = %{version}-%{release}

%description anacron
Anacron became part of cronie. Anacron is used only for running regular jobs.
The default settings execute regular jobs by anacron, however this could be
overloaded in settings.

%package noanacron
Summary: Utility for running simple regular jobs in old cron style
Group: System Environment/Base
Provides: dailyjobs
Requires: crontabs
Requires: %{name} = %{version}-%{release}

%description noanacron
Old style of {hourly,daily,weekly,monthly}.jobs without anacron. No features.

%prep
%setup -q
%patch1 -p1 -b .624043
%patch2 -p1 -b .676081
%patch3 -p1
%patch4 -p1 -b .commoncriteria
%patch5 -p1
%patch6 -p1 -b .dst
%patch7 -p1 -b .697485
%patch8 -p1 -b .orphan
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1 -b .PATH
%patch13 -p1 -b .lang
%patch14 -p1 -b .random
%patch15 -p1 -b .mail
%patch16 -p1 -b .2run
%patch17 -p1 -b .null-deref
%patch18 -p1 -b .sigterm
%patch19 -p1 -b .shutdown-msg
%patch20 -p1 -b .getpwnam
%patch21 -p1 -b .temp-name
%patch22 -p1 -b .refresh-users
%patch23 -p1 -b .syslog-output

%build
%configure \
%if %{with pam}
--with-pam \
%endif
%if %{with selinux}
--with-selinux \
%endif
%if %{with audit}
--with-audit \
%endif
%if %{with inotify}
--with-inotify \
%endif
--enable-anacron \
 CFLAGS="$RPM_OPT_FLAGS -fPIE -DPIE" \
 LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"


make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT DESTMAN=$RPM_BUILD_ROOT%{_mandir}
mkdir -pm700 $RPM_BUILD_ROOT%{_localstatedir}/spool/cron
mkdir -pm755 $RPM_BUILD_ROOT%{_initrddir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -pm755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
%if ! %{with pam}
    rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/crond
%endif
install -m 755 cronie.init $RPM_BUILD_ROOT%{_initrddir}/crond
install -m 600 crond.sysconfig $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/crond
touch $RPM_BUILD_ROOT%{_sysconfdir}/cron.deny
install -m 644 contrib/anacrontab $RPM_BUILD_ROOT%{_sysconfdir}/anacrontab
install -c -m755 contrib/0hourly $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/0hourly
mkdir -pm 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly
install -c -m755 contrib/0anacron $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/0anacron
mkdir -p $RPM_BUILD_ROOT/var/spool/anacron
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.daily
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.weekly
touch $RPM_BUILD_ROOT/var/spool/anacron/cron.monthly

# noanacron package
install -m 644 contrib/dailyjobs $RPM_BUILD_ROOT/%{_sysconfdir}/cron.d/dailyjobs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add crond

%post anacron
[ -e /var/spool/anacron/cron.daily ] || touch /var/spool/anacron/cron.daily
[ -e /var/spool/anacron/cron.weekly ] || touch /var/spool/anacron/cron.weekly
[ -e /var/spool/anacron/cron.monthly ] || touch /var/spool/anacron/cron.monthly

%preun
if [ "$1" = "0" ]; then
    service crond stop >/dev/null 2>&1 ||:
    /sbin/chkconfig --del crond
fi

%postun
if [ "$1" -ge "1" ]; then
    service crond condrestart > /dev/null 2>&1 ||:
fi

# empty /etc/crontab in case there are only old regular jobs
%triggerun -- cronie < 1.4.1
cp -a /etc/crontab /etc/crontab.rpmsave
sed -e '/^01 \* \* \* \* root run-parts \/etc\/cron\.hourly/d'\
  -e '/^02 4 \* \* \* root run-parts \/etc\/cron\.daily/d'\
  -e '/^22 4 \* \* 0 root run-parts \/etc\/cron\.weekly/d'\
  -e '/^42 4 1 \* \* root run-parts \/etc\/cron\.monthly/d' /etc/crontab.rpmsave > /etc/crontab
exit 0

#copy the lock, remove old daemon from chkconfig
%triggerun -- vixie-cron
cp -a /var/lock/subsys/crond /var/lock/subsys/cronie > /dev/null 2>&1 ||:

#if the lock exist, then we restart daemon (it was running in the past).
#add new daemon into chkconfig everytime, when we upgrade to cronie from vixie-cron
%triggerpostun -- vixie-cron
/sbin/chkconfig --add crond
[ -f /var/lock/subsys/cronie ] && ( rm -f /var/lock/subsys/cronie ; service crond restart ) > /dev/null 2>&1 ||:

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL README ChangeLog
%attr(755,root,root) %{_sbindir}/crond
%attr(4755,root,root) %{_bindir}/crontab
%{_mandir}/man8/crond.*
%{_mandir}/man8/cron.*
%{_mandir}/man5/crontab.*
%{_mandir}/man1/crontab.*
%dir %{_localstatedir}/spool/cron
%dir %{_sysconfdir}/cron.d
%{_initrddir}/crond
%if %{with pam}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/crond
%endif
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/crond
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/cron.deny
%attr(0644,root,root) %{_sysconfdir}/cron.d/0hourly

%files anacron
%defattr(-,root,root,-)
%{_sbindir}/anacron
%attr(0755,root,root) %{_sysconfdir}/cron.hourly/0anacron
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/anacrontab
%dir /var/spool/anacron
%attr(0600,root,root) %ghost %verify(not md5 size mtime) /var/spool/anacron/cron.daily
%attr(0600,root,root) %ghost %verify(not md5 size mtime) /var/spool/anacron/cron.weekly
%attr(0600,root,root) %ghost %verify(not md5 size mtime) /var/spool/anacron/cron.monthly
%{_mandir}/man5/anacrontab.*
%{_mandir}/man8/anacron.*

%files noanacron
%defattr(-,root,root,-)
%attr(0644,root,root) %{_sysconfdir}/cron.d/dailyjobs

%changelog
* Fri Jul 22 2016 Tomáš Mráz <tmraz@redhat.com> - 1.4.4-16.2
- fix support for syslogging of job output (#1237093)

* Fri May 13 2016 Tomáš Mráz <tmraz@redhat.com> - 1.4.4-16.1
- handle all getpwnam() failures as temporary

* Mon Sep 21 2015 Tomáš Mráz <tmraz@redhat.com> - 1.4.4-16
- crontab: use temporary filename properly ignored by crond

* Mon Mar 23 2015 Tomáš Mráz <tmraz@redhat.com> - 1.4.4-15
- fix regression in parsing environment variables in anacrontab (#1204175)

* Thu Feb  5 2015 Tomáš Mráz <tmraz@redhat.com> - 1.4.4-14
- fix segfault on null dereference in anacron (#1031383)
- do not remove daemon pid file in the child process
- add log message about crond shutdown (#1108384)
- add log message when getpwnam fails

* Thu Sep 12 2013 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-12
- nonroot gives different error messages than before 1006869
- Related: rhbz#706979

* Fri Aug 30 2013 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-11
- too many improvements lead to not running any jobs (#1002153)
- Related: rhbz#985888

* Mon Aug 12 2013 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-10
- There must be added CRON_CORRECT_MAIL_HEADER into man page.
- Related: rhbz#922829

* Tue Aug  6 2013 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-9
- during spring DST change are jobs executed 61 times if they are set
  for 2:00 or 3:00 am.
- 995089 - incorrectly running jobs when time difference is negative
- cronie doesn't drop privileges before popen
- adoptions at the crontab orphanage needed
- config file permissions are world readable
- 733697 - Service restart needlessly reports failure
- 743473 - Confusing comments in /etc/cron.hourly/0anacron
- 887859 - Incorrect example in anacrontab manpage
- 990710 - cron disallows setting PATH via PAM
- 985893 - do not use putenv
- 985888 - cronie drops $LANG and never passes it on to jobs run
- 829910 - random prefix in crontables for running jobs
- 922829 - crond generating invalid emails 
- 919440 - prevent new crond process when already running 
- Resolves: rhbz#821046, rhbz#697485, rhbz#738232, rhbz#706979, rhbz#733697
- Resolves: rhbz#743473, rhbz#887859, rhbz#990710, rhbz#985893, rhbz#985888
- Resolves: rhbz#829910, rhbz#922829, rhbz#995089, rhbz#919440

* Thu Mar  4 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-7
- switch off --enable-pie, because it's overloaded with flags in spec
- added RPM_OPT_FLAGS into CFLAGS
- Related: rhbz#676040

* Thu Mar  3 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-6
- apply relro (CFLAGS&DFLAGS) in specfile, because in configure we
 need to call autoreconf.
- Resolve: rhbz#676040

* Mon Feb 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-5
- remove excessive context_free from common criteria patch 677364
- Related: rhbz#677364

* Mon Feb 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-4
- 675077 anacron runs hourly instead of daily=>wrong option in bash script
- fix common criteria patch 677364
- Resolves: rhbz#675077

* Fri Feb 18 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-3
- 624043 selinux issue done by leaking file decriptor
- crontab has wrong permission 676081 & fix in files section 6755->4755
- 615107 echos twice OK in init script
- 677364 common criteria - freeing, cleaning code
- 676040 add relro and PIE into compiler flags
- Resolves: rhbz#624043, rhbz#676081, rhbz#615107, rhbz#677364, rhbz#676040

* Thu Apr 22 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.4-2
- remove patches because they were included in new release.
- 584006 lsb compliance
- upload correct source
- Resolves: bz#584006

* Fri Feb 19 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-6
- CVE-2010-0424 Race condition by setting timestamp
- Resolves: rhbz#566501

* Fri Feb 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-5
- add ISC license
- apply small fixes: anacrontab man page is more readable and
  values from /etc/security/pam_env.conf are used.
- Related: rhzb#543948

* Wed Jan 13 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-4
- 554689 jobs from nfs homes weren't executed
- Related: rhbz#543948

* Tue Jan 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-3
- rebuild with new audit-libs
- Related: rbhz#543948

* Thu Nov  5 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-2
- 533189 pam needs add a line and selinux needs defined one function

* Tue Nov  3 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.3-1
- 531963 and 532482 creating noanacron package

* Mon Oct 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.2-2
- 529632 service crond stop returns appropriate value

* Mon Oct 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.2-1
- new release

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.1-3
- rebuilt with new audit

* Fri Aug 14 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.1-2
- create the anacron timestamps in correct post script

* Fri Aug 14 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4.1-1
- update to 1.4.1
- create and own /var/spool/anacron/cron.{daily,weekly,monthly} to
 remove false warning about non existent files
- Resolves: 517398

* Wed Aug  5 2009 Tomas Mraz <tmraz@redhat.com> - 1.4-4
- 515762 move anacron provides and obsoletes to the anacron subpackage

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.4-2
- merge cronie and anacron in new release of cronie
- obsolete/provide anacron in spec

* Thu Jun 18 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.3-2
- 506560 check return value of access

* Mon Apr 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.3-1
- new release

* Fri Apr 24 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.2-8
- 496973 close file descriptors after exec

* Mon Mar  9 2009 Tomas Mraz <tmraz@redhat.com> - 1.2-7
- rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 Marcela Mašláňová <mmaslano@redhat.com> - 1.2-5
- 477100 NO_FOLLOW was removed, reload after change in symlinked
  crontab is needed, man updated.

* Fri Oct 24 2008 Marcela Mašláňová <mmaslano@redhat.com> - 1.2-4
- update init script

* Thu Sep 25 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-3
- add sendmail file into requirement, cause it's needed some MTA

* Thu Sep 18 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-2
- 462252  /etc/sysconfig/crond does not need to be executable 

* Thu Jun 26 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-1
- update to 1.2

* Tue Jun 17 2008 Tomas Mraz <tmraz@redhat.com> - 1.1-3
- fix setting keycreate context
- unify logging a bit
- cleanup some warnings and fix a typo in TZ code
- 450993 improve and fix inotify support

* Wed Jun  4 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.1-2
- 49864 upgrade/update problem. Syntax error in spec.

* Wed May 28 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.1-1
- release 1.1

* Tue May 20 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-6
- 446360 check for lock didn't call chkconfig

* Tue Feb 12 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-5
- upgrade from less than cronie-1.0-4 didn't add chkconfig

* Wed Feb  6 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-4
- 431366 after reboot wasn't cron in chkconfig

* Tue Feb  5 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-3
- 431366 trigger part => after update from vixie-cron on cronie will 
	be daemon running.

* Wed Jan 30 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-2
- change the provides on higher version than obsoletes

* Tue Jan  8 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.0-1
- packaging cronie
- thank's for help with packaging to my reviewers
