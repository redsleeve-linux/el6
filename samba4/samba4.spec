%define main_release 7

%define samba_version 4.2.10
%define talloc_version 2.0.7
%define ntdb_version 1.0
%define tdb_version 1.2.10
%define tevent_version 0.9.17
%define ldb_version 1.1.12
%define pre_release %nil

%define samba_release %{main_release}%{?dist}

%global with_libsmbclient 0
%global with_libwbclient 0
%global with_libnetapi 0

%global with_clustering_support 0

%global with_pam_smbpass 0
%global with_talloc 0
%global with_tevent 0
%global with_tdb 0
%global with_ntdb 1
%global with_ldb 0

%global with_usrmove 0

%global with_mitkrb5 1
%global with_dc 0

%if %with_usrmove
%global smb_lib %{_libdir}
%else
%global smb_lib %{_lib}
%endif

%{!?python_libdir: %define python_libdir %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1,1)")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           samba4
Version:        %{samba_version}
Release:        %{samba_release}
Epoch:          0

%define samba_depver %{version}-%{release}
%define samba_conflict_ver 3.9.9

Summary:        Server and Client software to interoperate with Windows machines
License:        GPLv3+ and LGPLv3+
Group:          System Environment/Daemons
URL:            http://www.samba.org/

Source0:        samba-%{version}%{pre_release}.tar.bz2

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source4: smb.conf.default
Source5: pam_winbind.conf
Source6: samba.pamd
Source7: samba4.sysconfig

Source100: nmb.init
Source101: smb.init
Source102: winbind.init

Source200: README.dc
Source201: README.downgrade
Patch1: samba-4.2.10-ldap-sasl-win2003.patch
Patch2: samba-4.2.10-s3-parm-clean-up-defaults-when-removing-global-param.patch
Patch3: samba-4.2.10-s3-winbind-make-sure-domain-member-can-talk-to-trust.patch
Patch4: samba-4.2.10-badlock-bugfixes.patch
Patch5: CVE-2016-2119-v4-2.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires(pre): /usr/sbin/groupadd
Requires(post): /sbin/chkconfig, /sbin/service
Requires(preun): /sbin/chkconfig, /sbin/service

Requires(pre): %{name}-common = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

Conflicts: samba < %{samba_conflict_ver}
Provides: samba = %{samba_depver}
Obsoletes: %{name}-swat < %{samba_depver}

%if %with_clustering_support
BuildRequires: ctdb-devel
%endif
BuildRequires: cups-devel
BuildRequires: docbook-style-xsl
BuildRequires: e2fsprogs-devel
BuildRequires: gawk
BuildRequires: krb5-devel >= 1.10
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libuuid-devel
BuildRequires: libxslt
BuildRequires: ncurses-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Parse::Yapp)
BuildRequires: popt-devel
BuildRequires: python-devel
BuildRequires: quota-devel
BuildRequires: readline-devel
BuildRequires: sed
BuildRequires: zlib-devel >= 1.2.3

%if ! %with_talloc
%global libtalloc_version 2.0.7

BuildRequires: libtalloc-devel >= %{libtalloc_version}
BuildRequires: pytalloc-devel >= %{libtalloc_version}
%endif

%if ! %with_tevent
%global libtevent_version 0.9.17

BuildRequires: libtevent-devel >= %{libtevent_version}
BuildRequires: python-tevent >= %{libtevent_version}
%endif

%if ! %with_ldb
%global libldb_version 1.1.11

BuildRequires: libldb-devel >= %{libldb_version}
BuildRequires: pyldb-devel >= %{libldb_version}
%endif

%if ! %with_tdb
%global libtdb_version 1.2.10

BuildRequires: libtdb-devel >= %{libtdb_version}
BuildRequires: python-tdb >= %{libtdb_version}
%endif

# UGLY HACK: Fix 'Provides' for libsmbclient and libwbclient
%if ! %with_libsmbclient && ! %with_libwbclient
%{?filter_setup:
%filter_from_provides /libsmbclient.so.0()/d; /libsmbclient.so.0$/d; /libwbclient.so.0()/d; /libwbclient.so.0$/d; /libnetapi.so.0()/d; /libnetapi.so.0$/d
%filter_from_requires /libsmbclient.so.0()/d; /libsmbclient.so.0$/d; /libwbclient.so.0()/d; /libwbclient.so.0$/d; /libnetapi.so.0()/d; /libnetapi.so.0$/d
%filter_setup
}
%endif

%description
Samba is the standard Windows interoperability suite of programs for Linux and Unix.

%package client
Summary: Samba client programs
Group: Applications/System
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

Conflicts: samba-client < %{samba_conflict_ver}
Provides: samba-client = %{samba_depver}

%description client
The samba4-client package provides some SMB/CIFS clients to complement
the built-in SMB/CIFS filesystem in Linux. These clients allow access
of SMB/CIFS shares and printing to SMB/CIFS printers.

%package libs
Summary: Samba libraries
Group: Applications/System
Requires: krb5-libs >= 1.10
%if %with_libwbclient
Requires: libwbclient
%endif

# Obsolete multilib version of the libraries. The current package
# links against the python library for provision.
Obsoletes: samba4-libs < 4.0.0-30.el6.rc2

%description libs
The samba4-libs package contains the libraries needed by programs that
link against the SMB, RPC and other protocols provided by the Samba suite.

%package python
Summary: Samba Python libraries
Group: Applications/System
Requires: %{name} = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
Requires: python-tevent
Requires: python-tdb
Requires: pyldb
Requires: pytalloc

%description python
The samba4-python package contains the Python libraries needed by programs
that use SMB, RPC and other Samba provided protocols in Python programs.

%package devel
Summary: Developer tools for Samba libraries
Group: Development/Libraries
Requires: %{name}-libs = %{samba_depver}

Conflicts: samba-devel < %{samba_conflict_ver}
Provides: samba-devel = %{samba_depver}

%description devel
The samba4-devel package contains the header files for the libraries
needed to develop programs that link against the SMB, RPC and other
libraries in the Samba suite.

%package pidl
Summary: Perl IDL compiler
Group: Development/Tools
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Parse::Yapp)

%description pidl
The samba4-pidl package contains the Perl IDL compiler used by Samba
and Wireshark to parse IDL and similar protocols

%package common
Summary: Files used by both Samba servers and clients
Group: Applications/System
Requires: %{name}-libs = %{samba_depver}
Requires: logrotate

Conflicts: samba-common < %{samba_conflict_ver}
Provides: samba-common = %{samba_depver}

%description common
samba4-common provides files necessary for both the server and client
packages of Samba.

%package test
Summary: Testing tools for Samba servers and clients
Group: Applications/System
Requires: %{name} = %{samba_depver}
Requires: %{name}-common = %{samba_depver}
%if %with_dc
Requires: %{name}-dc = %{samba_depver}
%endif
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-winbind = %{samba_depver}

%description test
samba4-test provides testing tools for both the server and client
packages of Samba.

%package winbind
Summary: Samba winbind
Group: Applications/System
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}

Conflicts: samba-winbind < %{samba_conflict_ver}
Provides: samba-winbind = %{samba_depver}

%description winbind
The samba-winbind package provides the winbind NSS library, and some
client tools.  Winbind enables Linux to be a full member in Windows
domains and to use Windows user and group accounts on Linux.

