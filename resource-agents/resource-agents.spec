# RHEL-6 specific changes to spec file vs upstream
#
# drop Requires: fsck.xfs (another rhn channel, not available with HA)
# ExclusiveArch: i686 x86_64
# don't build ldirectord
# drop drbd, smb and tomcat5 in install section
# Conflicts with old rgmanager

#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#






# 
# Since this spec file supports multiple distributions, ensure we
# use the correct group for each.
#

%global sap_script_prefix sap_redhat_cluster_connector
%global sap_hash 6353d27

# determine the ras-set to process based on configure invokation
%bcond_without rgmanager
%bcond_without linuxha

Name:		resource-agents
Summary:	Open Source HA Reusable Cluster Resource Scripts
Version:	3.9.5
Release:	34%{?rcver:%{rcver}}%{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}%{?dist}.2
License:	GPLv2+ and LGPLv2+
URL:		http://to.be.defined.com/
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Source0:	%{name}-%{version}-custom.tar.bz2
Source1:	%{sap_script_prefix}-%{sap_hash}.tar.gz
Patch0:		bz1047999-oracle-failure-to-stop-if-not-running.patch
Patch1:		bz960186-properly-detect-oracledb-exit.patch
Patch2:		bz960186-properly-detect-orainstance-exit.patch
Patch3:		bz1038474-fix-findmnt-usage.patch
Patch4:		bz1089004-force-kill-processes-accessing-shared-lib-on-mount.patch
Patch5:		bz1095943-ability-to-avoid-block-during-stop.patch
Patch6:		bz1023606-passing-ocft-tests.patch
Patch7:		bz974239-nfs-syntax-fix.patch
Patch8:		bz1091102-nfs-updates.patch
Patch9:		bz1059981-db2-support.patch 
Patch10:	bz1039119-ip-monitor-link-on-off.patch
Patch11:	bz1094789-fix-bindmount-metadata.patch
Patch12:	bz1115490-bind-mount-metadata-fix.patch
Patch13:	bz960186-oracledb-ps-match-fix.patch
Patch14:	bz1159805-ipv6-ua.patch
Patch15:	bz1175801-lvm-by-vg-stip-tag-on-stop.patch
Patch16:	bz1096376-nfs-custom-port-config-options.patch
Patch17:	bz1096990-fixes-passing-some-mount-options.patch
Patch18:	bz1134960-fixes-undefined-variable-warning-in-fs-lib.patch
Patch19:	bz1150702-fixes-mysql-not-stopped-if-data-fs-unavail.patch
Patch20:	bz1159018-fixes-postgres-agent-not-detected-correct-.patch
Patch21:	bz1173128-handle-nfs-path-ending-in-correctly.patch
Patch22:	bz1191669-oracle-errors-fix.patch
Patch23:	bz1181187-IPaddr2-findif.sh-Robust-parameter-checking-for.patch
Patch24:	bz1183735-fix-fs-lib-health-check.patch
Patch25:	bz1183148-mysql-handle-alt-user.patch 
Patch26:	bz1085109.patch
Patch27:	bz1168251-SAPHana-agents.patch
Patch28:	bz1150655-nginx-agent.patch
Patch29:	bz1179412-nfs-sysconfig-fix.patch
Patch30:	bz1168251-SAPHana-agents-update.patch
Patch31:	bz1168251-SAPHana-agents-update2.patch
Patch32:	bz1168251-SAPHana-agents-update3.patch
Patch33:	bz1168251-SAPHana-agents-update4.patch
Patch34:	bz1200639-orainstance-wait-90sec.patch
Patch35:	bz1191247-dad-ipv6.patch
Patch36:	bz1207285-mysql-slow-start-status-check-fix.patch
Patch37:	bz1234777-handle-failure-state.patch
Patch38:	bz1070479-oracle-agents.patch
Patch39:	bz1200903-saphana-mcos-support.patch
Patch40:	bz1269897-sap_redhat_cluster_connector-support-for-dash-in-hostnames.patch
Patch41:	bz1276698-use-ipv6-dad-for-collision-detection.patch
Patch42:	bz1266173-lvm-raid-segment-support.patch
Patch43:	bz1280319-tomcat-fix-selinux-enforced.patch
Patch44:	bz1286650-virtualdomain-add-migrate_options-parameter.patch
Patch45:	bz1024505-fs-remove-tmpfs.patch
Patch46:	bz1292054-mysql-fix-tmpfile-leak.patch
Patch47:	bz1285921-vm-add-migrate_options-parameter.patch
Patch48:	bz1272587.patch
Patch49: 	bz1302545-portblock.patch
Patch50:	bz1086838-oracle-data-guard.patch
Patch51:	bz1311963-rgmanager-fix-clumanager-statd-ownership.patch
Patch52:	bz1329547-tickle_tcp-fix.patch

Obsoletes:	heartbeat-resources <= %{version}
Provides:	heartbeat-resources = %{version}
Conflicts:	rgmanager < 3.0.12.1

ExclusiveArch: i686 x86_64

## Setup/build bits
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: automake autoconf pkgconfig
BuildRequires: perl python-devel
BuildRequires: libxslt glib2-devel
BuildRequires: which

%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
BuildRequires: cluster-glue-libs-devel
BuildRequires: docbook-style-xsl docbook-dtds
%if 0%{?rhel} == 0
BuildRequires: libnet-devel
%endif
%endif

%if 0%{?suse_version}  
%if 0%{?suse_version} >= 1140
BuildRequires:  libnet1
%else
BuildRequires:  libnet
%endif
BuildRequires:  libglue-devel
BuildRequires:  libxslt docbook_4 docbook-xsl-stylesheets
%endif

## Runtime deps
## These apply to rgmanager agents only to guarantee agents
## are functional
%if %{with rgmanager}
# system tools shared by several agents
Requires: /bin/bash /bin/grep /bin/sed /bin/gawk
Requires: /bin/ps /usr/bin/pkill /bin/hostname
Requires: /sbin/fuser
Requires: /sbin/findfs /bin/mount

# fs.sh
Requires: /sbin/quotaon /sbin/quotacheck
Requires: /sbin/fsck
Requires: /sbin/fsck.ext2 /sbin/fsck.ext3 /sbin/fsck.ext4

# ip.sh
Requires: /sbin/ip /usr/sbin/ethtool
Requires: /sbin/rdisc /usr/sbin/arping /bin/ping /bin/ping6

# lvm.sh
Requires: /sbin/lvm

# netfs.sh
Requires: /sbin/mount.nfs /sbin/mount.nfs4 /sbin/mount.cifs
Requires: /usr/sbin/rpc.nfsd /sbin/rpc.statd /usr/sbin/rpc.mountd
%endif

## Runtime dependencies required to guarantee heartbeat agents
## are functional
%if %{with linuxha}
# tools needed for Filesystem resource
Requires: psmisc
%endif

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager
service managers.

