%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

# we don't want to provide private python extension libs
%define __provides_exclude_from %{python_sitearch}.*.so$

# we need to directly link against libsmbclient from samba4-libs
# because package libcmbclient depends on samba3 which conflict with dependencies of ipa-server-trust-ad
#
# sh$ rpm -ql libsmbclient | grep smbclient.so
# /usr/lib64/libsmbclient.so.0
# sh$ rpm -ql samba4-libs | grep smbclient.so
# /usr/lib64/samba/libsmbclient.so.0
# /usr/lib64/samba/libsmbclient.so.0.2.0
%filter_from_requires /libsmbclient.so.0/d
# Do not check the NFS plugin for requires to avoid pulling in nfs-utils
# see RHBZ#1340927
%filter_from_requires /libnfsidmap.so.0/d
%filter_setup

# Determine the location of the LDB modules directory
%global ldb_modulesdir %(pkg-config --variable=modulesdir ldb)
%global ldb_version 1.1.13

Name: sssd
Version: 1.13.3
Release: 22%{?dist}.6
Group: Applications/System
Summary: System Security Services Daemon
License: GPLv3+
URL: http://fedorahosted.org/sssd/
Source0: https://fedorahosted.org/released/sssd/%{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

### Patches ###
Patch0001: 0001-nfs-idmap-fix-infinite-loop.patch
Patch0002: 0002-Use-right-domain-for-user-lookups.patch
Patch0003: 0003-sdap_save_grpmem-determine-domain-by-SID-if-possible.patch
Patch0004: 0004-ipa_s2n_save_objects-use-configured-user-and-group-t.patch
Patch0005: 0005-ldap-remove-originalMeberOf-if-there-is-no-memberOf.patch
Patch0006: 0006-SPEC-Change-package-ownership-of-pubconfpath-krb5.in.patch
Patch0007: 0007-AD-SRV-prefer-site-local-DCs-in-LDAP-ping.patch
Patch0008: 0008-KRB5-Adding-DNS-SRV-lookup-for-krb5-provider.patch
Patch0009: 0009-SDAP-do-not-fail-if-refs-are-found-but-not-processed.patch
Patch0010: 0010-sudo-remove-unused-param-name-in-sdap_sudo_get_usn.patch
Patch0011: 0011-sudo-remove-unused-param.-in-ldap_get_sudo_options.patch
Patch0012: 0012-SDAP-Add-request-that-iterates-over-all-search-bases.patch
Patch0013: 0013-SDAP-rename-sdap_get_id_specific_filter.patch
Patch0014: 0014-SDAP-support-empty-filters-in-sdap_combine_filters.patch
Patch0015: 0015-SUDO-use-sdap_search_bases-instead-custom-sb-iterato.patch
Patch0016: 0016-SUDO-make-sudo-sysdb-interface-more-reusable.patch
Patch0017: 0017-SUDO-move-code-shared-between-ldap-and-ipa-to-separa.patch
Patch0018: 0018-SUDO-allow-to-disable-ptask.patch
Patch0019: 0019-SUDO-fail-on-failed-request-that-cannot-be-retry.patch
Patch0020: 0020-IPA-add-ipa_get_rdn-and-ipa_check_rdn.patch
Patch0021: 0021-SDAP-use-ipa_get_rdn-in-nested-groups.patch
Patch0022: 0022-IPA-SUDO-choose-between-IPA-and-LDAP-schema.patch
Patch0023: 0023-IPA-SUDO-Add-ipasudorule-mapping.patch
Patch0024: 0024-IPA-SUDO-Add-ipasudocmdgrp-mapping.patch
Patch0025: 0025-IPA-SUDO-Add-ipasudocmd-mapping.patch
Patch0026: 0026-IPA-SUDO-Implement-sudo-handler.patch
Patch0027: 0027-IPA-SUDO-Implement-full-refresh.patch
Patch0028: 0028-IPA-SUDO-Implement-rules-refresh.patch
Patch0029: 0029-IPA-SUDO-Remember-USN.patch
Patch0030: 0030-SDAP-Add-sdap_or_filters.patch
Patch0031: 0031-IPA-SUDO-Implement-smart-refresh.patch
Patch0032: 0032-SUDO-sdap_sudo_set_usn-do-not-steal-usn.patch
Patch0033: 0033-SUDO-remove-full_refresh_in_progress.patch
Patch0034: 0034-SUDO-assume-zero-if-usn-is-unknown.patch
Patch0035: 0035-SUDO-allow-disabling-full-refresh.patch
Patch0036: 0036-SUDO-remember-usn-as-number-instead-of-string.patch
Patch0037: 0037-SUDO-simplify-usn-filter.patch
Patch0038: 0038-IPA-SUDO-Add-support-for-ipaSudoRunAsExt-attributes.patch
Patch0039: 0039-UTIL-allow-to-skip-default-options-for-child-process.patch
Patch0040: 0040-DP_TASK-add-be_ptask_get_timeout.patch
Patch0041: 0041-AD-add-task-to-renew-the-machine-account-password-if.patch
Patch0042: 0042-FO-add-fo_get_active_server.patch
Patch0043: 0043-FO-add-be_fo_get_active_server_name.patch
Patch0044: 0044-AD-try-to-use-current-server-in-the-renewal-task.patch
Patch0045: 0045-SDAP-Make-it-possible-to-silence-errors-from-derefer.patch
Patch0046: 0046-sdap_connect_send-fail-if-uri-or-sockaddr-is-NULL.patch
Patch0047: 0047-p11-add-gnome-screensaver-to-list-of-allowed-service.patch
Patch0048: 0048-IDMAP-Fix-computing-max-id-for-slice-range.patch
Patch0049: 0049-IDMAP-New-structure-for-domain-range-params.patch
Patch0050: 0050-IDMAP-Add-support-for-automatic-adding-of-ranges.patch
Patch0051: 0051-NSS-do-not-skip-cache-check-for-netgoups.patch
Patch0052: 0052-IDMAP-Man-change-for-ldap_idmap_range_size-option.patch
Patch0053: 0053-NSS-Fix-memory-leak-netgroup.patch
Patch0054: 0054-SDAP-Add-return-code-ERR_ACCOUNT_LOCKED.patch
Patch0055: 0055-PAM-Pass-account-lockout-status-and-display-message.patch
Patch0056: 0056-PAM-Fix-man-for-pam_account_-expired-locked-_message.patch
Patch0057: 0057-remove-user-certificate-if-not-found-on-the-server.patch
Patch0058: 0058-UTIL-Backport-error-code-ERR_ACCOUNT_LOCKED.patch
Patch0059: 0059-CLIENT-Reduce-code-duplication.patch
Patch0060: 0060-CLIENT-Retry-request-after-EPIPE.patch
Patch0061: 0061-IPA-SUDO-fix-typo.patch
Patch0062: 0062-IPA-SUDO-support-old-ipasudocmd-rdn.patch
Patch0063: 0063-pam_sss-reorder-pam_message-array.patch
Patch0064: 0064-SUDO-be-able-to-parse-modifyTimestamp-correctly.patch
Patch0065: 0065-tests-Extend-test_child_common.c-to-include-tests-fo.patch
Patch0066: 0066-UTIL-exit-the-forked-process-if-exec-ing-a-child-pro.patch
Patch0067: 0067-AD-Do-not-schedule-the-machine-renewal-task-if-adcli.patch
Patch0068: 0068-LDAP-Try-also-the-AD-access-control-for-IPA-users.patch
Patch0069: 0069-AD-Do-not-leak-file-descriptors-during-machine-passw.patch
Patch0070: 0070-Do-not-leak-fds-in-case-of-failures-setting-up-a-chi.patch
Patch0071: 0071-GPO-ignore-non-KVP-lines-if-possible.patch
Patch0072: 0072-gpo-gPCMachineExtensionNames-with-just-whitespaces.patch

### Dependencies ###
Requires: sssd-common = %{version}-%{release}
Requires: sssd-ldap = %{version}-%{release}
Requires: sssd-krb5 = %{version}-%{release}
Requires: sssd-ipa = %{version}-%{release}
Requires: sssd-common-pac = %{version}-%{release}
Requires: sssd-ad = %{version}-%{release}
Requires: sssd-proxy = %{version}-%{release}
Requires: python-sssdconfig = %{version}-%{release}

%global servicename sssd
%global sssdstatedir %{_localstatedir}/lib/sss
%global dbpath %{sssdstatedir}/db
%global keytabdir %{sssdstatedir}/keytabs
%global pipepath %{sssdstatedir}/pipes
%global mcpath %{sssdstatedir}/mc
%global pubconfpath %{sssdstatedir}/pubconf
%global gpocachepath %{sssdstatedir}/gpo_cache

### Build Dependencies ###

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: m4
BuildRequires: popt-devel
BuildRequires: libtalloc-devel
BuildRequires: libtevent-devel
BuildRequires: libtdb-devel
BuildRequires: libldb-devel >= %{ldb_version}
BuildRequires: libdhash-devel >= 0.4.2
BuildRequires: libcollection-devel
BuildRequires: libini_config-devel >= 1.1.0-11.el6_8.1
BuildRequires: dbus-devel
BuildRequires: dbus-libs
BuildRequires: openldap-devel
BuildRequires: pam-devel
BuildRequires: nss-devel
BuildRequires: nspr-devel
BuildRequires: pcre-devel
BuildRequires: libxslt
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
# Make sure krb5-devel with backported localauth plugin is around
BuildRequires: krb5-devel >= 1.10.3-42
BuildRequires: c-ares-devel
BuildRequires: python-devel
BuildRequires: check-devel
BuildRequires: doxygen
BuildRequires: libselinux-devel
BuildRequires: libsemanage-devel
BuildRequires: bind-utils
BuildRequires: keyutils-libs-devel
BuildRequires: gettext-devel
BuildRequires: pkgconfig
BuildRequires: diffstat
BuildRequires: findutils
BuildRequires: glib2-devel
BuildRequires: selinux-policy-targeted >= 3.7.19-166
BuildRequires: libnl3-devel
BuildRequires: nfs-utils-lib-devel
BuildRequires: samba4-devel >= 4.0.0-59beta2
BuildRequires: libsmbclient-devel

%description
Provides a set of daemons to manage access to remote directories and
authentication mechanisms. It provides an NSS and PAM interface toward
the system and a pluggable backend system to connect to multiple different
account sources. It is also the basis to provide client auditing and policy
services for projects like FreeIPA.

The sssd subpackage is a meta-package that contains the deamon as well as all
the existing back ends.

%package common
Summary: Common files for the SSSD
Group: Applications/System
License: GPLv3+
# Conflicts
Conflicts: selinux-policy < 3.7.19-166
Conflicts: sssd < 1.10.0-8%{?dist}.beta2
# Requires
Requires: libldb%{?_isa} >= %{ldb_version}
Requires: libtdb%{?_isa} >= 1.1.3
Requires: sssd-client%{?_isa} = %{version}-%{release}
Requires: libsss_idmap%{?_isa} = %{version}-%{release}
Requires: libini_config >= 1.1.0-11.el6_8.1
Requires(post): initscripts chkconfig
Requires(preun): initscripts chkconfig
Requires(postun): initscripts chkconfig


### Provides ###
Provides: libsss_sudo = %{version}-%{release}
Obsoletes: libsss_sudo <= 1.10.0-7%{?dist}.beta1
Provides: libsss_sudo-devel = %{version}-%{release}
Obsoletes: libsss_sudo-devel <= 1.10.0-7%{?dist}.beta1
Provides: libsss_autofs = %{version}-%{release}
Obsoletes: libsss_autofs <= 1.10.0-7%{?dist}.beta1

%description common
Common files for the SSSD. The common package includes all the files needed
to run a particular back end, however, the back ends are packaged in separate
subpackages such as sssd-ldap.

%package client
Summary: SSSD Client libraries for NSS and PAM
Group: Applications/System
License: LGPLv3+
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description client
Provides the libraries needed by the PAM and NSS stacks to connect to the SSSD
service.

%package tools
Summary: Userspace tools for use with the SSSD
Group: Applications/System
License: GPLv3+
Requires: sssd-common = %{version}-%{release}
Requires: python-sss = %{version}-%{release}
Requires: python-sssdconfig = %{version}-%{release}

%description tools
Provides userspace tools for manipulating users, groups, and nested groups in
SSSD when using id_provider = local in /etc/sssd/sssd.conf.

Also provides several other administrative tools:
    * sss_debuglevel to change the debug level on the fly
    * sss_seed which pre-creates a user entry for use in kickstarts
    * sss_obfuscate for generating an obfuscated LDAP password

%package -n python-sssdconfig
Summary: SSSD and IPA configuration file manipulation classes and functions
Group: Applications/System
License: GPLv3+
BuildArch: noarch

%description -n python-sssdconfig
Provides python2 files for manipulation SSSD and IPA configuration files.

%package -n python-sss
Summary: Python2 bindings for sssd
Group: Development/Libraries
License: LGPLv3+
Requires: sssd-common = %{version}-%{release}

%description -n python-sss
Provides python2 module for manipulating users, groups, and nested groups in
SSSD when using id_provider = local in /etc/sssd/sssd.conf.

Also provides several other useful python2 bindings:
    * function for retrieving list of groups user belongs to.
    * class for obfuscation of passwords

%package -n python-sss-murmur
Summary: Python2 bindings for murmur hash function
Group: Development/Libraries
License: LGPLv3+

%description -n python-sss-murmur
Provides python2 module for calculating the murmur hash version 3

%package ldap
Summary: The LDAP back end of the SSSD
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: sssd-common = %{version}-%{release}
Requires: sssd-krb5-common = %{version}-%{release}

%description ldap
Provides the LDAP back end that the SSSD can utilize to fetch identity data
from and authenticate against an LDAP server.

%package krb5-common
Summary: SSSD helpers needed for Kerberos and GSSAPI authentication
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: cyrus-sasl-gssapi%{?_isa}
Requires: sssd-common = %{version}-%{release}

%description krb5-common
Provides helper processes that the LDAP and Kerberos back ends can use for
Kerberos user or host authentication.

%package krb5
Summary: The Kerberos authentication back end for the SSSD
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: sssd-common = %{version}-%{release}
Requires: sssd-krb5-common = %{version}-%{release}

%description krb5
Provides the Kerberos back end that the SSSD can utilize authenticate
against a Kerberos server.

%package common-pac
Summary: Common files needed for supporting PAC processing
Group: Applications/System
License: GPLv3+
Requires: sssd-common = %{version}-%{release}

%description common-pac
Provides common files needed by SSSD providers such as IPA and Active Directory
for handling Kerberos PACs.

