%define _default_patch_fuzz 2

# Conditionals
# Invoke "rpmbuild --without <feature>" or "rpmbuild --with <feature>"
# to disable or enable specific features
%bcond_with testagents
%bcond_with watchdog
%bcond_with monitoring
%bcond_without snmp
%bcond_without dbus
# no InfiniBand stack on s390(x)
%ifnarch s390 s390x
%bcond_without rdma
%endif
%bcond_without runautogen

Name: corosync
Summary: The Corosync Cluster Engine and Application Programming Interfaces
Version: 1.4.7
Release: 5%{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}%{?dist}.0
License: BSD
Group: System Environment/Base
URL: http://ftp.corosync.org
Source0: ftp://ftp:user@ftp.corosync.org/downloads/%{name}-%{version}/%{name}-%{version}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}.tar.gz

Patch0: bz1136431-1-Adjust-MTU-for-IPv6-correctly.patch
Patch1: bz742999-1-config-Make-sure-user-doesn-t-mix-IPv6-and-IPv4.patch
Patch2: bz742999-2-config-Process-broadcast-option-consistently.patch
Patch3: bz742999-3-config-Ensure-mcast-address-port-differs-for-rrp.patch
Patch4: bz1163846-1-totem-Inform-RRP-about-membership-changes.patch
Patch5: bz1163846-2-totemnet-Add-totemnet_member_set_active.patch
Patch6: bz1163846-3-totemrrp-Implement-_membership_changed.patch
Patch7: bz1163846-4-totemudpu-Implement-member_set_active.patch
Patch8: bz1163846-5-totemudpu-Send-msgs-to-all-members-occasionally.patch
Patch9: bz1141367-1-ipcc-Fix-ERR_LIBRARY-error-if-finalise-called-inside.patch
Patch10: bz1278478-1-config-Fix-then-for-than-typos-in-messages-and-some-.patch
Patch11: bz1278478-2-totemconfig-Make-sure-join-timeout-is-less-than-cons.patch
Patch12: bz1278473-1-Reset-timer_problem_decrementer-on-fault.patch
Patch13: bz1278473-2-totem-Ignore-duplicated-commit-tokens-in-recovery.patch
Patch14: bz1278473-3-objdb-Fix-incorrect-using-lock.patch
Patch15: bz1278490-1-totemip-Be-more-selective-when-matching-bindnetaddr-.patch
Patch16: bz1200387-1-totem-Log-a-message-if-JOIN-or-LEAVE-message-is-igno.patch
Patch17: bz1286759-1-Revert-ipcc-Fix-ERR_LIBRARY-error-if-finalise-called.patch
Patch18: bz1286759-2-ipcc-Fix-ERR_LIBRARY-on-finalize-call-in-dispatch.patch
Patch19: bz1305119-1-totempg-Fix-memory-leak.patch

ExclusiveArch: i686 x86_64 %{arm}

# Runtime bits
Requires: corosynclib = %{version}-%{release}
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Conflicts: openais <= 0.89, openais-devel <= 0.89

# Build bits

%if %{with runautogen}
BuildRequires: autoconf automake
%endif
BuildRequires: nss-devel
%if %{with rdma}
BuildRequires: libibverbs-devel librdmacm-devel
%endif
%if %{with snmp}
BuildRequires: net-snmp-devel
%endif
%if %{with dbus}
BuildRequires: dbus-devel
%endif

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%prep
%setup -q -n %{name}-%{version}%{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}
%patch0 -p1 -b .bz1136431-1
%patch1 -p1 -b .bz742999-1
%patch2 -p1 -b .bz742999-2
%patch3 -p1 -b .bz742999-3
%patch4 -p1 -b .bz1163846-1
%patch5 -p1 -b .bz1163846-2
%patch6 -p1 -b .bz1163846-3
%patch7 -p1 -b .bz1163846-4
%patch8 -p1 -b .bz1163846-5
%patch9 -p1 -b .bz1141367-1
%patch10 -p1 -b .bz1278478-1
%patch11 -p1 -b .bz1278478-2
%patch12 -p1 -b .bz1278473-1
%patch13 -p1 -b .bz1278473-2
%patch14 -p1 -b .bz1278473-3
%patch15 -p1 -b .bz1278490-1
%patch16 -p1 -b .bz1200387-1
%patch17 -p1 -b .bz1286759-1
%patch18 -p1 -b .bz1286759-2
%patch19 -p1 -b .bz1305119-1

%build
%if %{with runautogen}
./autogen.sh
%endif

%if %{with rdma}
export ibverbs_CFLAGS=-I/usr/include/infiniband \
export ibverbs_LIBS=-libverbs \
export rdmacm_CFLAGS=-I/usr/include/rdma \
export rdmacm_LIBS=-lrdmacm \
%endif
%{configure} \
	--enable-nss \
%if %{with testagents}
	--enable-testagents \
%endif
%if %{with watchdog}
	--enable-watchdog \
%endif
%if %{with monitoring}
	--enable-monitoring \
%endif
%if %{with snmp}
	--enable-snmp \
%endif
%if %{with dbus}
	--enable-dbus \
%endif
%if %{with rdma}
	--enable-rdma \
%endif
	--with-initddir=%{_initrddir}