%package winbind-krb5-locator
Summary: Samba winbind krb5 locator
Group: Applications/System
Requires: %{name}-winbind = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient
%else
Requires: %{name}-libs = %{samba_depver}
%endif

Conflicts: samba-winbind-krb5-locator < %{samba_conflict_ver}
Provides: samba-winbind-krb5-locator = %{samba_depver}
# Handle winbind_krb5_locator.so as alternatives to allow
# IPA AD trusts case where it should not be used by libkrb5
# The plugin will be diverted to /dev/null by the FreeIPA
# freeipa-server-trust-ad subpackage due to higher priority
# and restored to the proper one on uninstall
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description winbind-krb5-locator
The winbind krb5 locator is a plugin for the system kerberos library to allow
the local kerberos library to use the same KDC as samba and winbind use

%package winbind-clients
Summary: Samba winbind clients
Group: Applications/System
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
%if %with_libwbclient
Requires: libwbclient
%endif
Requires: pam

Conflicts: samba-winbind-clients < %{samba_conflict_ver}

%description winbind-clients
The samba-winbind-clients package provides the NSS library and a PAM
module necessary to communicate to the Winbind Daemon


%if %with_libsmbclient
%package -n libsmbclient
Summary: The SMB client library
Group: Applications/System
Requires: %{name}-common = %{samba_depver}

Conflicts: libsmbclient < %{samba_conflict_ver}
Provides: libsmbclient = %{samba_depver}

%description -n libsmbclient
The libsmbclient contains the SMB client library from the Samba suite.

%package -n libsmbclient-devel
Summary: Developer tools for the SMB client library
Group: Development/Libraries
Requires: libsmbclient = %{samba_depver}

Conflicts: libsmbclient-devel < %{samba_conflict_ver}
Provides: libsmbclient-devel = %{samba_depver}

%description -n libsmbclient-devel
The libsmbclient-devel package contains the header files and libraries needed to
develop programs that link against the SMB client library in the Samba suite.
%endif # with_libsmbclient

%if %with_libwbclient
%package -n libwbclient
Summary: The winbind client library
Group: Applications/System

%description -n libwbclient
The libwbclient package contains the winbind client library from the Samba suite.

%package -n libwbclient-devel
Summary: Developer tools for the winbind library
Group: Development/Libraries
Requires: libwbclient = %{samba_depver}

%description -n libwbclient-devel
The libwbclient-devel package provides developer tools for the wbclient library.
%endif # with_libwbclient

%package dc
Summary: AD Domain Controller placeholder package.
Group: Applications/System
%if %with_dc
Requires: %{name}-libs = %{samba_depver}
Requires: %{name}-dc-libs = %{samba_depver}
Requires: %{name}-python = %{samba_depver}
%endif

%description dc
Placeholder package. Samba AD Domain Controller component is not available.

%package dc-libs
Summary: AD Domain Controller libraries placeholder package.
Group: Applications/System
%if %with_dc
Requires: %{name}-common = %{samba_depver}
Requires: %{name}-libs = %{samba_depver}
%endif

%description dc-libs
Placeholder package. Samba AD Domain Controller component is not available.

%prep
%setup -q -n samba-%{version}%{pre_release}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .samba-4.2.10-badlock-bugfixes.patch
%patch5 -p1 -b .CVE-2016-2119-v4-2.patch

%build
%global _talloc_lib ,talloc,pytalloc,pytalloc-util
%global _tevent_lib ,tevent,pytevent
%global _tdb_lib ,tdb,pytdb
%global _ldb_lib ,ldb,pyldb

%if ! %{with_talloc}
%global _talloc_lib ,!talloc,!pytalloc,!pytalloc-util
%endif

%if ! %{with_tevent}
%global _tevent_lib ,!tevent,!pytevent
%endif

%if ! %{with_tdb}
%global _tdb_lib ,!tdb,!pytdb
%endif

%if ! %{with_ldb}
%global _ldb_lib ,!ldb,!pyldb
%endif

%if ! %{with_ntdb}
%global _ntdb_lib ,!ntdb,!pyntdb
%endif

%global _samba4_libraries heimdal,!zlib,!popt%{_talloc_lib}%{_tevent_lib}%{_tdb_lib}%{_ldb_lib}%{_ntdb_lib}

%global _samba4_idmap_modules idmap_ad,idmap_rid,idmap_adex,idmap_hash,idmap_tdb2
%global _samba4_pdb_modules pdb_tdbsam,pdb_ldap,pdb_ads,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%global _samba4_auth_modules auth_unix,auth_wbc,auth_server,auth_netlogond,auth_script,auth_samba4
# auth_builtin, auth_domain, auth_sam and auth_winbind need to be static

%global _samba4_modules %{_samba4_idmap_modules},%{_samba4_pdb_modules},%{_samba4_auth_modules}

%global _libsmbclient %nil
%global _libwbclient %nil

%if ! %with_libsmbclient
%global _libsmbclient smbclient,
%endif

%if ! %with_libwbclient
%global _libwbclient wbclient,
%endif

%if ! %with_libnetapi
%global _libnetapi netapi,
%endif

%global _samba4_private_libraries %{_libsmbclient}%{_libwbclient}%{_libnetapi}

CFLAGS="-fno-strict-aliasing %{optflags}" CXXFLAGS="-fno-strict-aliasing %{optflags}" \
%configure \
        --enable-fhs \
        --with-piddir=/var/run \
        --with-sockets-dir=/var/run/samba \
        --with-modulesdir=%{_libdir}/samba \
        --with-pammodulesdir=/%{smb_lib}/security \
        --with-lockdir=/var/lib/samba \
        --with-cachedir=/var/lib/samba \
        --disable-gnutls \
        --disable-rpath-install \
        --with-shared-modules=%{_samba4_modules} \
        --bundled-libraries=%{_samba4_libraries} \
        --with-pam \
%if (! %with_libsmbclient) || (! %with_libwbclient) || (! %with_libnetapi)
        --private-libraries=%{_samba4_private_libraries} \
%endif
%if %with_mitkrb5
        --with-system-mitkrb5 \
%endif
%if ! %with_dc
        --without-ad-dc \
%endif
%if %with_clustering_support
        --with-cluster-support \
%endif
%if ! %with_pam_smbpass
        --without-pam_smbpass
%endif

export WAFCACHE=/tmp/wafcache
mkdir -p $WAFCACHE
make %{?_smp_mflags}

# Build PIDL for installation into vendor directories before
# 'make proto' gets to it.
(cd pidl && %{__perl} Makefile.PL INSTALLDIRS=vendor )

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install -d -m 0755 %{buildroot}/usr/{sbin,bin}
install -d -m 0755 %{buildroot}/%{_sysconfdir}/{pam.d,logrotate.d,security}
install -d -m 0755 %{buildroot}/%{smb_lib}/security
install -d -m 0755 %{buildroot}/var/lib/samba
install -d -m 0755 %{buildroot}/var/lib/samba/private
install -d -m 0755 %{buildroot}/var/lib/samba/winbindd_privileged
install -d -m 0755 %{buildroot}/var/lib/samba/scripts
install -d -m 0755 %{buildroot}/var/lib/samba/sysvol
install -d -m 0755 %{buildroot}/var/log/samba/old
install -d -m 0755 %{buildroot}/var/spool/samba
install -d -m 0755 %{buildroot}/var/run/samba
install -d -m 0755 %{buildroot}/var/run/winbindd
install -d -m 0755 %{buildroot}/%{_libdir}/samba
install -d -m 0755 %{buildroot}/%{_libdir}/pkgconfig

