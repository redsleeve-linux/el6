%define main_release 36

%define samba_version 3.6.23

#%define pre_release rc3
%define pre_release %nil

%define tdb_version 1.2.10
%define talloc_version 2.0.7
%define tevent_version 0.9.18

#%define samba_release %{main_release}%{pre_release}%{?dist}
%define samba_release %{main_release}%{?dist}

%define real_name samba
%define samba_source source3

%global with_vfs_glusterfs 0
# Only enable on x86_64
%ifarch x86_64
%global with_vfs_glusterfs 1
%endif

Summary: Server and Client software to interoperate with Windows machines
Name: samba
Epoch: 0
Version: %{samba_version}
Release: %{samba_release}
License: GPLv3+ and LGPLv3+
Group: System Environment/Daemons
URL: http://www.samba.org/

Source: http://www.samba.org/samba/ftp/samba/samba-%{samba_version}%{pre_release}.tar.bz2

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source3: swat.desktop
Source4: samba.sysconfig
Source5: smb.init
Source6: samba.pamd
Source7: smbprint
Source8: winbind.init
Source9: smb.conf.default
Source10: nmb.init
Source11: pam_winbind.conf

# Don't depend on Net::LDAP
Source999: filter-requires-samba.sh

# Upstream patches
Patch0: samba-3.6.99-fix_nbt_query_with_many_components.patch
Patch1: samba-3.6.99-fix_group_expansion_with_nss_templates.patch
Patch2: samba-3.6.99-fix_group_expansion_in_service_path.patch
Patch3: samba-3.6.99-fix_memleak_in_printer_list.patch
Patch4: samba-3.6.99-fix_lookups_with_one_way_trusts.patch
Patch5: samba-3.6.99-fix_setup_domain_child_logic.patch
Patch6: samba-3.6.99-fix_force_user_with_security_ads.patch
Patch7: samba-3.6.99-add_timeout_option_to_smbclient.patch

# Additional Red Hat patches
Patch100: samba-3.2.0pre1-pipedir.patch
Patch101: samba-3.2.0pre1-grouppwd.patch
Patch102: samba-3.2.5-inotify.patch
Patch103: samba-3.5.11-idmapdebug.patch
Patch104: samba-3.5.11-docs.patch
Patch105: samba-3.5.11-nss_info_doc.patch
Patch106: samba-3.5.11-wbinfo_manpage.patch
Patch107: samba-3.5.12-dns.patch
Patch108: samba-3.5.12-pam_radio_type.patch
Patch109: samba-3.6.18-fix_net_ads_join_segfault.patch
Patch110: samba-3.6.19-valid_users_doc.patch
Patch111: samba-3.6.23-gecos.patch
Patch112: samba-3.6.23-glusterfs.patch
Patch113: samba-3.6.23-libsmbclient.patch
Patch114: samba-3.6.23-fix_libads_krb5_ipv6.patch
Patch115: samba-CVE-2014-0244.patch
Patch116: samba-CVE-2014-3493.patch
Patch117: samba-3.6.26-smb2_case_sensitive.patch
Patch118: samba-3.6.99-fix_gecos_interactive.patch
Patch119: samba-3.6.99-fix_dropbox_share.patch
Patch120: samba-3.6.99-add_spoolss_os_version.patch
Patch121: CVE-2015-0240-3.6.patch
Patch122: samba-3.6.99-nt_printer_publish_guid.patch
Patch123: samba-3.6.99-fix_keytab_null_termination.patch
Patch124: samba-3.6.99-fix_printcap_cpu_utilization.patch
Patch125: samba-3.6.99-fix_smbclient_ntlmv2_auth.patch
Patch126: samba-3.6.99-fix_smb_conf_doc.patch
Patch127: samba-3.6.99-bug-1117059.patch
Patch128: samba-3.6.99-bug-1192211.patch
Patch129: samba-3.6.99-fix_usergroup_cache_lookup.patch
Patch130: samba-3.6.99-fix_force_user_winbind_default_domain.patch
Patch131: samba-3.6.99-fix_rpcclient_timeout_command.patch
Patch132: samba-3.6.99-fix_force_group.patch
Patch133: samba-3.6.99-fix_pam_winbind_parsing_segfault.patch
Patch134: samba-3.6.99-fix_mangling_hash_segfault.patch
Patch135: samba-3.6.99-doc_netbios_name_length_limit.patch
Patch136: samba-3.6.99-fix_map_to_guest_bad_uid.patch
Patch137: samba-3.6.99-fix_security_server_share_access.patch
Patch138: samba-3.6.99-fix_stale_printer_entries_on_rename.patch
Patch139: CVE-2015-5299-v3-6-bso11529.patch
Patch140: CVE-2015-5296-v3-6-bso11536.patch
Patch141: CVE-2015-5252-v3-6-bso11395.patch
Patch142: CVE-2015-5330-v3-6-bso11599.patch
Patch144: samba-3.6.99-net_ads_join_no_dns_updates.patch
Patch145: samba-3.6.99-asserted_identity_sid-S-1-18-1.patch
#Patch146: samba-3.6.99-clidfs.patch
Patch147: CVE-2015-7560-v3-6.patch
Patch148: samba-3.6.99-fix_symlink_verification.patch
Patch149: CVE-preparation-v3-6.patch
Patch150: CVE-2016-2110-v3-6.patch
Patch151: CVE-2016-2111-v3-6.patch
Patch152: CVE-2016-2112-v3-6.patch
Patch153: CVE-2016-2115-v3-6.patch
Patch154: CVE-2016-2118-v3-6.patch
Patch155: CVE-2015-5370-v3-6.patch
Patch156: samba-3.6.99-fix_winbind_cache_memory_leak.patch
Patch157: samba-3.6.99-fix_memleak_winbind_cached_creds.patch

Patch190: doc-update.patch

# This is a backported patch to use epoll on RHEL. We will maintain this
# patch just in our package. It will not be part of a 3.6 release cause it require
# at least libtevent 0.9.18.
Patch200: samba-3.6.x-winbind_tevent_poll.patch

Requires(pre): samba-common = %{epoch}:%{samba_version}-%{release}
Requires(pre): samba-winbind-clients = %{epoch}:%{samba_version}-%{release}
Requires: pam >= 0:0.64
Requires: logrotate >= 0:3.4
BuildRoot: %{_tmppath}/%{name}-%{samba_version}-%{release}-root
Requires(post): /sbin/chkconfig, /sbin/service
Requires(preun): /sbin/chkconfig, /sbin/service
BuildRequires: pam-devel, readline-devel, ncurses-devel, libacl-devel, krb5-devel, openldap-devel, openssl-devel, cups-devel, ctdb-devel
BuildRequires: autoconf, gawk, popt-devel, gtk2-devel, libcap-devel, libuuid-devel
BuildRequires: libtalloc-devel >= %{talloc_version}
BuildRequires: libtevent-devel >= %{tevent_version}
BuildRequires: libtdb-devel >= %{tdb_version}
%if %{with_vfs_glusterfs}
BuildRequires: pkgconfig(glusterfs-api) >= 4
BuildRequires: glusterfs-devel >= 3.4.0.16
%endif

# Working around perl dependency problem from docs
%define __perl_requires %{SOURCE999}


%description

Samba is the suite of programs by which a lot of PC-related machines
share files, printers, and other information (such as lists of
available files and printers). The Windows NT, OS/2, and Linux
operating systems support this natively, and add-on packages can
enable the same thing for DOS, Windows, VMS, UNIX of all kinds, MVS,
and more. This package provides an SMB/CIFS server that can be used to
provide network services to SMB/CIFS clients.
Samba uses NetBIOS over TCP/IP (NetBT) protocols and does NOT
need the NetBEUI (Microsoft Raw NetBIOS frame) protocol.


%package client
Summary: Samba client programs
Group: Applications/System
Requires: samba-common = %{epoch}:%{samba_version}-%{release}
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description client
The samba-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.


%package common
Summary: Files used by both Samba servers and clients
Requires: libtdb >= 0:%{tdb_version}
Requires: libtalloc >= 0:%{talloc_version}
Requires: libtevent >= 0:%{tevent_version}
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}
Group: Applications/System
Requires(pre): /usr/sbin/groupadd
Requires(post): /sbin/chkconfig, /sbin/service, coreutils
Requires(preun): /sbin/chkconfig, /sbin/service

%description common
Samba-common provides files necessary for both the server and client
packages of Samba.


%package winbind
Summary: Samba winbind
Group: Applications/System
Requires: samba-common = %{epoch}:%{samba_version}-%{release}
Requires(pre): /usr/sbin/groupadd
Requires(post): /sbin/chkconfig, /sbin/service, coreutils
Requires(preun): /sbin/chkconfig, /sbin/service
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description winbind
The samba-winbind package provides the winbind daemon and some client tools.
Winbind enables Linux to be a full member in Windows domains and to use
Windows user and group accounts on Linux.


%package winbind-clients
Summary: Samba winbind clients
Group: Applications/System
Requires: samba-winbind = %{epoch}:%{samba_version}-%{release}

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon


%package winbind-devel
Summary: Developer tools for the winbind library
Group: Development
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description winbind-devel
The samba-winbind package provides developer tools for the wbclient library.

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}
Group: Applications/System
Requires: samba-winbind = %{epoch}:%{samba_version}-%{release}
# Handle winbind_krb5_locator.so as alternatives to allow
# IPA AD trusts case where it should not be used by libkrb5
# The plugin will be diverted to /dev/null by the FreeIPA
# freeipa-server-trust-ad subpackage due to higher priority
# and restored to the proper one on uninstall
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives


Requires: samba-winbind = %{epoch}:%{samba_version}-%{release}
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package swat
Summary: The Samba SMB server Web configuration program
Group: Applications/System
Requires: samba = %{epoch}:%{samba_version}-%{release}, xinetd
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description swat
The samba-swat package includes the new SWAT (Samba Web Administration
Tool), for remotely managing Samba's smb.conf file using your favorite
Web browser.


%package doc
Summary: Documentation for the Samba suite
Group: Documentation
Requires: samba-common = %{epoch}:%{samba_version}-%{release}

%description doc
The samba-doc package includes all the non-manpage documentation for the
Samba suite.


%package domainjoin-gui
Summary: Domainjoin GUI
Group: Applications/System
Requires: samba-common = %{epoch}:%{samba_version}-%{release}, gtk2

%description domainjoin-gui
The samba-domainjoin-gui package includes a domainjoin gtk application.


%package -n libsmbclient
Summary: The SMB client library
Group: Applications/System
Requires: samba-winbind-clients = %{epoch}:%{samba_version}-%{release}

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.


%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development
Requires: libsmbclient = %{epoch}:%{samba_version}-%{release}

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.

%if %{with_vfs_glusterfs}
%package glusterfs
Summary: Samba VFS module for GlusterFS
Group: Applications/System
Requires: samba = %{epoch}:%{samba_version}-%{release}
Requires: glusterfs-api >= 3.4.0.16
Requires: glusterfs >= 3.4.0.16

%description glusterfs
Samba VFS module for GlusterFS integration.
%endif

%prep
# TAG: change for non-pre
%setup -q -T -b 0   -n %{real_name}-%{samba_version}%{pre_release}

# copy Red Hat specific scripts
install -d -m0755 packaging/Fedora
cp packaging/RHEL/setup/smbusers packaging/Fedora/
cp %{SOURCE5} packaging/Fedora/
cp %{SOURCE6} packaging/Fedora/
cp %{SOURCE7} packaging/Fedora/
cp %{SOURCE8} packaging/Fedora/winbind.init
cp %{SOURCE9} packaging/Fedora/
cp %{SOURCE10} packaging/Fedora/
cp %{SOURCE11} packaging/Fedora/

# Upstream patches
%patch0 -p1 -b .samba-3.6.99-fix_nbt_query_with_many_components.patch
%patch1 -p1 -b .samba-3.6.99-fix_group_expansion_with_nss_templates.patch
%patch2 -p1 -b .samba-3.6.99-fix_group_expansion_in_service_path.patch
%patch3 -p1 -b .samba-3.6.99-fix_memleak_in_printer_list.patch
%patch4 -p1 -b .samba-3.6.99-fix_lookups_with_one_way_trusts.patch
%patch5 -p1 -b .samba-3.6.99-fix_setup_domain_child_logic.patch
%patch6 -p1 -b .samba-3.6.99-fix_force_user_with_security_ads.patch
%patch7 -p1 -b .samba-3.6.99-add_timeout_option_to_smbclient.patch