%package ipa
Summary: The IPA back end of the SSSD
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: sssd-common = %{version}-%{release}
Requires: sssd-krb5-common = %{version}-%{release}
Requires: libipa_hbac%{?_isa} = %{version}-%{release}
Requires: bind-utils
Requires: sssd-common-pac = %{version}-%{release}

%description ipa
Provides the IPA back end that the SSSD can utilize to fetch identity data
from and authenticate against an IPA server.

%package ad
Summary: The AD back end of the SSSD
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: sssd-common = %{version}-%{release}
Requires: sssd-krb5-common = %{version}-%{release}
Requires: bind-utils
Requires: sssd-common-pac = %{version}-%{release}

%description ad
Provides the Active Directory back end that the SSSD can utilize to fetch
identity data from and authenticate against an Active Directory server.

%package proxy
Summary: The proxy back end of the SSSD
Group: Applications/System
License: GPLv3+
Conflicts: sssd < 1.10.0-8.beta2
Requires: sssd-common = %{version}-%{release}

%description proxy
Provides the proxy back end which can be used to wrap an existing NSS and/or
PAM modules to leverage SSSD caching.

%package -n libsss_idmap
Summary: FreeIPA Idmap library
Group: Development/Libraries
License: LGPLv3+
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libsss_idmap
Utility library to convert SIDs to Unix uids and gids

%package -n libsss_idmap-devel
Summary: FreeIPA Idmap library
Group: Development/Libraries
License: LGPLv3+
Requires: libsss_idmap = %{version}-%{release}

%description -n libsss_idmap-devel
Utility library to SIDs to Unix uids and gids

%package -n libipa_hbac
Summary: FreeIPA HBAC Evaluator library
Group: Development/Libraries
License: LGPLv3+
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libipa_hbac
Utility library to validate FreeIPA HBAC rules for authorization requests

%package -n libipa_hbac-devel
Summary: FreeIPA HBAC Evaluator library
Group: Development/Libraries
License: LGPLv3+
Requires: libipa_hbac = %{version}-%{release}

%description -n libipa_hbac-devel
Utility library to validate FreeIPA HBAC rules for authorization requests

%package -n python-libipa_hbac
Summary: Python2 bindings for the FreeIPA HBAC Evaluator library
Group: Development/Libraries
License: LGPLv3+
Requires: libipa_hbac = %{version}-%{release}
Provides: libipa_hbac-python = %{version}-%{release}
Obsoletes: libipa_hbac-python < 1.12.90

%description -n python-libipa_hbac
The python-libipa_hbac contains the bindings so that libipa_hbac can be
used by Python applications.

%package -n libsss_nss_idmap
Summary: Library for SID based lookups
Group: Development/Libraries
License: LGPLv3+
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libsss_nss_idmap
Utility library for SID based lookups

%package -n libsss_nss_idmap-devel
Summary: Library for SID based lookups
Group: Development/Libraries
License: LGPLv3+
Requires: libsss_nss_idmap = %{version}-%{release}

%description -n libsss_nss_idmap-devel
Utility library for SID based lookups

%package -n python-libsss_nss_idmap
Summary: Python2 bindings for libsss_nss_idmap
Group: Development/Libraries
License: LGPLv3+
Requires: libsss_nss_idmap = %{version}-%{release}
Provides: libsss_nss_idmap-python = %{version}-%{release}
Obsoletes: libsss_nss_idmap-python < 1.12.90

%description -n python-libsss_nss_idmap
The python-libsss_nss_idmap contains the bindings so that libsss_nss_idmap can
be used by Python applications.

%package dbus
Summary: The D-Bus responder of the SSSD
Group: Applications/System
License: GPLv3+
Requires: sssd-common = %{version}-%{release}

%description dbus
Provides the D-Bus responder of the SSSD, called the InfoPipe, that allows
the information from the SSSD to be transmitted over the system bus.

%package -n libsss_simpleifp
Summary: The SSSD D-Bus responder helper library
Group: Development/Libraries
License: GPLv3+
Requires: dbus-libs
Requires: sssd-dbus = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libsss_simpleifp
Provides library that simplifies D-Bus API for the SSSD InfoPipe responder.

%package -n libsss_simpleifp-devel
Summary: The SSSD D-Bus responder helper library
Group: Development/Libraries
License: GPLv3+
Requires: dbus-devel
Requires: libsss_simpleifp = %{version}-%{release}

%description -n libsss_simpleifp-devel
Provides library that simplifies D-Bus API for the SSSD InfoPipe responder.

%prep
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build, where "Level"
# is the patch prefix option (e.g. -p1)
# Taken from specfile for python-simplejson
UpdateTimestamps() {
  Level=$1
  PatchFile=$2

  # Locate the affected files:
  for f in $(diffstat $Level -l $PatchFile); do
    # Set the files to have the same timestamp as that of the patch:
    touch -r $PatchFile $f
  done
}

%setup -q

for p in %patches ; do
    %__patch -p1 -i $p
    UpdateTimestamps -p1 $p
done

%build
autoreconf -ivf

%configure \
    --with-test-dir=/dev/shm \
    --with-db-path=%{dbpath} \
    --with-mcache-path=%{mcpath} \
    --with-pipe-path=%{pipepath} \
    --with-pubconf-path=%{pubconfpath} \
    --with-gpo-cache-path=%{gpocachepath} \
    --with-init-dir=%{_initrddir} \
    --with-krb5-rcache-dir=%{_localstatedir}/cache/krb5rcache \
    --enable-nsslibdir=/%{_lib} \
    --enable-pammoddir=/%{_lib}/security \
    --enable-nfsidmaplibdir=%{_libdir}/libnfsidmap \
    --disable-static \
    --disable-rpath \
    --without-libwbclient \
    --disable-config-lib \
    --disable-cifs-idmap-plugin \
    --without-python3-bindings \
    --with-ad-gpo-default=permissive \
    SMBCLIENT_LIBS="-rpath %{_libdir}/samba/ %{_libdir}/samba/libsmbclient.so.0"

make %{?_smp_mflags} all docs

%check
export CK_TIMEOUT_MULTIPLIER=10
make %{?_smp_mflags} check
unset CK_TIMEOUT_MULTIPLIER

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Prepare language files
/usr/lib/rpm/find-lang.sh $RPM_BUILD_ROOT sssd

# Copy default logrotate file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d
install -m644 src/examples/logrotate $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/sssd

# Make sure SSSD is able to run on read-only root
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rwtab.d
install -m644 src/examples/rwtab $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/sssd

# Remove .la files created by libtool
find $RPM_BUILD_ROOT -name "*.la" -exec rm -f {} \;

# Suppress developer-only documentation
rm -Rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}

# Older versions of rpmbuild can only handle one -f option
# So we need to append to the sssd*.lang file
for file in `ls $RPM_BUILD_ROOT/%{python_sitelib}/*.egg-info 2> /dev/null`
do
    echo %{python_sitelib}/`basename $file` >> python_sssdconfig.lang
done

touch sssd_tools.lang
touch sssd_client.lang
for provider in ldap krb5 ipa ad proxy
do
    touch sssd_$provider.lang
done

for man in `find $RPM_BUILD_ROOT/%{_mandir}/??/man?/ -type f | sed -e "s#$RPM_BUILD_ROOT/%{_mandir}/##"`
do
    lang=`echo $man | cut -c 1-2`
    case `basename $man` in
        sss_cache*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd.lang
            ;;
        sss_*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_tools.lang
            ;;
        sssd_krb5_*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_client.lang
            ;;
        pam_sss*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_client.lang
            ;;
        sssd-ldap*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_ldap.lang
            ;;
        sssd-krb5*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_krb5.lang
            ;;
        sssd-ipa*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_ipa.lang
            ;;
        sssd-ad*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_ad.lang
            ;;
        sssd-proxy*)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd_proxy.lang
            ;;
        *)
            echo \%lang\(${lang}\) \%{_mandir}/${man}\* >> sssd.lang
            ;;
    esac
done

# Print these to the rpmbuild log
echo "sssd.lang:"
cat sssd.lang

echo "sssd_client.lang:"
cat sssd_client.lang

echo "sssd_tools.lang:"
cat sssd_tools.lang

for provider in ldap krb5 ipa ad proxy
do
    echo "sssd_$provider.lang:"
    cat sssd_$provider.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING

%files common -f sssd.lang
%defattr(-,root,root,-)
%doc COPYING
%doc src/examples/sssd-example.conf
%{_sbindir}/sssd
%{_initrddir}/%{name}

%dir %{_libexecdir}/%{servicename}
%{_libexecdir}/%{servicename}/sssd_be
%{_libexecdir}/%{servicename}/sssd_nss
%{_libexecdir}/%{servicename}/sssd_pam
%{_libexecdir}/%{servicename}/sssd_autofs
%{_libexecdir}/%{servicename}/sssd_ssh
%{_libexecdir}/%{servicename}/sssd_sudo
%{_libexecdir}/%{servicename}/p11_child

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libsss_simple.so

#Internal shared libraries
%{_libdir}/%{name}/libsss_child.so
%{_libdir}/%{name}/libsss_crypt.so
%{_libdir}/%{name}/libsss_cert.so
%{_libdir}/%{name}/libsss_debug.so
%{_libdir}/%{name}/libsss_krb5_common.so
%{_libdir}/%{name}/libsss_ldap_common.so
%{_libdir}/%{name}/libsss_util.so
%{_libdir}/%{name}/libsss_semanage.so

# 3rd party application libraries
%{_libdir}/sssd/modules/libsss_autofs.so
%{_libdir}/libsss_sudo.so
%{_libdir}/libnfsidmap/sss.so

%{ldb_modulesdir}/memberof.so
%{_bindir}/sss_ssh_authorizedkeys
%{_bindir}/sss_ssh_knownhostsproxy
%{_sbindir}/sss_cache
%{_libexecdir}/%{servicename}/sss_signal

%dir %{sssdstatedir}
%dir %{_localstatedir}/cache/krb5rcache
%attr(700,root,root) %dir %{dbpath}
%attr(755,root,root) %dir %{mcpath}
%ghost %attr(0644,root,root) %verify(not md5 size mtime) %{mcpath}/passwd
%ghost %attr(0644,root,root) %verify(not md5 size mtime) %{mcpath}/group
%ghost %attr(0644,root,root) %verify(not md5 size mtime) %{mcpath}/initgroups
%attr(755,root,root) %dir %{pipepath}
%attr(755,root,root) %dir %{pubconfpath}
%attr(755,root,root) %dir %{gpocachepath}
%attr(700,root,root) %dir %{pipepath}/private
%attr(750,root,root) %dir %{_var}/log/%{name}
%attr(700,root,root) %dir %{_sysconfdir}/sssd
%ghost %attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sssd/sssd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/sssd
%config(noreplace) %{_sysconfdir}/rwtab.d/sssd
%dir %{_datadir}/sssd
%{_datadir}/sssd/sssd.api.conf
%{_datadir}/sssd/sssd.api.d
%{_mandir}/man1/sss_ssh_authorizedkeys.1*
%{_mandir}/man1/sss_ssh_knownhostsproxy.1*
%{_mandir}/man5/sssd.conf.5*
%{_mandir}/man5/sssd-simple.5*
%{_mandir}/man5/sssd-sudo.5*
%{_mandir}/man5/sss_rpcidmapd.5*
%{_mandir}/man8/sssd.8*
%{_mandir}/man8/sss_cache.8*

%files ldap -f sssd_ldap.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/%{name}/libsss_ldap.so
%{_mandir}/man5/sssd-ldap.5*

%files krb5-common
%defattr(-,root,root,-)
%doc COPYING
%attr(755,root,root) %dir %{pubconfpath}/krb5.include.d
%{_libexecdir}/%{servicename}/ldap_child
%{_libexecdir}/%{servicename}/krb5_child

%files krb5 -f sssd_krb5.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/%{name}/libsss_krb5.so
%{_mandir}/man5/sssd-krb5.5*

%files common-pac
%defattr(-,root,root,-)
%doc COPYING
%{_libexecdir}/%{servicename}/sssd_pac

%files ipa -f sssd_ipa.lang
%defattr(-,root,root,-)
%doc COPYING
%attr(700,root,root) %dir %{keytabdir}
%{_libdir}/%{name}/libsss_ipa.so
%{_libexecdir}/%{servicename}/selinux_child
%{_mandir}/man5/sssd-ipa.5*

%files ad -f sssd_ad.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/%{name}/libsss_ad.so
%{_libexecdir}/%{servicename}/gpo_child
%{_mandir}/man5/sssd-ad.5*

%files proxy
%defattr(-,root,root,-)
%doc COPYING
%{_libexecdir}/%{servicename}/proxy_child
%{_libdir}/%{name}/libsss_proxy.so

%files dbus
%defattr(-,root,root,-)
%doc COPYING
%{_libexecdir}/%{servicename}/sssd_ifp
%{_mandir}/man5/sssd-ifp.5*
# InfoPipe DBus plumbing
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.sssd.infopipe.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.sssd.infopipe.service

%files -n libsss_simpleifp
%defattr(-,root,root,-)
%{_libdir}/libsss_simpleifp.so.*

%files -n libsss_simpleifp-devel
%defattr(-,root,root,-)
%doc sss_simpleifp_doc/html
%{_includedir}/sss_sifp.h
%{_includedir}/sss_sifp_dbus.h
%{_libdir}/libsss_simpleifp.so
%{_libdir}/pkgconfig/sss_simpleifp.pc

%files client -f sssd_client.lang
%defattr(-,root,root,-)
%doc src/sss_client/COPYING src/sss_client/COPYING.LESSER
/%{_lib}/libnss_sss.so.2
/%{_lib}/security/pam_sss.so
%{_libdir}/krb5/plugins/libkrb5/sssd_krb5_locator_plugin.so
%{_libdir}/krb5/plugins/authdata/sssd_pac_plugin.so
%{_libdir}/%{name}/modules/sssd_krb5_localauth_plugin.so
%{_mandir}/man8/pam_sss.8*
%{_mandir}/man8/sssd_krb5_locator_plugin.8*

