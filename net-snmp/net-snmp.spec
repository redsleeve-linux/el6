# use netsnmp_tcp_wrappers 0 to disable tcp_wrappers support
%{!?netsnmp_tcp_wrappers:%global netsnmp_tcp_wrappers 1}
# use nestnmp_check 0 to speed up packaging by disabling 'make test'
%{!?netsnmp_check: %global netsnmp_check 0}
# use netsnmp_enable_gui 1 to add net-snmp-gui subpackage
# (we don't have perl-Tk in RHEL6)
%{!?netsnmp_enable_gui: %global netsnmp_enable_gui 0}

# Arches on which we need to prevent arch conflicts on net-snmp-config.h
%define multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64 sparc sparcv9 sparc64
# allow compilation on old Fedoras
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: A collection of SNMP protocol tools and libraries
Name: net-snmp
Version: 5.5
Release: 57%{?dist}.1.0
Epoch: 1

License: BSD
Group: System Environment/Daemons
URL: http://net-snmp.sourceforge.net/
Source0: net-snmp-%{version}-noapsl.tar.gz
# Original source: http://dl.sourceforge.net/net-snmp/net-snmp-%{version}.tar.gz
# Net-snmp contains code licensed under APSL 1.1. This code is used on MacOS only,
# and it must be removed from source code before we distribute source RPM.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh 5.5
Source1: net-snmp.redhat.conf
Source2: net-snmpd.init
Source3: net-snmptrapd.init
Source4: net-snmp-config.h
Source5: net-snmp-config
Source6: net-snmp-trapd.redhat.conf
Source7: net-snmpd.sysconfig
Source8: net-snmptrapd.sysconfig
Patch1: net-snmp-5.4.1-pie.patch
Patch2: net-snmp-5.5-dir-fix.patch
Patch3: net-snmp-5.5-multilib.patch
Patch4: net-snmp-5.5-sensors3.patch
Patch5: net-snmp-5.5-udptable-index.patch
Patch6: net-snmp-5.5-missing-bcast.patch
Patch7: net-snmp-5.5-arp-ioctl.patch
Patch8: net-snmp-5.5-broadcast-response.patch
Patch9: net-snmp-5.5-createview.patch
Patch10: net-snmp-5.5-ip-32truncate.patch
Patch11: net-snmp-5.5-leaks.patch
Patch12: net-snmp-5.5-rmon-leak.patch
Patch13: net-snmp-5.5-man-netstat.patch
Patch14: net-snmp-5.5-test-tmpdir.patch
Patch15: net-snmp-5.5-rmon-fd-leak.patch
Patch16: net-snmp-5.5-ifdown-speed.patch
Patch17: net-snmp-5.5-bridge-mib.patch
Patch18: net-snmp-5.5-fix-u-parameter.patch
Patch19: net-snmp-5.5-test-udp6.patch
Patch20: net-snmp-5.5-ber-parse.patch
Patch21: net-snmp-5.5-parse-args-exit.patch
Patch22: net-snmp-5.5-leaks2.patch
Patch23: net-snmp-5.5-hrFSTable-indexes.patch
Patch24: net-snmp-5.5-stats-typo.patch
Patch25: net-snmp-5.5-include-struct.patch
Patch26: net-snmp-5.5-disman-crash.patch
Patch27: net-snmp-5.5-ipv6-forwarding.patch
Patch28: net-snmp-5.5-translate-unsigned-range.patch
Patch29: net-snmp-5.5-mktemp-size.patch
Patch30: net-snmp-5.5-gfs.patch
Patch31: net-snmp-5.5-sysobjectid-truncation.patch
Patch32: net-snmp-5.5-negative-stats.patch
Patch33: net-snmp-5.5-skip-ipv6-tests.patch
Patch34: net-snmp-5.5-smux-ppc.patch
Patch35: net-snmp-5.5-walk-oid-compare.patch
Patch36: net-snmp-5.5-ipv6-create-ipAddress.patch
Patch37: net-snmp-5.5-no-prefix-threads.patch
Patch38: net-snmp-5.5-reload-ipv6IfTable.patch
Patch39: net-snmp-5.5-bridge-mib2.patch
Patch40: net-snmp-5.5-64bit-wrap.patch
Patch41: net-snmp-5.5-smux-crash.patch
Patch42: net-snmp-5.5-bridge-mib3.patch
Patch43: net-snmp-5.5-python-regex.patch
Patch44: net-snmp-5.5-python-session-init.patch
Patch45: net-snmp-5.5-arp-null-check.patch
Patch46: net-snmp-5.5-xfs.patch
Patch47: net-snmp-5.5-pass-persist-sigchld.patch
Patch48: net-snmp-5.5-ifTable-duplicate-message.patch
Patch49: net-snmp-5.5-duplicate-ifTable-entry.patch
Patch50: net-snmp-5.5-trap-perl-leak.patch
Patch51: net-snmp-5.5-timezone-offset.patch
Patch52: net-snmp-5.5-systemstats-overflow.patch
Patch53: net-snmp-5.5-proc-crash.patch
Patch54: net-snmp-5.5-relro.patch
Patch55: net-snmp-5.5-smux-reqid.patch
Patch56: net-snmp-5.5-agentx-crash.patch
Patch57: net-snmp-5.5-agentx-many-subagents-crash.patch
Patch58: net-snmp-5.5-sysobjectid-truncation2.patch
Patch59: net-snmp-5.5-bridge-mib-ifIndex.patch
Patch60: net-snmp-5.5-proxy-logging.patch
Patch61: net-snmp-5.5-hrStorage-realStorageUnits.patch
Patch62: net-snmp-5.5-hrStorage-realStorageUnits2.patch
Patch63: net-snmp-5.5-hrStorage-fs.patch
Patch64: net-snmp-5.5-perl-reload-crash.patch
Patch65: net-snmp-5.5-snmpTargetAddrRowStatus-length.patch
Patch66: net-snmp-5.5-mibindex-crash.patch
Patch67: net-snmp-5.5-agentx-memleak.patch
Patch68: net-snmp-5.5-tcpTable-timeouts.patch
Patch69: net-snmp-5.5-iftable-row-restore.patch
Patch70: net-snmp-5.3.2.2-proxy-getnext.patch
Patch71: net-snmp-5.5-CVE-2012-2141.patch
Patch72: net-snmp-5.5-exec-dynamic.patch
Patch73: net-snmp-5.5-exec-cmdline.patch
Patch74: net-snmp-5.5-perl-rpath.patch
Patch75: net-snmp-5.5-clientaddr-port.patch
Patch76: net-snmp-5.5-trapd-perl-kill.patch
Patch77: net-snmp-5.5-trapsess-engineid.patch
Patch78: net-snmp-5.5-snmptrap-c-option.patch
Patch79: net-snmp-5.5-getnext-loop.patch
Patch80: net-snmp-5.5-diskIOLA.patch
Patch81: net-snmp-5.5-c64-wrap-errors.patch
Patch82: net-snmp-5.5-ipv6-messages.patch
Patch83: net-snmp-5.3.2.2-proc-counting.patch
Patch84: net-snmp-5.5-broadcast-response2.patch
Patch85: net-snmp-5.5-extTable-crash.patch
Patch86: net-snmp-5.5-ber-int-size.patch
Patch87: net-snmp-5.5-extend-realloc-leak.patch
Patch88: net-snmp-5.5-man-config-path.patch
Patch89: net-snmp-5.5-kernel-threads.patch
Patch90: net-snmp-5.5-python-retcodes.patch
Patch91: net-snmp-5.5-agentx-disconnect-crash.patch
Patch92: net-snmp-5.5-includefile.patch
Patch93: net-snmp-5.5-includefile-abi.patch
Patch94: net-snmp-5.5-netlink-msgsize.patch
Patch95: net-snmp-5.5-ifspeed-any.patch
Patch96: net-snmp-5.5-bridge-mib-bridge-port.patch
Patch97: net-snmp-5.5-agentaddress-hup.patch
Patch98: net-snmp-5.5-dskTable-dynamic.patch
Patch99: net-snmp-5.5-ber-int-size2.patch
Patch100: net-snmp-5.5-sendmail.patch
Patch101: net-snmp-5.7.2-fips.patch
Patch102: net-snmp-5.5-diskio-whitelist.patch
Patch103: net-snmp-5.7.2-icmp-mib.patch
Patch104: net-snmp-5.5-hrSWRunTable-cache.patch
Patch105: net-snmp-5.5-mvfs.patch
Patch106: net-snmp-5.5-snmptrapd-forward-crash.patch
Patch107: net-snmp-5.5-hrSystemProcesses.patch
Patch108: net-snmp-5.5-arp-cache.patch
Patch109: net-snmp-5.5-clientaddr-error-msg.patch
Patch110: net-snmp-5.5-clientaddr-error-msg2.patch
Patch111: net-snmp-5.5-perl-warn-security.patch
Patch112: net-snmp-5.5-iptable-broadcast.patch
Patch113: net-snmp-5.5-agentx-client-crash.patch
Patch114: net-snmp-5.5-monitor-crash.patch
Patch115: net-snmp-5.5-counter-assert.patch
Patch116: net-snmp-5.5-smux-64bit.patch
Patch117: net-snmp-5.5-hrProcessorLoad-many-cpus.patch
Patch118: net-snmp-5.5-create-user-multilib.patch
Patch119: net-snmp-5.5-python-addr-size.patch
Patch120: net-snmp-5.5-hrStorage-31bits.patch
Patch121: net-snmp-5.5-man-links.patch
Patch122: net-snmp-5.5-storageUseNFS.patch
Patch123: net-snmp-5.5-python-snmpset-zero.patch
Patch124: net-snmp-5.5-smux-logging.patch
Patch125: net-snmp-5.5-trap-forward-reqid.patch
Patch126: net-snmp-5.5-mib-typos.patch
Patch127: net-snmp-5.5-extend-close.patch
Patch128: net-snmp-5.5-sensors-duplicate.patch
Patch129: net-snmp-5.5-device-large-ifindex.patch
Patch130: net-snmp-5.5-null-integer.patch
Patch131: net-snmp-5.5-ipAddress-faster-load.patch
Patch132: net-snmp-5.5-incomplete-parse.patch
Patch133: net-snmp-5.5-udp6-clientaddr.patch
Patch134: net-snmp-5.5-agentx-big-packet.patch
Patch135: net-snmp-5.5-systemstats-ipv4.patch
Patch136: net-snmp-5.5-client-write-var.patch
Patch137: net-snmp-5.5-mib-typos2.patch
Patch138: net-snmp-5.5-client-udp6.patch
Patch139: net-snmp-5.5-duplicate-ipAddress-log.patch
Patch140: net-snmp-5.5-sctp-fd-leak.patch
Patch141: net-snmp-5.5-large-fdset.patch
# An SNMPv3 request with a small max message size can lead to SNMPv1/2c bulk requests timing out (#1363606)
Patch142: net-snmp-5.5-pdu-version.patch

