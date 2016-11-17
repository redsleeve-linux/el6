%global gname haclient
%global uname hacluster
%global pcmk_docdir %{_docdir}/%{name}

%global specversion 8
# 1.1.14
%global commit f0b585a6ad5ad0db5f6a0faabcf2872fff152d55 
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global github_owner ClusterLabs

# Turn off the auto compilation of python files not in the site-packages directory
# Needed so that the -devel package is multilib compliant
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global rawhide  %(test ! -e /etc/yum.repos.d/fedora-rawhide.repo; echo $?)
%global cs_version %(pkg-config corosync --modversion  | awk -F . '{print $1}')
%global py_site %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

# Conditionals
# Invoke "rpmbuild --without <feature>" or "rpmbuild --with <feature>"
# to disable or enable specific features

# Legacy stonithd fencing agents
%bcond_with stonithd

# Build with/without support for profiling tools
%bcond_with profiling

# Include Build with/without support for performing coverage analysis
%bcond_with coverage

# We generate docs using Publican, Asciidoc and Inkscape, but they're not available everywhere
%bcond_without doc

# Use a different versioning scheme
%bcond_with pre_release

# Ship an Upstart job file
%bcond_with upstart_job

# Turn off cman support on platforms that normally ship with it
%bcond_without cman

%if %{with profiling}
# This disables -debuginfo package creation and also the stripping binaries/libraries
# Useful if you want sane profiling data
%global debug_package %{nil}
%endif

%if %{with pre_release}
%global pcmk_release 0.%{specversion}.%{upstream_version}.git
%else
%global pcmk_release %{specversion}
%endif

Name:          pacemaker
Summary:       Scalable High-Availability cluster resource manager
Version:       1.1.14
Release:       %{pcmk_release}%{?dist}.2
License:       GPLv2+ and LGPLv2+
Url:           http://www.clusterlabs.org
Group:         System Environment/Daemons

Source0:        https://github.com/%{github_owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

# patches that aren't upstream commits
Patch1:        pcmk-plugin-warning.patch
Patch2:        pacemaker-no-doxygen.patch
Patch3:        README_RGManager_porting.patch
Patch4:        pacemaker-sbd-start.patch
Patch5:        CVE-2016-7035.patch

# graceful stops of pacemaker_remote
Patch100:      0100-Refactor-lrmd-handle-shutdown-a-little-more-cleanly.patch
Patch101:      0101-Refactor-lrmd-make-proxied-IPC-providers-clients-opa.patch
Patch102:      0102-Refactor-crmd-lrmd-liblrmd-use-defined-constants-for.patch
Patch103:      0103-Test-cts-simulate-pacemaker_remote-failure-with-kill.patch
Patch104:      0104-Feature-lrmd-liblrmd-add-lrmd-IPC-operations-for-req.patch
Patch105:      0105-Feature-crmd-support-graceful-pacemaker_remote-stops.patch
Patch106:      0106-Feature-pacemaker_remote-support-graceful-stops.patch
Patch107:      0107-Feature-PE-Honor-the-shutdown-transient-attributes-f.patch
Patch108:      0108-Feature-crmd-Set-the-shutdown-transient-attribute-in.patch
Patch109:      0109-Fix-attrd-Hook-up-the-client-name-so-we-can-track-re.patch
Patch110:      0110-Fix-attrd-Correctly-implement-mass-removal-of-a-node.patch
Patch111:      0111-Log-crmd-Graceful-proxy-shutdown-is-now-tested.patch
Patch112:      0112-Fix-crmd-set-remote-flag.patch
Patch113:      0113-Fix-attrd-correct-peer-cache.patch

# other upstream commits
Patch114:      0114-Fix-PACKAGE_URL.patch
Patch115:      0115-unexpected-remote-client.patch
Patch116:      0116-notify-clients-after-handshake.patch
Patch117:      0117-scalability-regression.patch
Patch118:      0118-remote-attributes.patch
Patch119:      0119-crm_report-sanitize-logfiles.patch
Patch120:      0120-fencing-unseen-nodes.patch
Patch121:      0121-skip-cman-option.patch

BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv:   on
Requires:      python >= 2.4
Requires:      resource-agents
Requires:      %{name}-libs = %{version}-%{release}
Requires:      %{name}-cluster-libs = %{version}-%{release}
Requires:      %{name}-cli = %{version}-%{release}

%if %{defined systemd_requires}
%systemd_requires
%endif

%if 0%{?rhel} > 0
ExclusiveArch: i686 x86_64
%endif

# Required for core functionality
BuildRequires: automake autoconf libtool pkgconfig python libtool-ltdl-devel
BuildRequires: pkgconfig(glib-2.0) libxml2-devel libxslt-devel libuuid-devel
BuildRequires: pkgconfig python-devel gcc-c++ bzip2-devel pam-devel

# Required for agent_config.h which specifies the correct scratch directory
BuildRequires: resource-agents

# We need reasonably recent versions of libqb
BuildRequires: libqb-devel > 0.17.0
Requires:      libqb > 0.17.0

# Enables optional functionality
BuildRequires: ncurses-devel openssl-devel libselinux-devel docbook-style-xsl
BuildRequires: bison byacc flex help2man gnutls-devel

%if %{defined _unitdir}
BuildRequires: systemd-devel
%endif

%if %{with cman}

%if 0%{?fedora} > 0
%if 0%{?fedora} < 17
BuildRequires: clusterlib-devel
%endif
%endif

%if 0%{?rhel} > 0
%if 0%{?rhel} < 7
BuildRequires: clusterlib-devel
%endif
%endif

%endif

Requires:      corosync
BuildRequires: corosynclib-devel

%if %{with stonithd}
BuildRequires: cluster-glue-libs-devel
%endif

%if !%{rawhide}
# More often than not, inkscape is busted on rawhide, don't even bother

%if %{with doc}
%ifarch %{ix86} x86_64
# BuildRequires: publican
BuildRequires: inkscape asciidoc
%endif
%endif

%endif

%description
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

It supports more than 16 node clusters with significant capabilities
for managing resources and dependencies.

It will run scripts at initialization, when machines go up or down,
when related resources fail and can be configured to periodically check
resource health.

Available rpmbuild rebuild options:
  --with(out) : cman stonithd doc coverage profiling pre_release upstart_job

%package cli
License:      GPLv2+ and LGPLv2+
Summary:      Command line tools for controlling Pacemaker clusters
Group:        System Environment/Daemons
Requires:     %{name}-libs = %{version}-%{release}
Requires:     perl-TimeDate

%description cli
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

The %{name}-cli package contains command line tools that can be used
to query and control the cluster from machines that may, or may not,
be part of the cluster.

%package -n %{name}-libs
License:      GPLv2+ and LGPLv2+
Summary:      Core Pacemaker libraries
Group:        System Environment/Daemons
Requires(pre): shadow-utils
Requires:      glib2 >= 2.28 

%description -n %{name}-libs
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

The %{name}-libs package contains shared libraries needed for cluster
nodes and those just running the CLI tools.