%ifarch x86_64
%package sap
License:      GPLv2+
Summary:      SAP cluster resource agents and connector script
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:     %{name} = %{version}-%{release}
Requires:	perl

%description sap
The SAP resource agents and connector script interface with 
Pacemaker to allow SAP instances to be managed in a cluster
environment.
%endif

%ifarch x86_64
%package sap-hana
License:      GPLv2+
Summary:      SAP HANA cluster resource agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:     %{name} = %{version}-%{release}
Requires:	perl

%description sap-hana
The SAP HANA resource agents interface with  Pacemaker to allow
SAP instances to be managed in a cluster environment.
%endif

%prep
%if 0%{?suse_version} == 0 && 0%{?fedora} == 0 && 0%{?centos_version} == 0 && 0%{?rhel} == 0
%{error:Unable to determine the distribution/version. This is generally caused by missing /etc/rpm/macros.dist. Please install the correct build packages or define the required macros manually.}
exit 1
%endif
%setup -q -n %{name}-%{version}-custom
%setup -a 1 -n %{name}-%{version}-custom

%patch0 -p1
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
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1

%build
./autogen.sh

chmod 755 heartbeat/nfsnotify
chmod 755 heartbeat/SAPHana
chmod 755 heartbeat/SAPHanaTopology

%if 0%{?fedora} >= 11 || 0%{?centos_version} > 5 || 0%{?rhel} > 5
CFLAGS="$(echo '%{optflags}')"
%global conf_opt_fatal "--enable-fatal-warnings=no"
%else
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
%global conf_opt_fatal "--enable-fatal-warnings=yes"
%endif

%if %{with rgmanager}
%global rasset rgmanager
%endif
%if %{with linuxha}
%global rasset linux-ha
%endif
%if %{with rgmanager} && %{with linuxha}
%global rasset all
%endif

export CFLAGS

%configure \
	%{conf_opt_fatal} \
	--with-pkg-name=%{name} \
	--with-ras-set=%{rasset}

%if %{defined jobs}
JFLAGS="$(echo '-j%{jobs}')"
%else
JFLAGS="$(echo '%{_smp_mflags}')"
%endif

make $JFLAGS

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

test -d %{buildroot}/usr/sbin || mkdir %{buildroot}/usr/sbin
mv %{sap_script_prefix}-%{sap_hash}/sap_redhat_cluster_connector %{buildroot}/usr/sbin/sap_redhat_cluster_connector

## tree fixup
# remove docs (there is only one and they should come from doc sections in files)
rm -rf %{buildroot}/usr/share/doc/resource-agents

# drop drbd, smb and tomcat5
(
  cd %{buildroot}/%{_datadir}/cluster
  rm -f drbd.* smb.sh tomcat-5.*
)
ln -s /usr/share/cluster/relaxng/ra-api-1-modified.dtd %{buildroot}/usr/share/resource-agents/

##
# Create symbolic link between IPAddr and IPAddr2
##
rm -f %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr
ln -s /usr/lib/ocf/resource.d/heartbeat/IPaddr2 %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPLv3 ChangeLog
%if %{with linuxha}
%doc doc/README.webapps
%doc %{_datadir}/%{name}/ra-api-1.dtd
%doc %{_datadir}/%{name}/ra-api-1-modified.dtd
%endif

%if %{with rgmanager}
%{_datadir}/cluster
%{_sbindir}/rhev-check.sh
%endif

%if %{with linuxha}
%dir /usr/lib/ocf
%dir /usr/lib/ocf/resource.d
%dir /usr/lib/ocf/lib

/usr/lib/ocf/lib/heartbeat

/usr/lib/ocf/resource.d/heartbeat
# drop the redhat symlink for pacemaker support now
# that the heartbeat agents are supported
%if %{with rgmanager}
%exclude /usr/lib/ocf/resource.d/redhat
%endif

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ocft
%{_datadir}/%{name}/ocft/configs
%{_datadir}/%{name}/ocft/caselib
%{_datadir}/%{name}/ocft/README
%{_datadir}/%{name}/ocft/README.zh_CN

%{_sbindir}/ocft

%{_includedir}/heartbeat

%dir %attr (1755, root, root)	%{_var}/run/resource-agents

