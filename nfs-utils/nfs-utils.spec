Summary: NFS utilities and supporting clients and daemons for the kernel NFS server
Name: nfs-utils
URL: http://sourceforge.net/projects/nfs
Version: 1.2.3
Release: 70%{?dist}.2
Epoch: 1

Source0: http://www.kernel.org/pub/linux/utils/nfs/%{name}-%{version}.tar.bz2

Source10: nfs.init
Source11: nfslock.init
Source12: rpcidmapd.init
Source13: rpcgssd.init
Source14: rpcsvcgssd.init
Source15: nfs.sysconfig
Source16: id_resolver.conf
Source17: nfs_cache_getent.sh

#
# RHEL6.1
#
Patch001: nfs-utils-1.2.4-rc5.patch
Patch002: nfs-utils-1.2.3-krb5-ad-style.patch
Patch003: nfs-utils-1.2.3-rpcsvcgssd-segfault.patch
#
# RHEL6.2
#
Patch004: nfs-utils-1.2.3-svcgssd-manpage.patch
Patch005: nfs-utils-1.2.3-mountnfs-cve20111749.patch
Patch006: nfs-utils-1.2.3-exportfsman-ipv6-update.patch
Patch007: nfs-utils-1.2.3-mountd-segfault.patch
Patch008: nfs-utils-1.2.3-exportfs-reliable.patch
Patch009: nfs-utils-1.2.3-umount-spaces.patch
Patch010: nfs-utils-1.2.3-umount-ipv6.patch
Patch011: nfs-utils-1.2.3-double-export.patch
Patch012: nfs-utils-1.2.3-mount-newmessage.patch
Patch013: nfs-utils-1.2.3-mount-versfails.patch
Patch014: nfs-utils-1.2.3-mount-filesize.patch
Patch015: nfs-utils-1.2.3-mount-ipv6-norollback.patch
Patch016: nfs-utils-1.2.3-rpcdebug-pnfs-debug.patch
#
# RHEL6.3
#
Patch017: nfs-utils-1.2.3-nfsidmap-keyring.patch
Patch018: nfs-utils-1.2.3-nfsman-tcp-timout.patch
Patch019: nfs-utils-1.2.3-idmapd-sigio.patch
Patch020: nfs-utils-1.2.3-link-libtirpc.patch
Patch021: nfs-utils-1.2.3-procfs-stdio-size.patch
Patch022: nfs-utils-1.2.3-gssd-creds.patch
Patch023: nfs-utils-1.2.3-mount-background.patch
Patch024: nfs-utils-1.2.3-umount-norm-paths.patch
Patch025: nfs-utils-1.2.3-nfsmount-parse-error.patch
Patch026: nfs-utils-1.2.3-idmap-umlauts-support.patch
Patch027: nfs-utils-1.2.3-exportfs-serial.patch
Patch028: nfs-utils-1.2.3-idmapd-octal-encoded.patch
Patch029: nfs-utils-1.2.3-mount-bg-v23.patch
Patch030: nfs-utils-1.2.3-umount-symlink.patch
Patch031: nfs-utils-1.2.3-mountd-vroots-rootsquash.patch
#
# RHEL6.4
#
Patch032: nfs-utils-1.2.3-nfsidmap-verbose.patch
Patch033: nfs-utils-1.2.3-mount.nfs-ipv6.patch
Patch034: nfs-utils-1.2.3-mount-netgrp-hang.patch
Patch035: nfs-utils-1.2.3-umount-ipv6-mtab.patch
Patch036: nfs-utils-1.2.3-mountd-use_ipaddr.patch
Patch037: nfs-utils-1.2.5-gssd-nolibgssapi-krb5.patch
Patch038: nfs-utils-1.2.3-fsloc-ipv6.patch
Patch039: nfs-utils-1.2.3-gssd-legacy-enctypes.patch
Patch040: nfs-utils-1.2.3-svcgssd-limit-enctypes.patch
Patch041: nfs-utils-1.2.3-id2strings.patch
Patch042: nfs-utils-1.2.3-nfsd-ipv6.patch
Patch043: nfs-utils-1.2.3-svcgssd-enctypes.patch
Patch044: nfs-utils-1.2.3-mount-opt-41.patch
Patch045: nfs-utils-1.2.3-mountd-use_ipaddr-regression.patch
Patch046: nfs-utils-1.2.3-mount-addrlist.patch
Patch047: nfs-utils-1.2.3-gssd-man-lflag.patch
#
# RHEL6.5
#
Patch048: nfs-utils-1.2.3-mountd-estale.patch
Patch049: nfs-utils-1.2.3-nfsstat-names.patch
Patch050: nfs-utils-1.2.3-nfsman-retrans.patch
Patch051: nfs-utils-1.2.3-smnotify-localhost.patch
Patch052: nfs-utils-1.2.3-nfsstat-pnfs.patch
Patch053: nfs-utils-1.2.3-exports-man-noacl.patch
Patch054: nfs-utils-1.2.3-conffile-sec-ignore.patch
Patch055: nfs-utils-1.2.3-smnotify-vflag.patch
Patch056: nfs-utils-1.2.3-nfsconfig.patch
#
# RHEL6.6
#
Patch057: nfs-utils-1.2.3-gssd-freeprivatedata.patch
Patch058: nfs-utils-1.2.3-gssd-lifetime.patch
Patch059: nfs-utils-1.2.3-idmap-dirscancb.patch
Patch060: nfs-utils-1.2.3-gssd-alwaysreturn.patch
Patch061: nfs-utils-1.2.3-nfsidmap-multikeyrings.patch
Patch062: nfs-utils-1.2.3-mount-remount.patch
Patch063: nfs-utils-1.2.3-rpcdebug-state.patch
Patch064: nfs-utils-1.2.3-nfsmountconf-attrs.patch
Patch065: nfs-utils-1.2.3-nfsidmap-xlogerrno.patch
Patch066: nfs-utils-1.2.3-statd-bindresvport.patch
Patch067: nfs-utils-1.2.3-statd-loopback.patch
Patch068: nfs-utils-1.2.3-nfsiostat-flush.patch
Patch069: nfs-utils-1.2.3-exportfs-bover.patch
Patch070: nfs-utils-1.2.3-mountd-subnets.patch
Patch071: nfs-utils-1.2.3-mount-locallock.patch
Patch072: nfs-utils-1.2.3-mountd-fedfs.patch
Patch073: nfs-utils-1.2.3-gssd-adhostname.patch
Patch074: nfs-utils-1.2.3-nfsiostat-manupdate.patch
Patch075: nfs-utils-1.2.3-mountd-manargs.patch
Patch076: nfs-utils-1.2.3-exportfs-ipv6-brackets.patch
Patch077: nfs-utils-1.2.3-exportfs-nordirplus.patch
Patch078: nfs-utils-1.2.3-gssd-pipfs-errors.patch
Patch079: nfs-utils-1.2.3-exportfs-warn.patch
Patch080: nfs-utils-1.2.3-nfsiostat-cache.patch
Patch081: nfs-utils-1.2.3-mountd-libblkid.patch
#
# RHEL6.7
#
Patch082: nfs-utils-1.2.3-exports-typeo.patch
Patch083: nfs-utils-1.2.3-mountd-vroots-v23.patch
Patch084: nfs-utils-1.2.3-exports-dot-d.patch
Patch085: nfs-utils-1.2.3-mount-remount-fail.patch
Patch086: nfs-utils-1.2.3-mountstats-update.patch
Patch087: nfs-utils-1.2.3-mountstats-returnvals.patch
Patch088: nfs-utils-1.2.3-mountstats-normal.patch
Patch089: nfs-utils-1.2.3-mountd-memoryleak.patch
Patch090: nfs-utils-1.2.3-mountd-vroots-secflavor.patch
Patch091: nfs-utils-1.2.3-exportfs-scandir.patch
Patch092: nfs-utils-1.2.3-gssd-nospkm3.patch
Patch093: nfs-utils-1.2.3-mountd-vroots-allflavors.patch
Patch094: nfs-utils-1.2.3-gssd-expired-creds.patch
Patch095: nfs-utils-1.2.3-gssd-no-printerr.patch
Patch096: nfs-utils-1.2.3-mount-ipv6-parsing.patch
#
# RHEL6.8
#
Patch097: nfs-utils-1.2.3-nfsidmap-args.patch
Patch098: nfs-utils-1.2.3-nfsidmap-display.patch
Patch099: nfs-utils-1.2.3-gssd-libdebug.patch
Patch100: nfs-utils-1.2.3-gssd-princname.patch
Patch101: nfs-utils-1.2.3-gssd-uppercase.patch
Patch102: nfs-utils-1.2.3-sm-notify-cleanup-sm-bak.patch
Patch103: nfs-utils-1.2.3-svccreat-errors.patch
Patch104: nfs-utils-1.2.3-gssd-no-pipfs-errors.patch
Patch105: nfs-utils-1.2.3-gssd-set-home.patch
Patch106: nfs-utils-1.2.3-statd-monitor-list.patch
Patch107: nfs-utils-1.2.3-mountstats-typo.patch
Patch108: nfs-utils-1.2.3-mount-econnrefused.patch
Patch109: nfs-utils-1.2.3-exportfs-nospaces.patch
Patch110: nfs-utils-1.2.3-idmapd-usage.patch
Patch111: nfs-utils-1.2.3-mountd-netgroup.patch
Patch112: nfs-utils-1.2.3-mountd-64bit-inodes.patch
Patch113: nfs-utils-1.2.3-gssd-timeout.patch
Patch114: nfs-utils-1.2.3-nfs_connect_nb.patch
Patch115: nfs-utils-1.2.3-nfsidmap-update.patch
#
# RHEL6.8-z
#
Patch116: nfs-utils-1.2.3-mount-nonblocking.patch
Patch117: nfs-utils-1.2.3-statd-warnings.patch
Patch118: nfs-utils-1.2.3-gssd-uppercase-fix.patch


Patch1000: nfs-utils-1.2.1-statdpath-man.patch
Patch1010: nfs-utils-1.2.2-statdpath.patch
Patch1020: nfs-utils-1.2.1-exp-subtree-warn-off.patch

Group: System Environment/Daemons
Provides: exportfs    = %{epoch}:%{version}-%{release}
Provides: nfsstat     = %{epoch}:%{version}-%{release}
Provides: showmount   = %{epoch}:%{version}-%{release}
Provides: rpcdebug    = %{epoch}:%{version}-%{release}
Provides: rpc.idmapd  = %{epoch}:%{version}-%{release}
Provides: rpc.mountd  = %{epoch}:%{version}-%{release}
Provides: rpc.nfsd    = %{epoch}:%{version}-%{release}
Provides: rpc.statd   = %{epoch}:%{version}-%{release}
Provides: rpc.gssd    = %{epoch}:%{version}-%{release}
Provides: rpc.svcgssd = %{epoch}:%{version}-%{release}
Provides: mount.nfs   = %{epoch}:%{version}-%{release}
Provides: mount.nfs4  = %{epoch}:%{version}-%{release}
Provides: umount.nfs  = %{epoch}:%{version}-%{release}
Provides: umount.nfs4 = %{epoch}:%{version}-%{release}
Provides: sm-notify   = %{epoch}:%{version}-%{release}
Provides: start-statd = %{epoch}:%{version}-%{release}

