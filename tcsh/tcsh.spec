%define	_bindir	/bin

Summary: An enhanced version of csh, the C shell
Name: tcsh
Version: 6.17
Release: 35%{?dist}.1
License: BSD
Group: System Environment/Shells
Source: ftp://ftp.astron.com/pub/tcsh/%{name}-%{version}.00.tar.gz
Patch1: tcsh-6.15.00-closem.patch
Patch2: tcsh-6.14.00-tinfo.patch
Patch3: tcsh-6.14.00-unprintable.patch
Patch4: tcsh-6.15.00-hist-sub.patch
Patch6: tcsh-6.15.00-ca-color.patch
Patch7: tcsh-6.14.00-set.patch
Patch8: tcsh-6.14.00-syntax.patch
Patch9: tcsh-6.13.00-memoryuse.patch
Patch11: tcsh-6.14.00-order.patch
Patch12: tcsh-6.15.00-rs-color.patch
Patch13: tcsh-6.17.00-mh-color.patch
Patch15: tcsh-6.17.00-printexitvalue.patch
Patch16: tcsh-6.17.00-testsuite.patch
Patch17: tcsh-6.17.00-negative_jobs.patch
Patch21: tcsh-6.17.00-dont-set-empty-remotehost.patch
Patch22: tcsh-6.17.00-dont-print-history-on-verbose.patch
Patch23: tcsh-6.17.00-extrafork.patch
Patch24: tcsh-6.17.00-bz607368.patch
Patch25: tcsh-6.17.00-child-kill-hang.patch
Patch26: tcsh-6.17.00-variable-names.patch
Patch30: tcsh-6.17.00-handle-signals-before-flush.patch
Patch31: tcsh-6.17.00-history-file-locking.patch
Patch33: tcsh-6.17.00-reverse-history-handling-in-loops.patch
Patch34: tcsh-6.17.00-sigint-while-waiting-for-child.patch
Patch35: tcsh-6.17.00-sysmalloc.patch
Patch36: tcsh-6.17.00-wait-hang.patch
Patch37: tcsh-6.17.00-if-statement-parsing.patch
Patch38: tcsh-6.17.00-backport-of-anyerror-variable.patch
Patch39: tcsh-6.17.00-tcsh_posix_status-variable-added.patch
Patch40: tcsh-6.17.00-use-stderr-upon-error.patch
Patch41: tcsh-6.17.00-source-memory-leak.patch
Patch42: tcsh-6.17.00-handle-interrupt-in-eval.patch
Patch43: tcsh-6.17.00-wide-characters-print.patch
Patch44: tcsh-6.17.00-use-long-long-for-calculations.patch
Patch45: tcsh-6.17.00-quote-backslashes-properly.patch

Provides: csh = %{version}
Requires(post): grep
Requires(postun): coreutils, grep
URL: http://www.tcsh.org/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, automake, ncurses-devel, gettext-devel

%description
Tcsh is an enhanced but completely compatible version of csh, the C
shell.  Tcsh is a command language interpreter which can be used both
as an interactive login shell and as a shell script command processor.
Tcsh includes a command line editor, programmable word completion,
spelling correction, a history mechanism, job control and a C language
like syntax.

%prep
%setup -q -n %{name}-%{version}.00
%patch1 -p1 -b .closem
%patch2 -p1 -b .tinfo
%patch3 -p1 -b .unprintable
%patch4 -p1 -b .hist-sub
%patch6 -p1 -b .ca-color
%patch7 -p1 -b .set
%patch8 -p1 -b .syntax
%patch9 -p1 -b .memoryuse
%patch11 -p1 -b .order
%patch12 -p1 -b .rs-color
%patch13 -p1 -b .mh-color
%patch15 -p1 -b .printexitvalue
%patch16 -p1 -b .testsuite
%patch17 -p1 -b .negative_jobs
%patch21 -p1 -b .dont-set-empty-remotehost
%patch22 -p1 -b .dont-print-history-on-verbose
%patch23 -p1 -b .extra-fork
%patch24 -p1 -b .bz607368
%patch25 -p1 -b .child-kill-hang
%patch26 -p1 -b .variable-names
%patch30 -p1 -b .handle-signals-before-flush
%patch31 -p1 -b .history-file-locking
%patch33 -p1 -b .reverse-history-handling-in-loops
%patch34 -p1 -b .sigint-while-waiting-for-child
%patch35 -p1 -b .sysmalloc
%patch36 -p1 -b .wait-hang
%patch37 -p1 -b .if-statement-parsing
%patch38 -p1 -b .backport-of-anyerror-variable
%patch39 -p1 -b .tcsh_posix_status-variable-added
%patch40 -p1 -b .use-stderr-upon-error
%patch41 -p1 -b .source-memory-leak
%patch42 -p1 -b .handle-interrupt-in-eval
%patch43 -p1 -b .wide-characters-print
%patch44 -p1 -b .use-long-long-for-calculations
%patch45 -p1 -b .quote-backslashes-properly

