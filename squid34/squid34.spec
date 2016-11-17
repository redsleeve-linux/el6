%define __perl_requires %{SOURCE98}

Name:     squid34
Version:  3.4.14
Release:  9%{?dist}.3
Summary:  The Squid proxy caching server
Epoch:    7
# See CREDITS for breakdown of non GPLv2+ code
License:  GPLv2+ and (LGPLv2+ and MIT and BSD and Public Domain)
Group:    System Environment/Daemons
URL:      http://www.squid-cache.org
Source0:  http://www.squid-cache.org/Versions/v3/3.4/squid-%{version}.tar.xz
Source1:  http://www.squid-cache.org/Versions/v3/3.4/squid-%{version}.tar.xz.asc
Source2:  squid.init
Source3:  squid.logrotate
Source4:  squid.sysconfig
Source5:  squid.pam
Source6:  squid.nm
Source98: perl-requires-squid.sh

Patch201: squid-3.1.0.9-config.patch
Patch202: squid-3.1.0.9-location.patch
Patch204: squid-3.0.STABLE1-perlpath.patch
Patch208: squid-3.0.STABLE7-from_manpg.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=639365 (?)
# https://bugzilla.redhat.com/show_bug.cgi?id=666533 (?)
Patch209: squid-3.1.9-ltdl.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=720504
Patch214: squid-3.1.10-interc-http.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=959460
# https://bugzilla.redhat.com/show_bug.cgi?id=895526
# https://bugzilla.redhat.com/show_bug.cgi?id=844723
# https://bugzilla.redhat.com/show_bug.cgi?id=832484
Patch216: squid-3.1.10-NTLM-pass-through.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=833086
Patch220: squid-fips.patch
Patch221: squid34-3.4.14-ssl-helper.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1301102
Patch222: squid-3.3.8-segfault-reboot.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1301638
Patch223: squid-3.3.8-ftp.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1315662
Patch224: squid-3.3.8-le-looping.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1329126
Patch225: squid-CVE-2016-4051.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1329136
Patch226: squid-CVE-2016-4052.patch
# http://www.squid-cache.org/Advisories/SQUID-2016_7.txt
Patch227: squid-CVE-2016-4553.patch
# http://www.squid-cache.org/Advisories/SQUID-2016_8.txt
Patch228: squid-CVE-2016-4554.patch
# http://www.squid-cache.org/Advisories/SQUID-2016_9.txt
Patch229: squid-CVE-2016-4555.patch
# http://www.squid-cache.org/Advisories/SQUID-2016_9.txt
Patch230: squid-CVE-2016-4556.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: bash >= 2.0
Conflicts: squid
Requires(pre): shadow-utils
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service /sbin/chkconfig
Requires(postun): /sbin/service
# squid_ldap_auth and other LDAP helpers require OpenLDAP
BuildRequires: openldap-devel
# squid_pam_auth requires PAM development libs
BuildRequires: pam-devel
# SSL support requires OpenSSL
BuildRequires: openssl-devel
# squid_kerb_aut requires Kerberos development libs
BuildRequires: krb5-devel
# squid_session_auth requires DB4
BuildRequires: db4-devel
# ESI support requires Expat & libxml2
BuildRequires: expat-devel libxml2-devel
# TPROXY requires libcap, and also increases security somewhat
BuildRequires: libcap-devel
#ip_user helper requires
BuildRequires: gcc-c++
# eCAP and some other need libltdl
BuildRequires: libtool libtool-ltdl-devel
# make check - compat/TestPreCompiler
BuildRequires: cppunit-devel

%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.

Squid consists of a main server program squid, a Domain Name System
lookup program (dnsserver), a program for retrieving FTP data
(ftpget), and some management and client tools.

%prep
%setup -q -n squid-%{version}

%patch201 -p1
%patch202 -p1
%patch204 -p1
%patch208 -p1
%patch209 -p1
%patch214 -p1
%patch216 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1 -b .reboot-segfault
%patch223 -p1 -b .ftp
%patch224 -p1 -b .le-looping
%patch225 -p0 -b .CVE-2016-4051
%patch226 -p1 -b .CVE-2016-4052
%patch227 -p0 -b .CVE-2016-4553
%patch228 -p0 -b .CVE-2016-4554
%patch229 -p0 -b .CVE-2016-4555
%patch230 -p0 -b .CVE-2016-4556

%build
%ifarch sparcv9 sparc64 s390 s390x
   CXXFLAGS="$RPM_OPT_FLAGS -fPIE" \
   CFLAGS="$RPM_OPT_FLAGS -fPIE" \
%else
   CXXFLAGS="$RPM_OPT_FLAGS -fpie" \
   CFLAGS="$RPM_OPT_FLAGS -fpie" \
%endif
LDFLAGS="$RPM_LD_FLAGS -pie -Wl,-z,relro -Wl,-z,now"