License: MIT and GPLv2 and GPLv2+ and BSD
Buildroot: %{_tmppath}/%{name}-%{version}-root
Requires: rpcbind, sed, gawk, sh-utils, fileutils, textutils, grep
Requires: modutils >= 2.4.26-9 keyutils >= 1.4-4
BuildRequires: libgssglue-devel libevent-devel libcap-devel
BuildRequires: nfs-utils-lib-devel >= 1.1.0-3 libtirpc-devel >= 0.2.1-11
BuildRequires: libblkid-devel
BuildRequires: krb5-libs >= 1.4 autoconf >= 2.57 openldap-devel >= 2.2
BuildRequires: automake, libtool, glibc-headers
BuildRequires: krb5-devel, tcp_wrappers-devel
Requires(pre): shadow-utils >= 4.0.3-25
Requires(pre): /sbin/chkconfig /sbin/nologin
Requires: nfs-utils-lib >= 1.1.0-3 libgssglue libevent
Requires: libtirpc >= 0.2.1-11 libblkid libcap python-argparse

%description
The nfs-utils package provides a daemon for the kernel NFS server and
related tools, which provides a much higher level of performance than the
traditional Linux NFS server used by most users.

This package also contains the showmount program.  Showmount queries the
mount daemon on a remote host for information about the NFS (Network File
System) server on the remote host.  For example, showmount can display the
clients which are mounted on that host.

This package also contains the mount.nfs and umount.nfs program.

%prep
%setup -q

%patch001 -p1

#
# RHEL6.1
#
# 671474 - Picking the right principal name when using krb5 security
%patch002 -p1
# 698220 - rpc.svcgssd: Segmentation fault on error
%patch003 -p1
#
# RHEL 6.2
#
# 697359 - -n option lack in the nfs-utils man page
%patch004 -p1
# 697981 - nfs-utils: mount.nfs fails to anticipate RLIMIT_FSIZE
%patch005 -p1
# 715078 - update exports(5) manpage with details about ipv6 configuration
%patch006 -p1
# 723438 - rpc.mountd can segfault with showmount
%patch007 -p1
# 715391 - mixing wildcard and host/subnet exports can allow unintended hosts to mount
%patch008 -p1
# 702273 - Cannot umount NFS mount containing spaces 
%patch009 -p1
# 732673 - [REG] Can not umount NFS IPv6 mount
%patch010 -p1
# 726112 - RH725530 - showmount -e to RHEL 6.x NFS server only 
#          returns the first host a directory is exported to
%patch011 -p1
# 723780 - submarvellous messages from mount.nfs
%patch012 -p1
# 731693 - mount.nfs needs a more descriptive error when nfs version is specified incorrectly
%patch013 -p1
# 697981 - nfs-utils: mount.nfs fails to anticipate RLIMIT_FSIZE (try 2)
%patch014 -p1
# 744657 - The same NFS share can be mounted on the same location multiple times on IPv6-ready network 
%patch015 -p1
# 747400 - RHEL 6.2 beta rpcdebug has no flag for pNFS debug
%patch016 -p1
# Bug 772496 - Enable the keyring based idmapping
%patch017 -p1
# 737990 - Incorrect timeout sequence on NFS/TCP client
%patch018 -p1
# 751089 - nfsd: nfsv4 idmapping failing: has idmapd died?
%patch019 -p1
# 772050 - only link in libtirpc to binaries that need it
%patch020 -p1
# 736741 - rpc.mountd switch not working
%patch021 -p1
# 738774 - gssd picking wrong creds
%patch022 -p1
# 740472 - mount can't run in background when using combination of bg
%patch023 -p1
#  758000 - umount can't work when mounted with duplicated slash between server_name and path_to_share
%patch024 -p1

# 754666 - nfs mount can't treat wsize defined in /etc/nfsmount.conf
%patch025 -p1
# 772619 - Add support for umlauts in group names
%patch026 -p1
# 800335 - Race in exportfs overwrites etab and causes missing exports
%patch027 -p1
# 787970 - idmapd fails to decode group names with spaces
%patch028 -p1
# 740472 - mount can't run in background when using combination of bg and vers/nfsvers=[2|3] options
%patch029 -p1
# 801085 - Unable to unmount an exported path which is a symlink using NFSv4
%patch030 -p1
# 816162 - mounting subdirectory of non-user account fails 
%patch031 -p1
# 816727 - nfsidmap command needs to use the Verbosity variable in /etc/idmapd.conf
%patch032 -p1
# 824517 - NFSv4 client not falling back properly to IPv4 address 
%patch033 -p1
# 815673 - NFS4 mounts hang on clients with many exports to netgroups
%patch034 -p1
# 811882 - umount can't remove mount entry against IPv6 from /etc/mtab
%patch035 -p1
# 797209 - NFS3 mounts hang on clients after getting "nfsd: Dropping request; may be revisited later" on server
%patch036 -p1
# 784909 - rpc.gssd linking issue
%patch037 -p1
# 820737 -  fix referrals that use IPv6 addresses
%patch038 -p1
# 802469 - RHEL6 fails to mount from RHEL5/Debian 6 nfs4 server with sec=krb5
%patch039 -p1
# 802469 - RHEL6 fails to mount from RHEL5/Debian 6 nfs4 server with sec=krb5
%patch040 -p1
# 849945 - regression: chown does not work in NFS4
%patch041 -p1
# 836947 - Upstream patch to "supress socket error when address family is not supported"
%patch042 -p1
# 877636 - RHEL6.4 kerberized NFS GSS-API error No supported enc ryption types
%patch043 -p1
# 877052 - "minorversion=" mount option missing in nfs(5) man page
%patch044 -p1
# 797209 - Fix a Regression with NFS3 mounts hang on clients after...
%patch045 -p1
# 876847 - Unable to mount localhost or 127.0.0.1 when exports with IP address or hostname
%patch046 -p1
# 889022 - no '-l' option demonstrate in rpc.gssd man page
%patch047 -p1
# 920293 - files on nfs server's exports start returning ESTALE...
%patch048 -p1
# 890146 - nfsstat names some values wrong
%patch049 -p1
# 952560 - Default value of retrans option in 'man 5 nfs' is incorrect
%patch050 -p1
# 950324 - sm-notify doesn't handle localhost properly
%patch051 -p1
# 962602 - nfsstat counters for pnfs ops are broken
%patch052 -p1
# 991302 - man page and documentation need to be updated regarding NFS export..
%patch053 -p1
# 889272 - Improve nfsmount.conf configuration parsing
%patch054 -p1
# 995484 - sm-notify: "-v hostname" doesn't work when IPV6_SUPPORT is enabled
%patch055 -p1
# 889272 - Improve nfsmount.conf configuration parsing
%patch056 -p1
# 1081198 - RHEL 6.5 nfs-utils-1.2.3 sends RPCSEC_GSS_DESTROY with no... 
%patch057 -p1
# 1081208 - RHEL GSSD: Pass GSS_context lifetime to the kernel
%patch058 -p1
# 1040135 - seeing rpc.idmapd messages "dirscancb: open():... 
%patch059 -p1
# 1070927 - RPC: AUTH_GSS upcall timed out
%patch060 -p1
# 1033708 - Updating to nfs-utils-1.2.3-39.el6 causes rpcidmapd 
%patch061 -p1
# 1079047 - mount -o remount fails if root squashing is enabled...
%patch062 -p1
# 1087878 - rpcdebug is missing handling for the 'state' flag for the nfs module
%patch063 -p1
# 918319 - Update man page of nfsmount.conf to include syntax for mount options
%patch064 -p1
# 1061505 - Invalid error reporting for nfs4_* functions in nfsidmap
%patch065 -p1
# 1075224 - generates a constant stream of "nsm_parse_reply: can't decode RPC reply"...
%patch066 -p1
# 1018358 - rpc.statd: Bind downcall socket to loopback address
%patch067 -p1
# 1007195 - nfsiostat: periodically flush stdout
%patch068 -p1
# 1008381 - [exportfs] buffer overflow
%patch069 -p1
# 1098592 - Stop Treat IP addresses a FQDN rather than SUBNETs.
%patch070 -p1
# 1017477 - manpage for NFS(5) implies that local_lock is not supported in RHEL 6, when it is
%patch071 -p1
# 1024035 - Support junction resolution in RHEL 6 rpc.mountd
%patch072 -p1
#1067423 - Use short hostname when using AD based KDC for secure NFS
%patch073 -p1
# 869684 - Man pages are not explaining the output of nfsiostat 
%patch074 -p1
# 1003555 - In rpc.mountd man page -V -f -p -H and so on need and args
%patch075 -p1
# 1112776 - exportfs currently doesn't support IPv6 address....
%patch076 -p1
# 1128281 - nfs-utils patch for Readdirplus / disable readdirplus
%patch077 -p1
# 1116698 - [rpc.gssd] rpc.gssd always start fail, and no enough log/message...
%patch078 -p1
# 1133562 - exportfs: warning - 'exp' may be used uninitialized in this function
%patch079 -p1
# 1066314 - nfsiostat command hitting in cache
%patch080 -p1
# 1113204 - Requesting upstream commit (mountd: optimize libblkid usage)...
%patch081 -p1
# 1152554 - typo in manpage
%patch082 -p1
# 1164317 - Cannot mount a wildcard export using NFS3 when...
%patch083 -p1
# 1123099 - Add support for /etc/exports.d to RHEL 6
%patch084 -p1
# 1026446 - mount.nfs with MS_REMOUNT doesn't print error message on failure
%patch085 -p1
# 1172827 - Update mountstats command to the latest upstream version
%patch086 -p1
# 1172827 - Fixed return values 
%patch087 -p1
# 1007281 - mountstats command could not process the argument /mountpoint/
%patch088 -p1
# 1194802 - rpc.mountd leaks memory in v4root_create() and getexportent()
%patch089 -p1
# 1187277 - rpc.mountd can set up pseudo exports without the correct security flavors 
%patch090 -p1
# 1203133 - exportfs -r always output garbage log: exportfs: scandir...
%patch091 -p1
# 1187277 - remove SPKM-3 support from gssd
%patch092 -p1
# 1187277 - enable all auth flavors on pseudofs exports
%patch093 -p1
# 1216156 - Failure to renew Kerberos credentials while running with uid=0
%patch094 -p1
# 949100 - krb5 mounts hang. complains that gssd is not running
%patch095 -p1
# 1202700 - mount.nfs permission denied on IPv6 address...
%patch096 -p1
# 1230600 - libnfsidmap: crash due to not checking arguments 
%patch097 -p1
# 948680 - Request a method(like a testperm) to show parameters 
%patch098 -p1
# 1273161 - Allow gssd and svcgssd to set the libtirpc debug level 
%patch099 -p1
# 1268031 - rpc.gssd needs to be able to override the machine...
%patch100 -p1
# 1273166 - rpc.gssd should not assume that the machine account is in uppercase
%patch101 -p1
# 1278921 - sm-notify doesn't clean up after itself 
%patch102 -p1
# 1156647 - Display proper message as to why rpc.statd failed...
%patch103 -p1
# 1220156 - rpc.gssd ERROR: can't open /var/lib/nfs/rpc_pipefs/nfs/clnt
%patch104 -p1
# 1223661 - Hangs when logging in on NFS4 /home
%patch105 -p1
# 1280024 - lockd's and statd's monitor lists get out of sync
%patch106 -p1
# 1263968 - typo in mountstats man page that should not contain "-s|--since" 
%patch107 -p1
# 1287894 - Trying to automount a non-existent directory using...
%patch108 -p1
# 735696 - exportfs give incorrect message for mount dir containing...
%patch109 -p1
# 1001439 - rpc.idmapd add help -h option, to output "usage:" info 
%patch110 -p1
# 1231998 - rpc.mountd does not check for membership of IP...
%patch111 -p1
# 994564 - 994564 - rpc.mountd produces stale file handles
%patch112 -p1
# 1296607 - have a configurable connection timeout for the rpcgssd service
%patch113 -p1
# 1299004 - Unhandled EINTR during connection establishment leads to...
%patch114 -p1
# 1303877 - [6.8] regression: nfs idmap fail
%patch115 -p1
# 1350702 - Back port of bz 1163891 required as rpc.mountd can be...
%patch116 -p1
# 1351259 - rpc.statd emits warnings like "Failed to delete: could not..
%patch117 -p1
# 1363837 - cthon - rpc.gssd crash reading krb5.keytab in find_keytab_entry()
%patch118 -p1