for i in Fixes WishList; do
 iconv -f iso-8859-1 -t utf-8 "$i" > "${i}_" && \
 touch -r "$i" "${i}_" && \
 mv "${i}_" "$i"
done

%build
# For tcsh-6.14.00-tinfo.patch
autoreconf
%configure --without-hesiod
make %{?_smp_mflags} all
make %{?_smp_mflags} -C nls catalogs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1 ${RPM_BUILD_ROOT}%{_bindir}
install -p -m 755 tcsh ${RPM_BUILD_ROOT}%{_bindir}/tcsh
install -p -m 644 tcsh.man ${RPM_BUILD_ROOT}%{_mandir}/man1/tcsh.1
ln -sf tcsh ${RPM_BUILD_ROOT}%{_bindir}/csh
ln -sf tcsh.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/csh.1

while read lang language ; do
	dest=${RPM_BUILD_ROOT}%{_datadir}/locale/$lang/LC_MESSAGES
	if test -f tcsh.$language.cat ; then
		mkdir -p $dest
		install -p -m 644 tcsh.$language.cat $dest/tcsh
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/tcsh"
	fi
done > tcsh.lang << _EOF
de german
el greek
en C
es spanish
et et
fi finnish
fr french
it italian
ja ja
pl pl
ru russian
uk ukrainian
_EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
 echo "%{_bindir}/tcsh" >> /etc/shells
 echo "%{_bindir}/csh"	>> /etc/shells
else
 grep -q '^%{_bindir}/tcsh$' /etc/shells || \
 echo "%{_bindir}/tcsh" >> /etc/shells
 grep -q '^%{_bindir}/csh$'  /etc/shells || \
 echo "%{_bindir}/csh"	>> /etc/shells
fi

%postun
if [ ! -x %{_bindir}/tcsh ]; then
 grep -v '^%{_bindir}/tcsh$'  /etc/shells | \
 grep -v '^%{_bindir}/csh$' > /etc/shells.rpm && \
 mv /etc/shells.rpm /etc/shells
fi

