# Define ONLY_CLIENT to only make the ipa-client, ipa-python and
# ipa-admintools subpackages
%{!?ONLY_CLIENT:%global ONLY_CLIENT 0}

%ifarch x86_64 %{ix86}
# Nothing, we want to force just building client on non-Intel
%else
%global ONLY_CLIENT 1
%endif

%global httpd_conf /etc/httpd/conf.d
%global plugin_dir %{_libdir}/dirsrv/plugins
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%global POLICYCOREUTILSVER 2.0.83-19.24
%global gettext_domain ipa
%global VERSION 3.0.0

Name:           ipa
Version:        3.0.0
Release:        50%{?date}%{?dist}.3
Summary:        The Identity, Policy and Audit system

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.freeipa.org/
Source0:        http://www.freeipa.org/downloads/src/freeipa-%{VERSION}.tar.gz
Source1:        rh-ipabanner.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0001:      0001-Remove-bogus-check-for-smbpasswd.patch
Patch0002:      0002-Add-uninstall-command-hints-to-ipa-install.patch
Patch0003:      0003-Don-t-configure-a-reverse-zone-if-not-desired-in-int.patch
Patch0004:      0004-extdom-handle-INP_POSIX_UID-and-INP_POSIX_GID-reque.patch
Patch0005:      0005-log-dogtag-errors.patch
Patch0006:      0006-Simpler-instructions-to-generate-certificate.patch
Patch0007:      0007-Fix-requesting-certificates-that-contain-subject-alt.patch
Patch0008:      0008-Create-reverse-zone-in-unattended-mode.patch
Patch0009:      0009-Add-fallback-for-httpd-restarts-on-sysV-platforms.patch
Patch0010:      0010-Report-ipa-upgradeconfig-errors-during-RPM-upgrade.patch
Patch0011:      0011-Refactoring-of-default.conf-man-page.patch
Patch0012:      0012-Make-service-naming-in-ipa-server-install-consistent.patch
Patch0013:      0013-Improve-error-messages-in-ipa-replica-manage.patch
Patch0014:      0014-Fixed-incorrect-link-to-browser-config-after-session.patch
Patch0015:      0015-ipa-client-automount-Add-the-autofs-service-if-it-d.patch
Patch0016:      0016-Remove-servertrls-and-clientctrls-options-from-renam.patch
Patch0017:      0017-The-SECURE_NFS-value-needs-to-be-lower-case-yes-on-S.patch
Patch0018:      0018-Use-common-encoding-in-modlist-generation.patch
Patch0019:      0019-Wait-for-the-directory-server-to-come-up-when-updati.patch
Patch0020:      0020-Resolve-external-members-from-trusted-domain-via-Glo.patch
Patch0021:      0021-Reword-description-of-the-passsync-option-of-ipa-rep.patch
Patch0022:      0022-Set-MLS-MCS-for-user_u-context-to-what-will-be-on-re.patch
Patch0023:      0023-Clarify-trust-add-help-regarding-multiple-runs-again.patch
Patch0024:      0024-Process-relative-nameserver-DNS-record-correctly.patch
Patch0025:      0025-Handle-the-case-where-there-are-no-replicas-with-lis.patch
Patch0026:      0026-ipa-adtrust-install-allow-to-reset-te-NetBIOS-domain.patch
Patch0027:      0027-Do-not-require-resolvable-nameserver-in-DNS-install.patch
Patch0028:      0028-Disable-global-forwarding-per-zone.patch
Patch0029:      0029-Web-UI-disable-global-forwarding-per-zone.patch
Patch0030:      0030-ipasam-better-Kerberos-error-handling-in-ipasam.patch
Patch0031:      0031-Filter-suffix-in-replication-management-tools.patch
Patch0032:      0032-trusts-replace-use-of-python-crypto-by-m2crypto.patch
Patch0033:      0033-Propagate-kinit-errors-with-trust-account.patch
Patch0034:      0034-WebUI-Change-of-default-value-of-type-of-new-group-b.patch
Patch0035:      0035-Editable-sshkey-mac-address-field-after-upgrade.patch
Patch0036:      0036-MS-PAC-Special-case-NFS-services.patch
Patch0037:      0037-Lookup-the-user-SID-in-external-group-as-well.patch
Patch0038:      0038-Restart-sssd-after-authconfig-update.patch
Patch0039:      0039-Do-not-recommend-how-to-configure-DNS-in-error-messa.patch
Patch0040:      0040-Honor-the-kdb-options-disabling-KDC-writes-in-ipa_lo.patch
Patch0041:      0041-Add-detection-for-users-from-trusted-invalid-realms.patch
Patch0042:      0042-Better-error-message-for-login-of-users-from-other-r.patch
Patch0043:      0043-ipachangeconf-allow-specifying-non-default-delimeter.patch
Patch0044:      0044-Specify-includedir-in-krb5.conf-on-new-installs.patch
Patch0045:      0045-Upload-CA-cert-in-the-directory-on-install.patch
Patch0046:      0046-Update-plugin-to-upload-CA-certificate-to-LDAP.patch
Patch0047:      0047-Do-SSL-CA-verification-and-hostname-validation.patch
Patch0048:      0048-Use-secure-method-to-acquire-IPA-CA-certificate.patch
Patch0049:      0049-Compliant-client-side-session-cookie-behavior.patch
Patch0050:      0050-After-unininstall-see-if-certmonger-is-still-trackin.patch
Patch0051:      0051-Enable-SSSD-on-client-install.patch
Patch0052:      0052-Fix-delegation-find-command-group-handling.patch
Patch0053:      0053-Cookie-Expires-date-should-be-locale-insensitive.patch
Patch0054:      0054-Do-not-crash-when-Kerberos-SRV-record-is-not-found.patch
Patch0055:      0055-Allow-PKI-CA-Replica-Installs-when-CRL-exceeds-defau.patch
Patch0056:      0056-Convert-uniqueMember-members-into-DN-objects.patch
Patch0057:      0057-permission-find-no-longer-crashes-with-targetgroup.patch
Patch0058:      0058-Avoid-CRL-migration-error-message.patch
Patch0059:      0059-Sort-LDAP-updates-properly.patch
Patch0060:      0060-Upgrade-process-should-not-crash-on-named-restart.patch
Patch0061:      0061-Improve-ipa-replica-prepare-error-message.patch
Patch0062:      0062-Use-new-certmonger-locking-to-prevent-NSS-database-c.patch
Patch0063:      0063-Installer-should-not-connect-to-127.0.0.1.patch
Patch0064:      0064-Don-t-initialize-NSS-if-we-don-t-have-to-clean-up-un.patch
Patch0065:      0065-Update-anonymous-access-ACI-to-protect-secret-attrib.patch
Patch0066:      0066-Fix-migration-for-openldap-DS.patch
Patch0067:      0067-Improve-migration-performance.patch
Patch0068:      0068-Add-LDAP-server-fallback-to-client-installer.patch
Patch0069:      0069-Prevent-a-crash-when-no-entries-are-successfully-mig.patch
Patch0070:      0070-Add-missing-v3-schema-on-upgrades-fix-typo-in-schema.patch
Patch0071:      0071-Remove-ORDERING-for-IA5-attributeTypes.patch
Patch0072:      0072-Allow-ipa-replica-conncheck-and-ipa-adtrust-install-.patch
Patch0073:      0073-Fix-includedir-directive-in-krb5.conf-template.patch
Patch0074:      0074-ipa-client-discovery-with-anonymous-access-off.patch
Patch0075:      0075-Avoid-double-base64-encoding.patch
Patch0076:      0076-Fix-merge-error-in-renew_ca_cert.patch
Patch0077:      0077-Fix-lockout-of-LDAP-bind.patch
Patch0078:      0078-Deprecate-HBAC-source-hosts-from-CLI.patch
Patch0079:      0079-Remove-any-reference-to-HBAC-source-hosts-from-help.patch
Patch0080:      0080-Remove-HBAC-source-hosts-from-web-UI.patch
Patch0081:      0081-Use-temporary-CCACHE-in-ipa-client-install.patch
Patch0082:      0082-Improve-client-install-LDAP-cert-retrieval-fallback.patch
Patch0083:      0083-Allow-host-re-enrollment-using-delegation.patch
Patch0084:      0084-Apply-LDAP-update-files-in-blocks-of-10-as-originall.patch
Patch0085:      0085-Add-userClass-attribute-for-hosts.patch
Patch0086:      0086-CLDAP-Fix-domain-handling-in-netlogon-requests.patch
Patch0087:      0087-CLDAP-Return-empty-reply-on-non-fatal-errors.patch
Patch0088:      0088-Fix-cldap-parser-to-work-with-a-single-equality-filt.patch
Patch0089:      0089-Use-LDAP-search-instead-of-group_show-to-check-if-a-.patch
Patch0090:      0090-Use-LDAP-search-instead-of-group_show-to-check-for-a.patch
Patch0091:      0091-Use-LDAP-modify-operation-directly-to-add-remove-gro.patch
Patch0092:      0092-Add-missing-substring-indices-for-attributes-managed.patch
Patch0093:      0093-Add-new-hidden-command-option-to-suppress-processing.patch
Patch0094:      0094-Web-UI-search-optimization.patch
Patch0095:      0095-Change-group-ownership-of-CRL-publish-directory.patch
Patch0096:      0096-ipa-kdb-Support-Windows-2012-Server.patch
Patch0097:      0097-Return-the-correct-Content-type-on-negotiated-XML-RP.patch
Patch0098:      0098-Make-gecos-field-editable-in-Web-UI.patch
Patch0099:      0099-ipa-client-install-Do-not-request-host-certificate-i.patch
Patch0100:      0100-ipa-kdb-avoid-ENOMEM-when-all-SIDs-are-filtered-out.patch
Patch0101:      0101-ipa-kdb-remove-memory-leaks.patch
Patch0102:      0102-Fix-RUV-search-scope-in-ipa-replica-manage.patch
Patch0103:      0103-Use-default.conf-as-flag-of-IPA-client-being-install.patch
Patch0104:      0104-cainstance-Read-CS.cfg-for-preop.pin-in-a-loop.patch
Patch0105:      0105-Remove-disabled-entries-from-sudoers-compat-tree.patch
Patch0106:      0106-Properly-handle-ipa-replica-install-when-its-zone-is.patch
Patch0107:      0107-Administrative-password-change-does-not-respect-pass.patch
Patch0108:      0108-Winsync-re-initialize-should-not-run-memberOf-fixup-.patch
Patch0109:      0109-ipalib.frontend-Do-API-version-check-before-converti.patch
Patch0110:      0110-Prevent-garbage-from-readline-on-standard-output-of-.patch
Patch0111:      0111-Fallback-to-global-policy-in-ipa-lockout-plugin.patch
Patch0112:      0112-ipa-lockout-do-not-fail-when-default-realm-cannot-be.patch
Patch0113:      0113-Harmonize-policy-discovery-to-kdb-driver.patch
Patch0114:      0114-Make-ipa-client-automount-backwards-compatible.patch
Patch0115:      0115-Increase-service-startup-timeout-default.patch
Patch0116:      0116-Proxy-PKI-clone-ca-ee-ca-profileSubmit-URI.patch
Patch0117:      0117-Use-EXTERNAL-auth-mechanism-in-ldapmodify.patch
Patch0118:      0118-DNS-classless-support-for-reverse-domains.patch
Patch0119:      0119-Don-t-add-another-nsDS5ReplicaId-on-updates-if-one-a.patch
Patch0120:      0120-ipa-client-Set-NIS-domain-name-in-the-installer.patch
Patch0121:      0121-ipa-client-install-Configure-sudo-to-use-SSSD-as-dat.patch
Patch0122:      0122-ipasam-delete-trusted-child-domains-before-removing-.patch
Patch0123:      0123-ipa-sam-cache-gid-to-sid-and-uid-to-sid-requests-in-.patch
Patch0124:      0124-ipa-client-install-put-eol-character-after-the-last-.patch
Patch0125:      0125-Prefer-TCP-connections-to-UDP-in-krb5-clients.patch
Patch0126:      0126-ipa-client-install-added-new-option-kinit-attempts.patch
Patch0127:      0127-Use-IPA-CA-certificate-when-available-and-ignore-NO_.patch
Patch0128:      0128-Always-record-that-pkicreate-has-been-executed.patch
Patch0129:      0129-Use-NSS-protocol-range-API-to-set-available-TLS-prot.patch
Patch0130:      0130-PATCH-Add-TLS-1.2-to-the-protocol-list-in-mod_nss-co.patch
Patch0131:      0131-Do-not-corrupt-sshd_config-in-client-install-when-tr.patch
Patch0132:      0132-Fix-syntax-of-the-dc-attributeType.patch
Patch0133:      0133-Fix-syntax-errors-in-schema-files.patch
Patch0134:      0134-Free-NSS-objects-in-external-ca-scenario.patch
Patch0135:      0135-Do-not-lookup-up-the-domain-too-early-if-only-the-SI.patch
Patch0136:      0136-Do-not-store-SID-string-in-a-local-buffer.patch
Patch0137:      0137-Allow-ID-to-SID-mappings-in-the-extdom-plugin.patch
Patch0138:      0138-Allow-user-to-force-Kerberos-realm-during-installati.patch
Patch0139:      0139-sysrestore-copy-files-instead-of-moving-them-to-avoi.patch
Patch0140:      0140-webui-add-Kerberos-configuration-instructions-for-Ch.patch
Patch0141:      0141-Remove-ico-files-from-Makefile.patch
Patch0142:      0142-ACI-plugin-correctly-parse-bind-rules-enclosed-in-pa.patch
Patch0143:      0143-Simplify-adding-options-in-ipachangeconf.patch
Patch0144:      0144-Remove-50-lockout-policy.update-file.patch
Patch0145:      0145-ipachangeconf-Add-ability-to-preserve-section-case.patch
Patch0146:      0146-ipa-client-automount-Leverage-IPAChangeConf-to-confi.patch
Patch0147:      0147-Skip-time-sync-during-client-install-when-using-no-n.patch
Patch0148:      0148-add-DS-index-for-userCertificate-attribute.patch
Patch0149:      0149-webui-use-manual-Firefox-configuration-for-Firefox-4.patch
Patch0150:      0150-cert-revoke-fix-permission-check-bypass.patch
Patch0151:      0151-Modififed-NSSConnection-not-to-shutdown-existing-dat.patch
Patch0152:      0152-Do-not-erroneously-reinit-NSS-in-Dogtag-interface.patch
Patch0153:      0153-Make-sure-replication-works-after-DM-password-is-cha.patch