%patch1000 -p1
%patch1010 -p1
%patch1020 -p1


# Remove .orig files
find . -name "*.orig" | xargs rm -f

%build

%ifarch s390 s390x sparcv9 sparc64
PIE="-fPIE"
%else
PIE="-fpie"
%endif
export PIE

sh -x autogen.sh

GSSGLUE_CFLAGS="`echo -Wl,-lgssglue`"
CFLAGS="`echo $RPM_OPT_FLAGS $ARCH_OPT_FLAGS $PIE -D_FILE_OFFSET_BITS=64`"
%configure \
    CFLAGS="$CFLAGS" \
    CPPFLAGS="$DEFINES" \
    LDFLAGS="-pie" \
	GSSGLUE_CFLAGS="$GSSGLUE_CFLAGS" \
    --enable-mount \
    --enable-mountconfig \
    --enable-ipv6 \
    --with-statdpath=/var/lib/nfs/statd \

make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{/sbin,/usr/sbin}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man5,man8}
mkdir -p $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/sysconfig,/etc/request-key.d}
make DESTDIR=$RPM_BUILD_ROOT install
install -m 755 tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT/usr/sbin
install -m 755 %{SOURCE10} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install -m 755 %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install -m 755 %{SOURCE12} $RPM_BUILD_ROOT/etc/rc.d/init.d/rpcidmapd
install -m 755 %{SOURCE13} $RPM_BUILD_ROOT/etc/rc.d/init.d/rpcgssd
install -m 755 %{SOURCE14} $RPM_BUILD_ROOT/etc/rc.d/init.d/rpcsvcgssd
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT/etc/sysconfig/nfs
install -m 644 %{SOURCE16} $RPM_BUILD_ROOT/etc/request-key.d/
install -m 644 utils/mount/nfsmount.conf  $RPM_BUILD_ROOT/etc
install -m 755 %{SOURCE17} $RPM_BUILD_ROOT/sbin/nfs_cache_getent
(cd $RPM_BUILD_ROOT/%{_mandir}/man8 && ln -s mount.nfs.8.gz mount.nfs4.8.gz)
(cd $RPM_BUILD_ROOT/%{_mandir}/man8 && ln -s umount.nfs.8.gz umount.nfs4.8.gz)

mkdir -p $RPM_BUILD_ROOT/var/lib/nfs/rpc_pipefs

touch $RPM_BUILD_ROOT/var/lib/nfs/rmtab
mv $RPM_BUILD_ROOT/usr/sbin/rpc.statd $RPM_BUILD_ROOT/sbin

mkdir -p $RPM_BUILD_ROOT/var/lib/nfs/statd/sm
mkdir -p $RPM_BUILD_ROOT/var/lib/nfs/statd/sm.bak
mkdir -p $RPM_BUILD_ROOT/var/lib/nfs/v4recovery

rm -f $RPM_BUILD_ROOT/usr/share/man/man5/idmapd.conf.5
rm -f $RPM_BUILD_ROOT/usr/sbin/gss_clnt_send_err
rm -f $RPM_BUILD_ROOT/usr/sbin/gss_destroy_creds

%clean
echo rm -rf $RPM_BUILD_ROOT

%pre
# move files so the running service will have this applied as well
for x in gssd svcgssd idmapd ; do
    if [ -f /var/lock/subsys/rpc.$x ]; then
        mv /var/lock/subsys/rpc.$x /var/lock/subsys/rpc$x
    fi
done

/usr/sbin/useradd -l -c "RPC Service User" -r \
        -s /sbin/nologin -u 29 -d /var/lib/nfs rpcuser 2>/dev/null || :
/usr/sbin/groupadd -g 29 rpcuser 2>/dev/null || :

# Using the 16-bit value of -2 for the nfsnobody uid and gid
%define nfsnobody_uid   65534

# Create nfsnobody gid as long as it does not already exist.
cat /etc/group | cut -d':' -f 1 | grep --quiet nfsnobody 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/groupadd -g %{nfsnobody_uid} nfsnobody 2>/dev/null || :
else
    /usr/sbin/groupmod -g %{nfsnobody_uid} nfsnobody 2>/dev/null || :
fi

# Create nfsnobody uid as long as it does not already exist.
cat /etc/passwd | cut -d':' -f 1 | grep --quiet nfsnobody 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/useradd -l -c "Anonymous NFS User" -r -g %{nfsnobody_uid} \
        -s /sbin/nologin -u %{nfsnobody_uid} -d /var/lib/nfs nfsnobody 2>/dev/null || :
else

    /usr/sbin/usermod -u %{nfsnobody_uid} -g %{nfsnobody_uid} nfsnobody 2>/dev/null || :
fi

%post
/sbin/chkconfig --add nfs
/sbin/chkconfig --add nfslock
/sbin/chkconfig --add rpcgssd
/sbin/chkconfig --add rpcsvcgssd
# Make sure statd used the correct uid/gid.
chown -R rpcuser:rpcuser /var/lib/nfs/statd

%preun
if [ "$1" = "0" ]; then
    /etc/rc.d/init.d/nfs condstop > /dev/null
    /etc/rc.d/init.d/rpcgssd condstop > /dev/null
    /etc/rc.d/init.d/nfslock condstop > /dev/null
    /sbin/chkconfig --del rpcgssd
    /sbin/chkconfig --del rpcsvcgssd
    /sbin/chkconfig --del nfs
    /sbin/chkconfig --del nfslock
    /usr/sbin/userdel rpcuser 2>/dev/null || :
    /usr/sbin/groupdel rpcuser 2>/dev/null || :
    /usr/sbin/userdel nfsnobody 2>/dev/null || :
    /usr/sbin/groupdel nfsnobody 2>/dev/null || :
    rm -rf /var/lib/nfs/statd
    rm -rf /var/lib/nfs/v4recovery
fi

%posttrans
if [ ! -f /etc/sysconfig/nfs-utils-disable-posttrans ]; then
	if [ -f /etc/rc.d/init.d/rpcgssd ]; then
    	/etc/rc.d/init.d/rpcgssd condrestart > /dev/null
	fi
	if [ -f /etc/rc.d/init.d/nfs ]; then
    	/etc/rc.d/init.d/nfs condrestart > /dev/null
	fi
	if [ -f /etc/rc.d/init.d/nfslock ]; then
		/etc/rc.d/init.d/nfslock condrestart > /dev/null
	fi
fi

%triggerpostun -- nfs-server
/sbin/chkconfig --add nfs

%triggerpostun -- knfsd
/sbin/chkconfig --add nfs

%triggerpostun -- knfsd-clients
/sbin/chkconfig --add nfslock

%files
%defattr(-,root,root)
%config /etc/rc.d/init.d/nfs
%config /etc/rc.d/init.d/rpcidmapd
%config /etc/rc.d/init.d/rpcgssd
%config /etc/rc.d/init.d/rpcsvcgssd
%config(noreplace) /etc/sysconfig/nfs
%config(noreplace) /etc/nfsmount.conf
%config(noreplace) %{_sysconfdir}/request-key.d/id_resolver.conf
%dir /var/lib/nfs/v4recovery
%dir /var/lib/nfs/rpc_pipefs
%dir /var/lib/nfs
%dir %attr(700,rpcuser,rpcuser) /var/lib/nfs/statd
%dir %attr(700,rpcuser,rpcuser) /var/lib/nfs/statd/sm
%dir %attr(700,rpcuser,rpcuser) /var/lib/nfs/statd/sm.bak
%config(noreplace) %verify(not md5 size mtime) %attr(644,rpcuser,rpcuser) /var/lib/nfs/state
%config(noreplace) %verify(not md5 size mtime) /var/lib/nfs/xtab
%config(noreplace) %verify(not md5 size mtime) /var/lib/nfs/etab
%config(noreplace) %verify(not md5 size mtime) /var/lib/nfs/rmtab
%doc linux-nfs/*
/sbin/rpc.statd
/sbin/nfs_cache_getent
/usr/sbin/exportfs
/usr/sbin/nfsstat
/usr/sbin/rpcdebug
/usr/sbin/rpc.mountd
/usr/sbin/rpc.nfsd
/usr/sbin/showmount
/usr/sbin/rpc.idmapd
/usr/sbin/rpc.gssd
/usr/sbin/rpc.svcgssd
/usr/sbin/sm-notify
/usr/sbin/start-statd
/usr/sbin/mountstats
/usr/sbin/nfsiostat
/usr/sbin/nfsidmap
%{_mandir}/*/*
%config /etc/rc.d/init.d/nfslock

%attr(4755,root,root)   /sbin/mount.nfs
%attr(4755,root,root)   /sbin/mount.nfs4
%attr(4755,root,root)   /sbin/umount.nfs
%attr(4755,root,root)   /sbin/umount.nfs4

%changelog
* Mon Aug 22 2016 Steve Dickson <steved@redhat.com> 1.2.3-70_8.2
- gssd: Fix inner-loop variable reuse (bz 1363837)

* Wed Jun 29 2016 Steve Dickson <steved@redhat.com> 1.2.3-70_8.1
- statd: suppress a benign log message in nsm_delete_host() (bz 1351259)

* Tue Jun 28 2016 Steve Dickson <steved@redhat.com> 1.2.3-70_8
- rpc.mountd: set libtirpc nonblocking mode to avoid DO (bz 1350702)

* Sat Feb 13 2016 Steve Dickson <steved@redhat.com> 1.2.3-70
- Fixed a regression introduced by a kernel change (bz 1303877)

* Thu Feb 11 2016 Steve Dickson <steved@redhat.com> 1.2.3-69
- nfs_connect_nb: handle EINTR during connection establishment (bz 1299004)

* Fri Jan  8 2016 Steve Dickson <steved@redhat.com> 1.2.3-68
- gssd: configurable connection timeout for the rpcgssd service (bz 1296607)

* Sat Dec 19 2015 Steve Dickson <steved@redhat.com> 1.2.3-67
- mount.nfs: Fix fallback from tcp to udp (bz 1287894)
- exportfs: escape path for function test_export (bz 735696)
- nfs-utils.spec: No verification on runtime configuration files (bz 1118176)
- idmapd: added usage statement (bz 1001439)
- mountd: fix netgroup lookup for short hostnames (bz 1231998)
- mountd: fix bug affecting exports of dirs with 64bit inode number (bz 994564)

* Wed Dec  2 2015 Steve Dickson <steved@redhat.com> 1.2.3-66
- svc_create: Make sure errors are logged (bz 1156647)
- gssd: suppress error message if rpc_pipefs dir disappears (bz 1220156)
- gssd: set $HOME to prevent recursion (bz 1223661)
- statd: Update existing record if we receive SM_MON... (bz 1280024)
- mountstats.man: fixed typo in man page (bz 1263968)

* Wed Nov 18 2015 Steve Dickson <steved@redhat.com> 1.2.3-65
- nfsidmap: make sure give arguments are valid (bz 1230600)
- nfsidmap: Display the effective NFSv4 domain name (bz 948680)
- gssd: allow gssd and svcgssd to set the libtirpc debug level (bz 1273161)
- gssd: select non-conventional principal (bz 1268031)
- gssd:  Don't assume the machine account will be in uppercase (bz 1273166)
- sm-notify: delete files in sm.bak after a NOTIFY reply (bz 1278921)

* Tue May 19 2015 Steve Dickson <steved@redhat.com> 1.2.3-64
- Stop removing '[]' brackets on IPv6 addresses (bz 1202700)