%files -f tcsh.lang
%defattr(-,root,root,-)
%doc Copyright BUGS FAQ Fixes NewThings WishList complete.tcsh README
%{_bindir}/tcsh
%{_bindir}/csh
%{_mandir}/man1/*.1*

%changelog
* Tue Jul 19 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-35.el6_8.1
- fix regression with 'jobs' builtin output not going to stdout (bug #1357127)
- fix several regressions in tcsh-6.17.00-quote-backslashes-properly.patch (bug #1357126)

* Sun Mar 20 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-35
- quote backslashes properly to preserve them in `...` expressions
  Resolves: #1301857

* Fri Jan 15 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-34
- use the 'long long' type (64 bits) for the internal calculations
  Resolves: #1298483

* Fri Jan 08 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-33
- fix the issues with wide characters printing while using LANG=C
  Resolves: #717367

* Tue Dec 15 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-32
- handle the ^C interrupt correctly when using the 'eval' built-in command
  Resolves: #1219923

* Thu Dec 10 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-31
- fix of memory leak when using the 'source' built-in command
  Resolves: #1134132

* Mon Dec 07 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-30
- print error message on stderr (instead of stdout)
  Resolves: #1019321

* Tue Nov 24 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-29
- our initial $tcsh_posix_status variable added for backward compatibility
  Resolves: #1256653

* Mon Nov 23 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-28
- upstream's $anyerror variable backported
  Related: #1256653

* Wed Nov 18 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-27
- spec file updated for build to include the Copyright file (#1186799)

* Fri Oct 30 2015 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 6.17-26
- fix of the 'if' statement parsing (#1231097)

* Tue Jan 20 2015 Pavel Raiskup <praiskup@redhat.com> - 6.17-25
- fix 'wait' built-in hang (#1181680)

* Thu Dec 13 2012 Roman Kollar <rkollar@redhat.com> 6.17-24
- Use system malloc
  Resolves: #769157

* Wed Dec 12 2012 Roman Kollar <rkollar@redhat.com> 6.17-23
- Fix tcsh being interruptible while waiting for child process
  Resolves: #884937

* Fri Oct 12 2012 Roman Kollar <rkollar@redhat.com> 6.17-22
- Fixed .history patch issue breaking upstream multibyte tests
  Resolves: #821796
- Revert history handling in loops
  Resolves: #814069

* Wed Sep 19 2012 Roman Kollar <rkollar@redhat.com> 6.17-21
- Fix dosource() calls after history file locking patch, requested release number bump
  Resolves: #847102

* Thu May 10 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-19
- Revert srcfile behaviour to return backward-compatible error codes (#658074)

* Thu May 03 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-18
- Fix several extra warnings breaking the upstream testsuite (#658074)

* Fri Mar 23 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-17
- Fix .history patch issues when tcsh runs in verbose mode (#658074)

* Fri Feb 20 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-16
- Revert exit status regression with it's opt-out variable $anyerror,
  added by "Fix status of pipelined/backquoted/list of commands" and
  opt-in the POSIX-like exit status behaviour by $status_posix_value
  variable instead (#784510)

* Thu Feb 16 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-15
- Handle pending signals before flush so that the the .history file
  does not get truncated
- Implement file locking using shared readers, exclusive writer
  to prevent any .history file data corruption

* Wed Oct 19 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-14
- Remove obsolete glob-automount patch; the issue should have been
  resolved (and is now resolved) in glibc posix/glob.c (#684063)

* Thu Aug 11 2011 Jan Kaluza <jkaluza@redhat.com> - 6.17-13
- Do not dereference null pointer in cwd
  Resolves: #700309
- Exit when child killed
  Resolves: #690356
- Do not allow variable names beginning with number
  Resolves: #672592
- Fix status of pipelined/backquoted/list of commands
  Resolves: #658190
- Fix unused res variable in sh.glob.c
  Resolves: #684063

* Mon Jan 31 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-12
- Remove extra fork when tcsh processes backquotes
  Resolves: #673556

* Fri Jan 28 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-11
- Modify verbose patch to match with upstream (don't print on history -S)
  Resolves: #658171

* Wed Jan 26 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-10
- Fix error message on exit
  Resolves: #658171

* Mon Jan 24 2011 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 6.17-9
- Don't set $REMOTEHOST on the local machine
  Resolves: #669176
- Don't print history in verbose mode
  Resolves: #658171

* Mon Jun 21 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-8
- Fix negative number of jobs with %%j formatting parameter in prompt

* Wed Apr 14 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-7
- Fix testsuite

* Wed Apr  7 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-6
- Fix tcsh obeys printexitvalue for back-ticks

* Mon Mar  1 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-5
- Ship README file

* Wed Nov  4 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-4
- Fix tcsh globbing causing bad automount

* Wed Aug 26 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-3
- Add new colorls variable
  Resolves: #518808

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.17-1
- Update to tcsh-6.17.00

* Thu Apr 30 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.16-1
- Update to tcsh-6.16.00
- Merge Review (fix License, add BUGS and WishList to documentation, convert Fixes and
  WishList to UTF-8, remove root checking from buildroot cleaning, preserve timestamps,
  use smp_flags, remove unused patches, improve postun script and minor fix to %%files)
  Resolves: #226483

* Mon Mar  2 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-8
- Fix tcsh needs to know about new colorls variables
  Resolves: #487783

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-6
- Fix UTF-8 Japanese character is garbled in tcsh script in
  a certain situation
  Related: #453785
- Fix calculation order of operators description in tcsh manpage
  Related: #442536
- Fix strings which begin with '0' are not recognized as octal numbers
  Related: #438109
- Fix memoryuse description in tcsh manpage
  Related: #437095
- Fix tcsh scripts with multiple case statement with end keywords
  break with error
  Related: #436956
- Fix description of builtin command 'set' in tcsh manpage
  Related: #430459

* Fri Aug 29 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-5
- Rediffed all patches to work with patch --fuzz=0
- Let tcsh know 'ca' colorls variable
  Resolves: #458716

* Fri Feb 29 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-4
- Fix '\' can not be used to quote all delimiters
  Related: #435421
- Fix $name[selector] should fail when any number of 'selector' is out of range
  Related: #435398

* Mon Feb 11 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-3
- Fix Buildroot

* Fri Jan 18 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-2
- Rebuild

* Mon Aug 27 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.15-1
- Update to tcsh-6.15.00
- Fix license
- Add gettext-devel to BuildRequires (AM_ICONV)

* Wed Apr 25 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 6.14-16
- Fix floating exception in print_by_column() with unprintable characters
  (#233525)

* Mon Feb 26 2007 Miloslav Trmac <mitr@redhat.com> - 6.14-15
- Fix License:
  Related: #226483.

* Mon Feb 12 2007 Miloslav Trmac <mitr@redhat.com> - 6.14-14
- Link to libtinfo instead of libncurses

* Thu Nov 30 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-13
- Link to ncurses instead of libtermcap
- Fix some rpmlint warnings

* Tue Sep 26 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-12
- Fix error handling in tcsh-6.14.00-wide-seeks.patch

* Sat Sep  9 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-11
- Fix an unlikely crash on startup (#188279)

* Wed Aug 16 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-10
- Fix an uninitialized variable causing stack corruption (#197968)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.14-9.1
- rebuild

* Mon Jul 10 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-9
- Fix seeking over multibyte characters (#195972)
- Don't ship obsolete eight-bit.txt

* Thu Mar 23 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-8
- Backport a patch to ignore LS_COLOR codes introduced in newer coreutils
  (#186037)

* Sat Mar 18 2006 Miloslav Trmac <mitr@redhat.com> - 6.14-7
- Fix a crash when reading scripts with multibyte characters (#183267)
- Block SIGINT while waiting for children (#177366)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.14-5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6.14-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Aug  5 2005 Miloslav Trmac <mitr@redhat.com> - 6.14-5
- Fix EOF handling in $< (#165095, patch by s_h_o_@hotmail.co.jp)

* Thu Jul  7 2005 Miloslav Trmac <mitr@redhat.com> - 6.14-3
- Fix -n (#162187)

* Mon Jun 20 2005 Miloslav Trmac <mitr@redhat.com> - 6.14-2
- Backport a column width calculation bugfix (#160760)

* Fri Mar 25 2005 Miloslav Trmac <mitr@redhat.com> - 6.14-1
- Update to tcsh-6.14.00

* Sat Mar  5 2005 Miloslav Trmac <mitr@redhat.com> - 6.13-13
- Rebuild with gcc 4

* Fri Feb 25 2005 Miloslav Trmac <mitr@redhat.com> - 6.13-12
- Don't ship the HTML documentation (generated from the man page, contains
  also a copy of the man page)

* Sun Jan 30 2005 Miloslav Trmac <mitr@redhat.com> - 6.13-11
- Fix the previous patch, handle a missed case (#146330)

* Sat Jan 15 2005 Miloslav Trmac <mitr@redhat.com> - 6.13-10
- Avoid reusing iconv_catgets' static buffer (#145177, #145195)

* Tue Sep 21 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-9
- Fix invalid argument to xprintf () (#133129)

* Wed Sep 15 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-8
- Fix $HOSTTYPE and $MACHTYPE for ppc64 and s390x, this time for sure

* Wed Sep 15 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-7
- Define $HOSTTYPE and $MACHTYPE for ppc64 and s390 (#115531),
  I hope that finally covers all architectures.

* Wed Sep 15 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-6
- Define $HOSTTYPE and $MACHTYPE also on IA-64 and s390x (#115531)
- Don't close sockets to avoid file descriptor conflits with nss_ldap (#112453)

* Tue Sep 14 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-5
- Fix HTML documentation generation, second attempt (#60664)
- Set dspmbyte using nl_langinfo(CODESET) if possible, should cover all
  cases where lang.csh was correctly setting dspmbyte (#89549)

* Wed Sep  8 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-4
- Remove unneeded patches

* Thu Aug 26 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-3
- Check for SIGWINCH more often (from tcsh-6.13.01, #130941)

* Wed Aug 18 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-2
- Make comparisons for ranges in bracket expressions symmetric (#59493)
- Run perl2html with LC_ALL=C to workaround what seems to be a perl bug
  (#60664)
- Define $HOSTTYPE and $MACHTYPE on x86_64 (#115531)
- Fix setting of O_LARGEFILE (#122558)

* Tue Aug 17 2004 Miloslav Trmac <mitr@redhat.com> - 6.13-1
- Update to tcsh-6.13.00
- Fix charset headers in some of the translations
- Convert translated messages to LC_CTYPE locale
- Fix automatic dspmbyte setting

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Nalin Dahyabhai <nalin@redhat.com> 6.12-7
- remove declaration of setpgrp() which conflicts with libc's (#115185)

* Fri Nov 21 2003 Nalin Dahyabhai <nalin@redhat.com> 6.12-6
- add missing buildprereqs on groff, libtermcap-devel (#110599)

* Tue Jul  8 2003 Nalin Dahyabhai <nalin@redhat.com>
- update URL

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 05 2002 Elliot Lee <sopwith@redhat.com> 6.12-3
- Merge changes from 8.0-hammer

* Tue Nov 19 2002 Nalin Dahyabhai <nalin@redhat.com> 6.12-3
- rebuild

* Thu Aug 08 2002 Phil Knirsch <pknirsch@redhat.com> 6.12-2
- Added csh.1 symlink to manpages.

* Tue Jun  4 2002 Nalin Dahyabhai <nalin@redhat.com> 6.11-1
- update to 6.11

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 31 2002 Bill Nottingham <notting@redhat.com>
- rebuild in new env

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Mar 28 2001 Akira TAGOH <tagoh@redhat.com> 6.10-5
- Fixed check locale.

* Tue Feb  6 2001 Adrian Havill <havill@redhat.com>
- use <time.h> instead of <sys/time.h> for pickier lib (#25935)
- allow arguments for login shells (#19926)

* Thu Nov 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 6.10.00 to fix here-script vulnerability

* Wed Sep 18 2000 Adrian Havill <havill@redhat.com>
- fix catalog locale dirname for Japanese

* Thu Jun 15 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- add locale support (#10345).

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies

* Thu Jan 27 2000 Jeff Johnson <jbj@redhat.com>
- append entries to spanking new /etc/shells.

* Mon Jan 10 2000 Jeff Johnson <jbj@redhat.com>
- update to 6.09.
- fix strcoll oddness (#6000, #6244, #6398).

* Sat Sep 25 1999 Michael K. Johnson <johnsonm@redhat.com>
- fix $shell by using --bindir

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Feb 24 1999 Cristian Gafton <gafton@redhat.com>
- patch for using PATH_MAX instead of some silly internal #defines for
  variables that handle filenames.

* Fri Nov  6 1998 Jeff Johnson <jbj@redhat.com>
- update to 6.08.00.

* Fri Oct 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 6.07.09 from the freebsd
- security fix

* Wed Aug  5 1998 Jeff Johnson <jbj@redhat.com>
- use -ltermcap so that /bin/tcsh can be used in single user mode w/o /usr.
- update url's

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 6.07; added BuildRoot
- cleaned up the spec file; fixed source url

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- added termios hacks for new glibc
- added /bin/csh to file list

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
 - Provides csh, adds and removes /bin/csh from /etc/shells if csh package
isn't installed.