%configure \
   --enable-internal-dns \
   --disable-strict-error-checking \
   --exec_prefix=/usr \
   --libexecdir=%{_libdir}/squid \
   --localstatedir=%{_var} \
   --datadir=%{_datadir}/squid \
   --sysconfdir=%{_sysconfdir}/squid \
   --with-logdir='$(localstatedir)/log/squid' \
   --with-pidfile='$(localstatedir)/run/squid.pid' \
   --disable-dependency-tracking \
   --enable-arp-acl \
   --enable-follow-x-forwarded-for \
   --enable-auth-basic="LDAP,MSNT,NCSA,PAM,SMB,POP3,RADIUS,SASL,getpwnam,NIS,MSNT-multi-domain" \
   --enable-auth-ntlm="smb_lm,fake" \
   --enable-auth-digest="file,LDAP,eDirectory" \
   --enable-auth-negotiate="kerberos" \
   --enable-external-acl-helpers="file_userip,LDAP_group,session,unix_group,wbinfo_group" \
   --enable-cache-digests \
   --enable-cachemgr-hostname=localhost \
   --enable-delay-pools \
   --enable-epoll \
   --enable-icap-client \
   --enable-ident-lookups \
   %ifnarch ppc64 ia64 x86_64 s390x aarch64
   --with-large-files \
   %endif
   --enable-linux-netfilter \
   --enable-referer-log \
   --enable-removal-policies="heap,lru" \
   --enable-snmp \
   --enable-ssl \
   --enable-storeio="aufs,diskd,ufs" \
   --enable-useragent-log \
   --enable-wccpv2 \
   --enable-esi \
   --enable-http-violations \
   --with-aio \
   --with-default-user="squid" \
   --with-filedescriptors=16384 \
   --with-dl \
   --with-openssl \
   --with-pthreads \
   --disable-arch-native

make \
	DEFAULT_SWAP_DIR='$(localstatedir)/spool/squid' \
	%{?_smp_mflags}

%check
make check
	
%install
rm -rf $RPM_BUILD_ROOT
make \
	DESTDIR=$RPM_BUILD_ROOT \
	install
echo "
#
# This is /etc/httpd/conf.d/squid.conf
#

ScriptAlias /Squid/cgi-bin/cachemgr.cgi %{_libdir}/squid/cachemgr.cgi

# Only allow access from localhost by default
<Location /Squid/cgi-bin/cachemgr.cgi>
 order allow,deny
 allow from localhost
 # Add additional allowed hosts as needed
 # allow from .example.com
</Location>" > $RPM_BUILD_ROOT/squid.httpd.tmp


mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/squid
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/squid
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/squid
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/squid
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/squid
install -m 644 $RPM_BUILD_ROOT/squid.httpd.tmp $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/squid.conf
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/dispatcher.d/20-squid
mkdir -p $RPM_BUILD_ROOT%{_var}/log/squid
mkdir -p $RPM_BUILD_ROOT%{_var}/spool/squid
chmod 644 contrib/url-normalizer.pl contrib/rredir.* contrib/user-agents.pl
iconv -f ISO88591 -t UTF8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog

# Move the MIB definition to the proper place (and name)
mkdir -p $RPM_BUILD_ROOT/usr/share/snmp/mibs
mv $RPM_BUILD_ROOT/usr/share/squid/mib.txt $RPM_BUILD_ROOT/usr/share/snmp/mibs/SQUID-MIB.txt

# squid.conf.documented is documentation. We ship that in doc/
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/squid/squid.conf.documented

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_bindir}/{RunAccel,RunCache}
rm -f $RPM_BUILD_ROOT/squid.httpd.tmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING COPYRIGHT README ChangeLog QUICKSTART src/squid.conf.documented
%doc contrib/url-normalizer.pl contrib/rredir.* contrib/user-agents.pl

%attr(755,root,root) %dir %{_libexecdir}/squid
%attr(755,root,root) %dir %{_sysconfdir}/squid
%attr(755,root,root) %dir %{_libdir}/squid
%attr(750,squid,squid) %dir %{_var}/log/squid
%attr(750,squid,squid) %dir %{_var}/spool/squid
%attr(750,squid,squid) %dir %{_var}/run/squid

%config(noreplace) %attr(644,root,root) %{_sysconfdir}/httpd/conf.d/squid.conf
%config(noreplace) %attr(640,root,squid) %{_sysconfdir}/squid/squid.conf
%config(noreplace) %attr(644,root,squid) %{_sysconfdir}/squid/cachemgr.conf
%config(noreplace) %{_sysconfdir}/squid/mime.conf
%config(noreplace) %{_sysconfdir}/squid/errorpage.css
%config(noreplace) %{_sysconfdir}/sysconfig/squid
%config(noreplace) %{_sysconfdir}/squid/msntauth.conf

# These are not noreplace because they are just sample config files
%config %{_sysconfdir}/squid/msntauth.conf.default
%config %{_sysconfdir}/squid/squid.conf.default
%config %{_sysconfdir}/squid/mime.conf.default
%config %{_sysconfdir}/squid/errorpage.css.default
%config %{_sysconfdir}/squid/cachemgr.conf.default
%config(noreplace) %{_sysconfdir}/pam.d/squid
%config(noreplace) %{_sysconfdir}/logrotate.d/squid