* Mon May 18 2015 Steve Dickson <steved@redhat.com> 1.2.3-63
- Removed printerr from gssd (bz 949100)

* Sat May 16 2015 Steve Dickson <steved@redhat.com> 1.2.3-62
- Fixed renew creds with uid=0 (bz 1216156)

* Mon Apr  6 2015 Steve Dickson <steved@redhat.com> 1.2.3-61
- Fixed typo in pseudofs exports patch (bz 1187277)

* Wed Apr  1 2015 Steve Dickson <steved@redhat.com> 1.2.3-60
- Remove SPKM-3 support from gssd (bz 1187277)
- Enable all auth flavors on pseudofs exports (bz 1187277)

* Wed Mar 10 2015 Steve Dickson <steved@redhat.com> 1.2.3-59
- Silently fail when /etc/exports.d does not exist (bz 1203133)

* Tue Mar 10 2015 Steve Dickson <steved@redhat.com> 1.2.3-58
- Fixed pseudo exports without security flavors  (bz 1187277)
- Made the posttrans conditional (bz 1078829)

* Sat Mar  7 2015 Steve Dickson <steved@redhat.com> 1.2.3-57
- Fixed a couple memory leakes in mountd (bz 1194802)

* Wed Mar  4 2015 Steve Dickson <steved@redhat.com> 1.2.3-56
- Fixed return values in mountstats (bz 1172827)
- mountstats: Normalize the mountpoints passed on the command line (bz 1007281)

* Thu Feb 19 2015 Steve Dickson <steved@redhat.com> 1.2.3-55
- Fixed typo in exports manpage  (bz 1152554)
- mountd need to ignore vroots on v3 mounts (bz 1164317)
- Added support for /etc/exports.d (bz 1123099)
- Print error message on remount failures (bz 1026446)
- Update mountstats to upstream version (bz 1172827)

* Thu Sep  4 2014 Steve Dickson <steved@redhat.com> 1.2.3-54
- Fixed typo in nfs-utils-1.2.3-nfsiostat-cache.patch (bz 1136814)

* Mon Aug 25 2014 Steve Dickson <steved@redhat.com> 1.2.3-53
- gssd: Error out when rpc_pipefs directory is empty (bz 1116698)
- exportfs: Removed a warning from exportfs.c (bz 1133562)
- nfsiostat: Corrected the cache hits (bz 1066314)
- mountd: optimize libblkid usage (bz 1113204)

* Sun Aug 24 2014 Steve Dickson <steved@redhat.com> 1.2.3-52
- exportfs: disable READERPLUS for v3 (bz 1128281)

* Tue Jul 22 2014 Steve Dickson <steved@redhat.com> 1.2.3-51
- Added ipv6 bracket support to exportfs (bz 1112776)

* Tue Jun 17 2014 Steve Dickson <steved@redhat.com> 1.2.3-50
- gssd: Drop full domain when constructing the Ad hostname (bz 1067423)
- Explained nfsiostat output in man page (bz 869684)
- mountd.man: Added missing arguments in man page (bz 1003555)

* Tue May 27 2014 Steve Dickson <steved@redhat.com> 1.2.3-49
- Added Fedfs support to rpc.mound (bz 1024035)

* Thu May 22 2014 Steve Dickson <steved@redhat.com> 1.2.3-48
- Reworked the V4 grace period is set (bz 1058354)

* Thu May 22 2014 Steve Dickson <steved@redhat.com> 1.2.3-47
- Stop Treat IP addresses a FQDN rather than SUBNETs. (bz 1098592)
- Removed the local_lock not supported line in man page (bz 1017477)

* Fri May 16 2014 Steve Dickson <steved@redhat.com> 1.2.3-46
- Have nfs.init signal rpc.idmapd when its already running (bz 1033708)

* Fri May  2 2014 Steve Dickson <steved@redhat.com> 1.2.3-45
- Smothed out upgrads from rhel6 to rhel7 (bz 1086625)
- rpc.statd: Bind downcall socket to loopback address (bz 1018358)
- nfsiostat: periodically flush stdout (bz 1007195)
- Fixed a buffer overflow in exportfs (bz 1008381)

* Tue Apr 29 2014 Steve Dickson <steved@redhat.com> 1.2.3-44
- Allow -o remounts to work (bz 1079047)
- Put state flag in rpcdebug (bz 1087878)
- Added more options to nfsmount.conf (bz 918319)
- Fixed error reporting in nfsidmap (bz 1061505)
- Fixed socket binding loop in rpc.statd (bz 1075224)

* Thu Apr 24 2014 Steve Dickson <steved@redhat.com> 1.2.3-43
- nfsidmap now creates multiple key rings. (bz 1033708)

* Tue Apr  1 2014 Steve Dickson <steved@redhat.com> 1.2.3-42
- gssd: Added GSS_contest lifetime to the kernel (bz 1081208)
- rpc.idmapd: Ignore open failures in dirscancb() (bz 1040135)
- gssd: always reply to rpc-pipe requests from kernel (bz 1070927)

* Mon Mar 31 2014 Steve Dickson <steved@redhat.com> 1.2.3-41
- gssd: Call authgss_free_private_data() if library provides it. (bz 1081198)

* Fri Mar 21 2014 Steve Dickson <steved@redhat.com> 1.2.3-40
- Re-enabled rpc.idmapd on the client (bz 1033708)

* Wed Oct  9 2013 Steve Dickson <steved@redhat.com> 1.2.3-39
- Remove duplicate options from mtab entry (bz 889272)

* Sat Aug 17  2013 Steve Dickson <steved@redhat.com> 1.2.3-38
- Fixed typo in nfsstat's output (bz 890146)
- Fixed retrans defaults in nfs(5) man page (bz 952560)
- Clean rpc.idmapd messages when nfsd starts (bz 892235)
- Fixed sm-notify to work with localhost (bz 950324)
- Fixed pNFS stats (bz 962602)
- Remove no_acl from exports(5) man page (bz 991302)
- Improve nfsmount.conf configuration parsing (bz 889272)
- Fixed sm-notify -v (bz 995484)

* Wed Jul  3 2013 Steve Dickson <steved@redhat.com> 1.2.3-37
- Stopped mountd from return ESTALE on large configurations (bz 920293)

* Thu Dec 20 2012 Steve Dickson <steved@redhat.com> 1.2.3-36
- Added -l flag to gssd man page. (bz 889022)

* Wed Nov 28 2012 Steve Dickson <steved@redhat.com> 1.2.3-35
- Fixed a regession in mountd that cause a localhost mounts to hang (bz 797209)
- Make sure mount tries all the addresses returned by getaddrinfo (bz 876847)

* Mon Nov 19 2012 Steve Dickson <steved@redhat.com> 1.2.3-34
- Update the default encryption types in svcgssd (bz 877636)
- Added the -v 4.1 mount option (bz 877052)

* Tue Nov  6  2012 Steve Dickson <steved@redhat.com> 1.2.3-33
- Install the nfs_cache_getent script for DNS resolution for NFSv4 referrals (bz 869400)

* Tue Nov  6 2012 Steve Dickson <steved@redhat.com> 1.2.3-32
- Supress socket error when address family is not supported (bz 836947)

* Mon Nov  5 2012 Steve Dickson <steved@redhat.com> 1.2.3-31
- Allow ID strings in idmapping to be handled correctly (bz 849945)

* Wed Oct 10 2012 Steve Dickson <steved@redhat.com> 1.2.3-30
- gssd: Don't link with libgssapi_krb5 (bz 784909)
- Fix referrals that use IPv6 addresses (bz 820737)
- Add -l option to gssd to force legacy behaviour (bz 802469)
- Add support to svcgssd to limit the negotiated enctypes (bz 802469)
- Changed nfs.init to allow umounts to happen cleanly during 
  system shutdown (bz 856923)

* Thu Sep 11 2012 Steve Dickson <steved@redhat.com> 1.2.3-29
- V4 mounts hang on exports to netgroups (bz 815673)
- Strip the '[]' off of ipv6 addresses (bz 811882)
- Removed a use_ipaddr race in mountd (bz 797209)

* Fri Jul  6 2012 Steve Dickson <steved@redhat.com> 1.2.3-28
- Corrected v4 mounts to fall back to IPv4 address (bz 824517)

* Thu Jul  5 2012 Steve Dickson <steved@redhat.com> 1.2.3-27
- Made nfsidmap look at Verbosity in idmap.conf (bz 816727)

* Tue May 29 2012 Steve Dickson <steved@redhat.com> 1.2.3-26
- Fixed typo in the checking of nfsnobody (bz 816149)
- Fixed the exporting of subdirectories (bz 816162)

* Fri May 25 2012 Steve Dickson <steved@redhat.com> 1.2.3-25
- Correctly search for the existence of nfsnobody (bz 816149)

* Tue May 22 2012 Steve Dickson <steved@redhat.com> 1.2.3-24
- Change the default group id for nfsnobody correctly (bz 816149)

* Tue May  8 2012 Steve Dickson <steved@redhat.com> 1.2.3-23
- Added content to the patch that fixes bz 740472

* Wed Apr 25 2012 Steve Dickson <steved@redhat.com> 1.2.3-22
- NFS initscript needs to do a rpcidmapd condrestart not a condstart (bz 809201)
- Allow v2|v3 background mounts to retry when server is down (bz 740472) 
- Fix the umounting of symbolic links (bz 801085)

* Fri Apr 13 2012 Steve Dickson <steved@redhat.com> 1.2.3-21
- Switch the order on how the server is brought up (bz 803946)

* Wed Mar 28 2012 Steve Dickson <steved@redhat.com> 1.2.3-20
- Fixed bug in Normalizing umount paths (bz 758000)

* Thu Mar  8 2012 Steve Dickson <steved@redhat.com> 1.2.3-19
- Fixed decode group names with spaces in idmapd (bz 787970)
- Remove two unused gss commands (bz 738932)

* Wed Mar  7 2012 Steve Dickson <steved@redhat.com> 1.2.3-18
- Fixed nfs initscript to handle reloads correctly (bz 784022)
- Add support for umlauts in group names in idmapper (bz 772619)
- Stoppped racing exportfs in clusters (bz 800335)

* Tue Mar  6 2012 Steve Dickson <steved@redhat.com> 1.2.3-17
- Used correct locking file in nfs.init script (bz 772543)
- Create a locking file for rpc.rquotad (bz 766472)
- Normalized umount paths (bz 758000)
- Fixed parsing error in nfsmount.conf code (bz 754666)

* Wed Feb 29 2012 Steve Dickson <steved@redhat.com> 1.2.3-16
- Enable the keyring based idmapping (bz 772496)
- Correct nfs(5) man page on how TCP retries are done (bz 737990)
- Fixed sigio problem in rpc.idmapd (bz 751089)
- Only link in libtirpc to binaries that need it (bz 772050)
- Increase the stdio file buffer size for procfs files (bz 736741)
- Fixed gssd from picking the wrong creds (bz 738774)
- Mounts fail with using -o bg,vers= options (bz 740472)

* Fri Oct 21 2011 Steve Dickson <steved@redhat.com> 1.2.3-15
- mout.nfs: Don't roll back to IPv4 whe IPv6 fails (bz 744657)
- rpcdebug: Added pNFS and FSCache debugging (bz 747400)

* Wed Oct 19 2011 Steve Dickson <steved@redhat.com> 1.2.3-14
- mount.nfs: Backported how upstream handles the SIGXFSZ signal (bz 697981)

* Tue Oct 18 2011 Steve Dickson <steved@redhat.com> 1.2.3-13
- mount.nfs: Reworked the code that deals with RLIMIT_FSIZE (bz 697981)