Requires(post): chkconfig
Requires(preun): chkconfig
# for /sbin/service
Requires(preun): initscripts
# for /bin/rm
Requires(preun): coreutils
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: openssl-devel, bzip2-devel, elfutils-devel
BuildRequires: libselinux-devel, elfutils-libelf-devel, rpm-devel
BuildRequires: perl-devel, perl(ExtUtils::Embed), gawk, procps
BuildRequires: python-devel, python-setuptools
BuildRequires: chrpath
# for netstat, needed by 'make test'
BuildRequires: net-tools
%ifnarch s390 s390x
BuildRequires: lm_sensors-devel >= 3
%endif
%if %{netsnmp_tcp_wrappers}
BuildRequires: tcp_wrappers-devel
%endif

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management. The NET-SNMP project includes various SNMP tools:
an extensible agent, an SNMP library, tools for requesting or setting
information from SNMP agents, tools for generating and handling SNMP
traps and a version of the netstat command which uses SNMP. This
package contains the snmpd and snmptrapd daemons, documentation, etc.

You will probably also want to install the net-snmp-utils package,
which contains NET-SNMP utilities.

%package utils
Group: Applications/System
Summary: Network management utilities using SNMP, from the NET-SNMP project
Requires: %{name}-libs = %{epoch}:%{version}-%{release}

%description utils
The net-snmp-utils package contains various utilities for use with the
NET-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You will also need to install the net-snmp
package.

%package devel
Group: Development/Libraries
Summary: The development environment for the NET-SNMP project
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
Requires: elfutils-devel, rpm-devel, elfutils-libelf-devel, openssl-devel
%if %{netsnmp_tcp_wrappers}
Requires: tcp_wrappers-devel
%endif
%ifnarch s390 s390x
Requires: lm_sensors-devel
%endif

%description devel
The net-snmp-devel package contains the development libraries and
header files for use with the NET-SNMP project's network management
tools.

Install the net-snmp-devel package if you would like to develop
applications for use with the NET-SNMP project's network management
tools. You'll also need to have the net-snmp and net-snmp-utils
packages installed.

%package perl
Group: Development/Libraries
Summary: The perl NET-SNMP module and the mib2c tool
Requires: %{name}-libs = %{epoch}:%{version}-%{release}, perl
BuildRequires: perl

%description perl
The net-snmp-perl package contains the perl files to use SNMP from within
Perl.

Install the net-snmp-perl package, if you want to use mib2c or SNMP 
with perl.

%if %{netsnmp_enable_gui}
%package gui
Group: Applications/System
Summary: An interactive graphical MIB browser for SNMP
Requires: perl-Tk, net-snmp-perl = %{epoch}:%{version}-%{release}

%description gui
The net-snmp-gui package contains tkmib utility, which is a graphical user 
interface for browsing the Message Information Bases (MIBs). It is also 
capable of sending or retrieving the SNMP management information to/from 
the remote agents interactively.

Install the net-snmp-gui package, if you want to use this interactive utility.
%endif

%package libs
Group: Development/Libraries
Summary: The NET-SNMP runtime libraries
# the libs link against libperl.so:
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description libs
The net-snmp-libs package contains the runtime libraries for shared binaries
and applications.

%package python
Group: Development/Libraries
Summary: The Python 'netsnmp' module for the NET-SNMP
Requires: %{name}-libs = %{epoch}:%{version}-%{release}

%description python
The 'netsnmp' module provides a full featured, tri-lingual SNMP (SNMPv3, 
SNMPv2c, SNMPv1) client API. The 'netsnmp' module internals rely on the
Net-SNMP toolkit library.


%prep
%setup -q

%ifnarch ia64
%patch1 -p1 -b .pie
%endif

%patch2 -p1 -b .dir-fix
%patch3 -p1 -b .multilib
%patch4 -p1 -b .sensors %{?_rawbuild}
%patch5 -p1 -b .udptable-index
%patch6 -p1 -b .missing-bcast
%patch7 -p1 -b .arp-ioctl
%patch8 -p1 -b .broadcast-response
%patch9 -p1 -b .createview
%patch10 -p1 -b .truncate-32
%patch11 -p1 -b .leaks
%patch12 -p1 -b .rmon-leak
%patch13 -p1 -b .man-netstat
# no backup of the following one! the backup would be executed!
%patch14 -p1
%patch15 -p1 -b .rmon-fd-leak
%patch16 -p1 -b .ifdown-speed
%patch17 -p0
%patch18 -p1 -b .fix-u-parameter
# no backup of the following one! the backup would be executed!
%patch19 -p1
%patch20 -p1 -b .ber-parse
%patch21 -p1 -b .parse-arg-exit
%patch22 -p1 -b .leaks2
%patch23 -p1 -b .hrFSTable-indexes
%patch24 -p1 -b .stats-typo
%patch25 -p1 -b .include-struct
%patch26 -p1 -b .disman-crash
%patch27 -p1 -b .ipv6-forwarding.patch
%patch28 -p1 -b .translate-unsigned-range
%patch29 -p1 -b .mktemp-size
%patch30 -p1 -b .gfs
%patch31 -p1 -b .sysobjectid
%patch32 -p1 -b .negative-stats
%patch33 -p1
%patch34 -p1 -b .smux-ppc
%patch35 -p2 -b .walk-oid-compare
%patch36 -p2 -b .ipv6-create
%patch37 -p1 -b .no-prefix-threads
%patch38 -p2 -b .reload
%patch39 -p2 -b .bridge-mib2
%patch40 -p2 -b .64bit-wrap
%patch41 -p2 -b .smux-crash
%patch42 -p2 -b .bridge-mib3
%patch43 -p1 -b .python-regex
%patch44 -p1 -b .python-session-init
%patch45 -p1 -b .arp-null-check
%patch46 -p1 -b .xfs
%patch47 -p1 -b .pass-persist-sigchld
%patch48 -p1 -b .ifTable-duplicate-message
%patch49 -p1 -b .duplicate-ifTable-entry
%patch50 -p1 -b .trap-perl-leak
%patch51 -p1 -b .timezone-offset
%patch52 -p1 -b .systemstats-overflow
%patch53 -p1 -b .proc-crash
%patch54 -p1 -b .relro
%patch55 -p1 -b .smux-reqid
%patch56 -p1 -b .agentx-crash
%patch57 -p1 -b .agentx-many-subagents-crash
%patch58 -p1 -b .sysobjectid-truncation2
%patch59 -p1 -b .bridge-mib-ifIndex
%patch60 -p1 -b .proxy-logging
%patch61 -p1 -b .realStorageUnits
%patch62 -p1 -b .realStorageUnits2
%patch63 -p1 -b .hrStorage-fs
%patch64 -p1 -b .perl-reload-crash
%patch65 -p1 -b .snmpTargetAddrRowStatus-length
%patch66 -p1 -b .mibindex-crash
%patch67 -p1 -b .agentx-memleak
%patch68 -p1 -b .tcpTable-timeout
%patch69 -p1 -b .iftable-row-restore
%patch70 -p2 -b .proxy-getnext
%patch71 -p1 -b .CVE-2012-2141
%patch72 -p1 -b .exec-dynamic
%patch73 -p1 -b .exec-cmdline
%patch74 -p1 -b .perl-rpath
%patch75 -p1 -b .clientaddr-port
%patch76 -p1 -b .trapd-perl-kill
%patch77 -p1 -b .trapsess-engineid
%patch78 -p1 -b .c-option
%patch79 -p1 -b .getnext-loop
%patch80 -p2 -b .diskIOLA
%patch81 -p1 -b .c64-wrap-errors
%patch82 -p1 -b .ipv6-messages
%patch83 -p2 -b .proc-counting
%patch84 -p1 -b .broadcast-response2
%patch85 -p1 -b .extTable-crash
%patch86 -p1 -b .ber-int-size
%patch87 -p1 -b .extend-realloc-leak
%patch88 -p1 -b .man-config-path
%patch89 -p1 -b .kernel-threads
%patch90 -p1 -b .python-retcodes
%patch91 -p1 -b .disconnect-crash
%patch92 -p1 -b .includefile
%patch93 -p1 -b .includefile-abi
%patch94 -p1 -b .netlink-msgsize
%patch95 -p1 -b .ifspeed-any
%patch96 -p1 -b .bridge-port
%patch97 -p1 -b .agentaddress-hup
%patch98 -p1 -b .dskTable-dynamic
%patch99 -p1 -b .ber-int-size2
%patch100 -p1 -b .sendmail
%patch101 -p1 -b .fips
%patch102 -p1 -b .diskio-whitelist
%patch103 -p1 -b .icmp-mib
%patch104 -p1 -b .hrSWRunTable-cache
%patch105 -p1 -b .mvfs
%patch106 -p1 -b .snmptrapd-forward-crash
%patch107 -p1 -b .hrSystemProcesses
%patch108 -p1 -b .arp-cache
%patch109 -p1 -b .clientaddr-error-msg
%patch110 -p1 -b .clientaddr-error-msg2
%patch111 -p1 -b .warn-security
%patch112 -p1 -b .iptable-broadcast
%patch113 -p1 -b .agentx-client-crash
%patch114 -p1 -b .monitor-crash
%patch115 -p1 -b .counter-assert
%patch116 -p1 -b .smux-64bit
%patch117 -p1 -b .hrProcessorLoad-many-cpus
%patch118 -p1 -b .create-user-multilib
%patch119 -p1 -b .python-addr-size
%patch120 -p1 -b .hrStorage-31bits
%patch121 -p1 -b .man-links
%patch122 -p1 -b .storageUseNFS
%patch123 -p1 -b .python-snmpset-zero
%patch124 -p1 -b .smux-logging
%patch125 -p1 -b .trap-forward-reqid
%patch126 -p1 -b .mib-typos
%patch127 -p1 -b .extend-close
%patch128 -p1 -b .sensors-duplicate
%patch129 -p1 -b .device-large-ifindex
%patch130 -p1 -b .null-integer
%patch131 -p1 -b .ipAddress-faster-load
%patch132 -p1 -b .incomplete-parse
%patch133 -p1 -b .udp6-clientaddr
%patch134 -p1 -b .agentx-big-packet
%patch135 -p1 -b .systemstats-ipv4
%patch136 -p1 -b .client-write-var
%patch137 -p1 -b .mib-typos2
%patch138 -p1 -b .client-udp6
%patch139 -p1 -b .duplicate-ipAddress-log
%patch140 -p1 -b .sctp-fd-leak
%patch141 -p1 -b .large-fdset
%patch142 -p1 -b .pdu-version