# Undo the PIDL install, we want to try again with the right options.
rm -rf %{buildroot}/%{_libdir}/perl5
rm -rf %{buildroot}/%{_datadir}/perl5

# Install PIDL.
( cd pidl && make install PERL_INSTALL_ROOT=%{buildroot} )

# winbind
%if ! %with_usrmove
install -d -m 0755 %{buildroot}%{_libdir}
install -d -m 0755 %{buildroot}/%{smb_lib}
mv -f %{buildroot}/%{_libdir}/libnss_winbind.so.2 %{buildroot}/%{smb_lib}/libnss_winbind.so.2
chmod 0755 %{buildroot}/%{smb_lib}/libnss_winbind.so.2
mv -f %{buildroot}/%{_libdir}/libnss_wins.so.2 %{buildroot}/%{smb_lib}/libnss_wins.so.2
chmod 0755 %{buildroot}/%{smb_lib}/libnss_wins.so.2
%endif
ln -sf /%{smb_lib}/libnss_winbind.so.2  %{buildroot}%{_libdir}/libnss_winbind.so
ln -sf /%{smb_lib}/libnss_wins.so.2  %{buildroot}%{_libdir}/libnss_wins.so

# Install other stuff
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/samba
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/samba/smb.conf
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/security/pam_winbind.conf
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/samba

echo 127.0.0.1 localhost > %{buildroot}%{_sysconfdir}/samba/lmhosts

install -d -m 0755 %{buildroot}%{_sysconfdir}/openldap/schema
install -m644 examples/LDAP/samba.schema %{buildroot}%{_sysconfdir}/openldap/schema/samba.schema

install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/sysconfig/samba

install -d -m 0755 %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 %{SOURCE201} %{buildroot}%{_defaultdocdir}/%{name}/README.downgrade

%if ! %with_dc
install -m 0644 %{SOURCE200} %{buildroot}%{_defaultdocdir}/%{name}/README.dc
install -m 0644 %{SOURCE200} %{buildroot}%{_defaultdocdir}/%{name}/README.dc-libs
%endif

install -d -m 0755 %{buildroot}%{_initrddir}
install -m 0755 %{SOURCE100} %{buildroot}%{_initrddir}/nmb
install -m 0755 %{SOURCE101} %{buildroot}%{_initrddir}/smb
install -m 0755 %{SOURCE102} %{buildroot}%{_initrddir}/winbind

# winbind krb5 locator
install -d -m 0755 %{buildroot}%{_libdir}/krb5/plugins/libkrb5
touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

# cleanup stuff that does not belong here
rm -f %{buildroot}/%{_mandir}/man3/ldb.3*
rm -f %{buildroot}/%{_mandir}/man3/talloc.3*

# Clean out crap left behind by the PIDL install.
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
rm -f %{buildroot}%{perl_vendorlib}/wscript_build
rm -rf %{buildroot}%{perl_vendorlib}/Parse/Yapp

# This makes the right links, as rpmlint requires that
# the ldconfig-created links be recorded in the RPM.
/sbin/ldconfig -N -n %{buildroot}%{_libdir}

# Fix up permission on perl install.
%{_fixperms} %{buildroot}%{perl_vendorlib}

# Remove stuff the buildsystem did not handle correctly
rm -f %{buildroot}/%{smb_lib}/security/pam_smbpass.so
rm -f %{buildroot}%{python_sitelib}/tevent.py

%if ! %with_libwbclient
ln -sf libwbclient.so.0 %{buildroot}%{_libdir}/samba/libwbclient.so
%endif

# Remove files we do not package for RHEL 6 update:
for i in /etc/xinetd.d/swat \
   /usr/share/man/man1/dbwrap_tool.1 \
   /usr/share/man/man1/log2pcap.1 ; do
	rm -f %{buildroot}$i
done

%if ! %with_dc
# Remove files we are not going to packages to avoid issues with debuginfo generator
# which does not support exclusions in file lists
for i in %{_libdir}/samba/ldb/ildap.so \
	 %{_libdir}/samba/ldb/ldbsamba_extensions.so \
	 %{_mandir}/man8/samba-tool.8 \
	 %{_mandir}/man8/samba.8 ; do
	rm -f %{buildroot}$i
done
%endif

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

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%if %with_dc
%post dc-libs -p /sbin/ldconfig

%postun dc-libs -p /sbin/ldconfig
%endif # with_dc

%post test -p /sbin/ldconfig

%postun test -p /sbin/ldconfig

%pre winbind
/usr/sbin/groupadd -g 88 wbpriv >/dev/null 2>&1 || :

%post winbind
/sbin/chkconfig --add winbind
if [ "$1" -ge "1" ]; then
    /sbin/service winbind condrestart >/dev/null 2>&1 || :
fi
exit 0

%preun winbind
if [ $1 = 0 ] ; then
    /sbin/service winbind stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del winbind
fi
exit 0

%post common -p /sbin/ldconfig

%postun common -p /sbin/ldconfig

%post winbind-clients -p /sbin/ldconfig

%postun winbind-clients -p /sbin/ldconfig

%if %with_libsmbclient
%post -n libsmbclient -p /sbin/ldconfig

%postun -n libsmbclient -p /sbin/ldconfig
%endif # with_libsmbclient

%if %with_libwbclient
%post -n libwbclient -p /sbin/ldconfig

%postun -n libwbclient -p /sbin/ldconfig
%endif # with_libwbclient

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/smbstatus
%{_bindir}/eventlogadm
%{_sbindir}/nmbd
%{_sbindir}/smbd
%{_libdir}/samba/auth
%{_libdir}/samba/vfs
%config(noreplace) %{_sysconfdir}/pam.d/samba
%attr(1777,root,root) %dir /var/spool/samba
%dir %{_sysconfdir}/openldap/schema
%{_sysconfdir}/openldap/schema/samba.schema
%{_initrddir}/nmb
%{_initrddir}/smb
%doc %{_defaultdocdir}/%{name}/README.downgrade
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man8/eventlogadm.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/vfs_*.8*

%files libs
%defattr(-,root,root)
%{_libdir}/libdcerpc-binding.so.*
%{_libdir}/libgensec.so.*
%{_libdir}/libndr.so.*
%{_libdir}/libndr-krb5pac.so.*
%{_libdir}/libndr-nbt.so.*
%{_libdir}/libndr-standard.so.*
%{_libdir}/libsamba-credentials.so.*
%{_libdir}/libsamba-passdb.so.*
%{_libdir}/libsamba-util.so.*
%{_libdir}/libsamba-hostconfig.so.*
%{_libdir}/libsamdb.so.*
%{_libdir}/libsmbconf.so.*
%{_libdir}/libsmbclient-raw.so.*
%{_libdir}/libsmbldap.so.*
%{_libdir}/libtevent-util.so.*
%{_libdir}/libregistry.so.*
%{_libdir}/libdcerpc.so.*
%{_libdir}/libdcerpc-atsvc.so.*
%{_libdir}/libdcerpc-samr.so.*
%{_libdir}/libsamba-policy.so.*

%if %with_libnetapi
%{_libdir}/libnetapi.so.*
%endif