Patch1001:      1001-hide-pkinit.patch
Patch1002:      1002-remove-pkinit.patch
Patch1003:      1003-ipa-RHEL-index.patch
Patch1004:      1004-ipa-remove-pkinit-man.patch
Patch1005:      1005-ipa-remove-entitlement.patch
Patch1006:      1006-ipa-uibranding.patch
Patch1007:      1007-ipa-remove-entitlement-update.patch
Patch1008:      1008-ipa_memcached-no-status-check.patch
Patch1009:      1009-Revert-Check-direct-reverse-hostname-address-resolut.patch
Patch1010:      1010-Revert-back-to-acutil.patch
Patch1011:      1011-xmlrpc_response.patch
Patch1012:      1012-Revert-global-catalog-code-back-to-acutil.patch
Patch1013:      1013-Check-to-see-if-port-443-is-available.-If-not-raise-.patch
Patch1014:      1014-Do-not-allow-installation-in-FIPS-mode.patch
Patch1015:      1015-Return-proper-error-if-autodiscovery-fails-on-AD-ser.patch
Patch1016:      1016-webui-fix-XSS-vulnerability-in-dialog-header.patch
Patch1017:      1017-ipa-client-install-adds-extra-sss-to-sudoers-in-nssw.patch
Patch1018:      1018-Properly-check-SANs-in-CSRs-generated-by-certmonger.patch
Patch1019:      1019-WebUI-fix-ipa_error.css.patch
Patch1020:      1020-webui-fix-browser-detection-in-browserconfig.html-an.patch

Patch1030:      1030-ipaserver-dcerpc-Ensure-LSA-pipe-has-session-key-bef.patch
Patch1031:      1031-Support-Samba-PASSDB-0.2.0-aka-interface-version-24.patch

Patch9999:     ipa-centos-branding.patch

%if ! %{ONLY_CLIENT}
BuildRequires:  389-ds-base-devel >= 1.2.11.15-22
BuildRequires:  svrcore-devel
BuildRequires:  /usr/share/selinux/devel/Makefile
BuildRequires:  policycoreutils >= %{POLICYCOREUTILSVER}
%endif
BuildRequires:  samba4-devel >= 4.2.10-1
BuildRequires:  samba4-python
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  openssl-devel
BuildRequires:  openldap-devel
BuildRequires:  krb5-devel >= 1.10
BuildRequires:  krb5-workstation
BuildRequires:  libuuid-devel
BuildRequires:  xmlrpc-c-devel >= 1.16.24-1200.1840.el6_1.4
BuildRequires:  libcurl-devel >= 7.19.7-26
BuildRequires:  popt-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  authconfig
BuildRequires:  python-ldap
BuildRequires:  python-setuptools
BuildRequires:  python-krbV
BuildRequires:  python-nss
BuildRequires:  python-netaddr
BuildRequires:  python-kerberos
BuildRequires:  pyOpenSSL
BuildRequires:  libipa_hbac-python
BuildRequires:  python-memcached
BuildRequires:  sssd >= 1.9.2
BuildRequires:  python-lxml
BuildRequires:  python-pyasn1 >= 0.0.9a
BuildRequires:  m2crypto
BuildRequires:  check >= 0.9.5
BuildRequires:  libsss_idmap-devel
BuildRequires:  authconfig

%description
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof).

%if ! %{ONLY_CLIENT}
%package server
Summary: The IPA authentication server
Group: System Environment/Base
Requires: %{name}-python = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Requires: %{name}-admintools = %{version}-%{release}
Requires: %{name}-server-selinux = %{version}-%{release}
Requires: 389-ds-base >= 1.2.11.15-51
Requires: openldap-clients
Requires: nss
Requires: nss-tools
Requires: krb5-server >= 1.10
Requires: krb5-server < 1.11
Requires: cyrus-sasl-gssapi%{?_isa}
Requires: ntp
Requires: httpd >= 2.2.15-24
Requires: mod_wsgi
Requires: mod_auth_kerb >= 5.4-8
Requires: mod_nss >= 1.0.10
Requires: python-ldap
Requires: python-krbV
Requires: acl
Requires: python-pyasn1 >= 0.0.9a
Requires: memcached
Requires: python-memcached >= 1.43-6
Requires: selinux-policy >= 3.7.19-193
Requires(post): selinux-policy-base
Requires: slapi-nis >= 0.40
Requires: pki-ca >= 9.0.3-40
Requires: pki-silent >= 9.0.3-40
Requires: pki-setup >= 9.0.3-40
Requires: ipa-pki-common-theme
Requires: ipa-pki-ca-theme
Requires(preun):  python initscripts chkconfig
Requires(postun): python initscripts chkconfig
Requires: zip
Requires: policycoreutils >= %{POLICYCOREUTILSVER}
Requires: openssh-clients
Requires(pre): certmonger >= 0.61-3
Requires(pre): pki-ca >= 9.0.3-40
Requires(pre): selinux-policy >= 3.7.19-193

# We have a soft-requires on bind. It is an optional part of
# IPA but if it is configured we need a way to require versions
# that work for us.
Conflicts: bind-dyndb-ldap < 2.3-2
Conflicts: bind < 9.8.2-0.10.rc1.el6_3.2

%description server
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). If you are installing an IPA server you need
to install this package (in other words, most people should NOT install
this package).

%package server-selinux
Summary: SELinux rules for ipa-server daemons
Group: System Environment/Base
Requires(post): %{name}-server = %{version}-%{release}
Requires(postun): %{name}-server = %{version}-%{release}
Requires(pre): policycoreutils >= %{POLICYCOREUTILSVER}

%description server-selinux
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). This package provides SELinux rules for the
daemons included in ipa-server

%package server-trust-ad
Summary: Virtual package to install packages required for Active Directory trusts
Group: System Environment/Base
Requires: %{name}-server = %version-%release
Requires: m2crypto
Requires: samba4-python
Requires: samba4 >= 4.0.0-31
Requires: libsss_idmap
Requires: samba4-winbind
# We use alternatives to divert winbind_krb5_locator.so plugin to libkrb5
# on the installes where server-trust-ad subpackage is installed because
# IPA AD trusts cannot be used at the same time with the locator plugin
# since Winbindd will be configured in a different mode
Requires(post): %{_sbindir}/update-alternatives
Requires(post): python
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives
%{?filter_setup:
%filter_from_requires /libwbclient.so.0()/d; /libwbclient.so.0$/d;
%filter_setup
}

%description server-trust-ad
Cross-realm trusts with Active Directory in IPA require working Samba 4 installation.
This package is provided for convenience to install all required dependencies at once.
%endif # ONLY_CLIENT


%package client
Summary: IPA authentication for use on clients
Group: System Environment/Base
Requires: %{name}-python = %{version}-%{release}
Requires: python-ldap
Requires: cyrus-sasl-gssapi%{?_isa}
Requires: ntp
Requires: krb5-workstation
Requires: authconfig
Requires: pam_krb5
Requires: wget
Requires: xmlrpc-c >= 1.16.24-1200.1840.el6_1.4
Requires: sssd >= 1.11.6
# Note that certmonger is (pre) in server subpackage
Requires: certmonger >= 0.61-3
Requires: nss-tools
Requires: bind-utils
Requires: oddjob-mkhomedir
Requires: python-krbV
Requires: libsss_autofs
Requires: autofs
Requires: nfs-utils
Requires(post): policycoreutils

# ipa-client was a separate package in RHEL 6.0. We need to make sure it
# gets completely removed when upgrading.
Obsoletes: ipa-client <= 2.0-9.el6
Obsoletes: ipa-client-debuginfo <= 2.0-9.el6

%description client
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). If your network uses IPA for authentication,
this package should be installed on every client machine.


%package admintools
Summary: IPA administrative tools
Group: System Environment/Base
Requires: %{name}-python = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Requires: python-krbV
Requires: python-ldap

%description admintools
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). This package provides command-line tools for
IPA administrators.

%package python
Summary: Python libraries used by IPA
Group: System Environment/Libraries
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
Requires: python-kerberos >= 1.1-3
%endif
Requires: authconfig
Requires: gnupg
Requires: iproute
Requires: keyutils
Requires: pyOpenSSL
Requires: python-nss >= 0.16
Requires: python-lxml
Requires: python-netaddr
Requires: libipa_hbac-python

%description python
IPA is an integrated solution to provide centrally managed Identity (machine,
user, virtual machines, groups, authentication credentials), Policy
(configuration settings, access control information) and Audit (events,
logs, analysis thereof). If you are using IPA you need to install this
package.

%prep
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build, where "Level"
# is the patch prefix option (e.g. -p1)
# Taken from specfile for sssd and python-simplejson
UpdateTimestamps() {
  Level=$1
  PatchFile=$2

  # Locate the affected files:
  for f in $(diffstat $Level -l $PatchFile); do
    # Set the files to have the same timestamp as that of the patch:
    touch -r $PatchFile $f
  done
}
%setup -n freeipa-%{VERSION} -q

for p in %patches ; do
    %__patch -p1 -i $p
    UpdateTimestamps -p1 $p
done

%build
export CFLAGS="$CFLAGS %{optflags}"
export CPPFLAGS="$CPPFLAGS %{optflags}"
make version-update
cd ipa-client; ../autogen.sh --prefix=%{_usr} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libdir=%{_libdir} --mandir=%{_mandir}; cd ..
%if ! %{ONLY_CLIENT}
cd daemons; ../autogen.sh --prefix=%{_usr} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libdir=%{_libdir} --mandir=%{_mandir} --with-openldap; cd ..
cd install; ../autogen.sh --prefix=%{_usr} --sysconfdir=%{_sysconfdir} --localstatedir=%{_localstatedir} --libdir=%{_libdir} --mandir=%{_mandir}; cd ..
%endif # ONLY_CLIENT