# Additional Red Hat patches
%patch100 -p1 -b .samba-3.2.0pre1-pipedir.patch
%patch101 -p1 -b .samba-3.2.0pre1-grouppwd.patch
%patch102 -p1 -b .samba-3.2.5-inotify.patch
%patch103 -p1 -b .samba-3.5.11-idmapdebug.patch
%patch104 -p1 -b .samba-3.5.11-docs.patch
%patch105 -p1 -b .samba-3.5.11-nss_info_doc.patch
%patch106 -p1 -b .samba-3.5.11-wbinfo_manpage.patch
%patch107 -p1 -b .samba-3.5.12-dns.patch
%patch108 -p1 -b .samba-3.5.12-pam_radio_type.patch
%patch109 -p1 -b .samba-3.6.18-fix_net_ads_join_segfault.patch
%patch110 -p1 -b .samba-3.6.19-valid_users_doc.patch
%patch111 -p1 -b .samba-3.6.23-gecos.patch
%patch112 -p1 -b .samba-3.6.23-glusterfs.patch
%patch113 -p1 -b .samba-3.6.23-libsmbclient.patch
%patch114 -p1 -b .samba-3.6.23-fix_libads_krb5_ipv6.patch
%patch115 -p1 -b .samba-CVE-2014-0244.patch
%patch116 -p1 -b .samba-CVE-2014-3493.patch
%patch117 -p1 -b .samba-3.6.26-smb2_case_sensitive.patch
%patch118 -p1 -b .samba-3.6.99-fix_gecos_interactive.patch
%patch119 -p1 -b .samba-3.6.99-fix_dropbox_share.patch
%patch120 -p1 -b .samba-3.6.99-add_spoolss_os_version.patch
%patch121 -p1 -b .CVE-2015-0240-3.6.patch
%patch122 -p1 -b .samba-3.6.99-nt_printer_publish_guid.patch
%patch123 -p1 -b .samba-3.6.99-fix_keytab_null_termination.patch
%patch124 -p1 -b .samba-3.6.99-fix_printcap_cpu_utilization.patch
%patch125 -p1 -b .samba-3.6.99-fix_smbclient_ntlmv2_auth.patch
%patch126 -p1 -b .samba-3.6.99-fix_smb_conf_doc.patch
%patch127 -p1 -b .samba-3.6.99-bug-1117059.patch
%patch128 -p1 -b .samba-3.6.99-bug-1192211.patch
%patch129 -p1 -b .samba-3.6.99-fix_usergroup_cache_lookup.patch
%patch130 -p1 -b .samba-3.6.99-fix_force_user_winbind_default_domain.patch
%patch131 -p1 -b .samba-3.6.99-fix_rpcclient_timeout_command.patch
%patch132 -p1 -b .samba-3.6.99-fix_force_group.patch
%patch133 -p1 -b .samba-3.6.99-fix_pam_winbind_parsing_segfault.patch
%patch134 -p1 -b .samba-3.6.99-fix_mangling_hash_segfault.patch
%patch135 -p1 -b .samba-3.6.99-doc_netbios_name_length_limit.patch
%patch136 -p1 -b .samba-3.6.99-fix_map_to_guest_bad_uid.patch
%patch137 -p1 -b .samba-3.6.99-fix_security_server_share_access.patch
%patch138 -p1 -b .samba-3.6.99-fix_stale_printer_entries_on_rename.patch
%patch139 -p1 -b .CVE-2015-5299-v3-6-bso11529.patch
%patch140 -p1 -b .CVE-2015-5296-v3-6-bso11536.patch
%patch141 -p1 -b .CVE-2015-5252-v3-6-bso11395.patch
%patch142 -p1 -b .CVE-2015-5330-v3-6-bso11599.patch
%patch144 -p1 -b .samba-3.6.99-net_ads_join_no_dns_updates.patch
%patch145 -p1 -b .samba-3.6.99-asserted_identity_sid-S-1-18-1.patch
#%patch146 -p1 -b .samba-3.6.99-clidfs.patch
%patch147 -p1 -b .CVE-2015-7560-v3-6.patch
%patch148 -p1 -b .samba-3.6.99-fix_symlink_verification.patch
%patch149 -p1 -b .CVE-preparation-v3-6.patch
%patch150 -p1 -b .CVE-2016-2110-v3-6.patch
%patch151 -p1 -b .CVE-2016-2111-v3-6.patch
%patch152 -p1 -b .CVE-2016-2112-v3-6.patch
%patch153 -p1 -b .CVE-2016-2115-v3-6.patch
%patch154 -p1 -b .CVE-2016-2118-v3-6.patch
%patch155 -p1 -b .CVE-2015-5370-v3-6.patch
%patch156 -p1 -b .samba-3.6.99-fix_winbind_cache_memory_leak.patch
%patch157 -p1 -b .samba-3.6.99-fix_memleak_winbind_cached_creds.patch

%patch190 -p1 -b .doc-update.patch
%patch200 -p1 -b .samba-3.6.x-winbind_tevent_poll.patch

mv %{samba_source}/VERSION %{samba_source}/VERSION.orig
sed -e 's/SAMBA_VERSION_VENDOR_SUFFIX=$/&\"%{samba_release}\"/' < %samba_source/VERSION.orig > %samba_source/VERSION
pushd %{samba_source}
script/mkversion.sh
popd

#Remove smbldap-tools, they are already packaged separately in Fedora
rm -fr examples/LDAP/smbldap-tools-*/


%build
pushd %{samba_source}

sh autogen.sh
%ifarch i386 sparc
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%endif
%ifarch ia64
#libtoolize --copy --force     # get it to recognize IA-64
#autoheader
#autoconf
EXTRA="-D_LARGEFILE64_SOURCE"
%endif

CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -DLDAP_DEPRECATED -fno-strict-aliasing" \
%configure \
    --with-dnsupdate \
    --with-ads \
    --with-acl-support \
    --with-automount \
    --with-dnsupdate \
    --with-libsmbclient \
    --with-libsmbsharemodes \
    --with-mmap \
    --with-pam \
    --with-pam_smbpass \
    --with-quotas \
    --with-sendfile-support \
    --with-syslog \
    --with-utmp \
    --with-vfs \
    --with-winbind \
    --without-smbwrapper \
    --with-lockdir=/var/lib/samba \
    --with-piddir=/var/run \
    --with-mandir=%{_mandir} \
    --with-privatedir=/var/lib/samba/private \
    --with-logfilebase=/var/log/samba \
    --with-libdir=%{_libdir} \
    --with-modulesdir=%{_libdir}/samba \
    --with-configdir=%{_sysconfdir}/samba \
    --with-pammodulesdir=%{_lib}/security \
    --with-swatdir=%{_datadir}/swat \
    --with-shared-modules=idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2 \
    --with-cluster-support \
    --with-libtalloc=no \
    --with-libtdb=no \
    --enable-external-libtalloc=yes \
    --enable-external-libtdb=yes \
    --with-aio-support \
%if ! %with_vfs_glusterfs
    --enable-glusterfs=no \
%endif
    --disable-fam

make idl_full

make  pch

make  LD_LIBRARY_PATH=$RPM_BUILD_DIR/%{name}-%{samba_version}%{pre_release}/%samba_source/bin \
    %{?_smp_mflags} \
    all ../nsswitch/libnss_wins.so modules test_pam_modules test_nss_modules test_shlibs

make  LD_LIBRARY_PATH=$RPM_BUILD_DIR/%{name}-%{samba_version}%{pre_release}/%samba_source/bin \
    %{?_smp_mflags} \
    -C lib/netapi/examples

make  debug2html smbfilter

popd

%install
rm -rf %{buildroot}

install -d -m 0755 %{buildroot}/sbin
install -d -m 0755 %{buildroot}/usr/{sbin,bin}
install -d -m 0755 %{buildroot}/%{_initrddir}
install -d -m 0755 %{buildroot}/%{_sysconfdir}/{pam.d,logrotate.d,security}
install -d -m 0755 %{buildroot}/%{_lib}/security
install -d -m 0755 %{buildroot}/var/lib/samba
install -d -m 0755 %{buildroot}/var/lib/samba/private
install -d -m 0755 %{buildroot}/var/lib/samba/winbindd_privileged
install -d -m 0755 %{buildroot}/var/lib/samba/scripts
install -d -m 0755 %{buildroot}/var/log/samba/old
install -d -m 0755 %{buildroot}/var/spool/samba
install -d -m 0755 %{buildroot}/%{_datadir}/swat/using_samba
install -d -m 0755 %{buildroot}/var/run/winbindd
install -d -m 0755 %{buildroot}/%{_libdir}/samba
install -d -m 0755 %{buildroot}/%{_libdir}/pkgconfig

pushd %{samba_source}

%makeinstall \
    BINDIR=%{buildroot}%{_bindir} \
    BASEDIR=%{buildroot}%{_prefix} \
    SBINDIR=%{buildroot}%{_sbindir} \
    DATADIR=%{buildroot}%{_datadir} \
    LOCKDIR=%{buildroot}/var/lib/samba \
    PRIVATEDIR=%{buildroot}%{_sysconfdir}/samba \
    LIBDIR=%{buildroot}%{_libdir}/ \
    MODULESDIR=%{buildroot}%{_libdir}/samba \
    CONFIGDIR=%{buildroot}%{_sysconfdir}/samba \
    PAMMODULESDIR=%{buildroot}/%{_lib}/security \
    MANDIR=%{buildroot}%{_mandir} \
    VARDIR=%{buildroot}/var/log/samba \
    CODEPAGEDIR=%{buildroot}%{_libdir}/samba \
    SWATDIR=%{buildroot}%{_datadir}/swat \
    SAMBABOOK=%{buildroot}%{_datadir}/swat/using_samba \
    PIDDIR=%{buildroot}/var/run

popd

# Install other stuff
install -m644 packaging/Fedora/smb.conf.default %{buildroot}%{_sysconfdir}/samba/smb.conf
install -m755 %samba_source/script/mksmbpasswd.sh %{buildroot}%{_bindir}
install -m644 packaging/Fedora/smbusers %{buildroot}%{_sysconfdir}/samba/smbusers
install -m755 packaging/Fedora/smbprint %{buildroot}%{_bindir}
install -m755 packaging/Fedora/smb.init %{buildroot}%{_initrddir}/smb
install -m755 packaging/Fedora/nmb.init %{buildroot}%{_initrddir}/nmb
install -m755 packaging/Fedora/winbind.init %{buildroot}%{_initrddir}/winbind
install -m644 packaging/Fedora/pam_winbind.conf %{buildroot}%{_sysconfdir}/security
#ln -s ../..%{_initrddir}/smb  %{buildroot}%{_sbindir}/samba
install -m644 packaging/Fedora/samba.pamd %{buildroot}%{_sysconfdir}/pam.d/samba
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/samba
echo 127.0.0.1 localhost > %{buildroot}%{_sysconfdir}/samba/lmhosts
install -d -m 0755 %{buildroot}%{_sysconfdir}/openldap/schema
install -m644 examples/LDAP/samba.schema %{buildroot}%{_sysconfdir}/openldap/schema/samba.schema

# winbind
install -d -m 0755 -p %{buildroot}%{_libdir}
install -m 755 nsswitch/libnss_winbind.so %{buildroot}/%{_lib}/libnss_winbind.so.2
ln -sf /%{_lib}/libnss_winbind.so.2  %{buildroot}%{_libdir}/libnss_winbind.so
install -m 755 nsswitch/libnss_wins.so %{buildroot}/%{_lib}/libnss_wins.so.2
ln -sf /%{_lib}/libnss_wins.so.2  %{buildroot}%{_libdir}/libnss_wins.so

# winbind krb5 locator
#install -d -m0755 %{buildroot}%{_libdir}/krb5/plugins/libkrb5
install -d -m 0755 %{buildroot}%{_libdir}/krb5/plugins/libkrb5
install -m 755 source3/bin/winbind_krb5_locator.so %{buildroot}/%{_libdir}/winbind_krb5_locator.so
touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

# libraries {
build_libdir="%{buildroot}%{_libdir}"

# make install puts libraries in the wrong place
# (but at least gets the versioning right now)

list="smbclient smbsharemodes netapi wbclient"
for i in $list; do
    install -m 644 %samba_source/pkgconfig/$i.pc $build_libdir/pkgconfig/ || true
done


/sbin/ldconfig -n %{buildroot}%{_libdir}

# }

install -d -m0755 %{buildroot}%{_sysconfdir}/xinetd.d
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/swat

install -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/samba

install -m 755 %samba_source/lib/netapi/examples/bin/netdomjoin-gui %{buildroot}/%{_sbindir}/netdomjoin-gui
install -d -m0755 %{buildroot}%{_datadir}/pixmaps/%{name}
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/samba.ico %{buildroot}/%{_datadir}/pixmaps/%{name}/samba.ico
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/logo.png %{buildroot}/%{_datadir}/pixmaps/%{name}/logo.png
install -m 644 %samba_source/lib/netapi/examples/netdomjoin-gui/logo-small.png %{buildroot}/%{_datadir}/pixmaps/%{name}/logo-small.png

rm -f %{buildroot}/%{_mandir}/man1/editreg.1*
rm -f %{buildroot}%{_mandir}/man1/log2pcap.1*
rm -f %{buildroot}%{_mandir}/man1/smbsh.1*
#rm -f %{buildroot}%{_mandir}/man1/smbget.1*
rm -f %{buildroot}%{_mandir}/man5/smbgetrc.5*
rm -f %{buildroot}%{_mandir}/man1/vfstest.1*
rm -f %{buildroot}%{_mandir}/man1/testprns.1*

