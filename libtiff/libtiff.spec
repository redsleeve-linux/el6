Summary: Library of functions for manipulating TIFF format image files
Name: libtiff
Version: 3.9.4
Release: 21%{?dist}

License: libtiff
Group: System Environment/Libraries
URL: http://www.remotesensing.org/libtiff/

Source: ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz
Patch1: libtiff-acversion.patch
Patch2: libtiff-mantypo.patch
Patch3: libtiff-scanlinesize.patch
Patch4: libtiff-getimage-64bit.patch
Patch5: libtiff-ycbcr-clamp.patch
Patch6: libtiff-3samples.patch
Patch7: libtiff-subsampling.patch
Patch8: libtiff-unknown-fix.patch
Patch9: libtiff-checkbytecount.patch
Patch10: libtiff-tiffdump.patch
Patch11: libtiff-CVE-2011-0192.patch
Patch12: libtiff-CVE-2011-1167.patch
Patch13: libtiff-CVE-2009-5022.patch
Patch14: libtiff-CVE-2012-1173.patch
Patch15: libtiff-CVE-2012-2088.patch
Patch16: libtiff-CVE-2012-2113.patch
Patch17: libtiff-CVE-2012-3401.patch
Patch18: libtiff-CVE-2012-4447.patch
Patch19: libtiff-CVE-2012-4564.patch
Patch20: libtiff-CVE-2012-5581.patch
Patch21: libtiff-tiffinfo-exif.patch
Patch22: libtiff-printdir-width.patch
Patch23: libtiff-CVE-2013-1960.patch
Patch24: libtiff-CVE-2013-1961.patch
Patch25: libtiff-CVE-2013-4231.patch
Patch26: libtiff-CVE-2013-4232.patch
Patch27: libtiff-CVE-2013-4244.patch
Patch28: libtiff-CVE-2013-4243.patch
Patch29: libtiff-CVE-2014-9330.patch
Patch30: libtiff-CVE-2014-8127.patch
Patch31: libtiff-CVE-2014-8129.patch
Patch32: libtiff-CVE-2014-8130.patch
Patch33: libtiff-CVE-2014-9655.patch
Patch34: libtiff-CVE-2015-1547_8784.patch
Patch35: libtiff-CVE-2015-8781.patch
Patch36: libtiff-CVE-2015-8683_8665.patch
Patch37: libtiff-CVE-2015-7554.patch
Patch38: libtiff-CVE-2015-8668.patch
Patch39: libtiff-CVE-2016-3632.patch
Patch40: libtiff-CVE-2016-3945.patch
Patch41: libtiff-CVE-2016-3990.patch
Patch42: libtiff-CVE-2016-3991.patch
Patch43: libtiff-CVE-2016-5320.patch
Patch44: libtiff-CVE-2016-9533_9534_9536_9537.patch
Patch45: libtiff-CVE-2016-9535.patch
Patch46: libtiff-CVE-2016-9540.patch
Patch47: libtiff-CVE-2016-5652.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel libjpeg-devel
BuildRequires: libtool automake autoconf

%global LIBVER %(echo %{version} | cut -f 1-2 -d .)

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary: Development tools for programs which will use the libtiff library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and documentation necessary for
developing programs which will manipulate TIFF format image files
using the libtiff library.

If you need to develop programs which will manipulate TIFF format
image files, you should install this package.  You'll also need to
install the libtiff package.

%package static
Summary: Static TIFF image format file library
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The libtiff-static package contains the statically linkable version of libtiff.
Linking to static libraries is discouraged for most applications, but it is
necessary for some boot packages.

%prep
%setup -q -n tiff-%{version}

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
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1

# Use build system's libtool.m4, not the one in the package.
rm -f libtool.m4

libtoolize --force  --copy
aclocal -I . -I m4
automake --add-missing --copy
autoconf
autoheader

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH make check

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# remove what we didn't want installed
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f html/man/tiffgt.1.html

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f html/man/sgi2tiff.1.html
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1
rm -f html/man/tiffsv.1.html

# multilib header hack
# we only apply this to known Red Hat multilib arches, per bug #233091
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv $RPM_BUILD_ROOT%{_includedir}/tiffconf.h \
     $RPM_BUILD_ROOT%{_includedir}/tiffconf-$wordsize.h

  cat >$RPM_BUILD_ROOT%{_includedir}/tiffconf.h <<EOF
#ifndef TIFFCONF_H_MULTILIB
#define TIFFCONF_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "tiffconf-32.h"
#elif __WORDSIZE == 64
# include "tiffconf-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