%build
MIBS="host agentx smux \
     ucd-snmp/diskio tcp-mib udp-mib mibII/mta_sendmail \
     ip-mib/ipv4InterfaceTable ip-mib/ipv6InterfaceTable \
     ip-mib/ipAddressPrefixTable/ipAddressPrefixTable \
     ip-mib/ipDefaultRouterTable/ipDefaultRouterTable \
     ip-mib/ipv6ScopeZoneIndexTable ip-mib/ipIfStatsTable \
     sctp-mib rmon-mib etherlike-mib"

%ifnarch s390 s390x
# there are no lm_sensors on s390
MIBS="$MIBS ucd-snmp/lmsensorsMib"
%endif

%configure \
    --disable-static --enable-shared \
    --with-cflags="$RPM_OPT_FLAGS -D_RPM_4_4_COMPAT" \
    --with-ldflags="-Wl,-z,relro -Wl,-z,now" \
    --with-sys-location="Unknown" \
    --with-logfile="/var/log/snmpd.log" \
    --with-persistent-directory="/var/lib/net-snmp" \
    --with-mib-modules="$MIBS" \
%if %{netsnmp_tcp_wrappers}
    --with-libwrap=yes \
%endif
    --sysconfdir=%{_sysconfdir} \
    --enable-ipv6 \
    --enable-ucd-snmp-compatibility \
    --with-openssl \
    --with-pic \
    --enable-embedded-perl \
    --enable-as-needed \
    --with-perl-modules="INSTALLDIRS=vendor" \
    --enable-mfd-rewrites \
    --enable-local-smux \
    --with-temp-file-pattern=/var/run/net-snmp/snmp-tmp-XXXXXX \
    --with-sys-contact="root@localhost" <<EOF
EOF

# remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# the package is not %_smp_mflags safe
make

# remove rpath from compiled perl libs
find perl/blib -type f -name "*.so" -print -exec chrpath --delete {} \;

# compile python module
pushd python
%{__python} setup.py --basedir="../" build
popd


%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

# Determine which arch net-snmp-config.h is going to try to #include.
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif

%ifarch %{multilib_arches}
# Do an net-snmp-config.h switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, as they each need
# their own correct-but-different versions of net-snmp-config.h to be usable.
mv ${RPM_BUILD_ROOT}/%{_bindir}/net-snmp-config ${RPM_BUILD_ROOT}/%{_bindir}/net-snmp-config-${basearch}
install -m 755 %SOURCE5 ${RPM_BUILD_ROOT}/%{_bindir}/net-snmp-config
mv ${RPM_BUILD_ROOT}/%{_includedir}/net-snmp/net-snmp-config.h ${RPM_BUILD_ROOT}/%{_includedir}/net-snmp/net-snmp-config-${basearch}.h
install -m644 %SOURCE4 ${RPM_BUILD_ROOT}/%{_includedir}/net-snmp/net-snmp-config.h
%endif

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp
install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmpd.conf
install -m 644 %SOURCE6 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmptrapd.conf

install -d ${RPM_BUILD_ROOT}%{_initrddir}
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}%{_initrddir}/snmpd
install -m 755 %SOURCE3 ${RPM_BUILD_ROOT}%{_initrddir}/snmptrapd

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %SOURCE7 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/snmpd
install -m 644 %SOURCE8 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/snmptrapd

# prepare /var/lib/net-snmp
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/lib/net-snmp
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/run/net-snmp

# remove things we don't want to distribute
rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpinform
ln -s snmptrap ${RPM_BUILD_ROOT}/usr/bin/snmpinform
rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpcheck
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/fixproc
rm -f ${RPM_BUILD_ROOT}/%{_mandir}/man1/fixproc*
rm -f ${RPM_BUILD_ROOT}/%{_bindir}/ipf-mod.pl
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.la
# remove special perl files
find $RPM_BUILD_ROOT -name perllocal.pod \
    -o -name .packlist \
    -o -name "*.bs" \
    -o -name Makefile.subs.pl \
    | xargs -ri rm -f {}
# remove docs that do not apply to Linux
rm -f README.aix README.hpux11 README.osX README.Panasonic_AM3X.txt README.solaris README.win32

# copy missing mib2c.conf files
install -m 644 local/mib2c.*.conf ${RPM_BUILD_ROOT}%{_datadir}/snmp

# install python module
pushd python
%{__python} setup.py --basedir=.. install -O1 --skip-build --root $RPM_BUILD_ROOT 
popd

find $RPM_BUILD_ROOT -name '*.so' | xargs chmod 0755

# trim down massive ChangeLog
dd bs=1024 count=250 if=ChangeLog of=ChangeLog.trimmed

# convert files to UTF-8
for file in README COPYING; do
    iconv -f 8859_1 -t UTF-8 <$file >$file.utf8
    mv $file.utf8 $file
done

# remove executable bit from documentation samples
chmod 644 local/passtest local/ipf-mod.pl

%if ! %{netsnmp_enable_gui}
rm -f $RPM_BUILD_ROOT/%{_bindir}/tkmib $RPM_BUILD_ROOT/%{_mandir}/man1/tkmib.1*
%endif