rm -f %{buildroot}%{_mandir}/man8/tdbbackup.8*
rm -f %{buildroot}%{_mandir}/man8/tdbdump.8*
rm -f %{buildroot}%{_mandir}/man8/tdbtool.8*

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbadd.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbdel.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbedit.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbmodify.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbsearch.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ldbrename.1*

# remove patch leftover
rm -f examples/misc/wall.perl.perl

%clean
rm -rf %{buildroot}

#%pre

%post
/sbin/chkconfig --add smb
/sbin/chkconfig --add nmb
if [ "$1" -ge "1" ]; then
    /sbin/service smb condrestart >/dev/null 2>&1 || :
    /sbin/service nmb condrestart >/dev/null 2>&1 || :
fi
exit 0

%preun
if [ $1 = 0 ] ; then
    /sbin/service smb stop >/dev/null 2>&1 || :
    /sbin/service nmb stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del smb
    /sbin/chkconfig --del nmb
fi
exit 0

#%postun


%pre winbind
/usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
/sbin/chkconfig --add winbind

if [ "$1" -ge "1" ]; then
    /sbin/service winbind condrestart >/dev/null 2>&1 || :
fi

%post common
/sbin/ldconfig

%preun winbind
if [ $1 = 0 ] ; then
    /sbin/service winbind stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del winbind
fi
exit 0

%postun common
/sbin/ldconfig


%post -n libsmbclient
/sbin/ldconfig

%postun -n libsmbclient
/sbin/ldconfig

%postun winbind-krb5-locator
if [ "$1" -ge "1" ]; then
        if [ "`readlink %{_sysconfdir}/alternatives/winbind_krb5_locator.so`" == "%{_libdir}/winbind_krb5_locator.so" ]; then
                %{_sbindir}/update-alternatives --set winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so
        fi
fi

%post winbind-krb5-locator
%{_sbindir}/update-alternatives --install %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so \
                                winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so 10

%preun winbind-krb5-locator
if [ $1 -eq 0 ]; then
        %{_sbindir}/update-alternatives --remove winbind_krb5_locator.so %{_libdir}/winbind_krb5_locator.so
fi


%files
%defattr(-,root,root)
%{_sbindir}/smbd
%{_sbindir}/nmbd
%{_bindir}/mksmbpasswd.sh
%{_bindir}/smbstatus
%{_bindir}/eventlogadm
%config(noreplace) %{_sysconfdir}/samba/smbusers
%attr(755,root,root) %{_initrddir}/smb
%attr(755,root,root) %{_initrddir}/nmb
%config(noreplace) %{_sysconfdir}/logrotate.d/samba
%config(noreplace) %{_sysconfdir}/pam.d/samba
%{_mandir}/man7/samba.7*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/eventlogadm.8*
%{_mandir}/man8/vfs_*.8*
%dir %{_libdir}/samba/vfs/
%{_libdir}/samba/vfs/acl_tdb.so
%{_libdir}/samba/vfs/acl_xattr.so
%{_libdir}/samba/vfs/aio_fork.so
%{_libdir}/samba/vfs/audit.so
%{_libdir}/samba/vfs/cap.so
%{_libdir}/samba/vfs/catia.so
%{_libdir}/samba/vfs/crossrename.so
%{_libdir}/samba/vfs/default_quota.so
%{_libdir}/samba/vfs/dirsort.so
%{_libdir}/samba/vfs/expand_msdfs.so
%{_libdir}/samba/vfs/extd_audit.so
%{_libdir}/samba/vfs/fake_perms.so
%{_libdir}/samba/vfs/fileid.so
%{_libdir}/samba/vfs/full_audit.so
%{_libdir}/samba/vfs/linux_xfs_sgid.so
%{_libdir}/samba/vfs/netatalk.so
%{_libdir}/samba/vfs/preopen.so
%{_libdir}/samba/vfs/readahead.so
%{_libdir}/samba/vfs/readonly.so
%{_libdir}/samba/vfs/recycle.so
%{_libdir}/samba/vfs/scannedonly.so
%{_libdir}/samba/vfs/shadow_copy.so
%{_libdir}/samba/vfs/shadow_copy2.so
%{_libdir}/samba/vfs/smb_traffic_analyzer.so
%{_libdir}/samba/vfs/streams_depot.so
%{_libdir}/samba/vfs/streams_xattr.so
%{_libdir}/samba/vfs/syncops.so
%{_libdir}/samba/vfs/time_audit.so
%{_libdir}/samba/vfs/xattr_tdb.so
%dir %{_libdir}/samba/auth/
%{_libdir}/samba/auth/script.so
%dir %{_libdir}/samba/charset/
%{_libdir}/samba/charset/CP437.so
%{_libdir}/samba/charset/CP850.so

%attr(1777,root,root) %dir /var/spool/samba
%dir %{_sysconfdir}/openldap/schema
%{_sysconfdir}/openldap/schema/samba.schema

%doc examples/autofs examples/LDAP examples/libsmbclient examples/misc examples/printer-accounting
%doc examples/printing

%files swat
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/xinetd.d/swat
%{_datadir}/swat
%{_sbindir}/swat
%{_mandir}/man8/swat.8*
%attr(755,root,root) %{_libdir}/samba/*.msg

%files client
%defattr(-,root,root)
%{_bindir}/rpcclient
%{_bindir}/smbcacls
%{_bindir}/findsmb
%{_bindir}/smbget
%{_bindir}/nmblookup
%{_bindir}/smbclient
%{_bindir}/smbprint
%{_bindir}/smbspool
%{_bindir}/smbta-util
%{_bindir}/smbtar
%{_bindir}/smbtree
%{_bindir}/sharesec
%{_mandir}/man1/findsmb.1*
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/rpcclient.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbtree.1*
%{_mandir}/man1/smbget.1*
%{_mandir}/man1/sharesec.1*
%{_mandir}/man8/smbspool.8*
%{_mandir}/man8/smbta-util.8*

%files common
%defattr(-,root,root)
%attr(755,root,root) /%{_lib}/security/pam_smbpass.so
%dir %{_libdir}/samba
%{_libdir}/samba/lowcase.dat
%{_libdir}/samba/upcase.dat
%{_libdir}/samba/valid.dat
%{_libdir}/libnetapi.so
%attr(755,root,root) %{_libdir}/libnetapi.so.*
%{_includedir}/netapi.h
%{_libdir}/pkgconfig/netapi.pc
%{_bindir}/net
%{_bindir}/testparm
%{_bindir}/smbpasswd
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/smbcquotas
%{_bindir}/smbcontrol
%dir /var/lib/samba
%attr(700,root,root) %dir /var/lib/samba/private
%dir /var/lib/samba/scripts
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %{_sysconfdir}/samba/lmhosts
%config(noreplace) %{_sysconfdir}/sysconfig/samba
%dir %{_sysconfdir}/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%{_mandir}/man1/dbwrap_tool.1*
%{_mandir}/man1/profiles.1*
%{_mandir}/man1/smbcquotas.1*
%{_mandir}/man1/smbcontrol.1*
#%{_mandir}/man1/vfstest.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man5/lmhosts.5*
%{_mandir}/man8/smbpasswd.8*
%{_mandir}/man8/pdbedit.8*
%{_mandir}/man8/net.8*
%{_datadir}/locale/*/LC_MESSAGES/net.mo

%doc README COPYING Manifest
%doc WHATSNEW.txt Roadmap