%if ! %{ONLY_CLIENT}
make IPA_VERSION_IS_GIT_SNAPSHOT=no %{?_smp_mflags} all
cd selinux
# This isn't multi-process make capable yet
make all
%else
make IPA_VERSION_IS_GIT_SNAPSHOT=no %{?_smp_mflags} client
%endif

%install
rm -rf %{buildroot}
%if ! %{ONLY_CLIENT}
make install DESTDIR=%{buildroot}
cd selinux
make install DESTDIR=%{buildroot}
cd ..
cp %SOURCE1 %{buildroot}%{_usr}/share/ipa/ui/images
rm %{buildroot}%{_usr}/share/ipa/ui/images/ipa-banner.png
%else
make client-install DESTDIR=%{buildroot}
%endif
%find_lang %{gettext_domain}


%if ! %{ONLY_CLIENT}
# Remove .la files from libtool - we don't want to package
# these files
rm %{buildroot}/%{plugin_dir}/libipa_pwd_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_enrollment_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_winsync.la
rm %{buildroot}/%{plugin_dir}/libipa_repl_version.la
rm %{buildroot}/%{plugin_dir}/libipa_uuid.la
rm %{buildroot}/%{plugin_dir}/libipa_modrdn.la
rm %{buildroot}/%{plugin_dir}/libipa_lockout.la
rm %{buildroot}/%{plugin_dir}/libipa_cldap.la
rm %{buildroot}/%{plugin_dir}/libipa_sidgen.la
rm %{buildroot}/%{plugin_dir}/libipa_sidgen_task.la
rm %{buildroot}/%{plugin_dir}/libipa_extdom_extop.la
rm %{buildroot}/%{plugin_dir}/libipa_range_check.la
rm %{buildroot}/%{_libdir}/krb5/plugins/kdb/ipadb.la
rm %{buildroot}/%{_libdir}/samba/pdb/ipasam.la

# Some user-modifiable HTML files are provided. Move these to /etc
# and link back.
mkdir -p %{buildroot}/%{_sysconfdir}/ipa/html
mkdir -p %{buildroot}/%{_localstatedir}/cache/ipa/sysrestore
mkdir -p %{buildroot}/%{_localstatedir}/cache/ipa/sysupgrade
mkdir %{buildroot}%{_usr}/share/ipa/html/
ln -s ../../../..%{_sysconfdir}/ipa/html/ffconfig.js \
    %{buildroot}%{_usr}/share/ipa/html/ffconfig.js
ln -s ../../../..%{_sysconfdir}/ipa/html/ffconfig_page.js \
    %{buildroot}%{_usr}/share/ipa/html/ffconfig_page.js
ln -s ../../../..%{_sysconfdir}/ipa/html/ssbrowser.html \
    %{buildroot}%{_usr}/share/ipa/html/ssbrowser.html
ln -s ../../../..%{_sysconfdir}/ipa/html/unauthorized.html \
    %{buildroot}%{_usr}/share/ipa/html/unauthorized.html
ln -s ../../../..%{_sysconfdir}/ipa/html/browserconfig.html \
    %{buildroot}%{_usr}/share/ipa/html/browserconfig.html
ln -s ../../../..%{_sysconfdir}/ipa/html/ipa_error.css \
    %{buildroot}%{_usr}/share/ipa/html/ipa_error.css

# So we can own our Apache configuration
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa.conf
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
/bin/touch %{buildroot}%{_sysconfdir}/httpd/conf.d/ipa-pki-proxy.conf
mkdir -p %{buildroot}%{_usr}/share/ipa/html/
/bin/touch %{buildroot}%{_usr}/share/ipa/html/ca.crt
/bin/touch %{buildroot}%{_usr}/share/ipa/html/configure.jar
/bin/touch %{buildroot}%{_usr}/share/ipa/html/kerberosauth.xpi
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb.con
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb.js
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krb5.ini
/bin/touch %{buildroot}%{_usr}/share/ipa/html/krbrealm.con
/bin/touch %{buildroot}%{_usr}/share/ipa/html/preferences.html
mkdir -p %{buildroot}%{_initrddir}
mkdir %{buildroot}%{_sysconfdir}/sysconfig/
install -m 644 init/ipa_memcached.conf %{buildroot}%{_sysconfdir}/sysconfig/ipa_memcached
install -m755 init/SystemV/ipa.init %{buildroot}%{_initrddir}/ipa
install -m755 init/SystemV/ipa_memcached.init %{buildroot}%{_initrddir}/ipa_memcached
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0700 %{buildroot}%{_localstatedir}/run/ipa_memcached/