* Mon Sep 19 2011 Steve Dickson <steved@redhat.com> 1.2.3-12
- Removed the stripping of debugging information from rpcdebug (bz 729001)

* Fri Sep 16 2011 Steve Dickson <steved@redhat.com> 1.2.3-11
- mount.nfs: Fixed problem in mount error verbosity patch (bz 731693) 

* Thu Sep 15 2011 Steve Dickson <steved@redhat.com> 1.2.3-10
- mount.nfs: add error verbosity to invalid versions (bz 731693)

* Tue Sep 13 2011 Steve Dickson <steved@redhat.com> 1.2.3-9
- umount.nfs: Got IPV6 unmounts working again (bz 732673)
- mountd: return multiple hosts exporting the same directory (bz 726112) 
- mount: Better error message for invalid version (bz 723780)

* Thu Aug 11 2011 Steve Dickson <steved@redhat.com> 1.2.3-8
- initscripts: just try to mount rpc_pipefs always (bz 692702) 
- Rely on crypto module autoloading in init scripts
- svcgssd: Document "-n" for svcgssd (bz 697359)
- mount.nfs: anticipate RLIMIT_FSIZE (bz 697981)
- exportfs manpage: Ipv6 update (bz 715078)
- mountd: Stop segfault in mtab code (bz 723438)
- exportfs: wilcards in exports can lead to unintended mounts (bz 715391)
- umount: allow spaces in unmount paths (bz 702273)
- specfile: reordered how libgssglue is linked in (bz 720479)

* Wed Apr 20 2011 Steve Dickson <steved@redhat.com> 1.2.3-7
- Fixed segfault in rpc.svcgssd (bz 698220)

* Wed Mar 30 2011 Steve Dickson <steved@redhat.com> 1.2.3-6
- Added support for AD style kerberos to rpc.gssd (bz 671474)
- Disabled the installing of the nfsidmap command

* Tue Mar 22 2011 Steve Dickson <steved@redhat.com> 1.2.3-5
- Remove MOUNTD_NFS_V1 from nfs.sysconfig (bz 641291)

* Mon Jan 17 2011 Steve Dickson <steved@redhat.com> 1.2.3-4
- Fixed type in groupadd args for rpcuser (bz 663153)

* Fri Jan 14 2011 Steve Dickson <steved@redhat.com> 1.2.3-3
- Updated to latest upstream release: nfs-utils-1-2-4-rc5 (bz 625080)

* Thu Jan 13 2011 Steve Dickson <steved@redhat.com> 1.2.3-1
- Initscripts changes needed to support NFS over RDMA (bz 631012)
- Initscripts changes needed for NFS to shutdown cleanly (bz 636513)
- Initscripts changes needed for rpcbind to be running 
  when nfs is started (bz 641291)

* Tue Sep 28 2010 Steve Dickson <steved@redhat.com> 1.2.3-0
- Updated to latest upstream release: 1.2.3 (bz 637198)

* Wed Aug 25 2010 Steve Dickson <steved@redhat.com> 1.2.2-7
- When the nfs service is stopped, the RPC svcgssd shutdown fails (bz 627062)

* Mon Aug  2 2010 Steve Dickson <steved@redhat.com> 1.2.2-6
- More initscripts improvement rpcgssd.init and rpcsvcgssd.init (bz 596095)

* Thu Jul 22 2010 Steve Dickson <steved@redhat.com> 1.2.2-5
- Removed the inconsistent default anonuid/anongid values. (bz 566888)
- Created the rpcuser group (bz 594206)

* Thu Jun  3 2010 Steve Dickson <steved@redhat.com> 1.2.2-4
- Turned off root squashing on pseudo roots (bz 599198)

* Tue May 25 2010 Steve Dickson <steved@redhat.com> 1.2.2-3
- Allow mountd to not listen for RPC calls when v2/v3 disabled (bz 538922)
- Added portmap to init script dependencies (bz 583007)
- Added in the mount.nfs4 and umount.nfs4 man pages (bz 528951)
- Did some initscripts improvement (bz 596095)
- Added error message for an invaild mount option value (bz 588886)
- Added error message for an invaild proto option value (bz 588879)

* Fri Apr 16 2010 Steve Dickson <steved@redhat.com> 1.2.2-2
- Updated to latest upstream RC release: 1.2.3-rc2 (bz 583137)

* Fri Apr  9 2010 Steve Dickson <steved@redhat.com> 1.2.2-1
- Updated to latest upstream version: 1.2.2 (bz 580528)

* Fri Feb 12 2010 Steve Dickson <steved@redhat.com> 1.2.1-11
- Removed the idmapd.conf man page which is now part
  of nfs-utils-lib (bz 561504)

* Thu Jan 28 2010 Steve Dickson <steved@redhat.com> 1.2.1-10
- Backed out patch of bz 557704

* Wed Jan 27 2010 Steve Dickson <steved@redhat.com> 1.2.1-9
- mount.nfs: Don't fail mounts when /etc/netconfig is nonexistent
  (bz 557704)

* Mon Jan 25 2010 Steve Dickson <steved@redhat.com> 1.2.1-8
- statd: Teach nfs_compare_sockaddr() to handle NULL 
  arguments (bz 558556)

* Thu Jan 21 2010 Steve Dickson <steved@redhat.com> 1.2.1-7
- mount.nfs: Configuration file parser ignoring options
- mount.nfs: Set the default family for lookups based on 
    defaultproto= setting
- Enabled ipv6  (bz 556484)

* Sun Jan 17 2010 Steve Dickson <steved@redhat.com> 1.2.1-6
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc8
  which includes Ipv6 support for tcpwrapper (disabled by default).

* Sat Jan 16 2010 Steve Dickson <steved@redhat.com> 1.2.1-5
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc7
  which includes Ipv6 support for statd (disabled by default).

* Thu Jan 14 2010 Steve Dickson <steved@redhat.com> 1.2.1-4
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc6
  which fixes bz(479362) and contains the upstream pseudo 
  root release.

* Mon Dec  7 2009 Steve Dickson <steved@redhat.com> 1.2.1-3
- Updated to the latest pseudo root release (rel9).
- mount.nfs: Retry v4 mounts with v3 on ENOENT error

* Fri Nov 20 2009 Steve Dickson <steved@redhat.com> 1.2.1-2
- Fixed a bug in v4root code that was causing ESTALE mounts
  (bz 538609)

* Fri Nov 13 2009  Steve Dickson <steved@redhat.com> 1.2.1-1
- Updated to latest upstream release 1.2.1
- Updated to the latest pseudo root release (rel8).
- Stop rpc.nfsd from failing to startup when the network
  is down (bz 532270)

* Mon Nov  2 2009 Steve Dickson <steved@redhat.com> 1.2.0-18
- Reworked and remove some of the Default-Start/Stop stanzas
  in the init scripts (bz 531425)

* Thu Oct 22 2009 Steve Dickson <steved@redhat.com> 1.2.0-17
- Updated to the latest pseudo root release (rel7).
- Added upstream 1.2.1-rc7 patch which fixes:
   - Stop ignoring the -o v4 option (bz 529407)
   - Allow network protocol roll backs when proto is set
      in the config file (bz 529864)

* Fri Oct  2 2009 Steve Dickson <steved@redhat.com> 1.2.0-16
- Fixed a whole where '-o v4' was not overriding the
  version in the conf file.

* Wed Sep 30 2009 Steve Dickson <steved@redhat.com> 1.2.0-14
- Change the nfsmount.conf file to define v3 as the default 
  protocol version.
- Make sure versions set on the command line override version
  set in nfsmount.conf
- Make version rollbacks still work when versions are set in
  nfsmount.conf

* Tue Sep 29 2009 Steve Dickson <steved@redhat.com> 1.2.0-13
- Added upstream 1.2.1-rc5 patch
  - mount.nfs: Support negotiation between v4, v3, and v2
  - mount.nfs: Keep server's address in nfsmount_info
  - mount.nfs: Sandbox each mount attempt
  - mount.nfs: Support negotiation between v4, v3, and v2

* Wed Sep 23 2009 Steve Dickson <steved@redhat.com> 1.2.0-12
- Updated to the latest pseudo root release (rel6).

* Tue Sep 15 2009 Steve Dickson <steved@redhat.com> 1.2.0-11
- Added upstream 1.2.1-rc5 patch
  - Added --sort --list functionality to nfs-iostat.py
  - Fixed event handler in idmapd
  - Added -o v4 support
  - Disabled IPv6 support in nfsd
  - Don't give client an empty flavor list
  - Fixed gssed so it does not blindly caches machine credentials

* Mon Aug 17 2009 Steve Dickson <steved@redhat.com> 1.2.0-10
- Added upstream 1.2.1-rc4 patch
  - Fix bug when both crossmnt
  - nfs(5): Add description of lookupcache mount option
  - nfs(5): Remove trailing blanks
  - Added nfs41 support to nfssat
  - Added support for mount to us a configuration file.

* Fri Aug 14 2009 Steve Dickson <steved@redhat.com> 1.2.0-9
- Added upstream 1.2.1-rc3 patch
  - Add IPv6 support to nfsd
  - Allow nfssvc_setfds to properly deal with AF_INET6
  - Convert nfssvc_setfds to use getaddrinfo
  - Move check for active knfsd to helper function
  - Declare a static common buffer for nfssvc.c routine
  - Convert rpc.nfsd to use xlog() and add --debug and --syslog options

* Tue Jul 28 2009 Steve Dickson <steved@redhat.com> 1.2.0-8
- Fixed 4.1 versioning problem (bz 512377)

* Wed Jul 15 2009 Steve Dickson <steved@redhat.com> 1.2.0-7
- Added upstream 1.2.1-rc2 patch
  - A large number of mount command changes.

* Mon Jul 13 2009 Steve Dickson <steved@redhat.com> 1.2.0-6
- Added NFSD v4 dynamic pseudo root patch which allows
  NFS v3 exports to be mounted by v4 clients.

* Mon Jun 29 2009 Steve Dickson <steved@redhat.com> 1.2.0-5
- Stopped rpc.idmapd from spinning (bz 508221)

* Mon Jun 22 2009 Steve Dickson <steved@redhat.com> 1.2.0-4
- Added upstream 1.2.1-rc1 patch 
  - Fix to check in closeall()
  - Make --enable-tirpc the default
  - Set all verbose types in gssd daemons
  - Retry exports if getfh() fails

* Wed Jun 10 2009 Steve Dickson <steved@redhat.com> 1.2.0-3
- Updated init scripts to add dependencies
  on other system facilities (bz 475133)

* Wed Jun 10 2009 Steve Dickson <steved@redhat.com> 1.2.0-2
- nfsnobody gid is wrong (bz 485379)

* Tue Jun  2 2009 Steve Dickson <steved@redhat.com> 1.2.0-1
- Updated to latest upstream release: 1.2.0

* Tue May 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.6-4
- Replace the Sun RPC license with the BSD license, with the explicit permission of Sun Microsystems

* Mon May 18 2009 Steve Dickson <steved@redhat.com> 1.1.6-3
- Added upstream 1.1.7-rc1 patch 
  - utils/nfsd: add support for minorvers4
  - sm-notify: Don't orphan addrinfo structs
  - sm-notify: Failed DNS lookups should be retried
  - mount: remove legacy version of nfs_name_to_address()
  - compiling error in rpcgen
  - nfs-utils: Fix IPv6 support in support/nfs/rpc_socket.c
  - umount.nfs: Harden umount.nfs error reportin

* Mon Apr 27 2009 Steve Dickson <steved@redhat.com> 1.1.6-2
- nfslock.init: options not correctly parsed (bz 459591)

* Mon Apr 20 2009 Steve Dickson <steved@redhat.com> 1.1.6-1
- Updated to latest upstream release: 1.1.6