make %{_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

%if %{with dbus}
mkdir -p -m 0700 %{buildroot}/%{_sysconfdir}/dbus-1/system.d
install -m 644 %{_builddir}/%{name}-%{version}/conf/corosync-signals.conf %{buildroot}/%{_sysconfdir}/dbus-1/system.d/corosync-signals.conf
%endif

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*
# /etc/sysconfig/corosync-notifyd
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 tools/corosync-notifyd.sysconfig.example \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-notifyd

%clean
rm -rf %{buildroot}

%description
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add corosync || :
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/service corosync stop &>/dev/null || :
	/sbin/chkconfig --del corosync || :
fi

%files
%defattr(-,root,root,-)
%doc LICENSE SECURITY
%{_bindir}/corosync-blackbox
%{_sbindir}/corosync
%{_sbindir}/corosync-keygen
%{_sbindir}/corosync-objctl
%{_sbindir}/corosync-cfgtool
%{_sbindir}/corosync-fplay
%{_sbindir}/corosync-pload
%{_sbindir}/corosync-cpgtool
%{_sbindir}/corosync-quorumtool
%{_sbindir}/corosync-notifyd
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/service.d
%dir %{_sysconfdir}/corosync/uidgid.d
%config(noreplace) %{_sysconfdir}/corosync/corosync.conf.example
%config(noreplace) %{_sysconfdir}/corosync/corosync.conf.example.udpu
%config(noreplace) %{_sysconfdir}/sysconfig/corosync-notifyd
%if %{with dbus}
%{_sysconfdir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with snmp}
%{_datadir}/snmp/mibs/COROSYNC-MIB.txt
%endif
%{_initrddir}/corosync
%{_initrddir}/corosync-notifyd
%dir %{_libexecdir}/lcrso
%{_libexecdir}/lcrso/coroparse.lcrso
%{_libexecdir}/lcrso/objdb.lcrso
%{_libexecdir}/lcrso/service_cfg.lcrso
%{_libexecdir}/lcrso/service_cpg.lcrso
%{_libexecdir}/lcrso/service_evs.lcrso
%{_libexecdir}/lcrso/service_confdb.lcrso
%{_libexecdir}/lcrso/service_pload.lcrso
%{_libexecdir}/lcrso/quorum_votequorum.lcrso
%{_libexecdir}/lcrso/quorum_testquorum.lcrso
%{_libexecdir}/lcrso/vsf_quorum.lcrso
%{_libexecdir}/lcrso/vsf_ykd.lcrso
%dir %{_localstatedir}/lib/corosync
%attr(755, root, root) %{_localstatedir}/log/cluster
%dir %{_localstatedir}/log/cluster
%{_mandir}/man8/corosync_overview.8*
%{_mandir}/man8/corosync.8*
%{_mandir}/man8/corosync-blackbox.8*
%{_mandir}/man8/corosync-objctl.8*
%{_mandir}/man8/corosync-keygen.8*
%{_mandir}/man8/corosync-cfgtool.8*
%{_mandir}/man8/corosync-cpgtool.8*
%{_mandir}/man8/corosync-fplay.8*
%{_mandir}/man8/corosync-pload.8*
%{_mandir}/man8/corosync-notifyd.8*
%{_mandir}/man8/corosync-quorumtool.8*
%{_mandir}/man5/corosync.conf.5*
%{_mandir}/man8/confdb_keys.8*

%package -n corosynclib
Summary: The Corosync Cluster Engine Libraries
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description -n corosynclib
This package contains corosync libraries.

%files -n corosynclib
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/libcfg.so.*
%{_libdir}/libcpg.so.*
%{_libdir}/libconfdb.so.*
%{_libdir}/libevs.so.*
%{_libdir}/libtotem_pg.so.*
%{_libdir}/liblogsys.so.*
%{_libdir}/libcoroipcc.so.*
%{_libdir}/libcoroipcs.so.*
%{_libdir}/libquorum.so.*
%{_libdir}/libvotequorum.so.*
%{_libdir}/libpload.so.*
%{_libdir}/libsam.so.*

%post -n corosynclib -p /sbin/ldconfig

%postun -n corosynclib -p /sbin/ldconfig

%package -n corosynclib-devel
Summary: The Corosync Cluster Engine Development Kit
Group: Development/Libraries
Requires: corosynclib = %{version}-%{release}
Requires: pkgconfig
Provides: corosync-devel = %{version}
Obsoletes: corosync-devel < 0.92-7

%description -n corosynclib-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%files -n corosynclib-devel
%defattr(-,root,root,-)
%doc LICENSE README.devmap
%dir %{_includedir}/corosync/
%{_includedir}/corosync/cs_config.h
%{_includedir}/corosync/corodefs.h
%{_includedir}/corosync/coroipc_types.h
%{_includedir}/corosync/coroipcs.h
%{_includedir}/corosync/coroipcc.h
%{_includedir}/corosync/cfg.h
%{_includedir}/corosync/confdb.h
%{_includedir}/corosync/corotypes.h
%{_includedir}/corosync/cpg.h
%{_includedir}/corosync/evs.h
%{_includedir}/corosync/hdb.h
%{_includedir}/corosync/list.h
%{_includedir}/corosync/mar_gen.h
%{_includedir}/corosync/sam.h
%{_includedir}/corosync/swab.h
%{_includedir}/corosync/quorum.h
%{_includedir}/corosync/votequorum.h
%dir %{_includedir}/corosync/totem/
%{_includedir}/corosync/totem/coropoll.h
%{_includedir}/corosync/totem/totem.h
%{_includedir}/corosync/totem/totemip.h
%{_includedir}/corosync/totem/totempg.h
%dir %{_includedir}/corosync/lcr/
%{_includedir}/corosync/lcr/lcr_ckpt.h
%{_includedir}/corosync/lcr/lcr_comp.h
%{_includedir}/corosync/lcr/lcr_ifact.h
%dir %{_includedir}/corosync/engine
%{_includedir}/corosync/engine/config.h
%{_includedir}/corosync/engine/coroapi.h
%{_includedir}/corosync/engine/logsys.h
%{_includedir}/corosync/engine/objdb.h
%{_includedir}/corosync/engine/quorum.h
%{_libdir}/libcfg.so
%{_libdir}/libcpg.so
%{_libdir}/libconfdb.so
%{_libdir}/libevs.so
%{_libdir}/libtotem_pg.so
%{_libdir}/liblogsys.so
%{_libdir}/libcoroipcc.so
%{_libdir}/libcoroipcs.so
%{_libdir}/libquorum.so
%{_libdir}/libvotequorum.so
%{_libdir}/libpload.so
%{_libdir}/libsam.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/cpg_*3*
%{_mandir}/man3/evs_*3*
%{_mandir}/man3/confdb_*3*
%{_mandir}/man3/votequorum_*3*
%{_mandir}/man3/sam_*3*
%{_mandir}/man8/cpg_overview.8*
%{_mandir}/man8/evs_overview.8*
%{_mandir}/man8/confdb_overview.8*
%{_mandir}/man8/logsys_overview.8*
%{_mandir}/man8/votequorum_overview.8*
%{_mandir}/man8/coroipc_overview.8*
%{_mandir}/man8/sam_overview.8*

%changelog
* Mon Sep 05 2016 Bjarne Saltbaek <bjarne@redsleeve.org> -  1.4.7-5.0
- Added patch from Jacco
- add ARM Architectures

* Wed Feb 10 2016 Jan Friesse <jfriesse@redhat.com> 1.4.7-5
- Resolves: rhbz#1305119

- totempg: Fix memory leak (rhbz#1305119)
- merge upstream commit 349613b2dce8219a5d08dad816cb4da9c12faf83 (rhbz#1305119)

* Tue Dec 01 2015 Jan Friesse <jfriesse@redhat.com> 1.4.7-4
- Resolves: rhbz#1286759

- Revert "ipcc: Fix ERR_LIBRARY error if finalise called inside dispatch" (rhbz#1286759)
- merge upstream commit 67242e15c298abff4f93a7bfcd72372f7ba60270 (rhbz#1286759)
- ipcc: Fix ERR_LIBRARY on finalize call in dispatch (rhbz#1286759)
- merge upstream commit 514dd9784559feb237af498020bf74cb16091a9e (rhbz#1286759)

* Tue Nov 10 2015 Jan Friesse <jfriesse@redhat.com> 1.4.7-3
- Resolves: rhbz#1200387
- Resolves: rhbz#1278473
- Resolves: rhbz#1278478
- Resolves: rhbz#1278490

- config: Fix 'then' for 'than' typos in messages and some comments. (rhbz#1278478)
- merge upstream commit 1be4f7b899f91a8dc23ade10c539177f2b39d88e (rhbz#1278478)
- totemconfig: Make sure join timeout is less than consensus (rhbz#1278478)
- merge upstream commit 17e90526aaa702cc3079fe5089253590267418d4 (rhbz#1278478)
- Reset timer_problem_decrementer on fault (rhbz#1278473)
- merge upstream commit c5a5bedf6e086acb9f3bda374ac495670a5fcf25 (rhbz#1278473)
- totem: Ignore duplicated commit tokens in recovery (rhbz#1278473)
- merge upstream commit 49236f3a16a0980cdb605040f027722b116a8250 (rhbz#1278473)
- objdb: Fix incorrect using lock (rhbz#1278473)
- merge upstream commit 42c09a78d9ed2dc393e76308f4fce000535674e6 (rhbz#1278473)
- totemip: Be more selective when matching bindnetaddr to IP addresses (rhbz#1278490)
- merge upstream commit 8e90c68fc0a7d5bce035fe7939eb03fa5cf333a2 (rhbz#1278490)
- totem: Log a message if JOIN or LEAVE message is ignored (rhbz#1200387)
- merge upstream commit d3c51cd6e4c293a7222172ccec4b80d70b79f5d4 (rhbz#1200387)

* Mon Mar 02 2015 Jan Friesse <jfriesse@redhat.com> 1.4.7-2
- Resolves: rhbz#1136431
- Resolves: rhbz#1141367
- Resolves: rhbz#1163846
- Resolves: rhbz#742999

- Adjust MTU for IPv6 correctly (rhbz#1136431)
- merge upstream commit 6fc58377d9f3201a74afedbb53311ff95fde700b (rhbz#1136431)
- config: Make sure user doesn't mix IPv6 and IPv4 (rhbz#742999)
- merge upstream commit df4d4da6e204a9f151a764c868bf7c99c97186f5 (rhbz#742999)
- config: Process broadcast option consistently (rhbz#742999)
- merge upstream commit 90d458532b59a15ae8e936f43e8bf1f8f3a32ac7 (rhbz#742999)
- config: Ensure mcast address/port differs for rrp (rhbz#742999)
- merge upstream commit 6f74374d3ff23735cf5e1d5e01e56d6cd866085c (rhbz#742999)
- totem: Inform RRP about membership changes (rhbz#1163846)
- merge upstream commit f35ffb168f8ee3eac4660309088372df4cb215f2 (rhbz#1163846)
- totemnet: Add totemnet_member_set_active (rhbz#1163846)
- merge upstream commit 3dafc4c508e4928d459719958918052ce49fd223 (rhbz#1163846)
- totemrrp: Implement *_membership_changed (rhbz#1163846)
- merge upstream commit 3dcdfeaddbe054fad63d3a3cb046dd018e118e69 (rhbz#1163846)
- totemudpu: Implement member_set_active (rhbz#1163846)
- merge upstream commit bd02ac319af40e4c484c6e4cdb8e049db8813541 (rhbz#1163846)
- totemudpu: Send msgs to all members occasionally (rhbz#1163846)
- merge upstream commit 0bd29025419204672e4d7857434019045bf7b456 (rhbz#1163846)
- ipcc: Fix ERR_LIBRARY error if finalise called inside dispatch (rhbz#1141367)
- merge upstream commit 83bf77e6f42c2a8b01b1d079e8dc792d9cc7d35d (rhbz#1141367)

* Mon Jun 02 2014 Jan Friesse <jfriesse@redhat.com> 1.4.7-1
- Resolves: rhbz#1055584

- Rebase to Corosync 1.4.7

* Thu May 15 2014 Jan Friesse <jfriesse@redhat.com> 1.4.1-19
- Related: rhbz#1001210

- totemiba: Fix incorrect failed log message (rhbz#1001210)
- merge upstream commit 4130d7448dcea024820d20e3c474c54e14ec9cb5 (rhbz#1001210)

* Wed May 14 2014 Jan Friesse <jfriesse@redhat.com> 1.4.1-18
- Resolves: rhbz#1001210
- Resolves: rhbz#1011307
- Resolves: rhbz#1018232
- Resolves: rhbz#1025321
- Resolves: rhbz#1067043

- totemiba: Properly allocate RDMA buffers (rhbz#1001210)
- merge upstream commit 795b04780ff6cd94b2e10aa1826a289f36119ce7 (rhbz#1001210)
- totemiba: Del channel fd from poll before destroy (rhbz#1001210)
- merge upstream commit 86fd9a14f6e74b711eb7e89cec72096bdcd1441b (rhbz#1001210)
- totemiba: Fix parameters position for poll_add (rhbz#1001210)
- merge upstream commit cba0f90af4af55702c1daa7afa03c8be10eaa5f3 (rhbz#1001210)
- corosync to start in infiniband + redundant ring active/passive mode (rhbz#1001210)
- merge upstream commit d0ca2ceb980242dd8c28b57f449eeeac1eb54176 (rhbz#1001210)
- totemiba: Check if configured MTU is allowed by HW (rhbz#1001210)
- merge upstream commit 3403fe06e8a915632679c48ccccb2662521746f2 (rhbz#1001210)
- logsys: Handle full /dev/shm correctly (rhbz#1011307)
- merge upstream commit 095a114ab84074e16d384f3ccaadfecff80b54a2 (rhbz#1011307)
- ipcs: Backport socket creds handling from libqb (rhbz#1018232)
- merge upstream commit 7897e4ae3e1c1ff20a2f375a0a5dc102ab0e98e8 (rhbz#1018232)
- ipcs: Set SO_PASSCRED also on listening socket (rhbz#1018232)
- merge upstream commit f11e5bf61941fd6aca018bb2f15f2371c668974f (rhbz#1018232)
- cpg: Avoid list corruption (rhbz#1025321)
- merge upstream commit 3c11ea7b84c109e6f8451229437351c5a14c7168 (rhbz#1025321)
- cpg: Refactor mh_req_exec_cpg_procleave (rhbz#1067043)
- merge upstream commit e9d9c4be7293c04ca97bfd84f95b76a22690a92a (rhbz#1067043)
- cpg: Make sure nodid is always logged as hex num (rhbz#1067043)
- merge upstream commit 0b825f22f2b95beca1aeb614d22a7e74a84c66b5 (rhbz#1067043)
- cpg: Make sure left nodes are really removed (rhbz#1067043)
- merge upstream commit b55f32fe2e1538db33a1ec584b67744c724328c6 (rhbz#1067043)
- totemiba: Add multicast recovery (rhbz#1001210)
- merge upstream commit 0ea20a3d545c4bf1a02306dd2152eb497a03b7d0 (rhbz#1001210)

* Wed Jul 10 2013 Jan Friesse <jfriesse@redhat.com> 1.4.1-17
- Resolves: rhbz#956739

- Add timestamps to the Corosync black-box output (rhbz#956739)
- merge upstream commit 3ede0352ea4a7ea71ebe16db59c0c7ad0a01f733 (rhbz#956739)

* Thu May 30 2013 Jan Friesse <jfriesse@redhat.com> 1.4.1-16
- Resolves: rhbz#854216
- Resolves: rhbz#877349
- Resolves: rhbz#880598
- Resolves: rhbz#881729
- Resolves: rhbz#906432
- Resolves: rhbz#907894
- Resolves: rhbz#915490
- Resolves: rhbz#915769
- Resolves: rhbz#916227
- Resolves: rhbz#922671
- Resolves: rhbz#924261
- Resolves: rhbz#947936
- Resolves: rhbz#949491
- Resolves: rhbz#959184
- Resolves: rhbz#959189

- If failed_to_recv is set, consensus can be empty (rhbz#854216)
- merge upstream commit 81ff0e8c94589bb7139d89e573a75473cfc5d173 (rhbz#854216)
- objdb: Don't read uninitialized memory in inc/dec (rhbz#880598)
- merge upstream commit 0a11d261a361726703084897471608d9914e0548 (rhbz#880598)
- log: Handle race in printf_to_logs and format_set (rhbz#881729)
- merge upstream commit a282eeecb4899ec415f76442217836338edfbeec (rhbz#881729)
- log: Avoid deadlock caused by previous commit (rhbz#881729)
- merge upstream commit e69f322d52a967e19ac6cf4eba60c54fc64b1688 (rhbz#881729)
- Handle colon in configuration file (rhbz#906432)
- merge upstream commit c04af91ada3c4ca29643cad599ed5605f6bb10bd (rhbz#906432)
- Handle unexpected closing brace in config file (rhbz#906432)
- merge upstream commit 60a9f809c17d6cfe73c34263233dbf8e4677d6b5 (rhbz#906432)
- Put handle to hdb in dispatch on unknown message (rhbz#922671)
- merge upstream commit 5a4610628334b1e02f87b7e6a8946b59b65a1ec1 (rhbz#922671)
- Properly check result of coroipcc_dispatch_put (rhbz#922671)
- merge upstream commit dc31a079e8374329f0818f16e74b619f31aa835e (rhbz#922671)
- Handle config file with service without name (rhbz#915769)
- merge upstream commit 6b719961b36b3b780f2c9ff148aa2273872f8788 (rhbz#915769)
- Move corosync exit semaphore initialization (rhbz#916227)
- merge upstream commit b6aaa6e2af625467316e54e67a39c6327cf73cbc (rhbz#916227)
- coroipcs: Ensure rb data are not overwritten (rhbz#922671)
- merge upstream commit c7e686181bcd0e975b09725502bef02c7d0c338a (rhbz#922671)
- Properly lock pending_semops (rhbz#922671)
- merge upstream commit 4d050cfac3cd30ad60a58e8294298968ee9d89f9 (rhbz#922671)
- cfg: When send_shutdown fails, clear shutdown_con (rhbz#924261)
- merge upstream commit fd967b6db504b1fe6667da8ce8a141924e3914a9 (rhbz#924261)
- cfgtool: Retry shutdown on CS_ERR_TRY_AGAIN (rhbz#924261)
- merge upstream commit 3324d31819d359fae75d6f91a942fc84e3b9be23 (rhbz#924261)
- totempg: Make iov_delv local variable (rhbz#907894)
- merge upstream commit 3e3231375c29d562af050a48f18b301bf1cdca82 (rhbz#907894)
- Fix race for sending_allowed (rhbz#907894)
- merge upstream commit 94331b5e0226f985364ef0632fdf4d5f0d91d625 (rhbz#907894)
- schedwrk: Set values before create callback (rhbz#907894)
- merge upstream commit 7f00dcb548584911191f1e70483d4523c3ba1319 (rhbz#907894)
- Remove exit thread and replace it by exit pipe (rhbz#907894)
- merge upstream commit 9f8279a3f1853139e9bd472c23f905baf9298c32 (rhbz#907894)
- totempg: Store and restore global variables (rhbz#907894)
- merge upstream commit 5e6e1a000db8b066aff08b0649886e4ce07b843c (rhbz#907894)
- Logsys: Ensure logging PID is really corosync (rhbz#915490)
- merge upstream commit 830df013a853ffa7e9b49efb030ccc7920d2f683 (rhbz#915490)
- fplay: Check minimum record size (rhbz#915490)
- merge upstream commit ef63aae13945bd790e54181593561468426baca4 (rhbz#915490)
- corosync-fplay: Check incorrect idx and cycle (rhbz#915490)
- merge upstream commit d8761bae84c12285ef40426c0ad7f09f569c3d87 (rhbz#915490)
- Improve handling of getpwnam_r() and getgrnam_r() (rhbz#947936)
- merge upstream commit c3422128a45a2833103c8351e0adc84ba6c341be (rhbz#947936)
- Detect big scheduling pauses (rhbz#949491)
- merge upstream commit 7475db7102bf387cfcd16a65b0b0ace3e194bd4b (rhbz#949491)
- Improve corosync-notifyd example (rhbz#877349)
- merge upstream commit 614d897209c8d9d8b38bc583d0ce056a5d3445b6 (rhbz#877349)
- Install sysconfig/corosync-notifyd in specfile (rhbz#877349)
- merge upstream commit bc130cb10c4ec014829286ba61c0de544f82656d (rhbz#877349)
- Free confdb message holder list on confdb exit (rhbz#959189)
- merge upstream commit 013b4ba8ebdc089da76313d43b1454fe324d597b (rhbz#959189)
- Handle SIGPIPE in req_setup_send (rhbz#959184)
- merge upstream commit a9c4bbd9f10d9453730f71d8bd9a02ee8bcf2eed (rhbz#959184)
- confdb: Make objdb_notify_dispatch preemptable (rhbz#959189)
- merge upstream commit 0194e6455983947c9c496658b5d593c769e58bfe (rhbz#959189)
- Lock sync_in_process variable (rhbz#907894)
- merge upstream commit 460a495243b1ebb225e15c1757554ff625aca99e (rhbz#907894)

* Wed Jan 23 2013 Jan Friesse <jfriesse@redhat.com> 1.4.1-15
- Resolves: rhbz#902397

- totemip: Properly detect ipv6 address (rhbz#902397)
- merge upstream commit d76759ec26ecaeb9cc01f49e9eb0749b61454d27 (rhbz#902397)

* Tue Jan 15 2013 Jan Friesse <jfriesse@redhat.com> 1.4.1-14
- Resolves: rhbz#865039

- coroipc: Don't spin when waiting on semaphore (rhbz#865039)
- merge upstream commit 7ce8718a71b7afe341d9f9ac21c6724d6f18dfc4 (rhbz#865039)
- On places with POLLERR check also POLLNVAL (rhbz#865039)
- merge upstream commit 105305a486ae9f171def221ad971d607604a4770 (rhbz#865039)
- Check socket_recv error code in ipc_dispatch_get (rhbz#865039)
- merge upstream commit 694a9c2cf0804428671bf815b974a080c7fd1c6c (rhbz#865039)
- coroipc: Handle pfd.revents as bit-field (rhbz#865039)
- merge upstream commit b6aabed698d34e4e79e03a3354e59a2d0121e692 (rhbz#865039)
- ipcc: Return dup of socket fd to user application (rhbz#865039)
- merge upstream commit 28c5907f59afd52a67be3bddff22df57e1fb36ba (rhbz#865039)

* Sun Jan 06 2013 Jan Friesse <jfriesse@redhat.com> 1.4.1-13
- Resolves: rhbz#830799
- Resolves: rhbz#863940
- Resolves: rhbz#869609

- cpg: Never choose downlist with localnode (rhbz#830799)
- merge upstream commit 559d4083ed8355fe83f275e53b9c8f52a91694b2 (rhbz#830799)
- cpg: Process join list after downlists (rhbz#830799)
- merge upstream commit 02c5dffa5bb8579c223006fa1587de9ba7409a3d (rhbz#830799)
- cpg: Enhance downlist selection algorithm (rhbz#830799)
- merge upstream commit 64d0e5ace025cc929e42896c5d6beb3ef75b8244 (rhbz#830799)
- Don't call sync_* funcs for unloaded services (rhbz#863940)
- merge upstream commit 6ed260b0bfc5e5230a4e765b9c63caf985708c41 (rhbz#863940)
- Handle sync and service unload correctly (rhbz#863940)
- merge upstream commit e7536bdaf82044671d2d18ee799eeacd8603af08 (rhbz#863940)
- Make service_build contain correct number of msgs (rhbz#863940)
- merge upstream commit 1cea171c4d8f9dd19b4995f96842111e41f23d6c (rhbz#863940)
- Ignore sync barrier msgs if sync doesn't started (rhbz#869609)
- merge upstream commit ee292e7968f749f7ebc4daddeb09f39cfbb037b4 (rhbz#869609)
- Fix problem with sync operations under very rare circumstances (rhbz#830799)
- merge upstream commit 6fae42ba72006941c1fde99616ea30f4f10ebb38 (rhbz#830799)
- Handle segfault in backlog_get (rhbz#830799)
- merge upstream commit a559ccf7247bc448ba30b6ebc02a91fa986f146f (rhbz#830799)
- Add waiting_trans_ack also to fragmentation layer (rhbz#830799)
- merge upstream commit 7de25c3b64b2066de19b3f9075c075fb08816de6 (rhbz#830799)

* Wed Nov 21 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-12
- Resolves: rhbz#794522
- Resolves: rhbz#873059
- Resolves: rhbz#876908

- Fix minor errors in man page documentation for corosync.conf (rhbz#873059)
- merge upstream commit b14cd84e96fff1083837a70548ff9e18472c938b (rhbz#873059)
- manpages: Fix typo in evs* manpages (rhbz#873059)
- merge upstream commit 6735455c598393880188db7f297ec699c8ae0492 (rhbz#873059)
- manpages: Add links for referenced confdb calls (rhbz#873059)
- merge upstream commit b98d4ab44979a52ef74259e0676929055442cbfb (rhbz#873059)
- manpages: Add confdb_key_get man page (rhbz#873059)
- merge upstream commit e414e2d34c2e5e26318cfc06f8bdd5b8c8812a7e (rhbz#873059)
- Add link to confdb_keys in corosync-objctl mpage (rhbz#794522)
- merge upstream commit a4e7e2bc46545a5acacb3c840bda5270efec987c (rhbz#794522)
- Track changes for confdb logging object (rhbz#876908)
- merge upstream commit 6c9cae79dc2680d363b0cca85cbbe55a2bc9b517 (rhbz#876908)
- Don't call reload on corosync-objctl actions (rhbz#876908)
- merge upstream commit bdabbf6f20138c5e33154caf32cf66330356893d (rhbz#876908)

* Tue Oct 09 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-11
- Resolves: rhbz#787789
- Resolves: rhbz#794522
- Resolves: rhbz#838743
- Resolves: rhbz#850757
- Resolves: rhbz#861032

- When flushing, discard only memb_join messages (rhbz#850757)
- merge upstream commit 17e15322b7500247c539166441fb2e78cc95d02b (rhbz#850757)
- Add man page with Confdb keys created by corosync (rhbz#794522)
- merge upstream commit c741dbe01ea9bb45ae5d8706c8e4287aeae4bfd5 (rhbz#794522)
- confdb_keys: Document few more runtime statistics (rhbz#794522)
- merge upstream commit 060abd069483aa7b9d90261c11c79b2a6f6e21c1 (rhbz#794522)
- Add support for debug level trace in config file (rhbz#838743)
- merge upstream commit 842d387c2f53e23c055da4509a2f28753d6ffa97 (rhbz#838743)
- Move some totem and cpg messages to trace level (rhbz#838743)
- merge upstream commit 9deff57e779375631541bd52146701c41e3bed68 (rhbz#838743)
- Don't access invalid mem in totemconfig (rhbz#861032)
- merge upstream commit 539917e35a8c74b3ea4eb9ae8cddc2f73378d203 (rhbz#861032)
- Use unix socket for local multicast loop (rhbz#787789)
- merge upstream commit cea2b1a302e6e4563ee5817782f15ea5d941daec (rhbz#787789)
- Move "Totem is unable to form..." message to main (rhbz#787789)
- merge upstream commit e032c14341c38be4d273093f1e6691f8417e264d (rhbz#787789)
- Return back "Totem is unable to form..." message (rhbz#787789)
- merge upstream commit b343668bbfa09ebcfa4816ddf205eeb8f2ea159c (rhbz#787789)
- Change specfile to use runautogen

* Tue Aug 21 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-10
- Related: rhbz#847232

- sa-confdb: fix crash due to incorrect malloc size (rhbz#847232)
- merge upstream commit 0a85b888b0384e83fa4a80c3751a23f4de8a9310 (rhbz#847232)

* Fri Aug 17 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-9
- Resolves: rhbz#847232
- Resolves: rhbz#848210

- confdb: Fix crash with long values and add API calls to get them (rhbz#847232)
- merge upstream commit 5704a34612d8829fce6991f130b7732108cca761 (rhbz#847232)
- confdb: Fix crash with long values (rhbz#847232)
- merge upstream commit 16d309be840045b3fc6d468faf07fbd727756b3f (rhbz#847232)
- Fix dbus part of corosync-notifyd (rhbz#848210)
- merge upstream commit 4ac9cd59e7873914fe5845e69fd79b7a2877c290 (rhbz#848210)
- flatiron: Free outq items list on conn exit (rhbz#848210)
- merge upstream commit 4cdaf8ef1e7676b179eaeb5bde18d4b63d17ce52 (rhbz#848210)

* Thu Aug 02 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-8
- Resolves: rhbz#770455
- Resolves: rhbz#783068
- Resolves: rhbz#786735
- Resolves: rhbz#786737
- Resolves: rhbz#794744
- Resolves: rhbz#821352
- Resolves: rhbz#824902
- Resolves: rhbz#827100
- Resolves: rhbz#838524

- Fixed bug when corosync receive JoinMSG in OPERATIONAL state (rhbz#786737)
- merge upstream commit ffe4943ff52843e1c7beba1250256dc7b6f283e4 (rhbz#786737)
- Correct nodeid of token when we retransmit it (rhbz#786735)
- merge upstream commit 081bfb0a4d6050416d4daa27d7a8417f0ba697fc (rhbz#786735)
- Wait for corosync-notifyd exit in init script (rhbz#783068)
- merge upstream commit fbe6de4d162644aa07b14e93aa2f01299bf4692f (rhbz#783068)
- iba: Use configured node id (rhbz#794744)
- merge upstream commit 0b6e1dc3290cfbc6c38a19bead9f39c582f54c40 (rhbz#794744)
- Correctly handle point-to-point IP (rhbz#821352)
- merge upstream commit a853b6180e9832fa763ea796f310dc3de5718324 (rhbz#821352)
- totemip: Support bind to exact address (rhbz#824902)
- merge upstream commit 1c7b706441d18fe45c6e9c0b17ed1c8c5a723114 (rhbz#824902)
- Register reload callback only once (rhbz#838524)
- merge upstream commit ec51f02373d7f0372b8739ab695ae79f2dea26ce (rhbz#838524)
- cpg: Be more verbose for procjoin message (rhbz#770455)
- merge upstream commit dc22fd13bff1c38888ac16bc8f8fea8117ef27bd (rhbz#770455)
- totemudpu: Bind sending sockets to bindto address (rhbz#827100)
- merge upstream commit 71e5257eb1485ed6544ed2d17792492043e0e48d (rhbz#827100)

* Wed May 09 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-7
- Resolves: rhbz#773720

- objctl: add missing calls to dispatch notifications and fix memory corruption (rhbz#773720)
- merge upstream commit dc9b04a7196b316a596036296ac1a78b21717e97 (rhbz#773720)

* Tue Feb 28 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-6
- Resolves: rhbz#741455
- Resolves: rhbz#797192

- Store error str if can't open logfile (rhbz#741455)
- merge upstream commit f954852ef12544de84a9c557316c2612123b5fec (rhbz#741455)
- Unlink shm buffers if init fails (rhbz#797192)
- merge upstream commit ab83b695b578e0fa68a238bf26dd3a1e338c7ec6 (rhbz#797192)

* Tue Jan 31 2012 Jan Friesse <jfriesse@redhat.com> 1.4.1-5
- Resolves: rhbz#743810
- Resolves: rhbz#743812
- Resolves: rhbz#743813
- Resolves: rhbz#743815
- Resolves: rhbz#752159
- Resolves: rhbz#752951
- Resolves: rhbz#758209
- Resolves: rhbz#747628

- coroipcc: use malloc for path in service_connect (rhbz#743810)
- merge upstream commit 3cfb0792155448d592b043d0d05586c1b76c9499 (rhbz#743810)
- cpg: Handle errors from totem_mcast (rhbz#743812)
- merge upstream commit eef5827dbb01433583da7ad5382789c2f83b9696 (rhbz#743812)
- cfg: Handle errors from totem_mcast (rhbz#743812)
- merge upstream commit af1b122e68dfeb8a42cf9c682de061859d8077ec (rhbz#743812)
- A CPG client can sometimes lockup if the local node is in the downlist (rhbz#743813)
- merge upstream commit ac1d79ea7c14997353427e962865781d0836d9fa (rhbz#743813)
- Resolve a deadlock between the timer and serialize locks. (rhbz#743815)
- merge upstream commit 23112099e1c2b620e6976ca099d2b9afc80721aa (rhbz#743815)
- Add calls to missing object_find_destroy() to fix mem leaks (rhbz#752159)
- merge upstream commit 9ddb845f412531b6a2761f42823b6be43216a9c8 (rhbz#752159)
- A rare condition can lead to fail to recv (rhbz#758209)
- merge upstream commit c68fb0caa2e337c6fdebfe564402c6d06b7fb018 (rhbz#758209)
- Free mem allocated by getaddrinfo (rhbz#752951)
- merge upstream commit a973b7cfb0688cd667d32df714014bbf4cf0bc77 (rhbz#752951)
- corosync and cman conflict on /var/log/cluster permissions (rhbz#747628)

* Thu Sep 22 2011 Jan Friesse <jfriesse@redhat.com> 1.4.1-4
- Resolves: rhbz#722522

- Deliver all messages from my_high_seq_recieved to the last gap (rhbz#722522)
- merge upstream commit e530376a60dc862f135bd0d4c52aebb43d948423 (rhbz#722522)

* Thu Sep 08 2011 Jan Friesse <jfriesse@redhat.com> 1.4.1-3
- Resolves: rhbz#722469
- totemconfig: change minimum RRP threshold
- merge upstream commit b1aba94732edc2ff084b7dd559a08b687f464ed0 (rhbz#722469)

* Tue Sep 06 2011 Jan Friesse <jfriesse@redhat.com> 1.4.1-2
- Resolves: rhbz#722469
- Resolves: rhbz#732698
- rrp: Handle endless loop if all ifaces are faulty (rhbz#722469)
- merge upstream commit dc862e15cc084926eccc5e1ff3241611c0cb54f0 (rhbz#722469)
- rrp: Higher threshold in passive mode for mcast (rhbz#722469)
- merge upstream commit 4e32c3112a2f13a302709d72b0ae989287a48563 (rhbz#722469)
- Ignore memb_join messages during flush operations (rhbz#732698)
- merge upstream commit be608c050247e5f9c8266b8a0f9803cc0a3dc881 (rhbz#732698)

* Tue Jul 26 2011 Jan Friesse <jfriesse@redhat.com> 1.4.1-1
- Resolves: rhbz#725058
- Related: rhbz#692620
- Rebase to Corosync 1.4.1

* Wed Jul 20 2011 Jan Friesse <jfriesse@redhat.com> 1.4.0-2
- Change attributes of cluster log directory

* Wed Jul 20 2011 Jan Friesse <jfriesse@redhat.com> 1.4.0-1
- Resolves: rhbz#709758
- Resolves: rhbz#722522
- Resolves: rhbz#692620
- Resolves: rhbz#529136
- Resolves: rhbz#696883
- Resolves: rhbz#707876
- Resolves: rhbz#712115
- Resolves: rhbz#722469
- Resolves: rhbz#696887
- Resolves: rhbz#707860
- Resolves: rhbz#712126
- Resolves: rhbz#712188
- Resolves: rhbz#599327
- Resolves: rhbz#667652
- Resolves: rhbz#677583
- Resolves: rhbz#688260
- Resolves: rhbz#707862
- Resolves: rhbz#707867
- Resolves: rhbz#707873
- Resolves: rhbz#707875
- Resolves: rhbz#682813
- Rebase to Corosync 1.4.0

* Tue Apr 12 2011 Steven Dake <sdake@redhat.com> 1.2.3-36
- Resolves: rhbz#629380
- merge upstream commit fd78f27715be326c6fe5439fa7e8d8077642db64 (rhbz#629380)
- Place statistics changes outside of IPC mutexes to avoid deadlocks (rhbz#629380)

* Mon Apr 11 2011 Steven Dake <sdake@redhat.com> 1.2.3-35
- Reverts: rhbz#599327
- revert upstream commit 061b770b83a9533dad527eda5f7d41e763cb40da (rhbz#599327)
- revert upstream commit 2f1b7a962911670493d0db3695fc9fb91ceb0c82 (rhbz#599327)
- Display warning and add object database feature to indicate when system
  firewall is enabled. (rhbz#599327)

* Fri Apr 1 2011 Steven Dak <sdake@redhat.com> 1.2.3-34
- Resolves: rhbz#629380
- merge non-committed patch which fixes stack protector failure.  (rhbz#629380)

* Tue Mar 29 2011 Steven Dake <sdake@redhat.com> 1.2.3-33
- Resolves: rhbz#629380
- Fix retrieving application's parent name in notifyd.  (rhbz#629380)
- merge upstream commit 1b7b4f0f888621aff2f8866ac81b4930b4b07c63 (rhbz#629380)
- Remove duplicate quarote events (rhbz#629380)
- merge upstream commit 821e031b925ad3a15ca057f816fecb3568c96cb9 (rhbz#629380)
- Add the service name to the connection name in statistics (rhbz#629380)
- merge upstream commit 78ae800f80fa9cd0fe593724f5c64138c205fec5 (rhbz#629380)
- Fix shutdown when a confdb client is still connected (rhbz#629380)
- merge upstream commit 8b1492b50b64725d72ae9c301682ad9a489de344 (rhbz#629380) 
- Fix compiler error with previous commit (rhbz#629380)
- merge upstream commit 5da31206bbb9bb0d1f80907e53a5798204eaf594 (rhbz#629380)

* Thu Mar 24 2011 Steven Dake <sdake@redhat.com> 1.2.3-32
- Resolves: rhbz#629380
- Resolves: rhbz#688691
- Resolves: rhbz#675783
- Only dispatch notification messages one message at a time. (rhbz#629380)
- merge upstream commit fbae3de885843debe9ccccb363e9ca8e98d5afea. (rhbz#629380)
- Send confdb notifications from the main thread.  (rhbz#629380)
- merge upstream commit abeb02277ee374531b910ce793213e60addb0fb5. (rhbz#629380)
- Remove recv_flush operations from totemsrp to remove recursion
  error.  (rhbz#688691)
- merge upstream commit 336741ee96caf3ae435b609ee8a76788902c9edf. (rhbz#688691)
- Only restore old ring id information once before operational
  state.  (rhbz#675783)
- merge upstream commit 0eabeee63eca7a4cc1d907607057ac668fafbcae.  (rhbz#675783)
- Free recovery messages during operational enter rather then
  via message_free() call.  (rhbz#675783)
- merge upstream commit 0fcf760977a73ef78bacff47e61c30ba21929faa.  (rhbz#675783)

* Mon Mar 21 2011 Steven Dake <sdake@redhat.com> 1.2.3-31
- Resolves: rhbz#688691
- Remove assertion during corosync shutdown.  (rhbz#688691)
- merge upstream commit 92a3a1aa9d07e769eb6bc59467454e0316549cf6 (rhbz#688691)

* Tue Mar 15 2011 Steven dake <sdake@redhat.com> 1.2.3-30
- Resolves: rhbz#684928
- Resolves: rhbz#684930
- Fix ttl defaults and range checking.  (rhbz#684928)
- merge upstream commit c5ee8757eb2a7026b26a6410f3f068c4797abcf8 (rhbz#684928)
- Remove the ttl option from the udpu code and rely on kernel
  ttl defaults (rhbz#684930)
- merge upstream commit 48cbb33d11fed7ed9db5e7c723cf84eb35cd9d29 (rhbz#684930)

* Tue Mar 8 2011 Steven Dake <sdake@redhat.com> 1.2.3-29
- Resolves: rhbz#675783
- Fix problem that leads to abort when token lost in
  recovery sate.  (rhbz#675783)
- merge upstream commit 6aa47fde953bf2179f5bd2dd07815fc7d80f47bb

* Mon Feb 28 2011 Steven Dake <sdake@redhat.com> 1.2.3-28
- Resolves: rhbz#677975
- Fix problem where objdb handle destroy is not called in
  clear_object.  (rhbz#677975)
- merge upstream commit ea18c71936edf8cdc647245374f3a7932ac7e686
- Fix problem where all items are not iterated in
  object_reload_notification.  (rhbz#677975)
- merge upstream commit 7f2e1da84d5883176f0f95936b8a4bf21de12a0a

* Thu Feb 24 2011 Steven Dake <sdake@redhat.com> 1.2.3-27
- Resolves: rhbz#680258
- Resolves: rhbz#675099
- Fix problem where corosync can't be built on an older
  installation. (rhbz#680258)
- merge upstream commit 5ee4fe19db4b1e9c3984a9bf1645b8cf6d711f3d
- Avoid abort if existing ring id file does not contain
  atleast 8 bytes.  (rhbz#675099)
- merge upstream commit bb35b86fef4f256a21993f73b71fd512d4763e2f

* Tue Feb 8 2011 Steven Dake <sdake@redhat.com> 1.2.3-26
- Resolves: rhbz#675859
- finish SNMP/DBUS integration
- Add a list of member nodes into the object database. (rhbz#675859)
- merge upstream commit 5af39894067252574020c60b1420599c12ca2027
- Add a list of member nodes into the object database. (rhbz#675859)
- merge upstream commit 732f761cfb89dc8e34d7330cf93ef07ea5815d16
- Delete trackers when an object is deleted.  (rhbz#675859)
- merge upstream commit 36265c20fb623e008e2774a89dd61a08956b65d1
- Make node state a string instead of integer. (rhbz#675859)
- merge upstream commit 8699ed2309340d45f090ff1a9c614e23110b66a9
- fix some strange typing that results in segfaults when using some
apis. (rhbz#675859)
- merge upstream commit 42a44572d892c4981ba3219933aa3d8e131b2d5c
- Fix order of parent and objct handles in object_created_notification
- merge upstream commit 267446a1524e442af4de4e60a2eb79e5ae561a7b
- Fix key name length on "join_count" (rhbz#675859)
- merge upstream commit 3c75fc86755da5c21b4a7620d1e92f0f3e46ce72

* Mon Feb 7 2011 Steven Dake <sdake@redhat.com> 1.2.3-25
- Resolves: rhbz#675741
- fix regression where version information for package is not set properly.

* Fri Feb 4 2011 Steven Dake <sdake@redhat.com> 1.2.3-24
- Resolves: rhbz#629380
- merge upstream commit 7bb8cd296715aaf82ba2184baa5eaf7456010116 (rhbz#629380)
- Increase space for application names in objdb (rhbz#629380)
- merge upstream commit 9415f6d0245d0375f3fc2622931584fc6d617fbf (rhbz#629380)
- Add confdb_object_name_get (rhbz#629380)
- merge upstream commit 159bdf75f33a6f9f8c6746ec1519d26d95fb4e8c (rhbz#629380)
- Add dbus and snmp notifier (rhbz#629380)
- merge upstream commit e48599638375d3ac72919227c6d764974d5ed5f5 (rhbz#629380)
- Make snmp mib match what is sent over dbus (rhbz#629380)
- merge upstream commit d7a9a2519655baf2cd7b25b8b86fb234afa3a650 (rhbz#629380)
- Match mib to notifyd and add SNMP quorum events (rhbz#629380)
- merge upstream commit ae8b5a389a20f15852579baa9e100fda36056ffa (rhbz#629380)
- expand the descriptions of the notifications (rhbz#629380)
- merge upstream commit 4f881071dc3eff5eed83b419154ff47b8ccaf7f7
- fix merge conflicts from 159bdf75f33a6f9f8c6746ec1519d26d95fb4e8c (rhbz#629380)


* Fri Feb 4 2011 Steven Dake <sdake@redhat.com> 1.2.3-23
- Resolves: rhbz#599327
- Resolves: rhbz#613836
- Resolves: rhbz#619918
- Resolves: rhbz#639023
- Resolves: rhbz#640311
- Resolves: rhbz#665165
- Resolves: rhbz#626962
- Resolves: rhbz#626962
- Resolves: rhbz#568164
- merge upstream commit 061b770b83a9533dad527eda5f7d41e763cb40da (rhbz#599327)
- merge upstream commit 2f1b7a962911670493d0db3695fc9fb91ceb0c82 (rhbz#599327)
- Display warning and add object database feature to indicate when system
  firewall is enabled. (rhbz#599327)
- merge upstream commit 9dfb3bbdb325c3908b108943094ca703d4bdfa8f (rhbz#613836)
- Indicate error when multicast address is incorrectly configured by
  user. (rhbz#613836)
- merge upstream commit 6ecad521035e3fe065140091f3cb277e3045f1c6 (rhbz#619918)
- Send error back to API rather then segfaulting corosync if error occured
  duing connection setup (rhbz#619918)
- merge upstream commit 82701ac43d1898f8b824d00fb72ec3065eb34746  (rhbz#639023)
- Remove delay on normal shutdown of corosync for clients (rhbz#639023)
- merge upstream commit d3b983953d43dd17162be04de405d223fb21cd26 (rhbz#640311)
- Add a ttl configuration option to corosync (rhbz#640311)
- merge upstream commit b57573b037aa2737aed2ba706bf55a4599884641 (rhbz#665165)
- Remove shared memory leak in clients if corosync faults (rhbz#665165)
- merge upstream commit b0ac86d3dd37d3a13c3c7ed0442b45ef94554321 (rhbz#626962)
- Since Corosync won't work with multiple instances running, only allow
  one instance to run. (rhb#626962)
- merge upstream commit 679294652f655ab217cbef958d79330049513003 (rhbz#614104)
- Resolve problem where if corosync init script was run by another
  service (such as cman), the init script will block (rhbz#614104)
- merge upstream commit 196d8dc6c2575476d936798f833ec40d50ffa15d (rhbz#568164)
- Add UDPU transport - set buffer sizes properly (rhbz#568164)
- merge upstream commit cab2a2d4803d8d574d61b482edf1c4705160c1d9 (rhbz#568164)
- Add UDPU transport - flushing code introducing data corruption. (rhbz#568164)
- merge upstream commit 893615057777537a86cd7c17597da44f23ac5cd8 (rhbz#568164)
- Add UDPU transport - main work. (rhbz#568164)
- merge upstream commit 0fa7bce07240670f699fe4b6b7d473ce2bcb1bec (rhbz#568164)
- Add UDPU transport - build system dependencies (rhbz#568164)
- merge upstream commit ba021fc66d3fce5eb87006c19192ea3042cd69d7 (rhbz#568164)
- Add UDPU transport - build system dependencies (rhbz#568164)

* Tue Jan 11 2011 Steven Dake <sdake@redhat.com> 1.2.3-22
- Resolves: rhbz#619496
- merge upstream commit bab4945b57c150301c034085f3ce7b4187b6c864
-  Works around problem where some switch hardware delays multicast
-  packets compared to the unicast token.  This would result in messages
-  being retransmitted when no retransmission was necessary.

* Tue Sep 7 2010 Steven Dake <sdake@redhat.com> 1.2.3-21
- Resolves: rhbz#630106
- merge upstream revision 3040 - change stop level from 20 to 80.

* Wed Aug 18 2010 Steven Dake <sdake@redhat.com> 1.2.3-20
- Resolves: rhbz#623790
- properly apply patch from 1.2.3-19

* Tue Aug 17 2010 Steven Dake <sdake@redhat.com> 1.2.3-19
- Resolves: rhbz#623790
- Add upstream revision 3023 - Properly detect server failure instead of falsely
  detecting during a configuration change.

* Tue Aug 3 2010 Steven Dake <sdake@redhat.com> 1.2.3-18
- Resolves: rhbz#619565
- Add upstream revision 3013 - dont cancel token retransmit timeout on receipt
  of a multicast message.

* Tue Jul 27 2010 Steven Dake <sdake@redhat.com> 1.2.3-17
- Resolves: rhbz#618570
- Add upstream revision 3006 - Remove consensus timeout floor check that leads
  to exit in two node clusters with smaller consensus timeouts.

* Thu Jul 22 2010 Angus Salkeld <asalkeld@redhat.com> 1.2.3-16
- Resolves: rhbz#579126
- Add upstream revision 3004 - Fix merge error with revision 3001.
- Add upstream revision 3003 - Fix problem where flow control could lock
  up ipc under very heavy load in very rare circumstances.
* Mon Jul 19 2010 Steven Dake <sdake@redhat.com> 1.2.3-15
- Resolves: rhbz#611676
- Add upstream revision 3000 - ensure aborts happen even if the currently
  running sync engine doesn't have an abort operation.
- Add upstream revision 2999 - reset internal variable in syncv2 on
  configuration change.

* Mon Jul 19 2010 Steven Dake <sdake@redhat.com> 1.2.3-14
- Resolves: rhbz#615203
- Add upstream revision 2998 - Fix logging_daeon cofig parser code.

* Wed Jul 14 2010 Steven Dake <sdake@redhat.com> 1.2.3-13
- Resolves: rhbz#614219
- Add upstream revision 2989 - Don't reset the token timer when a retransmitted
  token is received.  Only reset when a token is received.

* Wed Jul 7 2010 Steven dake <sdake@redhat.com> 1.2.3-12
- Resolves: rhbz#612292
- Add upstream revision 2987 - speed up connection process as a result of
  performance regression in upstream revision 2973.

* Tue Jul 6 2010 Steven Dake <sdake@redhat.com> 1.2.3-11
- Resolves: rhbz#580741
- Resolves: rhbz#605313
- Add upstream revision 2985 - fix fail list fault that occurs in very rare
  circumstances.
- Add upstream revision 2977 - fix mutex deadlock that occurs during cman
  reload.

* Tue Jul 6 2010 Steven Dake <sdake@redhat.com> 1.2.3-10
- Resolves: rhbz#583844
- Add upstream trunk revision 2814 - fix syncing of cpg downlist in certain circumstances
- Add upstream trunk revision 2785 - fix syncing of cpg downlist in certain circumstances.
- Add upstream trunk revision 2801 - fix syncing of cpg downlist in certain circumstances.
 
* Wed Jun 30 2010 Steven Dake <sdake@redhat.com> 1.2.3-9
- Resolves: rbhz#606463
- Add upstream revision 2978 - use freopen as to not cause glibc/fork to
  segfault in some rare circumstances when using pacemaker.

* Tue Jun 29 2010 Steven Dake <sdake@redhat.com> 1.2.3-8
- Resolves: rhbz#609198
- Add upstream revision 2975 - properly size all buffers used to describe the
  file names to PATH_MAX used in mappings in ipc layer.

* Tue Jun 29 2010 Steven dake <sdake@redhat.com> 1.2.3-7
- Resolves: rhbz#607738
- Add upstream revision 2973 - if /dev/shm is full, ipc clients will bus error - return error instead

* Mon Jun 28 2010 Steven Dake <sdake@redhat.com> 1.2.3-6
- Resolves: rhbz#596550
- Resolves: rhbz#606335
- Resolves: rhbz#607480
- Resolves: rhbz#607292
- Add upstream revision 2965 - add a man page for corosync-blackbox
- Add upstream revision 2966 - add a man page for corosync
- Add upstream revision 2967 - Add makefile and specfile changes to support 2965/2966
- Add upstream revision 2968 - remove use of pathconf which can fail resulting in segfault
- Add upstream revision 2969 - remove use of pathconf which can fail resulting in segfault
- Add upstream revision 2971 - add /var/log/cluster as owned directory and change example config file to log in /var/log/cluster

*Mon Jun 28 2010 Steven Dake <sdake@redhat.com> 1.2.3-5
- Reverts: rhbz#583844
- Revert trunk revision 2814 - fix syncing of cpg downlist in certain circumstances
- Revert upstream trunk revision 2785 - fix syncing of cpg downlist in certain circumstances.
- Revert upstream trunk revision 2801 - fix syncing of cpg downlist in certain circumstances.

* Tue Jun 22 2010 Steven Dake <sdake@redhat.com> 1.2.3-4
- Resolves: rhbz#583844
- Add trunk revision 2814 - fix syncing of cpg downlist in certain circumstances

* Mon Jun 21 2010 Steven Dake <sdake@redhat.com> 1.2.3-3
- Resolves: rhbz#600118
- Resolves: rhbz#606463
- Resolves: rhbz#583844
- Resolves: rhbz#605860
- Resolves: rhbz#605860
- Add upstream trunk revision 2785 - fix syncing of cpg downlist in certain circumstances.
- Add upstream trunk revision 2799 - fix problem where blackbox data isn't written during sos requests
- Add upstream trunk revision 2801 - fix syncing of cpg downlist in certain circumstances.
- Add upstream revision 2951 - fix segfault in fork() inside pacemaker service engine.
- Add upstream revision 2952 - fix problem where corosync deadlocks on single cpu system in spinlock call
- Add upstream revision 2954 - fix problem where totem stats updater triggers segfault when it's timer expires during shutdown

* Tue Jun 15 2010 Steven Dake <sdake@redhat.com> 1.2.3-2
- Resolves: rhbz#603886
- Resolves: rhbz#601018
- Resolves: rhbz#600068
- Resolves: rhbz#600043
- Resolves: rhbz#598680
- Resolves: rhbz#601011
- Resolves: rhbz#596550
- Resolves: rhbz#596552
- Resolves: rhbz#596405
- Resolves: rhbz#594924
- Resolves: rhbz#583844
- Add upstream revision 2947 - send CPG_REASON_PROCDOWN instead of
  CPG_REASON_LEAVE on proces exit.
- Add upstream revision 2945 - object_key_iter can dereference an invalid
  pointer
- Add upstream revision 2938 - have logsys use file mapped backing properly as
  intended
- Add upstream revision 2937 - handle sem_wait interrupted by signal properly
- Add upstream revision 2936 - fix fail to recv logic which happens rarely on
  high loss networks
- Add upstream revision 2935 - fix last_aru logic
- Add upstream revision 2934 - evs service fails to deliver messages
- Add upstream revision 2932 - Add man page for corosync-quorumtool
- Add upstream revision 2931 - Add man page for corosync-pload
- Add upstream revision 2930 - Add man page for corosync-fplay
- Add upstream revision 2929 - Add man page for corosync-cpgtool
- Add upstream revision 2928 - Add man page for corosync-cfgtool
- Add upstream revision 2927 - Add man page for corosync-keygen
- Add upstream revision 2926 - Update of corosync_overview man page
- Add upstream revision 2925 - resolve undefined behavior caused by sem_wait
  interruption by signals in coroipc
- Add upstream revision 2924 - Resolve problem where errant memcpy() operation
  sets incorrect scheduling parameters
- Add upstream revision 2923 - corosync won't build without corosync already
  intalled

* Wed May 19 2010 Steven dake <sdake@redhat.com> 1.2.3-1
- Resolves: rhbz#583800
- Rebase to upstream 1.2.3.
- Resolves 43 errors found with coverity.
- Fixes defects with totemsrp in 90% multicast message loss cases found
  through a field deployment.

* Sun May 16 2010 Steven Dake <sdake@redhat.com> 1.2.2-1
- Resolves: rhbz#583800
- Resolves: rhbz#553375
- Resolves: rhbz#582947
- Resolves: rhbz#553375
- Rebase to upstream 1.2.2.
- Add upstream trunk revision 2770 to add cpg_model_initialize api.

* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.2.1-5
- Resolves: rhbz#590983
- Do not build corosync on ppc and ppc64

* Tue Mar 23 2010 Steven Dake <sdake@redhat.com> 1.2.1-4
- Resolves: rhbz#574516
- Rebase to upstream 1.2.1.

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.2.0-3
- Resolves: rhbz#567995
- Do not build corosync on s390 and s390x

* Tue Jan 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.2.0-2
- Resolves: rhbz#554855
- Do not build IB support on s390 and s390x

* Tue Dec  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.2.0-1
- New upstream release
- Use global instead of define
- Update Source0 url
- Use more %name macro around
- Cleanup install section. Init script is now installed by upstream
- Cleanup whitespace
- Don't deadlock between package upgrade and corosync condrestart
- Ship service.d config directory
- Fix Conflicts vs Requires
- Ship new sam library and man pages

* Fri Oct 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.2-1
- New upstream release fixes major regression on specific loads

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.1-1
- New upstream release

* Fri Sep 25 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.0-1
- New upstream release
- spec file updates:
  * enable IB support
  * explicitly define built-in features at configure time

* Tue Sep 22 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.0.1-1
- New upstream release
- spec file updates:
  * use proper configure macro

* Tue Jul 28 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.0.0-3
- spec file updates:
  * more consistent use of macros across the board
  * fix directory ownership

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.0.0-1
- New upstream release

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.100-1
- New upstream release

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.98-1
- New upstream release
- spec file updates:
  * Drop corosync-trunk patch and alpha tag.
  * Fix alphatag vs buildtrunk handling.
  * Drop requirement on ais user/group and stop creating them.
  * New config file locations from upstream: /etc/corosync/corosync.conf.

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.97-1.svn2233
- spec file updates:
  * Update to svn version 2233 to include library linking fixes

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.97-1.svn2232
- New upstream release
- spec file updates:
  * Drop pkgconfig fix that's now upstream
  * Update to svn version 2232
  * Define buildtrunk if we are using svn snapshots
  * BuildRequires: nss-devel to enable nss crypto for network communication
  * Force autogen invokation if buildtrunk is defined
  * Whitespace cleanup
  * Stop shipping corosync.conf in favour of a generic example
  * Update file list

* Mon Mar 30 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.95-2
- Backport svn commit 1913 to fix pkgconfig files generation
  and unbreak lvm2 build.

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.95-1
- New upstream release
- spec file updates:
  * Drop alpha tag
  * Drop local patches (no longer required)
  * Allow to build from svn trunk by supporting rpmbuild --with buildtrunk 
  * BuildRequires autoconf automake if building from trunk
  * Execute autogen.sh if building from trunk and if no configure is available
  * Switch to use rpm configure macro and set standard install paths
  * Build invokation now supports _smp_mflags
  * Remove install section for docs and use proper doc macro instead
  * Add tree fixup bits to drop static libs and html docs (only for now)
  * Add LICENSE file to all subpackages
  * libraries have moved to libdir. Drop ld.so.conf.d corosync file
  * Update BuildRoot usage to preferred versions/names

* Tue Mar 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94-5.svn1797
- Update the corosync-trunk patch for real this time.

* Tue Mar 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94-4.svn1797
- Import fixes from upstream:
  * Cleanup logsys format init around to use default settings (1795)
  * logsys_format_set should use its own internal copy of format_buffer (1796)
  * Add logsys_format_get to logsys API (1797)
- Cherry pick svn1807 to unbreak CPG.

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94-3.svn1794
- Import fixes from upstream:
  * Add reserve/release feature to totem message queue space (1793)
  * Fix CG shutdown (1794)

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94-2.svn1792
- Import fixes from upstream:
  * Fix uninitialized memory. Spotted by valgrind (1788)
  * Fix logsys_set_format by updating the right bits (1789)
  * logsys: re-add support for timestamp  (1790)
  * Fix cpg crash (1791)
  * Allow logsys_format_set to reset to default (1792)

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.94-1
- New upstream release.
- Drop obsolete patches.
- Add soname bump patch that was missing from upstream.

* Wed Feb 25 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.93-4
- Add Makefile fix to install all corosync tools (commit r1780)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.93-2
- Rename gcc-4.4 patch to match svn commit (r1767).
- Backport patch from trunk (commit r1774) to fix quorum engine.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.93-1
- New upstream release.
- Drop alphatag from spec file.
- Drop trunk patch.
- Update Provides for corosynclib-devel.
- Backport gcc-4.4 build fix from trunk.

* Mon Feb  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.92-7.svn1756
- Update to svn trunk at revision 1756 from upstream.
- Add support pkgconfig to devel package.
- Tidy up spec files by re-organazing sections according to packages.
- Split libraries from corosync to corosynclib.
- Rename corosync-devel to corosynclib-devel.
- Comply with multiarch requirements (libraries).

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.92-6.svn1750
- Update to svn trunk at revision 1750 from upstream.
- Include new quorum service in the packaging.

* Mon Dec 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.92-5.svn1709
- Update to svn trunk at revision 1709 from upstream.
- Update spec file to include new include files.

* Wed Dec 10 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.92-4.svn1707
- Update to svn trunk at revision 1707 from upstream.
- Update spec file to include new lcrso services and include file.

* Mon Oct 13 2008 Dennis Gilmore <dennis@ausil.us> - 0.92-3
- remove ExclusiveArch line

* Fri Sep 24 2008 Steven Dake <sdake@redhat.com> - 0.92-2
- Add conflicts for openais and openais-devel packages older then 0.90.

* Wed Sep 24 2008 Steven Dake <sdake@redhat.com> - 0.92-1
- New upstream release corosync-0.92.

* Sun Aug 24 2008 Steven Dake <sdake@redhat.com> - 0.91-3
- move logsys_overview.8.* to devel package.
- move shared libs to main package.

* Wed Aug 20 2008 Steven Dake <sdake@redhat.com> - 0.91-2
- use /sbin/service instead of calling init script directly.
- put corosync-objctl man page in the main package.
- change all initrddir to initddir for fedora 10 guidelines.

* Thu Aug 14 2008 Steven Dake <sdake@redhat.com> - 0.91-1
- First upstream packaged version of corosync for rawhide review.