# libraries needed by the public libraries
%{_libdir}/samba/libCHARSET3-samba4.so
%{_libdir}/samba/libaddns-samba4.so
%{_libdir}/samba/libads-samba4.so
%{_libdir}/samba/libasn1util-samba4.so
%{_libdir}/samba/libauth-sam-reply-samba4.so
%{_libdir}/samba/libauth-samba4.so
%{_libdir}/samba/libauthkrb5-samba4.so
%{_libdir}/samba/libccan-samba4.so
%{_libdir}/samba/libcli-cldap-samba4.so
%{_libdir}/samba/libcli-ldap-common-samba4.so
%{_libdir}/samba/libcli-ldap-samba4.so
%{_libdir}/samba/libcli-nbt-samba4.so
%{_libdir}/samba/libcli-smb-common-samba4.so
%{_libdir}/samba/libcli-spoolss-samba4.so
%{_libdir}/samba/libcliauth-samba4.so
%{_libdir}/samba/libcmdline-credentials-samba4.so
%{_libdir}/samba/libdbwrap-samba4.so
%{_libdir}/samba/libdcerpc-samba-samba4.so
%{_libdir}/samba/liberrors-samba4.so
%{_libdir}/samba/libevents-samba4.so
%{_libdir}/samba/libflag-mapping-samba4.so
%{_libdir}/samba/libgpo-samba4.so
%{_libdir}/samba/libgse-samba4.so
%{_libdir}/samba/libhttp-samba4.so
%{_libdir}/samba/libinterfaces-samba4.so
%{_libdir}/samba/libkrb5samba-samba4.so
%{_libdir}/samba/libldbsamba-samba4.so
%{_libdir}/samba/liblibcli-lsa3-samba4.so
%{_libdir}/samba/liblibcli-netlogon3-samba4.so
%{_libdir}/samba/liblibsmb-samba4.so
%{_libdir}/samba/libmsrpc3-samba4.so
%{_libdir}/samba/libndr-samba-samba4.so
%{_libdir}/samba/libndr-samba4.so
%{_libdir}/samba/libnet-keytab-samba4.so
%{_libdir}/samba/libnetif-samba4.so
%{_libdir}/samba/libnpa-tstream-samba4.so
%{_libdir}/samba/libprinting-migrate-samba4.so
%{_libdir}/samba/libreplace-samba4.so
%{_libdir}/samba/libsamba-cluster-support-samba4.so
%{_libdir}/samba/libsamba-debug-samba4.so
%{_libdir}/samba/libsamba-modules-samba4.so
%{_libdir}/samba/libsamba-security-samba4.so
%{_libdir}/samba/libsamba-sockets-samba4.so
%{_libdir}/samba/libsamba3-util-samba4.so
%{_libdir}/samba/libsamdb-common-samba4.so
%{_libdir}/samba/libsecrets3-samba4.so
%{_libdir}/samba/libserver-role-samba4.so
%{_libdir}/samba/libsmb-transport-samba4.so
%{_libdir}/samba/libsmbd-base-samba4.so
%{_libdir}/samba/libsmbd-conn-samba4.so
%{_libdir}/samba/libsmbd-shim-samba4.so
%{_libdir}/samba/libsmbldaphelper-samba4.so
%{_libdir}/samba/libsmbregistry-samba4.so
%{_libdir}/samba/libsocket-blocking-samba4.so
%{_libdir}/samba/libtdb-wrap-samba4.so
%{_libdir}/samba/libtrusts-util-samba4.so
%{_libdir}/samba/libutil-cmdline-samba4.so
%{_libdir}/samba/libutil-ntdb-samba4.so
%{_libdir}/samba/libutil-reg-samba4.so
%{_libdir}/samba/libutil-setid-samba4.so
%{_libdir}/samba/libutil-tdb-samba4.so
%{_libdir}/samba/libLIBWBCLIENT-OLD-samba4.so
%{_libdir}/samba/libMESSAGING-samba4.so
%{_libdir}/samba/libauth-unix-token-samba4.so
%{_libdir}/samba/libauth4-samba4.so
%{_libdir}/samba/libcluster-samba4.so
%{_libdir}/samba/libdcerpc-samba4.so
%{_libdir}/samba/libdfs-server-ad-samba4.so
%{_libdir}/samba/libdnsserver-common-samba4.so
%{_libdir}/samba/libnon-posix-acls-samba4.so
%{_libdir}/samba/libsamba-net-samba4.so
%{_libdir}/samba/libsamba-python-samba4.so
%{_libdir}/samba/libshares-samba4.so
%{_libdir}/samba/libsmbpasswdparser-samba4.so
%{_libdir}/samba/libtdb-compat-samba4.so
%{_libdir}/samba/libxattr-tdb-samba4.so

%if %with_dc
%{_libdir}/samba/libdb-glue.so
%{_libdir}/samba/libHDB_SAMBA4.so
%{_libdir}/samba/libasn1-samba4.so.8
%{_libdir}/samba/libasn1-samba4.so.8.0.0
%{_libdir}/samba/libgssapi-samba4.so.2
%{_libdir}/samba/libgssapi-samba4.so.2.0.0
%{_libdir}/samba/libhcrypto-samba4.so.5
%{_libdir}/samba/libhcrypto-samba4.so.5.0.1
%{_libdir}/samba/libhdb-samba4.so.11
%{_libdir}/samba/libhdb-samba4.so.11.0.2
%{_libdir}/samba/libheimbase-samba4.so.1
%{_libdir}/samba/libheimbase-samba4.so.1.0.0
%{_libdir}/samba/libhx509-samba4.so.5
%{_libdir}/samba/libhx509-samba4.so.5.0.0
%{_libdir}/samba/libkrb5-samba4.so.26
%{_libdir}/samba/libkrb5-samba4.so.26.0.0
%{_libdir}/samba/libroken-samba4.so.19
%{_libdir}/samba/libroken-samba4.so.19.0.1
%{_libdir}/samba/libwind-samba4.so.0
%{_libdir}/samba/libwind-samba4.so.0.0.0
%endif

%if %{with_ldb}
%{_libdir}/samba/libldb.so.1
%{_libdir}/samba/libldb.so.%{ldb_version}
%{_libdir}/samba/libpyldb-util.so.1
%{_libdir}/samba/libpyldb-util.so.%{ldb_version}
%endif
%if %{with_talloc}
%{_libdir}/samba/libtalloc.so.2
%{_libdir}/samba/libtalloc.so.%{talloc_version}
%{_libdir}/samba/libpytalloc-util.so.2
%{_libdir}/samba/libpytalloc-util.so.%{talloc_version}
%endif
%if %{with_tevent}
%{_libdir}/samba/libtevent.so.0
%{_libdir}/samba/libtevent.so.%{tevent_version}
%endif
%if %{with_tdb}
%{_libdir}/samba/libtdb.so.1
%{_libdir}/samba/libtdb.so.%{tdb_version}
%endif
## we don't build it for now
%if %{with_ntdb}
%{_libdir}/samba/libntdb.so.*
%endif

%if ! %with_libsmbclient
%{_libdir}/samba/libsmbclient.so.*
# Conflict with libsmbclient-devel package.
%exclude %{_mandir}/man7/libsmbclient.7*
%endif # ! with_libsmbclient

%if ! %with_libwbclient
%{_libdir}/samba/libwbclient.so.*
%{_libdir}/samba/libwinbind-client-samba4.so
%endif # ! with_libwbclient

%if ! %with_libnetapi
%{_libdir}/samba/libnetapi.so.*
%endif # ! with_libnetapi