%{_mandir}/man7/*.7*

# only exclude these unsupported agents for rhel packages.
%if 0%{?rhel}
###
# Supported, but in another sub package
###
%exclude %{_sbindir}/sap_redhat_cluster_connector
%exclude %{_sbindir}/show_SAPHanaSR_attributes
%exclude /usr/lib/ocf/resource.d/heartbeat/SAP*
%exclude /usr/lib/ocf/lib/heartbeat/sap*
%exclude %{_mandir}/man7/*SAP*

###
# Unsupported
###
%exclude /usr/lib/ocf/resource.d/heartbeat/AoEtarget
%exclude /usr/lib/ocf/resource.d/heartbeat/AudibleAlarm
%exclude /usr/lib/ocf/resource.d/heartbeat/ClusterMon
%exclude /usr/lib/ocf/resource.d/heartbeat/EvmsSCC
%exclude /usr/lib/ocf/resource.d/heartbeat/Evmsd
%exclude /usr/lib/ocf/resource.d/heartbeat/ICP
%exclude /usr/lib/ocf/resource.d/heartbeat/IPv6addr
%exclude /usr/lib/ocf/resource.d/heartbeat/LinuxSCSI
%exclude /usr/lib/ocf/resource.d/heartbeat/ManageRAID
%exclude /usr/lib/ocf/resource.d/heartbeat/ManageVE
%exclude /usr/lib/ocf/resource.d/heartbeat/Pure-FTPd
%exclude /usr/lib/ocf/resource.d/heartbeat/Raid1
%exclude /usr/lib/ocf/resource.d/heartbeat/ServeRAID
%exclude /usr/lib/ocf/resource.d/heartbeat/SphinxSearchDaemon
%exclude /usr/lib/ocf/resource.d/heartbeat/Stateful
%exclude /usr/lib/ocf/resource.d/heartbeat/SysInfo
%exclude /usr/lib/ocf/resource.d/heartbeat/VIPArip
%exclude /usr/lib/ocf/resource.d/heartbeat/WAS
%exclude /usr/lib/ocf/resource.d/heartbeat/WAS6
%exclude /usr/lib/ocf/resource.d/heartbeat/WinPopup
%exclude /usr/lib/ocf/resource.d/heartbeat/Xen
%exclude /usr/lib/ocf/resource.d/heartbeat/anything
%exclude /usr/lib/ocf/resource.d/heartbeat/asterisk
%exclude /usr/lib/ocf/resource.d/heartbeat/eDir88
%exclude /usr/lib/ocf/resource.d/heartbeat/fio
%exclude /usr/lib/ocf/resource.d/heartbeat/iSCSITarget
%exclude /usr/lib/ocf/resource.d/heartbeat/ids
%exclude /usr/lib/ocf/resource.d/heartbeat/iscsi
%exclude /usr/lib/ocf/resource.d/heartbeat/jboss
%exclude /usr/lib/ocf/resource.d/heartbeat/ldirectord
%exclude /usr/lib/ocf/resource.d/heartbeat/lxc
%exclude /usr/lib/ocf/resource.d/heartbeat/pingd
%exclude /usr/lib/ocf/resource.d/heartbeat/pound
%exclude /usr/lib/ocf/resource.d/heartbeat/proftpd
%exclude /usr/lib/ocf/resource.d/heartbeat/scsi2reservation
%exclude /usr/lib/ocf/resource.d/heartbeat/sfex
%exclude /usr/lib/ocf/resource.d/heartbeat/syslog-ng
%exclude /usr/lib/ocf/resource.d/heartbeat/varnish
%exclude /usr/lib/ocf/resource.d/heartbeat/vmware
%exclude /usr/lib/ocf/resource.d/heartbeat/zabbixserver
%exclude /usr/lib/ocf/resource.d/heartbeat/mysql-proxy
%exclude /usr/lib/ocf/resource.d/heartbeat/rsyslog
%exclude /usr/lib/ocf/resource.d/heartbeat/slapd
%exclude %{_mandir}/man7/ocf_heartbeat_AoEtarget.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_AudibleAlarm.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ClusterMon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_EvmsSCC.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Evmsd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ICP.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_IPaddr.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_IPv6addr.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_LinuxSCSI.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageVE.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Pure-FTPd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Raid1.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ServeRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SphinxSearchDaemon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Stateful.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SysInfo.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_VIPArip.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS6.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WinPopup.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Xen.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_anything.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_asterisk.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_eDir88.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_fio.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_iSCSITarget.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ids.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_iscsi.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_jboss.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_lxc.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pingd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pound.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_proftpd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_scsi2reservation.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_sfex.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_syslog-ng.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_varnish.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_vmware.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_zabbixserver.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mysql-proxy.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_rsyslog.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_slapd.7.gz

###
# Other excluded files.
###
# This tool has to be updated for the new pacemaker lrmd.
%exclude %{_sbindir}/ocf-tester
%exclude %{_mandir}/man8/ocf-tester.8*
%exclude %{_sbindir}/sfex_init
%exclude %{_sbindir}/sfex_stat
%exclude %{_libexecdir}/heartbeat/sfex_daemon
%exclude %{_mandir}/man8/sfex_init.8.gz
# ldirectord is not supported
%exclude /etc/ha.d/resource.d/ldirectord
%exclude /etc/init.d/ldirectord
%exclude /etc/logrotate.d/ldirectord
%exclude /usr/sbin/ldirectord
%exclude %{_mandir}/man8/ldirectord.8.gz
%endif # end of rhel excludes

# For compatability with pre-existing agents
%dir %{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/shellfuncs

%{_libexecdir}/heartbeat
%endif

%if %{with rgmanager}
%post -n resource-agents
ccs_update_schema > /dev/null 2>&1 ||:
%endif

%ifarch x86_64
%files sap
%defattr(-,root,root)
%{_sbindir}/sap_redhat_cluster_connector
/usr/lib/ocf/resource.d/heartbeat/SAP*
/usr/lib/ocf/lib/heartbeat/sap*
%{_mandir}/man7/*SAP*
%exclude %{_mandir}/man7/*SAPHana*
%exclude /usr/lib/ocf/resource.d/heartbeat/SAPHana*
%endif

%ifarch x86_64
%files sap-hana
%defattr(-,root,root)
/usr/lib/ocf/resource.d/heartbeat/SAPHana*
%{_mandir}/man7/*SAPHana*
%endif


%changelog
* Mon Apr 25 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-34.2
- tickle_tcp: fix "Failed to open raw socket (Invalid argument)" issue

  Resolves: rhbz#1329547

* Thu Feb 25 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-34
- rgmanager: fix .clumanager/statd ownership in fs.sh and clusterfs.sh

  Resolves: rhbz#1311963

* Thu Feb 25 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-32
- Add portblock resource agent for Pacemaker
- Add Oracle Data Guard resource agent for rgmanager

  Resolves: rhbz#1302545
  Resolves: rhbz#1086838

* Wed Feb 24 2016 Jan Pokorny <jpokorny@redhat.com> - 3.9.5-31
- Fix up for wrongly generated RNG schema for cluster configuration
  wrt. "action" tag

  Related: rhbz#1272587

* Thu Jan 07 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-30
- Add migrate_options parameter to vm.sh

  Resolves: rhbz#1285921

* Mon Dec 21 2015 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-29
- Set VirtualDomain migrate_options default

  Resolves: rhbz#1286650

* Mon Dec 21 2015 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-28
- Use IPv6 DAD for collision detection in IPaddr2
- Add RAID segment type support for HA LVM
- Fix Tomcat SELinux failed in enforcing mode
- Add migrate_options parameter to VirtualDomain
- Remove not-working tmpfs "support" from fs.sh
- Fix tmpfile leak in mysql resource agent

  Resolves: rhbz#1276698
  Resolves: rhbz#1266173
  Resolves: rhbz#1280319
  Resolves: rhbz#1286650
  Resolves: rhbz#1024505
  Resolves: rhbz#1292054

* Mon Dec  7 2015 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-27
- SAP HANA add Multiple Components One System (MCOS) support
- sap_redhat_cluster_connector add support for "-" in hostnames

  Resolves: rhbz#1200903
  Resolves: rhbz#1269897

* Wed Oct 28 2015 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-26
- Match exact Oracle SID to avoid waiting for 90 seconds and killing other databases if their names include the name of the database you're trying to stop
- Use DAD to check for address collision instead of ping for IPv6 in rgmanager
- MySQL wait up to "startup_wait" seconds for mysqld to create PID
- Handle failure state during stop in orainstance.sh
- Add Oracle resource agents for Pacemaker

  Resolves: rhbz#1200639
  Resolves: rhbz#1191247
  Resolves: rhbz#1207285
  Resolves: rhbz#1234777
  Resolves: rhbz#1070479

* Thu Sep 10 2015 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.5-25
- SAP Hana update to address several bugs

  Resolves: rhbz#1245730

* Thu May 07 2015 David Vossel <dvossel@redhat.com> - 3.9.5-24
- Update addresses bug fixes for SAP Hana agents.

  Resolves: rhbz#1168251

* Tue Apr 21 2015 David Vossel <dvossel@redhat.com> - 3.9.5-23
- Update addresses bug fixes for SAP Hana agents.

  Resolves: rhbz#1168251

* Thu Apr 09 2015 David Vossel <dvossel@redhat.com> - 3.9.5-22
- Update SAP Hana agents.

  Resolves: rhbz#1168251

* Thu Apr 09 2015 David Vossel <dvossel@redhat.com> - 3.9.5-21
- Place SAP Hana agents in sap-hana subpackage

  Resolves: rhbz#1168251

* Tue Mar 03 2015 David Vossel <dvossel@redhat.com> - 3.9.5-20
- Preserves nfs sysconfig when using nfsserver agent.

  Resolves: rhbz#1179412

* Mon Mar 02 2015 David Vossel <dvossel@redhat.com> - 3.9.5-19
- Introduce the nginx agent.

  Resolves: rhbz#1150655

* Thu Feb 26 2015 David Vossel <dvossel@redhat.com> - 3.9.5-18
- SAP Hana agents.

  Resolves: rhbz#1168251

* Fri Feb 20 2015 David Vossel <dvossel@redhat.com> - 3.9.5-17
- Fixes rgmanager lvm agent's ability to exclusively activate
  volume groups on nodes with aliases

  Resolves: rhbz#1085109

* Fri Feb 20 2015 David Vossel <dvossel@redhat.com> - 3.9.5-16
- Fixes unreliable detection of nic device in IPaddr2
- Fix fs-lib.sh regression in is_alive write test failure detection
- Fix properly handle mysql when alternate user is specified.

  Resolves: rhbz#1181187
  Resolves: rhbz#1183735
  Resolves: rhbz#1183148

* Wed Feb 11 2015 David Vossel <dvossel@redhat.com> - 3.9.5-15
- Prevent oracle agents from failing on non critical errors

  Resolves: rhbz#1151379

* Mon Jan 19 2015 David Vossel <dvossel@redhat.com> - 3.9.5-14
- For lv_by_vg, only strip tag on stop if we are owner.
- NFS custom port config options
- Fixes typo preventing passing "noload" or "data=..." mount options
- Fixes undefined variable warning in fs-lib
- Fixes mysql not stopped if data fs unavailable
- Fixes postgres agent not detected correct user group
- Handle nfs path ending in '/' correctly

  Resolves: rhbz#1161727
  Resolves: rhbz#1096376
  Resolves: rhbz#1096990
  Resolves: rhbz#1134960
  Resolves: rhbz#1150702
  Resolves: rhbz#1159018
  Resolves: rhbz#1173128

* Thu Jul 31 2014 David Vossel <dvossel@redhat.com> - 3.9.5-13
- ip.sh now sends unsolicited advertisement packet for ipv6

  Resolves: rhbz#1159805

* Thu Jul 31 2014 David Vossel <dvossel@redhat.com> - 3.9.5-12
- Properly search for oracldb processes in oracledb.sh stop
  operations.

  Resolves: rhbz#960186

* Mon Jul 07 2014 David Vossel <dvossel@redhat.com> - 3.9.5-11
- Updates required, unique, and primary fields in bind-mount.sh
  metadata

  Resolves: rhbz#1094789

* Thu Jul 03 2014 David Vossel <dvossel@redhat.com> - 3.9.5-10
- Fixes bind-mount.sh metadata function.

  Resolves: rhbz#1094789

* Tue Jun 17 2014 David Vossel <dvossel@redhat.com> - 3.9.5-9
- When signalling pids accessing a mount_point to exit,
  make sure to only signal each pid once.

  Resolves: rhbz#1089004

* Fri Jun 13 2014 David Vossel <dvossel@redhat.com> - 3.9.5-8
- Revert accidental modification of exportfs's
  unlock_on_stop option.
- Add on/off as valid value for ip.sh monitor_link

  Resolves: rhbz#1091102
  Resolves: rhbz#1039119

* Fri Jun 13 2014 David Vossel <dvossel@redhat.com> - 3.9.5-7
- Update force_unmount=safe option so it does not process
  duplicate process ids.

  Resolves: rhbz#1095943

* Fri Jun 13 2014 David Vossel <dvossel@redhat.com> - 3.9.5-6
- Remove db2 exclude entries from spec file.
  Resolves: rhbz#1059981

* Fri Jun 13 2014 David Vossel <dvossel@redhat.com> - 3.9.5-5
- Add support for pacemaker db2 agent
- Fix syntax error in nfsserver.sh
- Updates pacemaker nfs server agents. Adds support for
  nfsnotify agent.

  Resolves: rhbz#1059981
  Resolves: rhbz#1091102
  Resolves: rhbz#974239

* Mon Jun 9 2014 David Vossel <dvossel@redhat.com> - 3.9.5-4
- Introduce passing ocft test cases.

  Resolves: rhbz#1023606

* Mon Jun 9 2014 David Vossel <dvossel@redhat.com> - 3.9.5-3
- Fix usage of findmnt in fs-lib.sh based rgmanager agents.
- When executing force kill of processes using a mountpoint,
  take into account those processes accessing shared memory.
- Add force_unount=safe option to avoid blocking Filesystem
  agent during the stop operation.
- Do not fail during stop if oracle listener is already down. 
- Correctly detect oracledb and orainstanch.sh shutdown.
- Remove unused patches left over from before patches were
  consolidated into the new source files.

  Resolves: rhbz#1038474
  Resolves: rhbz#1089004
  Resolves: rhbz#1095943
  Resolves: rhbz#1047999
  Resolves: rhbz#960186
  Resolves: rhbz#993431

* Sat Jun  7 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.5-2
- Build sap package only on x86_64

  Resolves: rhbz#1031601

* Thu May 29 2014 David Vossel <dvossel@redhat.com> - 3.9.5-1
- Package cleanup. This change is a no-op. The heartbeat
  agents were updated to the 3.9.5 upstream release in this
  package months ago. The release number is now being
  incremented to reflect this.

  Resolves: rhbz#993431

* Fri May 23 2014 David Vossel <dvossel@redhat.com> - 3.9.2-49
- Add iSCSILogicalUnit to rhel supported agents.

  Resolves: rhbz#1075000

* Fri May 09 2014 David Vossel <dvossel@redhat.com> - 3.9.2-48
- Configurable startup_wait timeout for rgmanager's 
  postgres-8.sh resource-agent
- Allow non rhel builds to included unsupported agents.
- Add bind-mount.sh rgmanager resource-agent.
- Add 'statdport' option to nfsserver resource.

  Resolves: rhbz#1035380
  Resolves: rhbz#1069621
  Resolves: rhbz#1094789
  Resolves: rhbz#918315

* Fri Apr 25 2014 David Vossel <dvossel@redhat.com> - 3.9.2-47
- Allow vm.sh to monitor kvm domains without requiring libvirtd
- Adds 'no_kill' option to vm.sh to prevent force killing vm
  during stop operation after timeout expires.

  Resolves: rhbz#853698
  Resolves: rhbz#1079039

* Tue Apr 22 2014 David Vossel <dvossel@redhat.com> - 3.9.2-46
- Updates the ocf:heartbeat:tomcat agent so it can be used
  in rhel6 with Pacemaker.

  Resolves: rhbz#1022792

* Tue Apr 22 2014 David Vossel <dvossel@redhat.com> - 3.9.2-45
- Fixes unintentional removal of patch in previous build

* Tue Apr 22 2014 David Vossel <dvossel@redhat.com> - 3.9.2-44
- New 'httpd' option for rgmanager apache.sh agent that allows
  custom httpd binary path to be set.
- Fixes issue with pending sm-notify processes preventing
  nfs-server instances from stopping.
- Fixes issue reported by coverity. 
- Fixes syntax error in some log error messages in the LVM agent
- Optimize fs-lib based agent's monitor operation
- Allow monitoring of kvm based virtual machines using the
  VirtualDomain agent without requiring libvirtd.
- Allows named to run as user other than root.

  Resolves: rhbz#952132
  Resolves: rhbz#974239
  Resolves: rhbz#999537
  Resolves: rhbz#1022277
  Resolves: rhbz#1023099
  Resolves: rhbz#1054327
  Resolves: rhbz#1067023

* Tue Feb 04 2014 David Vossel <dvossel@redhat.com> - 3.9.2-43
  Add sec=krb5 as a valid nfsclient mount option

  Resolves: rhbz1019931

* Thu Jan 09 2014 David Vossel <dvossel@redhat.com> - 3.9.2-42
- High: fs-lib.sh: Fixes failure to unmount local fs
  when process runs with cwd inside fs mount.

  Resolves: rhbz#1051115

* Mon Nov 25 2013 David Vossel <dvossel@redhat.com> - 3.9.2-41
- Add no_unmount functionality back into netfs.sh agent
- Use crm_node instead of uname -n when referencing cluster nodes.
- Adds Delay agent back into package.
- Drops nginx rsyslog mysql-proxy tomcat and slapd agents.

  Resolves: rhbz#993329
  Resolves: rhbz#1023340
  Resolves: rhbz#1028421
  Resolves: rhbz#1022793

* Mon Nov 18 2013 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-40.3
- Fix netfs mount detection

  Resolves: rhbz#1027410

* Wed Nov 13 2013 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-40.2
- Fix netnfs unmount self_fence integration in netfs.sh
- Ship send_ua helper binary to allow IPaddr2 to manage IPv6 addresses

  Resolves: rhbz#1027410
  Resolves: rhbz#1027412

* Thu Oct 10 2013 David Vossel <dvossel@redhat.com> - 3.9.2-40
- Advertises self_fence option in netfs.sh agent

  Resolves rhbz#1014298

* Mon Oct 07 2013 David Vossel <dvossel@redhat.com> - 3.9.2-39
- Fixes issue with mysql agent not being able to set transient
  attributes on local node correctly.

  Resolves: rhbz#989284

* Thu Oct 3 2013 David Vossel <dvossel@redhat.com> - 3.9.2-38
- Removes usage of fuser -kvm from fs-lib.sh based agents.
  This resolves issue with fuser blocking netfs mounts.
- tomcat-6.sh, Do not fail on stop if config validation fails.
- tomcat-6.sh, Set tomcat usr correctly.

  Resolves: rhbz#981717 
  Resolves: rhbz#983273
  Resolves: rhbz#1014298

* Thu Sep 19 2013 David Vossel <dvossel@redhat.com> - 3.9.2-37
- Fixes lvm metadata corruption caused when activating by lv
  using tags.

  Resolves: rhbz#1009772

* Mon Sep 16 2013 David Vossel <dvossel@redhat.com> - 3.9.2-36
- Disables LVM exclusive activation via clvmd as it is not
  supported.

  Resolves: rhbz#989284

* Thu Sep 12 2013 David Vossel <dvossel@redhat.com> - 3.9.2-35
- Fixes invalid return statement in LVM retry clvmd activation
- Adds ability to disable findmnt to avoid autofs complications
  for fs-util based rgmanager agents.

  Resolves: rhbz#974941
  Resolves: rhbz#989284

* Mon Aug 12 2013 David Vossel <dvossel@redhat.com> - 3.9.2-34
- Use correct default config for heartbeat apache agent
  Resolves: rhbz#989284

* Mon Aug 12 2013 Ryan McCabe <rmccabe@redhat.com> - 3.9.2-33
- Add support for setting TNS_ADMIN
  Resolves: rhbz#917807

* Mon Aug 12 2013 Ryan McCabe <rmccabe@redhat.com> - 3.9.2-32
- Med: oracledb.sh: Fix process name grep in exit_idle
  Resolves: rhbz#853220

* Thu Aug 8 2013 David Vossel <dvossel@redhat.com> - 3.9.2-31
- Fixes lvm agent unncessarily removing PVs/LVs when some
  PVs in VG fail.

  Resolves: rhbz#884326

* Wed Aug 7 2013 David Vossel <dvossel@redhat.com> - 3.9.2-30
- Add correct nfs server defaults.
  Resolves: rhbz#989284

* Mon Aug 5 2013 David Vossel <dvossel@redhat.com> - 3.9.2-29
- Add run-time dependencies for heartbeat agents.
  Resolves: rhbz#989284

* Mon Aug 5 2013 David Vossel <dvossel@redhat.com> - 3.9.2-28
- Merge upstream heartbeat agents in for Pacemaker support.
  Resolves: rhbz#989284

* Mon Jul 22 2013 David Vossel <dvossel@redhat.com> - 3.9.2-27
- Add missing sap agents to sap subpackage
  Resolves: rhbz#922838

* Thu Jul 18 2013 David Vossel <dvossel@redhat.com> - 3.9.2-26
- Add sap connector script
- Create SAP subpackage
  Resolves: rhbz#922838

* Wed Jul  3 2013 David Vossel <dvossel@redhat.com> - 3.9.2-25
- fast filesystem mounts
- properly handle NFS v4 mounts
- fix uppercase ipv6 addresses
- named transfer source options
- fix restart postgres
- fix honor self fence option
- fix mount log level
- fix wrong selinux context for nfs directory

  Resolves: rhbz#919231
  Resolves: rhbz#851188
  Resolves: rhbz#895075
  Resolves: rhbz#711586
  Resolves: rhbz#871659
  Resolves: rhbz#908457
  Resolves: rhbz#948730
  Resolves: rhbz#959520

* Thu Jun 27 2013 David Vossel <dvossel@redhat.com> - 3.9.2-24
- Fix: lvm: detection of clusternode with lvm using tags.
  Resolves: rhbz#976443

* Thu Jun 20 2013 Ryan McCabe <rmccabe@redhat.com> - 3.9.2-23
- Med: oracledb.sh: Set RESTART_RETRIES back to 0
  Resolves: rhbz#670022

* Mon Jun 10 2013 Ryan McCabe <rmccabe@redhat.com> - 3.9.2-22
- Clean up Oracle resource agents and add support for Oracle 11g
  Resolves: rhbz#670022

* Wed Jan 23 2013 Chris Feist <cfeist@redhat.com> - 3.9.2-21
- Fixed missing '$' in lvm_by_vg.sh script
- Retry VG shutdown to cope with udev collisions
- Resolves: rhbz#729812

* Fri Dec 07 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-20
- Update the rgmanager SAPInstance agent so resource limits configured in
  /usr/sap/services are properly applied.
- Resolves: rhbz#869695

* Fri Nov 30 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-19
- Better error messages for the script resource have been added to aid
  debugging
- Resolves: rhbz#773478

* Tue Nov 27 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-18
- SAPInstance and sapdb.sh were re-synced to the latest upstream versions
- Resolves: rhbz#834293

* Fri Nov 16 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-17
- HA LVM is now able to properly shutdown when device failures cause LVs
  to go missing which allows the service to migrate to another machine
- Resolves: rhbz#860981

* Thu Nov 01 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-16
- Add support for 'volume group per service HA-LVM support for RAID logical
  volumes'
- Resolves: rhbz#824153

* Mon Oct 15 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-15
- Fixes issue with rgmanager not recognizing a mounted cifs share due to
  trailing slashes
- Resolves: rhbz#848642

* Fri Oct 12 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-14
- Fixed issue causing fs.sh to fail when a device is still mounted
- Fixed random servie failures when starting multiple HA LVM services
- Tomcat resource now uses the proper defaults
- The pacemaker SAPInstance and SAPDatabase resources were updated to their
  latest version
- Updated lvm resource agent to not produce errors when used with pacemaker
- oracledb.sh script now properly checks the status of the Oracle database
- HA-LVM now supports RAID logical volumes
- ip.sh now properly assignes the ip address to the correct interface on
  hosts with multiple interfaces on the same network
- Stopping a filesystem when a device doesn't exist no longer results in
  failure
- Log output from the 'status' action from netfs is now properly logged
- In HA LVM clusters using tags, changing the lvm.conf file is now possible
- Using rg_test with HA LVM resources no longer results in a
  "too many arguments" error 
- Resolves: rhbz#728365 rhbz#714156 rhbz#853249 rhbz#843049 rhbz#817550 rhbz#729812 rhbz#839181 rhbz#824153 rhbz#822244 rhbz#860328 rhbz#847335 rhbz#834293

* Thu Aug 16 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-13
- Add nfsrestart option to fs and clustefs agents as last resource to umount the filesystem
- Resolves: rhbz#822053

* Mon Apr 30 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-12
- Fix for LVM HA agent for service relocation after leg failure (we now
  properly remove tag).
- Resolves: rhbz#772773

* Mon Mar 05 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-11
- In LVM HA agent, remove missing PVs before attempting to remove the tag
- Rgmanager now properly detects when clvmd is not running when using HA LVM
- vm.sh now supports a 'tunnelled' option
- Resource agent script now have common directory set properly
- Fixed apache resource agent configuration with IPv6
- fs-lib.sh now will now properly work with all return codes of mount
- netfs now allows you to have the same NFS export mounted in different locations
- The timeout in rhev-check has been increased to 90 seconds
- Resolves: rhbz#772773 rhbz#729481 rhbz#712174 rhbz#784357 rhbz#742859 rhbz#728086 rhbz#799998 rhbz#727546

* Thu Mar 01 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-10
- Fix to prevent /dev/shm being filled up by ocf_log debug messages
- NFS client resource are now recovered properly when they are missing in
  /var/lib/nfs/etab
- Resolves: rhbz#797922 rhbz#749713

* Mon Feb 27 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-9
- More SAPDatabase updates to fix SAP workloads
- Allow rgmanager SAP resource agent to manage SAP Webdispatcher & TREX
- Resolves: rhbz#726500 rhbz#746996

* Tue Feb 07 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-8
- Update SAPDatabase to more closely match upstream
- Resolves: rhbz#784209

* Tue Oct 18 2011 Chris Feist <cfeist@redhat.com> - 3.9.2-7
- Require server_name in ASEHAagent to be unique
- Resolves: rhbz#711852

* Fri Aug 12 2011 Chris Feist <cfeist@redhat.com> - 3.9.2-4
- Create a link for the modified dtd for rgmanager
- Fix ocf-tester so rgmanager agents requiring bash don't cause syntax errors
- Resolves: rhbz#727643

* Thu Aug 11 2011 Chris Feist <cfeist@redhat.com> - 3.9.2-3
- Main rgmanager resource agents now use proper return codes for use with
  pacemaker.
- NFS mounts now unmount faster when the network is lost.
- Resolves: rhbz#678497 rhbz#727643

* Fri Jul 22 2011 Chris Feist <cfeist@redhat.com> - 3.9.2-2
- Postgres-8 resource agent now properly detects if postgresql was started
- fs.sh resource agent now returns the proper response code when a device
  does not yet exist.
- Resolves: rhbz#709400 rhbz#694816

* Mon Jul 11 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-1
- Rebase package on top of new upstream
  * ship xsl and rng files required to build relaxng schema
  * drop local copy of sfex_init.8
  * drop bz711852-Fix-ASEHAagent-to-allow-for-multiple-ASEHA-agents-on.patch
    included upstream
- spec file update:
  add %post to generate new relaxng schema
  Resolves: rhbz#707127

* Fri Jun 24 2011 Chris Feist <cfeist@redhat.com> - 3.9.1-2
- Fix ASEHAagent to allow for multiple ASEHA agents
- Resolves: rhbz#711852

* Tue Jun 21 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-1
- Rebase package on top of new upstream:
  resource-agents: Improve LD_LIBRARY_PATH handling by SAP*
  resource-agents: Add resource type to logging
  oracledb.sh resource script should attempt a clean shutdown first
  resource-agent does not remove nfs service temp dirs when using nfslock=1
  Listen line in generated httpd.conf incorrect
  Include rhev-check upstream
- spec file update:
  * drop all patches
  * resync with upstream spec file. See top section for local deltas
  Resolves: rhbz#707127, rhbz#705763, rhbz#667217
- Move rgmanager S/Lang from resource-agents to rgmanager:
  * Add versioned Conflicts on rgmanager to avoid file conflicts
  Resolves: rhbz#693518

* Fri Apr 15 2011 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-22
- resource-agents: Fix nfs mount contexts
  (fix_nfs_mount_contexts.patch)
  Resolves: rhbz#635828

* Wed Apr 06 2011 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-21
- Mirror dev failure in HA LVM can cause service failur
  (fix_bug_683213_mirror_dev_failure_in_ha_lvm_can_cause_service_failure.patch)
  Resolves: rhbz#683213

* Tue Mar 15 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-20
- resource-agents: fs-lib: fix do_monitor device mapping
  (fs_lib_fix_do_monitor_device_mapping.patch)
  Resolves: rhbz#669832

* Thu Feb 03 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12-19
- resource-agents: Add multi-instance Oracle database agents
  (add_multi_instance_oracle_database_agents.patch)
  Resolves: rhbz#629275
- resource-agents: Stop using '-' as 1st char of log messages
  (stop_using_as_1st_char_of_log_messages.patch)
  Resolves: rhbz#633856
- resource-agents: Use literal quotes for tr calls
  (use_literal_quotes_for_tr_calls.patch)
  Resolves: rhbz#639252
- resource-agents: Fix migrateuriopt setting
  (fix_migrateuriopt_setting.patch)
  Resolves: rhbz#660337
- resource-agents: Support convalesce w/ central_processing
  (support_convalesce_w_central_processing.patch)
  rgmanager: Add failure tolerances to resources.rng
  (add_failure_tolerances_to_resources_rng.patch)
  Resolves: rhbz#674710

* Fri Jan 28 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-18
- Disable updates to static routes by RHCS IP tooling
  (resource-agents-Add-option-disable_rdisc-to-ip.sh.patch)
  Resolves: rhbz#621538

* Tue Nov 02 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-17
- fix resource agent for named
  (resource-agents-fix-resource-agent-for-named.patch)
  Resolves: rhbz#648897

* Tue Oct 05 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-16
- resource-agents: fix utility to obtain data from ccs_tool
  (fix_utility_to_obtain_data_from_ccs_tool.patch)
  Resolves: rhbz#631943

* Wed Jul 21 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-15
- postgresql RA does not work correctly with netmask
  (psql_does_not_work_correctly_with_netmask.patch)
  Resolves: rhbz#614457

* Tue Jul 20 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-14
- resource-agents: Drop tomcat-5 from build
  (drop_tomcat_5_from_build.patch)
  Resolves: rhbz#593721

* Wed Jul 14 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-13
- Allow other values for "yes" in fs-lib when unmounting
  file systems
  (fs-lib_allow_other_values_for_yes.patch)
  Resolves: rhbz#614421

* Wed Jul 14 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-12
- postgres RA will fail to stop gracefully if there 
  is active client connected
  (sigquit_if_sigterm_was_not_fast_enough.patch)
  Resolves: rhbz#612165
- new RA for tomcat6
  (resource_agent_tomcat-6.patch)
  (tomcat-6_change_build_system.patch)
  Resolves: rhbz#593721

* Mon Jul 12 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-10
- Fix changelog for 3.0.12-9 date
- Add RHEVM status program
  (add_rhevm_status_program.patch)
  Resolves: rhbz#609497

* Fri Jul 09 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-9
- Add NFSv4 server support
  (add_nfsv4_support.patch)
  (install_nfsv4_agent.patch)
  Resolves: rhbz#595547
- Fix migration mapping behavior
  (fix_migration_mapping_behavior.patch)
  Resolves: rhbz#596918

* Wed Jun 30 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-8
- Make fs-lib resolve links before checking for block devices
  (fix_incorrect_link_resolution_in_fs_lib.patch)
  Resolves: rhbz#609579

* Wed Jun 30 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-7
- Make vm.sh honor start and stop timeouts
  (Make_vm.sh_use_stop_start_timeouts.patch)
  Resolves: rhbz#606754

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-6
- Add missing documentation for resource agents
  (add_missing_resource_docs.patch)
- Clean up recursion in scheman output and documentation
  (clean_up_recursion_and_documentation.patch)
  Resolves: rhbz#606470

* Thu Jun  3 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-5
- Fix incorrect default for VM.sh agent
  (resolve_incorrect_default_for_vm_agent.patch)
  Resolves: rhbz#599643

* Fri May 28 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-4
- Add missing man pages
  (Add Source2: ocf-tester.8 and Source3: sfex_init.8)
  Resolves: rhbz#594332

* Wed May 19 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-3
- Do not package ldirectord on RHEL
  Resolves: rhbz#577264

* Wed May 19 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-2
- Drop Requires on xfsprogs since package moved to another channel
  Resolves: rhbz#593433
- Fix HALVM: lvm agent incorrectly reports vg is in volume_list
  (halvm_lvm_agent_incorrectly_reports_vg_in_volume_list.patch)
  Resolves: rhvz#593108

* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- Rebase on top of new upstream bug fix only release:
  * drop all bug fix patches.
  * refresh patches with official SHA1 git commits from RHEL6
    upstream branch:
    - drop_support_for_drbd_and_smb.patch
  * Addresses the follwing issues:
    from 3.0.12 release:
  Resolves: rhbz#582754, rhbz#582753, rhbz#585217, rhbz#583789
  * Rebase:
  Resolves: rhbz#582353
- Stop build on ppc and ppc64.
  Resolves: rhbz#590997
- Switch to file based Requires.
  Also address several other problems related to missing runtime
  components in different agents.
  With the current Requires: set, we guarantee all basic functionalities
  out of the box for lvm/fs/clusterfs/netfs/networking.
  Resolves: rhbz#584800
- New pacemaker agents upstream release
  * Patched build process to correctly generate ldirectord man page
  + High: pgsql: properly implement pghost parameter
  + High: RA: mysql: fix syntax error
  + High: SAPInstance RA: do not rely on op target rc when monitoring clones (lf#2371)
  + High: set the HA_RSCTMP directory to /var/run/resource-agents (lf#2378)
  + High: RA: vmware: fix set_environment() invocation (LF 2342)
  + High: RA: vmware: update to version 0.2
  + Medium: IPaddr/IPaddr2: add a description of the assumption in meta-data
  + Medium: IPaddr: return the correct code if interface delete failed
  + Medium: nfsserver: rpc.statd as the notify cmd does not work with -v (thanks to Carl Lewis)
  + Medium: oracle: reduce output from sqlplus to the last line for queries (bnc#567815)
  + Medium: pgsql: implement "config" parameter
  + Medium: RA: iSCSITarget: follow changed IET access policy
  + Medium: Filesystem: prefer /proc/mounts to /etc/mtab for non-bind mounts (lf#2388)
  + Medium: IPaddr2: don't bring the interface down on stop (thanks to Lars Ellenberg)
  + Medium: IPsrcaddr: modify the interface route (lf#2367)
  + Medium: ldirectord: Allow multiple email addresses (LF 2168)
  + Medium: ldirectord: fix setting defaults for configfile and ldirectord (lf#2328)
  + Medium: meta-data: improve timeouts in most resource agents
  + Medium: nfsserver: use default values (lf#2321)
  + Medium: ocf-shellfuncs: don't log but print to stderr if connected to a terminal
  + Medium: ocf-shellfuncs: don't output to stderr if using syslog
  + Medium: oracle/oralsnr: improve exit codes if the environment isn't valid
  + Medium: RA: iSCSILogicalUnit: fix monitor for STGT
  + Medium: RA: make sure that OCF_RESKEY_CRM_meta_interval is always defined (LF 2284)
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: VirtualDomain: bail out early if config file can't be read during probe (Novell 593988)
  + Medium: RA: VirtualDomain: fix incorrect use of __OCF_ACTION
  + Medium: RA: VirtualDomain: improve error messages
  + Medium: RA: VirtualDomain: spin on define until we definitely have a domain name
  + Medium: Route: add route table parameter (lf#2335)
  + Medium: sfex: don't use pid file (lf#2363,bnc#585416)
  + Medium: sfex: exit with success on stop if sfex has never been started (bnc#585416)

* Tue Mar  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- new upstream release
  Resolves: rhbz#569959
- spec file update:
  * update spec file copyright date
  * use bz2 tarball

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-5
- Resolves: rhbz#568010
- Do not build resource-agents on s390 and s390x.

* Mon Feb 22 2010 Marek Grac <mgrac@redhat.com> - 3.0.7-4
- Checksum error occurs on HA-LVM
- status on clusterfs "gfs" returned 1 (generic error)
- Resolves rhbz#563555 rhbz#558664

* Fri Feb 19 2010 Marek Grac <mgrac@redhat.com> - 3.0.7-3
- resource-agents can't be used by Pacemaker
- Resolves: rhbz#566176

* Wed Jan 13 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Drop support for drbd and smb (PM-drop-support-for-drbd-and-smb-resource-agents.patch)
- Explicitly list python as BuildRequires

* Mon Jan 11 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New rgmanager resource agents upstream release

* Mon Jan 11 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.6-2
- Update Pacameker agents to upstream version: c76b4a6eb576
  + High: RA: VirtualDomain: fix forceful stop (LF 2283)
  + High: apache: monitor operation of depth 10 for web applications (LF 2234)
  + Medium: IPaddr2: CLUSTERIP/iptables rule not always inserted on failed monitor (LF 2281)
  + Medium: RA: Route: improve validate (LF 2232)
  + Medium: mark obsolete RAs as deprecated (LF 2244)
  + Medium: mysql: escalate stop to KILL if regular shutdown doesn't work

* Mon Dec 7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New rgmanager resource agents upstream release
- spec file update:
  * use global instead of define
  * use new Source0 url
  * use %name macro more aggressively

* Mon Dec 7 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.5-2
- Update Pacameker agents to upstream version: bc00c0b065d9
  + High: RA: introduce OCF_FUNCTIONS_DIR, allow it to be overridden (LF2239)
  + High: doc: add man pages for all RAs (LF2237)
  + High: syslog-ng: new RA
  + High: vmware: make meta-data work and several cleanups (LF 2212)
  + Medium: .ocf-shellfuncs: add ocf_is_probe function
  + Medium: Dev: make RAs executable (LF2239)
  + Medium: IPv6addr: ifdef out the ip offset hack for libnet v1.1.4 (LF 2034)
  + Medium: add mercurial repository version information to .ocf-shellfuncs
  + Medium: build: add perl-MailTools runtime dependency to ldirectord package (LF 1469)
  + Medium: iSCSITarget, iSCSILogicalUnit: support LIO
  + Medium: nfsserver: use check_binary properly in validate (LF 2211)
  + Medium: nfsserver: validate should not check if nfs_shared_infodir exists (thanks to eelco@procolix.com) (LF 2219)
  + Medium: oracle/oralsnr: export variables properly
  + Medium: pgsql: remove the previous backup_label if it exists
  + Medium: postfix: fix double stop (thanks to Dinh N. Quoc)
  + RA: LVM: Make monitor operation quiet in logs (bnc#546353)
  + RA: Xen: Remove instance_attribute "allow_migrate" (bnc#539968)
  + ldirectord: OCF agent: overhaul

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New rgmanager resource agents upstream release

* Wed Oct 28 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.4-2
- Update Pacameker agents to upstream version: e2338892f59f
  + High: send_arp - turn on unsolicited mode for compatibilty with the libnet version's exit codes
  + High: Trap sigterm for compatibility with the libnet version of send_arp
  + Medium: Bug - lf#2147: IPaddr2: behave if the interface is down
  + Medium: IPv6addr: recognize network masks properly
  + Medium: RA: VirtualDomain: avoid needlessly invoking "virsh define"

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New rgmanager resource agents upstream release

* Mon Oct 12 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.3-3
- Update Pacameker agents to upstream version: 099c0e5d80db
  + Add the ha_parameter function back into .ocf-shellfuncs.
  + Bug bnc#534803 - Provide a default for MAILCMD
  + Fix use of undefined macro @HA_NOARCHDATAHBDIR@
  + High (LF 2138): IPsrcaddr: replace 0/0 with proper ip prefix (thanks to Michael Ricordeau and Michael Schwartzkopff)
  + Import shellfuncs from heartbeat as badly written RAs use it
  + Medium (LF 2173): nfsserver: exit properly in nfsserver_validate
  + Medium: RA: Filesystem: implement monitor operation
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable (addendum)
  + Medium: RA: iSCSILogicalUnit: use a 16-byte default SCSI ID
  + Medium: RA: iSCSITarget: be more persistent deleting targets on stop
  + Medium: RA: portblock: add per-IP filtering capability
  + Medium: mysql-proxy: log_level and keepalive parameters
  + Medium: oracle: drop spurious output from sqlplus
  + RA: Filesystem: allow configuring smbfs mounts as clones

* Wed Sep 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New rgmanager resource agents upstream release

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New rgmanager resource agents upstream release

* Tue Aug 18 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.0-16
- Create an ldirectord package
- Update Pacameker agents to upstream version: 2198dc90bec4
  + Build: Import ldirectord.
  + Ensure HA_VARRUNDIR has a value to substitute
  + High: Add findif tool (mandatory for IPaddr/IPaddr2)
  + High: IPv6addr: new nic and cidr_netmask parameters
  + High: postfix: new resource agent
  + Include license information
  + Low (LF 2159): Squid: make the regexp match more precisely output of netstat
  + Low: configure: Fix package name.
  + Low: ldirectord: add dependency on $remote_fs.
  + Low: ldirectord: add mandatory required header to init script.
  + Medium (LF 2165): IPaddr2: remove all colons from the mac address before passing it to send_arp
  + Medium: VirtualDomain: destroy domain shortly before timeout expiry
  + Medium: shellfuncs: Make the mktemp wrappers work.
  + Remove references to Echo function
  + Remove references to heartbeat shellfuncs.
  + Remove useless path lookups
  + findif: actually include the right header. Simplify configure.
  + ldirectord: Remove superfluous configure artifact.
  + ocf-tester: Fix package reference and path to DTD.

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.0.0-15
- Use bzipped upstream hg tarball.

* Wed Jul 29 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14
- Merge Pacemaker cluster resource agents:
  * Add Source1.
  * Drop noarch. We have real binaries now.
  * Update BuildRequires.
  * Update all relevant prep/build/install/files/description sections.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.rc4
- New upstream release.

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.rc3
- New upstream release.

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-9.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.rc1
- New upstream release.
- Update BuildRoot usage to preferred versions/names

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.beta1
- New upstream release.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha7
- New upstream release.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha6
- New upstream release.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha5
- Drop Conflicts with rgmanager.

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha5
- New upstream release.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha4
- Add comments on how to build this package.

* Thu Feb  5 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha4
- New upstream release.
- Fix datadir/cluster directory ownership.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha3
  - Initial packaging