%package -n %{name}-cluster-libs
License:      GPLv2+ and LGPLv2+
Summary:      Cluster Libraries used by Pacemaker
Group:        System Environment/Daemons
Requires:     %{name}-libs = %{version}-%{release}

%description -n %{name}-cluster-libs
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

The %{name}-cluster-libs package contains cluster-aware shared
libraries needed for nodes that will form part of the cluster nodes.

%package remote
License:      GPLv2+ and LGPLv2+
Summary:      Pacemaker remote daemon for non-cluster nodes
Group:        System Environment/Daemons
Requires:     %{name}-libs = %{version}-%{release}
Requires:      %{name}-cli = %{version}-%{release}
Requires:      resource-agents
%if %{defined systemd_requires}
%systemd_requires
%endif

%description remote
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

The %{name}-remote package contains the Pacemaker Remote daemon
which is capable of extending pacemaker functionality to remote
nodes not running the full corosync/cluster stack.

%package -n %{name}-libs-devel
License:      GPLv2+ and LGPLv2+
Summary:      Pacemaker development package
Group:        Development/Libraries
Requires:     %{name}-cts = %{version}-%{release}
Requires:     %{name}-libs = %{version}-%{release}
Requires:     %{name}-cluster-libs = %{version}-%{release}
Requires:     libtool-ltdl-devel libqb-devel libuuid-devel
Requires:     libxml2-devel libxslt-devel bzip2-devel glib2-devel
Requires:     corosynclib-devel

%description -n %{name}-libs-devel
Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.

The %{name}-libs-devel package contains headers and shared libraries
for developing tools for Pacemaker.

%package      cts
License:      GPLv2+ and LGPLv2+
Summary:      Test framework for cluster-related technologies like Pacemaker
Group:        System Environment/Daemons
Requires:     python
Requires:     %{name}-libs = %{version}-%{release}
%if %{defined systemd_requires}
Requires:      systemd-python
%endif

%description  cts
Test framework for cluster-related technologies like Pacemaker

%package      doc
License:      GPLv2+ and LGPLv2+
Summary:      Documentation for Pacemaker
Group:        Documentation

%description  doc
Documentation for Pacemaker.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Corosync, CMAN and/or Linux-HA.


%prep
# autosetup is particularly useful when backporting patches
#autosetup -n %{name}-%{commit} -p1 -S git

%setup -q -n %{name}-%{commit}
cp extra/rgmanager/README README_RGManager_porting

%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1

# Force the local time
#
# 'git' sets the file date to the date of the last commit.
# This can result in files having been created in the future
# when building on machines in timezones 'behind' the one the
# commit occurred in - which seriously confuses 'make'
find . -exec touch \{\} \;

%build
./autogen.sh

# RHEL <= 5 does not support --docdir
docdir=%{pcmk_docdir} %{configure}                 \
        %{?with_profiling:   --with-profiling}     \
        %{?with_coverage:    --with-coverage}      \
        %{!?with_cman:       --without-cman}       \
        --disable-systemd --disable-upstart        \
        --without-heartbeat                        \
        --with-initdir=%{_initrddir}               \
        --localstatedir=%{_var}                    \
        --with-version=%{version}-%{release}

%if 0%{?suse_version} >= 1200
# Fedora handles rpath removal automagically
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%endif

make %{_smp_mflags} V=1 docdir=%{pcmk_docdir} all

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} docdir=%{pcmk_docdir} V=1 install

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
mkdir -p ${RPM_BUILD_ROOT}%{_var}/lib/pacemaker/cores
install -m 644 mcp/pacemaker.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/pacemaker
install -m 644 tools/crm_mon.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/crm_mon

%if %{with upstart_job}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/init
install -m 644 mcp/pacemaker.upstart ${RPM_BUILD_ROOT}%{_sysconfdir}/init/pacemaker.conf
install -m 644 mcp/pacemaker.combined.upstart ${RPM_BUILD_ROOT}%{_sysconfdir}/init/pacemaker.combined.conf
install -m 644 tools/crm_mon.upstart ${RPM_BUILD_ROOT}%{_sysconfdir}/init/crm_mon.conf
%endif

# Scripts that should be executable
chmod a+x %{buildroot}/%{_datadir}/pacemaker/tests/cts/CTSlab.py

# These are not actually scripts
find %{buildroot} -name '*.xml' -type f -print0 | xargs -0 chmod a-x
find %{buildroot} -name '*.xsl' -type f -print0 | xargs -0 chmod a-x
find %{buildroot} -name '*.rng' -type f -print0 | xargs -0 chmod a-x
find %{buildroot} -name '*.dtd' -type f -print0 | xargs -0 chmod a-x

# Don't package static libs
find %{buildroot} -name '*.a' -type f -print0 | xargs -0 rm -f
find %{buildroot} -name '*.la' -type f -print0 | xargs -0 rm -f

# Do not package these either
rm -f %{buildroot}/%{_libdir}/service_crm.so
find %{buildroot} -name 'o2cb*' -type f -print0 | xargs -0 rm -f

# Don't ship init scripts for systemd based platforms
%if %{defined _unitdir}
rm -f %{buildroot}/%{_initrddir}/pacemaker
rm -f %{buildroot}/%{_initrddir}/pacemaker_remote
%endif

%if %{with coverage}
GCOV_BASE=%{buildroot}/%{_var}/lib/pacemaker/gcov
mkdir -p $GCOV_BASE
find . -name '*.gcno' -type f | while read F ; do
        D=`dirname $F`
        mkdir -p ${GCOV_BASE}/$D
        cp $F ${GCOV_BASE}/$D
done
%endif

%clean
rm -rf %{buildroot}

%if %{defined _unitdir}

%post
%systemd_post pacemaker.service

%preun
%systemd_preun pacemaker.service

%postun
%systemd_postun_with_restart pacemaker.service 

%post remote
%systemd_post pacemaker_remote.service

%preun remote
%systemd_preun pacemaker_remote.service

%postun remote
%systemd_postun_with_restart pacemaker_remote.service 

%else

%post
/sbin/chkconfig --add pacemaker || :

%preun
/sbin/service pacemaker stop  &>/dev/null || :
if [ $1 -eq 0 ]; then
    # Package removal, not upgrade
    /sbin/chkconfig --del pacemaker || :
fi

%post remote
/sbin/chkconfig --add pacemaker_remote || :

%preun remote
/sbin/service pacemaker_remote stop &>/dev/null || :
if [ $1 -eq 0 ]; then
    # Package removal, not upgrade
    /sbin/chkconfig --del pacemaker_remote || :
fi

%endif

%pre -n %{name}-libs

getent group %{gname} >/dev/null || groupadd -r %{gname} -g 189
getent passwd %{uname} >/dev/null || useradd -r -g %{gname} -u 189 -s /sbin/nologin -c "cluster user" %{uname}
exit 0

%post -n %{name}-libs -p /sbin/ldconfig

%postun -n %{name}-libs -p /sbin/ldconfig

%post -n %{name}-cluster-libs -p /sbin/ldconfig

%postun -n %{name}-cluster-libs -p /sbin/ldconfig