%files tools -f sssd_tools.lang
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/sss_useradd
%{_sbindir}/sss_userdel
%{_sbindir}/sss_usermod
%{_sbindir}/sss_groupadd
%{_sbindir}/sss_groupdel
%{_sbindir}/sss_groupmod
%{_sbindir}/sss_groupshow
%{_sbindir}/sss_obfuscate
%{_sbindir}/sss_override
%{_sbindir}/sss_debuglevel
%{_sbindir}/sss_seed
%{_mandir}/man8/sss_groupadd.8*
%{_mandir}/man8/sss_groupdel.8*
%{_mandir}/man8/sss_groupmod.8*
%{_mandir}/man8/sss_groupshow.8*
%{_mandir}/man8/sss_useradd.8*
%{_mandir}/man8/sss_userdel.8*
%{_mandir}/man8/sss_usermod.8*
%{_mandir}/man8/sss_obfuscate.8*
%{_mandir}/man8/sss_override.8*
%{_mandir}/man8/sss_debuglevel.8*
%{_mandir}/man8/sss_seed.8*

%files -n python-sssdconfig -f python_sssdconfig.lang
%defattr(-,root,root,-)
%dir %{python_sitelib}/SSSDConfig
%{python_sitelib}/SSSDConfig/*.py*

%files -n python-sss
%defattr(-,root,root,-)
%{python_sitearch}/pysss.so

%files -n python-sss-murmur
%defattr(-,root,root,-)
%{python_sitearch}/pysss_murmur.so

%files -n libsss_idmap
%defattr(-,root,root,-)
%doc src/sss_client/COPYING src/sss_client/COPYING.LESSER
%{_libdir}/libsss_idmap.so.*

%files -n libsss_idmap-devel
%defattr(-,root,root,-)
%doc idmap_doc/html
%{_includedir}/sss_idmap.h
%{_libdir}/libsss_idmap.so
%{_libdir}/pkgconfig/sss_idmap.pc

%files -n libipa_hbac
%defattr(-,root,root,-)
%doc src/sss_client/COPYING src/sss_client/COPYING.LESSER
%{_libdir}/libipa_hbac.so.*

%files -n libipa_hbac-devel
%defattr(-,root,root,-)
%doc hbac_doc/html
%{_includedir}/ipa_hbac.h
%{_libdir}/libipa_hbac.so
%{_libdir}/pkgconfig/ipa_hbac.pc

%files -n libsss_nss_idmap
%defattr(-,root,root,-)
%doc src/sss_client/COPYING src/sss_client/COPYING.LESSER
%{_libdir}/libsss_nss_idmap.so.*

%files -n libsss_nss_idmap-devel
%defattr(-,root,root,-)
%doc nss_idmap_doc/html
%{_includedir}/sss_nss_idmap.h
%{_libdir}/libsss_nss_idmap.so
%{_libdir}/pkgconfig/sss_nss_idmap.pc

%files -n python-libsss_nss_idmap
%defattr(-,root,root,-)
%{python_sitearch}/pysss_nss_idmap.so

%files -n python-libipa_hbac
%defattr(-,root,root,-)
%{python_sitearch}/pyhbac.so

%post common
/sbin/chkconfig --add %{servicename}

# sssd-1.8.0-24 changed the startup order
# We need to make sure this is always updated on
# clients
/sbin/chkconfig %{servicename} resetpriorities

if [ $1 -ge 1 ] ; then
    restorecon -R %{mcachepath} 2>/dev/null || :
fi

%posttrans
/sbin/service %{servicename} condrestart 2>&1 > /dev/null

%preun common
if [ $1 -eq 0 ] ; then
    /sbin/service %{servicename} stop 2>&1 > /dev/null
    /sbin/chkconfig --del %{servicename}
fi

%post client -p /sbin/ldconfig

%postun client -p /sbin/ldconfig

%post -n libipa_hbac -p /sbin/ldconfig

%postun -n libipa_hbac -p /sbin/ldconfig

%post -n libsss_idmap -p /sbin/ldconfig

%postun -n libsss_idmap -p /sbin/ldconfig

%changelog
* Thu Dec  1 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.6
- Explicitly Require the matching version of ding-libs
- Related: rhbz#1379580 - SSSD fails to process GPO from Active Directory.

* Tue Sep 27 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.5
- Resolves: rhbz#1379580 - SSSD fails to process GPO from Active Directory.

* Tue Jun 21 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.4
- Resolves: rhbz#1348538 - sssd-common requires libnfsidmap

* Thu Jun  9 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.3
- Resolves: rhbz#1344657 - The AD keytab renewal task leaks a file descriptor

* Thu Jun  2 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.2
- Resolves: rhbz#1342058 - In IPA-AD trust environment access is granted
                           to AD user even if the user is disabled on AD.

* Thu Jun  2 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22.1
- Resolves: rhbz#1343638 - sssd_be doesn't terminate forked child process

* Thu Mar 17 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-22
- Resolves: rhbz#1312062 - sssd does not pass LDAP rules to sudo

* Wed Mar 16 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-21
- Resolves: rhbz#1313940 - SSSD PAM module does not support multiple
                           password prompts (e.g. Password + Token) with sudo

* Wed Mar 16 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-20
- Actually apply patches from previous build
- Resolves: rhbz#1313940 - sudorule not working with ipa sudo_provider

* Mon Mar 14 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-19
- Resolves: rhbz#1313940 - sudorule not working with ipa sudo_provider

* Fri Mar 11 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-18
- Resolves: rhbz#1209600 - Getting ERROR (getpwnam() failed): Broken pipe
                           with 1.11.6

* Tue Mar  1 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-17
- Backport of a more minimal dependency patch to avoid changes to AD
  provider behaviour
- Related: rhbz#1264705 - Allow SSSD to notify user of denial due to AD
                          account lockout

* Tue Mar  1 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-16
- Resolves: rhbz#1308939 - After removing certificate from user in IPA
                           and even after sss_cache, FindByCertificate
                           still finds the user

* Tue Feb 16 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-15
- Require a newer selinux-policy to avoid issues when prompting for SC PIN
- Related: rhbz#1299066 - smartcard login does not prompt for pin when
                          ocsp checking is enabled (default config)

* Wed Feb 10 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-14
- Resolves: rhbz#1264705 - Allow SSSD to notify user of denial due to AD
                           account lockout

* Thu Feb  4 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-14
- Resolves: rhbz#1259687 - sssd_nss memory usage keeps growing on
                            sssd-1.12.4-47.el6.x86_64 (RHEL6.7) when
                            trying to retrieve non-existing netgroups

* Thu Feb  4 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-13
- Update sssd-ldap man page for the recent ID mapping changes
- Related: rhbz#1268902 - SSSD doesn't set the ID mapping range automatically

* Wed Jan 27 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-12
- Resolves: rhbz#1295883 - refresh_expired_interval stops sss_cache
                           from working

* Thu Jan 21 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-11
- Resolves: rhbz#1268902 - SSSD doesn't set the ID mapping range automatically

* Thu Jan 21 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-10
- Resolves: rhbz#1298253 - Screen lock prompts for smartcard user password
                           and not smartcard pin when logged in using smartcard
                           pin

* Wed Jan 20 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-9
- Resolves: rhbz#1292458 - sssd_be AD segfaults on missing A record

* Tue Jan 19 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-8
- Resolves: rhbz#1262981 - sssd dereference processing failed : Input/output
                           error

* Tue Jan 19 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-7
- Resolves: rhbz#1290761 - [RFE] Support Automatic Renewing of Kerberos
                           Host Keytabs

* Tue Jan 19 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-6
- Resolves: rhbz#1244957 - [RFE] SUDO: Support the IPA schema

* Mon Jan 18 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-5
- Resolves: rhbz#1298634 - Cannot retrieve users after upgrade from 1.12
                           to 1.13

* Mon Jan 18 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-4
- Resolves: rhbz#1287807 - SRV lookup for KDC servers doesn't work

* Tue Jan 12 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-3
- Resolves: rhbz#1273802 - ad_site parameter does not work

* Tue Jan 12 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-2
- Fix memory leak in the NFS plugin
- Related: rhbz#1269820 - Rebase SSSD to 1.13.x in RHEL-6.8
- Resolves: rhbz#1296620 - Properly remove OriginalMemberOf attribute in
                           SSSD cache if user has no secondary groups anymore
- Resolves: rhbz#1283898 - MAN: Clarify that subdomains always use service
                           discovery

* Tue Dec 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.3-1
- Rebase to 1.13.3
- Remove setuid bit from proxy_child, RHEL-6 doesn't support running
  SSSD as a non-privileged user
- Resolves: rhbz#1269820 - Rebase SSSD to 1.13.x in RHEL-6.8

* Thu Dec 10 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-7
- Don't own files as the SSSD user
- Resolves: rhbz#1289482 - warning: user sssd does not exist - using root

* Mon Nov 30 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-6
- Resolves: rhbz#1279971 - groups get deleted from the cache

* Fri Nov 27 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-5
- The p11_child doesn't have to run privileged anymore, remove the
  setuid bit
- Related: rhbz#1270027 - [RFE] Support for smart cards

* Thu Nov 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-4
- Resolves: rhbz#1266108 - Check next certificate on smart card if first
                           is not valid
- Also enable OCSP checks

* Thu Nov 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-3
- Resolves: rhbz#1285852 - sssd: [sysdb_add_user] (0x0400): Error: 17
                           (File exists)

* Thu Nov 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-2
- Silence compilation warnings and Coverity issues
- Related: rhbz#1269820 - Rebase SSSD to 1.13.x in RHEL-6.8

* Thu Nov 19 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.2-1
- Resolves: rhbz#1269820 - Rebase SSSD to 1.13.x in RHEL-6.8
- Squash in packaging review changes by lslebodn@redhat.com

* Thu Oct 29 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.13.1-1
- Resolves: rhbz#1269820 - Rebase SSSD to 1.13.x in RHEL-6.8
- The rebase also resolves the following bugzillas:
- Resolves: rhbz#1270029 - [RFE] Add a way to lookup users based on CAC
                           identity certificates
- Resolves: rhbz#1270027 - [RFE] Support for smart cards 
- Resolves: rhbz#1269422 - [FEAT] UID and GID mapping on individual clients
- Resolves: rhbz#1269421 - [RFE] The fast memory cache should cache initgroups
- Resolves: rhbz#1265429 - If the site discovery fails, ad-site option is
                           not taken into account.
- Resolves: rhbz#1254193 - Fix for cyclic dependencies between
                           sssd-{krb5,}-common
- Resolves: rhbz#1247997 - [IPA/IdM] sudoOrder not honored as expected
- Resolves: rhbz#1237142 - [RFE] authenticate against cache in SSSD
- Resolves: rhbz#1232632 - Kerberos-based providers other than krb5 do
                           not queue requests
- Resolves: rhbz#1227804 - Group members are not turned into ghost entries
                           when the user is purged from the SSSD cache
- Resolves: rhbz#1227685 - sssd with ldap backend throws error domain log
- Resolves: rhbz#1221365 - [RFE] Support GPOs from different domain controllers
- Resolves: rhbz#1215195 - Override for IPA users with login does not list
                           user all groups
- Resolves: rhbz#1196204 - sssd cache holding gid values for nss, but not
                           the alpha group name representation
- Resolves: rhbz#1194039 - [RFE] User's home directories are not
                           taken from AD when there is an IPA trust with AD

* Mon Oct  5 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-51
- Resolves: rhbz#1266404 - Memory leak / possible DoS with krb auth.

* Mon Oct  5 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-50
- Resolves: rhbz#1264524 - SSSD POSIX attribute check is too strict

* Mon Oct  5 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-49
- Resolves: rhbz#1255285 - cleanup_groups should sanitize dn of groups

* Mon Aug 31 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-48
- Resolves: rhbz#1251349 - sysdb sudo search doesn't escape special
                           characters

* Mon Jun 22 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-47
- Resolves: rhbz#1232738 - Cache is not updated after user is deleted from
                           ldap server

* Mon Jun  8 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-46
- Resolves: rhbz#1227860 - Provide a way to disable the cleanup task
- Resolves: rhbz#1227863 - ignore_group_members doesn't work for subdomains

* Wed Jun  3 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-45
- Resolves: rhbz#1226834 - id lookup for non-root domain users doesn't
                           return all groups on first attempt

* Tue Jun  2 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-44
- Resolves: rhbz#1225614 - IPA enumeration provider crashes

* Sun May 31 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-43
- Resolves: rhbz#1212610 - sssd ad groups work intermittently

* Mon May 25 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-42
- Resolves: rhbz#1215765 - sssd nss responder gets wrong number of
                           secondary groups

* Mon May 25 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-41
- Resolves: rhbz#1221358 - SSSD doesn't work with ID mapping and disabled
                           subdomains

* Fri May 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-40
- Resolves: rhbz#1219844 - Unable to resolve group memberships for AD
                           users when using sssd-1.12.2-58.el7_1.6.x86_64
                           client in combination with
                           ipa-server-3.0.0-42.el6.x86_64 with AD Trust

* Fri May 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-39
- Resolves: rhbz#1216094 - /usr/libexec/sssd/selinux_child crashes and
                           gets avc denial when ssh

* Wed May  6 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-38
- Include several upstream fixes related to ID views
- Resolves: rhbz#1215195 - Override for IPA users with login does not list
                           user all groups
- Resolves: rhbz#1213947 - Group resolution is inconsistent with group
                           overrides
- Resolves: rhbz#1213822 - Overrides with --login work in second attempt

* Thu Apr 30 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-37
- Resolves: rhbz#1217328 - autofs provider fails when default_domain_suffix
                           and use_fully_qualified_names set

* Thu Apr 30 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-36
- Resolves: rhbz#1212387 - sssd_be segfault id_provider = ad
                           src/providers/ad/ad_gpo.c:843

* Wed Apr 29 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-35
- Resolves: rhbz#1213940 - Overridde with --login fails trusted adusers
                           group membership resolution

* Tue Apr 28 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-34
- Resolves: rhbz#1170910 - SSSD should not fail authentication when only
                           allow rules are used

* Mon Apr 27 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-33
- Resolves: rhbz#1213716 - idoverridegroup for ipa group with --group-name
                           does not work
- Resolves: rhbz#1213822 - Overrides with --login work in second attempt

* Thu Apr 23 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-32
- Resolves: rhbz#1212017 - Sudo responder does not respect filter_users
                           and filter_groups

* Wed Apr 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-31
- Resolves: rhbz#1203642 - GPO access control looks for computer object
                           in user's domain only

* Wed Apr 15 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-30
- Related: rhbz#1211728 - Only set the selinux context if the context
                          differs from the local one

* Tue Apr 14 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-29
- Package the localauth plugin
- Related: rhbz#1168357 - [RFE] Implement localauth plugin for MIT krb5 1.12

* Tue Apr 14 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-28
- Resolves: rhbz#1207720 - id lookup resolves "Domain Local" group and
                           errors appear in domain log

* Tue Apr 14 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-27
- BuildRequire the proper libkrb5 version for correct localauth plugin build
- Related: rhbz#1168357 - [RFE] Implement localauth plugin for MIT krb5 1.12

* Tue Apr 14 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-26
- Resolves: rhbz#1194367 - sssd_be dumping core

* Fri Mar 27 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-25
- Resolves: rhbz#1206121 - ldap_access_order=ppolicy: Explicitly mention in
                           manpage that unsupported time specification will
                           lead to sssd denying access

* Fri Mar 27 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-24
- Resolves: rhbz#1205382 - Properly handle AD's binary objectGUID

* Thu Mar 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-23
- Resolves: rhbz#1205716 - Installing sssd-common-1.12.4-18.el6 might
                           install with wrong user account (root)

* Thu Mar 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-22
- Fix a typo in DEBUG message
- Related: rhbz#1173198 - [RFE] Have OpenLDAP lock out ssh keys when
                          account naturally expires

* Thu Mar 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-21
- Handle TTL=0 in SRV queries correctly
- Resolves: rhbz#1171378 - Read and use the TTL value when resolving a
                           SRV query

* Thu Mar 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-20
- Cherry-pick unit test changes from upstream to allow cherry-picking
  sssd-1-12 patches
- Remove unused LDAP provider code to avoid static analyser warnings
- Related: rhbz#1168347 - Rebase sssd to 1.12.x

* Thu Mar 26 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-19
- Resolves: rhbz#1206092 - sssd crashes intermittently in GPO code

* Fri Mar 20 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-18
- Resolves: rhbz#1202728 - sssd-ad requires samba3, but ipa-server-trust-ad
                           requires samba4

* Fri Mar 20 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-17
- Resolves: rhbz#1203630 - SSSD doesn't own the GPO cache directory

* Fri Mar 20 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-16
- Fix warning in SELinux code
- Handle setups with empty default and no SELinux maps
- Related: rhbz#1194302 - With empty ipaselinuxusermapdefault security
                          context on client is staff_u
- Resolves: rhbz#1202305 - sssd_be segfault on IPA(when auth with AD
                           trusted domain) client at
                           src/providers/ipa/ipa_s2n_exop.c:1605
- Resolves: rhbz#1201847 - SSSD downloads too much information when fetching
                           information about groups

* Fri Mar 13 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-15
- Fix PAM responder initgroups cache for subdomain users
- Log extop failures better
- Related: rhbz#1168344 - [RFE] ID Views: Support migration from the sync
                          solution to the trust solution

* Fri Mar 13 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-14
- Fix internal error codes broken when fixing rhbz#1036745
- Related: rhbz#1036745 - [RFE] Allow SSSD to issue shadow expiration
                          warning even if alternate authentication method
                          is used

* Fri Mar 13 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-13
- Resolves: rhbz#1200093 - sssd_nss segfaults if initgroups request is by
                           UPN and doesn't find anything

* Fri Mar 13 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-12
- Fix Coverity warning in ldap_child
- Add better debugging
- Related: rhbz#1198478 - ccname_file_dummy is not unlinked on error

* Sun Mar  8 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-11
- Resolves: rhbz#1098147 - [RFE] Implement background refresh for users,
                           groups or other cache objects

* Fri Mar  6 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-10
- Resolves: rhbz#1173198 - [RFE] Have OpenLDAP lock out ssh keys when
                           account naturally expires

* Fri Mar  6 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-9
- Initialize a pointer in ldap_child to NULL
- Resolves: rhbz#1198478 - ccname_file_dummy is not unlinked on error

* Fri Mar  6 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-8
- Relax the ldb requirement
- Related: rhbz#1168347 - Rebase sssd to 1.12.x

* Wed Mar  4 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-7
- Resolves: rhbz#1194302 - With empty ipaselinuxusermapdefault security
                           context on client is staff_u

* Wed Mar  4 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-6
- Resolves: rhbz#1198478 - ccname_file_dummy is not unlinked on error

* Wed Mar  4 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-5
- Resolves: rhbz#1171378 - Read and use the TTL value when resolving a
                           SRV query

* Tue Mar  3 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-4
- Resolves: rhbz#1171378 - Read and use the TTL value when resolving a
                           SRV query
- Rebuild against latest krb5, add a versioned BuildRequires
- Resolves: rhbz#1168357 - [RFE] Implement localauth plugin for MIT krb5 1.12

* Tue Mar  3 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-3
-  Related: rhbz#1036745 - [RFE] Allow SSSD to issue shadow expiration
                           warning even if alternate authentication method
                           is used

* Wed Feb 18 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-2
- Do not mark the selinux_child helper as setuid, we don't support rootless
  SSSD in 6.7
- Related: rhbz#1168347 - Rebase sssd to 1.12.x

* Wed Feb 18 2015 Jakub Hrozek <jhrozek@redhat.com> - 1.12.4-1
- Resolves: rhbz#1168347 - Rebase sssd to 1.12.x
- The rebase resolves the following RHEL bugzillas
- Resolves: rhbz#1172865 - sssd.conf(5) man page gives bad advice about
                           domains parameter
- Resolves: rhbz#1172494 - PAC: krb5_pac_verify failures should not
                           be fatal (backport fix from upstream)
- Resolves: rhbz#1171782 - [RFE]: SSSD should preserve case for user
                           uid field
- Resolves: rhbz#1170910 - SSSD should not fail authentication when only
                           allow rules are used
- Resolves: rhbz#1168377 - [RFE] User's home directories and shells are
                           not taken from AD when there is an IPA trust with AD
- Resolves: rhbz#1168363 - [RFE] Add domains= option to pam_sss
- Resolves: rhbz#1168344 - [RFE] ID Views: Support migration from the sync
                           solution to the trust solution
- Resolves: rhbz#1161564 - [RFE]ad provider dns_discovery_domain option:
                           kerberos discovery is not using this option
- Resolves: rhbz#1148582 - inconsistent group information when multiple
                           ad domain sections are configured in sssd
- Resolves: rhbz#1140909 - sssd.conf man page missing subdomains_provider
                           ad support
- Resolves: rhbz#1139878 - SSSD connection terminated after failing
                           anonymous bind to IBM Tivoli Directory Server
- Resolves: rhbz#1135838 - Man sssd-ldap shows parameter
                           ldap_purge_cache_timeout with "Default: 10800
                           (12 hours)"
- Resolves: rhbz#1135432 - Dereference code errors out when dereferencing
                           entries protected by ACIs
- Resolves: rhbz#1134942 - sssd does not recognize Windows server 2012
                           R2's LDAP as AD
- Resolves: rhbz#1123291 - automount segfaults in sss_nss_check_header
- Resolves: rhbz#1088402 - [RFE] Allow login through SSSD using multiple
                           attributes

* Tue Nov 18 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-33
- Resolves: rhbz#1154042 - RHEL6.6 sssd (1.11) doesn't return all group
                           memberships against an IPA server

* Tue Nov 18 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-32
- Resolves: rhbz#1160713 - TokenGroups for LDAP provider breaks in corner
                           cases

* Thu Sep 25 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-31
- Resolves: rhbz#1141814 - Password expiration policies are not being
                           enforced by SSSD

* Mon Sep 15 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-30
- Resolves: rhbz#1139044 - RHEL6.6 ipa user private group not found

* Thu Sep 04 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-29
- Resolves: rhbz#1103487 - CVE-2014-0249 - sssd: incorrect expansion of group
                           membership when encountering a non-POSIX group

* Tue Aug 26 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-28
- Resolves: rhbz#1125187 - simple_allow_groups does not lookup groups from
                           other AD domains

* Tue Aug 26 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-27
- Resolves: rhbz#1127270 - sssd connect to ipa-server is long

* Tue Aug 26 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-26
- Resolves: rhbz#1130017 - Saving group membership fails if provider is AD,
                           POSIX attributes are used and primary group contains
                           the user as a member

* Mon Aug 25 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-25
- Resolves: rhbz#1111528 - Expired shadow policy user(shadowLastChange=0)
                           is not prompted for password change

* Fri Aug 22 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-24
- Resolves: rhbz#1132361 - use-after-free in dyndns code

* Tue Aug 19 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-23
- Resolves: rhbz#1099290: RFE: Be able to configure sssd to honor openldap
                          account lock to restrict access via ssh key

* Tue Aug 19 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-22
- Use the correct sudo iterator
- Related: rhbz#1118336 - sudo: invalid sudoHost filter with asterisk

* Tue Aug 19 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-21
- Add notes about offline mode to sssd.conf
- Related: rhbz#1110226 - Requests queued during transition from offline
                           to online mode

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-20
- Resolves: rhbz#1127278 -  Auth fails when space in username is
                            replaced with character set by
                            override_default_whitespace

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-19
- Resolves: rhbz#1127757 - sssd can't retrieve sudo rules when using the
                           "default_domain_suffix" option

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-18
- Resolves: rhbz#1127265 - Problems with tokengroups and ldap_group_search_base

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-17
- Resolves: rhbz#1126636 - RHEL6.6 sssd not running after upgrade

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-16
- Resolves: rhbz#1128612 - IFP: FQDN lookups are broken

* Thu Aug 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-15
- Resolves: rhbz#1118336 - sudo: invalid sudoHost filter with asterisk

* Thu Jul 31 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-14
- Resolves: rhbz#1110226 - Requests queued during transition from offline
                           to online mode

* Thu Jul 31 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-13
- Resolves: rhbz#1122873 -  Failover does not always happen from SRV
                            to hostname resolution(via /etc/hosts)
- Remove spurious systemctl call on %postun

* Mon Jul 28 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-12
- Resolves: rhbz#1111317 - [RFE] Add option for sssd to replace space with
                           specified character in LDAP group

* Fri Jul 25 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-11
- Resolves: rhbz#1109188 - dereferencing control failure against openldap
                           server

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-10
- Resolves: rhbz#1084532 - sssd_sudo process segfaults

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-9
- Resolves: rhbz#1122158 - ad: group membership is empty when id mapping
                           is off and tokengroups are enabled

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-8
- Resolves: rhbz#1118541 - Floating point exception using ldap 

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-7
- Resolves: rhbz#1042922 - [RFE] Add fallback to sudoRunAs when sudoRunAsUser
                           is not defined and no ldap_sudorule_runasuser mapping
                           has been defined in SSSD

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-6
- Resolves: rhbz#1120508 - tokengroups do not work with id_provider=ldap 

* Thu Jul 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-5
- Fix potential NULL dereference in IFP code
- Related: rhbz#1110369 - sssd is started before messagebus, making
                          sssd-ifp fail

* Wed Jul 16 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-4
- BuildRequire the latest libini_config
- Related: #1051164 - Rebase SSSD to 1.11+ in RHEL6

* Mon Jul 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-3
- Resolves: rhbz#1110369 - sssd is started before messagebus, making
                           sssd-ifp fail

* Tue Jun 03 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-2
- Resolves: rhbz#1104145 - public key validator is too strict and does not
                           allow newlines anywhere in the public key string,
                           not even at the end

* Tue Jun 03 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.6-1
- Rebase to 1.11.6
- Resolves: #1051164 - Rebase SSSD to 1.11+ in RHEL6 

* Thu May 29 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.5.1-4
- Rebuild against new ding-libs
- Related: #1051164 - Rebase SSSD to 1.11+ in RHEL6

* Wed May 14 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.5.1-3
- Backport the InfoPipe patches needed for Sat6 integration
- Related: #1051164 - Rebase SSSD to 1.11+ in RHEL6 

* Mon May 12 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.5.1-2
- Resolves: #1085412 - SSSD Crashes when storage experiences high latency

* Wed Apr 16 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.11.5.1-1
- Resolves: #1051164 - Rebase SSSD to 1.11+ in RHEL6 

* Mon Feb 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-134
Resolves: #1036168 - sssd can't retrieve auto.master when using the
                     "default_domain_suffix"

* Mon Feb 24 2014 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-133
- Resolves: #1065534 - SSSD pam module accepts usernames with leading spaces

* Thu Dec 19 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-132
- Resolves: #1038098 - sssd_nss grows memory footprint when netgroups
                       are requested

* Tue Nov 19 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-131
- Allow combination of proxy id backend and LDAP auth backend
- Resolves: #1025813 - SSSD: Allow for custom attributes in RDN when using
                       id_provider = proxy

* Tue Nov 19 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-130
- Inherit UID limits for subdomains
- Resolves: #1020905 - Creating system accounts on a IdM client takes up
                       to 10 minutes when AD trust is configured in the IdM.

* Tue Oct 22 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-129
- Do not crash when LDAP disconnects while a search is still in progress
- Resolves: #1019979 - sssd_be segfault when authenticating against active
                       directory

* Thu Sep 26 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-128
- More upstream fixes to prevent memcache crashes
- Related: #997406 - sssd_nss core dumps under load

* Thu Sep 12 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-127
- Resolves: #1002929 - sssd_be segfaults if IPA dynamic DNS update times out

* Tue Sep  3 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-126
- Make IPA SELinux provider aware of subdomain users
- A better version of already committed patch
- Resolves: #954342 - In IPA AD trust setup, the sssd logs throws
                      'sysdb_search_user_by_name failed' error when
                      AD user tries to login via ipa client.

* Fri Aug 30 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-125
- Resolves: #997406 - sssd_nss core dumps under load
- Resolves: #984814 - sssd_nss terminated with segmentation fault

* Fri Aug 30 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-124
- Resolves: #1002161 - large number of sudo rules results in error -
                       Unable to create response: Invalid argument

* Mon Aug 19 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-123
- Silence restorecon on clean install
- Resolves: #987456 - RHEL6 sssd upgrade restorecon workaround for
                      /var/lib/sss/mc context

* Sun Aug 11 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-122
- Make IPA SELinux provider aware of subdomain users
- Resolves: #954342 - In IPA AD trust setup, the sssd logs throws
                      'sysdb_search_user_by_name failed' error when
                      AD user tries to login via ipa client.

* Sun Aug 11 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-121
- Print password complexity hint when password change fails with
  constraint violation
- Related: #983028 - passwd returns "Authentication token manipulation
                     error" when entering wrong current password

* Sun Aug 11 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-120
- Resolves: #983028 - passwd returns "Authentication token manipulation
                      error" when entering wrong current password

* Sun Aug 11 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-119
- Resolves: #948830 - sssd do too many disk writes causing delay in
                      "getent netgroup allmachines-netgroup" nested netgroups.

* Sun Aug 11 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-118
- Resolves: #984814 - sssd_nss terminated with segmentation fault

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-117
- Resolves: #966757 - SSSD failover doesn't work if the first DNS server
                     in resolv.conf is unavailable

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-116
- Resolves: #963235 - sssd_be crashing with nested ldap groups

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-115
- Apply a forgotten dependency for patch #254
- Related: #916997 - getgrnam / getgrgid for large user groups
                     is too slow due to range retrieval functionality
- Add two fixes for better handling of faulty SRV processing
- Related: #954275 - sssd fails connect to IPA server during boot when
                     spanning tree is enabled in network router.
- Remove enumerate=true from example in man page
- Related: #988381 - clarify the disadvantages of enumeration in sssd.conf

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-114
- Resolves: #914433 - sssd pam write_selinux_login_file creating the temp
                      file for SELinux data failed

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-113
- Resolves: #916997 - getgrnam / getgrgid for large user groups
                      is too slow due to range retrieval functionality

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-112
- Resolves: #918394 - sssd etas 99% CPU and runs out of file descriptors
                      when clearing cache

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-111
- Resolves: #924113 - man sssd-sudo has wrong title

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-110
- Resolves: #924397 - document what does access_provider=ad do

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-109
- Use permissive control when adding ghost users
- Resolves: #928797 - cyclic group memberships may not work depending on
                      order of operations

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-108
- Set correct state of SRV servers on resolving error
- Resolves: #954275 - sssd fails connect to IPA server during boot when
                      spanning tree is enabled in network router.

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-107
- Resolves: #954323 - SSSD doesn't display warning for last grace login.

* Fri Aug 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-106
- Format patch to configure sysv script differently
- RHEL-6 patch(1) apparently doesn't like the output of git format-patch
 -M -C and doesn't properly copy files on renames
- Resolves: #971435 - Enhance sssd init script so that it would source a
  configuration.

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-105
- Resolves: #973345 - SSSD service randomly dies

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-104
- Resolves: #971435 - Enhance sssd init script so that it would source
                      a configuration

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-103
- Resolves: #961356 - SUDO is not working for users from trusted AD domain

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-102
- Resolves: #970519 - [RFE] Add support for suppressing group members

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-101
- Resolves: #976273 - [RFE] Add a new override_homedir expansion for the
                      "original value"

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-100
- Resolves: #978966 - sudoHost mismatch response is incorrect sometimes

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-99
- Clarify the min_id/max_id limits further
- Resolves: #978994 - SSSD filter out ldap user/group if uid/gid is zero

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-98
- Resolves: #979046 - sssd_be goes to 99% CPU and causes significant login
                      delays when client is under load

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-97
- Resolves: #986379 - sss_cache -N/-n should invalidate the hash table
                      in sssd_nss

* Thu Aug 08 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-96
- Resolves: #988525 - sssd fails instead of skipping when a sudo ldap
                      filter returns entries with multiple CNs

* Thu Jul 25 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-95
- Mention that enumeration should be discouraged
- Resolves: #988381 - clarify the disadvantages of enumeration in sssd.conf

* Thu Jul 25 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-94
- Call restorecon on memcache files to force the right context on upgrades
- Resolves: #987456 - RHEL6 sssd upgrade restorecon workaround for
                      /var/lib/sss/mc context

* Wed Jul 24 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-93
- Resolves: #987479 - libsss_sudo should depend on sudo package with
                      sssd support

* Fri Jul 19 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-92
- Resolves: #951086 - sssd_pam segfaults if sssd_be is stuck

* Thu May 30 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-91
- Resolves: #967636 - SSSD frequently fails to return automount maps
                      from LDAP

* Wed May  1 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-90
- Resolves: #953165 - Enabling enumeration causes sssd_be process to
                      utilize 100% of the CPU

* Tue Apr 23 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-89
- Resolves: #906398 - sssd_be crashes sometimes

* Mon Apr 15 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-88
- Resolves: #950874: Simple access control always denies uppercased users
                     in case insensitive domain

* Tue Mar 20 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-87
- Resolves: #921454: Resolve local group members in LDAP groups
        
* Tue Mar 05 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-86
- Resolves: rhbz#911299 - sssd: simple access provider flaw prevents intended
                          ACL use when client to an AD provider

* Fri Mar 01 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-85
- Fix pwd_expiration_warning=0
- Resolves: rhbz#911329 - pwd_expiration_warning has wrong default for
                          Kerberos

* Fri Feb 22 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-84
- Resolves: rhbz#911329 - pwd_expiration_warning has wrong default for
                          Kerberos

* Wed Jan 30 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-83
- Resolves: rhbz#872827 - Serious performance regression in sssd

* Wed Jan 23 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-82
- Resolves: rhbz#888614 - Failure in memberof can lead to failed
                          database update

* Wed Jan 23 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-81
- Resolves: rhbz#903078 - TOCTOU race conditions by copying
                          and removing directory trees

* Wed Jan 23 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-80
- Resolves: rhbz#903078 - Out-of-bounds read flaws in
                          autofs and ssh services responders

* Tue Jan 22 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-79
- Resolves: rhbz#902716 - Rule mismatch isn't noticed before smart refresh
                          on ppc64 and s390x

* Tue Jan 22 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-78
- Resolves: rhbz#896476 - SSSD should warn when pam_pwd_expiration_warning
                          value is higher than passwordWarning LDAP attribute.

* Tue Jan 22 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-77
- Resolves: rhbz#902436 - possible segfault when backend callback is removed

* Mon Jan 21 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-76
- Resolves: rhbz#895132 - Modifications using sss_usermod tool are not
                          reflected in memory cache

* Wed Jan 16 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-75
- Resolves: rhbz#894302 - sssd fails to update to changes on autofs maps

* Wed Jan 16 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-74
- Resolves: rhbz894381 - memory cache is not updated after user is deleted
                         from ldb cache

* Wed Jan 16 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-73
- Resolves: rhbz895615 - ipa-client-automount: autofs failed in s390x and
                         ppc64 platform

* Tue Jan 15 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-72
- Resolves: rhbz#894997 - sssd_be crashes looking up members with groups
                          outside the nesting limit

* Tue Jan 15 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-71
- Resolves: rhbz#895132 - Modifications using sss_usermod tool are not
                          reflected in memory cache

* Tue Jan 15 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-70
- Resolves: rhbz#894428 - wrong filter for autofs maps in sss_cache

* Tue Jan 15 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-69
- Resolves: rhbz#894738 - Failover to ldap_chpass_backup_uri doesn't work

* Wed Jan 09 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-68
- Resolves: rhbz#887961 - AD provider: getgrgid removes nested group
                          memberships

* Mon Jan 07 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-67
- Resolves: rhbz#878583 - IPA Trust does not show secondary groups for AD
                          Users for commands like id and getent

* Mon Jan 07 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-66
- Resolves: rhbz#874579 - sssd caching not working as expected for selinux
                          usermap contexts

* Mon Jan 07 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-65
- Resolves: rhbz#892197 - Incorrect principal searched for in keytab

* Mon Jan 07 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-64
- Resolves: rhbz#891356 - Smart refresh doesn't notice "defaults" addition
                          with OpenLDAP

* Fri Jan 04 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-63
- Resolves: rhbz#878419 - sss_userdel doesn't remove entries from in-memory
                          cache

* Fri Jan 04 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-62
- Resolves: rhbz#886848 - user id lookup fails for case sensitive users
                          using proxy provider

* Fri Jan 04 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-61
- Resolves: rhbz#890520 - Failover to krb5_backup_kpasswd doesn't work

* Fri Jan 04 2013 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-60
- Resolves: rhbz#874618 - sss_cache: fqdn not accepted

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-59
- Resolves: rhbz#889182 - crash in memory cache

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-58
- Resolves: rhbz#889168 - krb5 ticket renewal does not read the renewable
                          tickets from cache

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-57
- Resolves: rhbz#886091 - Disallow root SSH public key authentication
- Add default section to switch statement (Related: rhbz#884666)

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-56
- Resolves: rhbz#886038 - sssd components seem to mishandle sighup

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-55
- Resolves: rhbz#888800 - Memory leak in new memcache initgr cleanup function

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-54
- Resolves: rhbz#888614 - Failure in memberof can lead to failed database
                          update

* Thu Dec 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-53
- Resolves: rhbz#885078 - sssd_nss crashes during enumeration if the
                          enumeration is taking too long

* Tue Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-52
- Related: rhbz#875851 - sysdb upgrade failed converting db to 0.11
- Include more debugging during the sysdb upgrade

* Tue Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-51
- Resolves: rhbz#877972 - ldap_sasl_authid no longer accepts full principal

* Tue Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-50
- Resolves: rhbz#870045 - always reread the master map from LDAP
- Resolves: rhbz#876531 - sss_cache does not work for automount maps

* Tue Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-49
- Resolves: rhbz#884666 - sudo: if first full refresh fails, schedule
                          another first full refresh

* Tue Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-48
- Resolves: rhbz#880956 - Primary server status is not always reset after
                          failover to backup server happened
- Silence a compilation warning in the memberof plugin (Related: rhbz#877974)
- Do not steal resolv result on error (Related: rhbz#882076)

* Mon Dec 17 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-47
- Resolves: rhbz#882923 - Negative cache timeout is not working for proxy
                          provider

* Sat Dec 15 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-46
- Resolves: rhbz#884600 - ldap_chpass_uri failover fails on using same
                          hostname

* Fri Dec 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-45
- Resolves: rhbz#858345 - pam_sss(crond:account): Request to sssd
                          failed. Timer expired

* Fri Dec 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-44
- Resolves: rhbz#878419 - sss_userdel doesn't remove entries from in-memory
                          cache

* Fri Dec 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-43
- Resolves: rhbz#880176 - memberUid required for primary groups to match
                          sudo rule

* Fri Dec 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-42
- Resolves: rhbz#885105 - sudo denies access with disabled
                          ldap_sudo_use_host_filter

* Tue Dec 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-41
- Resolves: rhbz#883408 - Option ldap_sudo_include_regexp named incorrectly

* Tue Dec 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-40
- Resolves: rhbz#880546 - krb5_kpasswd failover doesn't work
- Fix the error handler in sss_mc_create_file (Related: #789507)

* Tue Dec 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-39
- Resolves: rhbz#882221 - Offline sudo denies access with expired
                          entry_cache_timeout
- Fix several bugs found by Coverity and clang:
- Check the return value of diff_gid_lists (Related: #869071)
- Move misplaced sysdb assignment (Related: #827606)
- Remove dead assignment (Related: #827606)
- Fix copy-n-paste error in the memberof plugin (Related: #877974)

* Tue Dec 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-38
- Resolves: rhbz#882923 - Negative cache timeout is not working for proxy
                          provider
- Link sss_ssh_authorizedkeys and sss_ssh_knowhostsproxy with the client
  libraries (Related: #870060)
- Move sss_ssh_knownhosts documentation to the correct section
  (Related: #870060)

* Fri Dec 07 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-37
- Resolves: rhbz#884480 - user is not removed from group membership during
                          initgroups
- Fix incorrect synchronization in mmap cache (Related: #789507)

* Fri Dec 07 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-36
- Resolves: rhbz#883336 - sssd crashes during start if id_provider is
                          not mentioned

* Fri Dec 07 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-35
- Resolves: rhbz#882290 - arithmetic bug in the SSSD causes netgroup
                          midpoint refresh to be always set to 10 seconds

* Thu Dec 06 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-34
- Resolves: rhbz#877974 - updating top-level group does not reflect ghost
                          members correctly
- Resolves: rhbz#880159 - delete operation is not implemented for ghost users

* Thu Dec 06 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-33
- Resolves: rhbz#881773 - mmap cache needs update after db changes

* Thu Dec 06 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-32
- Resolves: rhbz#875677 - password expiry warning message doesn't appear
                          during auth
- Fix potential NULL dereference when skipping built-in AD groups
  (Related: rhbz#874616)
- Add missing parameter to DEBUG message (Related: rhbz#829742)

* Thu Dec 06 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-31
- Resolves: rhbz#882076 - SSSD crashes when c-ares returns success but an
                          empty hostent during the DNS update
- Do not version libsss_sudo, it's not supposed to be linked against, but
  dlopened (Related: rhbz#761573)

* Wed Nov 28 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-30
- Resolves: rhbz#880140 - sssd hangs at startup with broken configurations

* Wed Nov 28 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-29
- Resolves: rhbz#878420 - SIGSEGV in IPA provider when ldap_sasl_authid is not set

* Wed Nov 28 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-28
- Resolves: rhbz#874616 - Silence the DEBUG messages when ID mapping code
                          skips a built-in group

* Tue Nov 27 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-27
- Resolves: rhbz#824244 - sssd does not warn into sssd.log for broken
                          configurations

* Tue Nov 27 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-26
- Resolves: rhbz#874673 - user id lookup fails using proxy provider
- Fix a possibly uninitialized variable in the LDAP provider
- Related: rhbz#877130

* Wed Nov 21 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-25
- Resolves: rhbz#878262 - ipa password auth failing for user principal
                          name when shorter than IPA Realm name
- Resolves: rhbz#871843 - Nested groups are not retrieved appropriately
                          from cache

* Tue Nov 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-24
- Resolves: rhbz#870238 - IPA client cannot change AD Trusted User password

* Tue Nov 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-23
- Resolves: rhbz#877972 - ldap_sasl_authid no longer accepts full principal

* Tue Nov 20 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-22
- Resolves: rhbz#861075 - SSSD_NSS failure to gracefully restart
                          after sbus failure

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-21
- Resolves: rhbz#877354 - ldap_connection_expire_timeout doesn't expire
                          ldap connections

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-20
- Related: rhbz#877126 - Bump the release tag

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-20
- Resolves: rhbz#877126 - subdomains code does not save the proper
                          user/group name

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-19
- Resolves: rhbz#877130 - LDAP provider fails to save empty groups
- Related: rhbz#869466 - check the return value of waitpid()

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-18
- Resolves: rhbz#870039 - sss_cache says 'Wrong DB version'

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-17
- Resolves: rhbz#875740 - "defaults" entry ignored

* Mon Nov 19 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-16
- Resolves: rhbz#875738 - offline authentication failure always returns
                          System Error

* Sun Nov 18 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-15
- Resolves: rhbz#875851 - sysdb upgrade failed converting db to 0.11

* Thu Nov 15 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-14
- Resolves: rhbz#870278 -  ipa client setup should configure host properly
                           in a trust is in place

* Wed Nov 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-13
- Resolves: rhbz#871160 - sudo failing for ad trusted user in IPA environment

* Sun Nov 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-12
- Resolves: rhbz#870278 -  ipa client setup should configure host properly
                           in a trust is in place

* Sun Nov 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-11
- Resolves: rhbz#869678 - sssd not granting access for AD trusted user in HBAC rule

* Sun Nov 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-10
- Resolves: rhbz#872180 - subdomains: Invalid sub-domain request type
- Related: rhbz#867933 - invalidating the memcache with sss_cache doesn't work
                         if the sssd is not running

* Sun Nov 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-9
- Resolves: rhbz#873988 - Man page issue to list 'force_timeout' as an
                          option for the [sssd] section

* Sun Nov 11 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-8
- Resolves: rhbz#873032 - Move sss_cache to the main subpackage

* Tue Nov 06 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-7
- Resolves: rhbz#873032 - Move sss_cache to the main subpackage
- Resolves: rhbz#829740 - Init script reports complete before sssd is actually
                          working
- Resolves: rhbz#869466 - SSSD starts multiple processes due to syntax error in
                          ldap_uri
- Resolves: rhbz#870505 - sss_cache: Multiple domains not handled properly
- Resolves: rhbz#867933 - invalidating the memcache with sss_cache doesn't work
                          if the sssd is not running
- Resolves: rhbz#872110 - User appears twice on looking up a nested group

* Sun Nov 04 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-6
- Resolves: rhbz#871576 - sssd does not resolve group names from AD
- Resolves: rhbz#872324 - pam: fd leak when writing the selinux login file
                          in the pam responder
- Resolves: rhbz#871424 - authconfig chokes on sssd.conf with chpass_provider
                          directive

* Fri Nov 02 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-5
- Do not send SIGKILL to service right after sending SIGTERM
- Resolves: #771975
- Fix the initial sudo smart refresh
- Resolves: #869013
- Implement password authentication for users from trusted domains
- Resolves: #869071
- LDAP child crashed with a wrong keytab
- Resolves: #869150
- The sssd_nss process grows the memory consumption over time
- Resolves: #869443

* Mon Oct 15 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-4
- BuildRequire selinux-policy so that selinux login support is built in
- Resolves: #867932

* Mon Oct 15 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-3
- Do not segfault if namingContexts contain no values or multiple values
- Resolves: rhbz#866542

* Mon Oct 15 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-2
- Fix the "ca" translation of the sssd-simple manual page
- Related: rhbz#827606 - Rebase SSSD to 1.9 in 6.4

* Sun Oct 14 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.2-1
- New upstream release 1.9.2

* Sun Oct 07 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.1-1
- Rebase to 1.9.1

* Wed Oct 03 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.0-3
- Require the latest libldb

* Tue Sep 25 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.0-2
- Rebase to 1.9.0
- Resolves: rhbz#827606 - Rebase SSSD to 1.9 in 6.4

* Mon Sep 24 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.9.0-1.rc1
- Rebase to 1.9.0 RC1
- Resolves: rhbz#827606 - Rebase SSSD to 1.9 in 6.4
- Bump the selinux-policy version number to pull in required fixes

* Thu Aug 09 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.8.0-33
- Resolves: rhbz#840089 - Update the shadowLastChange attribute
                          with days since the Epoch, not seconds

* Tue May 29 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-32
- Fix protocol break for services map
- Related:  rhbz#825028 - Service lookups by port number doesn't work on
                          s390x/ppc64 arches

* Thu May 24 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-31
- Resolves: rhbz#825028 - Service lookups by port number doesn't work on
                          s390x/ppc64 arches

* Thu May 24 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-30
- Resolves: rhbz#824616 - sssd_nss crashes when configured with
                          use_fully_qualified_names = true

* Tue May 22 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-29
- Resolves: rhbz#824062 - sssd_be crashed with SIGSEGV in
                          _tevent_schedule_immediate()

* Wed May 16 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-28
- Resolves: rhbz#822236 - SSSD netgroups do not honor
                          entry_cache_nowait_percentage

* Fri May 11 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-27
- Resolves: rhbz#820759 - AVC denial seen on sssd upgrade during ipa-client
                          upgrade
- Resolves: rhbz#821044 - sss_groupadd no longer detects duplicate GID numbers

* Thu May 10 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-26
- Resolves: rhbz#818642 - Auth fails for user with non-default attribute names
- Resolves: rhbz#819063 - sssd fails to provide partial data till paged search
                          returns "Size Limit Exceeded"
- Resolves: rhbz#820585 - Group enumeration fails in proxy provider

* Mon Apr 30 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-25
- Resolves: rhbz#816616 - group members are now lowercased in case insensitive
                          domains

* Wed Apr 25 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-24
- Resolves: rhbz#805431 - NFS files/folders are mapped to nobody user if NFS
                          top level directory is chowned by a SSSD user

* Fri Apr 20 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-23
- Resolves: rhbz#805924 - SSSD should attempt to get the RootDSE after binding
- Resolves: rhbz#814237 - sdap_check_aliases must not error when detects the
                          same user
- Resolves: rhbz#812281 - autofs client: map name length used as key length
- Related:  rhbz#784870 - SSSD fails during autodetection of search bases for
                          new LDAP features
- Related:  rhbz#814269 - sssd-1.5.1-66.el6_2.3.x86_64 freezes

* Mon Apr 09 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-22
- Fix typo in patch for SSH umask
- Related:  rhbz#808107 - Coverity revealed memory management defects

* Mon Apr 09 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-21
- Resolves: rhbz#808458 - Authconfig crashes when sets krb realm
- Resolves: rhbz#808597 - sssd_nss crashes on request when no back end is
                          running
- Resolves: rhbz#808107 - Coverity revealed memory management defects

* Fri Mar 30 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-20
- Related: rhbz#805452  - Unable to lookup user, group, netgroup aliases with
                          case_sensitive=false

* Fri Mar 30 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-18
- Resolves: rhbz#804057 - Initial service lookups having name with uppercase
                          alphabets doesn't work
- Resolves: rhbz#804065 - Service lookup using case-sensitive protocol names
                          doesn't work when case_sensitive=false
- Resolves: rhbz#805281 - sssd: Uses the wrong key when there a multiple
                          realms in a single keytab
- Resolves: rhbz#805452 - Unable to lookup user, group, netgroup aliases with
                          case_sensitive=false
- Resolves: rhbz#805918 - Wrong resolv_status might cause crash when name
                          resolution times out
- Resolves: rhbz#805431 - NFS files/folders are mapped to nobody user if NFS
                          top level directory is chowned by a SSSD user

* Fri Mar 16 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-17
- Related:  rhbz#802207 - getent netgroup hangs when
                          "use_fully_qualified_names = TRUE" in sssd
- Resolves: rhbz#801719 - "Error looking up public keys" while ssh to replica
                          using IP address
- Resolves: rhbz#803659 - Service lookup shows case sensitive names twice with
                          case_sensitive=false
- Resolves: rhbz#803842 - Unable to bind to LDAP server when minssf set
- Resolves: rhbz#805034 - accessing an undefined variable might cause crash
- Resolves: rhbz#805108 - sss_ssh_knownhostproxy infinite loop hangs SSH login

* Mon Mar 12 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-15
- Update translations
- Resolves: rhbz#802372 - Pick up latest translation files for SSSD
- Resolves: rhbz#802207 - getent netgroup hangs when
                          "use_fully_qualified_names = TRUE" in sssd
- Related:  rhbz#801451 - Logging in with ssh pub key should consult
                          authentication authority policies

* Fri Mar 09 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-12
- Resolves: rhbz#801407 - sssd_nss gets hung processing identical search
                          requests
- Resolves: rhbz#801451 - Logging in with ssh pub key should consult
                          authentication authority policies
- Resolves: rhbz#795562 - Infinite loop checking Kerberos credentials
- Resolves: rhbz#798317 - sssd crashes when ipa_hbac_support_srchost is set to
                          true
- Resolves: rhbz#799039 - --debug option for sss_debuglevel doesn't work
- Resolves: rhbz#799915 - Unable to lookup netgroups with case_sensitive=false
- Resolves: rhbz#799929 - Raise limits for max num of files sssd_nss/sssd_pam
                          can use
- Resolves: rhbz#799971 - sssd_be crashes on shutdown
- Resolves: rhbz#801533 - sssd_be crashes when resolving non-trivial nested
                          group structure
- Resolves: rhbz#801368 - Group lookups doesn't return members with proxy
                          provider configured
- Resolves: rhbz#801377 - getent returns non-existing netgroup name, when sssd
                          is configured as proxy provider

* Thu Mar 01 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-11
- Do not auto-upgrade debug levels
- Tool still available for manual use
- Reverts:  rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade
- Resolves: rhbz#798881 - Install-time warnings
- Resolves: rhbz#798774 - IPA provider should assume that ipa_domain is also
                          the dns_discovery_domain
- Resolves: rhbz#798655 - Password logins failing due to a process with high
                          UID

* Wed Feb 29 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-10
- Fix explicit requires to use openldap instead of openldap-libs
- Related:  rhbz#797282 - sssd-1.5.1-66.el6.x86_64 needs
                          openldap >= openldap-2.4.23-20.el6.x86_64

* Tue Feb 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-9
- Fix multilib-clean issue due to upgrade script
- Remove old copy from the spec file
- Related:  rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade

* Tue Feb 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-8
- Fix multilib-clean issue due to upgrade script
- Fix typo in the patch
- Related:  rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade

* Tue Feb 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-7
- Fix multilib-clean issue due to upgrade script
- Use a patch and install the script to python_sitelib
- Related:  rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade

* Tue Feb 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-6
- Fix multilib-clean issue due to upgrade script
- Related:  rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade

* Tue Feb 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-5
- Resolves: rhbz#753763 - Provide logging configuration compatibility on
                          SSSD 1.5/1.6 upgrade
- Resolves: rhbz#785871 - wrong build dependency on nscd
- Resolves: rhbz#785873 - IPA host search base cannot be set
- Resolves: rhbz#791208 - Entries lacking a POSIX username value break group
                          lookups
- Resolves: rhbz#796307 - Simple Paged Search control needs to be used more
                          sparingly
- Resolves: rhbz#797282 - sssd-1.5.1-66.el6.x86_64 needs
                          openldap >= openldap-2.4.23-20.el6.x86_64
- Resolves: rhbz#787035 - ipa - sssd slow response with thousands of user
                          entries
- Resolves: rhbz#742509 - [RFE] Add SSSD Tool to purge cache
- Resolves: rhbz#772297 - Fails to update if all nisNetgroupTriple or
                          memberNisNetgroup entries are deleted from a
                          netgroup
- Resolves: rhbz#783138 - Backend occasionally goes offline under heavy load
- Resolves: rhbz#797975 - sssd_be: The requested target is not configured is
                          logged at each login
- Resolves: rhbz#735422 - Rebase SSSD to 1.8.0 in RHEL 6.3

* Wed Feb 15 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-4.beta3
- Resolves: rhbz#761570 - [RFE] support looking up autofs maps via SSSD
- Resolves: rhbz#788979 - sssd crashes during initgroups against a user
                          belonging to nested rfc2307bis group

* Fri Feb 10 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-3.beta2
- Handle filtering python Provides in a safer way
- Related:  rhbz#735422 - Rebase SSSD to 1.8.0 in RHEL 6.3

* Tue Feb 07 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.8.0-2.beta2
- Related:  rhbz#735422 - Rebase SSSD to 1.8.0 in RHEL 6.3
- Resolves: rhbz#786553 - sssd on ppc64 doesn't pull cyrus-sasl-gssapi.ppc as
                          a dependancy
- Resolves: rhbz#785909 - --debug-timestamps=1 is not passed to providers
- Resolves: rhbz#785908 - ldap_*_search_base doesn't fully limit the group and
                          netgroup search base correctly
- Resolves: rhbz#785907 - [RFE] Add support to request canonicalization on krb
                          AS requests
- Resolves: rhbz#785905 - [RFE] DEBUG timestamps should offer higher precision
- Resolves: rhbz#785904 - [RFE] SSSD should have --version option
- Resolves: rhbz#785902 - Errors with empty loginShell and proxy provider
- Resolves: rhbz#785898 - Enable midway cache refresh by default
- Resolves: rhbz#785888 - sssd returns empty netgroup at a second request for
                          a non-existing netgroup
- Resolves: rhbz#785884 - Honour TTL when resolving host names
- Resolves: rhbz#785883 - check DNS records before updates
- Resolves: rhbz#785881 - List the keytab to pick the princiapl to use instead
                          of guessing
- Resolves: rhbz#785880 - debug_level in sssd.conf overrides command-line
- Resolves: rhbz#785879 - sss_obfuscate/python config parser modifies config
                          file too much
- Resolves: rhbz#785877 - on reconnect we need to detect that a ipa/ds server
                          has been reinitialized
- Resolves: rhbz#785741 - sssd.api.conf and sssd.api.d should not be in /etc
- Resolves: rhbz#773660 - Kerberos errors should go to syslog
- Resolves: rhbz#772163 - Iterator loop reuse cases a tight loop in the native
                          IPA netgroups code
- Resolves: rhbz#771706 - sssd_be crashes during auth when there exists UTF
                          source host group in an hbacrule
- Resolves: rhbz#771702 - sssd_pam crashes during change password operation
                          against a IPA server
- Resolves: rhbz#771361 - case_sensitive function not working as intended for
                          ldap
- Resolves: rhbz#768935 - Crash when applying settings
- Resolves: rhbz#766941 - The full dyndns update message should be logged into
                          debug logs
- Resolves: rhbz#766930 - [RFE] Add a new option to override home directory
                          value
- Resolves: rhbz#766913 - [RFE] Add option to select validate and FAST keytab
                          principal name
- Resolves: rhbz#766907 - Use [...] for IPv6 addresses in kdc info files
- Resolves: rhbz#766904 - [RFE] Create a command line tool to change the debug
                          levels on the fly
- Resolves: rhbz#766876 - [RFE] Make HBAC srchost processing optional
- Resolves: rhbz#766141 - [RFE] SSSD should support FreeIPA's internal
                          netgroup representation
- Resolves: rhbz#761582 - [RFE] Add ldap_sasl_minssf option
- Resolves: rhbz#759186 - [abrt] sssd-1.6.3-1.fc16: ping_check: Process
                          /usr/sbin/sssd was killed by signal 11 (SIGSEGV)
- Resolves: rhbz#755506 - [RFE] Add host-based (pam_host_attr) access control
- Resolves: rhbz#753876 - [RFE] Add support for the services map
- Resolves: rhbz#746181 - "getgrgid call returned more than one result" after
                          group name change in MSAD
- Resolves: rhbz#744197 - [RFE] close LDAP connection to the server when idle
                          for some (configurable) time
- Resolves: rhbz#742510 - [RFE] Separate Cache Timeouts for SSSD
- Related:  rhbz#742509 - [RFE] Add SSSD Tool to purge cache
- Resolves: rhbz#742052 - id -G group resolution takes extremely long
- Resolves: rhbz#739312 - [RFE] sssd does not set shadowLastChange
- Resolves: rhbz#736150 - [RFE] SSSD should support multiple search bases
- Resolves: rhbz#735827 - [RFE] Ability to set a domain as case sensitive or
                          insensitive
- Resolves: rhbz#735405 - [RFE] Option to disable warnings for unknown users
- Resolves: rhbz#728212 - [RFE] sssd does not handle when paging control
                          disabled for openldap
- Resolves: rhbz#726467 - SSSD takes 30+ seconds to login
- Resolves: rhbz#721289 - Process /usr/libexec/sssd/sssd_be was killed by
                          signal 11 during auth when password for the user is
                          not set

* Tue Jan 17 2012 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-68
- Resolves: rhbz#773655 - Race-condition bug in LDAP auth provider

* Tue Nov 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-67
- Resolves: rhbz#753842 - sssd_nss crashes when passed invalid UTF-8 for the
                          username in getpwnam()
- Resolves: rhbz#758157 - LDAP failover not working if server refuses
                          connections

* Mon Oct 31 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-66
- Related:  rhbz#750359 - Major cached entry performance regression

* Mon Oct 31 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-65
- Resolves: rhbz#750359 - Major cached entry performance regression

* Mon Oct 31 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-64
- Resolves: rhbz#749822 - SSSD may go into infinite loop during RFC2307bis
                          initgroups when groups appear in multiple nesting
                          levels

* Wed Oct 26 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-63
- Resolves: rhbz#749256 - SELinux errors with SSSD Downgrade

* Tue Oct 25 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-62
- Resolves: rhbz#748924 - RHEL6.1/sssd_pam segmentation fault

* Tue Oct 25 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-61
- Resolves: rhbz#748412 - Memory leaks during the initgroups() operation

* Tue Oct 18 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-60
- Related:  rhbz#743841 - SSSD can crash due to dbus server removing a UNIX
                          socket

* Mon Oct 17 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-59
- Resolves: rhbz#742288 - RFC2307bis initgroups calls are slow
- Resolves: rhbz#746654 - SSSD backend gets killed on slow systems
- Related:  rhbz#743925 - HBAC processing is very slow when dealing with
                          FreeIPA deployments with large numbers of hosts
                          Fixes a crash introduced by the earlier patch.
- Related:  rhbz#733382 - SSSD should pick a user/group name when there are
                          multi-valued names
                          Fixes for internationalization

* Fri Oct 14 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-58
- Related:  rhbz#742278 - Rework the example config

* Fri Oct 14 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-57
- Resolves: rhbz#743925 - HBAC processing is very slow when dealing with
                          FreeIPA deployments with large numbers of hosts
- Resolves: rhbz#745966 - sssd_pam segfaults on sssd restart
- Related:  rhbz#743841 - SSSD can crash due to dbus server removing a UNIX
                          socket

* Thu Oct 13 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-56
- Resolves: rhbz#742278 - Rework the example config
- Resolves: rhbz#746037 - Only access sssd_nss internal hash table if it was
                          initialized
- Resolves: rhbz#742526 - SSSD's man pages are missing information
- Resolves: rhbz#743841 - SSSD can crash due to dbus server removing a UNIX
                          socket

* Thu Oct 06 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-55
- Resolves: rhbz#738621 - Lookup fails for non-primary usernames with
                          multi-valued uid
- Resolves: rhbz#738629 - Group lookups doesn't return it's member for
                          sometime when the member has multi-valued uid
- Resolves: rhbz#742295 - Use an explicit base 10 when converting uidNumber
                          to integer
- Resolves: rhbz#733382 - SSSD should pick a user/group name when there are
                          multi-valued names

* Fri Sep 30 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-53
- Resolves: rhbz#741751 - HBAC rule evaluation does not properly handle host
                          groups
- Resolves: rhbz#740501 - SSSD not functional after "self" reboot
- Resolves: rhbz#742539 - HBAC: Hostname comparisons should be
                          case-insensitive

* Tue Sep 20 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-52
- Resolves: rhbz#728343 - SSSD taking 5 minutes to log in
- Resolves: rhbz#739850 - Coverity defects newly introduced in rhel 6.2

* Mon Sep 12 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-51
- Resolves: rhbz#737157 - "System error" appears in log during change password
                          operation of a user in openldap server with ppolicy
                          enabled
- Resolves: rhbz#737172 - "Unknown (private extension) error(21853), (null)"
                          messages are logged during change password operation
                          of a user in openldap server with ppolicy enabled

* Wed Sep 07 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-50
- Resolves: rhbz#736314 - sssd crashes during auth while there exists multiple
                          external hosts along with managed host
- Resolves: rhbz#732974 - [RFE] Have SSSD cache properly with
  krb5_validate = True and SElinux enabled

* Mon Aug 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-49
- Resolves: rhbz#732010 - LDAP+GSSAPI needs explicit Kerberos realm
- Resolves: rhbz#733382 - SSSD should pick a user/group name when there are
                          multi-valued names
- Resolves: rhbz#733409 - Improve password policy error message
- Resolves: rhbz#733663 - Authentication fails when there exists an empty
                          hbacsvcgroup
- Resolves: rhbz#732935 - Add LDAP provider option to set
                          LDAP_OPT_X_SASL_NOCANON
- Resolves: rhbz#734101 - sssd blocks login of ipa-users

* Wed Aug 24 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-48
- Related:  rhbz#728353 - Resolve RPMDiff errors in SSSD

* Mon Aug 08 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-47
- Resolves: rhbz#728961 - Provide a mechanism for vetoing the use of certain
                          shells

* Thu Aug 04 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-46
- Related:  rhbz#728267 - When non-posix groups are skipped, initgroups
                          returns random GID

* Thu Aug 04 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-45
- Related:  rhbz#726466 - HBAC rule evaluation does not support extended
                          UTF-8 languages
- Related:  rhbz#718250 - Remove DENY rules from the HBAC access provider
- Fixes an issue on big endian platforms

* Thu Aug 04 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-44
- Resolves: rhbz#700828 - Process /usr/libexec/sssd/sssd_be was killed by
                          signal 11 (SIGSEGV) when ldap_uri is misconfigured
- Resolves: rhbz#726438 - sssd doesn't honor ldap supportedControls 
- Resolves: rhbz#726466 - HBAC rule evaluation does not support extended
                          UTF-8 languages
- Resolves: rhbz#718250 - Remove DENY rules from the HBAC access provider
- Resolves: rhbz#728267 - When non-posix groups are skipped, initgroups
                          returns random GID
- Resolves: rhbz#726475 - sssd_pam leaks file descriptors
- Resolves: rhbz#725868 - Explicitly ignore groups with gidNumber = 0

* Wed Jul 13 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-43
- Related:  rhbz#721052 - sssd does not handle kerberos server IP change
-                         Use ares_search instead of ares_query to honor
-                         search entries in /etc/resolv.conf

* Wed Jul 13 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-42
- Resolves: rhbz#711416 - During the change password operation the ccache is
-                         not replaced by a new one if the old one isn't
-                         active anymore
- Resolves: rhbz#715609 - Certificate validation fails with message
-                         "Connection error: TLS: hostname does not match CN
-                         in peer certificate"
- Resolves: rhbz#719089 - IPA dynamic DNS update mangles AAAA records
- Resolves: rhbz#721052 - sssd does not handle kerberos server IP change
-                         Honor TTL values when resolving hostnames

* Fri Jun 24 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-41
- Resolves: rhbz#713961 - libsss_ldap segfault at login against OpenLDAP
- Resolves: rhbz#713438 - sssd shuts down if inotify crashes

* Thu Jun 02 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-40
- Resolves: rhbz#709081 - sssd.$arch should require sssd-client.$arch

* Thu Jun 02 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-39
- Resolves: rhbz#709342 - Typo in negative cache notification for initgroups()
- Resolves: rhbz#708009 - "renew_all_tgts" and "renew_handlers" messages are
-                         being logged multiple times when the provider comes
-                         back online
- Resolves: rhbz#707997 - The IPA provider does not work with IPv6
- Resolves: rhbz#677327 - [RFE] Support overriding attribute value
- Resolves: rhbz#692090 - SSSD is not populating nested groups in
-                         Active Directory


* Fri May 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-38
- Resolves: rhbz#707627 - Include valid "ldap_uri" formats in sssd-ldap man
-                         page

* Wed May 25 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-37
- Resolves: rhbz#707513 - Unable to authenticate users when username
-                         contains "\0"

* Tue May 24 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-36
- Resolves: rhbz#698723 - kpasswd fails when using sssd and
-                         kadmin server != kdc server

* Tue May 24 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-35
- Resolves: rhbz#707282 - latest sssd fails if ldap_default_authtok_type is
-                         not mentioned
- Resolves: rhbz#692404 - rfc2307bis groups are being enumerated even when the
-                         gidNumber is out of the range of min_id,max_id.
- Resolves: rhbz#699530 - Users with a local group as their primary GID are
-                         denied access by the simple access provider
- Resolves: rhbz#700172 - RFE: SSSD should support paged LDAP lookups
- Resolves: rhbz#705434 - IPA provider fails initgroups() if user is not a
-                         member of any group
- Resolves: rhbz#703624 - SSSD's async resolver only tries the first
-                         nameserver in /etc/resolv.conf

* Tue May 03 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-34
- Resolves: rhbz#701700 - sssd client libraries use select() but should use
-                         poll() instead

* Mon May 02 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-33
- Related: rhbz#693818 - Automatic TGT renewal overwrites cached password
- Fix segfault in TGT renewal

* Fri Apr 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-32
- Related: rhbz#693818 - Automatic TGT renewal overwrites cached password
- Fix typo causing build breakage

* Fri Apr 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-31
- Resolves: rhbz#693818 - Automatic TGT renewal overwrites cached password

* Fri Apr 15 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-30
- Resolves: rhbz#696972 - Filters not honoured against fully-qualified users

* Thu Apr 14 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-29
- Resolves: rhbz#694146 - SSSD consumes GBs of RAM, possible memory leak

* Tue Apr 12 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-28
- Related:  rhbz#691678 - SSSD needs to fall back to 'cn' for GECOS
-                         information

* Tue Apr 12 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-27
- Related:  rhbz#694783 - SSSD crashes during getent when anonymous bind is
-                         disabled

* Mon Apr 11 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-26
- Resolves: rhbz#694444 - Unable to resolve SRV record when called with
-                         _srv_,<fixed ldap uri> in ldap_uri
- Related:  rhbz#694783 - SSSD crashes during getent when anonymous bind is
-                         disabled

* Fri Apr 08 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-25
- Resolves: rhbz#694783 - SSSD crashes during getent when anonymous bind is
-                         disabled

* Fri Apr 01 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-24
- Resolves: rhbz#692472 - Process /usr/libexec/sssd/sssd_be was killed by
-                         signal 11 (SIGSEGV)
-                         Fix is to not attempt to resolve nameless servers

* Wed Mar 30 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-23
- Resolves: rhbz#691678 - SSSD needs to fall back to 'cn' for GECOS
-                         information

* Mon Mar 28 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-21
- Resolves: rhbz#690866 - Groups with a zero-length memberuid attribute can
-                         cause SSSD to stop caching and responding to
-                         requests

* Fri Mar 25 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-20
- Resolves: rhbz#690131 - Traceback messages seen while interrupting
-                         sss_obfuscate using ctrl+d
- Resolves: rhbz#690421 - [abrt] sssd-1.2.1-28.el6_0.4: _talloc_free: Process
-                         /usr/libexec/sssd/sssd_be was killed by signal 11
-                         (SIGSEGV)

* Mon Mar 21 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-17
- Related: rhbz#683885 - SSSD should skip over groups with multiple names

* Mon Mar 21 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-16
- Resolves: rhbz#683158 - SSSD breaks on RDNs with a comma in them
- Resolves: rhbz#689886 - group memberships are not populated correctly during
-                         IPA provider initgroups
- Resolves: rhbz#683885 - SSSD should skip over groups with multiple names

* Wed Mar 09 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-15
- Resolves: rhbz#683860 - Skip users and groups that have incomplete contents
- Resolves: rhbz#688491 - authconfig fails when access_provider is set as krb5
-                         in sssd.conf

* Wed Mar 09 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-14
- Resolves: rhbz#683255 - sudo/ldap lookup via sssd gets stuck for 5min
-                         waiting on netgroup
- Resolves: rhbz#683431 - sssd consumes 100% CPU
- Related: rhbz#680440  - sssd does not handle kerberos server IP change

* Tue Mar 08 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-13
- Related: rhbz#680440 - sssd does not handle kerberos server IP change
-   SSSD was staying with the old server if it was still online

* Mon Mar 07 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-12
- Resolves: rhbz#682850 - IPA provider should use realm instead of ipa_domain
-                         for base DN

* Mon Mar 07 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-11
- Resolves: rhbz#682340 - sssd-be segmentation fault - ipa-client on
-                         ipa-server
- Resolves: rhbz#680440 - sssd does not handle kerberos server IP change
- Resolves: rhbz#680442 - Dynamic DNS update fails if multiple servers are
-                         given in ipa_server config option
- Resolves: rhbz#680932 - Do not delete sysdb memberOf if there is no memberOf
-                         attribute on the server
- Resolves: rhbz#682807 - sssd_nss core dumps with certain lookups

* Tue Feb 22 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-10
- Related: rhbz#678614 - SSSD needs to look at IPA's compat tree for netgroups
- Related: rhbz#679082 - SSSD IPA provider should honor the krb5_realm option

* Tue Feb 22 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-9
- Resolves: rhbz#679082 - SSSD IPA provider should honor the krb5_realm option
- Resolves: rhbz#677318 - Does not read renewable ccache at startup

* Mon Feb 21 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-8
- Resolves: rhbz#678593 - User information not updated on login for secondary
-                         domains
- Resolves: rhbz#678777 - IPA provider does not update removed group
-                         memberships on initgroups

* Sat Feb 19 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-7
- Resolves: rhbz#677588 - sssd crashes at the next tgt renewals it tries
- Resolves: rhbz#678410 - name service caches names, so id command shows
-                         recently deleted users
- Resolves: rhbz#678614 - SSSD needs to look at IPA's compat tree for
-                         netgroups

* Tue Feb 08 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-6
- Resolves: rhbz#670511 - SSSD and sftp-only jailed users with pubkey login
- Resolves: rhbz#675284 - "no matching rule" message logged on all successful
-                         requests
- Resolves: rhbz#676911 - SSSD attempts to use START_TLS over LDAPS for
-                         authentication

* Thu Feb 03 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-5
- Resolves: rhbz#674164 - sss_obfuscate fails if there's no domain named
-                         "default"
- Resolves: rhbz#674515 - -p option always uses empty string to obfuscate
-                         password
- Resolves: rhbz#674141 - Traceback call messages displayed while
-                         "sss_obfuscate" command is executed as a non-root
-                         user

* Tue Feb 01 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-4
- Resolves: rhbz#674172 - Group members are not sanitized in nested group
- processing
- Put translated tool manpages into the sssd-tools subpackage

* Thu Jan 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-3
- Related:  rhbz#670259 - Refresh SSSD in 6.1 to 1.5.1
- Also add the updated ding-libs to the BuildRequires

* Thu Jan 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-2
- Related:  rhbz#670259 - Refresh SSSD in 6.1 to 1.5.1
- Explicitly require updated ding-libs

* Thu Jan 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.1-1
- Resolves: rhbz#670259 - Refresh SSSD in 6.1 to 1.5.1
- New upstream release 1.5.1
- Addresses CVE-2010-4341 - DoS in sssd PAM responder can prevent logins
- Vast performance improvements when enumerate = true
- All PAM actions will now perform a forced initgroups lookup instead of just
- a user information lookup
-   This guarantees that all group information is available to other
-   providers, such as the simple provider.
- For backwards-compatibility, DNS lookups will also fall back to trying the
- SSSD domain name as a DNS discovery domain.
- Support for more password expiration policies in LDAP
-    389 Directory Server
-    FreeIPA
-    ActiveDirectory
- Support for ldap_tls_{cert,key,cipher_suite} config options
- Assorted bugfixes

* Thu Jan 13 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-2
- Add noverify to sssd.conf
- Resolves: rhbz#627165 - TPS VerifyTest failure

* Thu Dec 23 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.5.0-1
- Related: rhbz#644072 - Rebase SSSD to 1.5
- New upstream release 1.5.0
- Fixed issues with LDAP search filters that needed to be escaped
- Add Kerberos FAST support on platforms that support it
- Reduced verbosity of PAM_TEXT_INFO messages for cached credentials
- Added a Kerberos access provider to honor .k5login
- Addressed several thread-safety issues in the sss_client code
- Improved support for delayed online Kerberos auth
- Significantly reduced time between connecting to the network/VPN and
- acquiring a TGT
- Added feature for automatic Kerberos ticket renewal
- Provides the kerberos ticket for long-lived processes or cron jobs
- even when the user logs out
- Added several new features to the LDAP access provider
- Support for 'shadow' access control
- Support for authorizedService access control
- Ability to mix-and-match LDAP access control features
- Added an option for a separate password-change LDAP server for those
- platforms where LDAP referrals are not supported
- Added support for manpage translations

* Tue Dec 07 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-28.4
- Resolves: rhbz#660592 - SSSD shutdown sometimes hangs
- Resolves: rhbz#660585 - getent passwd <username>' returns nothing if its
-                         uidNumber gt 2147483647

* Thu Dec 02 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-36
- Resolves: rhbz#659401 - SSSD shutdown sometimes hangs

* Thu Dec 02 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-35
- Resolves: rhbz#645449 - 'getent passwd <username>' returns nothing if its
-                         uidNumber gt 2147483647

* Tue Nov 30 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-28.3
- Resolves: rhbz#658374 - sssd stops on upgrade

* Wed Nov 24 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-34
- Resolves: rhbz#658158 - sssd stops on upgrade

* Wed Nov 03 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-28.2
- Resolves: rhbz#649312 - SSSD will sometimes lose groups from the cache

* Wed Nov 03 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-33
- Resolves: rhbz#649286 - SSSD will sometimes lose groups from the cache

* Mon Oct 11 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-28.1
- Resolves: rhbz#637070 - the krb5 locator plugin isn't packaged for multilib
- Resolves: rhbz#642412 - SSSD initgroups does not behave as expected

* Mon Oct 11 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-32
- Resolves: rhbz#633406 - the krb5 locator plugin isn't packaged for multilib
- Resolves: rhbz#633487 - SSSD initgroups does not behave as expected

* Thu Sep 23 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-29
- Resolves: rhbz#633406 - the krb5 locator plugin isn't packaged for multilib

* Fri Sep 03 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-28
- Resolves: rhbz#629949 - sssd stops on upgrade

* Wed Aug 18 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-27
- Resolves: rhbz#625122 - GNOME Lock Screen unocks without a password

* Wed Aug 04 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-26
- Resolves: rhbz#621307 - Password changes are broken on LDAP

* Fri Jul 30 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-23
- Resolves: rhbz#617623 - SSSD suffers from serious performance issues on
-                         initgroups calls

* Fri Jul 23 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-21
- Resolves: rhbz#607233 - SSSD users cannot log in through GDM
-                       - Real issue was that long-running services
-                       - do not reconnect if sssd is restarted

* Fri Jul 09 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-20
- Resolves: rhbz#591715 - sssd should emit warnings if there are problems with
-                         /etc/krb5.keytab file

* Mon Jun 28 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-19
- Resolves: rhbz#606836 - libcollection needs an soname bump before RHEL 6
-                         final
- Resolves: rhbz#608661 - SASL with OpenLDAP server fails
- Resolves: rhbz#608688 - SSSD doesn't properly request RootDSE attributes

* Fri Jun 18 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-15
- New upstream bugfix release 1.2.1
- Resolves: rhbz#601770 - SSSD in RHEL 6.0 should ship with zero open Coverity
-                         bugs.
- Resolves: rhbz#603041 - Remove unnecessary option krb5_changepw_principal
- Resolves: rhbz#604704 - authconfig should provide error with no trace back
-                         if disabling sssd when sssd is not enabled
- Resolves: rhbz#591873 - Connecting to the network after an offline kerberos
-                         auth logs continuous error messages to sssd_ldap.log
- Resolves: rhbz#596295 - Authentication fails for user from the second domain
-                         when the same user name is filtered out from the
-                         first domain
- Related:  rhbz#598559 - Update translation files for SSSD before RHEL 6
-                         final

* Thu Jun 10 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-14
- Resolves: rhbz#593696 - Empty list of simple_allow_users causes sssd service
-                         to fail while restart
- Resolves: rhbz#600352 - Wrapping the value for "ldap_access_filter" in
-                         parentheses causes ldap_search_ext to fail
- Resolves: rhbz#600468 - Segfault in krb5_child
- Related:  rhbz#601770 - SSSD in RHEL 6.0 should ship with zero open Coverity
-                         bugs.

* Wed Jun 02 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-13
- Resolves: rhbz#598670 - Ccache file of a user is removed too early
- Resolves: rhbz#599057 - Incomplete comparison of a service name in
-                         IPA access provider
- Resolves: rhbz#598496 - Failure with IPA access provider
- Resolves: rhbz#599027 - Makefile typo causes SSSD not to use the
-                         kernel keyring

* Mon May 24 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-12
- New stable upstream version 1.2.0
- Support ServiceGroups for FreeIPA v2 HBAC rules
- Fix long-standing issue with auth_provider = proxy
- Better logging for TLS issues in LDAP
- Resolves: rhbz#584001 - Rebase sssd to 1.2
- Resolves: rhbz#584017 - Unconfiguring sssd leaves KDC locator file
- Resolves: rhbz#587384 - authconfig fails if krb5_kpasswd in sssd.conf
- Resolves: rhbz#587743 - Need to replicate pam_ldap's pam_filter in sssd.conf
- Resolves: rhbz#590134 - sssd: auth_provider = proxy regression
- Resolves: rhbz#591131 - Kerberos provider needs to rewrite kdcinfo file when
-                         going online
- Resolves: rhbz#591136 - Change SSSD ipa BE to handle new structure of the
-                         HBAC rule

* Wed May 19 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.92-11.1
- Improve DEBUG logs for STARTTLS failures

* Tue May 18 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.92-11
- New LDAP access provider allows for filtering user access by LDAP attribute
- Reduced default timeout for detecting offline status with LDAP
- GSSAPI ticket lifetime made configurable
- Better offline->online transition support in Kerberos

* Fri May 07 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.91-10
- Release new upstream version 1.1.91
- Enhancements when using SSSD with FreeIPA v2
- Support for deferred kinit
- Support for DNS SRV records for failover

* Fri Apr 02 2010 Simo Sorce <ssorce@redhat.com> - 1.1.1-3
- Bump up release number to avoid library sub-packages version issues with
  previous releases.

* Thu Apr 01 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.1-1
- New upstream release 1.1.1
- Fixed the IPA provider (which was segfaulting at start)
- Fixed a bug in the SSSDConfig API causing some options to revert to
- their defaults
- This impacted the Authconfig UI
- Ensure that SASL binds to LDAP auto-retry when interrupted by a signal

* Tue Mar 22 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-2
- Release SSSD 1.1.0 final
- Fix two potential segfaults
- Fix memory leak in monitor
- Better error message for unusable confdb

* Wed Mar 17 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-1.pre20100317git0ea7f19
- Release candidate for SSSD 1.1
- Add simple access provider
- Create subpackages for libcollection, libini_config, libdhash and librefarray
- Support IPv6
- Support LDAP referrals
- Fix cache issues
- Better feedback from PAM when offline

* Wed Feb 24 2010 Stephen Gallagehr <sgallagh@redhat.com> - 1.0.5-2
- Rebuild against new libtevent

* Fri Feb 19 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.0.5-1
- Fix licenses in sources and on RPMs

* Mon Jan 25 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Fix regression on 64-bit platforms

* Fri Jan 22 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- Fixes link error on platforms that do not do implicit linking
- Fixes double-free segfault in PAM
- Fixes double-free error in async resolver
- Fixes support for TCP-based DNS lookups in async resolver
- Fixes memory alignment issues on ARM processors
- Manpage fixes

* Thu Jan 14 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Fixes a bug in the failover code that prevented the SSSD from detecting when it went back online
- Fixes a bug causing long (sometimes multiple-minute) waits for NSS requests
- Several segfault bugfixes

* Mon Jan 11 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Fix CVE-2010-0014

* Mon Dec 21 2009 Stephen Gallagher <sgallagh@redhat.com> - 1.0.0-2
- Patch SSSDConfig API to address
- https://bugzilla.redhat.com/show_bug.cgi?id=549482

* Fri Dec 18 2009 Stephen Gallagher <sgallagh@redhat.com> - 1.0.0-1
- New upstream stable release 1.0.0

* Fri Dec 11 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.99.1-1
- New upstream bugfix release 0.99.1

* Mon Nov 30 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.99.0-1
- New upstream release 0.99.0

* Tue Oct 27 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.7.1-1
- Fix segfault in sssd_pam when cache_credentials was enabled
- Update the sample configuration
- Fix upgrade issues caused by data provider service removal

* Mon Oct 26 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.7.0-2
- Fix upgrade issues from old (pre-0.5.0) releases of SSSD

* Fri Oct 23 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.7.0-1
- New upstream release 0.7.0

* Thu Oct 15 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.6.1-2
- Fix missing file permissions for sssd-clients

* Tue Oct 13 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.6.1-1
- Add SSSDConfig API
- Update polish translation for 0.6.0
- Fix long timeout on ldap operation
- Make dp requests more robust

* Tue Sep 29 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.6.0-1
- Ensure that the configuration upgrade script always writes the config
  file with 0600 permissions
- Eliminate an infinite loop in group enumerations

* Mon Sep 28 2009 Sumit Bose <sbose@redhat.com> - 0.6.0-0
- New upstream release 0.6.0

* Mon Aug 24 2009 Simo Sorce <ssorce@redhat.com> - 0.5.0-0
- New upstream release 0.5.0

* Wed Jul 29 2009 Jakub Hrozek <jhrozek@redhat.com> - 0.4.1-4
- Fix for CVE-2009-2410 - Native SSSD users with no password set could log in
  without a password. (Patch by Stephen Gallagher)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Simo Sorce <ssorce@redhat.com> - 0.4.1-2
- Fix a couple of segfaults that may happen on reload

* Thu Jun 11 2009 Simo Sorce <ssorce@redhat.com> - 0.4.1-1
- add missing configure check that broke stopping the daemon
- also fix default config to add a missing required option

* Mon Jun  8 2009 Simo Sorce <ssorce@redhat.com> - 0.4.1-0
- latest upstream release.
- also add a patch that fixes debugging output (potential segfault)

* Mon Apr 20 2009 Simo Sorce <ssorce@redhat.com> - 0.3.2-2
- release out of the official 0.3.2 tarball

* Mon Apr 20 2009 Jakub Hrozek <jhrozek@redhat.com> - 0.3.2-1
- bugfix release 0.3.2
- includes previous release patches
- change permissions of the /etc/sssd/sssd.conf to 0600

* Tue Apr 14 2009 Simo Sorce <ssorce@redhat.com> - 0.3.1-2
- Add last minute bug fixes, found in testing the package

* Mon Apr 13 2009 Simo Sorce <ssorce@redhat.com> - 0.3.1-1
- Version 0.3.1
- includes previous release patches

* Mon Apr 13 2009 Simo Sorce <ssorce@redhat.com> - 0.3.0-2
- Try to fix build adding automake as an explicit BuildRequire
- Add also a couple of last minute patches from upstream

* Mon Apr 13 2009 Simo Sorce <ssorce@redhat.com> - 0.3.0-1
- Version 0.3.0
- Provides file based configuration and lots of improvements

* Tue Mar 10 2009 Simo Sorce <ssorce@redhat.com> - 0.2.1-1
- Version 0.2.1

* Tue Mar 10 2009 Simo Sorce <ssorce@redhat.com> - 0.2.0-1
- Version 0.2.0

* Sun Mar 08 2009 Jakub Hrozek <jhrozek@redhat.com> - 0.1.0-5.20090309git691c9b3
- package git snapshot

* Fri Mar 06 2009 Jakub Hrozek <jhrozek@redhat.com> - 0.1.0-4
- fixed items found during review
- added initscript

* Thu Mar 05 2009 Sumit Bose <sbose@redhat.com> - 0.1.0-3
- added sss_client

* Mon Feb 23 2009 Jakub Hrozek <jhrozek@redhat.com> - 0.1.0-2
- Small cleanup and fixes in the spec file

* Thu Feb 12 2009 Stephen Gallagher <sgallagh@redhat.com> - 0.1.0-1
- Initial release (based on version 0.1.0 upstream code)