%dir %{_datadir}/squid
%attr(-,root,root) %{_datadir}/squid/errors
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/squid
%attr(755,root,root) %{_sysconfdir}/NetworkManager/dispatcher.d/20-squid
%{_datadir}/squid/icons
%{_sbindir}/squid
%{_bindir}/squidclient
%{_bindir}/purge
%{_mandir}/man8/*
%{_mandir}/man1/*
%{_libdir}/squid/*
%{_datadir}/snmp/mibs/SQUID-MIB.txt

%pre
if ! getent group squid >/dev/null 2>&1; then
  /usr/sbin/groupadd -g 23 squid
fi

if ! getent passwd squid >/dev/null 2>&1 ; then
  /usr/sbin/useradd -g 23 -u 23 -d /var/spool/squid -r -s /sbin/nologin squid >/dev/null 2>&1 || exit 1 
fi

for i in /var/log/squid /var/spool/squid ; do
        if [ -d $i ] ; then
                for adir in `find $i -maxdepth 0 \! -user squid`; do
                        chown -R squid:squid $adir
                done
        fi
done

exit 0

%post
/sbin/chkconfig --add squid

%preun
if [ $1 = 0 ] ; then
        service squid stop >/dev/null 2>&1
        rm -f /var/log/squid/*
        /sbin/chkconfig --del squid
fi

%postun
if [ "$1" -ge "1" ] ; then
        service squid condrestart >/dev/null 2>&1
fi

%triggerin -- samba-common
if ! getent group wbpriv >/dev/null 2>&1 ; then
  /usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :
fi
/usr/sbin/usermod -a -G wbpriv squid >/dev/null 2>&1 || \
    chgrp squid /var/cache/samba/winbindd_privileged >/dev/null 2>&1 || :

%changelog
* Mon May 09 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-9.3
- Resolves: #1334499 - CVE-2016-4554 CVE-2016-4555 CVE-2016-4556
  squid34: various flaws
- Resolves: #1334506 - CVE-2016-4553 squid34: squid: Cache poisoning
  issue in HTTP Request handling

* Fri Apr 29 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-9.2
- Related: #1330574 - CVE-2016-4051 CVE-2016-4052 CVE-2016-4053 CVE-2016-4054
  squid34: various flaws

* Fri Apr 29 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-9.1
- Resolves: #1330574 - CVE-2016-4051 CVE-2016-4052 CVE-2016-4053 CVE-2016-4054
  squid34: various flaws

* Thu Mar 31 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-9
- Resolves: #1322364 - squid fails to start in FIPS 140-2 mode

* Mon Mar 21 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-8
- Related: #1315662 - squid with digest auth on big endian
  systems start looping

* Wed Mar 09 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-7
- Resolves: #1315662 - squid with digest auth on big endian 
  systems start looping

* Tue Jan 26 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-6
- Resolves: #1301897 - missing /var/run/squid needed for smp mode

* Mon Jan 25 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-5
- Resolves: #1301638 - squid doesn't work with active ftp

* Mon Jan 25 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-4
- Resolves: #1301005 - insufficient check for running service
  in condrestart and try-restart actions

* Mon Jan 25 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-3
- Resolves: #1301020 - should BuildRequire: g++

* Mon Jan 25 2016 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-2
- Resolves: #1301102 - squid crashes by segfault when it reboots

* Tue Dec 08 2015 Luboš Uhliarik <luhliari@redhat.com> - 7:3.4.14-1
- Resolves: #1265328 - Add new version (3.4.14) of Squid proxy as
  new component
- removed old Resolves and Related tags from Changelog

* Mon May 25 2015 Luboš Uhliarik <luhliari@redhat.com> - 7:3.1.23-9
- removed unwanted changes in MIB file

* Fri May 22 2015 Luboš Uhliarik <luhliari@redhat.com> - 7:3.1.23-8
- fix init script typo

* Thu May 21 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-7
- squid crashes by segfault when it reboots

* Wed Apr 15 2015 Luboš Uhliarik <luhliari@redhat.com> - 7:3.1.23-6
- fix init script issue

* Wed Mar 18 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-5
- avoid rm -rf /*

* Thu Feb 12 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-4
- build with --enable-http-violations

* Thu Feb 12 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-3
- squid aborting at assert(isOpen(fd));

* Thu Feb 12 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-2
- squid: increase the threshold in c->locks assertion

* Wed Feb 11 2015 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.23-1
- rebase to squid-3.1.23

* Mon Dec 22 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-35
- When squid returns an ACL tag utilizing an external ACL,
  sometimes the incorrect tag is used for redirection

* Mon Dec 22 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-34
- service squid restart sometimes leaves duplicate
  processes

* Mon Dec 22 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-33
- Malformed ipv6 DNS reverse lookup

* Thu Dec 18 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-32
- (squid): xstrdup: tried to dup a NULL pointer!

* Tue Dec 09 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-31
- A monitoring program failed to load MIB modules because
  of wrong MIB files

* Tue Dec 02 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-30
- squid crashes by segfault when it reboots

* Mon Sep 01 2014 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-29
- CVE-2013-4115 buffer overflow when processing overly long DNS names

* Fri Aug 29 2014 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-28
- CVE-2014-3609 assertion failure in header processing

* Wed May 21 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-27
- CVE-2014-0128 squid: denial of service when using
  SSL-Bump

* Tue May 20 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-26
- issues with timeout on HTTPS connections

* Wed Apr 30 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-25
- extend basic auth memleak fix to other methods

* Mon Apr 28 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-24
- issues with timeout on HTTPS connections

* Wed Apr 09 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-23
- unexpanded macros in man page

* Wed Apr 09 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-22
- memory utilization of Squid becomes very large
- cachemgr.cgi doesn't work by default
- Init script: missing condrestart in Usage
- Child process of squid exited abnormally and generated core files
- assert(!fd_table[fd].closing()) failed in comm_write()

* Wed Apr 09 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-21
- squid assertion failed: c->locks < 65535

* Fri Jan 10 2014 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-20
- Squid getting abort in idnsReadVCHeader

* Wed Sep 18 2013 Pavel Šimerda <psimerda@redhat.com> - 7:3.1.10-19
- cachemgr.cgi crashes for authenticated connections.

* Thu Jun 20 2013 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-18
- Squid sends "Proxy-Connection: keepalive" in http GET 

* Tue Jun 11 2013 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-17
- Active mode FTP causes assertion failed

* Tue Jan 15 2013 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-16
- CVE-2012-5643: improved upstream patch

* Tue Jan 15 2013 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-15
- Squid delays on FQDNs that don't contains AAAA record

* Wed Dec 19 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-14
- CVE-2012-5643: patch

* Wed Dec 19 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-13
- CVE-2012-5643: DoS (excessive resource consumption)

* Thu Oct 4 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-12
- add configure directive --enable-internal-dns

* Thu Oct 4 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-11	
- Squid delays on FQDNs that don't contains AAAA record

* Thu Sep 13 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-10
- Client timeout uses server-side "read_timeout"
- Private md5 hash function does not comply FIPS
- Squid crashes by segfault when it reboots
- Squid userid is not added to wbpriv group
- Disable strict-error-checking on account of squid-fips.patch

* Fri Sep 07 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-9
- Squid incorrectly marks elements as stale

* Wed Aug 29 2012 Michal Luscon <mluscon@redhat.con> - 7:3.1.10-8
- NTLM pass-through authentication does not work
- Squid exits when IPv6 is disabled and request contains IPv6 address

* Tue Aug 21 2012 Michal Luscon <mluscon@redhat.com> - 7:3.1.10-7
- Squid child process aborts on assertion failed

* Tue Apr 24 2012 Michal Luscon <mluscon@redhat.com> -7:3.1.10-6
- Squid logging wrong error message

* Thu Apr 05 2012 Jiri Skala <jskala@redhat.com> -7:3.1.10-5
- Squid doesn't pass ident to url_rewrite_program

* Wed Feb 08 2012 Jiri Skala <jskala@redhat.com> -7:3.1.10-4
- High memory consumption by squid process

* Mon Nov 21 2011 Jiri Skala <jskala@redhat.com> -7:3.1.10-3
- CVE-2011-4096: Invalid free by processing CNAME DNS record

* Mon Sep 05 2011 Jiri Skala <jskala@redhat.com> -7:3.1.10-2
- CVE-2011-3205 squid: buffer overflow flaw in Squid's Gopher reply parser
- removed unused patch from cvs

* Thu Jan 06 2011 Jiri Skala <jskala@redhat.com> -7:3.1.10-1
- Rebase squid to version 3.1.10
- small memleak in squid-3.1.4

* Thu Jun 03 2010 Jiri Skala <jskala@redhat.com> -7:3.1.4-1
- Rebase squid to stable upstream tarball 3.1.4
- bugfix release, issues relating to IPv6, TPROXY, Memory
  management, follow_x_forwarded_for, and stability fixes

* Wed Apr 28 2010 Jiri Skala <jskala@redhat.com> -7:3.1.1-1
- Rebase squid to stable upstream tarball 3.1.1

* Fri Feb 19 2010 Jiri Skala <jskala@redhat.com> -7:3.1.0.16-3
- added licenses to spec
- replaced /etc by _sysconfdir

* Tue Feb 16 2010 Jiri Skala <jskala@redhat.com> -7:3.1.0.16-2
- squid: HTCP packet temporary DoS (SQUID-2010:2)

* Fri Feb 12 2010 Jiri Skala <jskala@redhat.com> - 7:3.1.0.16-1
- Rebase to new upstream tarball (fixes licensing issues)
- CVE-2010-0308 squid: temporary DoS (assertion failure) triggered by truncated DNS packet (SQUID-2010:1)
- fixes rpmlint issues in spec file
- fixed rpmlint issue initscript file

* Wed Jan 13 2010 Jiri Skala <jskala@redhat.com> - 7:3.1.0.15-4
- TPROXY needs libcap. Also increases security a little.
- merged relevant upstream bugfixes waiting for next 3.1 release

* Tue Jan 12 2010 Jiri Skala <jskala@redhat.com> - 7:3.1.0.15-3
- modified tarball - removed spare files due to MS license

* Mon Nov 23 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.15-2
- Update to 3.1.0.15 with a number of bugfixes and a workaround for
  ICEcast/SHOUTcast streams.

* Mon Nov 23 2009 Jiri Skala <jskala@redhat.com> 7:3.1.0.14-2
- Syntactic error in /etc/init.d/squid
- cannot initialize cache_dir with user specified config file

* Sun Sep 27 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.14-1
- Update to 3.1.0.14

* Sat Sep 26 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.13-7
- Include upstream patches fixing important operational issues
- Enable ESI support now that it does not conflict with normal operation

* Fri Sep 18 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.13-6
- Rotate store.log if enabled

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 7:3.1.0.13-5
- Use password-auth common PAM configuration instead of system-auth

* Tue Sep 15 2009 Jiri Skala <jskala@redhat.com> - 7:3.1.0.13-4
- fixed #521596 - wrong return code of init script

* Tue Sep 08 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.13-3
- Enable squid_kerb_auth

* Mon Sep 07 2009 Henrik Nordstrom <henrik@henriknordtrom.net> - 7:3.1.0.13-2
- Cleaned up packaging to ease future maintenance

* Fri Sep 04 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.1.0.13-1
- Upgrade to next upstream release 3.1.0.13 with many new features
  * IPv6 support
  * NTLM-passthru
  * Kerberos/Negotiate authentication scheme support
  * Localized error pages based on browser language preferences
  * Follow X-Forwarded-For capability
  * and more..

* Mon Aug 31 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 3.0.STABLE18-3
- silence logrotate when Squid is not running

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 7:3.0.STABLE18-2
- rebuilt with new openssl

* Tue Aug 04 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE18-1
- Update to 3.0.STABLE18

* Sat Aug 01 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE17-3
- Squid Bug #2728: regression: assertion failed: http.cc:705: "!eof"

* Mon Jul 27 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE17-2
- Bug #514014, update to 3.0.STABLE17 fixing the denial of service issues
  mentioned in Squid security advisory SQUID-2009_2.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:3.0.STABLE16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Jiri Skala <jskala@redhat.com> 7:3.0.STABLE16-2
- fixed patch parameter of bXXX patches

* Mon Jun 29 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE16-1
- Upgrade to 3.0.STABLE16

* Sat May 23 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE15-2
- Bug #453304 - Squid requires restart after Network Manager connection setup

* Sat May 09 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE15-1
- Upgrade to 3.0.STABLE15

* Tue Apr 28 2009 Jiri Skala <jskala@redhat.com> - 7:3.0.STABLE14-3
- fixed ambiguous condition in the init script (exit 4)

* Mon Apr 20 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE14-2
- Squid bug #2635: assertion failed: HttpHeader.cc:1196: "Headers[id].type == ftInt64"

* Sun Apr 19 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE14-1
- Upgrade to 3.0.STABLE14

* Fri Mar 06 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE13-2
- backported logfile.cc syslog parameters patch from 3.1 (b9443.patch)
- GCC-4.4 workaround in src/wccp2.cc

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:3.0.STABLE13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 5 2009 Jonathan Steffan <jsteffan@fedoraproject.org> - 7:3.0.STABLE13-1
- upgrade to latest upstream

* Tue Jan 27 2009 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE12-1
- upgrade to latest upstream

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 7:3.0.STABLE10-4
- rebuild with new openssl

* Fri Dec 19 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE10-3
- actually include the upstream bugfixes in the build

* Fri Dec 19 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE10-2
- upstream bugfixes for cache corruption and access.log response size errors

* Fri Oct 24 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE10-1
- upgrade to latest upstream

* Sun Oct 19 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE9-2
- disable coss support, not officially supported in 3.0

* Sun Oct 19 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE9-1
- update to latest upstream

* Thu Oct 09 2008 Henrik Nordstrom <henrik@henriknordstrom.net> - 7:3.0.STABLE7-4
- change logrotate to move instead of copytruncate

* Wed Oct 08 2008 Jiri Skala <jskala@redhat.com> - 7:3.0.STABLE7-3
- fix #465052 -  FTBFS squid-3.0.STABLE7-1.fc10

* Thu Aug 14 2008 Jiri Skala <jskala@redhat.com> - 7:3.0.STABLE7-2
- used ncsa_auth.8 from man-pages. there will be this file removed due to conflict
- fix #458593 noisy initscript
- fix #463129 init script tests wrong conf file
- fix #450352 - build.patch patches only generated files

* Wed Jul 02 2008 Jiri Skala <jskala@redhat.com> - 7:3.0.STABLE7-1
- update to latest upstream
- fix #453214

* Mon May 26 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE6-2
- fix bad allocation

* Wed May 21 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE6-1
- upgrade to latest upstream
- fix bad allocation

* Fri May 09 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE5-2
- fix configure detection of netfilter kernel headers (#435499),
  patch by aoliva@redhat.com
- add support for negotiate authentication (#445337)

* Fri May 02 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE5-1
- upgrade to latest upstream

* Tue Apr 08 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE4-1
- upgrade to latest upstream

* Thu Apr 03 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE2-2
- add %%{optflags} to make
- remove warnings about unused return values

* Thu Mar 13 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE2-1
- upgrade to latest upstream 3.0.STABLE2
- check config file before starting (#428998)
- whitespace unification of init script
- some minor path changes in the QUICKSTART file
- configure with the --with-filedescriptors=16384 option

* Tue Feb 26 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE1-3
- change the cache_effective_group default back to none

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE1-2
- rebuild for 4.3

* Wed Jan 23 2008 Martin Nagy <mnagy@redhat.com> - 7:3.0.STABLE1-1
- upgrade to latest upstream 3.0.STABLE1

* Tue Dec 04 2007 Martin Bacovsky <mbacovsk@redhat.com> - 2.6.STABLE17-1
- upgrade to latest upstream 2.6.STABLE17

* Wed Oct 31 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE16-3
- arp-acl was enabled

* Tue Sep 25 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE16-2
- our fd_config patch was replaced by upstream's version 
- Source1 (FAQ.sgml) points to local source (upstream's moved to wiki)

* Fri Sep 14 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE16-1
- upgrade to latest upstream 2.6.STABLE16

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 7:2.6.STABLE14-2
- Rebuild for selinux ppc32 issue.

* Thu Jul 19 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE14-1
- update to latest upstream 2.6.STABLE14
- resolves: #247064: Initscript Review

* Tue Mar 27 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE12-1
- update to latest upstream 2.6.STABLE12
- Resolves: #233913: squid: unowned directory

* Mon Feb 19 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE9-2
- Resolves: #226431: Merge Review: squid

* Mon Jan 29 2007 Martin Bacovsky <mbacovsk@redhat.com> - 7:2.6.STABLE9-1
- update to the latest upstream

* Sun Jan 14 2007 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE7-1
- update to the latest upstream

* Tue Dec 12 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE6-1
- update to the latest upstream

* Mon Nov  6 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE5-1
- update to the latest upstream

* Thu Oct 26 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE4-4
- added fix for #205568 - marked cachemgr.conf as world readable

* Wed Oct 25 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE4-3
- added fix for #183869 - squid can abort when getting status
- added upstream fixes:
    * Bug #1796: Assertion error HttpHeader.c:914: "str"
    * Bug #1779: Delay pools fairness, correction to first patch
    * Bug #1802: Crash on exit in certain conditions where cache.log is not writeable
    * Bug #1779: Delay pools fairness when multiple connections compete for bandwidth
    * Clarify the select/poll/kqueue/epoll configure --enable/disable options
- reworked fd patch for STABLE4

* Tue Oct 17 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE4-2
- upstream fixes:
  * Accept 00:00-24:00 as a valid time specification (upstream BZ #1794)
  * aioDone() could be called twice
  * Squid reconfiguration (upstream BZ #1800)

* Mon Oct 2 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE4-1
- new upstream
- fixes from upstream bugzilla, items #1782,#1780,#1785,#1719,#1784,#1776

* Tue Sep 5 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE3-2
- added upstream patches for ACL

* Mon Aug 21 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE3-1
- the latest stable upstream

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 7:2.6.STABLE2-3
- added some requirements for pre/post install scripts

* Fri Aug 04 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE2-2
- added patch for #198253 - squid: don't chgrp another pkg's
  files/directory

* Mon Jul 31 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE2-1
- the latest stable upstream
- reworked fd config patch

* Tue Jul 25 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE1-3
- the latest CVS upstream snapshot

* Wed Jul 19 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE1-2
- the latest CVS snapshot

* Tue Jul 18 2006 Martin Stransky <stransky@redhat.com> - 7:2.6.STABLE1-1
- new upstream + the latest CVS snapshot from 2006/07/18
- updated fd config patch
- enabled epoll
- fixed release format (#197405)
- enabled WCCPv2 support (#198642)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 7:2.5.STABLE14-2.1
- rebuild

* Thu Jun 8 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE14-2
- fix for squid BZ#1511 - assertion failed: HttpReply.c:105: "rep"

* Tue May 30 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE14-1
- update to new upstream

* Sun May 28 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE13-5
- fixed libbind patch (#193298)

* Wed May 3  2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE13-4
- added extra group check (#190544)

* Wed Mar 29 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE13-3
- improved pre script (#187217) - added group switch

* Thu Mar 23 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE13-2
- removed "--with-large-files" on 64bit arches

* Mon Mar 13 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE13-1
- update to new upstream

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 7:2.5.STABLE12-5.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Martin Stransky <stransky@redhat.com> - 7:2.5.STABLE12-5
- new upstream patches

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 7:2.5.STABLE12-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Dec 28 2005  Martin Stransky <stransky@redhat.com> 7:2.5.STABLE12-4
- added follow-xff patch (#176055)
- samba path fix (#176659)

* Mon Dec 19 2005  Martin Stransky <stransky@redhat.com> 7:2.5.STABLE12-3
- fd-config.patch clean-up
- SMB_BadFetch patch from upstream

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 28 2005  Martin Stransky <stransky@redhat.com> 7:2.5.STABLE12-2
- rewriten patch squid-2.5.STABLE10-64bit.patch, it works with
  "--with-large-files" option now
- fix for #72896 - squid does not support > 1024 file descriptors,
  new "--enable-fd-config" option for it.

* Wed Nov 9 2005  Martin Stransky <stransky@redhat.com> 7:2.5.STABLE12-1
- update to STABLE12
- setenv patch

* Mon Oct 24 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE11-6
- fix for delay pool from upstream

* Thu Oct 20 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE11-5
- fix for #171213 - CVE-2005-3258 Squid crash due to malformed FTP response
- more fixes from upstream

* Fri Oct 14 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE11-4
- enabled support for large files (#167503)

* Thu Oct 13 2005 Tomas Mraz <tmraz@redhat.com> 7:2.5.STABLE11-3
- use include instead of pam_stack in pam config

* Thu Sep 29 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE11-2
- added patch for delay pools and some minor fixes

* Fri Sep 23 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE11-1
- update to STABLE11

* Mon Sep 5 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE10-4
- Three upstream patches for #167414
- Spanish and Greek messages
- patch for -D_FORTIFY_SOURCE=2 

* Tue Aug 30 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE10-3
- removed "--enable-truncate" option (#165948)
- added "--enable-cache-digests" option (#102134)
- added "--enable-ident-lookups" option (#161640)
- some clean up (#165949)

* Fri Jul 15 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE10-2
- pam_auth and ncsa_auth have setuid (#162660)

* Thu Jul 7 2005 Martin Stransky <stransky@redhat.com> 7:2.5.STABLE10-1
- new upstream version
- enabled fakeauth utility (#154020)
- enabled digest authentication scheme (#155882)
- all error pages marked as config (#127836)
- patch for 64bit statvfs interface (#153274)
- added httpd config file for cachemgr.cgi (#112725)

* Mon May 16 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE9-7
- Upgrade the upstream -dns_query patch from -4 to -5

* Wed May 11 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE9-6
- More upstream patches, including a fix for
  bz#157456 CAN-2005-1519 DNS lookups unreliable on untrusted networks

* Tue Apr 26 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE9-5
- more upstream patches, including a fix for
  CVE-1999-0710 cachemgr malicious use

* Fri Apr 22 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE9-4
- More upstream patches, including the fixed 2GB patch.
- include the -libbind patch, which prevents squid from using the optional
  -lbind library, even if it's installed.

* Tue Mar 15 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE9-2
- New upstream version, with 14 upstream patches.

* Wed Feb 16 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE8-2
- new upstream version with 4 upstream patches.
- Reorganize spec file to apply upstream patches first

* Tue Feb 1 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE7-4
- Include two more upstream patches for security vulns:
  bz#146783 Correct handling of oversized reply headers
  bz#146778 CAN-2005-0211 Buffer overflow in WCCP recvfrom() call

* Tue Jan 25 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE7-3
- Include more upstream patches, including two for security holes.

* Tue Jan 18 2005 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE7-2
- Add a triggerin on samba-common to make /var/cache/samba/winbindd_privileged
  accessable so that ntlm_auth will work.  It needs to be in this rpm,
  because the Samba RPM can't assume the squid user exists.
  Note that this will only work if the Samba RPM is recent enough to create
  that directory at install time instead of at winbindd startup time.
  That should be samba-common-3.0.0-15 or later.
  This fixes bugzilla #103726
- Clean up extra whitespace in this spec file.
- Add additional upstream patches. (Now 18 upstream patches).
- patch #112 closes CAN-2005-0096 and CAN-2005-0097, remote DOS security holes.
- patch #113 closes CAN-2005-0094, a remote buffer-overflow DOS security hole.
- patch #114 closes CAN-2005-0095, a remote DOS security hole.
- Remove the -nonbl (replaced by #104) and -close (replaced by #111) patches, since
  they're now fixed by upstream patches.

* Mon Oct 25 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE7-1
- new upstream version, with 3 upstream patches.
  Updated the -build and -config patches
- Include patch from Ulrich Drepper <frepper@redhat.com> to more
  intelligently close all file descriptors.

* Mon Oct 18 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE6-3
- include patch from Ulrich Drepper <drepper@redhat.com> to stop
  problems with O_NONBLOCK.  This closes #136049

* Tue Oct 12 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE6-2
- Include fix for CAN-2004-0918

* Tue Sep 28 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE6-1
- New upstream version, with 32 upstream patches.
  This closes #133970, #133931, #131728, #128143, #126726

- Change the permissions on /etc/squid/squid.conf to 640.  This closes
  bugzilla #125007

* Mon Jun 28 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5STABLE5-5
- Merge current upstream patches.
- Fix the -pipe patch to have the correct name of the winbind pipe.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 5 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE5-2
- Include the first 10 upstream patches
- Add a patch for the correct location of the winbindd pipe.  This closes
  bugzilla #107561
- Remove the change to ssl_support.c from squid-2.5.STABLE3-build patch
  This closes #117851
- Include /etc/pam.d/squid .  This closes #113404
- Include a patch to close #111254 (assignment in assert)
- Change squid.init to put output messages in /var/log/squid/squid.out
  This closes #104697
- Only useradd the squid user if it doesn't already exist, and error out
  if the useradd fails.  This closes #118718.

* Tue Mar 2 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE5-1
- New upstream version, obsoletes many patches.
- Fix --datadir passed to configure.  Configure automatically adds /squid
  so we shouldn't.
- Remove the problematic triggerpostun trigger, since is's broken, and FC2
  never shipped with that old version.
- add %%{?_smp_mflags} to make line.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com>
- Use ':' instead of '.' as separator for chown.

* Fri Feb 20 2004 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE4-3
- Clean up the spec file to work on 64-bit platforms (use %%{_libdir}
  instead of /usr/lib, etc)
- Make the release number in the changelog section agree with reality.
- use -fPIE rather than -fpie.  s390 fails with just -fpie

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 5 2004 Jay Fenlason <fenlason@redhat.com>
- Incorporate many upstream patches
- Include many spec file changes from D.Johnson <dj@www.uk.linux.org>

* Tue Sep 23 2003 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE4-1
- New upstream version.
- Fix the Source: line in this spec file to point to the correct URL.
- redo the -location patch to work with the new upstream version.

* Mon Jun 30 2003 Jay Fenlason <fenlason@redhat.com> 7:2.5.STABLE3-0
- Spec file change to enable the nul storage module. bugzilla #74654
- Upgrade to 2.5STABLE3 with current official patches.
- Added --enable-auth="basic,ntlm": closes bugzilla #90145
- Added --with-winbind-auth-challenge: closes bugzilla #78691
- Added --enable-useragent-log and --enable-referer-log, closes
- bugzilla #91884
# - Changed configure line to enable pie
# (Disabled due to broken compilers on ia64 build machines)
#- Patched to increase the maximum number of file descriptors #72896
#- (disabled for now--needs more testing)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Bill Nottingham <notting@redhat.com> 7:2.5.STABLE1-1
- update to 2.5.STABLE1

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 7:2.4.STABLE7-5
- remove unpackaged files from the buildroot

* Tue Aug 27 2002 Nalin Dahyabhai <nalin@redhat.com> 2.4.STABLE7-4
- rebuild

* Wed Jul 31 2002 Karsten Hopp <karsten@redhat.de>
- don't raise an error if the config file is incomplete
  set defaults instead (#69322, #70065)

* Thu Jul 18 2002 Bill Nottingham <notting@redhat.com> 2.4.STABLE7-2
- don't strip binaries

* Mon Jul  8 2002 Bill Nottingham <notting@redhat.com>
- update to 2.4.STABLE7
- fix restart (#53761)

* Tue Jun 25 2002 Bill Nottingham <notting@redhat.com>
- add various upstream bugfix patches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Mar 22 2002 Bill Nottingham <notting@redhat.com>
- 2.4.STABLE6
- turn off carp

* Mon Feb 18 2002 Bill Nottingham <notting@redhat.com>
- 2.4.STABLE3 + patches
- turn off HTCP at request of maintainers
- leave SNMP enabled in the build, but disabled in the default config

* Fri Jan 25 2002 Tim Powers <timp@redhat.com>
- rebuild against new libssl

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- require linuxdoc-tools instead of sgml-tools

* Tue Sep 25 2001 Bill Nottingham <notting@redhat.com>
- update to 2.4.STABLE2

* Mon Sep 24 2001 Bill Nottingham <notting@redhat.com>
- add patch to fix FTP crash

* Mon Aug  6 2001 Bill Nottingham <notting@redhat.com>
- fix uninstall (#50411)

* Mon Jul 23 2001 Bill Nottingham <notting@redhat.com>
- add some buildprereqs (#49705)

* Sun Jul 22 2001 Bill Nottingham <notting@redhat.com>
- update FAQ

* Tue Jul 17 2001 Bill Nottingham <notting@redhat.com>
- own /etc/squid, /usr/lib/squid

* Tue Jun 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment
- s/Copyright:/License:/

* Tue Apr 24 2001 Bill Nottingham <notting@redhat.com>
- update to 2.4.STABLE1 + patches
- enable some more configure options (#24981)
- oops, ship /etc/sysconfig/squid

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Feb  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- improve i18n
- make the initscript use the standard OK/FAILED

* Tue Jan 23 2001 Bill Nottingham <notting@redhat.com>
- change i18n mechanism

* Fri Jan 19 2001 Bill Nottingham <notting@redhat.com>
- fix path references in QUICKSTART (#15114)
- fix initscript translations (#24086)
- fix shutdown logic (#24234), patch from <jos@xos.nl>
- add /etc/sysconfig/squid for daemon options & shutdown timeouts
- three more bugfixes from the Squid people
- update FAQ.sgml
- build and ship auth modules (#23611)

* Thu Jan 11 2001 Bill Nottingham <notting@redhat.com>
- initscripts translations

* Mon Jan  8 2001 Bill Nottingham <notting@redhat.com>
- add patch to use mkstemp (greg@wirex.com)

* Fri Dec 01 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Sat Nov 11 2000 Bill Nottingham <notting@redhat.com>
- fix the acl matching cases (only need the second patch)

* Tue Nov  7 2000 Bill Nottingham <notting@redhat.com>
- add two patches to fix domain ACLs
- add 2 bugfix patches from the squid people

* Fri Jul 28 2000 Bill Nottingham <notting@redhat.com>
- clean up init script; fix condrestart
- update to STABLE4, more bugfixes
- update FAQ

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error in init script
- finish adding condrestart support

* Fri Jul 14 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul  6 2000 Bill Nottingham <notting@redhat.com>
- prereq /etc/init.d
- add bugfix patch
- update FAQ

* Thu Jun 29 2000 Bill Nottingham <notting@redhat.com>
- fix init script

* Tue Jun 27 2000 Bill Nottingham <notting@redhat.com>
- don't prereq new initscripts

* Mon Jun 26 2000 Bill Nottingham <notting@redhat.com>
- initscript munging

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- rebuild for exciting FHS stuff

* Wed May 31 2000 Bill Nottingham <notting@redhat.com>
- fix init script again (#11699)
- add --enable-delay-pools (#11695)
- update to STABLE3
- update FAQ

* Fri Apr 28 2000 Bill Nottingham <notting@redhat.com>
- fix init script (#11087)

* Fri Apr  7 2000 Bill Nottingham <notting@redhat.com>
- three more bugfix patches from the squid people
- buildprereq jade, sgmltools

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- make %%pre more portable

* Thu Mar 16 2000 Bill Nottingham <notting@redhat.com>
- bugfix patches
- fix dependency on /usr/local/bin/perl

* Sat Mar  4 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE2

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- Yet More Bugfix Patches

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- add more bugfix patches
- --enable-heap-replacement

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- grab some bugfix patches

* Mon Jan 10 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE1 (whee, another serial number)

* Tue Dec 21 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix compliance with ftp RFCs
  (http://www.wu-ftpd.org/broken-clients.html)
- Work around a bug in some versions of autoconf
- BuildPrereq sgml-tools - we're using sgml2html

* Mon Oct 18 1999 Bill Nottingham <notting@redhat.com>
- add a couple of bugfix patches

* Wed Oct 13 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE5.
- update FAQ, fix URLs.

* Sat Sep 11 1999 Cristian Gafton <gafton@redhat.com>
- transform restart in reload and add restart to the init script

* Tue Aug 31 1999 Bill Nottingham <notting@redhat.com>
- add squid user as user 23.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging
- fix conflict between logrotate & squid -k (#4562)

* Wed Jul 28 1999 Bill Nottingham <notting@redhat.com>
- put cachemgr.cgi back in /usr/lib/squid

* Wed Jul 14 1999 Bill Nottingham <notting@redhat.com>
- add webdav bugfix patch (#4027)

* Mon Jul 12 1999 Bill Nottingham <notting@redhat.com>
- fix path to config in squid.init (confuses linuxconf)

* Wed Jul  7 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE4

* Wed Jun 9 1999 Dale Lovelace <dale@redhat.com>
- logrotate changes
- errors from find when /var/spool/squid or
- /var/log/squid didn't exist

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE3

* Thu Apr 22 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE.2

* Sun Apr 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE1

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't need to run groupdel on remove
- fix useradd

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- fix effective_user (bug #2124)

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- duh. adduser does require a user name.
- add a serial number

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- add an adduser in %%pre, too

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- oog. chkconfig must be in %%preun, not %%postun

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- switch to using group squid
- turn off icmp (insecure)
- update to 2.2.DEVEL3
- build FAQ docs from source

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Feb 10 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.PRE2

* Wed Dec 30 1998 Bill Nottingham <notting@redhat.com>
- cache & log dirs shouldn't be world readable
- remove preun script (leave logs & cache @ uninstall)

* Tue Dec 29 1998 Bill Nottingham <notting@redhat.com>
- fix initscript to get cache_dir correct

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 2.1.PATCH2
- merge in some changes from RHCN version

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.1.22

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- don't make packages conflict with each other...

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- added a proxy auth patch from Alex deVries <adevries@engsoc.carleton.ca>
- fixed initscripts

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.21/1.NOVM.21

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated the init script to use reconfigure option to restart squid instead
  of shutdown/restart (both safer and quicker)

* Sat Feb 07 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.20
- added the NOVM package and tryied to reduce the mess in the spec file

* Wed Jan 7 1998 Cristian Gafton <gafton@redhat.com>
- first build against glibc
- patched out the use of setresuid(), which is available only on kernels
  2.1.44 and later