%files
###########################################################
%defattr(-,root,root)

%exclude %{_datadir}/pacemaker/tests

%config(noreplace) %{_sysconfdir}/sysconfig/pacemaker
%config(noreplace) %{_sysconfdir}/logrotate.d/pacemaker
%{_sbindir}/pacemakerd

%if %{defined _unitdir}
%{_unitdir}/pacemaker.service
%else
%{_initrddir}/pacemaker
%endif

%exclude %{_datadir}/pacemaker/report.common
%exclude %{_datadir}/pacemaker/report.collector
%{_datadir}/pacemaker
%{_datadir}/snmp/mibs/PCMK-MIB.txt

%exclude %{_libexecdir}/pacemaker/lrmd_test
%exclude %{_sbindir}/pacemaker_remoted
%{_libexecdir}/pacemaker/*

%{_sbindir}/crm_attribute
%{_sbindir}/crm_master
%{_sbindir}/crm_node
%{_sbindir}/attrd_updater
%{_sbindir}/fence_legacy
%{_sbindir}/fence_pcmk
%{_sbindir}/stonith_admin

%if %{with cman}
%if 0
%{_bindir}/ccs2cib
%{_bindir}/ccs_flatten
%{_bindir}/disable_rgmanager
%else
%doc README_RGManager_porting
%endif
%endif

%doc %{_mandir}/man7/*
%doc %{_mandir}/man8/attrd_updater.*
%doc %{_mandir}/man8/crm_attribute.*
%doc %{_mandir}/man8/crm_node.*
%doc %{_mandir}/man8/crm_master.*
%doc %{_mandir}/man8/fence_pcmk.*
%doc %{_mandir}/man8/fence_legacy.*
%doc %{_mandir}/man8/pacemakerd.*
%doc %{_mandir}/man8/stonith_admin.*

%doc COPYING
%doc AUTHORS
%doc ChangeLog

%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cib
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/cores
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/pengine
%dir %attr (750, %{uname}, %{gname}) %{_var}/lib/pacemaker/blackbox
%ghost %dir %attr (750, %{uname}, %{gname}) %{_var}/run/crm
%dir /usr/lib/ocf
%dir /usr/lib/ocf/resource.d
/usr/lib/ocf/resource.d/pacemaker
/usr/lib/ocf/resource.d/.isolation

%if "%{?cs_version}" != "UNKNOWN"
%if 0%{?cs_version} < 2
%{_libexecdir}/lcrso/pacemaker.lcrso
%endif
%endif

%if %{with upstart_job}
%config(noreplace) %{_sysconfdir}/init/pacemaker.conf
%config(noreplace) %{_sysconfdir}/init/pacemaker.combined.conf
%endif

%files cli
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/crm_mon

%if %{with upstart_job}
%config(noreplace) %{_sysconfdir}/init/crm_mon.conf
%endif

%{_sbindir}/cibadmin
%{_sbindir}/crm_diff
%{_sbindir}/crm_error
%{_sbindir}/crm_failcount
%{_sbindir}/crm_mon
%{_sbindir}/crm_resource
%{_sbindir}/crm_standby
%{_sbindir}/crm_verify
%{_sbindir}/crmadmin
%{_sbindir}/iso8601
%{_sbindir}/crm_shadow
%{_sbindir}/crm_simulate
%{_sbindir}/crm_report
%{_sbindir}/crm_ticket
%{_datadir}/pacemaker/report.common
%{_datadir}/pacemaker/report.collector
%doc %{_mandir}/man8/*
%exclude %{_mandir}/man8/attrd_updater.*
%exclude %{_mandir}/man8/crm_attribute.*
%exclude %{_mandir}/man8/crm_node.*
%exclude %{_mandir}/man8/crm_master.*
%exclude %{_mandir}/man8/fence_pcmk.*
%exclude %{_mandir}/man8/fence_legacy.*
%exclude %{_mandir}/man8/pacemakerd.*
%exclude %{_mandir}/man8/pacemaker_remoted.*
%exclude %{_mandir}/man8/stonith_admin.*

%doc COPYING
%doc AUTHORS
%doc ChangeLog

%files -n %{name}-libs
%defattr(-,root,root)

%{_libdir}/libcib.so.*
%{_libdir}/liblrmd.so.*
%{_libdir}/libcrmservice.so.*
%{_libdir}/libcrmcommon.so.*
%{_libdir}/libpe_status.so.*
%{_libdir}/libpe_rules.so.*
%{_libdir}/libpengine.so.*
%{_libdir}/libstonithd.so.*
%{_libdir}/libtransitioner.so.*
%doc COPYING.LIB
%doc AUTHORS

%files -n %{name}-cluster-libs
%defattr(-,root,root)
%{_libdir}/libcrmcluster.so.*
%doc COPYING.LIB
%doc AUTHORS

%files remote
%defattr(-,root,root)

%config(noreplace) %{_sysconfdir}/sysconfig/pacemaker
%if %{defined _unitdir}
%{_unitdir}/pacemaker_remote.service
%else
%{_initrddir}/pacemaker_remote
%endif

%{_sbindir}/pacemaker_remoted
%{_mandir}/man8/pacemaker_remoted.*
%doc COPYING.LIB
%doc AUTHORS

%files doc
%defattr(-,root,root)
%doc %{pcmk_docdir}

%files cts
%defattr(-,root,root)
%{py_site}/cts
%{_datadir}/pacemaker/tests/cts
%{_libexecdir}/pacemaker/lrmd_test
%doc COPYING.LIB
%doc AUTHORS

%files -n %{name}-libs-devel
%defattr(-,root,root)
%exclude %{_datadir}/pacemaker/tests/cts
%{_datadir}/pacemaker/tests
%{_includedir}/pacemaker
%{_libdir}/*.so
%if %{with coverage}
%{_var}/lib/pacemaker/gcov
%endif
%{_libdir}/pkgconfig/*.pc
%doc COPYING.LIB
%doc AUTHORS

%changelog
* Mon Oct 24 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-8.2
- Fix CVE-2016-7035

  Resolves: rhbz#1374774

* Fri Jul 15 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-8.1
 - add --skip-cman option when stopping pacemaker

  Resolves: rhbz#1355738

* Thu Mar 24 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-8
 - fenced unseen nodes should not be considered unclean

  Resolves: rhbz#1321110

* Mon Mar 21 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-7
 - sanitize log files collected by crm_report

  Resolves: rhbz#1219103

* Fri Mar 18 2016 Klaus Wenninger <kwenning@redhat.com> - 1.1.14-6
 - start sbd if configured and enabled

  Resolves: rhbz#1313246

* Fri Mar 18 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-5
 - support remote node attributes

  Resolves: rhbz#1297564

* Wed Mar 16 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-4
 - preserve CIB scalability

  Resolves: rhbz#1195500

* Wed Feb 24 2016 Ken Gaillot <kgaillot@redhat.com> - 1.1.14-3
 - prevent crmd crash after unexpected Pacemaker Remote connection takeover
 - ensure package URL is displayed correctly

  Resolves: rhbz#1252206

* Wed Jan 27 2016 Klaus Wenninger <kwenning@redhat.com> - 1.1.14-2.0
 - fix issues with graceful remote stops feature

  Resolves: rhbz#1297564

* Mon Jan 18 2016 Klaus Wenninger <kwenning@redhat.com> - 1.1.14-1.1
 - removed unneeded dbus requirement

  Resolves: rhbz#1252206

* Fri Jan 15 2016 Klaus Wenninger <kwenning@redhat.com> - 1.1.14-1.0
 - Update to upstream release 1.1.14
 - added README_RGManager_porting to document replacement of
     ccs2cib, ccs_flatten & disable_rgmanager
 - added patchset (0100-0111) from master to implement graceful
     stop of pacemaker_remote
 - require minimum-version 0.17.0 of libqb

  Resolves: rhbz#1193499
  Resolves: rhbz#1195500
  Resolves: rhbz#1200853
  Resolves: rhbz#1215809
  Resolves: rhbz#1219103
  Resolves: rhbz#1235316
  Resolves: rhbz#1246490
  Resolves: rhbz#1246563
  Resolves: rhbz#1252206
  Resolves: rhbz#1257333
  Resolves: rhbz#1275223
  Resolves: rhbz#1287535
  Resolves: rhbz#1297564

* Fri Oct 09 2015 Andrew Beekhof <abeekhof@redhat.com> - 1.1.12-8.2
  Resolves: rhbz#1249474

* Wed Jul 22 2015 Ken Gaillot <kgaillot@redhat.com> - 1.1.12-9
 - Fix use-after-free issues related to peer status callbacks

  Resolves: rhbz#1235316

* Wed Jul 22 2015 Ken Gaillot <kgaillot@redhat.com> - 1.1.12-8.1
 - Fix use-after-free issues related to peer status callbacks

  Resolves: rhbz#1249474

* Fri May 08 2015 David Vossel <dvossel@redhat.com> - 1.1.12-8
 - Reduce log severity for style upgrade notice.
 - Properly export pacemaker related sysconfig variables
 - Remove warning during yum update of pacemaker packages.

  Resolves: rhbz#1163982
  Resolves: rhbz#1177821
  Resolves: rhbz#1210291

* Fri Apr 10 2015 Andrew Beekhof <abeekhof@redhat.com> - 1.1.12-7
- Ensure relevant components clear cache entries are cleared when peers leave the cluster

  Resolves: rhbz#1193499

* Wed Apr 1 2015 David Vossel <dvossel@redhat.com> - 1.1.12-6
- Fixes invalid free in attrd
- Fixes crm_mon -E option for external script.
- Fixes acl read-only access role assignment.

  Resolves: rhbz#1205292
  Resolves: rhbz#1208896
  Resolves: rhbz#1207621

* Mon Mar 30 2015 David Vossel <dvossel@redhat.com> - 1.1.12-5
- Properly clear shutdown transient attribute after node leaves
  membership.

  Resolves: rhbz#1198638

* Thu Jul 3 2014 Andrew Beekhof <beekhof@redhat.com> - 1.1.12-4

- Ensure glib2 matches at least the version we built against
  Resolves: rhbz#1113189

* Thu Jun 19 2014 Andrew Beekhof <beekhof@redhat.com> - 1.1.12-3

- Fix: crmd: avoid double free caused by nested hash table removal
- Fix: ignore SIGPIPE with gnutls is in use
- Fix: cib: cl#5222 - Prevent assert in xml_calculate_changes() on performing cib operations
    Resolves: rhbz#1071995

* Mon Jun 16 2014 Andrew Beekhof <beekhof@redhat.com> - 1.1.12-2

- Bug rhbz#1054307 - cname pattern match should be more restrictive in init script
    Resolves: rhbz#1054307

* Mon Jun 16 2014 Andrew Beekhof <abeekhof@redhat.com> - 1.1.12-1
- Update to upstream release 1.1.12-rc3
- The CIB has O(2) better performance and updates are applied with greater reliablity
- Transient attributes are now recorded in a truely atomic manner
- Supports fencing agents that need the host to be unfenced at startup
- CIB ACLs have been reimplemented and are now enabled 
- Various bugs squashed

- Resolves: rhbz#1020210 rhbz#1036631 rhbz#1069279
- Resolves: rhbz#1069795 rhbz#1071995

* Tue Apr 15 2014 David Vossel <dvossel@redhat.com> - 1.1.10-16

- Fix: pengine: fixes invalid transition caused by clones with more than 10 instances
    Resolves: rhbz#1078954

* Mon Jan 20 2014 David Vossel <dvossel@redhat.com> - 1.1.10-15

- Fix: Removes unnecessary newlines in crm_resource -O output
    Resolves: rhbz#1038155
- Fix: lrmd: Correctly cancel monitor actions for lsb/systemd/service resources on cleaning up (cherry picked from commit 1c14b9d69470ff56fd814091867394cd0a1cf61d)
    Resolves: rhbz#1046131
- Fix: services: Fixes segfault associated with cancelling in-flight recurring operations.
    Resolves: rhbz#1046131

* Thu Oct 03 2013 Andrew Beekhof <beekhof@redhat.com> - 1.1.10-14

- Log: crmd: Supply arguments in the correct order
    Resolves: rhbz#996850
- Fix: Invalid formatting of log message causes crash
    Resolves: rhbz#996850

* Wed Oct 02 2013 Andrew Beekhof <beekhof@redhat.com> - 1.1.10-13

- Fix: cman: Start clvmd and friends from the init script if enabled

* Tue Oct 01 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-12

- Fix: Consistently use 'Slave' as the role for unpromoted master/slave resources
    Resolves: rhbz#1011618
- Fix: pengine: Location constraints with role=Started should prevent masters from running at all
    Resolves: rhbz#902407
- Fix: crm_resource: Observe --master modifier for --move
    Resolves: rhbz#902407

* Sun Sep 22 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-11
  + Fix: cman: Do not start pacemaker if cman startup fails
  + Fix: Fencing: Observe pcmk_host_list during automatic unfencing
    Resolves: rhbz#996850

* Wed Sep 18 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-10
- Remove unsupported resource agent
    Resolves: rhbz#1005678
- Provide a meaningful error if --master is used for primitives and groups

* Fri Aug 23 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-9
  + Fix: xml: Location constraints are allowed to specify a role
  + Bug rhbz#902407 - crm_resource: Handle --ban for master/slave resources as advertised
    Resolves: rhbz#902407

* Mon Aug 19 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-8
  + Fix: mcp: Remove LSB hints that instruct chkconfig to start pacemaker at boot time
    Resolves: rhbz#997346

* Wed Aug 14 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-7
  + Fencing: Support agents that need the host to be unfenced at startup
    Resolves: rhbz#996850
  + Fix: crm_report: Collect corosync quorum data
    Resolves: rhbz#989292

* Thu Aug 08 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-6
- Regenerate patches to have meaningful names

* Thu Aug 08 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-5
  + Fix: systemd: Prevent glib assertion - only call g_error_free with non-NULL arguments
  + Fix: systemd: Prevent additional use-of-NULL assertions in g_error_free
  + Fix: logging: glib CRIT messages should not produce core files in the background
  + Fix: crmd: Correcty update the history cache when recurring ops change their return code
  + Log: crm_mon: Unmangle the output for failed operations
  + Log: cib: Correctly log short-form xml diffs
  + Log: pengine: Better indicate when a resource has failed

* Fri Aug 02 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-4
  + Fix: crmd: Prevent crash by passing log arguments in the correct order
  + Fix: pengine: Do not re-allocate clone instances that are blocked in the Stopped state
  + Fix: pengine: Do not allow colocation with blocked clone instances

* Thu Aug 01 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.10-3
  + Fix: pengine: Do not restart resources that depend on unmanaged resources
  + Fix: crmd: Prevent recurring monitors being cancelled due to notify operations

* Fri Jul 26 2013 Andrew Beekhof <andrew@beekhof.net> 1.1.10-2
- Drop rgmanager 'provides' directive

* Fri Jul 26 2013 Andrew Beekhof <andrew@beekhof.net> 1.1.10-1
- Update source tarball to revision: Pacemaker-1.1.10
- See included ChangeLog file or https://raw.github.com/ClusterLabs/pacemaker/master/ChangeLog for full details

- Resolves: rhbz#891766
- Resolves: rhbz#902407
- Resolves: rhbz#908450
- Resolves: rhbz#913093
- Resolves: rhbz#951340
- Resolves: rhbz#951371
- Related: rhbz#987355

* Wed Jan 09 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.8-7
- Resolves: rhbz#880249
- Update to upstream ca7bf5e

  + Fencing: Only try peers for non-topology based operations once
  + tools: Have crm_resource generate a valid transition key when sending resource commands to the crmd

* Sun Jan 06 2013 Andrew Beekhof <abeekhof@redhat.com> - 1.1.8-6
- Resolves: rhbz#877364
- Update to upstream d20d06f

  + cib: Avoid use-after-free by correctly support cib_no_children for non-xpath queries
  + cib: Remove text nodes from cib replace operations
  + Cluster: Preserve corosync membership state when matching node name/id entries
  + cman: Do not wait for unmanaged resources during shutdown
  + cman: Ensure reliable shutdown
  + cman: Ignore qdisk 'nodes'
  + Core: Prevent use-of_NULL in IPC code
  + corosync: Ensure peer state is preserved when matching names to nodeids
  + crmd: Avoid filling the ipc queue with data we don't need
  + crmd: Prevent election storms caused by getrusage() values being too close
  + Fencing: Correctly terminate when all device options have been exhausted
  + Fencing: Record delegated self-fencing operations in case they fail
  + legacy: Re-enable logging from the pacemaker plugin
  + pengine: Bug rhbz#880249 - Ensure orphan masters are demoted before being stopped
  + pengine: Bug rhbz#880249 - Teach the PE how to recover masters into primitives
  + pengine: Ensure previous migrations are completed before attempting another one
  + tools: crm_report - Fix node list detection

* Thu Dec 13 2012 Andrew Beekhof <abeekhof@redhat.com> - 1.1.8-5
- Resolves: rhbz#877364
- Update to upstream e69dfc1

  + attrd: Correctly handle deletion of non-existant attributes
  + cib: Do not pass local variables to mainloop_add_fd() when creating remote connections
  + Cluster: Do not strip the domain from node names calculated from uname(2)
  + Core: Supply the correct number of arguments for the format string
  + corosync: Avoid errors when closing failed connections
  + fencing: Automatically append 'nodeid' to fencing agent args if it is detected agent supports 'nodeid' parameter
  + mcp: chmod the correct directory instead of /var/run
  + pengine: Prevent double-free for cloned primitive from template

* Wed Oct 31 2012 Andrew Beekhof <abeekhof@redhat.com> - 1.1.8-4
- Resolves: rhbz#816875
- Update to upstream db9410b

  + Cluster: Detect node name collisions in corosync
  + Cluster: Strip domains from node names by default
  + Core: Prevent ordering changes when applying xml diffs
  + Fencing: On failure, only try a topology device once from the remote level.
  + Fencing: Retry stonith device for duration of action's timeout period.
  + Fencing: Support 'on_target' option in fencing device metadata for forcing unfence on target node
  + mcp: Re-attach to existing pacemaker components when mcp fails
  + pengine: Bug cl#5101 - Ensure stop order is preserved for partially active groups
  + pengine: Bug cl#5111 - When clone/master child rsc has on-fail=stop, insure all children stop on failure.
  + pengine: Correctly unpack active anonymous clones
  + pengine: Support a 'requires' resource meta-attribute for controlling whether it needs quorum, fencing or nothing
  + pengine: Support resources that require unfencing before start

* Tue Oct 2 2012 Andrew Beekhof <andrew@beekhof.net> 1.1.8-3
- Fix multilib support by turning off the auto compilation of python files
- Resolves: rhbz#816875

* Mon Oct 1 2012 Andrew Beekhof <andrew@beekhof.net> 1.1.8-2
- Fix internal package dependancies
- Resolves: rhbz#816875

- Update to upstream 0b45588
  + Correctly disable syslog output when requested
  + Warn about node names containing a capital letter
  + Do not start fencing until entire device topology is found or query results timeout.
  + Allow nodes to use a name other than uname()

* Fri Sep 21 2012 Andrew Beekhof <andrew@beekhof.net> 1.1.8-1
- Rebuild for upstream 1.1.8 release
- Resolves: rhbz#816875

- See included ChangeLog file or https://raw.github.com/ClusterLabs/pacemaker/master/ChangeLog for full details

  + New IPC implementation from libqb
  + New logging implementation from libqb
  + Quieter - info, debug and trace logs are no longer sent to syslog
  + Dropped dependancy on cluster-glue
  + Config and core directories no longer located in heartbeat directories
  + Support for managing systemd services
  + Rewritten local resource management daemon
  + Version bumps for every shared library due to API cleanups
  + Removes crm shell, install/use pcs shell and GUI instead

* Tue Apr 10 2012 David Vossel <dvossel@redhat.com> - 1.1.7-6
- Clear failcount history from crmd's lrm cache.
  Resolves: rhbz#789397

* Fri Mar 30 2012 David Vossel <dvossel@redhat.com> - 1.1.7-5
- Use default value for HB_DAEMON_DIR define when clusterglue does not provide one.
  Resolves: rhbz#808557

* Tue Mar 27 2012 David Vossel <dvossel@redhat.com> - 1.1.7-3
- Add libqb-devel as a dependancy of pacemaker-libs-devel
- Medium: PE: Report resources as active in correct data about resource location
  Resolves:  rhbz#799070
- Low: Tools: Bug rhbz#801351 - Fix crm_report help text
  Resolves: rhbz#801351

* Thu Mar 1 2012 Andrew Beekhof <abeekhof@redhat.com> - 1.1.7-2
- Update patch level to upstream version: c26e624
- Resolves: rhbz#720214 rhbz#720218 rhbz#754216 rhbz#789397
  For full details, see:
    https://github.com/ClusterLabs/pacemaker/compare/c26e624...148fccf

* Thu Feb 16 2012 Andrew Beekhof <abeekhof@redhat.com> - 1.1.7-1
- Update tarball to upstream version: 148fccf
  See included ChangeLog file or, for full details:
    https://github.com/ClusterLabs/pacemaker/compare/148fccf...a12de08
- Add libqb-devel as a build dependancy
- Resolves: rhbz#782255 rhbz#754216 rhbz#729035
- Related:  rhbz#790627

* Wed Oct 19 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.6-3
- Resolves: rhbz#745526

* Thu Oct 06 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.6-2
- Restore the ExclusiveArch directive
- Related: rhbz#743175

* Thu Oct 06 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.6-1
- Update tarball to upstream version: a02c0f1
  See included ChangeLog file or, for full details:
    https://github.com/ClusterLabs/pacemaker/compare/a12de08...a02c0f1
- Do not build in support for snmp, esmtp by default
- Create a package for cluster unaware libraries to minimze our footprint
  on non-cluster nodes
- Better subpackage descriptions
- Resolves: rhbz#743175

* Mon Aug 08 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-8
- Update patch level to: 8ab3842021a5
- Resolves: rhbz#729035

* Mon Aug 08 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-7
- Fix install typo
- Related: rhbz#720136

* Mon Aug 08 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-6
- Update tarball to upstream version: b933cbea41b5
- Resolves: rhbz#708797
- Resolves: rhbz#451848
- Resolves: rhbz#708722
- Resolves: rhbz#720136

* Fri Mar 25 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-5
- Fix another multi-lib header issue
- Related: rhbz#668466

* Fri Mar 25 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-4
- Fix multi-lib header issue
- Related: rhbz#668466

* Tue Mar 22 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-3
- Resolves: rhbz#684838 - Correctly notify fenced of a successful fencing event

* Fri Mar 18 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-2
- Fix cman integration
- Resolves: rhbz#684838 - Correctly notify fenced of a successful fencing event
- Resolves: rhbz#684825 - Ensure Pacemaker uses the most recent membership/quorum information

* Thu Mar 10 2011 Andrew Beekhof <abeekhof@redhat.com> - 1.1.5-1
- Fix rpmlint warnings
- Rebase on new upstream release
  See included ChangeLog file or http://hg.clusterlabs.org/pacemaker/1.1/file/tip/ChangeLog for details
  + Bugs lf#2445, lf#2493, lf#2508, lf#2518, lf#2527, lf#2544,
         lf#2545, lf#2550, lf#2551, lf#2554, lf#2558, bnc#665131
- Resolves: rhbz#676286 - Add per device 'diag' option to pacemaker stonith action

* Fri Jan 14 2011 Andrew Beekhof <andrew@beekhof.net> 1.1.4-1
- Resolves: rhbz#668466
- Update tarball to upstream version: 3ac6ac993d6d
  + Performance improvements for larger clusters
  + Miscellaneous bug fixes

* Tue Jul 13 2010 Andrew Beekhof <andrew@beekhof.net> 1.1.2-7
- Resolves: rhbz#610815 - add cman support
  + High: ais: Use service slot 10 to avoid conflicting with cman

* Sat Jul 10 2010 Andrew Beekhof <andrew@beekhof.net> 1.1.2-6
- Resolves: rhbz#610815 - add cman support
  + High: cib: Also free query result for xpath operations that return more than one hit
  + High: cib: Fix the application of unversioned diffs
  + High: Core: Correctly unpack HA_Messages containing multiple entries with the same name
  + High: Core: Resolve coverity RESOURCE_LEAK defects
  + High: crmd: All nodes should see status updates, not just he DC
  + High: crmd: Allow non-DC nodes to clear failcounts too
  + High: crmd: Base DC election on process relative uptime
  + High: crmd: Make sure the membership cache is accurate after a sucessful fencing operation
  + High: crmd: Make sure we always poke the FSA after a transition to clear any TE_HALT actions
  + High: crmd: Prevent segmentation fault
  + High: PE: Avoid creating invalid ordering constraints for probes that are not needed
  + High: PE: Bug lf#1959 - Fail unmanaged resources should not prevent other services from shutting down
  + High: PE: Bug lf#2422 - Ordering dependencies on partially active groups not observed properly
  + High: PE: Bug lf#2424 - Use notify oepration definition if it exists in the configuration
  + High: PE: Bug lf#2433 - No services should be stopped until probes finish
  + High: PE: Correctly detect when there is a real failcount that expired and needs to be cleared
  + High: PE: Correctly handle pseudo action creation
  + High: PE: Fix colocation for interleaved clones
  + High: PE: Fix colocation with partially active groups
  + High: PE: Fix potential use-after-free defect from coverity
  + High: PE: Fix use-after-free in order_actions() reported by valgrind
  + High: PE: Prevent endless loop when looking for operation definitions in the configuration
  + High: stonith: Correctly parse pcmk_host_list parameters that appear on a single line
  + High: tools: crm_simulate - Resolve coverity USE_AFTER_FREE defect

* Tue May 25 2010 Andrew Beekhof <andrew@beekhof.net> 1.1.2-5
- Resolves: rhbz#594296 - rpmdiff checks
  + Remove legacy scripts
  + Add missing man pages
  + Fix sub-package version requires

* Tue May 18 2010 Andrew Beekhof <andrew@beekhof.net> 1.1.2-3
- Resolves: rhbz#590667
- Rebase on new upstream release
  + High: Core: Bug lf#2401 - Backed out changeset 6e6980376f01

* Wed May 12 2010 Andrew Beekhof <andrew@beekhof.net> 1.1.2-2
- Do not build on ppc and ppc64.
  Resolves: rhbz#590992
- Rebase on new upstream release
  + High: ais: Do not count votes from offline nodes and calculate current votes before sending quorum data
  + High: ais: Ensure the list of active processes sent to clients is always up-to-date
  + High: ais: Look for the correct conf variable for turning on file logging
  + High: ais: Use the threadsafe version of getpwnam
  + High: Core: Bug lf#2414 - Prevent use-after-free reported by valgrind when doing xpath based deletions
  + High: Core: fix memory leaks exposed by valgrind
  + High: crmd: Bug 2401 - Improved detection of partially active peers
  + High: crmd: Bug lf#2379 - Ensure the cluster terminates when the PE is not available
  + High: crmd: Bug lf#2414 - Prevent use-after-free of the PE connection after it dies
  + High: crmd: Bug lf#2414 - Prevent use-after-free of the stonith-ng connection
  + High: crmd: Do not allow the target_rc to be misused by resource agents
  + High: crmd: Do not ignore action timeouts based on FSA state
  + High: crmd: Ensure we dont get stuck in S_PENDING if we loose an election to someone that never talks to us again
  + High: crmd: Fix memory leaks exposed by valgrind
  + High: crmd: Remove race condition that could lead to multiple instances of a clone being active on a machine
  + High: crmd: Send erase_status_tag() calls to the local CIB when the DC is fenced, since there is no DC to accept them
  + High: crmd: Use global fencing notifications to prevent secondary fencing operations of the DC
  + High: PE: Bug lf#2317 - Avoid needless restart of primitive depending on a clone
  + High: PE: Bug lf#2361 - Ensure clones observe mandatory ordering constraints if the LHS is unrunnable
  + High: PE: Bug lf#2383 - Combine failcounts for all instances of an anonymous clone on a host
  + High: PE: Bug lf#2384 - Fix intra-set colocation and ordering
  + High: PE: Bug lf#2403 - Enforce mandatory promotion (colocation) constraints
  + High: PE: Bug lf#2412 - Correctly locate clone instances by their prefix
  + High: PE: Don ot be so quick to pull the trigger on nodes that are coming up
  + High: PE: Fix memory leaks exposed by valgrind
  + High: PE: Repair handling of unordered groups in RHS ordering constraints
  + High: PE: Rewrite native_merge_weights() to avoid Fix use-after-free
  + High: Shell: always reload status if working with the cluster (bnc#590035)
  + High: Shell: check timeouts also against the default-action-timeout property
  + High: Shell: Default to using the status section from the live CIB (bnc#592762)
  + High: Shell: edit multiple meta_attributes sets in resource management (lf#2315)
  + High: Shell: enable comments (lf#2221)
  + High: Tools: crm_mon - fix memory leaks exposed by valgrind

* Mon Mar 08 2010 Andrew Beekhof <andrew@beekhof.net> - 1.1.1-2
- Resolves: rhbz#570807 - Offline nodes should not have their quorum votes counted

* Thu Mar 04 2010 Andrew Beekhof <andrew@beekhof.net> - 1.1.1-1
- Resolves: rhbz#559868
- Split off the doc package as it has grown quite large
- Split off the cluster test suite (CTS) so that it can be used by other projects
- Update the tarball from upstream to version 46e288ab9014
  + High: PE: Repair handling of unordered groups in RHS ordering constraints
  + High: Agents: Prevent shell expansion of '*' when there are files in /var/lib/heartbeat/cores/root
  + High: ais: Bug lf#2340 - Force rogue child processes to terminate after waiting 2.5 minutes
  + High: ais: Bug lf#2359 - Default expected votes to 2 inside Corosync/OpenAIS plugin
  + High: ais: Bug lf#2359 - expected-quorum-votes not correctly updated after membership change
  + High: ais: Bug rhbz#525552 - Move non-threadsafe calls to setenv() to after the fork()
  + High: crmd: Bug bnc#578644 - Improve handling of cancelled operations caused by resource cleanup
  + High: crmd: Make sure we wait for fencing to complete before continuing
  + High: crmd: Prevent use-of-NULL when non-DCs get stonith callbacks
  + High: Fencing: Account for stonith_get_info() always returning a pointer to the same static buffer
  + High: Fencing: Bug bnc#577007 - Correctly parse the hostlist output from stonith agents
  + High: Fencing: Correctly parse arg maps and do not return a provider for unknown agents
  + High: fencing: Fix can_fence_host_with_device() logic and improve hostlist output parsing
  + High: PE: Bug lf#2358 - Fix master-master anti-colocation
  + High: PE: Correctly implement optional colocation between primitives and clone resources
  + High: PE: Suppress duplicate ordering constraints to achieve orders of magnitude speed increases for large clusters
  + High: Shell: move scores from resource sets to the constraint element (lf#2331)
  + High: Shell: recovery from bad/outdated help index file
  + Medium: Shell: implement lifetime for rsc migrate and node standby (lf#2353)
  + Medium: Shell: node attributes update in configure (bnc#582767)

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.0-2
- Resolves: rhbz#568008
- Do not build pacemaker on s390 and s390x.

* Fri Jan 15 2010 Andrew Beekhof <andrew@beekhof.net> - 1.1.0-1
- Related: rhbz#543948
- Update the tarball from upstream to version 07ab245be519
  + High: crmd: Always connect to stonith
  + High: crmd: Ensure batch-limit is correctly enforced
  + High: crmd: Ensure we have the latest status after a transition abort
  + High: Fencing: Overhaul the fencing daemon
  + High: PE: Bug lf#2153 - non-clones shouldn't restart when clones stop/start on other nodes - improved
  + Medium: PE: Allow resource sets to be reused between ordering and colocation constraints
  + Medium: PE: Implement serializing order constraints that dont cause restarts or inhibit migration
  + Medium: PE: Include node attributes for the node to be fenced
  + Medium: PE: Make crm_simulate a full replacement for ptest
  + Medium: PE: Only complain about target-role=master for non m/s resources
  + Medium: PE: Prevent non-multistate resources from being promoted through target-role
  + Medium: PE: Simplify the rsc_order syntax - don't make funky inferences based on score
  + Medium: PE: Support serialized sets of resources
  + Medium: Tools: Bug lf#2286 - Allow the shell to accept template parameters on the command line
  + Medium: Tools: Bug lf#2307 - Provide a way to determin the nodeid of past cluster members
  + Medium: Tools: crm: add update method to template apply (LF 2289)
  + Medium: Tools: crm: direct RA interface for stonith class resource agents (LF 2270)
  + Medium: Tools: crm: don't remove sets which contain id-ref attribute (LF 2304)
  + Medium: Tools: crm: exclude locations when testing for pathological constraints (LF 2300)
  + Medium: Tools: crm: fix exit code on single shot commands
  + Medium: Tools: crm: fix node delete (LF 2305)
  + Medium: Tools: crm: implement -F (--force) option
  + Medium: Tools: crm: rename status to cibstatus (LF 2236)
  + Medium: Tools: crm: stay in crm if user specified level only (LF 2286)

* Tue Dec 15 2009 Andrew Beekhof <andrew@beekhof.net> - 1.1.0-0.1-00d9bcac8775.hg
- Related: rhbz#rhbz#543948
- Update the tarball from upstream to version 00d9bcac8775
  + High: PE: Bug 2213 - Ensure groups process location constraints so that clone-node-max works for cloned groups
  + High: PE: Bug lf#2153 - Update regression tests
  + High: PE: Bug lf#2153 - non-clones shouldn't restart when clones stop/start on other nodes
  + High: PE: Bug lf#2209 - Clone ordering should be able to prevent startup of dependant clones
  + High: PE: Bug lf#2216 - Correctly identify the state of anonymous clones when deciding when to probe
  + High: PE: Bug lf#2225 - Operations that require fencing should wait for 'stonith_complete' not 'all_stopped'.
  + High: PE: Bug lf#2225 - Prevent clone peers from stopping while another is instance is (potentially) being fenced
  + High: PE: Correctly anti-colocate with a group
  + High: PE: Correctly unpack ordering constraints for resource sets to avoid graph loops
  + High: Replace stonithd with the new fencing subsystem
  + High: cib: Ensure the loop searching for a remote login message terminates
  + High: cib: Finally fix reliability of receiving large messages over remote plaintext connections
  + High: cib: Fix remote notifications
  + High: cib: For remote connections, default to CRM_DAEMON_USER since thats the only one that the cib can validate the password for using PAM
  + High: cib: Remote plaintext - Retry sending parts of the message that didn't fit the first time
  + Medium: PE: Bug lf#2206 - rsc_order constraints always use score at the top level
  + Medium: PE: Provide a default action for resource-set ordering
  + Medium: PE: Silently fix requires=fencing for stonith resources so that it can be set in op_defaults
  + Medium: ais: Some clients such as gfs_controld want a cluster name, allow one to be specified in corosync.conf
  + Medium: cib: Create valid notification control messages
  + Medium: cib: Indicate where the remote connection came from
  + Medium: cib: Send password prompt to stderr so that stdout can be redirected
  + Medium: extra: Add the daemon parameter to the controld metadata
  + Medium: fencing: Re-engineer the stonith daemon to support RHCS agents
  + Medium: tools: Make crm_mon functional with remote connections
  + Medium: xml: Bug bnc#552713 - Treat node unames as text fields not IDs
  + Medium: xml: Bug lf#2215 - Create an always-true expression for empty rules when upgrading from 0.6

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.5-6.2
- Rebuilt for RHEL 6

* Wed Nov 25 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.5-6.1
- Rebuilt for RHEL 6

* Sat Oct 31 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-6
- Let snmp automatically pull in lm_sensors-devel if required
  and available on that arch (its not on s390x)

* Sat Oct 31 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-5
- Disable Heartbeat support

* Thu Oct 29 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-4
- Include the fixes from CoroSync integration testing
- Move the resource templates - they're not documentation
- Ensure documentation is placed in a standard location
- Exclude documentation that is included elsewhere in the package

- Update the tarball from upstream to version ee19d8e83c2a
  + High: cib: Correctly clean up when both plaintext and tls remote ports are requested
  + High: PE: Bug bnc#515172 - Provide better defaults for lt(e) and gt(e) comparisions
  + High: PE: Bug lf#2197 - Allow master instances placemaker to be influenced by colocation constraints
  + High: PE: Make sure promote/demote pseudo actions are created correctly
  + High: PE: Prevent target-role from promoting more than master-max instances
  + High: ais: Bug lf#2199 - Prevent expected-quorum-votes from being populated with garbage
  + High: ais: Prevent deadlock - dont try to release IPC message if the connection failed
  + High: cib: For validation errors, send back the full CIB so the client can display the errors
  + High: cib: Prevent use-after-free for remote plaintext connections
  + High: crmd: Bug lf#2201 - Prevent use-of-NULL when running heartbeat

* Tue Oct 13 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-3
- Update the tarball from upstream to version 38cd629e5c3c
  + High: Core: Bug lf#2169 - Allow dtd/schema validation to be disabled
  + High: PE: Bug lf#2106 - Not all anonymous clone children are restarted after configuration change
  + High: PE: Bug lf#2170 - stop-all-resources option had no effect
  + High: PE: Bug lf#2171 - Prevent groups from starting if they depend on a complex resource which can't
  + High: PE: Disable resource management if stonith-enabled=true and no stonith resources are defined
  + High: PE: Don't include master score if it would prevent allocation
  + High: ais: Avoid excessive load by checking for dead children every 1s (instead of 100ms)
  + High: ais: Bug rh#525589 - Prevent shutdown deadlocks when running on CoroSync
  + High: ais: Gracefully handle changes to the AIS nodeid
  + High: crmd: Bug bnc#527530 - Wait for the transition to complete before leaving S_TRANSITION_ENGINE
  + High: crmd: Prevent use-after-free with LOG_DEBUG_3
  + Medium: xml: Mask the "symmetrical" attribute on rsc_colocation constraints (bnc#540672)
  + Medium (bnc#520707): Tools: crm: new templates ocfs2 and clvm
  + Medium: Build: Invert the disable ais/heartbeat logic so that --without (ais|heartbeat) is available to rpmbuild
  + Medium: PE: Bug lf#2178 - Indicate unmanaged clones
  + Medium: PE: Bug lf#2180 - Include node information for all failed ops
  + Medium: PE: Bug lf#2189 - Incorrect error message when unpacking simple ordering constraint
  + Medium: PE: Correctly log resources that would like to start but can't
  + Medium: PE: Stop ptest from logging to syslog
  + Medium: ais: Include version details in plugin name
  + Medium: crmd: Requery the resource metadata after every start operation

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.5-2.1
- rebuilt with new openssl

* Wed Aug 19 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-2
- Add versioned perl dependancy as specified by
    https://fedoraproject.org/wiki/Packaging/Perl#Packages_that_link_to_libperl
- No longer remove RPATH data, it prevents us finding libperl.so and no other
  libraries were being hardcoded
- Compile in support for heartbeat
- Conditionally add heartbeat-devel and corosynclib-devel to the -devel requirements
  depending on which stacks are supported

* Mon Aug 17 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-1
- Add dependancy on resource-agents
- Use the version of the configure macro that supplies --prefix, --libdir, etc
- Update the tarball from upstream to version 462f1569a437 (Pacemaker 1.0.5 final)
  + High: Tools: crm_resource - Advertise --move instead of --migrate
  + Medium: Extra: New node connectivity RA that uses system ping and attrd_updater
  + Medium: crmd: Note that dc-deadtime can be used to mask the brokeness of some switches

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.5-0.7.c9120a53a6ae.hg
- Use bzipped upstream tarball.

* Wed Jul  29 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-0.6.c9120a53a6ae.hg
- Add back missing build auto* dependancies
- Minor cleanups to the install directive

* Tue Jul  28 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-0.5.c9120a53a6ae.hg
- Add a leading zero to the revision when alphatag is used

* Tue Jul  28 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.5-0.4.c9120a53a6ae.hg
- Incorporate the feedback from the cluster-glue review
- Realistically, the version is a 1.0.5 pre-release
- Use the global directive instead of define for variables
- Use the haclient/hacluster group/user instead of daemon
- Use the _configure macro
- Fix install dependancies

* Fri Jul  24 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.4-3
- Include an AUTHORS and license file in each package
- Change the library package name to pacemaker-libs to be more
  Fedora compliant
- Remove execute permissions from xml related files
- Reference the new cluster-glue devel package name
- Update the tarball from upstream to version c9120a53a6ae
  + High: PE: Only prevent migration if the clone dependancy is stopping/starting on the target node
  + High: PE: Bug 2160 - Dont shuffle clones due to colocation
  + High: PE: New implementation of the resource migration (not stop/start) logic
  + Medium: Tools: crm_resource - Prevent use-of-NULL by requiring a resource name for the -A and -a options
  + Medium: PE: Prevent use-of-NULL in find_first_action()
  + Low: Build: Include licensing files

* Tue Jul 14 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.4-2
- Reference authors from the project AUTHORS file instead of listing in description
- Change Source0 to reference the project's Mercurial repo
- Cleaned up the summaries and descriptions
- Incorporate the results of Fedora package self-review

* Tue Jul 14 2009 Andrew Beekhof <andrew@beekhof.net> - 1.0.4-1
- Initial checkin