%files common
%defattr(-,root,root)
#%{_libdir}/samba/charset ???
%{_bindir}/net
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/smbcontrol
%{_bindir}/testparm
%{_datadir}/samba/codepages
%config(noreplace) %{_sysconfdir}/logrotate.d/samba
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%attr(0755,root,root) %dir /var/lib/samba
%dir /var/run/samba
%dir /var/run/winbindd
%attr(700,root,root) %dir /var/lib/samba/private
%attr(755,root,root) %dir %{_sysconfdir}/samba
%config(noreplace) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %{_sysconfdir}/samba/lmhosts
%config(noreplace) %{_sysconfdir}/sysconfig/samba
%{_mandir}/man1/profiles.1*
%{_mandir}/man1/smbcontrol.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man5/lmhosts.5*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man7/samba.7*
%{_mandir}/man8/net.8*
%{_mandir}/man8/pdbedit.8*

# common libraries
%{_libdir}/samba/libpopt-samba3-samba4.so
%{_libdir}/samba/pdb

%if %with_pam_smbpass
/%{smb_lib}/security/pam_smbpass.so
%endif

%files dc
%defattr(-,root,root)
%if %with_dc
%{_bindir}/samba-dig
%{_libdir}/samba/ldb/ildap.so
%{_libdir}/samba/ldb/ldbsamba_extensions.so
%{_libdir}/samba/libldb-cmdline.so
%{_libdir}/samba/libdfs_server_ad.so
%{_libdir}/samba/libdsdb-module.so
%{_bindir}/samba-tool
%{_sbindir}/samba
%{_sbindir}/samba_kcc
%{_sbindir}/samba_dnsupdate
%{_sbindir}/samba_spnupdate
%{_sbindir}/samba_upgradedns
%{_sbindir}/samba_upgradeprovision
%{_libdir}/mit_samba.so
%{_libdir}/samba/bind9/dlz_bind9.so
%{_libdir}/samba/libheimntlm-samba4.so.1
%{_libdir}/samba/libheimntlm-samba4.so.1.0.1
%{_libdir}/samba/libkdc-samba4.so.2
%{_libdir}/samba/libkdc-samba4.so.2.0.0
%{_libdir}/samba/libpac.so
%{_libdir}/samba/gensec
%dir /var/lib/samba/sysvol
%{_datadir}/samba/setup
%{_mandir}/man8/samba-tool.8*
%{_mandir}/man8/samba.8*
%else # with_dc
%doc %{_defaultdocdir}/%{name}/README.dc
%endif # with_dc

%files dc-libs
%defattr(-,root,root)
%if %with_dc
%{_libdir}/samba/libprocess_model.so
%{_libdir}/samba/libservice.so
%{_libdir}/samba/process_model
%{_libdir}/samba/service
%{_libdir}/libdcerpc-server.so.*
%{_libdir}/samba/libntvfs.so
%{_libdir}/samba/libposix_eadb.so
%{_libdir}/samba/bind9/dlz_bind9_9.so
%else
%doc %{_defaultdocdir}/%{name}/README.dc-libs
%endif # with_dc

%files winbind
%defattr(-,root,root)
#%{_bindir}/wbinfo3
%{_libdir}/samba/idmap
%{_libdir}/samba/nss_info
%{_libdir}/samba/libnss-info-samba4.so
%{_libdir}/samba/libidmap-samba4.so
%{_sbindir}/winbindd
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%{_mandir}/man8/winbindd.8*
%{_mandir}/man8/idmap_*.8*
#%{_datadir}/locale/*/LC_MESSAGES/pam_winbind.mo
%{_initrddir}/winbind

%files winbind-krb5-locator
%defattr(-,root,root)
%ghost %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so
%{_libdir}/winbind_krb5_locator.so
%{_mandir}/man7/winbind_krb5_locator.7*

%files winbind-clients
%defattr(-,root,root)
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%{_libdir}/libnss_winbind.so
/%{smb_lib}/libnss_winbind.so.2
%{_libdir}/libnss_wins.so
/%{smb_lib}/libnss_wins.so.2
/%{smb_lib}/security/pam_winbind.so
%config(noreplace) %{_sysconfdir}/security/pam_winbind.conf
%{_mandir}/man1/ntlm_auth.1.gz
%{_mandir}/man1/wbinfo.1*
%{_mandir}/man5/pam_winbind.conf.5*
%{_mandir}/man8/pam_winbind.8*