%files winbind
%defattr(-,root,root)
%{_libdir}/samba/idmap
%{_libdir}/samba/nss_info
%{_sbindir}/winbindd
%dir /var/run/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%{_initrddir}/winbind
%{_mandir}/man8/winbindd.8*
%{_mandir}/man8/idmap_*.8*
%{_datadir}/locale/*/LC_MESSAGES/pam_winbind.mo

%files winbind-clients
%defattr(-,root,root)
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%{_libdir}/libnss_winbind.so
/%{_lib}/libnss_winbind.so.2
%{_libdir}/libnss_wins.so
/%{_lib}/libnss_wins.so.2
/%{_lib}/security/pam_winbind.so
%config(noreplace) %{_sysconfdir}/security/pam_winbind.conf
%attr(755,root,root) %{_libdir}/libwbclient.so.*
%{_mandir}/man1/ntlm_auth.1*
%{_mandir}/man1/wbinfo.1*
%{_mandir}/man8/pam_winbind.8*
%{_mandir}/man5/pam_winbind.conf.5*

%files winbind-devel
%defattr(-,root,root)
%{_includedir}/wbclient.h
%{_libdir}/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc

%files winbind-krb5-locator
%defattr(-,root,root)
%{_mandir}/man7/winbind_krb5_locator.7*
%ghost %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so
%{_libdir}/winbind_krb5_locator.so

%files doc
%defattr(-,root,root)
%doc docs/Samba3-Developers-Guide.pdf docs/Samba3-ByExample.pdf
%doc docs/Samba3-HOWTO.pdf
%doc docs/htmldocs

%files -n libsmbclient
%defattr(-,root,root)
%attr(755,root,root) %{_libdir}/libsmbclient.so.*
%attr(755,root,root) %{_libdir}/libsmbsharemodes.so.*

%files -n libsmbclient-devel
%defattr(-,root,root)
%{_includedir}/libsmbclient.h
%{_includedir}/smb_share_modes.h
%{_libdir}/libsmbclient.so
%{_libdir}/libsmbsharemodes.so
%{_libdir}/pkgconfig/smbclient.pc
%{_libdir}/pkgconfig/smbsharemodes.pc
%{_mandir}/man7/libsmbclient.7*

%files domainjoin-gui
%defattr(-,root,root)
%{_sbindir}/netdomjoin-gui
%dir %{_datadir}/pixmaps/samba
%{_datadir}/pixmaps/samba/samba.ico
%{_datadir}/pixmaps/samba/logo.png
%{_datadir}/pixmaps/samba/logo-small.png

%if %{with_vfs_glusterfs}
%files glusterfs
%{_libdir}/samba/vfs/glusterfs.so
%endif

%changelog
* Tue May 24 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-36
- resolves: #1364363 - Fix winbind memory leak with each cached creds login

* Mon Apr 25 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-35
- related: #1329967 - Bump release version

* Thu Apr 21 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-34
- resolves: #1329967 - Fix netlogon credential checks
- resolves: #1329975 - Fix dcerpc trailer verificaton

* Tue Apr 12 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-33
- related: #1322687 - Update CVE patchset

* Mon Apr 11 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-32
- related: #1322687 - Update manpages

* Mon Apr 11 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-31
- related: #1322687 - Update CVE patchset

* Fri Apr 08 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-30
- related: #1322687 - Update CVE patchset

* Fri Apr 08 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-29
- resolves: #1322687 - Fix CVE-2015-5370
- resolves: #1322687 - Fix CVE-2016-2110
- resolves: #1322687 - Fix CVE-2016-2111
- resolves: #1322687 - Fix CVE-2016-2112
- resolves: #1322687 - Fix CVE-2016-2115
- resolves: #1322687 - Fix CVE-2016-2118 (Known as Badlock)

* Mon Mar 14 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-28
- resolves: #1305870 - Fix symlink verification

* Mon Mar 07 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-27
- resolves: #1314671 - Fix CVE-2015-7560

* Wed Jan 20 2016 Guenther Deschner <gdeschner@redhat.com> - 3.6.23-26
- resolves: #1211744 - Fix DFS client access with Windows Server 2008

* Fri Jan 15 2016 Guenther Deschner <gdeschner@redhat.com> - 3.6.23-25
- resolves: #1242614 - Fix unmappable S-1-18-1 sid truncates group lookups

* Thu Jan 07 2016 Andreas Schneider <asn@redhat.com> - 3.6.23-24
- resolves: #1271763 - Fix segfault in NTLMv2_generate_names_blob()
- resolves: #1261265 - Add '--no-dns-updates' option for 'net ads join'

* Fri Dec 11 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-23
- resolves: #1290707 - CVE-2015-5299
- related: #1290707 - CVE-2015-5296
- related: #1290707 - CVE-2015-5252
- related: #1290707 - CVE-2015-5330

* Thu Oct 15 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-22
- resolves: #1232021 - Do not overwrite smb.conf manpage
- resolves: #1216060 - Document netbios name length limitations
- resolves: #1234249 - Fix 'map to guest = Bad Uid' option
- resolves: #1219570 - Fix 'secuirtiy = server' (obsolete) share access
- resolves: #1211657 - Fix stale cache entries if a printer gets renamed

* Fri Sep 18 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-21
- resolves: #1252180 - Fix 'force group' with 'winbind use default domain'.
- resolves: #1250100 - Fix segfault in pam_winbind if option parsing fails
- resolves: #1222985 - Fix segfault with 'mangling method = hash' option

* Fri Apr 10 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-20
- resolves: #1164269 - Fix rpcclient timeout command.
* Wed Apr 01 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-19
- resolves: #1201611 - Fix 'force user' with 'winbind use default domain'.

* Thu Mar 12 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-18
- resolves: #1194549 - Fix winbind caching issue and support SID compression.

* Wed Mar 04 2015 Michael Adam <madam@redhat.com> - 3.6.23-17
- resolves: #1192211 - Fix restoring shadow copy snapshot with SMB2.

* Tue Mar 03 2015 Michael Adam <madam@redhat.com> - 3.6.23-16
- resolves: #1117059 - Fix nss group enumeration with unresolved groups.

* Wed Feb 18 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-15
- resolves: #1165750 - Fix guid retrieval for published printers.
- resolves: #1163383 - Fix 'net ads join -k' with existing keytab entries.
- resolves: #1195456 - Fix starting daemons on read only filesystems.
- resolves: #1138552 - Fix CPU utilization when re-reading the printcap info.
- resolves: #1144916 - Fix smbclient NTLMv2 authentication.
- resolves: #1164336 - Document 'sharesec' command for
                       'access based share enum' option.

* Mon Feb 16 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-14
- related: #1191339 - Update patchset for CVE-2015-0240.

* Thu Feb 12 2015 Andreas Schneider <asn@redhat.com> - 3.6.23-13
- resolves: #1191339 - CVE-2015-0240: RCE in netlogon.

* Wed Aug 20 2014 - Guenther Deschner <gdeschner@redhat.com> - 3.6.23-12
- resolves: #1127723 - Fix samlogon secure channel recovery.

* Tue Aug 12 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-11
- resolves: #1129006 - Add config variables to set spoolss os version.

* Tue Aug 12 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-10
- resolves: #1124835 - Fix dropbox share.

* Tue Jul 15 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-9
- related: #1053886 - Fix receiving the gecos field with winbind.

* Wed Jul 09 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-8
- resolves: #1110733 - Fix write operations as guest with 'security = share'.
- resolves: #1053886 - Fix receiving the gecos field with winbind.

* Tue Jun 24 2014 - Guenther Deschner <gdeschner@redhat.com> - 3.6.23-7
- resolves: #1107777 - Fix SMB2 with "case sensitive = True"

* Wed Jun 11 2014 - Guenther Deschner <gdeschner@redhat.com> - 3.6.23-6
- resolves: #1105500 - CVE-2014-0244: DoS in nmbd.
- resolves: #1108841 - CVE-2014-3493: DoS in smbd with unicode path names.

* Fri Jun 06 2014 - Guenther Deschner <gdeschner@redhat.com> - 3.6.23-5
- related: #1061301 - Only link glusterfs libraries to vfs module.

* Wed Jun 04 2014 - Guenther Deschner <gdeschner@redhat.com> - 3.6.23-4
- resolves: #1051656 - Fix gecos field copy debug warning.
- resolves: #1061301 - Add glusterfs vfs module.
- resolves: #1087472 - Fix libsmbclient crash when HOME variable isn't set.
- resolves: #1099443 - 'net ads testjoin' fails with IPv6.
- resolves: #1100670 - Fix 'force user' with 'security = ads'.
- resolves: #1096522 - Fix enabling SMB2 causes file operations to fail.

* Wed Apr 02 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-3
- resolves: #1081539 - Add timeout option to smbclient.

* Thu Mar 27 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-2
- resolves: #1022534 - Do not build Samba with fam support.
- resolves: #1059301 - Fix nbt query with many components.
- resolves: #1057332 - Fix force user with guest account.
- resolves: #1021706 - Fix %G substitution in 'template homedir'.
- resolves: #1040472 - Fix group expansion in service path.
- resolves: #1069570 - Fix memory leak reading printer list.
- resolves: #1067607 - Fix wbinfo -i with one-way trusts.
- resolves: #1050887 - Fix 100% CPU utilization in winbindd when trying to
                       free memory in winbindd_reinit_after_fork.
- resolves: #1029000 - Fix 'force user' with 'security = ads'.

* Tue Mar 11 2014 - Andreas Schneider <asn@redhat.com> - 3.6.23-1
- resolves: #1073356 - Fix CVE-2013-4496, CVE-2012-6150 and CVE-2013-6442.
- resolves: #1018038 - Fix CVE-2013-4408.

* Fri Feb 28 2014 - Andreas Schneider <asn@redhat.com> - 3.6.22-1
- resolves: #1003921 - Rebase Samba to 3.6.22.
- resolves: #1035332 - Fix force user with 'security = user'.

* Fri Nov 08 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-165
- resolves: #1028086 - Fix CVE-2013-4475.

* Fri Oct 11 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-164
- resolves: #1008574 - Fix offline logon cache not updating for cross child
                       domain group membership.

* Wed Oct 09 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-163
- resolves: #1015359 - Fix CVE-2013-0213 and CVE-2013-0214 in SWAT.

* Tue Sep 17 2013 - Guenther Deschner <gdeschner@redhat.com> - 3.6.9-162
- resolves: #978007 - Fix "valid users" manpage documentation.

* Thu Sep 05 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-161
- resolves: #997338 - Fix smbstatus as non root user.
- resolves: #1003689 - Fix Windows 8 printer driver support.

* Wed Aug 14 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-160
- resolves: #948071 - Group membership is not correct on logins with new
                      AD groups.
- resolves: #953985 - User and group info not return from a Trusted Domain.

* Mon Aug 12 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-159
- resolves: #995109 - net ads join - segmentation fault if no realm has been
                      specified.
- List all vfs, auth and charset modules in the spec file.

* Tue Aug 06 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-158
- resolves: #984808 - CVE-2013-4124: DoS via integer overflow when reading
                      an EA list

* Fri Aug 02 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-157
- Fix Windows 8 Roaming Profiles.
- resolves: #990685

* Mon Jul 08 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-156
- Fix PIDL parsing with newer versions of gcc.
- Fix dereferencing a unique pointer in the WKSSVC server.
- resolves: #980382

* Mon Jun 17 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-155
- Check for system libtevent and require version 0.9.18.
- Use tevent epoll backend in winbind.
- resolves: #951175

* Fri Jun 14 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-154
- Add encoding option to 'net printing (migrate|dump)' command.
- resolves: #915455

* Wed Jun 12 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-153
- Fix overwrite of errno in check_parent_exists().
- resolves: #966489
- Fix dir code using dirfd() without vectoring trough VFS calls.
- resolves: #971283

* Wed May 22 2013 - Andreas Schneider <asn@redhat.com> - 3.6.9-152
- Fix 'map untrusted to domain' with NTLMv2.
- resolves: #961932
- Fix the username map optimization.
- resolves: #952268
- Fix 'net ads keytab add' not respecting the case.
- resolves: #955683
- Fix write operations as guest with security = share
- resolves: #953025
- Fix pam_winbind upn to username conversion if you have different seperator.
- resolves: #949613
- Change chkconfig order to start winbind before netfs.
- resolves: #948623
- Fix cache issue when resoliving groups without domain name.
- resolves: #927383

* Mon Dec 17 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-151
- Fix typo in winbind-krb-locator post uninstall script.
- related: #864950

* Thu Dec 06 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-150
- Fix typo in winbind-krb-locator post uninstall script.
- related: #864950

* Wed Dec 05 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-149
- Fix leaking sockets of SMB connections to a DC.
- resolves: #852175

* Fri Nov 30 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-148
- Fix work around for 'winbind use default domain'.
- resolves: #876262

* Wed Nov 28 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-147
- Rebuild with correct libtalloc and libtdb versions.
- related: #879578

* Wed Nov 28 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-146
- Fix large read requests cause server to issue malformed reply.
- resolves: #879578

* Wed Nov 14 2012 - Andreas Schneider <asn@redhat.com> - 3.6.9-145
- Failover if LogonSamLogon fails to connect to Netlogon.
- resolves: #875879

* Tue Nov 13 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.9-144
- Fix AES session key usage
- related: #748407

* Fri Nov 09 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.9-143
- Fix winbind rpm dependency
- related: #649479

* Mon Oct 30 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.9-142
- Rebase to version 3.6.9.
- related: #649479

* Mon Oct 30 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.8-141
- Fix AES kerberos key detection
- related: #748407

* Wed Oct 24 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-140
- Fix net ads join improperly using 'realm' to describe 'dns name'.
- resolves: #866570

* Wed Oct 19 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-139
- Move pam_winbind.conf to the package of the module.
- resolves: #867315

* Thu Oct 18 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.8-138
- Fix winbind krb5 locator RPM requires
- related: #864950

* Wed Oct 10 2012 - Alexander Bokovoy <abokovoy@redhat.com> - 3.6.8-137
- Use alternatives to configure winbind_krb5_locator.so.
- Move wbinfo and ntlm_auth to the correct package so samba4 can
  correctly handle conflicts.
- resolves: #864950

* Mon Oct 08 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-136
- Fix loading the imap hash module.
- resolves: #864045
- Fix raw printing support.
- related: #857942

* Fri Oct 05 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-135
- ACL masks incorrectly applied when setting ACLs.
- resolves: #863173

* Tue Oct 03 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.8-134
- Use AES Kerberos keys also in smb session setup
- related: #748407

* Tue Oct 02 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.8-133
- Use AES Kerberos keys
- resolves: #748407

* Mon Oct 01 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-132
- Fix client timeouts during printer imports.
- resolves: #861935

* Thu Sep 27 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-131
- Handle error if invalid ports have been specified gracefully.
- resolves: #845760
- Fix printing regression with builtin forms.
- resolves: #860967

* Wed Sep 19 2012 - Guenther Deschner <gdeschner@redhat.com> - 3.6.8-130
- Fix pam_winbind return code in error path
- resolves: #760109

* Tue Sep 18 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-129
- Fix rap printing spoolss access.
- resolves: #857942

* Mon Sep 17 2012 - Andreas Schneider <asn@redhat.com> - 3.6.8-128
- Rebase to version 3.6.8.
- related: #649479

* Wed Aug 22 2012 - Andreas Schneider <asn@redhat.com> - 3.6.7-127
- Rebase to version 3.6.7.
- related: #649479

* Mon Jul 23 2012 - Andreas Schneider <asn@redhat.com> - 3.6.6-126
- Rebase to version 3.6.6.
- resolves: #649479

* Wed Apr 25 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-125
- Security Release, fixes CVE-2012-2111
- resolves: #815689

* Wed Apr 25 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-124
- Avoid private krb5_locate_kdc usage
- resolves: #816123

* Thu Apr 05 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-123
- Disable PAM_RADIO_TYPE handling in pam_winbind
- resolves: #788089

* Thu Apr 05 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-122
- Fix posix acl set handling
- resolves: #808449

* Tue Mar 20 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-121
- Security Release, fixes CVE-2012-1182
- resolves: #804646

* Wed Feb 15 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-120
- Fix smbd crash with security = server
- resolves: #753143

* Tue Feb 14 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-119
- Increase log level for debug message
- resolves: #771812

* Mon Feb 13 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-118
- Fix winbind pwent enumeration
- resolves: #767659

* Mon Feb 13 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-117
- Add timeout to winbind cache entries
- resolves: #767656

* Mon Feb 13 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-116
- Fix potentially wrong DNS SRV queries
- resolves: #753747

* Mon Feb 13 2012 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-115
- Fix smbclient return code
- resolves: #755347

* Wed Oct 26 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-114
- Fix join using kerberos patch
- related: #737808

* Mon Oct 24 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-113
- Fix winbindd manpage (remove -Y option)
- resolves: #748348

* Mon Oct 24 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-112
- Fix DFS breaks zip file extracting unless "follow symlinks = no" set
- resolves: #748325

* Tue Oct 18 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-111
- Fix AD LDAP schema "primaryGroupID" usage documentation
- resolves: #652609

* Mon Oct 10 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-110
- Fix IE9 on Windows 7 download to samba share
- resolves: #743892

* Mon Oct 10 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-109
- Handle case when all DNS servers are down in 'net ads dns register'
- related: #691423

* Wed Oct 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-108
- Fix winbind lookup rid
- resolves: #743211

* Tue Oct 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-107
- Fix "force create mode" regression
- resolves: #740832

* Thu Sep 29 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-106
- Fix krb5 usage in smb client code
- related: #737808

* Thu Sep 29 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-105
- Fix support for old samba 3.0 domain controllers
- resolves: #741934

* Wed Sep 21 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-104
- Allow to use default krb5 credential cache in 'net' using -k
- resolves: #737808

* Tue Sep 20 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-103
- Fix idmap initialization debug message
- resolves: #739186

* Tue Sep 20 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-102
- Document -k option in the 'net' manpage
- resolves: #737810

* Tue Sep 20 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-101
- Remove patch leftover from rpmlint fix
- related: #730680

* Mon Sep 19 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-100
- Fix rpmlint errors
- resolves: #730680

* Fri Aug 05 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-99
- Fix wbinfo manpage
- resolves: #719365

* Thu Aug 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-98
- Fix cleartext authentication after applying Windows security patch KB2536276
- resolves: #719355

* Thu Aug 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-97
- Fix several issues discovered by coverity scan
- resolves: #717294

* Tue Aug 02 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.10-96
- Rebase to security update release 3.5.10
- related: #722561

* Tue Jul 26 2011 Simo Sorce <ssorce@redhat.com> - 3.5.9-95
- Fix file descriptor leak in pam_winbind.c
- resolves: #725281

* Sat Jul 23 2011 Simo Sorce <ssorce@redhat.com> - 3.5.9-94
- Security Release, fixes CVE-2011-2694, CVE-2011-2522
- resolves: #722561

* Thu Jun 16 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.9-93
- Update to 3.5.9
- related: #694543

* Wed Jun 01 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.8-92
- Fix server principal name guessing
- resolves: #703412

* Wed Jun 01 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.8-91
- Fix lsa lookupsids calls over ncacn_ip_tcp that caused getent passwd queries
  to fail
- resolves: #709641

* Wed Jun 01 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.8-90
- Fix cups location publishing
- resolves: #709617

* Tue May 31 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.8-89
- Fix printcap handling and cups spooler interaction
- resolves: #709070
- Fix spoolss form index mixup (wrong papersize)
- resolves: #703393 

* Mon May 30 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.8-88
- Update to 3.5.8
- resolves: #694543

* Mon Mar 28 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.6-87
- Fix DNS updates when having multiple DNS servers
- resolves: #691423

* Fri Feb 18 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.6-86
- Security Release, fixes CVE-2011-0719
- resolves: #678335

* Fri Feb 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.6-85
- Fix krb5 access to some 3rd party cifs servers
- resolves: #667675

* Fri Feb 04 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.6-84
- Add %verify(not md5 size mtime) to smb.conf
- resolves: #628955

* Fri Jan 14 2011 Guenther Deschner <gdeschner@redhat.com> - 3.5.6-83
- Update to 3.5.6 bugfix release
- resolves: #660667

* Thu Dec 09 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-82
- Add configtest parameter to smb init script
- resolves: #614853

* Thu Dec 09 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-81
- Add Posix fallocate performance patch (strict allocate = yes)
- resolves: #659884

* Thu Dec 09 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-80
- Fix inconsistent getpwnam name lookup
- resolves: #645173

* Wed Dec 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-79
- Fix smbd changing mode of files after rename
- resolves: #629374

* Wed Dec 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-78
- Fix 'default case' manpage documentation
- resolves: #639141

* Wed Dec 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-77
- Fix nmb init script description
- resolves: #641368

* Tue Dec 07 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-76
- Fix SPNEGO parsing for Windows 7
- resolves: #651947

* Tue Dec 07 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-75
- Fix charset handling
- resolves: #650244

* Tue Dec 07 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-74
- Add "winbind max clients" configure option
- resolves: #650245

* Tue Nov 30 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-73
- Fix libsmbclient SMB signing
- resolves: #654426

* Tue Nov 30 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-72
- Put winbind krb5 locator plugin into a separate rpm
- resolves: #629396

* Tue Nov 30 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-71
- Fix typos in default smb.conf (selinux et al.)
- resolves: #596345, #626473

* Tue Nov 30 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-70
- Fix cupsaddsmb upload for Win9x drivers
- resolves: #640888

* Thu Sep 09 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-69
- Security Release, fixes CVE-2010-3069
- resolves: #632265

* Tue Aug 24 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-68
- Fix winbind offline mode
- resolves: #626407

* Mon Aug 23 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-67
- Further fixes for winbind secure channel
- related: #622627

* Tue Aug 10 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-66
- Fix winbind secure channel (samlogonex)
- resolves: #622627

* Mon Jun 28 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.4-65
- Update to 3.5.4
- resolves: #608875

* Fri Jun 18 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-64
- Silence strict aliasing warning
- resolves: #605309

* Tue Jun 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-63
- Keep old machine password for kerberos clients
- resolves: #599544

* Fri May 21 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5-2-62
- Add explicit subpackage dependencies to samba-winbind-clients
- resolves: #594339

* Tue May 18 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-61
- Fix pidfile fd leak (avoids selinux AVC message)
- resolves: #582250

* Mon May 17 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-60
- Fix winbind over ipv6
- resolves: #580643

* Wed May 12 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-59
- Make sure nmb and smb initscripts return LSB compliant return codes
- resolves: #530954

* Tue May 11 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-58
- Fix smbclient with security=share
- resolves: #590021

* Tue Apr 20 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.2-57
- Update to 3.5.2
- resolves: #583773

* Tue Mar 09 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.1-56
- Update to 3.5.1
- Security update that resolves CVE-2010-0728
- Remove cifs.upcall and mount.cifs entirely
- related: #556558

* Thu Feb 25 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.0rc3-55
- Raise required tdb version to 1.2.1
- Build with recent external libtdb
- related: #556558

* Mon Feb 22 2010 Guenther Deschner <gdeschner@redhat.com> - 3.5.0rc3-53
- Update to 3.5.0rc3
- related: #556558

* Wed Jan 27 2010 Guenther Deschner <gdeschner@redhat.com> - 3.3.4-51
- Security Release, fixes CVE-2009-3297
- resolves: #559274

* Fri Jan 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.4.4-50
- Update to 3.4.4
- related: #543948

* Fri Jan 08 2010 Guenther Deschner <gdeschner@redhat.com> - 3.4.2-49
- Add missing defattrs in specfile
- Fix upstream tarball url in specfile
- Cleanup unapplied patch
- related: #543948

* Fri Dec 18 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.2-48
- add pam_winbind.conf(5) manpage
- resolves: #528919

* Fri Oct 09 2009 Simo Sorce <ssorce@redhat.com> - 3.4.2-47
- Spec file cleanup
- Fix sources upstream location
- Remove conditionals to build talloc and tdb, now they are completely indepent
  packages in Fedora
- Add defattr() where missing
- Turn all tabs into 4 spaces
- Remove unused migration script
- Split winbind-clients out of main winbind package to avoid multilib to include
  huge packages for no good reason


* Thu Oct 01 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.2-0.46
- Update to 3.4.2
- Security Release, fixes CVE-2009-2813, CVE-2009-2948 and CVE-2009-2906

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 3.4.1-0.45
- Use password-auth common PAM configuration instead of system-auth

* Wed Sep 09 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.1-0.44
- Update to 3.4.1

* Thu Aug 20 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0-0.43
- Fix cli_read()
- resolves: #516165

* Thu Aug 06 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0-0.42
- Fix required talloc version number
- resolves: #516086

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:3.4.0-0.41.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0-0.41
- Fix Bug #6551 (vuid and tid not set in sessionsetupX and tconX)
- Specify required talloc and tdb version for BuildRequires

* Fri Jul 03 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0-0.40
- Update to 3.4.0

* Fri Jun 19 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0rc1-0.39
- Update to 3.4.0rc1

* Mon Jun 08 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0pre2-0.38
- Update to 3.4.0pre2

* Thu Apr 30 2009 Guenther Deschner <gdeschner@redhat.com> - 3.4.0pre1-0.37
- Update to 3.4.0pre1

* Wed Apr 29 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.4-0.36
- Update to 3.3.4

* Mon Apr 20 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.3-0.35
- Enable build of idmap_tdb2 for clustered setups

* Wed Apr  1 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.3-0.34
- Update to 3.3.3

* Thu Mar 26 2009 Simo Sorce <ssorce@redhat.com> - 3.3.2-0.33
- Fix nmbd init script nmbd reload was causing smbd not nmbd to reload the
  configuration
- Fix upstream bug 6224, nmbd was waiting 5+ minutes before running elections on
  startup, causing your own machine not to show up in the network for 5 minutes
  if it was the only client in that workgroup (fix committed upstream)

* Thu Mar 12 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.2-0.31
- Update to 3.3.2
- resolves: #489547

* Thu Mar  5 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.1-0.30
- Add libcap-devel to requires list (resolves: #488559)

* Tue Mar  3 2009 Simo Sorce <ssorce@redhat.com> - 3.3.1-0.29
- Make the talloc and ldb packages optionsl and disable their build within
  the samba3 package, they are now built as part of the samba4 package
  until they will both be released as independent packages.

* Wed Feb 25 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.1-0.28
- Enable cluster support

* Tue Feb 24 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.1-0.27
- Update to 3.3.1

* Thu Feb 21 2009 Simo Sorce <ssorce@redhat.com> - 3.3.0-0.26
- Rename ldb* tools to ldb3* to avoid conflicts with newer ldb releases

* Tue Feb  3 2009 Guenther Deschner <gdeschner@redhat.com> - 3.3.0-0.25
- Update to 3.3.0 final
- Add upstream fix for ldap connections to AD (Bug #6073)
- Remove bogus perl dependencies (resolves: #473051)

* Fri Nov 28 2008 Guenther Deschner <gdeschner@redhat.com> - 3.3.0-0rc1.24
- Update to 3.3.0rc1

* Thu Nov 27 2008 Simo Sorce <ssorce@redhat.com> - 3.2.5-0.23
- Security Release, fixes CVE-2008-4314

* Thu Sep 18 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.4-0.22
- Update to 3.2.4
- resolves: #456889
- move cifs.upcall to /usr/sbin

* Wed Aug 27 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.3-0.21
- Security fix for CVE-2008-3789

* Mon Aug 25 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.2-0.20
- Update to 3.2.2

* Mon Aug 11 2008 Simo Sorce <ssorce@redhat.com> - 3.2.1-0.19
- Add fix for CUPS problem, fixes bug #453951

* Wed Aug  6 2008 Simo Sorce <ssorce@redhat.com> - 3.2.1-0.18
- Update to 3.2.1

* Tue Jul  1 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-2.17
- Update to 3.2.0 final
- resolves: #452622

* Tue Jun 10 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.rc2.16
- Update to 3.2.0rc2
- resolves: #449522
- resolves: #448107

* Fri May 30 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.rc1.15
- Fix security=server
- resolves: #449038, #449039

* Wed May 28 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.rc1.14
- Add fix for CVE-2008-1105
- resolves: #446724

* Fri May 23 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.rc1.13
- Update to 3.2.0rc1

* Wed May 21 2008 Simo Sorce <ssorce@redhat.com> - 3.2.0-1.pre3.12
- make it possible to print against Vista and XP SP3 as servers
- resolves: #439154

* Thu May 15 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre3.11
- Add "net ads join createcomputer=ou1/ou2/ou3" fix (BZO #5465)

* Fri May 09 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre3.10
- Add smbclient fix (BZO #5452)

* Fri Apr 25 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre3.9
- Update to 3.2.0pre3

* Tue Mar 18 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre2.8
- Add fixes for libsmbclient and support for r/o relocations

* Mon Mar 10 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre2.7
- Fix libnetconf, libnetapi and msrpc DSSETUP call

* Thu Mar 06 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre2.6
- Create separate packages for samba-winbind and samba-winbind-devel
- Add cifs.spnego helper

* Wed Mar 05 2008 Guenther Deschner <gdeschner@redhat.com> - 3.2.0-1.pre2.3
- Update to 3.2.0pre2
- Add talloc and tdb lib and devel packages
- Add domainjoin-gui package

* Fri Feb 22 2008 Simo Sorce <ssorce@redhat.com> - 3.2.0-0.pre1.3
- Try to fix GCC 4.3 build
- Add --with-dnsupdate flag and also make sure other flags are required just to
  be sure the features are included without relying on autodetection to be
  successful

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:3.2.0-1.pre1.2
- Autorebuild for GCC 4.3

* Tue Dec 04 2007 Release Engineering <rel-eng at fedoraproject dot org> - 3.2.0-0.pre1.2
 - Rebuild for openldap bump

* Thu Oct 18 2007 Guenther Deschner <gdeschner@redhat.com> 3.2.0-0.pre1.1.fc9
- 32/64bit padding fix (affects multilib installations)

* Wed Oct 8 2007 Simo Sorce <ssorce@redhat.com> 3.2.0-0.pre1.fc9
- New major relase, minor switched from 0 to 2
- License change, the code is now GPLv3+
- Numerous improvements and bugfixes included
- package libsmbsharemodes too
- remove smbldap-tools as they are already packaged separately in Fedora
- Fix bug 245506 

* Tue Oct 2 2007 Simo Sorce <ssorce@redhat.com> 3.0.26a-1.fc8
- rebuild with AD DNS Update support

* Tue Sep 11 2007 Simo Sorce <ssorce@redhat.com> 3.0.26a-0.fc8
- upgrade to the latest upstream realease
- includes security fixes released today in 3.0.26

* Tue Aug 24 2007 Simo Sorce <ssorce@redhat.com> 3.0.25c-4.fc8
- add fix reported upstream for heavy idmap_ldap memleak

* Tue Aug 21 2007 Simo Sorce <ssorce@redhat.com> 3.0.25c-3.fc8
- fix a few places were "open" is used an interfere with the new glibc

* Tue Aug 21 2007 Simo Sorce <ssorce@redhat.com> 3.0.25c-2.fc8
- remove old source
- add patch to fix samba bugzilla 4772

* Tue Aug 21 2007 Guenther Deschner <gdeschner@redhat.com> 3.0.25c-0.fc8
- update to 3.0.25c

* Tue Jun 29 2007 Simo Sorce <ssorce@redhat.com> 3.0.25b-3.fc8
- handle cases defined in #243766

* Tue Jun 26 2007 Simo Sorce <ssorce@redhat.com> 3.0.25b-2.fc8
- update to 3.0.25b
- better error codes for init scripts: #244823

* Tue May 29 2007 Günther Deschner <gdeschner@redhat.com>
- fix pam_smbpass patch.

* Fri May 25 2007 Simo Sorce <ssorce@redhat.com>
- update to 3.0.25a as it contains many fixes
- add a fix for pam_smbpass made by Günther but committed upstream after 3.0.25a was cut.

* Mon May 14 2007 Simo Sorce <ssorce@redhat.com>
- final 3.0.25
- includes security fixes for CVE-2007-2444,CVE-2007-2446,CVE-2007-2447

* Mon Apr 30 2007 Günther Deschner <gdeschner@redhat.com>
- move to 3.0.25rc3

* Thu Apr 19 2007 Simo Sorce <ssorce@redhat.com>
- fixes in the spec file
- moved to 3.0.25rc1
- addedd patches (merged upstream so they will be removed in 3.0.25rc2)

* Wed Apr 4 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-12.fc7
- fixes in smb.conf
- advice in smb.conf to put scripts in /var/lib/samba/scripts
- create /var/lib/samba/scripts so that selinux can be happy
- fix Vista problems with msdfs errors

* Tue Apr 03 2007 Guenther Deschner <gdeschner@redhat.com> 3.0.24-11.fc7
- enable PAM and NSS dlopen checks during build
- fix unresolved symbols in libnss_wins.so (bug #198230)

* Fri Mar 30 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-10.fc7
- set passdb backend = tdbsam as default in smb.conf
- remove samba-docs dependency from swat, that was a mistake
- put back COPYING and other files in samba-common
- put examples in samba not in samba-docs
- leave only stuff under docs/ in samba-doc

* Thu Mar 29 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-9.fc7
- integrate most of merge review proposed changes (bug #226387)
- remove libsmbclient-devel-static and simply stop shipping the
  static version of smbclient as it seem this is deprecated and
  actively discouraged

* Wed Mar 28 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-8.fc7
- fix for bug #176649

* Mon Mar 26 2007 Simo Sorce <ssorce@redhat.com>
- remove patch for bug 106483 as it introduces a new bug that prevents
  the use of a credentials file with the smbclient tar command
- move the samba private dir from being the same as the config dir
  (/etc/samba) to /var/lib/samba/private

* Mon Mar 26 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-7.fc7
- make winbindd start earlier in the init process, at the same time
  ypbind is usually started as well
- add a sepoarate init script for nmbd called nmb, we need to be able
  to restart nmbd without dropping al smbd connections unnecessarily

* Fri Mar 23 2007 Simo Sorce <ssorce@redhat.com>
- add samba.schema to /etc/openldap/schema

* Thu Mar 22 2007 Florian La Roche <laroche@redhat.com>
- adjust the Requires: for the scripts, add "chkconfig --add smb"

* Tue Mar 20 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-6.fc7
- do not put comments inline on smb.conf options, they may be read
  as part of the value (for example log files names)

* Mon Mar 19 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-5.fc7
- actually use the correct samba.pamd file not the old samba.pamd.stack file
- fix logifles and use upstream convention of log.* instead of our old *.log
  Winbindd creates its own log.* files anyway so we will be more consistent
- install our own (enhanced) default smb.conf file
- Fix pam_winbind acct_mgmt PAM result code (prevented local users from
  logging in). Fixed by Guenther.
- move some files from samba to samba-common as they are used with winbindd
  as well

* Fri Mar 16 2007 Guenther Deschner <gdeschner@redhat.com> 3.0.24-4.fc7
- fix arch macro which reported Vista to Samba clients.

* Thu Mar 15 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-3.fc7
- Directories reorg, tdb files must go to /var/lib, not
  to /var/cache, add migration script in %%post common
- Split out libsmbclient, devel and doc packages
- Remove libmsrpc.[h|so] for now as they are not really usable
- Remove kill -HUP from rotate, samba use -HUP for other things
  noit to reopen logs

* Tue Feb 20 2007 Simo Sorce <ssorce@redhat.com> 3.0.24-2.fc7
- New upstream release
- Fix packaging issue wrt idmap modules used only by smbd
- Addedd Vista Patchset for compatibility with Windows Vista
- Change default of "msdfs root", it seem to cause problems with
  some applications and it has been proposed to change it for
  3.0.25 upstream

* Fri Sep 1 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23c-2
- New upstream release.

* Tue Aug 8 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23b-2
- New upstream release.

* Mon Jul 24 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23a-3
- Fix the -logfiles patch to close
  bz#199607 Samba compiled with wrong log path.
  bz#199206 smb.conf has incorrect log file path

* Mon Jul 24 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23a-2
- Upgrade to new upstream 3.0.23a
- include upstream samr_alias patch

* Tue Jul 11 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23-2
- New upstream release.
- Use modified filter-requires-samba.sh from packaging/RHEL/setup/
  to get rid of bogus dependency on perl(Unicode::MapUTF8)
- Update the -logfiles and -smb.conf patches to work with 3.0.23

* Thu Jul 6 2006 Jay Fenlason <fenlason@redhat.com> 3.0.23-0.RC3
- New upstream RC release.
- Update the -logfiles, and -passwd patches for
  3.0.23rc3
- Include the change to smb.init from Bastien Nocera <bnocera@redhat.com>)
  to close
  bz#182560 Wrong retval for initscript when smbd is dead
- Update this spec file to build with 3.0.23rc3
- Remove the -install.mount.smbfs patch, since we don't install
  mount.smbfs any more.

* Wed Jun 14 2006 Tomas Mraz <tmraz@redhat.com> - 2.0.21c-3
- rebuilt with new gnutls

* Fri Mar 17 2006 Jay Fenlason <fenlason@redhat.com> 2.0.21c-2
- New upstream version.

* Mon Feb 13 2006 Jay Fenlason <fenlason@redhat.com> 3.0.21b-2
- New upstream version.
- Since the rawhide kernel has dropped support for smbfs, remove smbmount
  and smbumount.  Users should use mount.cifs instead.
- Upgrade to 3.0.21b

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0:3.0.20b-2.1.1
- bump again for double-long bug on ppc(64)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 13 2005 Jay Fenlason <fenlason@redhat.com> 3.0.20b-2
- turn on -DLDAP_DEPRECATED to allow access to ldap functions that have
  been depricated in 2.3.11, but which don't have well-documented
  replacements (ldap_simple_bind_s(), for example).
- Upgrade to 3.0.20b, which includes all the previous upstream patches.
- Updated the -warnings patch for 3.0.20a.
- Include  --with-shared-modules=idmap_ad,idmap_rid to close
  bz#156810 --with-shared-modules=idmap_ad,idmap_rid
- Include the new samba.pamd from Tomas Mraz (tmraz@redhat.com) to close
  bz#170259 pam_stack is deprecated

* Sun Nov 13 2005 Warren Togami <wtogami@redhat.com> 3.0.20-3
- epochs from deps, req exact release
- rebuild against new openssl

* Mon Aug 22 2005 Jay Fenlason <fenlason@redhat.com> 3.0.20-2
- New upstream release
  Includes five upstream patches -bug3010_v1, -groupname_enumeration_v3,
    -regcreatekey_winxp_v1, -usrmgr_groups_v1, and -winbindd_v1
  This obsoletes the -pie and -delim patches
  the -warning and -gcc4 patches are obsolete too
  The -man, -passwd, and -smbspool patches were updated to match 3.0.20pre1
  Also, the -quoting patch was implemented differently upstream
  There is now a umount.cifs executable and manpage
  We run autogen.sh as part of the build phase
  The testprns command is now gone
  libsmbclient now has a man page
- Include -bug106483 patch to close
  bz#106483 smbclient: -N negates the provided password, despite documentation
- Added the -warnings patch to quiet some compiler warnings.
- Removed many obsolete patches from CVS.

* Mon May 2 2005 Jay Fenlason <fenlason@redhat.com> 3.0.14a-2
- New upstream release.
- the -64bit-timestamps, -clitar, -establish_trust, user_rights_v1,
  winbind_find_dc_v2 patches are now obsolete.

* Thu Apr 7 2005 Jay Fenlason <fenlason@redhat.com> 3.0.13-2
- New upstream release
- add my -quoting patch, to fix swat with strings that contain
  html meta-characters, and to use correct quote characters in
  lists, closing bz#134310
- include the upstream winbindd_2k3sp1 patch
- include the -smbclient patch.
- include the -hang patch from upstream.

* Thu Mar 24 2005 Florian La Roche <laroche@redhat.com>
- add a "exit 0" to the postun of the main samba package

* Wed Mar  2 2005 Tomas Mraz <tmraz@redhat.com> 3.0.11-5
- rebuild with openssl-0.9.7e

* Thu Feb 24 2005 Jay Fenlason <fenlason@redhat.com> 3.0.11-4
- Use the updated filter-requires-samba.sh file, so we don't accidentally
  pick up a dependency on perl(Crypt::SmbHash)

* Fri Feb 18 2005 Jay Fenlason <fenlason@redhat.com> 3.0.11-3
- add -gcc4 patch to compile with gcc 4.
- remove the now obsolete -smbclient-kerberos.patch
- Include four upstream patches from
  http://samba.org/~jerry/patches/post-3.0.11/
  (Slightly modified the winbind_find_dc_v2 patch to apply easily with
  rpmbuild).

* Fri Feb 4 2005 Jay Fenlason <fenlason@redhat.com> 3.0.11-2
- include -smbspool patch to close bz#104136

* Wed Jan 12 2005 Jay Fenlason <fenlason@redhat.com> 3.0.10-4
- Update the -man patch to fix ntlm_auth.1 too.
- Move pam_smbpass.so to the -common package, so both the 32
  and 64-bit versions will be installed on multiarch platforms.
  This closes bz#143617
- Added new -delim patch to fix mount.cifs so it can accept
  passwords with commas in them (via environment or credentials
  file) to close bz#144198

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 3.0.10-3
- Rebuilt for new readline.

* Fri Dec 17 2004 Jay Fenlason <fenlason@redhat.com> 3.0.10-2
- New upstream release that closes CAN-2004-1154  bz#142544
- Include the -64bit patch from Nalin.  This closes bz#142873
- Update the -logfiles patch to work with 3.0.10
- Create /var/run/winbindd and make it part of the -common rpm to close
  bz#142242

* Mon Nov 22 2004 Jay Fenlason <fenlason@redhat.com> 3.0.9-2
- New upstream release.  This obsoletes the -secret patch.
  Include my changetrustpw patch to make "net ads changetrustpw" stop
  aborting.  This closes #134694
- Remove obsolete triggers for ancient samba versions.
- Move /var/log/samba to the -common rpm.  This closes #76628
- Remove the hack needed to get around the bad docs files in the
  3.0.8 tarball.
- Change the comment in winbind.init to point at the correct pidfile.
  This closes #76641

* Mon Nov 22 2004 Than Ngo <than@redhat.com> 3.0.8-4
- fix unresolved symbols in libsmbclient which caused applications
  such as KDE's konqueror to fail when accessing smb:// URLs. #139894

* Thu Nov 11 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-3.1
- Rescue the install.mount.smbfs patch from Juanjo Villaplana
  (villapla@si.uji.es) to prevent building the srpm from trashing your
  installed /usr/bin/smbmount

* Tue Nov 9 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-3
- Include the corrected docs tarball, and use it instead of the
  obsolete docs from the upstream 3.0.8 tarball.
- Update the logfiles patch to work with the updated docs.

* Mon Nov 8 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-2
- New upstream version fixes CAN-2004-0930.  This obsoletes the
  disable-sendfile, salt, signing-shortkey and fqdn patches.
- Add my <fenlason@redhat.com> ugly non-ascii-domain patch.
- Updated the pie patch for 3.0.8.
- Updated the logfiles patch for 3.0.8.

* Tue Oct 26 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-0.pre2
- New upstream version
- Add Nalin's signing-shortkey patch.

* Tue Oct 19 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-0.pre1.3
- disable the -salt patch, because it causes undefined references in
  libsmbclient that prevent gnome-vfs from building.

* Fri Oct 15 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-0.pre1.2
- Re-enable the x_fclose patch that was accidentally disabled
  in 3.0.8-0.pre1.1.  This closes #135832
- include Nalin's -fqdn and -salt patches.

* Wed Oct 13 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-0.pre1.1
- Include disable-sendfile patch to default "use sendfile" to "no".
  This closes #132779

* Wed Oct 6 2004 Jay Fenlason <fenlason@redhat.com>
- Include patch from Steven Lawrance (slawrance@yahoo.com) that modifies
  smbmnt to work with 32-bit uids.

* Mon Sep 27 2004 Jay Fenlason <fenlason@redhat.com> 3.0.8-0.pre1
- new upstream release.  This obsoletes the ldapsam_compat patches.

* Wed Sep 15 2004 Jay Fenlason <fenlason@redhat.com> 3.0.7-4
- Update docs section to not carryover the docs/manpages directory
  This moved many files from /usr/share/doc/samba-3.0.7/docs/* to
  /usr/share/doc/samba-3.0.7/*
- Modify spec file as suggested by Rex Dieter (rdieter@math.unl.edu)
  to correctly create libsmbclient.so.0 and to use %%_initrddir instead
  of rolling our own.  This closes #132642
- Add patch to default "use sendfile" to no, since sendfile appears to
  be broken
- Add patch from Volker Lendecke <vl@samba.org> to help make
  ldapsam_compat work again.
- Add patch from "Vince Brimhall" <vbrimhall@novell.com> for ldapsam_compat
  These two patches close bugzilla #132169

* Mon Sep 13 2004 Jay Fenlason <fenlason@redhat.com> 3.0.7-3
- Upgrade to 3.0.7, which fixes CAN-2004-0807 CAN-2004-0808
  This obsoletes the 3.0.6-schema patch.
- Update BuildRequires line to include openldap-devel openssl-devel
  and cups-devel

* Mon Aug 16 2004 Jay Fenlason <fenlason@redhat.com> 3.0.6-3
- New upstream version.
- Include post 3.0.6 patch from "Gerald (Jerry) Carter" <jerry@samba.org>
  to fix a duplicate in the LDAP schema.
- Include 64-bit timestamp patch from Ravikumar (rkumar@hp.com)
  to allow correct timestamp handling on 64-bit platforms and fix #126109.
- reenable the -pie patch.  Samba is too widely used, and too vulnerable
  to potential security holes to disable an important security feature
  like -pie.  The correct fix is to have the toolchain not create broken
  executables when programs compiled -pie are stripped.
- Remove obsolete patches.
- Modify this spec file to put libsmbclient.{a,so} in the right place on
  x86_64 machines.

* Wed Aug  5 2004 Jason Vas Dias <jvdias@redhat.com> 3.0.5-3
- Removed '-pie' patch - 3.0.5 uses -fPIC/-PIC, and the combination
- resulted in executables getting corrupt stacks, causing smbmnt to
- get a SIGBUS in the mount() call (bug 127420).

* Fri Jul 30 2004 Jay Fenlason <fenlason@redhat.com> 3.0.5-2
- Upgrade to 3.0.5, which is a regression from 3.0.5pre1 for a
  security fix.
- Include the 3.0.4-backport patch from the 3E branch.  This restores
  some of the 3.0.5pre1 and 3.0.5rc1 functionality.

* Tue Jul 20 2004 Jay Fenlason <fenlason@redhat.com> 3.0.5-0.pre1.1
- Backport base64_decode patche to close CAN-2004-0500
- Backport hash patch to close CAN-2004-0686
- use_authtok patch from Nalin Dahyabhai <nalin@redhat.com>
- smbclient-kerberos patch from Alexander Larsson <alexl@redhat.com>
- passwd patch uses "*" instead of "x" for "hashed" passwords for
  accounts created by winbind.  "x" means "password is in /etc/shadow" to
  brain-damaged pam_unix module.

* Fri Jul 2 2004 Jay Fenlason <fenlason@redhat.com> 3.0.5.0pre1.0
- New upstream version
- use %% { SOURCE1 } instead of a hardcoded path
- include -winbind patch from Gerald (Jerry) Carter (jerry@samba.org)
  https://bugzilla.samba.org/show_bug.cgi?id=1315
  to make winbindd work against Windows versions that do not have
  128 bit encryption enabled.
- Moved %%{_bindir}/net to the -common package, so that folks who just
  want to use winbind, etc don't have to install -client in order to
  "net join" their domain.
- New upstream version obsoletes the patches added in 3.0.3-5
- Remove smbgetrc.5 man page, since we don't ship smbget.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 4 2004 Jay Fenlason <fenlason@redhat.com> 3.0.3-5
- Patch to allow password changes from machines patched with
  Microsoft hotfix MS04-011.
- Include patches for https://bugzilla.samba.org/show_bug.cgi?id=1302
  and https://bugzilla.samba.org/show_bug.cgi?id=1309

* Thu Apr 29 2004 Jay Fenlason <fenlason@redhat.com> 3.0.3-4
- Samba 3.0.3 released.

* Wed Apr 21 2004 jay Fenlason <fenlason@redhat.com> 3.0.3-3.rc1
- New upstream version
- updated spec file to make libsmbclient.so executable.  This closes
  bugzilla #121356

* Mon Apr 5 2004 Jay Fenlason <fenlason@redhat.com> 3.0.3-2.pre2
- New upstream version  
- Updated configure line to remove --with-fhs and to explicitly set all
  the directories that --with-fhs was setting.  We were overriding most of
  them anyway.  This closes #118598

* Mon Mar 15 2004 Jay Fenlason <fenlason@redhat.com> 3.0.3-1.pre1
- New upstream version.
- Updated -pie and -logfiles patches for 3.0.3pre1
- add krb5-devel to buildrequires, fixes #116560
- Add patch from Miloslav Trmac (mitr@volny.cz) to allow non-root to run
  "service smb status".  This fixes #116559

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 16 2004 Jay Fenlason <fenlason@redhat.com> 3.0.2a-1
- Upgrade to 3.0.2a

* Mon Feb 16 2004 Karsten Hopp <karsten@redhat.de> 3.0.2-7 
- fix ownership in -common package

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Jay Fenlason <fenlason@redhat.com>
- Change all requires lines to list an explicit epoch.  Closes #102715
- Add an explicit Epoch so that %%{epoch} is defined.

* Mon Feb 9 2004 Jay Fenlason <fenlason@redhat.com> 3.0.2-5
- New upstream version: 3.0.2 final includes security fix for #114995
  (CAN-2004-0082)
- Edit postun script for the -common package to restart winbind when
  appropriate.  Fixes bugzilla #114051.

* Mon Feb 2 2004 Jay Fenlason <fenlason@redhat.com> 3.0.2-3rc2
- add %%dir entries for %%{_libdir}/samba and %%{_libdir}/samba/charset
- Upgrade to new upstream version
- build mount.cifs for the new cifs filesystem in the 2.6 kernel.

* Mon Jan 19 2004 Jay Fenlason <fenlason@redhat.com> 3.0.2-1rc1
- Upgrade to new upstream version

* Wed Dec 17 2003 Felipe Alfaro Solana <felipe_alfaro@linuxmail.org> 3.0.1-1
- Update to 3.0.1
- Removed testparm patch as it's already merged
- Removed Samba.7* man pages
- Fixed .buildroot patch
- Fixed .pie patch
- Added new /usr/bin/tdbdump file

* Thu Sep 25 2003 Jay Fenlason <fenlason@redhat.com> 3.0.0-15
- New 3.0.0 final release
- merge nmbd-netbiosname and testparm patches from 3E branch
- updated the -logfiles patch to work against 3.0.0
- updated the pie patch
- update the VERSION file during build
- use make -j if avaliable
- merge the winbindd_privileged change from 3E
- merge the "rm /usr/lib" patch that allows Samba to build on 64-bit
  platforms despite the broken Makefile

* Mon Aug 18 2003 Jay Fenlason <fenlason@redhat.com>
- Merge from samba-3E-branch after samba-3.0.0rc1 was released

* Wed Jul 23 2003 Jay Fenlason <fenlason@redhat.com> 3.0.0-3beta3
- Merge from 3.0.0-2beta3.3E
- (Correct log file names (#100981).)
- (Fix pidfile directory in samab.log)
- (Remove obsolete samba-3.0.0beta2.tar.bz2.md5 file)
- (Move libsmbclient to the -common package (#99449))

* Tue Jun 22 2003 Nalin Dahyabhai <nalin@redhat.com> 2.2.8a-4
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 28 2003 Jay Fenlason <fenlason@redhat.com> 2.2.8a-2
- add libsmbclient.so for gnome-vfs-extras
- Edit specfile to specify /var/run for pid files
- Move /tmp/.winbindd/socket to /var/run/winbindd/socket

* Wed May 14 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add proper ldconfig calls

* Thu Apr 24 2003 Jay Fenlason <fenlason@redhat.com> 2.2.8a-1
- upgrade to 2.2.8a
- remove old .md5 files
- add "pid directory = /var/run" to the smb.conf file.  Fixes #88495
- Patch from jra@dp.samba.org to fix a delete-on-close regression

* Mon Mar 24 2003 Jay Fenlason <fenlason@redhat.com> 2.2.8-0
- Upgrade to 2.2.8
- removed commented out patches.
- removed old patches and .md5 files from the repository.
- remove duplicate /sbin/chkconfig --del winbind which causes
  warnings when removing samba.
- Fixed minor bug in smbprint that causes it to fail when called with
  more than 10 parameters: the accounting file (and spool directory
  derived from it) were being set wrong due to missing {}.  This closes
  bug #86473.
- updated smb.conf patch, includes new defaults to close bug #84822.

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 20 2003 Jonathan Blandford <jrb@redhat.com> 2.2.7a-5
- remove swat.desktop file

* Thu Feb 20 2003 Nalin Dahyabhai <nalin@redhat.com> 2.2.7a-4
- relink libnss_wins.so with SHLD="%%{__cc} -lnsl" to force libnss_wins.so to
  link with libnsl, avoiding unresolved symbol errors on functions in libnsl

* Mon Feb 10 2003 Jay Fenlason <fenlason@redhat.com> 2.2.7a-3
- edited spec file to put .so files in the correct directories
  on 64-bit platforms that have 32-bit compatability issues
  (sparc64, x86_64, etc).  This fixes bugzilla #83782.
- Added samba-2.2.7a-error.patch from twaugh.  This fixes
  bugzilla #82454.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan  9 2003 Jay Fenlason <fenlason@redhat.com> 2.2.7a-1
- Update to 2.2.7a
- Change default printing system to CUPS
- Turn on pam_smbpass
- Turn on msdfs

* Sat Jan  4 2003 Jeff Johnson <jbj@redhat.com> 2.2.7-5
- use internal dep generator.

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 2.2.7-4
- don't use rpms internal dep generator

* Mon Dec 02 2002 Elliot Lee <sopwith@redhat.com> 2.2.7-3
- Fix missing doc files.
- Fix multilib issues

* Wed Nov 20 2002 Bill Nottingham <notting@redhat.com> 2.2.7-2
- update to 2.2.7
- add patch for LFS in smbclient (<tcallawa@redhat.com>)

* Wed Aug 28 2002 Trond Eivind Glomsød <teg@redhat.com> 2.2.5-10
- logrotate fixes (#65007)

* Mon Aug 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-9
- /usr/lib was used in place of %%{_libdir} in three locations (#72554)

* Mon Aug  5 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-8
- Initscript fix (#70720)

* Fri Jul 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-7
- Enable VFS support and compile the "recycling" module (#69796)
- more selective includes of the examples dir 

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-6
- Fix the lpq parser for better handling of LPRng systems (#69352)

* Tue Jul 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-5
- desktop file fixes (#69505)

* Wed Jun 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-4
- Enable ACLs

* Tue Jun 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-3
- Make it not depend on Net::LDAP - those are doc files and examples

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.5-1
- 2.2.5

* Fri Jun 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.4-5
- Move the post/preun of winbind into the -common subpackage, 
  where the script is (#66128)

* Tue Jun  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.4-4
- Fix pidfile locations so it runs properly again (2.2.4 
  added a new directtive - #65007)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.4-2
- Fix #64804

* Thu May  9 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.4-1
- 2.2.4
- Removed some zero-length and CVS internal files
- Make it build

* Wed Apr 10 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3a-6
- Don't use /etc/samba.d in smbadduser, it should be /etc/samba

* Thu Apr  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3a-5
- Add libsmbclient.a w/headerfile for KDE (#62202)

* Tue Mar 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3a-4
- Make the logrotate script look the correct place for the pid files 

* Thu Mar 14 2002 Nalin Dahyabhai <nalin@redhat.com> 2.2.3a-3
- include interfaces.o in pam_smbpass.so, which needs symbols from interfaces.o
  (patch posted to samba-list by Ilia Chipitsine)

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3a-2
- Rebuild

* Thu Feb  7 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3a-1
- 2.2.3a

* Mon Feb  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.2.3-1
- 2.2.3

* Thu Nov 29 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-8
- New pam configuration file for samba

* Tue Nov 27 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-7
- Enable PAM session controll and password sync

* Tue Nov 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-6
- Move winbind files to samba-common. Add separate initscript for
  winbind 
- Fixes for winbind - protect global variables with mutex, use
  more secure getenv

* Thu Nov  8 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-5
- Teach smbadduser about "getent passwd" 
- Fix more pid-file references
- Add (conditional) winbindd startup to the initscript, configured in
  /etc/sysconfig/samba

* Wed Nov  7 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-4
- Fix pid-file reference in logrotate script
- include pam and nss modules for winbind

* Mon Nov  5 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-3
- Add "--with-utmp" to configure options (#55372)
- Include winbind, pam_smbpass.so, rpcclient and smbcacls
- start using /var/cache/samba, we need to keep state and there is
  more than just locks involved

* Sat Nov 03 2001 Florian La Roche <Florian.LaRoche@redhat.de> 2.2.2-2
- add "reload" to the usage string in the startup script

* Mon Oct 15 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.2-1
- 2.2.2

* Tue Sep 18 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.2.1a-5
- Add patch from Jeremy Allison to fix IA64 alignment problems (#51497)

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Don't include smbpasswd in samba, it's in samba-common (#51598)
- Add a disabled "obey pam restrictions" statement - it's not
  active, as we use encrypted passwords, but if the admin turns
  encrypted passwords off the choice is available. (#31351)

* Wed Aug  8 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Use /var/cache/samba instead of /var/lock/samba 
- Remove "domain controller" keyword from smb.conf, it's 
  deprecated (from #13704)
- Sync some examples with smb.conf.default
- Fix password synchronization (#16987)

* Fri Jul 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Tweaks of BuildRequires (#49581)

* Wed Jul 11 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.2.1a bugfix release

* Tue Jul 10 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.2.1, which should work better for XP

* Sat Jun 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.2.0a security fix
- Mark lograte and pam configuration files as noreplace

* Fri Jun 22 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add the /etc/samba directory to samba-common

* Thu Jun 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add improvements to the smb.conf as suggested in #16931

* Tue Jun 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
  (these changes are from the non-head version)
- Don't include /usr/sbin/samba, it's the same as the initscript
- unset TMPDIR, as samba can't write into a TMPDIR owned 
  by root (#41193)
- Add pidfile: lines for smbd and nmbd and a config: line
  in the initscript  (#15343)
- don't use make -j
- explicitly include /usr/share/samba, not just the files in it

* Tue Jun 19 2001 Bill Nottingham <notting@redhat.com>
- mount.smb/mount.smbfs go in /sbin, *not* %%{_sbindir}

* Fri Jun  8 2001 Preston Brown <pbrown@redhat.com>
- enable encypted passwords by default

* Thu Jun  7 2001 Helge Deller <hdeller@redhat.de> 
- build as 2.2.0-1 release
- skip the documentation-directories docbook, manpages and yodldocs
- don't include *.sgml documentation in package
- moved codepage-directory to /usr/share/samba/codepages
- make it compile with glibc-2.2.3-10 and kernel-headers-2.4.2-2   

* Mon May 21 2001 Helge Deller <hdeller@redhat.de> 
- updated to samba 2.2.0
- moved codepages to %%{_datadir}/samba/codepages
- use all available CPUs for building rpm packages
- use %%{_xxx} defines at most places in spec-file
- "License:" replaces "Copyright:"
- dropped excludearch sparc
- de-activated japanese patches 100 and 200 for now 
  (they need to be fixed and tested wth 2.2.0)
- separated swat.desktop file from spec-file and added
  german translations
- moved /etc/sysconfig/samba to a separate source-file
- use htmlview instead of direct call to netscape in 
  swat.desktop-file

* Mon May  7 2001 Bill Nottingham <notting@redhat.com>
- device-remove security fix again (<tridge@samba.org>)

* Fri Apr 20 2001 Bill Nottingham <notting@redhat.com>
- fix tempfile security problems, officially (<tridge@samba.org>)
- update to 2.0.8

* Sun Apr  8 2001 Bill Nottingham <notting@redhat.com>
- turn of SSL, kerberos

* Thu Apr  5 2001 Bill Nottingham <notting@redhat.com>
- fix tempfile security problems (patch from <Marcus.Meissner@caldera.de>)

* Thu Mar 29 2001 Bill Nottingham <notting@redhat.com>
- fix quota support, and quotas with the 2.4 kernel (#31362, #33915)

* Mon Mar 26 2001 Nalin Dahyabhai <nalin@redhat.com>
- tweak the PAM code some more to try to do a setcred() after initgroups()
- pull in all of the optflags on i386 and sparc
- don't explicitly enable Kerberos support -- it's only used for password
  checking, and if PAM is enabled it's a no-op anyway

* Mon Mar  5 2001 Tim Waugh <twaugh@redhat.com>
- exit successfully from preun script (bug #30644).

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Wed Feb 14 2001 Bill Nottingham <notting@redhat.com>
- updated japanese stuff (#27683)

* Fri Feb  9 2001 Bill Nottingham <notting@redhat.com>
- fix trigger (#26859)

* Wed Feb  7 2001 Bill Nottingham <notting@redhat.com>
- add i18n support, japanese patch (#26253)

* Wed Feb  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- i18n improvements in initscript (#26537)

* Wed Jan 31 2001 Bill Nottingham <notting@redhat.com>
- put smbpasswd in samba-common (#25429)

* Wed Jan 24 2001 Bill Nottingham <notting@redhat.com>
- new i18n stuff

* Sun Jan 21 2001 Bill Nottingham <notting@redhat.com>
- rebuild

* Thu Jan 18 2001 Bill Nottingham <notting@redhat.com>
- i18n-ize initscript
- add a sysconfig file for daemon options (#23550)
- clarify smbpasswd man page (#23370)
- build with LFS support (#22388)
- avoid extraneous pam error messages (#10666)
- add Urban Widmark's bug fixes for smbmount (#19623)
- fix setgid directory modes (#11911)
- split swat into subpackage (#19706)

* Wed Oct 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- set a default CA certificate path in smb.conf (#19010)
- require openssl >= 0.9.5a-20 to make sure we have a ca-bundle.crt file

* Mon Oct 16 2000 Bill Nottingham <notting@redhat.com>
- fix swat only_from line (#18726, others)
- fix attempt to write outside buildroot on install (#17943)

* Mon Aug 14 2000 Bill Nottingham <notting@redhat.com>
- add smbspool back in (#15827)
- fix absolute symlinks (#16125)

* Sun Aug 6 2000 Philipp Knirsch <pknirsch@redhat.com>
- bugfix for smbadduser script (#15148)

* Mon Jul 31 2000 Matt Wilson <msw@redhat.com>
- patch configure.ing (patch11) to disable cups test
- turn off swat by default

* Fri Jul 28 2000 Bill Nottingham <notting@redhat.com>
- fix condrestart stuff

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- add copytruncate to logrotate file (#14360)
- fix init script (#13708)

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back
- remove 'Using Samba' book from %%doc 
- move stuff to /etc/samba (#13708)
- default configuration tweaks (#13704)
- some logrotate tweaks

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 11 2000 Bill Nottingham <notting@redhat.com>
- fix logrotate script (#13698)

* Thu Jul  6 2000 Bill Nottingham <notting@redhat.com>
- fix initscripts req (prereq /etc/init.d)

* Wed Jul 5 2000 Than Ngo <than@redhat.de>
- add initdir macro to handle the initscript directory
- add a new macro to handle /etc/pam.d/system-auth

* Thu Jun 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable Kerberos 5 and SSL support
- patch for duplicate profile.h headers

* Thu Jun 29 2000 Bill Nottingham <notting@redhat.com>
- fix init script

* Tue Jun 27 2000 Bill Nottingham <notting@redhat.com>
- rename samba logs (#11606)

* Mon Jun 26 2000 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jun 16 2000 Bill Nottingham <notting@redhat.com>
- configure the swat stuff usefully
- re-integrate some specfile tweaks that got lost somewhere

* Thu Jun 15 2000 Bill Nottingham <notting@redhat.com>
- rebuild to get rid of cups dependency

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak logrotate configurations to use the PID file in /var/lock/samba

* Sun Jun 11 2000 Bill Nottingham <notting@redhat.com>
- rebuild in new environment

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- change PAM setup to use system-auth

* Mon May  8 2000 Bill Nottingham <notting@redhat.com>
- fixes for ia64

* Sat May  6 2000 Bill Nottingham <notting@redhat.com>
- switch to %%configure

* Wed Apr 26 2000 Nils Philippsen <nils@redhat.de>
- version 2.0.7

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- simplify preun

* Thu Mar 16 2000 Bill Nottingham <notting@redhat.com>
- fix yp_get_default_domain in autoconf
- only link against readline for smbclient
- fix log rotation (#9909)

* Fri Feb 25 2000 Bill Nottingham <notting@redhat.com>
- fix trigger, again.

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- fix trigger.

* Fri Feb  4 2000 Bill Nottingham <notting@redhat.com>
- turn on quota support

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fox dependencies
- man pages are compressed

* Fri Jan 21 2000 Bill Nottingham <notting@redhat.com>
- munge post scripts slightly

* Wed Jan 19 2000 Bill Nottingham <notting@redhat.com>
- turn on mmap again. Wheee.
- ship smbmount on alpha

* Mon Dec  6 1999 Bill Nottingham <notting@redhat.com>
- turn off mmap. ;)

* Wed Dec  1 1999 Bill Nottingham <notting@redhat.com>
- change /var/log/samba to 0700
- turn on mmap support

* Thu Nov 11 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.6

* Fri Oct 29 1999 Bill Nottingham <notting@redhat.com>
- add a %%defattr for -common

* Tue Oct  5 1999 Bill Nottingham <notting@redhat.com>
- shift some files into -client
- remove /home/samba from package.

* Tue Sep 28 1999 Bill Nottingham <notting@redhat.com>
- initscript oopsie. killproc <name> -HUP, not other way around.

* Sat Sep 26 1999 Bill Nottingham <notting@redhat.com>
- script cleanups. Again.

* Wed Sep 22 1999 Bill Nottingham <notting@redhat.com>
- add a patch to fix dropped reconnection attempts

* Mon Sep  6 1999 Jeff Johnson <jbj@redhat.com>
- use cp rather than mv to preserve /etc/services perms (#4938 et al).
- use mktemp to generate /etc/tmp.XXXXXX file name.
- add prereqs on sed/mktemp/killall (need to move killall to /bin).
- fix trigger syntax (i.e. "samba < 1.9.18p7" not "samba < samba-1.9.18p7")

* Mon Aug 30 1999 Bill Nottingham <notting@redhat.com>
- sed "s|nawk|gawk|" /usr/bin/convert_smbpasswd

* Sat Aug 21 1999 Bill Nottingham <notting@redhat.com>
- fix typo in mount.smb

* Fri Aug 20 1999 Bill Nottingham <notting@redhat.com>
- add a %%trigger to work around (sort of) broken scripts in
  previous releases

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Mon Aug  9 1999 Bill Nottingham <notting@redhat.com>
- add domain parsing to mount.smb

* Fri Aug  6 1999 Bill Nottingham <notting@redhat.com>
- add a -common package, shuffle files around.

* Fri Jul 23 1999 Bill Nottingham <notting@redhat.com>
- add a chmod in %%postun so /etc/services & inetd.conf don't become unreadable

* Wed Jul 21 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.5
- fix mount.smb - smbmount options changed again.........
- fix postun. oops.
- update some stuff from the samba team's spec file.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- split off clients into separate package
- don't run samba by default

* Mon Jun 14 1999 Bill Nottingham <notting@redhat.com>
- fix one problem with mount.smb script
- fix smbpasswd on sparc with a really ugly kludge

* Thu Jun 10 1999 Dale Lovelace <dale@redhat.com>
- fixed logrotate script

* Tue May 25 1999 Bill Nottingham <notting@redhat.com>
- turn of 64-bit locking on 32-bit platforms

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- so many releases, so little time
- explicitly uncomment 'printing = bsd' in sample config

* Tue May 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.4a
- fix mount.smb arg ordering

* Fri Apr 16 1999 Bill Nottingham <notting@redhat.com>
- go back to stop/start for restart (-HUP didn't work in testing)

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- add a mount.smb to make smb mounting a little easier.
- smb filesystems apparently don't work on alpha. Oops.

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- always create codepages

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- updated init script to use graceful restart (not stop/start)

* Tue Mar  9 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.3

* Thu Feb 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.2

* Mon Feb 15 1999 Bill Nottingham <notting@redhat.com>
- swat swat

* Tue Feb  9 1999 Bill Nottingham <notting@redhat.com>
- fix bash2 breakage in post script

* Fri Feb  5 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0.0

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- make sure all binaries are stripped

* Thu Sep 17 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.9.18p10.
- fix %%triggerpostun.

* Tue Jul 07 1998 Erik Troan <ewt@redhat.com>
- updated postun triggerscript to check $0
- clear /etc/codepages from %%preun instead of %%postun

* Mon Jun 08 1998 Erik Troan <ewt@redhat.com>
- made the %%postun script a tad less agressive; no reason to remove
  the logs or lock file (after all, if the lock file is still there,
  samba is still running)
- the %%postun and %%preun should only exectute if this is the final
  removal
- migrated %%triggerpostun from Red Hat's samba package to work around
  packaging problems in some Red Hat samba releases

* Sun Apr 26 1998 John H Terpstra <jht@samba.anu.edu.au>
- minor tidy up in preparation for release of 1.9.18p5
- added findsmb utility from SGI package

* Wed Mar 18 1998 John H Terpstra <jht@samba.anu.edu.au>
- Updated version and codepage info.
- Release to test name resolve order

* Sat Jan 24 1998 John H Terpstra <jht@samba.anu.edu.au>
- Many optimisations (some suggested by Manoj Kasichainula <manojk@io.com>
- Use of chkconfig in place of individual symlinks to /etc/rc.d/init/smb
- Compounded make line
- Updated smb.init restart mechanism
- Use compound mkdir -p line instead of individual calls to mkdir
- Fixed smb.conf file path for log files
- Fixed smb.conf file path for incoming smb print spool directory
- Added a number of options to smb.conf file
- Added smbadduser command (missed from all previous RPMs) - Doooh!
- Added smbuser file and smb.conf file updates for username map