mkdir -p %{buildroot}%{_libdir}/krb5/plugins/libkrb5
touch %{buildroot}%{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so

(cd %{buildroot}/%{python_sitelib}/ipaserver && find . -type f  | \
        grep -v dcerpc | grep -v adtrustinstance | \
        sed -e 's,\.py.*$,.*,g' | sort -u | \
        sed -e 's,\./,%%{python_sitelib}/ipaserver/,g' ) >server-python.list
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ipa/
/bin/touch %{buildroot}%{_sysconfdir}/ipa/default.conf
/bin/touch %{buildroot}%{_sysconfdir}/ipa/ca.crt
mkdir -p %{buildroot}/%{_localstatedir}/lib/ipa-client/sysrestore

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 contrib/completion/ipa.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/ipa

%if %{ONLY_CLIENT}
# Manually do the installation for the admintools files as upstream doesn't
# install these with the install client target.
mkdir -p %{buildroot}%{_bindir}
install -pm 755 ipa %{buildroot}%{_bindir}
gzip ipa.1
install -pm 644 ipa.1.gz %{buildroot}%{_mandir}/man1
%endif

%clean
rm -rf %{buildroot}

%if ! %{ONLY_CLIENT}
%post server
if [ $1 = 1 ]; then
    /sbin/chkconfig --add ipa
fi
if [ $1 -gt 1 ] ; then
    /sbin/service certmonger condrestart 2>&1 > /dev/null
    /usr/sbin/ipa-upgradeconfig --quiet >/dev/null || :
fi

%posttrans server
# This must be run in posttrans so that updates from previous
# execution that may no longer be shipped are not applied.
/usr/sbin/ipa-ldap-updater --upgrade >/dev/null 2>&1 || :

%preun server
if [ $1 = 0 ]; then
    /sbin/chkconfig --del ipa
    /sbin/service ipa stop >/dev/null 2>&1 || :
fi

%postun server
if [ "$1" -ge "1" ]; then
    /sbin/service ipa condrestart >/dev/null 2>&1 || :
fi

%pre server
# Stop ipa_kpasswd if it exists before upgrading so we don't have a
# zombie process when we're done.
if [ -e /usr/sbin/ipa_kpasswd ]; then
    /sbin/service ipa_kpasswd stop >/dev/null 2>&1 || :
fi

%pre server-selinux
if [ -s /etc/selinux/config ]; then
       . %{_sysconfdir}/selinux/config
       FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
       if [ "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT} ]; then \
               cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}
       fi
fi

%post server-selinux
semodule -s targeted -i /usr/share/selinux/targeted/ipa_httpd.pp /usr/share/selinux/targeted/ipa_dogtag.pp
. %{_sysconfdir}/selinux/config
FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
selinuxenabled
if [ $? == 0  -a "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT}.%{name} ]; then
       fixfiles -C ${FILE_CONTEXT}.%{name} restore
       rm -f ${FILE_CONTEXT}.%name
fi

%preun server-selinux
if [ $1 = 0 ]; then
if [ -s /etc/selinux/config ]; then
       . %{_sysconfdir}/selinux/config
       FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
       if [ "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT} ]; then \
               cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}
       fi
fi
fi

%postun server-selinux
if [ $1 = 0 ]; then
semodule -s targeted -r ipa_httpd ipa_dogtag
. %{_sysconfdir}/selinux/config
FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
selinuxenabled
if [ $? == 0  -a "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT}.%{name} ]; then
       fixfiles -C ${FILE_CONTEXT}.%{name} restore
       rm -f ${FILE_CONTEXT}.%name
fi
fi

%postun server-trust-ad
if [ "$1" -ge "1" ]; then
	if [ "`readlink %{_sysconfdir}/alternatives/winbind_krb5_locator.so`" == "/dev/null" ]; then
		%{_sbindir}/alternatives --set winbind_krb5_locator.so /dev/null
	fi
fi

%post server-trust-ad
%{_sbindir}/update-alternatives --install %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so \
				winbind_krb5_locator.so /dev/null 90
python -c "import sys; from ipaserver.install import installutils; sys.exit(0 if installutils.is_ipa_configured() else 1);" > /dev/null 2>&1
if [  $? -eq 0 ]; then
    /sbin/service httpd condrestart >/dev/null 2>&1 || :
fi

%preun server-trust-ad
if [ $1 -eq 0 ]; then
	%{_sbindir}/update-alternatives --remove winbind_krb5_locator.so /dev/null
fi
%endif # ONLY_CLIENT

%post client
if [ $1 -gt 1 ] ; then
    # Has the client been configured?
    restore=0
    test -f '/var/lib/ipa-client/sysrestore/sysrestore.index' && restore=$(wc -l '/var/lib/ipa-client/sysrestore/sysrestore.index' | awk '{print $1}')

    if [ -f '/etc/sssd/sssd.conf' -a $restore -ge 2 ]; then
        if ! egrep -q '/var/lib/sss/pubconf/krb5.include.d/' /etc/krb5.conf  2>/dev/null ; then
            echo "includedir /var/lib/sss/pubconf/krb5.include.d/" > /etc/krb5.conf.ipanew
            cat /etc/krb5.conf >> /etc/krb5.conf.ipanew
            mv -Z /etc/krb5.conf.ipanew /etc/krb5.conf
            /sbin/restorecon /etc/krb5.conf
        fi
    fi
fi

%if ! %{ONLY_CLIENT}
%files server -f server-python.list
%defattr(-,root,root,-)
%doc COPYING README Contributors.txt
%{_sbindir}/ipa-ca-install
%{_sbindir}/ipa-dns-install
%{_sbindir}/ipa-server-install
%{_sbindir}/ipa-replica-conncheck
%{_sbindir}/ipa-replica-install
%{_sbindir}/ipa-replica-prepare
%{_sbindir}/ipa-replica-manage
%{_sbindir}/ipa-csreplica-manage
%{_sbindir}/ipa-server-certinstall
%{_sbindir}/ipa-ldap-updater
%{_sbindir}/ipa-compat-manage
%{_sbindir}/ipa-nis-manage
%{_sbindir}/ipa-managed-entries
%{_sbindir}/ipactl
%{_sbindir}/ipa-upgradeconfig
%{_libexecdir}/certmonger/dogtag-ipa-retrieve-agent-submit
%config(noreplace) %{_sysconfdir}/sysconfig/ipa_memcached
%dir %attr(0700,apache,apache) %{_localstatedir}/run/ipa_memcached/
%attr(755,root,root) %{_initrddir}/ipa
%attr(755,root,root) %{_initrddir}/ipa_memcached
%dir %{python_sitelib}/ipaserver
%dir %{python_sitelib}/ipaserver/install
%dir %{python_sitelib}/ipaserver/install/plugins
%dir %{python_sitelib}/ipaserver/plugins
%dir %{_libdir}/ipa/certmonger
%attr(755,root,root) %{_libdir}/ipa/certmonger/*
%dir %{_usr}/share/ipa
%{_usr}/share/ipa/wsgi.py*
%{_usr}/share/ipa/*.ldif
%{_usr}/share/ipa/*.uldif
%dir %{_usr}/share/ipa/ffextension
%{_usr}/share/ipa/ffextension/bootstrap.js
%{_usr}/share/ipa/ffextension/install.rdf
%{_usr}/share/ipa/ffextension/chrome.manifest
%dir %{_usr}/share/ipa/ffextension/chrome
%dir %{_usr}/share/ipa/ffextension/chrome/content
%{_usr}/share/ipa/ffextension/chrome/content/kerberosauth.js
%{_usr}/share/ipa/ffextension/chrome/content/kerberosauth_overlay.xul
%dir %{_usr}/share/ipa/ffextension/locale
%dir %{_usr}/share/ipa/ffextension/locale/en-US
%{_usr}/share/ipa/ffextension/locale/en-US/kerberosauth.properties
%{_usr}/share/ipa/*.template
%dir %{_usr}/share/ipa/html
%{_usr}/share/ipa/html/ssbrowser.html
%{_usr}/share/ipa/html/browserconfig.html
%{_usr}/share/ipa/html/unauthorized.html
%{_usr}/share/ipa/html/ipa_error.css
%dir %{_usr}/share/ipa/migration
%{_usr}/share/ipa/migration/error.html
%{_usr}/share/ipa/migration/index.html
%{_usr}/share/ipa/migration/invalid.html
%{_usr}/share/ipa/migration/migration.py*
%dir %{_usr}/share/ipa/ui
%{_usr}/share/ipa/ui/index.html
%{_usr}/share/ipa/ui/login.html
%{_usr}/share/ipa/ui/logout.html
%{_usr}/share/ipa/ui/reset_password.html
%{_usr}/share/ipa/ui/*.ico
%{_usr}/share/ipa/ui/*.css
%{_usr}/share/ipa/ui/*.js
%{_usr}/share/ipa/ui/*.eot
%{_usr}/share/ipa/ui/*.svg
%{_usr}/share/ipa/ui/*.ttf
%{_usr}/share/ipa/ui/*.woff
%dir %{_usr}/share/ipa/ui/ext
%config(noreplace) %{_usr}/share/ipa/ui/ext/extension.js
%dir %{_usr}/share/ipa/ui/images
%{_usr}/share/ipa/ui/images/*.png
%{_usr}/share/ipa/ui/images/*.gif
%dir %{_sysconfdir}/ipa
%dir %{_sysconfdir}/ipa/html
%{_usr}/share/ipa/html/ffconfig.js
%{_usr}/share/ipa/html/ffconfig_page.js
%config(noreplace) %{_sysconfdir}/ipa/html/ffconfig.js
%config(noreplace) %{_sysconfdir}/ipa/html/ffconfig_page.js
%config(noreplace) %{_sysconfdir}/ipa/html/ssbrowser.html
%config(noreplace) %{_sysconfdir}/ipa/html/ipa_error.css
%config(noreplace) %{_sysconfdir}/ipa/html/unauthorized.html
%config(noreplace) %{_sysconfdir}/ipa/html/browserconfig.html
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-pki-proxy.conf
%{_usr}/share/ipa/ca_renewal
%{_usr}/share/ipa/ipa.conf
%{_usr}/share/ipa/ipa-rewrite.conf
%{_usr}/share/ipa/ipa-pki-proxy.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_usr}/share/ipa/html/ca.crt
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/configure.jar
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/kerberosauth.xpi
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb.con
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb.js
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krb5.ini
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/krbrealm.con
%ghost %attr(0644,root,apache) %{_usr}/share/ipa/html/preferences.html
%dir %{_usr}/share/ipa/updates/
%{_usr}/share/ipa/updates/*
%attr(755,root,root) %{plugin_dir}/libipa_pwd_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_enrollment_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_winsync.so
%attr(755,root,root) %{plugin_dir}/libipa_repl_version.so
%attr(755,root,root) %{plugin_dir}/libipa_uuid.so
%attr(755,root,root) %{plugin_dir}/libipa_modrdn.so
%attr(755,root,root) %{plugin_dir}/libipa_lockout.so
%attr(755,root,root) %{plugin_dir}/libipa_cldap.so
%attr(755,root,root) %{plugin_dir}/libipa_range_check.so
%dir %{_localstatedir}/lib/ipa
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/sysrestore
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/sysupgrade
%attr(755,root,root) %dir %{_localstatedir}/lib/ipa/pki-ca
%ghost %dir %{_localstatedir}/lib/ipa/pki-ca/publish
%dir %{_localstatedir}/cache/ipa
%attr(700,apache,apache) %dir %{_localstatedir}/cache/ipa/sessions
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/ipadb.so
%{_mandir}/man1/ipa-replica-conncheck.1.gz
%{_mandir}/man1/ipa-replica-install.1.gz
%{_mandir}/man1/ipa-replica-manage.1.gz
%{_mandir}/man1/ipa-csreplica-manage.1.gz
%{_mandir}/man1/ipa-replica-prepare.1.gz
%{_mandir}/man1/ipa-server-certinstall.1.gz
%{_mandir}/man1/ipa-server-install.1.gz
%{_mandir}/man1/ipa-dns-install.1.gz
%{_mandir}/man1/ipa-ca-install.1.gz
%{_mandir}/man1/ipa-compat-manage.1.gz
%{_mandir}/man1/ipa-nis-manage.1.gz
%{_mandir}/man1/ipa-managed-entries.1.gz
%{_mandir}/man1/ipa-ldap-updater.1.gz
%{_mandir}/man8/ipactl.8.gz
%{_mandir}/man8/ipa-upgradeconfig.8.gz

%files server-selinux
%defattr(-,root,root,-)
%doc COPYING README Contributors.txt
%{_usr}/share/selinux/targeted/ipa_httpd.pp
%{_usr}/share/selinux/targeted/ipa_dogtag.pp

%files server-trust-ad
%{_sbindir}/ipa-adtrust-install
%attr(755,root,root) %{plugin_dir}/libipa_extdom_extop.so
%{_usr}/share/ipa/smb.conf.empty
%attr(755,root,root) %{_libdir}/samba/pdb/ipasam.so
%attr(755,root,root) %{plugin_dir}/libipa_sidgen.so
%attr(755,root,root) %{plugin_dir}/libipa_sidgen_task.so
%{_mandir}/man1/ipa-adtrust-install.1.gz
%{python_sitelib}/ipaserver/dcerpc*
%{python_sitelib}/ipaserver/install/adtrustinstance*
%ghost %{_libdir}/krb5/plugins/libkrb5/winbind_krb5_locator.so
%endif # ONLY_CLIENT

%files client
%defattr(-,root,root,-)
%doc COPYING README Contributors.txt
%{_sbindir}/ipa-client-install
%{_sbindir}/ipa-client-automount
%{_sbindir}/ipa-getkeytab
%{_sbindir}/ipa-rmkeytab
%{_sbindir}/ipa-join
%dir %{_usr}/share/ipa
%dir %{_usr}/share/ipa/ipaclient
%dir %{_localstatedir}/lib/ipa-client
%dir %{_localstatedir}/lib/ipa-client/sysrestore
%{_usr}/share/ipa/ipaclient/ipa.cfg
%{_usr}/share/ipa/ipaclient/ipa.js
%dir %{python_sitelib}/ipaclient
%{python_sitelib}/ipaclient/*.py*
%{_mandir}/man1/ipa-getkeytab.1.gz
%{_mandir}/man1/ipa-rmkeytab.1.gz
%{_mandir}/man1/ipa-client-install.1.gz
%{_mandir}/man1/ipa-client-automount.1.gz
%{_mandir}/man1/ipa-join.1.gz
%{_mandir}/man5/default.conf.5.gz

%files admintools
%defattr(-,root,root,-)
%doc COPYING README Contributors.txt
%{_bindir}/ipa
%config %{_sysconfdir}/bash_completion.d
%{_mandir}/man1/ipa.1.gz

%files python -f %{gettext_domain}.lang
%defattr(-,root,root,-)
%doc COPYING README Contributors.txt
%dir %{python_sitelib}/ipapython
%dir %{python_sitelib}/ipapython/platform
%{python_sitelib}/ipapython/*.py*
%{python_sitelib}/ipapython/platform/*.py*
%dir %{python_sitelib}/ipalib
%{python_sitelib}/ipalib/*
%{python_sitearch}/default_encoding_utf8.so
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%{python_sitelib}/ipapython-*.egg-info
%{python_sitelib}/freeipa-*.egg-info
%{python_sitearch}/python_default_encoding-*.egg-info
%endif
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/default.conf
%ghost %attr(0644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/ca.crt

%changelog
* Tue Oct  4 2016 Johnny Hughes <johnny@centos.org> - 3.0.0-50.el6.3
- Added Patch9999 for Branding.

* Tue Aug 30 2016 Jan Cholasta <jcholast@redhat.com> - 3.0.0-50.el6.3
- Resolves: #1369470 IPA Replica-Install from RHEL6 to RHEL7 Fails
  - Modififed NSSConnection not to shutdown existing database.
  - Do not erroneously reinit NSS in Dogtag interface
  - Make sure replication works after DM password is changed

* Mon Aug 22 2016 Jan Cholasta <jcholast@redhat.com> - 3.0.0-50.el6.2
- Resolves: #1351593 CVE-2016-5404 ipa: Insufficient privileges check in
  certificate revocation
  - cert-revoke: fix permission check bypass (CVE-2016-5404)

* Tue Apr 12 2016 Alexander Bokovoy <abokovoy@redhat.com> - 3.0.0-50.el6.1
- Update IPA code to support Samba 4.2
- Related: #1322689

* Thu Jan  7 2016 Jan Cholasta <mbasti@redhat.com> - 3.0.0-50.el6
- Resolves: #1225868 display browser config options that apply to the browser -
  Chrome
  - Remove ico files from Makefile
- Resolves: #1232843 ipa-client-install errors out if client and server time
  are not in sync or unreachable
  - Skip time sync during client install when using --no-ntp
- Resolves: #1288495 Add userCertificate index used in Smart Card
  authentication
  - add DS index for userCertificate attribute
- Resolves: #1293588 JavaScript error in ssbrowser.html - TypeError: Cannot
  read property 'mozilla' of undefined
  - webui: fix browser detection in browserconfig.html and ssbrowser.html
- Resolves: #1296124 Adjust Firefox configuration to new extension signing
  policy
  - webui: use manual Firefox configuration for Firefox >= 40
- Remove binary patching from patch 0140

* Tue Dec 22 2015 Martin Basti <mbasti@redhat.com> - 3.0.0-49.el6
- Resolves: #1127211 ipa-server-install --uninstall produces avc
  - sysrestore: copy files instead of moving them to avoind SELinux issues
  - Use 'mv -Z' in specfile to restore SELinux context
- Resolves: #1222999 ipa aci plugin is not parsing aci's correctly.
  - ACI plugin: correctly parse bind rules enclosed in parentheses
- Resolves: #1225868 display browser config options that apply to the browser -
  Chrome
  - webui: add Kerberos configuration instructions for Chrome
  - Remove ico files from Makefile
  - WebUI: fix ipa_error.css
- Resolves: #1232468 The Domain option is not correctly set in idmapd.conf when
  ipa-client-automount is executed.
  - Simplify adding options in ipachangeconf
  - ipachangeconf: Add ability to preserve section case
  - ipa-client-automount: Leverage IPAChangeConf to configure the domain for
    idmapd
- Resolves: #1232899 ipa-client-install does not respect --realm option
  - Allow user to force Kerberos realm during installation.
- Resolves: #1276358 Remove /usr/share/ipa/updates/50-lockout-policy.update
  file from IPA 3.0 releases
  - Remove 50-lockout-policy.update file

* Thu Nov 12 2015 Jan Cholasta <jcholast@redhat.com> - 3.0.0-48.el6
- Resolves: #1263703 ipa-server-install with externally signed CA fails with
  NSS error (SEC_ERROR_BUSY)
  - Free NSS objects in --external-ca scenario
- Resolves: #1263262 Unable to resolve group memberships for AD users when
  using sssd-1.12.2-58.el7_1.6.x86_64 client in combination with
  ipa-server-3.0.0-42.el6.x86_64 with AD Trust
  - Do not lookup up the domain too early if only the SID is known
  - Do not store SID string in a local buffer
  - Allow ID-to-SID mappings in the extdom plugin

* Wed May 13 2015 Petr Vobornik <pvoborni@redhat.com> - 3.0.0-47.el6
- Resolves: #1220788 - Some IPA schema files are not RFC 4512 compliant

* Tue Apr 07 2015 Petr Vobornik <pvoborni@redhat.com> - 3.0.0-46.el6
- Use tls version range in NSSHTTPS initialization
- Resolves: #1154687 - POODLE: force using safe ciphers (non-SSLv3) in IPA
                       client and server
- Resolves: #1012224 - host certificate not issued to client during
                       ipa-client-install

* Wed Mar 25 2015 Petr Vobornik <pvoborni@redhat.com> - 3.0.0-45.el6
- Resolves: #1205660 -  ipa-client rpm should require keyutils

* Tue Mar 24 2015 Petr Vobornik <pvoborni@redhat.com> - 3.0.0-44.el6
- Release 3.0.0-44
- Resolves: #1201454 - ipa breaks sshd config

* Fri Feb 27 2015 Petr Vobornik <pvoborni@redhat.com> - 3.0.0-43.el6
- Release 3.0.0-43
- Resolves: #1191040 - ipa-client-automount: failing with error LDAP server
                       returned UNWILLING_TO_PERFORM. This likely means that
                       minssf is enabled.
- Resolves: #1185207 - ipa-client dont end new line character in
                       /etc/nsswitch.conf
- Resolves: #1166241 - CVE-2010-5312 CVE-2012-6662 ipa: various flaws
- Resolves: #1161722 - IDM client registration failure in a high load
                       environment
- Resolves: #1154687 - POODLE: force using safe ciphers (non-SSLv3) in IPA
                       client and server
- Resolves: #1146870 - ipa-client-install fails with "KerbTransport instance
                       has no attribute '__conn'" traceback
- Resolves: #1132261 - ipa-client-install failing produces a traceback
                       instead of useful error message
- Resolves: #1131571 - Do not allow IdM server/replica/client installation
                       in a FIPS-140 mode
- Resolves: #1198160 - /usr/sbin/ipa-server-install --uninstall does not
                       clean /var/lib/ipa/pki-ca
- Resolves: #1198339 - ipa-client-install adds extra sss to sudoers in
                       nsswitch.conf
- Require: 389-ds-base >= 1.2.11.15-51
- Require: mod_nss >= 1.0.10
- Require: pki-ca >= 9.0.3-40
- Require: python-nss >= 0.16

* Fri Jul  4 2014 Martin Kosek <mkosek@redhat.com> - 3.0.0-42.el6
- Require 389-ds-base >= 1.2.11.15-38 to fix roken dereference control with
  the FreeIPA 4.0 ACIs (#1112698)

* Tue Jun 24 2014 Martin Kosek <mkosek@redhat.com> - 3.0.0-41.el6
- ipasam does not support deleting multiple child trusted domains due
  to LDAP delete operation (#1110664)
- Excessive LDAP calls by ipa-sam during file operations to samba file
  share on freeipa master cause high CPU and slow performance (#1074314)

* Thu Jun 19 2014 Martin Kosek <mkosek@redhat.com> - 3.0.0-40.el6
- Explicitly specify auth mechanism when calling ldapmodify in
  the installers (#1108661)
- Add support for DNS classless reverse domains (#1095250)
- Multiple nsDS5ReplicaId attributes created in
  cn=replication,cn=etc (#1109050)
- ipa-client-install should configure sudo automatically (#1111121)

* Fri Jun 13 2014 Martin Kosek <mkosek@redhat.com> - 3.0.0-39.el6
- Rebuild package to fix a brew tag

* Fri Jun 13 2014 Martin Kosek <mkosek@redhat.com> - 3.0.0-38.el6
- ipa-server-install intermittently crashed with "Unable to find
  preop.pin" (#905064)
- Disabled sudo rules were still active in the sudoers tree (#1022199)
- Replica installation fails if forward zone is not present (#1034478)
- Administrative password change did not respect user password
  policy (#1029921)
- Re-initializing a winsync connection exits with "Can't contact
  LDAP server" (#1016042)
- Server checked for unknown attributes before "ipa" tool version
  check (#1015481)
- CA subsystem certificate renewal was broken on CA clones (#1040009)
- Lockout plugin worked inconsistently compared to KDC lockout
  mechanism. Also, default user policy may not have been applied if
  krbPwdPolicyReference was missing (#1088772)
- ipa-client-automount was not backwards compatible (#1082590)
- Increase service timeout from 120s to 300s as some services are
  known to start for more than 120s (#1060639)
- Proxy calls to /ca/ee/ca/profileSubmit to PKI to enable installation
  of replicas with Dogtag 10 PKI (#1083878)

* Mon Sep 30 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-37.el6
- group-add-member command reported wrong error on duplicates (#970541)
- ipa-client installation succeeding in ipa server instance (#1011044)

* Tue Sep 17 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-36.el6
- ipa-join failed when doing a forced host re-enrollment (#924009)

* Mon Sep  9 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-35.el6
- ipa-replica-manage del always exits with error (#1005448)

* Thu Sep  5 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-34.el6
- Host and Hostgroup commands were broken after upgrade (#1001810)

* Mon Aug  5 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-33.el6
- Fix coverity issue in AD 2012 stabilization patch fixing
  memleaks (#980409)

* Mon Aug  5 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-32.el6
- Fix coverity issue in AD 2012 support patch and add 2 related
  stabilization patches (#980409)

* Fri Aug  2 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-31.el6
- Require 389-ds-base >= 1.2.11.15-14 to pick up fix for CVE-2013-1897
  (#928162)
- Password policy lockout plugin does not work as expected (#907881
- Remove deprecated support of the HBAC source host (#924542)
- ipa-client-install may not obtain CA certificate (#924004)
- Allow client to re-enroll without first unenrolling (#924009)
- Enrolling a host into may take two attempts (#950014)
- Add userClass attribute for host objects (#955698)
- Inconsistent replies from FreeIPA to Netlogon ping queries (#967870)
- Performance improvement for IPA CLI and UI user and group related
  plugins (#970541)
- Do not create /var/lib/ipa/pki-ca/publish, retain reference as
  ghost (#975431)
- Add support for AD 2012 trusted domains (#980409)
- XML-RPC server may return a wrong Content-Type (#976716)
- Add missing openssh-clients Requires to ipa-server package (#983463)
- Add an option to edit "Gecos" field from Web UI (#986211)

* Fri May 17 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-30.el6
- LDAP upload CA cert sometimes double-encodes the value (#948928)
- wrong trust argument assigned to renewed certs in ipa cert automatic
  renew (#952241)

* Tue Mar 19 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-29.el6
- ipa-client-install fails to autodiscover on LDAP servers with disabled
  anonymous access (#922843)

* Wed Feb 27 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-28.el6
- ipa-adtrust-install and ipa-replica-conncheck may not parse krb5.conf
  correctly and crash (#916209)

* Wed Feb 27 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-27.el6
- Missing LDAP schema attributeType and objectClass after upgrade (#915745)

* Thu Feb  7 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-26.el6
- Significant decrease in migration performance. (#904119)
- ipa-client-install failed to fall over to replica with master down (#905626)
- During Migration - If Schema is unavailable migration fails (#906846)

* Tue Jan 29 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-25.el6
- Filter generated winbind dependencies so the right version of samba
  can be installed. (#905594)

* Thu Jan 24 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-24.el6
- Add certmonger condrestart to server post scriptlet (#903758)
- Make certmonger a (pre) Requires (#903758)
- Add selinux-policy to Requires(pre) to avoid post scriptlet AVCs
  (#903758)
- Set minimum version of pki-ca to 9.0.3-30 and add to Requires(pre)
  to pick up certmonger upgrade fix (#902474)
- Update anonymous access ACI to protect secret attributes (#902481)

* Mon Jan 21 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-23.el6
- Installer should not connect to 127.0.0.1. (#895561)
- Don't initialize NSS if we don't have to. (#878220)

* Tue Jan 15 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-22.el6
- Set minimum version of bind-dyndb-ldap to 2.3-2 to pick up missing DNS
  zone SOA serial fix (#894131)
- Stopped named service crashed ipa-upgradeconfig program (#895298)
- ipa-replica-prepare crashed when manipulating DNS zone without SOA
  serial (#894143)
- Use new certmonger locking to prevent NSS database corruption during
  CA subsystem renewal (#883484)
- Set minimum selinux-policy to 3.7.19-193 to allow certmonger to talk
  to dbus in an rpm scriptlet. (related #883484)
- Set minimum vresion of certmonger to 0.61-3 for new locking scheme
  (related #883484)

* Fri Jan 11 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-21.el6
- Properly handle migrated uniqueMember attributes (#894090)
- ipa permission-find using valid targetgroup throws internal error (#893827)
- Fix migration of CRLs to new directory location (#893722)
- Installing IPA with a single realm component sometimes fails (#893187)

* Tue Jan  8 2013 Rob Crittenden <rcritten@redhat.com> - 3.0.0-20.el6
- Set maxbersize to a large value to accomondate large CRLs during replica
  installation. (#888956)
- Set minimum version of pki-ca, pki-slient and pki-setup to 9.0.3-29 to
  pick up default CA validity period of 20 years. (#891980)

* Wed Jan  2 2013 Martin Kosek <mkosek@redhat.com> - 3.0.0-19.el6
- Client installation crashes when Kerberos SRV record is not found (#889583)
- Fix typo in patch 0048 for CVE-2012-5484 (#878220)

* Thu Dec 20 2012 Martin Kosek <mkosek@redhat.com> - 3.0.0-18.el6
- Cookie Expires date should be locale insensitive to avoid CLI errors (#888915)

* Wed Dec 19 2012 Martin Kosek <mkosek@redhat.com> - 3.0.0-17.el6
- ipa delegation-find --group option returns internal error (#888524)
- Add missing Requires for python-crypto replacement (#878969)

* Tue Dec 18 2012 Martin Kosek <mkosek@redhat.com> - 3.0.0-16.el6
- sssd is not enabled on client/server install (#888124)

* Fri Dec 14 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-15.el6
- ipa-server-install --uninstall doesn't clear certmonger dirs, which leads
  to install failing (#817080)

* Thu Dec 13 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-14.el6
- Compliant client side session cookie behavior. CVE-2012-5631.
  (#886371)

* Wed Dec 12 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-13.el6
- Use secure method to retrieve IPA CA during client enrollment.
  CVE-2012-5484 (#878220)
- Reformat patch 0044 so it works with git-am

* Tue Dec 11 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-12.el6
- Include /var/lib/sss/pubconf/krb5.include.d/ for domain-realm mappings
  in krb5.conf (#883166)
- Set minimum selinux-policy >= 3.7.19-184 to allow domains that can read
  sssd_public_t files to also list the directory (#881413)
- Remove dist label from changelog entries.
- Fix timestamp on patched files to avoid multilib warnings

* Fri Dec  6 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-11.el6
- Set Requires on httpd 2.2.15-24, mod_nss to 1.0.8-18 and patch to
  check for existing mod_ssl configuration. These versions allow mod_proxy
  to simultaneously support SSL servers using mod_ssl and mod_proxy (#761574)
- IPA WebUI login for AD Trusted User fails (#875261)
- Add 'disable_last_success' and 'disable_lockout' to the ipa_lockout
  plugin (#824488)

* Tue Dec  4 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-10.el6
- Make default group type POSIX in ui (#880655)
- Write replacement for python-crypto (#878969)
- ipa trust-add prints misleading information about required DNS setting
  (#878485)
- Lookup user SIDs in external groups (#878480)
- Special case NFS related ticket to avoid attaching MS-PACs (#878462)
- IPA users are not available after ipa-server-install because sssd not running
  (#878288)
- Incorrect error message when time difference between AD and IPA is too great
  (#877434)
- Missing option to add SSH Public Key in Web UI after upgrade (#877324)

* Mon Nov 26 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-9.el6
- Update minimum BR and Requires of sssd to 1.9.2-25 (related #870278,
  related #871160, related #878262)
- Replication agreement tools report errors with new single instance CA database
  (#878491)
- If time is moved back on the IPA server, ipasam does not invalidate the
  existing ticket (#866576)

* Fri Nov  9 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-8.el6
- Server installation fails to find A/AAAA record for IPA hostname (#874935)
- Out of range error when listing RUV on host with no agreements (#873726)
- Tighten dependency on krb5-server to limit to 1.10 (#872707)
- Default SELinuxusermaporder needs to mapped with default selinux users list
  (#870053)
- Clarify trust-add help regarding multiple runs against the same domain
  (#869741)
- Improve reliabilityof RA renewal script (#869663)
- Add option to disable DNS forwarding by zone (#869658)
- Update minimum version of bind-dyndb-ldap to 2.3-1 (#869658)
- Improve information on passsync user in man page, command help (#869656)
- Resolve external members from trusted domain via Global Catalog (#869616)
- Process relative nameserver DNS record correctly (#868956)
- ipa-adtrust-install does not reset all information when re-run (#867447)
- Fix potential memory leak in KDB backend (#811989)

* Mon Oct 29 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-7.el6
- Fix type conversion of integers when doing modifications (#870446)
- Set SECURE_NFS to lowercase yes rather than uppercase (#869654)
- Add autofs service to sssd.conf before enabling it (#869649)
- Add strict Requires for policycoreutils to avoid user removing them
  during package lifetime (#869281)
- Make internal rename_s() call compatible with python-ldap-2.3.10 (#867902)
- Update minimum version of bind-dyndb-ldap to 2.2-1.el6 (related #871583)
- Restart httpd after running ipa-adtrust-install (#866966)

* Wed Oct 24 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-6.el6
- Add patch to override xmlrpc request method for session (#786199)
- Bad link to Web UI config page after session is expired (#869279)
- extdom plugin does not handle Posix UID and GID request (#867676)
- ipa-server-install --setup-dns always installs reverse zone (#866978)
- Inform user when ipa-upgradeconfig reports errors (#866977)
- Certificate request fails when CSR has subjectAltnames (#866955)
- ipa-adtrust-install checks for /usr/bin/smbpasswd, which is not
  required (#866572)
- Instructions to uninstall are unclear (#856294)
- Inconsistent service naming in ipa-server-install (#856292)
- Improve instructions to generate certificate in Web UI (#856282)
- /etc/ipa/default.conf is out of date (#855855)
- Time synchronization is disabled in ipa-client-install (#854325)
- ipa-replica-install httpd restart sometimes fails (#845405)
- Improve error messages during ipa-replica-manage del (#835632)
- Always log errors from dogtag (#813401)

* Fri Oct 15 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-5.el6
- Update to upstream 3.0.0 GA release (#827602)
- Add zip dependency, needed for creating unsigned Firefox extensions
- Filter generated winbind dependencies so the right version of samba
  can be installed.
- Remove patch to support python-ldap 2.3.10. Fixed upstream.
- Add directory /var/lib/ipa/pki-ca/publish for CRL published by pki-ca (#864533)
- Add zip dependency, needed for creating unsigned Firefox extensions

* Wed Oct 10 2012 Alexander Bokovoy <abokovoy@redhat.com> - 3.0.0-4.el6
- Make sure server-trust-ad subpackage alternates winbind_krb5_locator.so
  plugin to /dev/null since they cannot be used when trusts are configured
  (related #864889)
- Update BR and Requires of samba4 to 4.0.0-31 to pick up winbind_krb5_locator
  alternatives change. (related #864889)

* Fri Oct  5 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-3.el6
- Update to upstream 3.0.0.rc2 release (#827602)
- Provide new Firefox extension.
- Own /etc/ipa/ca.crt

* Tue Sep 25 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-2.el6
- Remove Requires on krb5-pkinit-openssl as part of disabling pkinit code.
- Add missing subdirectories in site-packages/ipaserver discovered by
  rpmdiff. (#827602)

* Mon Sep 24 2012 Rob Crittenden <rcritten@redhat.com> - 3.0.0-1.el6
- Update to upstream 3.0.0.rc1 release (#827602)
- Update BR and Requires of 389-ds-base to 1.2.11.14
- Update BR and Requires of krb5 to 1.10
- Update BR and Requires of samba4 to 4.0.0-24
- Update BR and Requires of sssd to 1.9.0
- Update Requires on policycoreutils to 2.0.83-19.24
- Update Requires on httpd to httpd-2.2.15-17 to pick up #787247
- Update minimum version of bind-dyndb-ldap to 1.1.0-0.9.b1.el6_3.1
- Update minimum version of bind to 9.8.2-0.10.rc1.el6_3.2
- Sync upstream spec file Requires
- Add patch to support python-ldap 2.3.10

* Fri May 25 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-16.el6
- SSH Tech Preview feature enabled by default (#825321)

* Tue May 22 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-15.el6
- Test for locked users before incrementing failed login counter (#822429)

* Tue May 15 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-14.el6
- Fix host page to display all data when DNS is not configured (#818868)

* Tue May  8 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-13.el6
- Make ipa 2.2 client capable of joining an older server (#817867)

* Mon Apr 30 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-12.el6
- Remove patch 0042 and add revert patch for handling which attributes are
  allowed in a permission. (#783502)
- ipa-client-install sets "KerberosAuthenticate yes" in sshd.conf, breaking
  SSSD auth (#817030)
- pwpolicy_find does not sort by priority in UI (#815799)
- Improve zonemgr validation (#745705)

* Mon Apr 23 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-11.el6
- Make new DNS permission mixed-case (#807361)
- hbactest returns failure when hostgroups are chained (#801769)
- Man Page : Document client IP addressing / FQDN requirements (#768257)
- Login failed attempts counter or locked out status are not displayed (#759501)
- Wrong title and icon in login and logout pages (#814752)

* Wed Apr 18 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-10.el6
- Don't interactively prompt for dnsrecord options provided on the
  command-line options (#790295)
- Validate external hosts added to netgroups (#797256)
- Handle invalid RDN for container in migration (#804807)
- Unable to use permission-mod to rename permission object (#805478)
- Migration: don't append basedn to container if it is included (#807371)
- Raise correct exception when LDAP limits are exceeded (#808042)
- Notify user that password needs to be reset in forms-based login (#811296)
- DNS Resource records: add & delete A & AAAA record does not work in root
  (#811744)
- user-mod --rename with an empty string fails (#811748)
- DNS CNAME record: delete sometimes does not work (#811758)
- Delegation UI does not allow to specify permission (#812110)
- IPA uninstall after upgrade returns some sysrestore.state errors (#812391)
- Improve migration plugin error when 2 groups have identical GID (#813389)

* Tue Apr 10 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-9.el6
- Fix password policy history enforcement (#810900)
- Privilege page should not have choice to list permissions by "indirect
  membership" (#810350)
- ipa-server-install fails when domain name is not resolvable (#809190)
- Identity->DNS->Settings:Forward policy: change check box to radio buttons
  (#808620)
- When adding permissions for a type, attributes that are not allowed are
  listed (#807755)
- user-mod --rename is successful for more than max login characters
  (#807417)
- Can't specify netgroup host, user category to all in Web UI (#807366)
- Permission names cannot contains '<' or '>' (#807304)
- ipa-server-install --uninstall errors out when trying to start dirsrv.
  (#801376)
- Should not be allowed to run host-disable on an IPA Server or
  service-disable on an IPA Server service  (#800119)
- permission with filter or subtree does not allow attr to be specified
  (#783536)
- Netgroups compat plugin not reporting users correctly (#767372)
- certmonger renews server certificates ok but those services need a restart
  (related #766167)
- Set minimum vresion of certmonger to 0.56 (related #766167)
- Set minimum version of slapi-nis to 0.40 (#767372)
- Unable to disable or enable hbacrule with --setattr (#810948)
- When adding a user with --noprivate option gidNumber should be required
  (#805546)
- Fix error when no value is given in --revocation-reason optional argument
  with "ipa cert-revoke" (#808099)
- Set minimum version of bind-dyndb-ldap to 1.1.0-0.5.b1 (related #805814)

* Wed Apr  4 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-8.el6
- Fix ambiguous error msg in automount indirect map creation (#790131)
- Invalid error message attempting to delete config attributes (#791373)
- Enforce single-value attributes (#794746)
- config-mod allowed to add additional certificate subjects bases (#794750)
- Embedded carriage returns in a CSV not handled (#797569)
- WebUI displays "Insufficient access: invalid credentials" when a password
  doesn't meet policy requirements (#802786)
- Tech Preview: SELinux User Mapping (#803821)
- Tech Preview: Add support for central management of the SSH keys (#803822)
- Password Policy Failure Interval Reset is not working. (#804096)
- Set SELinux booleans properly (#806330)
- DNS records in LDAP are publicly accessible (#807361)
- Upgrading replication agreements without nsDS5ReplicatedAttributeList fails
  (#808201)
- IPA Upgrade Web UI failure with internal server error (#809262)
- Do not create private groups for migrated users (#809560)

* Wed Mar 28 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-7.el6
- Remove version requirement from BuildRequires on sssd. (related #736865)

* Wed Mar 28 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-6.el6
- Set minimum version of 389-ds-base to 1.2.10.2-4 (related #803930)
- Only split CSV on client (#797565)
- Search allowed attributes in superior objectclasses (#783502)
- Fix precallback validators in DNS plugin (#804562)
- Fix memleak in KDB backend (#800363)
- Harden raw record processing in DNS plugin (#804572)
- Fix attributes that contain DNs when migrating (#804609)
- Wait for child process to terminate after receiving SIGINT (#754635)
- Avoid deleting DNS zone when a context is reused (#801380)
- Fix default SOA serial format (#805427)
- Set nsslapd-minssf-exclude-rootdse to on so the DSE is always available.
  (#803836)
- Amend permissions for new DNS attributes (related #766073)
- Improve user awareness about dnsconfig (#802864)
- Fix uses of O=REALM instead of the configured certificate subject base.
  (#802912)
- Fix dnsrecord-del interactive mode (#807230)
- Add requires on python-krbV to client subpackage (#807362)
- Tolerate UDP port failures in conncheck (#802860)
- Netgroup nisdomain and hosts validation (#797256)
- Remove Conflicts on mod_ssl (#804605)
- Set minimum version of pki-ca, pki-slient and pki-setup to 9.0.3-24.
  Change location of TOMCAT_LOG to match tomcat6 changes (related #802396)
- Add python-lxml, python-pyasn1 and sssd to BuildRequires
- Set minimum selinux-policy >= 3.7.19-142 to pick up certmonger_t type
  (related #790967)
- netgroup-add and netgroup-mod --nisdomain should not allow commas (#797237)

* Wed Mar 21 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-5.el6
- Set minimum version of pki-ca, pki-silent and pki-setup to 9.0.3-23.
  Either we shell escape or dogtag does, we can't both do it. (#802832)
- Set dbdir in request context after a connection is created (#804128)
- Don't overwrite content by an error message (#803050)
- Don't allow IPA master hosts/services to be disabled (#800119)
- Don't error out on empty option (#798792)
- Populate gidnumber in entries added via winsync (#798352)
- Set subjectKeyIdentifier in SSL certs that IPA issues (#797274)
- Fix escaping and comma-separated value handling (#769491)
- Display certificate serial numbers in both hex and deciaml (#746060)
- Use attribute name/option name when returning errors (#718015)
- DNS forwarder's value can consist of IP address and part (#766073)
- Store DNS global options in LDAP (#766073)
- Move extension.js to subdirectory to suppress rpm warning

* Wed Mar 14 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-4.el6
- Allow removing sudo commands with special characters (#800537)
- Ignore case in yes/no prompts when deleting DNS records (#800483)
- Refresh resolvers after DNS server configuration (#799335)
- Fix nsslapd-anonlimitsdn in cn=config (#798361)
- Handle more exceptions gracefully in ipa-client-install (#797567)
- Fixed checkbox value in table without pkey (#791324)
- Fix exception when removing all values from configuration (#782974)
- Set httpd_manage_ipa SELinux boolean
- Fix mask validator in network validator (#802848)
- Don't shell escape arguments sent to pkisilent (#802832)
- Reorder patches so those that disable unsupported features are applied last
- Rebase disable persistent search patch

* Mon Mar  5 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-3.el6
- Rebase to upstream 2.1.90.rc1 release (#736865)
- Remove dependency on krb5-server-ldap, we use our own backend now (#797564)
- Set minimum mod_auth_kerb to 5.4-8 for S4U2Proxy support (related #767741)
- Set minimum selinux-policy >= 3.7.19-137 to pick up ipa_memcache boolean
- Set minimum python-memcached >= 1.43-6 to pick up status check fix
- Set minimum version of 389-ds-base to 1.2.10.1-1
- Set minimum version of krb5-server to 1.9-27
- Set minimum version of sssd to 1.8.0-11 (#766068)
- Add Requires: oddjob-mkhomedir to ipa-client (#786223)
- Remove Requires on krb5-server-ldap (#797564)
- Add Conflicts on mod_ssl (#761574)
- Remove BuildRequires on python-rhsm
- Renumber all patches
- Don't remove dirsrv user on uninstall (#797566)
- Don't allow host-del on active replicas (#797563)
- Fix invalid hostnames when hostname contains trailing dot (#797562)
- encode Bool attributes used in setattr/addattr/delattr (#797561)
- Migration plugin raises Internal Server Error (#796401)
- man page for ipa-replica-manage has typos in examples (#796347)
- Can not add new user objectclass to ipa configuration (#794474)
- Don't require SELinux to be enabled on client (#790513)
- dnsrecord-add does not validate the record names with space in between (#790318)
- Prompt for missing DNS options (#790295)
- Resource Record type options should be more descriptive (#790017)
- Correction in error message while deleting a invalid record (#789987)
- Adding some of the RR type from the "allowed values" results in an error message (#789980)
- IP address with just 3 octets are accepted as valid addresses (#789919)
- Errors not reported correctly when logging into WebUI (#789459)
- Need option for ipa-client-install to not call authconfig (#789413)
- IPA nested netgroups not seen from ypcat (#788625)
- gid number: 0 and negative number accepted (#786240)
- Allow basedn to be passed into migrate-ds (#786185)
- permission with filter or subtree does not allow attr to be specified (#783536)
- ipa permission-add does not fail if using invalid attribute (#783502)
- When migrating warn user if compat is enabled (#783270)
- Make ipausers a non-posix group on new installs (#773488)
- Need tool to update exclusive list in replication agreements (#772359)
- Reverse DNS rec not created upon creation of fwd DNS rec (#772301)
- Adding a netgroup with a "+" causes ns-slapd to crash (#772043)
- Man Page : Document client IP addressing / FQDN requirements (#768257)
- GSS-TSIG DNS updates should update reverse entries as well (#767725)
- UI for SELinux user mapping (tech preview)
- Allow forms based kerberos authentication (#766070)
- Add support for central management of the SSH keys (tech preview)
- Login failed attempts counter or locked out status are not displayed (#759501)
- Better message for error diagnosis while adding an existing winsync agreement (#755450)
- "force-sync, re-initialize and del" options for ipa-replica-manage fail against AD (#754973)
- Connect after del using ipa-replica-manage fails (#754539)
- Unable to delete migrated groups containing spaces (#753966)
- support bind forward zones, aka DNS conditional forwarding (#753483)
- IPA needs a check to ensure hostnames 'underscore' is not allowed when installing a replica (#752874)
- Unable to select dns zone when only one exists in UI (#751529)
- ipa-replica-conncheck does does not properly check UDP ports (#751063)
- Adding loc records to a ipa-dns server breaks name resolution for some other records (#750947)
- Allow specifying query and transfer policy settings for a zone (#701677)

* Fri Feb 17 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-2.el6
- Add missing changelog information caught by rpmdiff.

* Fri Feb 17 2012 Rob Crittenden <rcritten@redhat.com> - 2.2.0-1.el6
- Update to upstream 2.1.90.pre2 release (#736865)

* Mon Nov  7 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-9.el6
- Add current password prompt when changing own password in web UI (#751179)
- Remove extraneous trailing ' from netgroup patch (#749352)

* Tue Nov  1 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-8.el6
- Updated patch for CVE-2011-3636 to include CR in the HTTP headers.
  xmlrpc-c in RHEL-6 doesn't suppose the dont_advertise option so that is
  not set any more. Another fake header, X-Original-User_Agent, is added
  so there is no more trailing junk after the Referer header.  (#749870)

* Mon Oct 31 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-7.el6
- Require an HTTP Referer header to address CSRF attackes. CVE-2011-3636.
  (#749870)

* Fri Oct 28 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-6.el6
- Users not showing up in nis netgroup triple (#749352)

* Tue Oct 25 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-5.el6
- Add update file to remove entitlement roles, privileges and
  permissions (#739060)

* Tue Oct 25 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-4.el6
- Quote worker option in krb5kdc (#748754)

* Fri Oct 21 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-3.el6
- hbactest fails while you have svcgroup in hbacrule (#746227)
- Add Kerberos domain mapping for system hostname (#747443)
- Format certificates as PEM in browser (#701325)

* Tue Oct 18 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-2.el6
- ipa-client-install hangs if the discovered server is unresponsive (#745392)
- Fix minor problems in help system (#747028)
- Remove help fix from Disable automember patch (#746717)
- Update minimum version of sssd to 1.5.1-60 to pick up SELinux fix (#746265)

* Mon Oct 17 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.3-1.el6
- Update to upstream 2.1.3 release (#736170)
- Additional branding (#742264)
- Disable automember cli (#746717)
- ipa-client-install sometimes fails to start sssd properly (#736954)
- ipa-client-install adds duplicate information to krb5.conf (#714597)
- ipa-client-install should configure hostname (#714919)
- inconsistency in enabling "delete" buttons (#730751)
- hbactest does not resolve canonical names during simulation (#740850)
- Default DNS Administration Role - Permissions missing (#742327)
- named fails to start after installing ipa server when short (#742875)
- Duplicate hostgroup and netgroup should not be allowed (#743253)
- named fails to start (#743680)
- Global password policy should not be able to be deleted (#744074)
- Client install fails when anonymous bind is disabled (#744101)
- Internal Server Error adding invalid reverse DNS zone (#744234)
- ipa hbactest does not evaluate indirect members from groups. (#744410)
- Leaks KDC password and master password via command line arguments (#744422)
- Traceback when upgrading from ipa-server-2.1.1-1 (#744798)
- IPA User's Primary GID is not being set to their UPG's GID (#745552)
- --forwarder option of ipa-dns-install allows invalid IP addr (#745698)
- UI does not grant access based on roles (#745957)
- Unable to add external user for RunAs User for Sudo (#746056)
- Typo in error message while adding invalid ptr record. (#746199)
- Don't use python 2.7-only syntax (#746229)
- Error when using ipa-client-install with --no-sssd option (#746276)
- Installation fails if sssd.conf exists and is already config (#746298)
- External hosts are not removed properly from sudorule (#709665)
- Competely remove entitlement support (#739060)
- Add winsync section to ipa-replica-manage man page (#744306)

* Fri Oct  7 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.2-2.el6
- Remove python-rhsm as a Requires (#739060)

* Fri Oct  7 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.2-1.el6
- Update to upstream 2.1.2 release (#736170)
- More completely disable entitlement support (#739060)
- Drop patch to ignore return value from restorecon (upstreamed)
- Set min version of 389-ds-base to 1.2.9.12-2
- Set min version of dogtag to 9.0.3-20
- Rebased hide-pkinit, ipa-RHEL-index and remove-persistent-search
  patches (#700586)

* Wed Sep 20 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.1-4.el6
- Update RHEL patch (#740094)

* Tue Sep 20 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.1-3.el6
- Ignore return value from restorecon (#739604)
- Disable entitlement support (#739060, #739061)

* Fri Sep 16 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.1-2.el6
- Update minimum xmlrpc-c version (#736787)
- Fix package installation order causing SELinux problems (#737516)

* Thu Sep  1 2011 Rob Crittenden <rcritten@redhat.com> - 2.1.1-1.el6
- Update to upstream 2.1.1 release (#732803)

* Mon Aug 15 2011 John Dennis <jdennis@redhat.com> - 2.1.0-1.el6
- Resolves: rhbz#708388 - Update to upstream 2.1.0 release

* Tue May 31 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-25
- Remove client debug logging patch (#705800)

* Wed May 25 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-24
- Wait for 389-ds tasks to complete (#698421)
- Set replica to restart ipa on boot (#705794)
- Improve client debug logging (#705800)
- Managed Entries not configured on replicas (#703869)
- Don't create bogus aRecord when creating new zone (#704012)

* Wed Apr 20 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-23
- Update ipa-Fix-traceback-in-nis-manage.patch to fix python error (#697583)

* Tue Apr 19 2011 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-22
- Resolves: rhbz#697583 - Can not enable ipa-nis-manage plugin

* Thu Apr 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-21
- Default groups are missing ipaUniqueID attribute (#696508)

* Tue Apr  5 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-20
- Set min version of 389-ds-base to 1.2.8.0-1 for fix in BZ 693466.
- Fix some problems in IPA schema (#692978)
- postalCode should be a string not an integer (#692945)

* Wed Mar 30 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-19
- Port 7390 is managed by selinux-policy-3.7.19-80. Update
  ipa-repl_selinux.patch to not manage it any more. (#691883)
- Patch to fix setting gidnumber when a user is created. (#692168)

* Mon Mar 28 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-18
- Fix uninitialized variable in password plugin (#690595)

* Tue Mar 23 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-17
- Wait for Directory Service ports to open (#688934)
- Mixed case hostname can cause issues and confusion (#688622)
- Wrong timeout parameter in ipapython (#684273)
- Run ipa-ldap-updater on upgrades (#688931)
- Internal Error and trace back when adding DNS AAAA record (#689452)

* Tue Mar 15 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-16
- Use realm provided by installer in LDAP Updater (#684744)
- Use args for domain and server when doing DNS discovery in client (#684780)
- Fix 2 SELinux issues in dogtag replication (#684269)

* Mon Mar 14 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-15
- Add Obsoletes so upgrade from ipa-client package is possible (#684931)

* Thu Mar 10 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-14
- Update to upstream 2.0.0rc3 (#680993)
- Set minimum version of sssd to 1.5.1-12
- Remove SuitespotGroup patch
- Rebase remove-pkinit patch

* Thu Feb 24 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-13
- Set the SuitespotGroup directive in the 389-ds installation template.
  This ensures group read/write to /var/run/dirsrv. (#680201)
- Make single line out of python sitelib/sitearch code.

* Wed Feb 23 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-12
- Update to upstream 2.0.0rc2 (#675282)
- Set minimum version of sssd to 1.5.1-10
- Set minimum version of python-nss to 0.11
- Set minimum version of 389-ds to 1.2.8
- Add bind-utils as Requires in client subpackage
- Remove unused BuildRequires e2fsprogs-devel and libcap-devel
- Add branding patch
- Add default.conf man page
- Upstream moved some utilites from the admintools subpackage, reflect that
  here as well.

* Fri Feb 11 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-11
- Add pyOpenSSL to BuildRequires. (#670954)

* Mon Feb  7 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-10
- ExcludeArch doesn't do per-package exclusions, use ifarch to force
  ONLY_CLIENT on non-supported architectures. (#670954)
- Manually install ipa-admintools since the upstream client-install
  target doesn't.
- Move a lot of the BuildRequires out of the ! ONLY_CLIENT conditional
  because the API validator in the upstream code requires them.

* Mon Feb  7 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-9
- Exclude building server and server-selinux on ppc, ppc64, s390 and s390x
  platforms. (#670954)
- Add date variable to the release to make daily builds easier.

* Tue Feb  1 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-8
- Merge in changes from FreeIPA beta 2 (#670954)
- Add patches to disable pkinit

* Thu Jan 27 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-7
- Set minimum version of dogtag to 9.0.0 and add Requires for
  the theme we need. (#658275)
- Remove unnecessary moving of v1 CA serial number file in post script
- Move some man pages into admintools subpackage

* Mon Jan 24 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-6
- Drop specific Requires on libcurl and krb5-libs (#658275)

* Wed Jan 19 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-5
- Consistent usage of buildroot vs RPM_BUILD_ROOT (#658275)

* Mon Jan 17 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-4
- Drop Requires on nss-ldap (#658275)

* Thu Jan 13 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-3
- Temporarily disable building on s390

* Thu Jan 13 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-2
- Drop optional radius package, the underlying code isn't there
- Re-arrange the doc lines so that defattr is first (#658275)

* Wed Jan 12 2011 Rob Crittenden <rcritten@redhat.com> - 2.0.0-1
- Initial 2.0.0 build (#658275)
- This is IPA v2.0.0 beta 1 plus all patches through git commit
  4da9228fb2ac34adab8eb1884ae414236adb84fa
- Removed some Fedora conditionals

* Wed Jan 12 2011 Rob Crittenden <rcritten@redhat.com> - 1.99-36
- Drop BuildRequires on mozldap-devel

* Mon Dec 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-35
- Add Requires on krb5-pkinit-openssl

* Fri Dec 10 2010 Jr Aquino <jr.aquino@citrix.com> - 1.99-34
- Add ipa-host-net-manage script

* Tue Dec  7 2010 Simo Sorce <ssorce@redhat.com> - 1.99-33
- Add ipa init script

* Fri Nov 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-32
- Set minimum level of 389-ds-base to 1.2.7 for enhanced memberof plugin

* Wed Nov  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-31
- remove ipa-fix-CVE-2008-3274

* Wed Oct  6 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-30
- Remove duplicate %%files entries on share/ipa/static
- Add python default encoding shared library

* Mon Sep 20 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-29
- Drop requires on python-configobj (not used any more)
- Drop ipa-ldap-updater message, upgrades are done differently now

* Wed Sep  8 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-28
- Drop conflicts on mod_nss
- Require nss-pam-ldapd on F-14 or higher instead of nss_ldap (#606847)
- Drop a slew of conditionals on older Fedora releases (< 12)
- Add a few conditionals against RHEL 6
- Add Requires of nss-tools on ipa-client

* Fri Aug 13 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-27
- Set minimum version of certmonger to 0.26 (to pck up #621670)
- Set minimum version of pki-silent to 1.3.4 (adds -key_algorithm)
- Set minimum version of pki-ca to 1.3.6
- Set minimum version of sssd to 1.2.1

* Tue Aug 10 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-26
- Add BuildRequires for authconfig

* Mon Jul 19 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-25
- Bump up minimum version of python-nss to pick up nss_is_initialize() API

* Thu Jun 24 2010 Adam Young <ayoung@redhat.com> - 1.99-24
- Removed python-asset based webui

* Thu Jun 24 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-23
- Change Requires from fedora-ds-base to 389-ds-base
- Set minimum level of 389-ds-base to 1.2.6 for the replication
  version plugin.

* Tue Jun  1 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-22
- Drop Requires of python-krbV on ipa-client

* Mon May 17 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-21
- Load ipa_dogtag.pp in post install

* Mon Apr 26 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-20
- Set minimum level of sssd to 1.1.1 to pull in required hbac fixes.

* Thu Mar  4 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-19
- No need to create /var/log/ipa_error.log since we aren't using
  TurboGears any more.

* Mon Mar 1 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-18
- Fixed share/ipa/wsgi.py so .pyc, .pyo files are included

* Wed Feb 24 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-17
- Added Require mod_wsgi, added share/ipa/wsgi.py

* Thu Feb 11 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-16
- Require python-wehjit >= 0.2.2

* Wed Feb  3 2010 Rob Crittenden <rcritten@redhat.com> - 1.99-15
- Add sssd and certmonger as a Requires on ipa-client

* Wed Jan 27 2010 Jason Gerard DeRose <jderose@redhat.com> - 1.99-14
- Require python-wehjit >= 0.2.0

* Fri Dec  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-13
- Add ipa-rmkeytab tool

* Tue Dec  1 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-12
- Set minimum of python-pyasn1 to 0.0.9a so we have support for the ASN.1
  Any type

* Wed Nov 25 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-11
- Remove v1-style /etc/ipa/ipa.conf, replacing with /etc/ipa/default.conf

* Fri Nov 13 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-10
- Add bash completion script and own /etc/bash_completion.d in case it
  doesn't already exist

* Tue Nov  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-9
- Remove ipa_webgui, its functions rolled into ipa_httpd

* Mon Oct 12 2009 Jason Gerard DeRose <jderose@redhat.com> - 1.99-8
- Removed python-cherrypy from BuildRequires and Requires
- Added Requires python-assets, python-wehjit

* Mon Aug 24 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-7
- Added httpd SELinux policy so CRLs can be read

* Thu May 21 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-6
- Move ipalib to ipa-python subpackage
- Bump minimum version of slapi-nis to 0.15

* Thu May  6 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-5
- Set 0.14 as minimum version for slapi-nis

* Wed Apr 22 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-4
- Add Requires: python-nss to ipa-python sub-package

* Thu Mar  5 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-3
- Remove the IPA DNA plugin, use the DS one

* Wed Mar  4 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-2
- Build radius separately
- Fix a few minor issues

* Tue Feb  3 2009 Rob Crittenden <rcritten@redhat.com> - 1.99-1
- Replace TurboGears requirement with python-cherrypy

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-3
- rebuild with new openssl

* Fri Dec 19 2008 Dan Walsh <dwalsh@redhat.com> - 1.2.1-2
- Fix SELinux code

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-1
- Fix breakage caused by python-kerberos update to 1.1

* Fri Dec 5 2008 Simo Sorce <ssorce@redhat.com> - 1.2.1-0
- New upstream release 1.2.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.0-4
- Rebuild for Python 2.6

* Fri Nov 14 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-3
- Respin after the tarball has been re-released upstream
  New hash is 506c9c92dcaf9f227cba5030e999f177

* Thu Nov 13 2008 Simo Sorce <ssorce@redhat.com> - 1.2.0-2
- Conditionally restart also dirsrv and httpd when upgrading

* Wed Oct 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.2.0-1
- Update to upstream version 1.2.0
- Set fedora-ds-base minimum version to 1.1.3 for winsync header
- Set the minimum version for SELinux policy
- Remove references to Fedora 7

* Wed Jul 23 2008 Simo Sorce <ssorce@redhat.com> - 1.1.0-3
- Fix for CVE-2008-3274
- Fix segfault in ipa-kpasswd in case getifaddrs returns a NULL interface
- Add fix for bug #453185
- Rebuild against openldap libraries, mozldap ones do not work properly
- TurboGears is currently broken in rawhide. Added patch to not build
  the UI locales and removed them from the ipa-server files section.

* Wed Jun 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-2
- Add call to /usr/sbin/upgradeconfig to post install

* Wed Jun 11 2008 Rob Crittenden <rcritten@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0
- Patch for indexing memberof attribute
- Patch for indexing uidnumber and gidnumber
- Patch to change DNA default values for replicas
- Patch to fix uninitialized variable in ipa-getkeytab

* Fri May 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-5
- Set fedora-ds-base minimum version to 1.1.0.1-4 and mod_nss minimum
  version to 1.0.7-4 so we pick up the NSS fixes.
- Add selinux-policy-base(post) to Requires (446496)

* Tue Apr 29 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-4
- Add missing entry for /var/cache/ipa/kpasswd (444624)
- Added patch to fix permissions problems with the Apache NSS database.
- Added patch to fix problem with DNS querying where the query could be
  returned as the answer.
- Fix spec error where patch1 was in the wrong section

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-3
- Added patch to fix problem reported by ldapmodify

* Fri Apr 25 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-2
- Fix Requires for krb5-server that was missing for Fedora versions > 9
- Remove quotes around test for fedora version to package egg-info

* Fri Apr 18 2008 Rob Crittenden <rcritten@redhat.com> - 1.0.0-1
- Update to upstream version 1.0.0

* Tue Mar 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-12
- Pull upstream changelog 722
- Add Conflicts mod_ssl (435360)

* Thu Feb 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-11
- Pull upstream changelog 698
- Fix ownership of /var/log/ipa_error.log during install (435119)
- Add pwpolicy command and man page

* Thu Feb 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-10
- Pull upstream changelog 678
- Add new subpackage, ipa-server-selinux
- Add Requires: authconfig to ipa-python (bz #433747)
- Package i18n files

* Mon Feb 18 2008 Rob Crittenden <rcritten@redhat.com> 0.99-9
- Pull upstream changelog 641
- Require minimum version of krb5-server on F-7 and F-8
- Package some new files

* Thu Jan 31 2008 Rob Crittenden <rcritten@redhat.com> 0.99-8
- Marked with wrong license. IPA is GPLv2.

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-7
- Ensure that /etc/ipa exists before moving user-modifiable html files there
- Put html files into /etc/ipa/html instead of /etc/ipa

* Tue Jan 29 2008 Rob Crittenden <rcritten@redhat.com> 0.99-6
- Pull upstream changelog 608 which renamed several files

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-5
- package the sessions dir /var/cache/ipa/sessions
- Pull upstream changelog 597

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-4
- Updated upstream pull (596) to fix bug in ipa_webgui that was causing the
  UI to not start.

* Thu Jan 24 2008 Rob Crittenden <rcritten@redhat.com> 0.99-3
- Included LICENSE and README in all packages for documentation
- Move user-modifiable content to /etc/ipa and linked back to
  /usr/share/ipa/html
- Changed some references to /usr to the {_usr} macro and /etc
  to {_sysconfdir}
- Added popt-devel to BuildRequires for Fedora 8 and higher and
  popt for Fedora 7
- Package the egg-info for Fedora 9 and higher for ipa-python

* Tue Jan 22 2008 Rob Crittenden <rcritten@redhat.com> 0.99-2
- Added auto* BuildRequires

* Mon Jan 21 2008 Rob Crittenden <rcritten@redhat.com> 0.99-1
- Unified spec file

* Thu Jan 17 2008 Rob Crittenden <rcritten@redhat.com> - 0.6.0-2
- Fixed License in specfile
- Include files from /usr/lib/python*/site-packages/ipaserver

* Fri Dec 21 2007 Karl MacMillan <kmacmill@redhat.com> - 0.6.0-1
- Version bump for release

* Wed Nov 21 2007 Karl MacMillan <kmacmill@mentalrootkit.com> - 0.5.0-1
- Preverse mode on ipa-keytab-util
- Version bump for relase and rpm name change

* Thu Nov 15 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.1-2
- Broke invididual Requires and BuildRequires onto separate lines and
  reordered them
- Added python-tgexpandingformwidget as a dependency
- Require at least fedora-ds-base 1.1

* Thu Nov  1 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.1-1
- Version bump for release

* Wed Oct 31 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-6
- Add dep for freeipa-admintools and acl

* Wed Oct 24 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-5
- Add dependency for python-krbV

* Fri Oct 19 2007 Rob Crittenden <rcritten@redhat.com> - 0.4.0-4
- Require mod_nss-1.0.7-2 for mod_proxy fixes

* Thu Oct 18 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-3
- Convert to autotools-based build

* Tue Sep 25 2007 Karl MacMillan <kmacmill@redhat.com> - 0.4.0-2

* Fri Sep 7 2007 Karl MacMillan <kmacmill@redhat.com> - 0.3.0-1
- Added support for libipa-dna-plugin

* Fri Aug 10 2007 Karl MacMillan <kmacmill@redhat.com> - 0.2.0-1
- Added support for ipa_kpasswd and ipa_pwd_extop

* Mon Aug  5 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-3
- Abstracted client class to work directly or over RPC

* Wed Aug  1 2007 Rob Crittenden <rcritten@redhat.com> - 0.1.0-2
- Add mod_auth_kerb and cyrus-sasl-gssapi to Requires
- Remove references to admin server in ipa-server-setupssl
- Generate a client certificate for the XML-RPC server to connect to LDAP with
- Create a keytab for Apache
- Create an ldif with a test user
- Provide a certmap.conf for doing SSL client authentication

* Fri Jul 27 2007 Karl MacMillan <kmacmill@redhat.com> - 0.1.0-1
- Initial rpm version