# don't include documentation Makefiles, they are a multilib hazard
find html -name 'Makefile*' | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT README RELEASE-DATE VERSION
%{_bindir}/*
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,0755)
%doc TODO ChangeLog html
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%{_mandir}/man3/*

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%changelog
* Fri Jan 20 2017 Nikola Forró <nforro@redhat.com> - 3.9.4-21
- Fix patch for CVE-2016-5652
- Related: #1412078

* Wed Jan 18 2017 Nikola Forró <nforro@redhat.com> - 3.9.4-20
- Fix CWE-476 defect found by covscan
- Related: #1412078

* Fri Jan 13 2017 Nikola Forró <nforro@redhat.com> - 3.9.4-19
- Add patches for CVEs:
- CVE-2016-9533 CVE-2016-9534 CVE-2016-9535
- CVE-2016-9536 CVE-2016-9537 CVE-2016-9540
- CVE-2016-5652
- Resolves: #1412078

* Wed Jul 20 2016 Nikola Forró <nforro@redhat.com> - 3.9.4-18
- Update patch for CVE-2014-8127
- Related: #1335099

* Wed Jul 20 2016 Nikola Forró <nforro@redhat.com> - 3.9.4-17
- Fix patches for CVE-2016-3990 and CVE-2016-5320
- Related: #1335099

* Wed Jul 20 2016 Nikola Forró <nforro@redhat.com> - 3.9.4-16
- Add patches for CVEs:
- CVE-2016-3632 CVE-2016-3945 CVE-2016-3990
- CVE-2016-3991 CVE-2016-5320
- Related: #1335099

* Wed Jul 20 2016 Nikola Forró <nforro@redhat.com> - 3.9.4-15
- Update patch for CVE-2014-8129
- Related: #1335099

* Tue Jul 19 2016 Nikola Forró <nforro@redhat.com> - 3.9.4-14
- Merge previously released fixes for CVEs:
- CVE-2013-1960 CVE-2013-1961 CVE-2013-4231
- CVE-2013-4232 CVE-2013-4243 CVE-2013-4244
- Resolves: #1335099

* Mon Apr 25 2016 Petr Hracek <phracek@redhat.com> - 3.9.4-13
- Patch typos in CVE-2014-8127
- Related: #1299919

* Mon Apr 25 2016 Petr Hracek <phracek@redhat.com> - 3.9.4-12
- Fix CVE-2014-8127 and CVE-2015-8668 patches
- Related: #1299919

* Wed Mar 09 2016 Petr Hracek <phracek@redhat.com> - 3.9.4-11
- Fixed patches on preview CVEs
- Related: #1299919

* Tue Feb 16 2016 Petr Hracek <phracek@redhat.com> - 3.9.4-10
- This resolves several CVEs
- CVE-2014-8127, CVE-2014-8129, CVE-2014-8130
- CVE-2014-9330, CVE-2014-9655, CVE-2015-8781
- CVE-2015-8784, CVE-2015-1547, CVE-2015-8683
- CVE-2015-8665, CVE-2015-7554, CVE-2015-8668
- Resolves: #1299919

* Thu Dec 13 2012 Tom Lane <tgl@redhat.com> 3.9.4-9
- Still more fixes to make test case for CVE-2012-5581 work on all platforms
Resolves: #885311

* Tue Dec 11 2012 Tom Lane <tgl@redhat.com> 3.9.4-8
- Fix incomplete patch for CVE-2012-3401
- Add libtiff-tiffinfo-exif.patch so that our test case for CVE-2012-5581 works
  with pre-4.0.2 libtiff
Resolves: #885311

* Mon Dec 10 2012 Tom Lane <tgl@redhat.com> 3.9.4-7
- Add fixes for CVE-2012-3401, CVE-2012-4447, CVE-2012-4564, CVE-2012-5581
Resolves: #885311

* Wed Jun 27 2012 Tom Lane <tgl@redhat.com> 3.9.4-6
- Add fixes for CVE-2012-2088, CVE-2012-2113
Resolves: #835749

* Mon Apr  2 2012 Tom Lane <tgl@redhat.com> 3.9.4-5
- Add fix for CVE-2012-1173
Resolves: #CVE-2012-1173

* Wed Apr 13 2011 Tom Lane <tgl@redhat.com> 3.9.4-4
- Add fix for CVE-2009-5022
Resolves: #696144

* Fri Mar 18 2011 Tom Lane <tgl@redhat.com> 3.9.4-3
- Fix incorrect fix for CVE-2011-0192
Resolves: #688830
- Add fix for CVE-2011-1167
Resolves: #688743

* Wed Feb 23 2011 Tom Lane <tgl@redhat.com> 3.9.4-2
- Add fix for CVE-2011-0192
Resolves: #679299

* Mon Jun 28 2010 Tom Lane <tgl@redhat.com> 3.9.4-1
- Update to libtiff 3.9.4, for numerous bug fixes including fixes for
  CVE-2010-1411, CVE-2010-2065, CVE-2010-2067, CVE-2010-2233
Resolves: #606708, #588784, #589034, #603024
- Add fixes for multiple SIGSEGV problems
Resolves: #603081, #603699, #603703

* Tue Jan 12 2010 Tom Lane <tgl@redhat.com> 3.9.2-3
- Sync with F-12, including:
- Update to libtiff 3.9.2; stop carrying a lot of old patches
- Apply Warmerdam's partial fix for bug #460322 ... better than nothing.
- Use build system's libtool instead of what package contains;
  among other cleanup this gets rid of unwanted rpath specs in executables
- add sparc/sparc64 to multilib header support
- Apply Adam Goode's fix for Warmerdam's fix
Resolves: #552360
Resolves: #533353
- Add some defenses to prevent tiffcmp from crashing on downsampled JPEG
  images; this isn't enough to make it really work correctly though

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.8.2-15.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Tom Lane <tgl@redhat.com> 3.8.2-14
- Fix buffer overrun risks caused by unchecked integer overflow (CVE-2009-2347)
Related: #510041

* Wed Jul  1 2009 Tom Lane <tgl@redhat.com> 3.8.2-13
- Fix some more LZW decoding vulnerabilities (CVE-2009-2285)
Related: #507465
- Update upstream URL

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Tom Lane <tgl@redhat.com> 3.8.2-11
- Fix LZW decoding vulnerabilities (CVE-2008-2327)
Related: #458674
- Use -fno-strict-aliasing per rpmdiff recommendation

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.8.2-10
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Tom Lane <tgl@redhat.com> 3.8.2-9
- Update License tag
- Rebuild to fix Fedora toolchain issues

* Thu Jul 19 2007 Tom Lane <tgl@redhat.com> 3.8.2-8
- Restore static library to distribution, in a separate -static subpackage
Resolves: #219905
- Don't apply multilib header hack to unrecognized architectures
Resolves: #233091
- Remove documentation for programs we don't ship
Resolves: #205079
Related: #185145

* Tue Jan 16 2007 Tom Lane <tgl@redhat.com> 3.8.2-7
- Remove Makefiles from the shipped /usr/share/doc/html directories
Resolves: bz #222729

* Tue Sep  5 2006 Jindrich Novy <jnovy@redhat.com> - 3.8.2-6
- fix CVE-2006-2193, tiff2pdf buffer overflow (#194362)
- fix typo in man page for tiffset (#186297)
- use %%{?dist}

* Mon Jul 24 2006 Matthias Clasen <mclasen@redhat.com>
- Fix several vulnerabilities (CVE-2006-3460 CVE-2006-3461
  CVE-2006-3462 CVE-2006-3463 CVE-2006-3464 CVE-2006-3465)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.8.2-4.1
- rebuild

* Fri Jun  2 2006 Matthias Clasen <mclasen@redhat.com> - 3.8.2-3
- Fix multilib conflict

* Thu May 25 2006 Matthias Clasen <mclasen@redhat.com> - 3.8.2-3
- Fix overflows in tiffsplit

* Wed Apr 26 2006 Matthias Clasen <mclasen@redhat.com> - 3.8.2-2
- Drop tiffgt to get rid of the libGL dependency (#190768)

* Wed Apr 26 2006 Matthias Clasen <mclasen@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.7.4-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.7.4-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 16 2005 Matthias Clasen <mclasen@redhat.com> 3.7.4-3
- Don't ship static libs

* Fri Nov 11 2005 Matthias Saou <http://freshrpms.net/> 3.7.4-2
- Remove useless explicit dependencies.
- Minor spec file cleanups.
- Move make check to %%check.
- Add _smp_mflags.

* Thu Sep 29 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4
- Drop upstreamed patches

* Wed Jun 29 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.2-1
- Update to 3.7.2
- Drop upstreamed patches

* Fri May  6 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.1-6
- Fix a stack overflow

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.1-5
- Don't use mktemp

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.1-4
- Rebuild with gcc4

* Wed Jan  5 2005 Matthias Clasen <mclasen@redhat.com> - 3.7.1-3
- Drop the largefile patch again
- Fix a problem with the handling of alpha channels
- Fix an integer overflow in tiffdump (#143576)

* Wed Dec 22 2004 Matthias Clasen <mclasen@redhat.com> - 3.7.1-2
- Readd the largefile patch (#143560)

* Wed Dec 22 2004 Matthias Clasen <mclasen@redhat.com> - 3.7.1-1
- Upgrade to 3.7.1
- Remove upstreamed patches
- Remove specfile cruft
- make check

* Thu Oct 14 2004 Matthias Clasen <mclasen@redhat.com> 3.6.1-7
- fix some integer and buffer overflows (#134853, #134848)

* Tue Oct 12 2004 Matthias Clasen <mclasen@redhat.com> 3.6.1-6
- fix http://bugzilla.remotesensing.org/show_bug.cgi?id=483

* Mon Sep 27 2004 Rik van Riel <riel@redhat.com> 3.6.1-4
- compile using RPM_OPT_FLAGS (bz #133650)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 20 2004 Matthias Clasen <mclasen@redhat.com> 3.6.1-2
- Fix and use the makeflags patch

* Wed May 19 2004 Matthias Clasen <mclasen@redhat.com> 3.6.1-1
- Upgrade to 3.6.1
- Adjust patches
- Don't install tiffgt man page  (#104864)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- really add symlink to shared lib by running ldconfig at compile time

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Oct 09 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- link shared lib against -lm (Jakub Jelinek)

* Thu Sep 25 2003 Jeremy Katz <katzj@redhat.com> 3.5.7-13
- rebuild to fix gzipped file md5sum (#91281)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 3.5.7-11
- Fixed rebuild problems.

* Tue Feb 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlink to shared lib

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 3.5.7-8
- rebuild on all arches

* Mon Aug 19 2002 Phil Knirsch <pknirsch@redhat.com> 3.5.7-7
- Added LFS support (#71593)

* Tue Jun 25 2002 Phil Knirsch <pknirsch@redhat.com> 3.5.7-6
- Fixed wrong exit code of tiffcp app (#67240)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 15 2002 Phil Knirsch <pknirsch@redhat.com>
- Fixed segfault in fax2tiff tool (#64708).

* Mon Feb 25 2002 Phil Knirsch <pknirsch@redhat.com>
- Fixed problem with newer bash versions setting CDPATH (#59741)

* Tue Feb 19 2002 Phil Knirsch <pknirsch@redhat.com>
- Update to current release 3.5.7

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Aug 28 2001 Phil Knirsch <phil@redhat.de>
- Fixed ia64 problem with tiffinfo. Was general 64 bit arch problem where s390x
  and ia64 were missing (#52129).

* Tue Jun 26 2001 Philipp Knirsch <pknirsch@redhat.de>
- Hopefully final symlink fix

* Thu Jun 21 2001 Than Ngo <than@redhat.com>
- add missing libtiff symlink

* Fri Mar 16 2001 Crutcher Dunnavant <crutcher@redhat.com>
- killed tiff-to-ps.fpi filter

* Wed Feb 28 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed missing devel version dependancy.

* Tue Dec 19 2000 Philipp Knirsch <pknirsch@redhat.de>
- rebuild

* Mon Aug  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- added a tiff-to-ps.fpi filter for printing

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply Peter Skarpetis's fix for the 32-bit conversion

* Mon Jul  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- make man pages non-executable (#12811)

* Mon Jun 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove CVS repo info from data directories

* Thu May 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix build rooting
- fix syntax error in configure script
- move man pages to {_mandir}

* Wed May 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for an errata release

* Wed Mar 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 3.5.5, which integrates our fax2ps fixes and the glibc fix

* Tue Mar 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix fax2ps swapping height and width in the bounding box

* Mon Mar 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- move man pages from devel package to the regular one
- integrate Frank Warmerdam's fixed .fax handling code (keep until next release
  of libtiff)
- fix fax2ps breakage (bug #8345)

* Sat Feb 05 2000 Nalin Dahyabhai <nalin@redhat.com>
- set MANDIR=man3 to make multifunction man pages friendlier

* Mon Jan 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix URLs

* Fri Jan 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- link shared library against libjpeg and libz

* Tue Jan 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable zip and jpeg codecs
- change defattr in normal package to 0755
- add defattr to -devel package

* Wed Dec 22 1999 Bill Nottingham <notting@redhat.com>
- update to 3.5.4

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Wed Jan 13 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against fixed jpeg libs (libjpeg-6b)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- new version to replace the one from libgr
- patched for glibc
- added shlib support