# dirty hack for #604636, until it's fixed properly upstream
install -m 755 -d $RPM_BUILD_ROOT/usr/include/net-snmp/agent/util_funcs
install -m 644  agent/mibgroup/util_funcs/*.h $RPM_BUILD_ROOT/usr/include/net-snmp/agent/util_funcs


%check
%if %{netsnmp_check}
LD_LIBRARY_PATH=${RPM_BUILD_ROOT}/%{_libdir} make test
%endif


%post
/sbin/chkconfig --add snmpd 
/sbin/chkconfig --add snmptrapd

# move local state files from /var/net-snmp to new location when updating the package
/bin/mv %{_localstatedir}/net-snmp/* %{_localstatedir}/lib/net-snmp/ &>/dev/null || :


%preun
if [ $1 = 0 ]; then
    service snmpd stop >/dev/null 2>&1
    /sbin/chkconfig --del snmpd
    service snmptrapd stop >/dev/null 2>&1
    /sbin/chkconfig --del snmptrapd
fi


%postun
if [ "$1" -ge "1" ]; then
    service snmpd condrestart >/dev/null 2>&1 || :
    service snmptrapd condrestart >/dev/null 2>&1 || :
fi

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog.trimmed EXAMPLE.conf FAQ NEWS TODO
%doc README README.agent-mibs README.agentx README.krb5 README.snmpv3
%doc local/passtest local/ipf-mod.pl
%doc README.thread AGENT.txt PORTING local/README.mib2c
%{_initrddir}/snmpd
%{_initrddir}/snmptrapd
%config(noreplace,missingok) %{_sysconfdir}/sysconfig/snmpd
%config(noreplace,missingok) %{_sysconfdir}/sysconfig/snmptrapd
%dir %{_sysconfdir}/snmp
%config(noreplace,missingok) %attr(0600,root,root) %{_sysconfdir}/snmp/snmpd.conf
%config(noreplace,missingok) %attr(0600,root,root) %{_sysconfdir}/snmp/snmptrapd.conf
%{_bindir}/snmpconf
%{_bindir}/net-snmp-create-v3-user
%{_sbindir}/*
%attr(0644,root,root) %{_mandir}/man[58]/snmp*d*
%attr(0644,root,root) %{_mandir}/man5/snmp_config.5.gz
%attr(0644,root,root) %{_mandir}/man5/variables*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-create-v3-user*
%attr(0644,root,root) %{_mandir}/man1/snmpconf.1.gz
%dir %{_datadir}/snmp
%{_datadir}/snmp/snmpconf-data
%dir %{_localstatedir}/run/net-snmp

%files utils
%defattr(-,root,root,-)
%{_bindir}/encode_keychange
%{_bindir}/snmp[^c-]*
%attr(0644,root,root) %{_mandir}/man1/snmp[^-]*.1*
%attr(0644,root,root) %{_mandir}/man1/encode_keychange*.1*
%attr(0644,root,root) %{_mandir}/man5/snmp.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/variables.5.gz


%files devel
%defattr(0644,root,root,0755)
%{_libdir}/lib*.so
/usr/include/*
%attr(0644,root,root) %{_mandir}/man3/*.3.*
%attr(0755,root,root) %{_bindir}/net-snmp-config*
%attr(0644,root,root) %{_mandir}/man1/net-snmp-config*.1.*

%files perl
%defattr(-,root,root)
%{_bindir}/mib2c-update
%{_bindir}/mib2c
%dir %{_datadir}/snmp
%{_datadir}/snmp/mib2c*
%{_datadir}/snmp/*.pl
%{_bindir}/traptoemail
%attr(0644,root,root) %{_mandir}/man[15]/mib2c*
%attr(0644,root,root) %{_mandir}/man3/*.3pm.*
%attr(0644,root,root) %{_mandir}/man1/traptoemail*.1*
%{perl_vendorarch}/*SNMP*
%{perl_vendorarch}/auto/*SNMP*
# perl bridge-mib iplementation is no available in rawbuild
# (=without RHEL patches)
%{!?_rawbuild: %{_bindir}/snmp-bridge-mib}
%{!?_rawbuild: %attr(0644,root,root) %{_mandir}/man1/snmp-bridge-mib*.1*}

%files python
%defattr(-,root,root,-)
%doc python/README
%{python_sitearch}/*

%if %{netsnmp_enable_gui}
%files gui
%defattr(-,root,root)
%{_bindir}/tkmib
%attr(0644,root,root) %{_mandir}/man1/tkmib.1*
%endif

%files libs
%defattr(-,root,root)
%doc COPYING README ChangeLog.trimmed FAQ NEWS TODO
%{_libdir}/lib*.so.*
%dir %{_datadir}/snmp
%dir %{_datadir}/snmp/mibs
%{_datadir}/snmp/mibs/*
%dir %{_localstatedir}/lib/net-snmp

%changelog
* Tue Sep 29 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 1:5.5-57.el6_8.1.0
- Disabled net test since it will fail in mock/koji

* Wed Aug  3 2016 Josef Ridky <jridky@redhat.com> - 1:5.5-57.el6_8.1
- Resolves: #1363606 - An SNMPv3 request with a small max message size can lead to SNMPv1/2c bulk requests timing out

* Wed Jan 20 2016 Jan Safranek <jsafrane@redhat.com> - 1:5.5-57.el6
- Removed debug output in large FD_SET processing

* Tue Jan 19 2016 Jan Safranek <jsafrane@redhat.com> - 1:5.5-56.el6
- Fixed crash when processing large file descriptor (#1261727)

* Thu Nov 26 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-55.el6
- Fixed 'clientaddr' option for UDPv6 client messages (#1279501)
- Increased maximum size of AgentX packets (#1271196).
- Fixed IP-MIB::ipSystemStatsInOctets and similar counters for IPv4
  (#1250023).
- Fixed client utilities reporting 'read_config_store open failure on
  /var/lib/net-snmp/snmpapp.conf' (#1246568)
- Fixed typos in NET-SNMP-AGENT-MIB.txt (#1241865)
- Allow clients to use UDPv6 addresses without 'udp6:' prefix (#1227640)
- Restored message about duplicate IP address (#1227374)
- Fixed fd leak in sctp statistics (#1291054)

* Thu Jul 30 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-54.el6_7.1
- Fixed parsing of invalid variables in incoming packets (#1248410)

* Thu Apr 30 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-54
- Quicker loading of IP-MIB::ipAddrTable (#1191393)

* Fri Apr 24 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-53
- Quicker loading of IP-MIB::ipAddressTable (#1191393)

* Tue Apr  7 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-52
- Fixed snmptrapd crash when '-OQ' parameter is used and invalid trap is
  received (#CVE-2014-3565)

* Tue Jan 13 2015 Jan Safranek <jsafrane@redhat.com> - 1:5.5-51
- added faster caching into IP-MIB::ipNetToMediaTable (#789500)
- fixed compilation with "-Werror=format-security" (#1181994)
- added clear error message when port specified in 'clientaddrr' config
  option cannot be bound (#886468)
- fixed error check in IP-MIB::ipAddressTable (#1012430)
- fixed agentx client crash on failed response (#1023570)
- fixed dashes in net-snmp-config.h (#1034441)
- fixed crash on monitor trigger (#1050970)
- fixed 'netsnmp_assert 1 == new_val->high failed' message in system log
  (#1065210)
- fixed parsing of 64bit counters from SMUX subagents (#1069046)
- Fixed HOST-RESOURCES-MIB::hrProcessorTable on machines with >100 CPUs
  (#1070075)
- fixed net-snmp-create-v3-user to have the same content on 32 and 64bit
  installations (#1073544)
- fixed IPADDRESS value length in Python bindings (#1100099)
- fixed hrStorageTable to contain 31 bits integers (#1104293)
- fixed links to developer man pages (#1119567)
- fixed storageUseNFS functionality in hrStorageTable (#1125793)
- fixed netsnmp_set Python bindings call truncating at the first '\000'
  character (#1126914)
- fixed log level of SMUX messages (#1140234)
- use python/README to net-snmp-python subpackage (#1157373)
- fixed forwarding of traps with RequestID=0 in snmptrapd (#1146948)
- fixed typos in NET-SNMP-PASS-MIB and SMUX-MIB (#1162040)
- fixed close() overhead of extend commands (#1188295)
- fixed lmSensorsTable not reporting sensors with duplicate names (#967871)
- fixed hrDeviceTable with interfaces with large ifIndex (#1195547)

* Thu Mar  6 2014 Jan Safranek <jsafrane@redhat.com> - 1:5.5-50
- added 'diskio' option to snmpd.conf, it's possible to monitor only selected
  devices in diskIOTable (#990674)
- fixed CVE-2014-2284: denial of service flaw in Linux implementation of
  ICMP-MIB (#1073223)
- added cache to hrSWRunTable to provide consistent results (#1007634)
- skip 'mvfs' (ClearCase) when skipNFSInHostResources is enabled (#1073237)
- fixed snmptrapd crashing on forwarding SNMPv3 traps (#1131844)
- fixed HOST-RESOURCES-MIB::hrSystemProcesses (#1134335)

* Wed Sep 11 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-49
- fixed snmp daemons and utilities crashing in FIPS mode (#1001830)
- added support of btrfs filesystem in hrStorageTable (#1006706)

* Thu Aug 15 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-48
- fixed issues found by static analysis tools

* Tue Aug 13 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-47
- restored ABI of read_configs_* functions

* Tue Aug 13 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-46
- fixed parsing of bulk responses (#983116)
- added support of vzfs filesystem in hrStorageTable (#989498)
- fixed endless loop when parsing sendmail configuration file with
  queue groups (#991213)

* Wed Jun 26 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-45
- fixed potential memory leak on realloc failure when processing 'extend'
  option (#893119)
- added precise enumeration of configuration files searched to
  snmp_config(5) man page (#907571)
- set permissions of snmpd.conf and snmptrapd conf to 0600 (#919239)
- fixed kernel threads in hrSWRunTable (#919952)
- fixed various error codes in Python module (#955771)
- fixed snmpd crashing in the middle of agentx request processing when
  a subagent disconnects (#955511)
- allow 'includeFile' and 'includeDir' options in configuration files
  (#917816)
- fixed netlink message size (#927474)
- fixed IF-MIB::ifSpeedHi on systems with non-standard interface speeds
  (#947973)
- fixed BRIDGE-MIB::dot1dBasePortTable not to include the bridge itself
  as a port (#960568)
- fixed snmpd segfault when 'agentaddress' configuration options is used
  and too many SIGHUP signals are received (#968898)
- updated UCD-SNMP-MIB::dskTable to dynamically add/remove disks
  if 'includeAllDisks' is specified in snmpd.conf (#922691)

* Wed Jun  5 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-44.2
- fixed crash when parsing invalid SNMP packets (#953926)

* Tue Apr 16 2013 Jan Safranek <jsafrane@redhat.com> - 1:5.5-44.1
- fixed snmpd crashing with 'exec' command with no arguments in snmpd.conf
  (#919259)

* Wed Oct 10 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-44
- rebuild with fixed libnetsnmpmibs linking broken by perl-rpath patch

* Mon Sep 10 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-43
- fixed value of UCD-SNMP-MIB::extCommand to contain full command
  line (#842279)
- fixed rpath to perl.so (#848319)
- added support for port numbers in 'clientaddr' configuration
  option (#833013)
- fixed rare snmptrapd crash on SIGHTERM handling when embedded perl
  is used (#824402)
- fixed engineID of outgoing traps if 'trapsess -e <engineID>' is used in
  snmpd.conf (#800671)
- updated documentation of '-c' option of snmptrapd (#784502)
- fixed endless loop when SIGTEM arrives in middle of internal query
  processing (#851637)
- fixed UCD-DISKIO-MIB::diskIOLA values (#848155)
- removed various error log messages related to counte64 expansions
  (#846906)
- removed various error log messages when IPv6 is disabled (#845157)
- added support of cvfs filesystem in hrStorageTable (#846532)
- fixed rare race condintion when populating UCD-SNMP-MIB::prTable,
  which could result in some entries missing in the table (#846436)
- added support of simfs filesystem in hrStorageTable (#861152)
- fixed responding to requests on a multihost machine (#825889)

* Wed Jun 27 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-42
- removed fixed limit of 50 'exec' entries in snmpd.conf (#829271)

* Fri May 18 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-41
- moved /var/lib/net-snmp fro net-snmp to net-snmp-libs package
  (#822480)

* Wed May  9 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-40
- fixed CVE-2012-2141 (#820100)

* Tue Apr 10 2012 Jan Safranek <jsafrane@redhat.com> - 1:5.5-39
- fixed proxying of out-of-tree GETNEXT requests (#799291)

* Mon Nov 14 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-38
- fixed snmpd crashing with many AgentX subagent (#749227)
- fixed SNMPv2-MIB::sysObjectID value when "sysObjectID" config file
  option with long OID was used (#786931)
- fixed value of BRIDGE-MIB::dot1dBasePortIfIndex.1 (#740172)
- fixed parsing of "proxy" snmpd.conf option not to enable
  verbose logging by default (#746903)
- added new "realStorageUnits" config file option to support
  disks > 16 TB in hrStorageTable (#741789)
- added vxfs, reiserfs and ocfs2 filesystem support to hrStorageTable
  (#746903)
- fixed snmpd sigsegv when embedded perl script registers one handler
  twice (#748907)
- fixed setting of SNMP-TARGET-MIB::snmpTargetAddrRowStatus via
  SNMP-SET request on 64-bit platforms (#754275)
- fixed crash when /var/lib/net-snmp/mib_indexes/ files have wrong
  SELinux context (#754971)
- fixed memory leak when agentx subagent disconnects in the middle
  of request processing (#736580)
- fixed slow (re-)loads of TCP-MIB::tcpConnectionTable (#789909)
- removed 'error finding row index in _ifXTable_container_row_restore'
  error message (#788954)

* Mon Sep 12 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-37
- recompiled with relro in perl and python modules (#725657)

* Mon Sep  5 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-36
- fixed crash in AgentX when closing subagent session (#729738)

* Wed Aug 24 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-35
- fixed few QA complaints in bugs #681949, #708370 and #710667

* Mon Aug 15 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-34
- another rebuild with updated SMUX to ensure ABI compatibility of
  libsnmpagent.so

* Mon Aug 15 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-33
- rebuilt with updated SMUX to ensure ABI compatibility of libsnmpagent.so

* Fri Aug 12 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-32
- fixed varbind parsing in python netsnmp module (#711481)
- fixed session initialization in python netsnmp module (#710667)
- fixed crash when getting out-of-memory in inetNetToMediaTable (#708947)
- added xfs and jfs filesystem support to hrStorageTable (#707912)
- fixed snmpd to purge zombies resulted from pass_persist process exit
  (#703682)
- added a log message when snmpd detects two interfaces with the same
  IP address and thus having only one ipTable entry for both (#702171)
- added new snmpd.conf options 'interface_fadeout' and
  'interface_replace_old' to controll snmpd behavior when more
  interfaces get the same name (#702165)
- fixed snmptrapd leaking memory when processing traps in embedded perl
  (#678314)
- fixed hrSystemDate timezone sign (#683680)
- fixed snmp logging 'truncating integer value > 32 bits' for
  UCD-SNMP-MIB::systemStats (#681949)
- fixed rare race condition in hrSWRunTable (#683563)
- recompiled with relro for better security (#725657)
- snmpd should not change request-id when sending multiple SMUX messages
  (#708370)

* Thu Feb 17 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-31
- fixed BRIDGE-MIB implementation in /usr/bin/snmp-bridge-mib,
  now it supports embedded perl and answers GETNEXT requests correctly
  (#630157).

* Mon Feb 14 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-30
- fixed snmpd crashing on registration of smux peer (#672595)

* Fri Feb  4 2011 Jan Safranek <jsafrane@redhat.com> - 1:5.5-29
- fixed snmpd printing "looks like a 64bit wrap, but prev!=new" to syslog
  (#674757)

* Wed Dec  1 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-28
- fixed recompilation of the package on machine without IPv6 (#657835)
- fixed SMUX getting stuck on big-endian platforms (#665053)
- fixed OID comparsion in snmpwalk, now the output does not include
  objects outside requested subtree (#636890)
- fixed IPv4 address creation in ipAddressTable (#616764)
- added IPv6 address creation to ipAddressTable (#616336)
- fixed value of ipAddressPrefixAutonomousFlag OID (#625262)
- fixed ipv6IfTable - new interfaces were not added there (#627564)
- extended BRIDGE-MIB implementation to cover RFC 4363 (#630157)

* Thu Nov 11 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-27.1
- fixed truncation of sysObjectID (#641113)
- fixed assertions in calculating of statistics in IF-MIB (#621664)

* Wed Aug  4 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-27
- removed APSL 1.1 licensed files from source tarball (#619906)

* Wed Jul 28 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-26
- fixed gfs2 support in hrFSTable and hrStorageTable (#616496)

* Tue Jul 20 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-25
- fixed temporary filename generation in snmptrapd (#560081)

* Wed Jul 14 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-24
- further improved snmptranslate dysplaying ranges on 32-bit HW (#606874)

* Fri Jun 25 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-23
- fixed segfault when parsing snmpd.conf with disman entries (#607080)
- fixed value of IP-MIB::ipv6InterfaceForwarding (#607074)
- fixed output of snmptranslate tool when displaying ranges of UNSIGNED
  type (#606874)

* Thu Jun  3 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-22
- fixed value of ipIfStatsTable.Ip6ReasmReqds (#597265)
- added missing include files from util_funcs directory (#604636)

* Tue May 25 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-21
- fixed hrFSTable and hrStorageTable to provide persistent table indexes
  according to RFS 2790 (#595325)

* Fri May 14 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-20
- fixed a memory leak in TCP-MIB and LM-SENSORS-MIB (#591005)

* Fri Apr 23 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-19
- fixed exit code of snmp utilities when wrong argument to '-A' option
  is specified (#574061)
- fixed BER parsing of incoming packets - siletnly discard the invalid ones
  according to RFC (#568651)

* Wed Apr 14 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-18
- fixed the automated test suite running with udp6 and tcp6 transports
  (#581873)

* Tue Apr  6 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-17
- fixed snmpd running as different user using '-u' parameter (#578405)

* Wed Mar 31 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-16
- added Perl implementation of BRIDGE-MIB, see man snmp-bridge-mib
  (#532759)

* Thu Mar  4 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-15
- remove net-snmp-gui subpackage, perl-Tk is being removed from
  distro (#568786)
- fix IF-MIB::ifSpeed of inactive interfaces (#561884)
- correct the package license

* Fri Jan 29 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-14
- store temporary files in /var/run/net-snmp instead of /tmp (SELinux does
  not allow writing /tmp) (#560081)
- fix filedescriptor leak in RMON-MIB and Etherlike-MIB (#562108)

* Wed Jan 20 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-13
- fix minor typo in snmpnetstat man page (#556838)

* Thu Jan 14 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-12
- fix memory leak in RMON-MIB and ETHERLIKE-MIB when there are aliased interfaces
  (#555318)

* Wed Jan 13 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-11
- fix additional memory leak in ipAddressPrefixTable, related to #518633

* Tue Jan 12 2010 Stepan Kasal <skasal@redhat.com> - 1:5.5-10
- move the perl(:MODULE_COMPAT_5.10.x) require to net-snmp-libs

* Tue Jan 12 2010 Stepan Kasal <skasal@redhat.com> - 1:5.5-9
- require perl(:MODULE_COMPAT_5.10.x) because the package links against
  libperl.so

* Mon Jan 11 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-8
- rebuild with new rpm
- plug another leak as port from RHEL5

* Tue Jan  5 2010 Jan Safranek <jsafrane@redhat.com> - 1:5.5-7
- fix invalid access to memory in tcpListenerTable (#551030)
- fix crash with interfaces without broadcast addresses (like OpenVPN's tun0)
  (#549390)
- fix responding to broadcast SNMP requests (#549390)
- port patches from RHEL-5 to avoid regressions

* Tue Dec  8 2009 Jan Safranek <jsafrane@redhat.com> - 1:5.5-6
- fix compilation of the python module

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1:5.5-5
- rebuild against perl 5.10.1

* Wed Dec  2 2009 Jan Safranek <jsafrane@redhat.com> 1:5.5-4
- fix udpTable indexes on big-endian systems (#543352)
- fix snmptrapd init script to survive with empty /etc/sysconfig/snmptrapd
- lower the default log level of snmpd to get rid of the debug messages

* Wed Nov 25 2009 Jan Safranek <jsafrane@redhat.com>  1:5.5-3
- prepare the .spec file for review
- run automatic regression suite after the compilation of the package
  to check for obvious regressions
- remove unnecessary package dependencies

* Tue Nov 24 2009 Jan Safranek <jsafrane@redhat.com>  1:5.5-2
- introduce /etc/sysconfig/snmptrapd. Use it to specify snmptrapd command
  line options.  /etc/snmp/snmptrapd.options is not used anymore (#540799)
- build-in ipAddressPrefixTable, ipDefaultRouterTable, ipv6ScopeZoneIndexTable,
  ipIfStatsTable, SCTP-MIB, RMON-MIB and Etherlike-MIBs
- remove ucd5820stat helper script, it depends on get5820stats, which is not
  available in Fedora
- move sample services ipf-mod.pl to documentation
- remove logrotate config, snmpd logs into syslog

* Tue Sep 29 2009 Jan Safranek Jan Safranek <jsafranek@redhat.com> 5.5-1
- update to Net-SNMP 5.5
- remove static libraries from -devel subpackage

* Mon Sep 14 2009 Jan Safranek <orion@cora.nwra.com> 1:5.4.2.1-17
- implement force-reload command in initscripts (#523126)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1:5.4.2.1-16
- rebuilt with new openssl

* Fri Aug 14 2009 Orion Poplawski <orion@cora.nwra.com> 1:5.4.2.1-15
- Prevent post script failure on fresh installs

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.4.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-13
- package cleanup, remove unnecessary patches
- move local state file from /var/net-snmp/ to /var/lib/net-snmp

* Wed Jul  1 2009 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-12
- make the default configuration less noisy, i.e. do not print "Connection from
  UDP:" and "Received SNMP packet(s) from UDP:" messages on each connection.
  (#509055)

* Mon May 18 2009 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-11
- fix divison-by-zero in cpu statistics (#501210)

* Fri Mar 06 2009 Jesse Keating <jkeating@redhat.com> - 5.4.2.1-10
- Rebuild for new rpm

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.4.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-8
- fix tcp_wrappers integration (CVE-2008-6123)

* Fri Jan 30 2009 Karsten Hopp <karsten@redhat.com> 5.4.2.1-7
- fix build on s390x which has no libsensors

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 5.4.2.1-7
- rebuild with new openssl

* Wed Dec 17 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-6
- rebuilt for new python again...

* Mon Dec  1 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-5
- fix rpm ownership of all created directories (#473582)

* Mon Dec  1 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-4
- Rebuild for fixed rpm (#473420)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:5.4.2.1-3
- Rebuild for Python 2.6

* Mon Nov  3 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2.1-1
- explicitly require the right version and release of net-snmp and
  net-snmp-libs
- update to net-snmp-5.4.2.1 to fix CVE-2008-4309

* Fri Sep 26 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2-3
- further tune up the distribution of files among subpackages
  and dependencies

* Fri Sep 26 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2-2
- redistribute the perl scripts to the net-snmp package,
  net-snmp-utils doesn't depend on perl now (#462484)

* Wed Sep 17 2008 Jan Safranek <jsafranek@redhat.com> 5.4.2-1
- update to net-snmp-5.4.2

* Wed Sep 10 2008 John A. Khvatov <ivaxer@fedoraproject.org> 5.4.1-22
- add net-snmp-python

* Tue Jul 22 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-21
- fix perl SNMP::Session::set (#452131)

* Fri Jul 11 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-20
- prepare for new rpm version

* Tue Jun 10 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-19
- fix various flaws (CVE-2008-2292 CVE-2008-0960)

* Sat May 31 2008 Dennis Gilmore <dennis@ausil.us> 5.4.1-18
- fix sparc handling in /usr/bin/net-snmp-config

* Thu May 29 2008 Dennis Gilmore <dennis@ausil.us> 5.4.1-17
- fix sparc handling in /usr/include/net-snmp/net-snmp-config-sparc.h

* Sun May 25 2008 Dennis Gilmore <dennis@ausil.us> 5.4.1-16
-sparc multilib handling

* Mon Apr 21 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-15
- explicitly require lm_sensor > 3 for build (#442718)
- create multilib net-snmp-config on multilib architectures only

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.4.1-14
- add Requires for versioned perl (libperl.so)
- get rid of silly file Requires

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.4.1-13
- BR: perl(ExtUtils::Embed)

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.4.1-12
- rebuild for new perl

* Thu Feb 21 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-11
- add openssl-devel to the list of netsnmp-devel deps

* Thu Feb 14 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-10
- fixing ipNetToMediaNetAddress to show IP address (#432780)

* Tue Feb 12 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-9
- introduce /etc/sysconfig/snmpd. Use it to specify snmpd command line options.
  /etc/snmp/snmpd.options is not used anymore (#431391)

* Mon Jan 28 2008 Jan Safranek <jsafranek@redhat.com> 5.4.1-8
- init scripts made LSB compliant

* Wed Dec  5 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-7
- rebuild for openssl soname bump

* Wed Nov 14 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-6
- add support of lm_sensors v3
- added procps to build dependencies (#380321)
- removed beecrypt from dependencies
- fixed crash on reading xen interfaces (#386611)

* Thu Oct 25 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-5
- move mib2c-update from net-snmp-utils to net-snmp-perl, where
  mib2c is located
- add tkmib to net-snmp-gui package (#167933)

* Tue Oct 16 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-4
- License: field fixed to "BSD and CMU"

* Thu Aug 23 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-3
- include these tables: ip-mib/ipv4InterfaceTable
  ip-mib/ipv6InterfaceTable, ip-mib/ipAddressPrefixTable
- fix Requires of net-snmp-devel to include lmsensors-devel on supported
  architectures

* Wed Aug 22 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-2
- gawk added to build dependencies

* Tue Aug  7 2007 Jan Safranek <jsafranek@redhat.com> 5.4.1-1
- License: field changed to MIT
- 5.4.1 integrated

* Tue Jul 31 2007 Jan Safranek <jsafranek@redhat.com> 5.4-16
- supported lm_sensors on ppc64 (#249255)
- snmpconf generates config files with proper selinux context
  (#247462)
- fix leak  in udp transport (#247771)
- add alpha to supported archs in net-snmp-config (#246825)
- fix hrSWInst (#250237)

* Thu Jun 28 2007 Jan Safranek <jsafranek@redhat.com> 5.4-15
- fix default snmptrapd.conf

* Thu May  3 2007 Jan Safranek <jsafranek@redhat.com> 5.4-14
- fix snmptrapd hostname logging (#238587)
- fix udpEndpointProcess remote IP address (#236551)
- fix -M option of net-snmp-utils (#244784)
- default snmptrapd.conf added (#243536)
- fix crash when multiple exec statements have the same name
  (#243536)
- fix ugly error message when more interfaces share
  one IP address (#209861)

* Mon Mar 12 2007 Radek Vokál <rvokal@redhat.com> - 1:5.4-13
- fix overly verbose log message (#221911)
- few minor tweaks for review - still not perfect
- fix linking with lcrypto (#231805)

* Fri Mar  9 2007 Radek Vokál <rvokal@redhat.com> - 5.4-12
- lm_sensors-devel only where avaliable

* Thu Mar  1 2007 Radek Vokál <rvokal@redhat.com> - 5.4-11
- fix lm_sensors-devel Requires (#229109)

* Mon Feb 26 2007 Vitezslav Crhonek <vcrhonek@redhat.com> - 5.4-10
- fix net-snmp-config strange values for --libs (#228588)

* Fri Feb 23 2007 Radek Vokál <rvokal@redhat.com> - 5.4-9
- fix dependency on lm_sensors-devel (#229109)
- spec file cleanups

* Tue Jan 23 2007 Radek Vokál <rvokal@redhat.com> - 5.4-8
- fix occasional segfaults when snmpd starts

* Thu Jan 11 2007 Radek Vokál <rvokal@redhat.com> - 5.4-7
- fix ethtool extension (#222268)

* Thu Jan 11 2007 Radek Vokál <rvokal@redhat.com> - 5.4-6
- swith to new disman implementation

* Tue Dec 12 2006 Radek Vokál <rvokal@redhat.com> - 5.4-5
- fix memleaks in ip-addr and tcpConn

* Thu Dec  7 2006 Radek Vokál <rvokal@redhat.com> - 5.4-4
- fix rtnetlink.h/if_addr.h 

* Thu Dec  7 2006 Joe Orton <jorton@redhat.com> - 5.4-3
- add Requires for tcp_wrappers-devel for -devel

* Mon Dec  4 2006 Radek Vokál <rvokal@redhat.com> - 5.4-2
- rebuilt against tcp_wrappers-devel

* Mon Nov 27 2006 Radek Vokal <rvokal@redhat.com> - 5.4-1
- upgrade to 5.4
- patch cleanup
- snmpd uses /var/run/snmpd.pid (#211264)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 5.3.1-11
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Radek Vokal <rvokal@redhat.com> 5.3.1-10
- add mibII/mta_sendmail (#207909)

* Fri Sep 22 2006 Radek Vokal <rvokal@redhat.com> 5.3.1-9
- fix deprecated syscall base_reachable_time (#207273)

* Wed Sep 13 2006 Radek Vokal <rvokal@redhat.com> 5.3.1-8
- enable smux to listen only on LOCAL by default (#181667)
- use correct answer adrress 

* Tue Sep  5 2006 Radek Vokal <rvokal@redhat.com> 5.3.1-7
- better upstream patch for byteorder
- add epoch to corespond with upstream versioning 

* Wed Aug 30 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-6
- fix IPv4/IPv6 address presentation (#200255)

* Wed Aug 23 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-5
- SMUX support is still needed .. will disappear later!
- static libs should be in devel not libs (#203571)
- fix lm_sensors issues

* Tue Aug 22 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-4
- turn off SMUX support (#110931)
- add dist tag

* Thu Aug 10 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-3
- fix lib dirs in configure (#197684)

* Thu Aug  3 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-2
- better patch for depreciated sysctl call

* Mon Jul 17 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.0-1
- update to 5.3.1 final version, fix version number

* Wed Jul 12 2006 Radek Vokál <rvokal@redhat.com> 5.3.1.rc4-2
- fix init script, read .options files from /etc/snmp (#195702)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.3.1.rc4-1.1
- rebuild

* Mon Jul 10 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.rc4-1
- update to release candidate 4
- fix lib dependencies on 64bit archs
- supress perl build

* Tue Jun 13 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre3-2
- add tcp-mib (#194856)

* Fri Jun  2 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre3-1
- update to another prerelease (fixes perl agents)

* Fri May 26 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre2-4
- fix lib version 

* Thu May 25 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre2-3
- another multilib fix. Fix also net-snmp-config script

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre2-2
- another attempt to fix multilib issue. Generate dummy net-snmp-config.h file

* Tue May 23 2006 Radek Vokal <rvokal@redhat.com> 5.3.1.pre2-1
- update to 5.3.1.pre2
- fix multilib issues (#192736)
  On system with /usr/lib64 use net-snmp-config64 and net-snmp-config64.h

* Sat Apr 15 2006 Radek Vokál <rvokal@redhat.com> 5.3-8
- fix missing IF-MIB::ifNumber.0 (#189007)

* Wed Apr 05 2006 Radek Vokál <rvokal@redhat.com> 5.3-7
- fix parsing of /proc/diskstats
- fix disman monitor crash
- fix perl vendor name
- fix OID lookup fail

* Sat Mar 25 2006 Radek Vokal <rvokal@redhat.com> 5.3-6
- use net.ipv6.neigh.lo.retrans_time_ms (#186546)

* Mon Mar 20 2006 Radek Vokal <rvokal@redhat.com> 5.3-5
- allow disman/event-mib

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.3-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.3-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb  2 2006 Radek Vokál <rvokal@redhat.com> 5.3-4
- fix crash on s390x and ppc64

* Mon Jan 30 2006 Radek Vokál <rvokal@redhat.com> 5.3-3
- fix for lm_Senors, the max is no longer a fixed value
- parsing fixed for /proc/net/if_inet6

* Wed Jan 18 2006 Radek Vokal <rvokal@redhat.com> 5.3-2
-  Security fix. Bug granting write access to read-only users 
   or communities which were configured  using the "rocommunity" 
   or "rouser" snmpd.conf tokens fixed

* Fri Dec 30 2005 Radek Vokal <rvokal@redhat.com>
- upgrade to 5.3 

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 16 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-4
- check for header files in configure
- patch for SNMPv3 traps / session user creation (net-snmp bz#1374087)

* Fri Dec 09 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-3
- fix ipaddr return type on 64bit machines 

* Wed Dec 07 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-2
- fix read problem on stream sockets (net-snmp bz#1337534)

* Tue Nov 29 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-1
- upgrade to 5.2.2 final

* Mon Nov 21 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-0.rc6.1
- update to rc6, snmpnetstat changes due to license problems
- persistent files in directory defined by snmp.conf persistentDir are 
  loaded at startup

* Tue Nov 15 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-0.rc5.1
- another release candidate 

* Tue Nov 08 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-0.rc4.2
- Remove .la file from net-snmp-libs (#172618)
- grab new openssl

* Mon Nov 07 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-0.rc4.1
- update to release candidate 4

* Tue Nov 01 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2-0.rc3.1
- release candidate 3 of net-snmp-5.2.2

* Tue Oct 25 2005 Radek Vokal <rvokal@redhat.com> - 5.2.2.rc2-1
- rc2 prebuilt

* Tue Sep 20 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1.2-3
- fix endian issues for addresses

* Fri Aug 12 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1.2-2
- fix for s390x counter32 overflow (sachinp@in.ibm.com)

* Wed Jul 13 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1.2-1
- CAN-2005-2177 new upstream version fixing DoS (#162908)

* Tue May 31 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-13
- CAN-2005-1740 net-snmp insecure temporary file usage (#158770)
- patch from suse.de

* Wed May 18 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-12
- session free fixed, agentx modules build fine (#157851)
- fixed dependency for net-snmp libs (#156932)

* Wed May 04 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-11
- report gigabit Ethernet speeds using Ethtool (#152480)

* Tue Apr 19 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-10
- fixed missing requires for devel package (#155221)

* Wed Apr 06 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-9
- switching to a different 64bit patch, hopefully 64bit problems are gone for a while

* Mon Apr 04 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-8
- net-snmp properly deals with large partitions (#153101) <jryska@redhat.com>

* Thu Mar 31 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-7
- agentx double free error fix <jp.fujitsu>

* Thu Mar 24 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-6
- fixed unexpected length for type ASN_UNSIGNED (#151892)
- fixed uptime problems on ia64

* Wed Mar 09 2005 Radek Vokal <rvokal@redhat.com> - 5.2.1-5
- 64bit needed some changes, was causing timeouts on 64bit archs!? 
- affects bugs #125432 and #132058

* Tue Mar  1 2005 Tomas Mraz <tmraz@redhat.com> - 5.2.1-4
- rebuild with openssl-0.9.7e

* Wed Feb 23 2005 Radek Vokal <rvokal@redhat.com> - 5.1.2-3
- patch from CVS - kill extra carriage return (#144917)
- removed patch for interface indexing - doesn't show virtual interfaces

* Tue Feb  8 2005 Jeremy Katz <katzj@redhat.com> - 5.2.1-2
- rebuild for new librpm

* Mon Jan 31 2005 Radek Vokal <rvokal@redhat.com> 5.2.1-1
- new release, fixing several issues
- pointer needs to be inicialized (#146417)

* Mon Dec 27 2004 Radek Vokal <rvokal@redhat.com> 5.2-2
- patch adding ipv6 support to ip system stats

* Tue Nov 30 2004 Radek Vokal <rvokal@redhat.com> 5.2-1
- net-snmp-5.2, patch clean-up

* Mon Nov 15 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-12
- snmpd crash with 'interfaces' directives in snmpd.conf fixed #139010
- rather dirty patch fixing conf directory for net-snmp-config

* Fri Oct 15 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-11
- Logrotate support added (#125004)

* Thu Oct 14 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-10
- Extended the libwrap and bsdcompat patches

* Mon Oct 11 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-9
- Droped obsolete lm-sensors patch and enabled lmSensors module
- Marked several patches to be removed for 5.1.3

* Wed Sep 29 2004 Warren Togami <wtogami@redhat.com> 5.1.2-8
- remove README* that do not apply to Linux
- trim massive ChangeLog

* Wed Sep 22 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- move ldconfig post/postun to libs subrpm

* Wed Sep 15 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-6
- Split out libs package for multilib compatibility

* Wed Sep 08 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-4
- New prereq for net-snmp-devel
- lelf check removed from configure.in (#128748)
- fixed snmpd coredump when sent SIGHUP (#127314)

* Tue Sep 07 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-3
- Agentx failed to send trap, fixed (#130752, #122338)

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-2
- Patch fixing uninitalized stack variable in smux_trap_process (#130179)

* Wed Aug 18 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-1
- Update to 5.1.2
- Removed net-snmp-5.0.1-initializer patch, included upstream

* Tue Jun 15 2004 Phil Knirsch <pknirsch@redhat.com>
- Fixed small bug in snmptrapd initscript (#126000).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-3
- Reworked the perl filelist stuff (Thanks to marius feraru).

* Thu Apr 08 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-2
- Added Kaj J. Niemi that fixes ipAdEntIfIndex problem (#119106)
- Added Kaj J. Niemi to shut up memshared message for 2.6 kernel (#119203)

* Tue Mar 23 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-1
- Update to latest upstream version 5.1.1
- Included updated patches from Kaj J. Niemi (#118580).

* Thu Mar 18 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-12
- Hacked an ugly perl hack to get rid of perl RPATH problems.
- Fixed 64bit patch and applied it. ;-)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-10
- Included 64bit fix from Mark Langsdorf (#114645).

* Tue Feb 03 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-9
- Reverted removal of _includir redefiniton due to php-snmp dependancy.
- Remove SO_BSDCOMPAT setsockopt() call, deprecated.

* Thu Jan 29 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-8
- Quite a bit of specfile cleanup from Marius FERARU.

* Thu Jan 22 2004 Thomas Woerner <twoerner@redhat.com> 5.1-7
- enabled pie (snmpd, snmptrapd) - postponed for ia64
- added --with-pic to configure call

* Thu Jan 15 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-6
- Fixed 64bit build problems when 32bit popt lib is installed.

* Tue Jan 13 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-5
- rebuilt

* Sun Jan 11 2004 Florian La Roche <Florian.LaRoche@redhat.de> 5.1-4
- rebuild for new rpm

* Wed Dec 10 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-3
- Removed snmpcheck again, needs perl(Tk) which we don't ship (#111194).
- Fixed getopt definition in include file (#111209).
- Included Kaj J. Niemi's patch for broken perl module (#111319).
- Included Kaj J. Niemi's patch for broken async getnext perl call (#111479).
- Included Kaj J. Niemi's patch for broken hr_storage (#111502).

* Wed Nov 26 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-2
- Included BuildPrereq on lm_sensors-devel on x86 archs (#110616).
- Fixed deprecated initscript options (#110618).

* Wed Nov 19 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-1
- Updated to latest net-snmp-5.1 upstream version.
- Tons of specfile and patch cleanup.
- Cleaned up perl stuff (mib2c etc, see #107707).
- Added lm_sensors support patch for x86 archs from Kaj J. Niemi (#107618).
- Added support for custom mib paths and mibs to snmptrapd initscript (#102762)

* Mon Oct 13 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.9-2
- Due to rpm-devel we need elfutils-devel, too (#103982).

* Mon Sep 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.9-1
- Updated to latest upstream version net-snmp-5.0.9
- Added patch to fix net-snmp-perl problems (#105842).

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without tcp_wrappers

* Wed Sep 17 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-11.1
- rebuilt

* Wed Sep 17 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-11
- Fixed permission for net-snmp-config in net-snmp-devel

* Mon Sep 08 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-10.1
- rebuilt

* Mon Sep 08 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-10
- Moved net-snmp-config into devel package (#103927)

* Fri Aug 22 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-9.1
- rebuilt

* Thu Aug 21 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-9
- Added sample config to make net-snmp RFC 1213 compliant.

* Fri Aug 15 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-8
- Fixed problem with perl option (#102420).
- Added patch for libwrap fix (#77926).

* Tue Aug 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-7.1
- rebuilt

* Tue Aug 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-7
- Fixed build problems on ppc64
- Fixed double packaged manpages (#102075).

* Thu Aug 07 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed problem with new proc output (#98619, #89960).

* Wed Aug 06 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed ro/rw problem with v2 and v3 request (#89612)

* Tue Aug 05 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed permission problem for debuginfo (#101456)

* Thu Jul 31 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-6.1
- Fixed file list for latest build.

* Thu Jul 31 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-6
- Fixed build problems for net-snmp-perl.

* Sun Jul 27 2003 Florian La Roche <Florian.LaRoche@redhat.de> 5.0.8-5
- actually apply ipv6 patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-3
- bumped release and rebuilt.

* Tue Apr 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-2
- Hack to make it build on 64bit platforms with /usr/lib64 correctly.
- Fixed bug #85071 (leak of open descriptors for ipv6).

* Fri Mar 28 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-1
- Updated to latest upstream version 5.0.8 (bug #88580)

* Thu Feb 13 2003 Phil Knirsch <pknirsch@redhat.com>
- Included generation of perl stuff. Thanks to Harald Hoyer.

* Wed Feb 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.7-1
- Updated to net-snmp-5.0.7. Fixed especially the performance problem with
  limited trees.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-17
- Fixed ucd-snmp.redhat.conf (#78391).
- Fixed snmpwalk examples in config file.

* Mon Feb 10 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-15
- Fixed invalid SMUX packet (#83487).

* Thu Feb 06 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-14
- Fixed the libdir problem.

* Wed Feb 05 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-13
- Updated the old libtool rpath patch.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 5.0.6-12
- rebuilt

* Tue Jan 14 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-11
- Updated nolibelf patch and activated it again.

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 5.0.6-10
- Rebuild

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-9
- Added bzip2-devel to BuildPreReq (#76086, #70199).

* Thu Nov 28 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-8
- Added patch to increase SMUXMAXSTRLEN. 

* Thu Nov  7 2002 Tim Powers <timp@redhat.com> 5.0.6-6
- rebuilt to fix broken deps
- remove files from the buildroot that we don't want to ship

* Thu Nov  7 2002 Joe Orton <jorton@redhat.com> 5.0.6-5
- add fix for -DUCD_COMPATIBLE (#77405)

* Thu Nov 07 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-4
- Another bump required. Some more specfile changes.

* Wed Nov 06 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-3
- Bumped release and rebuilt.
- Removed all dbFOO cruft again.

* Wed Oct 09 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-2
- Updated to latest released version.

* Sat Aug 31 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not link against -lelf

* Thu Jun 27 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.1-5
- Added --enable-ucd-snmp-compatibility for compatibility with older version
  and fixed installation thereof.
- Got rid of the perl(Tk) dependancy by removing snmpcheck.
- Include /usr/include/ucd-snmp in the filelist.
- Fixed a problem with the ucd-snmp/version.h file.

* Wed Jun 26 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.1-1
- Updated to 5.0.1
- Dropped --enable-reentrant as it's currently broken

* Tue Apr 23 2002 Phil Knirsch <pknirsch@redhat.com> 5.0-1
- Switch to latest stable version, 5.0
- Renamed the packate to net-snmp and obsoleted ucd-snmp.

* Wed Apr 17 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4-3
- Fixed problem with reload in initscript (#63526).

* Mon Apr 15 2002 Tim Powers <timp@redhat.com> 4.2.4-2
- rebuilt in new environment

* Mon Apr 15 2002 Tim Powers <timp@redhat.com> 4.2.4-1
- update to 4.2.4 final

* Sat Apr 13 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-5
- Added some missing files to the %%files section.

* Tue Apr 09 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-4
- Hardcoded the ETC_MNTTAB to point to "/etc/mtab".

* Mon Apr 08 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-3
- Removed the check for dbFOO as we don't want to add another requirement.

* Fri Apr 05 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-2
- Added missing BuildPrereq to openssl-devel (#61525)

* Thu Apr 04 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-1
- Added ucd5820stat to the files section.
- Updated to latest version (4.2.4.pre3)

* Mon Mar 18 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre2-1
- Updated to latest version (4.2.4.pre2)

* Tue Jan 29 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.3-4
- Added the snmptrapd init script as per request (#49205)
- Fixed the again broken rpm query stuff (#57444)
- Removed all old and none-used db related stuff (libs and header checks/files)

* Mon Jan 07 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.3-2
- Included the Axioma Security Research fix for snmpnetstat from bugtraq.

* Mon Dec 03 2001 Phil Knirsch <phil@redhat.de> 4.2.3-1
- Update to 4.2.3 final.
- Fixed libtool/rpath buildroot pollution problem.
- Fixed library naming problem.

* Fri Oct  5 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed a server segfault for snmpset operation (#53640). Thanks to Josh Giles
  and Wes Hardaker for the patch.

* Mon Sep 10 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed problem with RUNTESTS script.

* Tue Sep  4 2001 Preston Brown <pbrown@redhat.com>
- fixed patch related to bug #35016 (Dell)

* Fri Aug 24 2001 Philipp Knirsch <pknirsch@redhat.de> 4.2.1-6
- Fixed snmpd description (#52366)

* Wed Aug 22 2001 Philipp Knirsch <pknirsch@redhat.de>
- Final bcm5820 fix. Last one was broken.
- Fixed bugzilla bug (#51960) where the binaries contained rpath references.

* Wed Aug 15 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed a couple of security issues:
  o /tmp race and setgroups() privilege problem
  o Various buffer overflow and format string issues.
  o One signedness problem in ASN handling.
- Fixed an important RFE to support bcm5820 cards. (#51125)

* Fri Jul 20 2001 Philipp Knirsch <pknirsch@redhat.de>
- Removed tkmib from the package once again as we don't ship the Tk.pm CPAN
  perl module required to run it (#49363)
- Added missing Provides for the .so.0 libraries as rpm doesn't seem to find
  those during the build anymore (it used to) (#46388)

* Thu Jul 19 2001 Philipp Knirsch <pknirsch@redhat.de>
- Enabled IPv6 support (RFE #47764)
- Hopefully final fix of snmpwalk problem (#42153). Thanks to Douglas Warzecha
  for the patch and Matt Domsch for reporting the problem.

* Tue Jun 26 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed smux compilation problems (#41452)
- Fixed wrong paths displayed in manpages (#43053)

* Mon Jun 25 2001 Philipp Knirsch <pknirsch@redhat.de>
- Updated to 4.2.1. Removed 2 obsolete patches (fromcvs and #18153)
- Include /usr/share/snmp/snmpconf in %%files

* Wed Jun 13 2001 Than Ngo <than@redhat.com>
- fix to use libwrap in distro
- add buildprereq: tcp_wrappers

* Fri Jun  1 2001 Bill Nottingham <notting@redhat.com>
- add a *new* patch for IP address return sizes

* Fri Apr 20 2001 Bill Nottingham <notting@redhat.com>
- add patch so that only four bytes are returned for IP addresses on ia64 (#32244)

* Wed Apr 11 2001 Bill Nottingham <notting@redhat.com>
- rebuild (missing alpha packages)

* Fri Apr  6 2001 Matt Wilson <msw@redhat.com>
- added ucd-snmp-4.2-null.patch to correcly handle a NULL value (#35016)

* Tue Apr  3 2001 Preston Brown <pbrown@redhat.com>
- clean up deinstallation (#34168)

* Tue Mar 27 2001 Matt Wilson <msw@redhat.com>
- return a usable RETVAL when running "service snmpd status" (#33571)

* Tue Mar 13 2001 Matt Wilson <msw@redhat.com>
- configure with --enable-reentrant and added "smux" and "agentx" to
  --with-mib-modules= argument (#29626)

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Mon Feb 26 2001 Tim Powers <timp@redhat.com>
- fixed initscript, for reload and restart it was start then stop,
  fixed. (#28477)

* Fri Feb  2 2001 Trond Eivind Glomsrod <teg@redhat.com>
- i18nize initscript

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- don't depend on /etc/init.d so that package will work with 6.2.
- perl path fiddles no longer needed.
- rely on brp-compress frpm rpm to compress man pages.
- patch from ucd-snmp CVS (Wes Hardaker).
- configure.in needs to check for rpm libraries correctly (#23033).
- add simple logrotate script (#21399).
- add options to create pidfile and log with syslog with addresses (#23476).

* Sat Dec 30 2000 Jeff Johnson <jbj@redhat.com>
- package for Red Hat 7.1.

* Thu Dec 07 2000 Wes Hardaker <hardaker@users.sourceforge.net>
- update for 4.2

* Thu Oct 12 2000 Jeff Johnson <jbj@redhat.com>
- add explicit format for syslog call (#18153).

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild per Trond's request.

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error that crept in with condrestart

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript and add condrestart magic

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- fix %%attr on man pages

* Mon Jun 12 2000 Jeff Johnson <jbj@redhat.com>
- tkmib doco had #!/usr/bin/perl55
- include snmpcheck and tkmib again (still needs some CPAN module, however).

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- update to 4.1.2.
- FHS packaging.
- patch for rpm 4.0.

* Thu May 18 2000 Trond Eivind Glomsrod <teg@redhat.com>
- add version to buildroot
- rebuilt with new libraries

* Sun Feb 27 2000 Jeff Johnson <jbj@redhat.com>
- default config was broken (from Wes Hardaker) (#9752)

* Sun Feb 13 2000 Jeff Johnson <jbj@redhat.com>
- compressed man pages.

* Fri Feb 11 2000 Wes Hardaker <wjhardaker@ucdavis.edu>
- update to 4.1.1

* Sat Feb  5 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change %%postun to %%preun

* Thu Feb 3 2000 Elliot Lee <sopwith@redhat.com>
- Don't ship tkmib, since we don't ship the perl modules needed to run it.
(Bug #4881)

* Tue Aug 31 1999 Jeff Johnson <jbj@redhat.com>
- default config permits RO access to system group only (Wed Hardaker).

* Sun Aug 29 1999 Jeff Johnson <jbj@redhat.com>
- implement suggestions from Wes Hardaker.

* Fri Aug 27 1999 Jeff Johnson <jbj@redhat.com>
- stateless access to rpm database.

* Wed Aug 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.0.1.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.6.2 (#3219,#3259).
- add missing man pages (#3057).

* Thu Apr  8 1999 Wes Hardaker <wjhardaker@ucdavis.edu>
- fix Source0 location.
- fix the snmpd.conf file to use real community names.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.6.1, fix configuration file stuff.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- restore host resources mib
- simplified config file
- rebuild for 6.0.

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- remove backup file to fix perl dependencies

* Tue Dec  8 1998 Jeff Johnson <jbj@redhat.com>
- add all relevant rpm scalars to host resources mib.

* Sun Dec  6 1998 Jeff Johnson <jbj@redhat.com>
- enable libwrap (#253)
- enable host module (rpm queries over SNMP!).

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.3.
- don't include snmpcheck until perl-SNMP is packaged.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- ucd-snmpd.init: start daemon w/o -f.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- don't start snmpd unless requested
- start snmpd after pcmcia.

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- all but config (especially SNMPv2p) ready for prime time

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.

* Tue Dec 30 1997 Otto Hammersmith <otto@redhat.com>
- created the package... possibly replace cmu-snmp with this.