%files client
%defattr(-,root,root)
%{_bindir}/cifsdd
%{_bindir}/dbwrap_tool
%{_bindir}/nmblookup
%{_bindir}/oLschema2ldif
%{_bindir}/regdiff
%{_bindir}/regpatch
%{_bindir}/regshell
%{_bindir}/regtree
%{_bindir}/rpcclient
%{_bindir}/sharesec
%{_bindir}/smbcacls
%{_bindir}/smbclient
%{_bindir}/smbcquotas
%{_bindir}/smbget
#%{_bindir}/smbiconv
%{_bindir}/smbpasswd
%{_bindir}/smbspool
%{_bindir}/smbta-util
%{_bindir}/smbtree
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/oLschema2ldif.1*
%{_mandir}/man1/regdiff.1*
%{_mandir}/man1/regpatch.1*
%{_mandir}/man1/regshell.1*
%{_mandir}/man1/regtree.1*
%exclude %{_mandir}/man1/findsmb.1*
%{_mandir}/man1/rpcclient.1*
%{_mandir}/man1/sharesec.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/smbcquotas.1*
%{_mandir}/man1/smbget.1*
%{_mandir}/man5/smbgetrc.5*
%exclude %{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbtree.1*
%{_mandir}/man8/smbpasswd.8*
%{_mandir}/man8/smbspool.8*
%{_mandir}/man8/smbta-util.8*

## we don't build it for now
%if %{with_ntdb}
%{_bindir}/ntdbbackup
%{_bindir}/ntdbdump
%{_bindir}/ntdbrestore
%{_bindir}/ntdbtool
%{_mandir}/man8/ntdbbackup.8*
%{_mandir}/man8/ntdbdump.8*
%{_mandir}/man8/ntdbrestore.8*
%{_mandir}/man8/ntdbtool.8*
%else
%exclude %{_mandir}/man8/ntdbbackup.8*
%exclude %{_mandir}/man8/ntdbdump.8*
%exclude %{_mandir}/man8/ntdbrestore.8*
%exclude %{_mandir}/man8/ntdbtool.8*
%endif

%if %{with_tdb}
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbrestore
%{_bindir}/tdbtool
%{_mandir}/man8/tdbbackup.8.gz
%{_mandir}/man8/tdbdump.8.gz
%{_mandir}/man8/tdbrestore.8.gz
%{_mandir}/man8/tdbtool.8.gz
%endif

%{_bindir}/samba-regedit
%{_bindir}/smbtar
%{_mandir}/man8/samba-regedit.8*

%if %with_ldb
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbrename
%{_bindir}/ldbsearch
%{_mandir}/man1/ldbadd.1.gz
%{_mandir}/man1/ldbdel.1.gz
%{_mandir}/man1/ldbedit.1.gz
%{_mandir}/man1/ldbmodify.1.gz
%{_mandir}/man1/ldbrename.1.gz
%{_mandir}/man1/ldbsearch.1.gz
%endif

%files test
%defattr(-,root,root)
%{_bindir}/gentest
%{_bindir}/locktest
%{_bindir}/masktest
%{_bindir}/ndrdump
%{_bindir}/smbtorture
%{_libdir}/libtorture.so.*
%{_libdir}/samba/libsubunit-samba4.so
%if %with_dc
%{_libdir}/samba/libdlz-bind9-for-torture.so
%else
%{_libdir}/samba/libdsdb-module-samba4.so
%endif
%{_mandir}/man1/gentest.1*
%{_mandir}/man1/locktest.1*
%{_mandir}/man1/masktest.1*
%{_mandir}/man1/ndrdump.1*
%{_mandir}/man1/smbtorture.1*
%{_mandir}/man1/vfstest.1*

%files devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/charset.h
%{_includedir}/samba-4.0/core/doserr.h
%{_includedir}/samba-4.0/core/error.h
%{_includedir}/samba-4.0/core/hresult.h
%{_includedir}/samba-4.0/core/ntstatus.h
%{_includedir}/samba-4.0/core/werror.h
%{_includedir}/samba-4.0/credentials.h
%{_includedir}/samba-4.0/dcerpc.h
%{_includedir}/samba-4.0/dlinklist.h
%{_includedir}/samba-4.0/tstream_smbXcli_np.h
%{_includedir}/samba-4.0/domain_credentials.h
%{_includedir}/samba-4.0/gen_ndr/atsvc.h
%{_includedir}/samba-4.0/gen_ndr/auth.h
%{_includedir}/samba-4.0/gen_ndr/dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/epmapper.h
%{_includedir}/samba-4.0/gen_ndr/krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/lsa.h
%{_includedir}/samba-4.0/gen_ndr/mgmt.h
%{_includedir}/samba-4.0/gen_ndr/misc.h
%{_includedir}/samba-4.0/gen_ndr/nbt.h
%{_includedir}/samba-4.0/gen_ndr/drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_atsvc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_atsvc_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_epmapper.h
%{_includedir}/samba-4.0/gen_ndr/ndr_epmapper_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/ndr_mgmt.h
%{_includedir}/samba-4.0/gen_ndr/ndr_mgmt_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_misc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_nbt.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl_c.h
%{_includedir}/samba-4.0/gen_ndr/netlogon.h
%{_includedir}/samba-4.0/gen_ndr/samr.h
%{_includedir}/samba-4.0/gen_ndr/security.h
%{_includedir}/samba-4.0/gen_ndr/server_id.h
%{_includedir}/samba-4.0/gen_ndr/svcctl.h
%{_includedir}/samba-4.0/gensec.h
%{_includedir}/samba-4.0/ldap-util.h
%{_includedir}/samba-4.0/ldap_errors.h
%{_includedir}/samba-4.0/ldap_message.h
%{_includedir}/samba-4.0/ldap_ndr.h
%{_includedir}/samba-4.0/ldb_wrap.h
%{_includedir}/samba-4.0/lookup_sid.h
%{_includedir}/samba-4.0/machine_sid.h
%{_includedir}/samba-4.0/ndr.h
%{_includedir}/samba-4.0/ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/ndr/ndr_nbt.h
%{_includedir}/samba-4.0/netapi.h
%{_includedir}/samba-4.0/param.h
%{_includedir}/samba-4.0/passdb.h
%{_includedir}/samba-4.0/policy.h
%{_includedir}/samba-4.0/read_smb.h
%{_includedir}/samba-4.0/registry.h
%{_includedir}/samba-4.0/roles.h
%{_includedir}/samba-4.0/rpc_common.h
%{_includedir}/samba-4.0/samba/session.h
%{_includedir}/samba-4.0/samba/version.h
%{_includedir}/samba-4.0/share.h
%{_includedir}/samba-4.0/smb2.h
%{_includedir}/samba-4.0/smb2_constants.h
%{_includedir}/samba-4.0/smb2_create_blob.h
%{_includedir}/samba-4.0/smb2_lease.h
%{_includedir}/samba-4.0/smb2_lease_struct.h
%{_includedir}/samba-4.0/smb2_signing.h
%{_includedir}/samba-4.0/smb_cli.h
%{_includedir}/samba-4.0/smb_cliraw.h
%{_includedir}/samba-4.0/smb_common.h
%{_includedir}/samba-4.0/smb_composite.h
%{_includedir}/samba-4.0/smbconf.h
%{_includedir}/samba-4.0/smb_constants.h
%{_includedir}/samba-4.0/smb_ldap.h
%{_includedir}/samba-4.0/smbldap.h
%{_includedir}/samba-4.0/smb_raw.h
%{_includedir}/samba-4.0/smb_raw_interfaces.h
%{_includedir}/samba-4.0/smb_raw_signing.h
%{_includedir}/samba-4.0/smb_raw_trans2.h
%{_includedir}/samba-4.0/smb_request.h
%{_includedir}/samba-4.0/smb_seal.h
%{_includedir}/samba-4.0/smb_signing.h
%{_includedir}/samba-4.0/smb_unix_ext.h
%{_includedir}/samba-4.0/smb_util.h
%{_includedir}/samba-4.0/tdr.h
# libtorture is not supported in RHEL6.
%exclude %{_includedir}/samba-4.0/torture.h
%{_includedir}/samba-4.0/tsocket.h
%{_includedir}/samba-4.0/tsocket_internal.h
%{_includedir}/samba-4.0/samba_util.h
%{_includedir}/samba-4.0/util/attr.h
%{_includedir}/samba-4.0/util/byteorder.h
%{_includedir}/samba-4.0/util/data_blob.h
%{_includedir}/samba-4.0/util/debug.h
%{_includedir}/samba-4.0/util/memory.h
%{_includedir}/samba-4.0/util/safe_string.h
%{_includedir}/samba-4.0/util/string_wrappers.h
%{_includedir}/samba-4.0/util/talloc_stack.h
%{_includedir}/samba-4.0/util/tevent_ntstatus.h
%{_includedir}/samba-4.0/util/tevent_unix.h
%{_includedir}/samba-4.0/util/tevent_werror.h
%{_includedir}/samba-4.0/util/time.h
%{_includedir}/samba-4.0/util/xfile.h
%{_includedir}/samba-4.0/util_ldb.h
%{_includedir}/samba-4.0/util/blocking.h
%{_includedir}/samba-4.0/util/fault.h
%{_includedir}/samba-4.0/util/idtree.h
%{_includedir}/samba-4.0/util/idtree_random.h
%{_includedir}/samba-4.0/util/signal.h
%{_includedir}/samba-4.0/util/substitute.h
%{_libdir}/libdcerpc-atsvc.so
%{_libdir}/libdcerpc-binding.so
%{_libdir}/libdcerpc-samr.so
%{_libdir}/libdcerpc.so
%{_libdir}/libgensec.so
%{_libdir}/libndr-krb5pac.so
%{_libdir}/libndr-nbt.so
%{_libdir}/libndr-standard.so
%{_libdir}/libndr.so
%if %with_libnetapi
%{_libdir}/libnetapi.so
%{_libdir}/pkgconfig/netapi.pc
%endif
%{_libdir}/libregistry.so
%{_libdir}/libsamba-credentials.so
%{_libdir}/libsamba-hostconfig.so
%{_libdir}/libsamba-policy.so
%{_libdir}/libsamba-util.so
%{_libdir}/libsamdb.so
%{_libdir}/libsmbclient-raw.so
%{_libdir}/libsmbconf.so
%{_libdir}/libtevent-util.so
# libtorture is not supported in RHEL6.
%exclude %{_libdir}/libtorture.so
%{_libdir}/pkgconfig/dcerpc.pc
%{_libdir}/pkgconfig/dcerpc_atsvc.pc
%{_libdir}/pkgconfig/dcerpc_samr.pc
%{_libdir}/pkgconfig/gensec.pc
%{_libdir}/pkgconfig/ndr.pc
%{_libdir}/pkgconfig/ndr_krb5pac.pc
%{_libdir}/pkgconfig/ndr_nbt.pc
%{_libdir}/pkgconfig/ndr_standard.pc
%{_libdir}/pkgconfig/registry.pc
%{_libdir}/pkgconfig/samba-credentials.pc
%{_libdir}/pkgconfig/samba-hostconfig.pc
%{_libdir}/pkgconfig/samba-policy.pc
%{_libdir}/pkgconfig/samba-util.pc
%{_libdir}/pkgconfig/samdb.pc
%{_libdir}/pkgconfig/smbclient-raw.pc
# libtorture is not supported in RHEL6.
%exclude %{_libdir}/pkgconfig/torture.pc
%{_libdir}/libsamba-passdb.so
%{_libdir}/libsmbldap.so

%if %with_dc
%{_includedir}/samba-4.0/dcerpc_server.h
%{_libdir}/libdcerpc-server.so
%{_libdir}/pkgconfig/dcerpc_server.pc
%endif

%if %with_talloc
%{_includedir}/samba-4.0/pytalloc.h
%endif

%if ! %with_libsmbclient
%{_includedir}/samba-4.0/libsmbclient.h
%endif # ! with_libsmbclient

%if ! %with_libwbclient
%{_libdir}/samba/libwbclient.so
%{_includedir}/samba-4.0/wbclient.h
%endif # ! with_libwbclient
%{_mandir}/man3/ntdb.3*

%files python
%defattr(-,root,root,-)
%{python_sitearch}/*

%files pidl
%defattr(-,root,root,-)
%{perl_vendorlib}/Parse/Pidl*
%{_mandir}/man1/pidl*
%{_mandir}/man3/Parse::Pidl*
%attr(755,root,root) %{_bindir}/pidl

%if %with_libsmbclient
%files -n libsmbclient
%defattr(-,root,root)
%attr(755,root,root) %{_libdir}/libsmbclient.so.*

%files -n libsmbclient-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/libsmbclient.h
%{_includedir}/samba-4.0/smb_share_modes.h
%{_libdir}/libsmbclient.so
%{_libdir}/pkgconfig/smbclient.pc
%{_mandir}/man7/libsmbclient.7*
%endif # with_libsmbclient

%if %with_libwbclient
%files -n libwbclient
%defattr(-,root,root)
%{_libdir}/samba/wbclient/libwbclient.so.*
%{_libdir}/samba/libwinbind-client-samba4.so

%files -n libwbclient-devel
%defattr(-,root,root)
%{_includedir}/samba-4.0/wbclient.h
%{_libdir}/samba/wbclient/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc
%endif # with_libwbclient

%changelog
* Tue Jul 05 2016 Andreas Schneider <asn@redhat.com> - 4.2.10-7
- resolves: #1351957 - Fix CVE-2016-2119

* Tue Apr 12 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-6
- Fix domain member winbind not being able to talk to trusted domains' DCs
- Related: #1322689

* Mon Apr 11 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-5
- Fix crash in smb.conf processing
- Related: #1322689

* Fri Apr 08 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-4
- Fix LDAP SASL handling for arcfour-hmac-md5
- resolves: #1322689

* Thu Apr 07 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-3
- Make sure the package owns /var/lib/samba and uses it for cache purposes
- resolves: #1322689

* Wed Apr 06 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-2
- Remove ldb modules which only needed for DC build
- resolves: #1322689

* Mon Apr 04 2016 Alexander Bokovoy <abokovoy@redhat.com> - 4.2.10-1
- resolves: #1322689

* Fri Mar 04 2016 Andreas Schneider <asn@redhat.com> - 4.0.0-68.rc4
- resolves: #1314670 - Fix CVE-2015-7560

* Fri Dec 11 2015 Andreas Schneider <asn@redhat.com> - 4.0.0-67.rc4
- resolves: #1290709 - CVE-2015-7540
- related: #1290709 - CVE-2015-5299
- related: #1290709 - CVE-2015-5296
- related: #1290709 - CVE-2015-5252
- related: #1290709 - CVE-2015-5330

* Mon Feb 16 2015 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-66.rc4
- related: #1191388 - Update patchset for CVE-2015-0240.

* Thu Feb 12 2015 Andreas Schneider <asn@redhat.com> - 4.0.0-65.rc4
- resolves: #1191388 - CVE-2015-0240: RCE in netlogon.

* Fri Aug 01 2014 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-64.rc4
- resolves: #1126012 - CVE-2014-3560: remote code execution in nmbd.

* Fri Jun 27 2014 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-63.rc4
- Set correct defaults for client min/max protocol options in winbindd
- resolves: #1061596

* Wed Jun 11 2014 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-62.rc4
- resolves: #1105502 - CVE-2014-0244: DoS in nmbd.
- resolves: #1108843 - CVE-2014-3493: DoS in smbd with unicode path names.
- resolves: #1105572 - CVE-2014-0178: Uninitialized memory exposure.

* Fri Mar 07 2014 - Andreas Schneider <asn@redhat.com> - 4.0.0-61.rc4
- resolves: #1073356 - Fix CVE-2012-6150.
- resolves: #1073356 - Fix CVE-2013-4496.
- resolves: #1073356 - Fix CVE-2013-6442.

* Mon Nov 25 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-60.rc4
- resolves: #1073356 - Fix CVE-2013-4408.

* Tue Oct 22 2013 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-59.rc4
- Fix usage of client min/max protocol options in winbindd
- related: #949993

* Wed Sep 11 2013 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-58.rc4
- Fix winbind lsat reconnection code, avoids ntlmv2-only session setup problems
- resolves: #949993

* Tue Aug 06 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-57.rc4
- resolves: #984809 - CVE-2013-4124: DoS via integer overflow when reading
                      an EA list

* Wed Jun 12 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-56.rc4
- Fix libwbclient.so.0 symlink.
- resolves: #882338
- Fix correct linking of libreplace with cmdline-credentials.
- resolves: #911264

* Wed Jan 23 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-55.rc4
- Fix dependencies of samba4-test package.
- related: #896142

* Thu Jan 17 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-54.rc4
- Fix summary and description of dc subpackages.
- resolves: #896142
- Remove conflicting libsmbclient.7 manpage.
- resolves: #896240

* Wed Jan 16 2013 - Andreas Schneider <asn@redhat.com> - 4.0.0-53.rc4
- Fix provides filter rules to remove conflicting libraries from samba4-libs.
- resolves: #895718

* Mon Dec 17 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-52.rc4
- Fix typo in winbind-krb-locator post uninstall script.
- related: #864889

* Fri Dec 14 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-51.rc4
- Make sure we use the same directory as samba package for the winbind pipe.
- resolves: #886157

* Mon Dec 10 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-50.rc4
- Fix typo in winbind-krb-locator post uninstall script.
- related: #864889

* Mon Dec 10 2012 - Guenther Deschner <gdeschner@redhat.com> - 4.0.0-49.rc4
- Fix Netlogon AES encryption.
- resolves: #885089

* Fri Nov 30 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-48.rc4
- Fix IPA trust AD lookup of users.
- resolves: #878564

* Wed Nov 21 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-47.rc4
- Add require for krb5-libs >= 1.10 to samba4-libs.
- resolves: #877533

* Thu Nov 15 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-46.rc4
- Rename /etc/sysconfig/samba4 to name to mach init scripts.
- resolves: #877085

* Thu Nov 15 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-45.rc4
- Don't require samba4-common and samba4-test in samba4-devel package.
- related: #871748

* Tue Nov 06 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-44.rc4
- Make libnetapi and internal library to fix dependencies.
- resolves: #873491

* Mon Nov 05 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-43.rc4
- Move libnetapi and internal printing migration lib to libs package.
- related: #766333

* Mon Nov 05 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-42.rc4
- Fix perl, pam and logrotate dependencies.
- related: #766333

* Mon Nov 05 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-41.rc4
- Fix library dependencies found by rpmdiff.
- Update winbind offline logon patch.
- related: #766333

* Thu Nov 01 2012 - Sumit Bose <sbose@redhat.com> - 4.0.0-40.rc4
- Move libgpo to samba-common
- resolves: #871748

* Tue Oct 30 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-39.rc4
- Rebase to version 4.0.0rc4.
- related: #766333

* Mon Oct 22 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-38.rc3
- Add missing export KRB5CCNAME in init scripts.
- resolves: #868419

* Fri Oct 19 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-37.rc3
- Move /var/log/samba to samba-common package for winbind which
  requires it.
- resolves: #868248

* Thu Oct 18 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-36.rc3
- The standard auth modules need to be built into smbd to function.
- resolves: #867854

* Wed Oct 17 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-35.rc3
- Move pam_winbind.conf to the package of the module.
- resolves: #867317

* Tue Oct 16 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-34.rc3
- Built auth_builtin as static module.
- related: #766333

* Tue Oct 16 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-33.rc3
- Add back the AES patches which didn't make it in rc3.
- related: #766333

* Tue Oct 16 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-32.rc3
- Rebase to version 4.0.0rc3.
- related: #766333

* Wed Oct 10 2012 - Alexander Bokovoy <abokovoy@redhat.com> - 4.0.0-31.rc2
- Use alternatives to configure winbind_krb5_locator.so
- resolves: #864889

* Thu Oct 04 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-30.rc2
- Fix multilib package installation.
- resolves: #862047
- Filter out libsmbclient and libwbclient provides.
- resolves: #861892
- Rebase to version 4.0.0rc2.
- related: #766333

* Tue Sep 25 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-29.rc1
- Fix Requires and Conflicts.
- related: #766333

* Tue Sep 25 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-28.rc1
- Move pam_winbind and wbinfo manpages to the right subpackage.
- related: #766333

* Tue Sep 25 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-27.rc1
- Fix permission for init scripts.
- Define a common KRB5CCNAME for smbd and winbind.
- Set piddir back to /var/run in RHEL6.
- related: #766333

* Mon Sep 24 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-26.rc1
- Add "-fno-strict-aliasing" to CFLAGS again.
- related: #766333

* Mon Sep 24 2012 - Andreas Schneider <asn@redhat.com> - 4.0.0-25.rc1
- Build with syste libldb package which has been just added.
- related: #766333

* Wed Sep 19 2012 - Andreas Schneider <asn@redhat.com> 4.0.0-24.rc1
- Rebase to version 4.0.0rc1.
- resolves: #766333

* Mon Jun 07 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-23.alpha11
- Add "-fno-strict-aliasing" to CFLAGS (RH bug #596209)

* Mon Feb 01 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-22.alpha11
- Upgrade to alpha11 (RH bug #560025)

* Fri Jan 29 2010 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-19.1.alpha8_git20090916
- Fix rpmlint warnings.

* Mon Jan 11 2010 Stepan Kasal <skasal@redhat.com> - 4.0.0-19.alpha8_git20090916
- fix typo in samba4_release
- rebuild against perl-5.10.1

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 4.0.0-18.1alpha8_git20090916.1
- Rebuilt for RHEL 6

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.1.alpha8_git20090916
- Need docbook stuff to build man pages

* Thu Sep 17 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-18.alpha8_git20090916
- Fix broken dependencies

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-17.alpha8_git20090916
- Upgrade to alpha8-git20090916

* Wed Sep 16 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-16.alpha7
- Stop building libtevent, it is now an external package

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-15.2alpha7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-15.2alpha7
- Fix dependency

* Sat May 09 2009  Simo Sorce <ssorce@redhat.com> - 4.0.0-15.1alpha7
- Don't build talloc and tdb, they are now separate packages

* Mon Apr 06 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-14alpha7
- Fix a build issue in samba4-common (RH bug #494243).

* Wed Mar 25 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-13alpha7
- rebuild with correct CFLAGS (also fixes debuginfo)

* Tue Mar 10 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-12alpha7
- Second part of fix for the ldb segfault problem from upstream

* Mon Mar 09 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-11alpha7
- Add upstream patch to fix a problem within ldb

* Sun Mar 08 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-10alpha7
- Remove ldb.pc from samba4-devel (RH bug #489186).

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-9alpha7
- Make talloc,tdb,tevent,ldb easy to exclude using defines
- Fix package for non-mock "dirty" systems by deleting additional
  files we are not interested in atm

* Wed Mar  4 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-8alpha7
- Fix typo in Requires

* Mon Mar  2 2009 Simo Sorce <ssorce@redhat.com> - 4.0.0-7alpha7
- Compile and have separate packages for additional samba libraries
  Package in their own packages: talloc, tdb, tevent, ldb

* Fri Feb 27 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-4.alpha7
- Update to 4.0.0alpha7

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-3.alpha6
- Formal package review cleanups.

* Mon Feb 23 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-2.alpha6
- Disable subpackages not needed by OpenChange.
- Incorporate package review feedback.

* Mon Jan 19 2009 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-1.alpha6
- Update to 4.0.0alpha6

* Wed Dec 17 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.8.alpha6.GIT.3508a66
- Fix another file conflict: smbstatus

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.7.alpha6.GIT.3508a66
- Disable the winbind subpackage because it conflicts with samba-winbind
  and isn't needed to support OpenChange.

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 4.0.0-0.6.alpha6.GIT.3508a66
- Update to the GIT revision OpenChange is now requiring.

* Fri Aug 29 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.5.alpha5.fc10
- Fix licence tag (the binaries are built into a GPLv3 whole, so the BSD licence need not be mentioned)

* Fri Jul 25 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.4.alpha5.fc10
- Remove talloc and tdb dependency (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)
- Fix deps on chkconfig and service to main pkg (not -common) 
  (per https://bugzilla.redhat.com/show_bug.cgi?id=453083)

* Mon Jul 21 2008 Brad Hards <bradh@frogmouth.ent> - 0:4.0.0-0.3.alpha5.fc10
- Use --sysconfdir instead of --with-configdir
- Add patch for C++ header compatibility

* Mon Jun 30 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.2.alpha5.fc9
- Update per review feedback
- Update for alpha5

* Thu Jun 26 2008 Andrew Bartlett <abartlet@samba.org> - 0:4.0.0-0.1.alpha4.fc9
- Rework Fedora's Samba 3.2.0-1.rc2.16 spec file for Samba4