* Mon Mar 23 2009 Steve Dickson <steved@redhat.com> 1.1.5-4
- Added upstream rc3 patch
  - gssd: initialize fakeseed in prepare_krb5_rfc1964_buffer
  - gssd: NULL-terminate buffer after read in read_service_info (try #2)
  - gssd: free buffer allocated by gssd_k5_err_msg
  - gssd: fix potential double-frees in gssd
  - Removed a number of warn_unused_result warnings

* Mon Mar 16 2009 Steve Dickson <steved@redhat.com> 1.1.5-3
- Added upstream rc2 patch

* Fri Mar  6 2009 Steve Dickson <steved@redhat.com> 1.1.5-2
- Fixed lockd not using settings in sysconfig/nfs (bz 461043)
- Fixed some lost externs in the tcpwrapper code

* Thu Mar  5 2009 Steve Dickson <steved@redhat.com> 1.1.5-1
- Updated to latest upstream version: 1.1.5

* Wed Mar  4 2009 Steve Dickson <steved@redhat.com> 1.1.4-21
- configure: fix AC_CACHE_VAL warnings

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Steve Dickson <steved@redhat.com> 1.1.4-19
- Exportfs and rpc.mountd optimalization (bz 76643)

* Tue Feb 17 2009 Steve Dickson <steved@redhat.com> 1.1.4-18
- umount.nfs command: Add an AF_INET6-capable version of nfs_call_unmount()
- umount.nfs command: Support AF_INET6 server addresses
- umount command: remove do_nfs_umount23 function

* Tue Feb 17 2009 Steve Dickson <steved@redhat.com> 1.1.4-17
- Integrated the upstream fix for bz 483375
- mount: segmentation faults on UDP mounts (bz 485448)

* Sat Jan 31 2009 Steve Dickson <steved@redhat.com> 1.1.4-16
- Fixed typo in -mount-textbased.patch (bz 483375)

* Sat Jan 31 2009 Steve Dickson <steved@redhat.com> 1.1.4-15
- Reworked tcp wrapper code to correctly use API (bz 480223)
- General clean up of tcp wrapper code.

* Tue Jan 27 2009 Steve Dickson <steved@redhat.com> 1.1.4-14
- text-based mount command: make po_rightmost() work for N options
- text-based mount command: Function to stuff "struct pmap" from mount options
- text-based mount options: Use new pmap stuffer when	rewriting mount options
- text-based mount command: fix mount option rewriting logic
- text-based mount command: support AF_INET6 in rewrite_mount_options()

* Tue Jan 20 2009 Steve Dickson <steved@redhat.com> 1.1.4-13
- mountd: Don't do tcp wrapper check when there are no rules (bz 448898)

* Wed Jan  7 2009 Steve Dickson <steved@redhat.com> 1.1.4-12
- configure: Remove inet_ntop(3) check from configure.ac
- configure: Add new build option "--enable-tirpc"
- showmount command: Quiesce warning when TI-RPC is disabled

* Sat Jan  3 2009 Steve Dickson <steved@redhat.com> 1.1.4-11
- Added warnings to tcp wrapper code when mounts are 
  denied due to misconfigured DNS configurations.
- gssd: By default, don't spam syslog when users' credentials expire
- mount: revert recent fix for build problems on old systems
- mount: use gethostbyname(3) when building on old systems
- mount: getport: don't use getaddrinfo(3) on old systems
- mount: Random clean up
- configure: use "--disable-uuid" instead of	"--without-uuid"

* Fri Dec 19 2008 Steve Dickson <steved@redhat.com> 1.1.4-10
- Re-enabled and fixed/enhanced tcp wrappers.

* Wed Dec 17 2008 Steve Dickson <steved@redhat.com> 1.1.4-9
- text-based mount command: add function to parse numeric mount options
- text-based mount command: use po_get_numeric() for handling retry
- sm-notify command: fix a use-after-free bug
- statd: not unlinking host files

* Thu Dec 11 2008 Steve Dickson <steved@redhat.com> 1.1.4-8
- mount command: AF_INET6 support for probe_bothports()
- mount command: support AF_INET6 in probe_nfsport() and probe_mntport()
- mount command: full support for AF_INET6 addresses in probe_port()
- gssd/svcgssd: add support to retrieve actual context expiration
- svcgssd: use the actual context expiration for cache

* Sat Dec  6 2008 Steve Dickson <steved@redhat.com> 1.1.4-7
- sm-notify: always exiting without any notification.

* Tue Dec  2 2008 Steve Dickson <steved@redhat.com> 1.1.4-6
- mount command: remove local getport() implementation
- mount command: Replace clnt_ping() and getport() calls in probe_port()
- mount command: Use nfs_error() instead of perror()
- mount command: Use nfs_pmap_getport() in probe_statd()

* Mon Dec  1 2008 Steve Dickson <steved@redhat.com> 1.1.4-5
- Make sure /proc/fs/nfsd exists when the nfs init script
  does the exports (bz 473396)
- Fixed typo in nfs init script that caused rpc.rquotad daemons
  to be started but not stoppped (bz 473929)

* Wed Nov 26 2008 Steve Dickson <steved@redhat.com> 1.1.4-4
- gssd: unblock DNOTIFY_SIGNAL in case it was blocked
- Ensure statd gets started if required when non-root
  user mounts an NFS filesystem

* Tue Nov 25 2008 Steve Dickson <steved@redhat.com> 1.1.4-3
- Give showmount support for querying via rpcbindv3/v4 

* Tue Nov 18 2008 Steve Dickson <steved@redhat.com> 1.1.4-2
- Add AF_INET6-capable API to acquire an RPC CLIENT
- Introduce rpcbind client utility functions

* Sat Oct 18 2008 Steve Dickson <steved@redhat.com> 1.1.4-1
- Updated to latest upstream version: 1.1.4

* Tue Oct 14 2008 Steve Dickson <steved@redhat.com> 1.1.3-6
- sm-notify exists when there are no hosts to notify

* Thu Sep 18 2008 Steve Dickson <steved@redhat.com> 1.1.3-5
- Reworked init scripts so service will be able to
  stop when some of the checks fail. (bz 462508)
- Pre-load nfsd when args to rpc.nfsd are given (bz 441983)

* Thu Aug 28 2008 Steve Dickson <steved@redhat.com> 1.1.3-4
- Added in a number of up upstream patches (101 thru 110).

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.3-3
- fix license tag

* Thu Jul 31 2008 Steve Dickson <steved@redhat.com> 1.1.3-2
- Mount command did not compile against older glibc versions.

* Mon Jul 28 2008 Steve Dickson <steved@redhat.com> 1.1.3-1
- Updated to latest upstream version: 1.1.3

* Wed Jul  2 2008 Steve Dickson <steved@redhat.com> 1.1.2-12
- Changed the default directories for sm-notify (bz 435480)
- Added 'condstop' to init scripts so service are not
  started when nfs-utils is removed.

* Mon Jun 30 2008 Dennis Gilmore <dennis@ausil.us> 1.1.2-11
- add sparc arch handling 

* Mon Jun 30 2008 Steve Dickson <steved@redhat.com>  1.1.2-10
- Rebuild for the updated libevent lib.

* Fri Jun 27 2008 Steve Dickson <steved@redhat.com>  1.1.2-9
- Removed the nfslock service start/stop from %%post section 
  (bz 453046)

* Wed Jun 25 2008 Steve Dickson <steved@redhat.com>  1.1.2-8
- FQDNs in the rmtab causes exportfs to seg fault (bz 444275)

* Mon Jun 23 2008 Steve Dickson <steved@redhat.com>  1.1.2-7
- Added -D_FILE_OFFSET_BITS=64 to CFLAGS
- make nfsstat read and print stats as unsigned integers
- Added (but not installed) the mountstats and nfs-iostat
  python scripts.

* Fri Jun  6 2008 Steve Dickson <steved@redhat.com>  1.1.2-6
- Added 5 (111 thru 115) upstream patches that fixed
  things mostly in the text mounting code.

* Thu May  8 2008 Steve Dickson <steved@redhat.com>  1.1.2-5
- Added 10 (101 thru 110) upstream patches that fixed
  things mostly in the mount and gssd code.

* Wed May  7 2008 Steve Dickson <steved@redhat.com>  1.1.2-4
- Added ppc arch to the all_32bit_archs list (bz 442847)

* Wed Apr 23 2008 Steve Dickson <steved@redhat.com>  1.1.2-3
- Documented how to turn off/on protocol support for
  rpc.nfsd in /etc/sysconfig/nfs (bz443625)
- Corrected the nfslock initscript 'status' return code (bz 441605)
- Removed obsolete code from the nfslock initscript (bz 441604)

* Mon Apr 14 2008 Steve Dickson <steved@redhat.com>  1.1.2-2
- Make EACCES a non fatal error (bz 439807)

* Tue Mar 25 2008 Steve Dickson <steved@redhat.com>  1.1.2-1
- Upgrade to nfs-utils-1.1.2

* Mon Mar  3 2008 Steve Dickson <steved@redhat.com>  1.1.1-5
- Stopped mountd from incorrectly logging an error
  (commit 9dd9b68c4c44f0d9102eb85ee2fa36a8b7f638e3)
- Stop gssd from ignoring the machine credential caches
  (commit 46d439b17f22216ce8f9257a982c6ade5d1c5931)
- Fixed typo in the nfsstat command line arugments.
  (commit acf95d32a44fd8357c24e8a04ec53fc6900bfc58)
- Added test to stop buffer overflow in idmapd
  (commit bcd0fcaf0966c546da5043be700587f73174ae25)

* Sat Feb  9 2008 Steve Dickson <steved@redhat.com>  1.1.1-4
- Cleaned up some typos that were found in the various
  places in the mountd code

* Thu Jan 24 2008 Steve Dickson <steved@redhat.com>  1.1.1-3
- Added in relatime mount option so mount.nfs stays
  compatible with the mount command in util-linux-ng (bz 274301)

* Tue Jan 22 2008 Steve Dickson <steved@redhat.com>  1.1.1-2
- Added -S/--since to the nfsstat(1) manpage
- The wording in the exportfs man page can be a bit confusing, implying
  that "exportfs -u :/foo" will unexport /foo from all hosts, which it won't
- Removed nfsprog option since the kernel no longer supports it.
- Removed mountprog option since the kernel no longer supports it.
- Stop segfaults on amd64 during warnings messages.
- Fix bug when both crossmnt and fsid are set.

* Sat Jan  5 2008 Steve Dickson <steved@redhat.com>  1.1.1-1
- Updated to latest upstream release, nfs-utils-1.1.1
- Added the removal of sm-notify.pid to nfslock init script.
- Changed spec file to use condrestart instead of condstop
  when calling init scripts.
- Fixed typo in rpc.mountd man page 
- Turn on 'nohide' automatically for all refer exports (bz 313561)

* Tue Dec 04 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.1.0-7
 - Rebuild for openldap bump

* Wed Oct 17 2007 Steve Dickson <steved@redhat.com>  1.1.0-6
- Switch the libgssapi dependency to libgssglue

* Fri Sep 14 2007 Steve Dickson <steved@redhat.com>  1.1.0-5
- Changed the default paths in sm-notify to 
  /var/lib/nfs/statd (bz 258461)
- Updated exportfs manpage (bz 262861)

* Wed Aug 15 2007 Steve Dickson <steved@redhat.com>  1.1.0-4
- Make sure the open() system calling in exportfs uses
  mode bits when creating the etab file (bz 252440).

* Mon Aug 13 2007 Steve Dickson <steved@redhat.com>  1.1.0-3
- Added nosharecache mount option which re-enables
  rw/ro mounts to the same server (bz 243913).

* Thu Aug  2 2007 Steve Dickson <steved@redhat.com>  1.1.0-2
- Make sure the gss and idmap daemons remove thier lock
  files when they are stopped.

* Sat Jul 28 2007 Steve Dickson <steved@redhat.com>  1.1.0-1
- Upgraded to the latest upstream version (nfs-utils-1.1.0)

* Thu May 24 2007 Steve Dickson <steved@redhat.com> 1.0.10-7
- Fixed typo in mount.nfs4 that causes a segfault during
  error processing (bz 241190)

* Tue May 22 2007 Steve Dickson <steved@redhat.com> 1.0.10-6
- Make sure the condrestarts exit with a zero value (bz 240225)
- Stopped /etc/sysconfig/nfs from being overwritten on updates (bz 234543)
- Added -o nordirplus mount option to disable READDIRPLUS (bz 240357)
- Disabled the FSCache patch, for now... 

* Wed May 10 2007 Steve Dickson <steved@redhat.com> 1.0.12-5
- Fix mount.nfs4 to display correct error message (bz 227212)
- Updated mountd and showmount reverse lookup flags (bz 220772)
- Eliminate timeout on nfsd shutdowns (bz 222001)
- Eliminate memory leak in mountd (bz 239536)
- Make sure statd uses correct uid/gid by chowning
  the /var/lib/nfs/statd with the rpcuser id. (bz 235216)
- Correct some sanity checking in rpc.nfsd. (bz 220887) 
- Added missing unlock_mtab() call in moutnd
- Have mountd hold open etab file to force inode number to change (bz 236823)
- Create a /etc/sysconfig/nfs with all the possible init script
  variables (bz 234543)
- Changed nfs initscript to exit with correct value (bz 221874)

* Tue Apr  3 2007 Steve Dickson <steved@redhat.com> 1.0.12-4
- Replace portmap dependency with an rpcbind dependency (bz 228894)

* Mon Mar 12 2007 Steve Dickson <steved@redhat.com> 1.0.12-3
- Incorporated Merge Review comments (bz 226198)

* Fri Mar  9 2007 Steve Dickson <steved@redhat.com> 1.0.12-2
- Added condstop to all the initscripts (bz 196934)
- Made no_subtree_check a default export option (bz 212218)

* Tue Mar  6 2007 Steve Dickson <steved@redhat.com> 1.0.12-1
- Upgraded to 1.0.12 
- Fixed typo in Summary.

* Thu Mar  1 2007 Karel Zak <kzak@redhat.com>  1.0.11-2
- Fixed mount.nfs -f (fake) option (bz 227988)

* Thu Feb 22 2007 Steve Dickson <steved@redhat.com> 1.0.11-1
- Upgraded to 1.0.11 

* Wed Feb 21 2007 Steve Dickson <steved@redhat.com> 1.0.10-7
- Added FS_Location support

* Mon Dec 18 2006 Karel Zak <kzak@redhat.com> 1.0.10-6
- add support for mount options that contain commas (bz 219645)

* Wed Dec 13 2006 Steve Dickson <steved@redhat.com> 1.0.10-5
- Stopped v4 umounts from ping rpc.mountd (bz 215553)

* Wed Nov 28 2006 Steve Dickson <steved@redhat.com> 1.0.10-4
- Doing a connect on UDP sockets causes the linux network
  stack to reject UDP patches from multi-home server with
  nic on the same subnet. (bz 212471)

* Wed Nov 15 2006 Steve Dickson <steved@redhat.com> 1.0.10-3
- Removed some old mounting versioning code that was
  stopping tcp mount from working (bz 212471)

* Tue Oct 31 2006 Steve Dickson <steved@redhat.com> 1.0.10-2
- Fixed -o remount (bz 210346)
- fix memory leak in rpc.idmapd (bz 212547)
- fix use after free bug in dirscancb (bz 212547)
- Made no_subtree_check a default export option (bz 212218)

* Wed Oct 25 2006 Steve Dickson <steved@redhat.com> 1.0.10-1
- Upgraded to 1.0.10 

* Mon Oct 16 2006 Steve Dickson <steved@redhat.com> 1.0.9-10
- Fixed typo in nfs man page (bz 210864).

* Fri Oct 13 2006 Steve Dickson <steved@redhat.com> 1.0.9-9
- Unable to mount NFS V3 share where sec=none is specified (bz 210644)

* Tue Sep 26 2006 Steve Dickson <steved@redhat.com> 1.0.9-8
- mount.nfs was not returning a non-zero exit value 
  on failed mounts (bz 206705)

* Wed Sep 20 2006 Karel Zak <kzak@redhat.com> 1.0.9-7
- Added support for the mount -s (sloppy) option (#205038)
- Added nfs.5 man page from util-linux
- Added info about [u]mount.nfs to the package description

* Mon Sep 11 2006  <SteveD@RedHat.com> 1.0.9-6
- Removed the compiling of getiversion and getkversion since
  UTS_RELEASE is no longer defined and these binary are
  not installed.

* Fri Aug 18 2006 <SteveD@RedHat.com> 1.0.9-5
- Changed gssd daemons to cache things in memory
  instead of /tmp which makes selinux much happier.
  (bz 203078)

* Wed Aug 16 2006 <SteveD@RedHat.com> 1.0.9-4
- Allow variable for HA callout program in /etc/init.d/nfslock
  (bz 202790)

* Wed Aug 02 2006 <wtogami@redhatcom> 1.0.9-3
- add epoch (#196359)

* Fri Jul 28 2006 <SteveD@RedHat.com> 1.0.9-2
- Enabled the creating of mount.nfs and umount.nfs binaries
- Added mount option fixes suggested by upstream.
- Fix lazy umounts (bz 169299)
- Added -o fsc mount option.

* Mon Jul 24 2006 <SteveD@RedHat.com> 1.0.9-1
- Updated to 1.0.9 release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0.8-5.1
- rebuild

* Sun Jul  2 2006 <jkeating@redhat.com> 1:1.0.8-5
- Introduce epoch to fix upgrade path

* Sat Jul  1 2006 <SteveD@RedHat.com> 1.0.8-3
- Fixed typos in /etc/rc.d/init.d/nfs file (bz 184486)

* Fri Jun 30 2006 <SteveD@RedHat.com> 1.0.8-3
- Split the controlling of nfs version, ports, and protocol 
  into two different patches
- Fixed and added debugging statements to rpc.mountd.
- Fixed -p arg to work with priviledged ports (bz 156655)
- Changed nfslock initscript to set LOCKD_TCPPORT and
  LOCKD_UDPPORT (bz 162133)
- Added MOUNTD_NFS_V1 variable to version 1 of the
  mount protocol can be turned off. (bz 175729)
- Fixed gssd to handel mixed case characters in
  the domainname. (bz 186069)

* Wed Jun 21 2006 <SteveD@RedHat.com> 1.0.8-2
- Updated to nfs-utils-1.0.8

* Thu Jun  8 2006 <SteveD@RedHat.com> 1.0.8.rc4-1
- Upgraded to the upstream 1.0.8.rc4 version

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.8.rc2-4.FC5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.8.rc2-4.FC5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 20 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-4.FC5
- Added new libnfsidmap call, nfs4_set_debug(), to rpc.idmapd
  which turns on debugging in the libarary.

* Mon Jan 16 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-3.FC5
- Added innetgr patch that changes configure scripts to 
  check for the innetgr function. (bz 177899)

* Wed Jan 11 2006 Peter Jones <pjones@redhat.com> 1.0.8.rc2-2.FC5
- Fix lockfile naming in the initscripts so they're stopped correctly.

* Mon Jan  9 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-1.FC5
- Updated to 1.0.8-rc2 release
- Broke out libgssapi into its own rpm
- Move librpcsecgss and libnfsidmap in the new nfs-utils-lib rpm
- Removed libevent code; Required to be installed.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Oct 23 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-19
- Updated to latest code in SourceForge CVS
- Updated to latest CITI patches (1.0.7-4)
- Fix bug in nfsdreopen by compiling in server defaults

* Thu Sep 22 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-18
- Updated libnfsidmap to 0.11
- Updated libgssapi to 0.5
- Made sure the gss daemons and new libs are
  all using the same include files.
- Removed code from the tree that is no longer used.
- Add ctlbits patch that introduced the -N -T and -U
  command line flags to rpc.nfsd.

* Sun Sep 18 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-17
- Updated to latest nfs-utils code in upstream CVS tree
- Updated libevent from 1.0b to 1.1a
- Added libgssapi-0.4 and librpcsecgss-0.6 libs from CITI

* Tue Sep  8 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-16
- Reworked the nfslock init script so if lockd is running
  it will be killed which is what the HA community needs. (bz 162446)
- Stopped rpcidmapd.init from doing extra echoing when
  condstart-ed.

* Wed Aug 24 2005 Peter Jones <pjones@redhat.com> - 1.0.7-15
- don't strip during "make install", so debuginfo packages are generated right

* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- no need to still keep a requirement for kernel-2.2 or newer

* Tue Aug 16 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-13
- Changed mountd to use stat64() (bz 165062)

* Tue Aug  2 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-12
- Changed useradd to use new -l flag (bz149407)
- 64bit fix in gssd code (bz 163139)
- updated broken dependencies
- updated rquotad to compile with latest
  quota version.

* Thu May 26 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-8
- Fixed subscripting problem in idmapd (bz 158188)

* Thu May 19 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-7
- Fixed buffer overflow in rpc.svcgssd (bz 114288)

* Wed Apr 13 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-6
- Fixed misformated output from nfslock script (bz 154648)

* Mon Mar 29 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-4
- Fixed a compile error on x86_64 machines in the gss code.
- Updated the statd-notify-hostname.patch to eliminate 
  a segmentation fault in rpc.statd when an network 
  interface was down. (bz 151828)

* Sat Mar 19 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-3
- Changed xlog to use LOG_INFO instead of LOG_DEBUG
  so debug messages will appear w/out any config
  changes to syslog.conf.
- Reworked how /etc/exports is setup (bz 151389)

* Wed Mar  2 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-2
- Tied the rpcsecgss debugging in with gssd and
  svcgssd debugging

* Mon Feb 14 2005 Steve Dickson <SteveD@RedHat.com>
- Added support to rpcgssd.init and rpcsvcgssd.init scripts
  to insmod security modules.
- Changed the nfs.init script to bring rpc.svcgssd up and down,
  since rpc.svcgssd is only needed with the NFS server is running.

* Tue Dec 14 2004 Steve Dickson <SteveD@RedHat.com>
- Fix problem in idmapd that was causing "xdr error 10008"
  errors (bz 142813)
- make sure the correct hostname is used in the SM_NOTIFY
  message that is sent from a rebooted server which has 
  multiple network interfaces. (bz 139101)

- Changed nfslock to send lockd a -KILL signal
  when coming down. (bz 125257)

* Thu Nov 11 2004 Steve Dickson <SteveD@RedHat.com>
- Replaced a memcopy with explicit assignments
  in getquotainfo() of rquotad to fix potential overflow
  that can occur on 64bit machines. (bz 138068)

* Mon Nov  8 2004 Steve Dickson <SteveD@RedHat.com>
- Updated to latest sourceforge code
- Updated to latest CITIT nfs4 patches

* Sun Oct 17 2004 Steve Dickson <SteveD@RedHat.com>
- Changed nfs.init to bring down rquotad correctly
  (bz# 136041)

* Thu Oct 14 2004 Steve Dickson <SteveD@RedHat.com>
- Added "$RQUOTAD_PORT" variable to nfs.init which
  allows the rpc.rquotad to use a predefined port
  (bz# 124676)

* Fri Oct  1 2004 <SteveD@RedHat.com
- Incorporate some clean up code from Ulrich Drepper (bz# 134025)
- Fixed the chkconfig number in the rpcgssd, rpcidmapd, and 
  rpcsvcgssd initscrpts (bz# 132284)

* Fri Sep 24 2004 <SteveD@RedHat.com>
- Make sure the uid/gid of nfsnobody is the
  correct value for all archs (bz# 123900)
- Fixed some security issues found by SGI (bz# 133556)

* Mon Aug 30 2004 Steve Dickson <SteveD@RedHat.com>
- Major clean up. 
- Removed all unused/old patches
- Rename and condensed a number of patches
- Updated to CITI's nfs-utils-1.0.6-13 patches

* Tue Aug 10 2004 Bill Nottingham <notting@redhat.com>
- move if..fi condrestart stanza to %%postun (#127914, #128601)

* Wed Jun 16 2004 <SteveD@RedHat.com>
- nfslock stop is now done on package removals
- Eliminate 3 syslog messages that are logged for
  successful events.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 14 2004 <SteveD@RedHat.com>
- Fixed syntax error in nfs initscripts when
  NETWORKING is not defined
- Removed sync warning on readonly exports.
- Changed run levels in rpc initscripts.
- Replaced modinfo with lsmod when checking
  for loaded modules.

* Tue Jun  1 2004 <SteveD@RedHat.com>
- Changed the rpcgssd init script to ensure the 
  rpcsec_gss_krb5 module is loaded

* Tue May 18 2004 <SteveD@RedHat.com>
- Removed the auto option from MOUNTD_NFS_V2 and
  MOUNTD_NFS_V3 variables. Since v2 and v3 are on
  by default, there only needs to be away of 
  turning them off.

* Thu May 10 2004 <SteveD@RedHat.com>
- Rebuilt

* Thu Apr 15 2004 <SteveD@RedHat.com>
- Changed the permission on idmapd.conf to 644
- Added mydaemon code to svcgssd
- Updated the add_gssd.patch from upstream

* Wed Apr 14 2004 <SteveD@RedHat.com>
- Created a pipe between the parent and child so 
  the parent process can report the correct exit
  status to the init scripts
- Added SIGHUP processing to rpc.idmapd and the 
  rpcidmapd init script.

* Mon Mar 22 2004 <SteveD@RedHat.com>
- Make sure check_new_cache() is looking in the right place 

* Wed Mar 17 2004 <SteveD@RedHat.com>
- Changed the v4 initscripts to use $prog for the
  arugment to daemon

* Tue Mar 16 2004 <SteveD@RedHat.com>
- Made the nfs4 daemons initscripts work better when 
  sunrpc is not a module
- added more checks to see if modules are being used.

* Mon Mar 15 2004 <SteveD@RedHat.com>
- Add patch that sets up gssapi_mech.conf correctly

* Fri Mar 12 2004 <SteveD@RedHat.com>
- Added the shutting down of the rpc v4 daemons.
- Updated the Red Hat only patch with some init script changes.

* Thu Mar 11 2004 Bill Nottingham <notting@redhat.com>
- rpc_pipefs mounting and aliases are now in modutils; require that

* Thu Mar 11 2004 <SteveD@RedHat.com>
- Updated the gssd patch.

* Sun Mar  7 2004 <SteveD@RedHat.com>
- Added the addition and deletion of rpc_pipefs to /etc/fstab
- Added the addition and deletion of module aliases to /etc/modules.conf

* Mon Mar  1 2004 <SteveD@RedHat.com>
- Removed gssd tarball and old nfsv4 patch.
- Added new nfsv4 patches that include both the
   gssd and idmapd daemons
- Added redhat-only v4 patch that reduces the
   static librpc.a to only contain gss rpc related
   routines (I would rather have gssd use the glibc 
   rpc routines)
-Changed the gssd svcgssd init scripts to only
   start up if SECURE_NFS is set to 'yes' in
   /etc/sysconfig/nfs

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Thomas Woerner <twoerner@redhat.com>
- make rpc.lockd, rpc.statd, rpc.mountd and rpc.nfsd pie

* Wed Jan 28 2004 Steve Dickson <SteveD@RedHat.com>
- Added the NFSv4 bits

* Mon Dec 29 2003 Steve Dickson <SteveD@RedHat.com>
- Added the -z flag to nfsstat

* Wed Dec 24 2003  Steve Dickson <SteveD@RedHat.com>
- Fixed lockd port setting in nfs.int script

* Wed Oct 22 2003 Steve Dickson <SteveD@RedHat.com>
- Upgrated to 1.0.6
- Commented out the acl path for fedora

* Thu Aug  27 2003 Steve Dickson <SteveD@RedHat.com>
- Added the setting of lockd ports via sysclt interface
- Removed queue setting code since its no longer needed

* Thu Aug  7 2003 Steve Dickson <SteveD@RedHat.com>
- Added back the acl patch Taroon b2

* Wed Jul 23 2003 Steve Dickson <SteveD@RedHat.com>
- Commented out the acl patch (for now)

* Wed Jul 21 2003 Steve Dickson <SteveD@RedHat.com>
- Upgrated to 1.0.5

* Wed Jun 18 2003 Steve Dickson <SteveD@RedHat.com>
- Added security update
- Fixed the drop-privs.patch which means the chroot
patch could be removed.

* Mon Jun  9 2003 Steve Dickson <SteveD@RedHat.com>
- Defined the differ kinds of debugging avaliable for mountd in
the mountd man page. 

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Steve Dickson <SteveD@RedHat.com>
- Upgraded to 1.0.3 
- Fixed numerous bugs in init scrips
- Added nfsstat overflow patch

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 1.0.1-2.9
- rebuild

* Fri Dec 13 2002 Daniel J Walsh <dwalsh@redhat.com>
- change init script to not start rpc.lock if already running

* Wed Dec 11 2002 Daniel J Walsh <dwalsh@redhat.com>
- Moved access code to be after dropping privs

* Mon Nov 18 2002 Stephen C. Tweedie <sct@redhat.com>
- Build with %%configure
- Add nhfsgraph, nhfsnums and nhfsrun to the files list

* Mon Nov 11 2002 Stephen C. Tweedie <sct@redhat.com>
- Don't drop privs until we've bound the notification socket

* Thu Nov  7 2002 Stephen C. Tweedie <sct@redhat.com>
- Ignore SIGPIPE in rpc.mountd

* Thu Aug  1 2002 Bob Matthews <bmatthews@redhat.com>
- Add Sean O'Connell's <sean@ee.duke.edu> nfs control tweaks
- to nfs init script.

* Mon Jul 22 2002 Bob Matthews <bmatthews@redhat.com>
- Move to nfs-utils-1.0.1

* Mon Feb 18 2002 Bob Matthews <bmatthews@redhat.com>
- "service nfs restart" should start services even if currently 
-   not running (#59469)
- bump version to 0.3.3-4

* Wed Oct  3 2001 Bob Matthews <bmatthews@redhat.com>
- Move to nfs-utils-0.3.3
- Make nfsnobody a system account (#54221)

* Tue Aug 21 2001 Bob Matthews <bmatthews@redhat.com>
- if UID 65534 is unassigned, add user nfsnobody (#22685)

* Mon Aug 20 2001 Bob Matthews <bmatthews@redhat.com>
- fix typo in nfs init script which prevented MOUNTD_PORT from working (#52113)

* Tue Aug  7 2001 Bob Matthews <bmatthews@redhat.com>
- nfs init script shouldn't fail if /etc/exports doesn't exist (#46432)

* Fri Jul 13 2001 Bob Matthews <bmatthews@redhat.com>
- Make %%pre useradd consistent with other Red Hat packages.

* Tue Jul 03 2001 Michael K. Johnson <johnsonm@redhat.com>
- Added sh-utils dependency for uname -r in nfs init script

* Tue Jun 12 2001 Bob Matthews <bmatthews@redhat.com>
- make non RH kernel release strings scan correctly in 
-   nfslock init script (#44186)

* Mon Jun 11 2001 Bob Matthews <bmatthews@redhat.com>
- don't install any rquota pages in _mandir: (#39707, #44119)
- don't try to manipulate rpc.rquotad in init scripts 
-   unless said program actually exists: (#43340)

* Tue Apr 10 2001 Preston Brown <pbrown@redhat.com>
- don't translate initscripts for 6.x

* Tue Apr 10 2001 Michael K. Johnson <johnsonm@redhat.com>
- do not start lockd on kernel 2.2.18 or higher (done automatically)

* Fri Mar 30 2001 Preston Brown <pbrown@redhat.com>
- don't use rquotad from here now; quota package contains a version that 
  works with 2.4 (#33738)

* Tue Mar 12 2001 Bob Matthews <bmatthews@redhat.com>
- Statd logs at LOG_DAEMON rather than LOG_LOCAL5
- s/nfs/\$0/ where appropriate in init scripts

* Tue Mar  6 2001 Jeff Johnson <jbj@redhat.com>
- Move to nfs-utils-0.3.1

* Wed Feb 14 2001 Bob Matthews <bmatthews@redhat.com>
- #include <time.h> patch

* Mon Feb 12 2001 Bob Matthews <bmatthews@redhat.com>
- Really enable netgroups

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize initscripts

* Fri Jan 19 2001 Bob Matthews <bmatthews@redhat.com>
- Increased {s,r}blen in rpcmisc.c:makesock to accommodate eepro100

* Tue Jan 16 2001 Bob Matthews <bmatthews@redhat.com>
- Hackish fix in build section to enable netgroups

* Wed Jan  3 2001 Bob Matthews <bmatthews@redhat.com>
- Fix incorrect file specifications in statd manpage.
- Require gawk 'cause it's used in nfslock init script.

* Thu Dec 13 2000 Bob Matthews <bmatthews@redhat.com>
- Require sed because it's used in nfs init script

* Tue Dec 12 2000 Bob Matthews <bmatthews@redhat.com>
- Don't do a chroot(2) after dropping privs, in statd.

* Mon Dec 11 2000 Bob Matthews <bmatthews@redhat.com>
- NFSv3 if kernel >= 2.2.18, detected in init script

* Thu Nov 23 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.2.1

* Tue Nov 14 2000 Bill Nottingham <notting@redhat.com>
- don't start lockd on 2.4 kernels; it's unnecessary

* Tue Sep  5 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- more portable fix for mandir

* Sun Sep  3 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to 0.2-release

* Fri Sep  1 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- fix reload script

* Thu Aug 31 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to 0.2 from CVS
- adjust statd-drop-privs patch
- disable tcp_wrapper support

* Wed Aug  2 2000 Bill Nottingham <notting@redhat.com>
- fix stop priority of nfslock

* Tue Aug  1 2000 Bill Nottingham <notting@redhat.com>
- um, actually *include and apply* the statd-drop-privs patch

* Mon Jul 24 2000 Bill Nottingham <notting@redhat.com>
- fix init script ordering (#14502)

* Sat Jul 22 2000 Bill Nottingham <notting@redhat.com>
- run statd chrooted and as non-root
- add prereqs

* Tue Jul 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use "License", not "Copyright"
- use %%{_tmppath} and %%{_mandir}

* Mon Jul 17 2000 Matt Wilson <msw@redhat.com>
- built for next release

* Mon Jul 17 2000 Matt Wilson <msw@redhat.com>
- 0.1.9.1
- remove patch0, has been integrated upstream

* Wed Feb  9 2000 Bill Nottingham <notting@redhat.com>
- the wonderful thing about triggers, is triggers are wonderful things...

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- switch to nfs-utils as the base tree
- fix the statfs patch for the new code base
- single package that obsoletes everything we had before (if I am to keep
  some traces of my sanity with me...)

* Mon Jan 17 2000 Preston Brown <pbrown@redhat.com>
- use statfs syscall instead of stat to determinal optimal blksize
