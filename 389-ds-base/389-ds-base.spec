
%global pkgname   dirsrv
# for a pre-release, define the prerel field e.g. .a1 .rc2 - comment out for official release
# also remove the space between % and global - this space is needed because
# fedpkg verrel stupidly ignores comment lines
# % global prerel .rc2
# the source tarball may have a different pre-release tag
%global srcver 1.2.11.15
# % global srcprerel .rc2
# also need the relprefix field for a pre-release e.g. .0 - also comment out for official release
# % global relprefix 0.

%global use_openldap 1
# % global use_db4 0
# If perl-Socket-2.000 or newer is available, set 0 to use_Socket6.
%global use_Socket6 1

# fedora 15 and later uses tmpfiles.d
# otherwise, comment this out
#%{!?with_tmpfiles_d: %global with_tmpfiles_d %{_sysconfdir}/tmpfiles.d}

Summary:          389 Directory Server (base)
Name:             389-ds-base
Version:          1.2.11.15
Release:          %{?relprefix}75%{?prerel}%{?dist}
License:          GPLv2 with exceptions
URL:              http://port389.org/
Group:            System Environment/Daemons
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         %{name}-libs = %{version}-%{release}
# for migration tools
Provides:         ldif2ldbm

ExclusiveArch:    x86_64 %{ix86}
BuildRequires:    nspr-devel
BuildRequires:    nss-devel
BuildRequires:    svrcore-devel
%if %{use_openldap}
BuildRequires:    openldap-devel
%else
BuildRequires:    mozldap-devel
%endif
BuildRequires:    db4-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    icu
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel
# The following are needed to build the snmp ldap-agent
BuildRequires:    net-snmp-devel
%ifnarch sparc sparc64 ppc ppc64 s390 s390x
BuildRequires:    lm_sensors-devel
%endif
BuildRequires:    bzip2-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    tcp_wrappers
# the following is for the pam passthru auth plug-in
BuildRequires:    pam-devel

# this is needed for using semanage from our setup scripts
Requires:         policycoreutils-python

# the following are needed for some of our scripts
%if %{use_openldap}
Requires:         openldap-clients
%else
Requires:         mozldap-tools
%endif
# use_openldap assumes perl-Mozilla-LDAP is built with openldap support
Requires:         perl-Mozilla-LDAP

# this is needed to setup SSL if you are not using the
# administration server package
Requires:         nss-tools

# these are not found by the auto-dependency method
# they are required to support the mandatory LDAP SASL mechs
Requires:         cyrus-sasl-gssapi
Requires:         cyrus-sasl-md5

# this is needed for verify-db.pl
Requires:         db4-utils

# for setup-ds.pl to support ipv6 
%if %{use_Socket6}
Requires:         perl-Socket6
%else
Requires:         perl-Socket
%endif
Requires:         perl-NetAddr-IP

# This picks up libperl.so as a Requires, so we add this versioned one
Requires:         perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# for the init script
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

Source0:          http://port389.org/sources/%{name}-%{srcver}%{?srcprerel}.tar.bz2
Source1:          %{name}-devel.README
Patch0:           0000-Trac-Ticket-340-Change-on-SLAPI_MODRDN_NEWSUPERIOR-i.patch
Patch1:           0001-Ticket-478-passwordTrackUpdateTime-stops-working-wit.patch
Patch2:           0002-Bug-863576-Dirsrv-deadlock-locking-up-IPA.patch
Patch3:           0003-Ticket-446-anonymous-limits-are-being-applied-to-dir.patch
Patch4:           0004-Ticket-481-expand-nested-posix-groups.patch
Patch5:           0005-Ticket-491-multimaster_extop_cleanruv-returns-wrong-.patch
Patch6:           0006-Coverity-defects.patch
Patch7:           0007-Fixing-compiler-warnings-in-the-posix-winsync-plugin.patch
Patch8:           0008-Trac-Ticket-494-slapd-entered-to-infinite-loop-durin.patch
Patch9:           0009-Coverity-defects.patch
Patch10:          0010-Trac-Ticket-498-Cannot-abaondon-simple-paged-result-.patch
Patch11:          0011-Ticket-503-Improve-AD-version-in-winsync-log-message.patch
Patch12:          0012-Trac-Ticket-500-Newly-created-users-with-organizatio.patch
Patch13:          0013-Trac-Ticket-519-Search-with-a-complex-filter-includi.patch
Patch14:          0014-Trac-Ticket-520-RedHat-Directory-Server-crashes-segf.patch
Patch15:          0015-Ticket-517-crash-in-DNA-if-no-dnaMagicRegen-is-speci.patch
Patch16:          0016-Ticket-495-internalModifiersname-not-updated-by-DNA-.patch
Patch17:          0017-Ticket-337-improve-CLEANRUV-functionality.patch
Patch18:          0018-Ticket-526-Coverity-Fixes.patch
Patch19:          0019-Ticket-20-Allow-automember-to-work-on-entries-that-h.patch
Patch20:          0020-Ticket-216-disable-replication-agreements.patch
Patch21:          0021-Ticket-526-Coverity-Issues-for-1.2.11.patch
Patch22:          0022-Ticket-527-ns-slapd-segfaults-if-it-cannot-rename-th.patch
Patch23:          0023-Ticket-541-RootDN-Access-Control-plugin-is-missing-a.patch
Patch24:          0024-Ticket-541-need-to-set-plugin-as-off-in-ldif-templat.patch
Patch25:          0025-Ticket-549-DNA-plugin-no-longer-reports-additional-i.patch
Patch26:          0026-Ticket-495-1.2.11-plugin-dn-is-missing-from-pblock.patch
Patch27:          0027-Ticket-556-Don-t-overwrite-certmap.conf-during-upgra.patch
Patch28:          0028-Ticket-572-PamConfig-schema-not-updated-during-upgra.patch
Patch29:          0029-Bug-906005-Valgrind-reports-memleak-in-modify_update.patch
Patch30:          0030-Ticket-570-DS-returns-error-20-when-replacing-values.patch
Patch31:          0031-Ticket-367-Invalid-chaining-config-triggers-a-disk-f.patch
Patch32:          0032-Ticket-576-DNA-use-event-queue-for-config-update-onl.patch
Patch33:          0033-Ticket-579-Error-messages-encountered-when-using-POS.patch
Patch34:          0034-Ticket-518-dse.ldif-is-0-length-after-server-kill-or.patch
Patch35:          0035-Ticket-590-ns-slapd-segfaults-while-trying-to-delete.patch
Patch36:          0036-Bugzilla-912964-bug-in-handling-of-LDAPv3-control-da.patch
Patch37:          0037-Ticket-623-cleanAllRUV-task-fails-to-cleanup-config-.patch
Patch38:          0038-Coverity-issue-13091.patch
Patch39:          0039-Ticket-634-Deadlock-in-DNA-plug-in.patch
Patch40:          0040-Ticket-627-ns-slapd-crashes-sporadically-with-segmen.patch
Patch41:          0041-Ticket-628-crash-in-aci-evaluation.patch
Patch42:          0042-Ticket-47308-unintended-information-exposure-when-an.patch
Patch43:          0043-Ticket-623-cleanAllRUV-task-fails-to-cleanup-config-.patch
Patch44:          0044-Coverity-fix.patch  
Patch45:          0045-Ticket-623-cleanAllRUV-task-fails-to-cleanup-config-.patch
Patch46:          0046-Ticket-47385-DS-not-shutting-down-when-disk-monitori.patch
Patch47:          0047-CVE-2013-2219-ACLs-inoperative-in-some-search-scenar.patch
Patch48:          0048-Tickets-47427-47385-Disk-Monitoring-Fixes.patch
Patch49:          0049-Ticket-47427-Overflow-in-nsslapd-disk-monitoring-thr.patch
Patch50:          0050-Disk-Monitoring-fix-log-output-Ticket-47427.patch
Patch51:          0051-Ticket-47427-limits-check-reported-wrong-value.patch
Patch52:          0052-Ticket-47412-Modify-RUV-should-be-serialized-in-ldbm.patch
Patch53:          0053-Ticket-632-389-ds-base-cannot-handle-Kerberos-ticket.patch
Patch54:          0054-Ticket-47367-phase-1-ldapdelete-returns-non-leaf-ent.patch
Patch55:          0055-Ticket-47327-error-syncing-group-if-group-member-use.patch
Patch56:          0056-Ticket-47376-DESC-should-not-be-empty-as-per-RFC-225.patch
Patch57:          0057-Ticket-47349-DS-instance-crashes-under-a-high-load.patch
Patch58:          0058-Ticket-47347-Simple-paged-results-should-support-asy.patch
Patch59:          0059-Trac-Ticket-531-loading-an-entry-from-the-database-s.patch
Patch60:          0060-Ticket-47362-ipa-upgrade-selinuxusermap-data-not-rep.patch
Patch61:          0061-Ticket-47361-Empty-control-list-causes-LDAP-protocol.patch
Patch62:          0062-Ticket-47359-new-ldap-connections-can-block-ldaps-an.patch
Patch63:          0063-Ticket-580-Wrong-error-code-return-when-using-EXTERN.patch
Patch64:          0064-Ticket-47375-flush_ber-error-sending-back-start_tls-.patch
Patch65:          0065-Ticket-47377-make-listen-backlog-size-configurable.patch
Patch66:          0066-Ticket-47383-connections-attribute-in-cn-snmp-cn-mon.patch
Patch67:          0067-Ticket-47392-ldbm-errors-when-adding-modifying-delet.patch
Patch68:          0068-fix-coverity-11895-null-deref-caused-by-fix-to-ticke.patch
Patch69:          0069-Ticket-47391-deleting-and-adding-userpassword-fails-.patch
Patch70:          0070-Ticket-47391-deleting-and-adding-userpassword-fails-.patch
Patch71:          0071-Ticket-47395-47397-v2-correct-behaviour-of-account-p.patch
Patch72:          0072-Fix-compiler-warnings-for-Ticket-47395-and-47397.patch
Patch73:          0073-Ticket-47396-crash-on-modrdn-of-tombstone.patch
Patch74:          0074-Ticket-47393-Attribute-are-not-encrypted-on-a-consum.patch
Patch75:          0075-Ticket-47410-changelog-db-deadlocks-with-DNA-and-rep.patch
Patch76:          0076-Ticket-47402-Attribute-names-are-incorrect-in-search.patch
Patch77:          0077-Ticket-47409-allow-setting-db-deadlock-rejection-pol.patch
Patch78:          0078-Ticket-47409-allow-setting-db-deadlock-rejection-pol.patch
Patch79:          0079-Ticket-47409-allow-setting-db-deadlock-rejection-pol.patch
Patch80:          0080-Ticket-47424-Replication-problem-with-add-delete-req.patch
Patch81:          0081-Ticket-47428-Memory-leak-in-389-ds-base-1.2.11.15.patch
Patch82:          0082-Ticket-47378-fix-recent-compiler-warnings.patch
Patch83:          0083-Ticket-47378-fix-recent-compiler-warnings.patch
Patch84:          0084-Ticket-47435-Very-large-entryusn-values-after-enabli.patch
Patch85:          0085-Ticket-47421-memory-leaks-in-set_krb5_creds.patch
Patch86:          0086-Ticket-47449-deadlock-after-adding-and-deleting-entr.patch
Patch87:          0087-Ticket-543-Sorting-with-attributes-in-ldapsearch-giv.patch
Patch88:          0088-Ticket-47441-Disk-Monitoring-not-checking-filesystem.patch
Patch89:          0089-Coverity-Fixes-part-1.patch
Patch90:          0090-Coverity-Fixes-Part-2.patch
Patch91:          0091-Coverity-Fixes-Part-3.patch
Patch92:          0092-Coverity-Fixes-Part-4.patch
Patch93:          0093-Coverity-Fixes-Part-5.patch
Patch94:          0094-Fri-Jun-7-10-41-00-2013-0400.patch
Patch95:          0095-Coverity-Fixes-Part-7.patch
Patch96:          0096-fix-compiler-warning.patch
Patch97:          0097-fix-compiler-warning-in-posix-winsync-code-for-posix.patch
Patch98:          0098-fix-coverity-11915-dead-code-introduced-with-fix-for.patch
Patch99:          0099-Revert-fix-coverity-11915-dead-code-introduced-with-.patch
Patch100:         0100-Ticket-47318-server-fails-to-start-after-upgrade-sch.patch
Patch101:         0101-Bug-999634-ns-slapd-crash-due-to-bogus-DN.patch
Patch102:         0102-Ticket-47427-Overflow-in-nsslapd-disk-monitoring-thr.patch
Patch103:         0103-Ticket-47523-Set-up-replcation-agreement-before-init.patch
Patch104:         0104-Ticket-47489-Under-specific-values-of-nsDS5ReplicaNa.patch
Patch105:         0105-Ticket-47534-RUV-tombstone-search-with-scope-one-doe.patch
Patch106:         0106-Ticket-47509-CLEANALLRUV-doesnt-run-across-all-repli.patch
Patch107:         0107-Ticket-47509-Cleanallruv-jenkins-error.patch
Patch108:         0108-Ticket-47488-Users-from-AD-sub-OU-does-not-sync-to-I.patch
Patch109:         0109-Ticket-47559-hung-server-related-to-sasl-and-initial.patch
Patch110:         0110-Bug-1024552-DoS-due-to-improper-handling-of-ger-attr.patch
Patch111:         0111-Revert-Ticket-47559-hung-server-related-to-sasl-and-.patch
Patch112:         0112-Ticket-47739-directory-server-is-insecurely-misinter.patch
Patch113:         0113-Ticket-47623-fix-memleak-caused-by-47347.patch
Patch114:         0114-Ticket-47623-fix-memleak-caused-by-47347.patch
Patch115:         0115-Ticket-47707-389-DS-Server-crashes-and-dies-while-ha.patch
Patch116:         0116-Ticket-47516-replication-stops-with-excessive-clock-.patch
Patch117:         0117-Ticket-47492-PassSync-removes-User-must-change-passw.patch
Patch118:         0118-Ticket-47504-idlistscanlimit-per-index-type-value.patch
Patch119:         0119-Ticket-47504-idlistscanlimit-per-index-type-value.patch
Patch120:         0120-Ticket-47504-idlistscanlimit-per-index-type-value.patch
Patch121:         0121-Ticket-356-RFE-Track-bind-info.patch
Patch122:         0122-Ticket-539-logconv.pl-should-handle-microsecond-timi.patch
Patch123:         0123-Ticket-471-logconv.pl-tool-removes-the-access-logs-c.patch
Patch124:         0124-TIcket-419-logconv.pl-improve-memory-management.patch
Patch125:         0125-Ticket-419-logconv.pl-improve-memory-management.patch
Patch126:         0126-Ticket-611-logconv.pl-missing-stats-for-StartTLS-LDA.patch
Patch127:         0127-Ticket-47336-logconv.pl-m-not-working-for-all-stats.patch
Patch128:         0128-Ticket-47341-logconv.pl-m-time-calculation-is-wrong.patch
Patch129:         0129-Ticket-47348-add-etimes-to-per-second-minute-stats.patch
Patch130:         0130-Ticket-47447-logconv.pl-man-page-missing-m-M-B-D.patch
Patch131:         0131-Ticket-47461-logconv.pl-Use-of-comma-less-variable-l.patch
Patch132:         0132-Ticket-47354-Indexed-search-are-logged-with-notes-U-.patch
Patch133:         0133-Ticket-47387-improve-logconv.pl-performance-with-lar.patch
Patch134:         0134-Ticket-47387-improve-logconv.pl-performance-with-lar.patch
Patch135:         0135-Ticket-47520-Fix-various-issues-with-logconv.pl.patch
Patch136:         0136-Ticket-47501-logconv.pl-uses-var-tmp-for-BDB-temp-fi.patch
Patch137:         0137-Ticket-47533-logconv-some-stats-do-not-work-across-s.patch
Patch138:         0138-Coverity-fixes-12023-12024-and-12025.patch
Patch139:         0139-Ticket-422-389-ds-base-Can-t-call-method-getText.patch
Patch140:         0140-Ticket-47517-fix-memory-leak-in-ldbm_delete.c.patch
Patch141:         0141-Ticket-47551-logconv-V-does-not-produce-unindexed-se.patch
Patch142:         0142-Ticket-47550-logconv-failed-logins-Use-of-uninitiali.patch
Patch143:         0143-ticket-47550-wip.patch
Patch144:         0144-Ticket-47577-crash-when-removing-entries-from-cache.patch
Patch145:         0145-Ticket-47581-Winsync-plugin-segfault-during-incremen.patch
Patch146:         0146-Ticket-47581-Winsync-plugin-segfault-during-incremen.patch
Patch147:         0147-Ticket-47585-Replication-Failures-related-to-skipped.patch
Patch148:         0148-Ticket-47596-attrcrypt-fails-to-find-unlocked-key.patch
Patch149:         0149-Ticket-47596-attrcrypt-fails-to-find-unlocked-key.patch
Patch150:         0150-Ticket-47591-entries-with-empty-objectclass-attribut.patch
Patch151:         0151-Ticket-47587-hard-coded-limit-of-64-masters-in-agree.patch
Patch152:         0152-Ticket-47627-changelog-iteration-should-ignore-clean.patch
Patch153:         0153-Ticket-47627-Fix-replication-logging.patch
Patch154:         0154-Ticket-47516-replication-stops-with-excessive-clock-.patch
Patch155:         0155-Ticket-47678-modify-delete-userpassword.patch
Patch156:         0156-Ticket-47641-7-bit-check-plugin-not-checking-MODRDN-.patch
Patch157:         0157-Ticket-47427-Overflow-in-nsslapd-disk-monitoring-thr.patch
Patch158:         0158-Ticket-47638-Overflow-in-nsslapd-disk-monitoring-thr.patch
Patch159:         0159-Ticket-47463-IDL-style-can-become-mismatched-during-.patch
Patch160:         0160-Ticket-471-logconv.pl-tool-removes-the-access-logs-c.patch
Patch161:         0161-Ticket-47693-Environment-variables-are-not-passed-wh.patch
Patch162:         0162-Ticket-47693-Environment-variables-are-not-passed-wh.patch
Patch163:         0163-Ticket-47677-Size-returned-by-slapi_entry_size-is-no.patch
Patch164:         0164-Ticket-47692-single-valued-attribute-replicated-ADD-.patch
Patch165:         0165-Ticket-47642-Windows-Sync-group-issues.patch
Patch166:         0166-Ticket-415-winsync-doesn-t-sync-DN-valued-attributes.patch
Patch167:         0167-Ticket-346-version-4-Slow-ldapmodify-operation-time-.patch
Patch168:         0168-Ticket-47369-version2-provide-default-syntax-plugin.patch
Patch169:         0169-fix-coverity-11915-dead-code-introduced-with-fix-for.patch
Patch170:         0170-Ticket-47455-valgrind-value-mem-leaks-uninit-mem-usa.patch
Patch171:         0171-Ticket-47637-rsa_null_sha-should-not-be-enabled-by-d.patch
Patch172:         0172-Ticket-47729-Directory-Server-crashes-if-shutdown-du.patch
Patch173:         0173-Ticket-47731-A-tombstone-entry-is-deleted-by-ldapdel.patch
Patch174:         0174-Ticket-47735-e_uniqueid-fails-to-set-if-an-entry-is-.patch
Patch175:         0175-Ticket-47737-Under-heavy-stress-failure-of-turning-a.patch
Patch176:         0176-Ticket-47704-invalid-sizelimits-in-aci-group-evaluat.patch
Patch177:         0177-Ticket-47722-rsearch-filter-error-on-any-search-filt.patch
Patch178:         0178-Ticket47722-Fixed-filter-not-correctly-identified.patch
Patch179:         0179-Ticket-47734-Change-made-in-resolving-ticket-346-fai.patch
Patch180:         0180-Ticket-47740-Coverity-Fixes-Mark-part-1.patch
Patch181:         0181-Ticket-47538-RFE-repl-monitor.pl-plain-text-output-c.patch
Patch182:         0182-Ticket-47740-Fix-coverity-issues-part-3.patch
Patch183:         0183-Ticket-47740-Fix-coverity-erorrs-Part-4.patch
Patch184:         0184-Ticket-47740-Fix-coverity-issues-Part-5.patch
Patch185:         0185-Ticket-47740-Coverity-issue-in-1.3.3.patch
Patch186:         0186-Ticket-47735-e_uniqueid-fails-to-set-if-an-entry-is-.patch
Patch187:         0187-Ticket-47740-Fix-coverity-issues-null-deferences-Par.patch
Patch188:         0188-Ticket-47740-Crash-caused-by-changes-to-certmap.c.patch
Patch189:         0189-Ticket-47743-Memory-leak-with-proxy-auth-control.patch
Patch190:         0190-Ticket-47748-Simultaneous-adding-a-user-and-binding-.patch
Patch191:         0191-Ticket-47740-Fix-coverity-issues-part-7.patch
Patch192:         0192-Ticket-47448-Segfault-in-389-ds-base-1.3.1.4-1.fc19-.patch
Patch193:         0193-Ticket-47492-PassSync-removes-User-must-change-passw.patch
Patch194:         0194-Ticket-47766-Tombstone-purging-can-crash-the-server-.patch
Patch195:         0195-Ticket-47767-Nested-tombstones-become-orphaned-after.patch
Patch196:         0196-Ticket-47771-Performing-deletes-during-tombstone-pur.patch
Patch197:         0197-Ticket-47773-mem-leak-in-do_bind-when-there-is-an-er.patch
Patch198:         0198-Ticket-47774-mem-leak-in-do_search-rawbase-not-freed.patch
Patch199:         0199-Ticket-47772-empty-modify-returns-LDAP_INVALID_DN_SY.patch
Patch200:         0200-Ticket-47736-Import-incorrectly-updates-numsubordina.patch
Patch201:         0201-Ticket-47772-empty-modify-returns-LDAP_INVALID_DN_SY.patch
Patch202:         0202-Ticket-47782-Parent-numbordinate-count-can-be-incorr.patch
Patch203:         0203-Ticket-346-Slow-ldapmodify-operation-time-for-large-.patch
Patch204:         0204-Ticket-47771-Cherry-pick-issue-parentsdn-freed-twice.patch
Patch205:         0205-Ticket-47771-Move-parentsdn-initialization-to-avoid-.patch
Patch206:         0206-Ticket-47793-Server-crashes-if-uniqueMember-is-inval.patch
Patch207:         0207-Ticket-47772-fix-coverity-issue.patch
Patch208:         0208-Ticket-47649-Server-hangs-in-cos_cache-when-adding-a.patch
Patch209:         0209-Ticket-47750-Creating-a-glue-fails-if-one-above-leve.patch
Patch210:         0210-Ticket-47764-Problem-with-deletion-while-replicated.patch
Patch211:         0211-Ticket-47787-A-replicated-MOD-fails-Unwilling-to-per.patch
Patch212:         0212-Ticket-47780-Some-VLV-search-request-causes-memory-l.patch
Patch213:         0213-Ticket-47804-db2bak.pl-error-with-changelogdb.patch
Patch214:         0214-Ticket-47670-Aci-warnings-in-error-log.patch
Patch215:         0215-Ticket-47713-Logconv.pl-with-an-empty-access-log-giv.patch
Patch216:         0216-Ticket-47446-logconv.pl-memory-continually-grows.patch
Patch217:         0217-Ticket-47770-481-breaks-possibility-to-reassemble-me.patch
Patch218:         0218-Ticket-47813-managed-entry-plugin-fails-to-update-me.patch
Patch219:         0219-Ticket-47813-remove-goto-bail-from-previous-commit.patch
Patch221:         0220-Ticket-47809-find-a-way-to-remove-replication-plugin.patch
Patch220:         0221-Ticket-47423-7-bit-check-plugin-does-not-work-for-us.patch
Patch222:         0222-Ticket-47426-move-compute_idletimeout-out-of-handle_.patch
Patch223:         0223-Ticket47426-Coverity-issue-with-last-commit-move-com.patch
Patch224:         0224-Ticket-47331-Self-entry-access-ACI-not-working-prope.patch
Patch225:         0225-Ticket-47331-Self-entry-access-ACI-not-working-prope.patch
Patch226:         0226-Ticket-417-458-47522-Password-Administrator-Backport.patch
Patch227:         0227-Ticket-47820-1.2.11-branch-coverity-errors.patch
Patch228:         0228-Ticket-47820-1.2.11-branch-coverity-errors-2.patch
Patch229:         0229-Revert-Ticket-47423-7-bit-check-plugin-does-not-work.patch
Patch230:         0230-Ticket-47831-server-restart-wipes-out-index-config-i.patch
Patch231:         0231-Ticket-47821-deref-plugin-cannot-handle-complex-acis.patch
Patch232:         0232-Ticket-47750-Creating-a-glue-fails-if-one-above-leve.patch
Patch233:         0233-Ticket-47750-Creating-a-glue-fails-if-one-above-leve.patch
Patch234:         0234-Ticket-47750-Creating-a-glue-fails-if-one-above-leve.patch
Patch235:         0235-Revert-Ticket-47750-Creating-a-glue-fails-if-one-abo.patch
Patch236:         0236-Ticket-47824-paged-results-control-is-not-working-in.patch
Patch237:         0237-Ticket-47863-New-defects-found-in-389-ds-base-1.2.11.patch
Patch238:         0238-Ticket-47862-Repl-monitor.pl-ignores-the-provided-co.patch
Patch239:         0239-Trac-Ticket-443-Deleting-attribute-present-in.patch
Patch240:         0240-Ticket-443-Deleting-attribute-present-in-nsslapd-all.patch
Patch241:         0241-Ticket-616-High-contention-on-computed-attribute-loc.patch
Patch242:         0242-Bug-1123477-unauthenticated-information-disclosure.patch
Patch243:         0243-Ticket-47692-single-valued-attribute-replicated-ADD-.patch
Patch244:         0244-Ticket-47862-repl-monitor-fails-to-convert-to-defaul.patch
Patch245:         0245-Ticket-47872-Filter-AND-with-only-one-clause-should-.patch
Patch246:         0246-Ticket-47874-Performance-degradation-with-scope-ONE-.patch
Patch247:         0247-Ticket-415-winsync-doesn-t-sync-DN-valued-attributes.patch
Patch248:         0248-Trac-Ticket-443-Deleting-attribute-present-in-nsslap.patch
Patch249:         0249-Ticket-47446-logconv.pl-memory-continually-grows.patch
Patch250:         0250-Ticket-47875-dirsrv-not-running-with-old-openldap.patch
Patch251:         0251-Ticket-47875-dirsrv-not-running-with-old-openldap.patch
Patch252:         0252-Revert-Ticket-47875-dirsrv-not-running-with-old-open.patch  
Patch253:         0253-Revert-Ticket-47875-dirsrv-not-running-with-old-open.patch  
Patch254:         0254-Ticket-47875-dirsrv-not-running-with-old-openldap.patch
Patch255:         0255-Ticket-47875-dirsrv-not-running-with-old-openldap.patch
Patch256:         0256-Bug-1129660-Adding-users-to-user-group-throws-Intern.patch
Patch257:         0257-Ticket-47885-deref-plugin-should-not-return-referenc.patch
Patch258:         0258-Ticket-47748-Simultaneous-adding-a-user-and-binding-.patch
Patch259:         0259-fix-for-47885-did-not-always-return-a-response-contr.patch
Patch260:         0260-Ticket-47750-Fix-incomplete-backport-to-1.3.1-1.2.11.patch
Patch261:         0261-Ticket-47750-Entry-cache-part-2.patch
Patch262:         0262-Ticket-47750-Entry-cache-part-2.patch
Patch263:         0263-Ticket-47889-DS-crashed-during-ipa-server-install-on.patch
Patch264:         0264-Fix-for-CVE-2014-8105.patch
Patch265:         0265-Description-Fix-for-ticket-47915-replication-inconsi.patch
Patch266:         0266-Ticket-47457-default-nsslapd-sasl-max-buffer-size-sh.patch
Patch267:         0267-Ticket-47953-Should-not-check-aci-syntax-when-deleti.patch
Patch268:         0268-Ticket-569-examine-replication-code-to-reduce-amount.patch
Patch269:         0269-Ticket-47907-ldclt-assertion-failure-with-e-add-coun.patch
Patch270:         0270-Ticket-47900-Adding-an-entry-with-an-invalid-passwor.patch
Patch271:         0271-Ticket-47900-Server-fails-to-start-if-password-admin.patch
Patch272:         0272-Ticket-47900-Fix-backport-issue-to-1.2.11.patch
Patch273:         0273-Ticket-47952-PasswordAdminDN-attribute-is-not-proper.patch
Patch274:         0274-Ticket-47958-Memory-leak-in-password-admin-if-the-ad.patch
Patch275:         0275-Ticket-47950-Bind-DN-tracking-unable-to-write-to-int.patch
Patch276:         0276-Ticket-47963-RFE-memberOf-add-option-to-skip-nested-.patch
Patch277:         0277-Ticket-47963-skip-nested-groups-breaks-memberof-fixu.patch
Patch278:         0278-Ticket-47967-cos_cache_build_definition_list-does-no.patch
Patch279:         0279-Ticket-47969-COS-memory-leak-when-rebuilding-the-cac.patch
Patch280:         0280-Ticket-47969-Fix-coverity-issue.patch
Patch281:         0281-Ticket-47970-Account-lockout-attributes-incorrectly-.patch
Patch282:         0282-Ticket-47965-Fix-coverity-issues-2014-11-24.patch
Patch283:         0283-Ticket-47965-Fix-coverity-issues-2014-12-16.patch
Patch284:         0284-Ticket-47750-Need-to-refresh-cache-entry-after-calle.patch
Patch285:         0285-Ticket-47750-During-delete-operation-do-not-refresh-.patch
Patch286:         0286-Ticket-408-Backport-of-Normalized-DN-Cache.patch
Patch287:         0287-Ticket-47980-Nested-COS-definitions-can-be-incorrect.patch
Patch288:         0288-Ticket-47962-perl-scripts-not-returning-expected-err.patch
Patch289:         0289-Ticket-547-Incorrect-assumption-in-ndn-cache.patch
Patch290:         0290-Coverity-defects.patch
Patch291:         0291-Ticket-47981-COS-cache-doesn-t-properly-mark-vattr-c.patch
Patch292:         0292-Ticket-47949-logconv.pl-support-parsing-showing-repo.patch
Patch293:         0293-Ticket-47928-Disable-SSL-v3-by-default-389-ds-base-1.patch
Patch294:         0294-Ticket-47945-Add-SSL-TLS-version-info-to-the-access-.patch
Patch295:         0295-Ticket-47880-provide-enabled-ciphers-as-search-resul.patch
Patch296:         0296-Ticket-47659-ldbm_usn_init-Valgrind-reports-Invalid-.patch
Patch297:         0297-Ticket-47884-WinSync-manual-replica-refresh-removes-.patch
Patch298:         0298-Ticket-47973-During-schema-reload-sometimes-the-sear.patch
Patch299:         0299-Ticket-47905-Bad-manipulation-of-passwordhistory.patch
Patch300:         0300-Ticket-47934-nsslapd-db-locks-modify-not-taking-into.patch
Patch301:         0301-Ticket-47989-Windows-Sync-accidentally-cleared-raw_e.patch
Patch302:         0302-Ticket-47996-ldclt-needs-to-support-SSL-Version-rang.patch
Patch303:         0303-Ticket-47963-memberof-skip-nested-groups-breaks-the-.patch
Patch304:         0304-Ticket-47752-Don-t-add-unhashed-password-mod-if-we-d.patch
Patch305:         0305-Ticket-47965-Fix-coverity-issues-and-compiler-warnin.patch
Patch306:         0306-Coverity-fix-Invalid-Dereference-in-ndn_cache_add-dn.patch
Patch307:         0307-Ticket-48133-Non-tombstone-entry-which-dn-starting-w.patch
Patch308:         0308-Ticket-48135-memory-leak-in-new_passwdPolicy-1.2.11-.patch
Patch309:         0309-Ticket-561-disable-writing-unhashed-user-password-to.patch
Patch310:         0310-Ticket-47942-DS-hangs-during-online-total-update.patch
Patch311:         0311-Ticket-408-Backport-of-Normalized-DN-Cache.patch
Patch312:         0312-Ticket-48148-start-stop-restart-dirsrv-utilities-sho.patch
Patch313:         0313-Ticket-47928-Disable-SSL-v3-by-default-389-ds-base-1.patch
Patch314:         0314-Ticket-48154-abort-cleanAllRUV-tasks-should-not-cert.patch
Patch315:         0315-Ticket-48143-Password-is-not-correctly-passed-to-per.patch
Patch316:         0316-Ticket-48146-async-simple-paged-results-issue.patch
Patch317:         0317-Ticket-48146-async-simple-paged-results-issue-log-pr.patch
Patch318:         0318-Ticket-48146-async-simple-paged-results-issue-need-t.patch
Patch319:         0319-Ticket-48146-async-simple-paged-results-issue.patch
Patch320:         0320-Ticket-48180-Lowering-the-log-level-of-Configured-SS.patch
Patch321:         0321-Ticket-48151-Improve-CleanAllRUV-logging.patch
Patch322:         0322-Ticket-48158-Remove-cleanAllRUV-task-limit-of-4.patch
Patch323:         0323-Ticket-48148-start-stop-restart-dirsrv-utilities-sho.patch
Patch324:         0324-Ticket-48151-fix-coverity-issues.patch
Patch325:         0325-Ticket-48158-cleanAllRUV-task-limit-not-being-enforc.patch
Patch326:         0326-Ticket-48183-bind-on-db-chained-to-AD-returns-err-32.patch
Patch327:         0327-Ticket-48146-async-simple-paged-results-issue.patch
Patch328:         0328-Ticket-48146-async-simple-paged-results-issue.patch
Patch329:         0329-Ticket-48149-ns-slapd-double-free-or-corruption-cras.patch
Patch330:         0330-Ticket-48149-ns-slapd-double-free-or-corruption-cras.patch
Patch331:         0331-Ticket-48148-start-stop-restart-dirsrv-utilities-sho.patch
Patch332:         0332-Ticket-48192-Individual-abandoned-simple-paged-resul.patch
Patch333:         0333-Ticket-48192-Individual-abandoned-simple-paged-resul.patch
Patch334:         0334-Ticket-48192-Individual-abandoned-simple-paged-resul.patch
Patch335:         0335-Ticket-621-modify-operations-without-values-do-not-g.patch
Patch336:         0336-Ticket-47981-COS-cache-doesn-t-properly-mark-vattr-c.patch
Patch337:         0337-Ticket-48192-Individual-abandoned-simple-paged-resul.patch
Patch338:         0338-Ticket-48266-Fractional-replication-evaluates-severa.patch
Patch339:         0339-Ticket-48266-coverity-issue.patch
Patch340:         0340-Ticket-48266-Online-init-crashes-consumer.patch
Patch341:         0341-Ticket-48284-free-entry-when-internal-add-fails.patch
Patch342:         0342-Ticket-48266-do-not-free-repl-keep-alive-entry-on-er.patch
Patch343:         0343-Ticket-48299-pagedresults-when-timed-out-search-resu.patch
Patch344:         0344-Ticket-48192-Individual-abandoned-simple-paged-resul.patch
Patch345:         0345-Ticket-48266-1.2.11-only-Fractional-replication-eval.patch
Patch346:         0346-Ticket-48208-CleanAllRUV-should-completely-purge-cha.patch
Patch347:         0347-Ticket-48283-many-attrlist_replace-errors-in-connect.patch
Patch348:         0348-Ticket-48245-Man-pages-and-help-for-remove-ds.pl-doe.patch
Patch349:         0349-Ticket-48195-Slow-replication-when-deleting-large.patch
Patch350:         0350-Ticket-48175-Avoid-using-regex-in-ACL-if-possible.patch
Patch351:         0351-Ticket-48212-Dynamic-nsMatchingRule-changes-had-no-e.patch
Patch352:         0352-Ticket-48206-Crash-during-retro-changelog-trimming.patch
Patch353:         0353-Ticket-48232-winsync-lastlogon-attribute-not-syncing.patch
Patch354:         0354-Ticket-48215-verify_db.pl-doesn-t-verify-DB-specifie.patch
Patch355:         0355-Ticket-48215-update-dbverify-usage-in-main.c.patch
Patch356:         0356-Ticket-48231-logconv-autobind-handling-regression-ca.patch
Patch357:         0357-Ticket-48228-wrong-password-check-if-passwordInHisto.patch
Patch358:         0358-Ticket-48228-wrong-password-check-if-passwordInHisto.patch
Patch359:         0359-Ticket-48252-db2index-creates-index-entry-from-delet.patch
Patch360:         0360-Ticket-48305-perl-module-conditional-test-is-not-con.patch
Patch361:         0361-Ticket-48304-ns-slapd-LOGINFO-Unable-to-remove-file.patch
Patch362:         0362-Ticket-48287-Double-free-while-adding-entries-1.2.11.patch
Patch363:         0363-Ticket-47978-Deadlock-between-two-MODs-on-the-same-e.patch
Patch364:         0364-Ticket-47976-deadlock-in-mep-delete-post-op.patch
Patch365:         0365-Ticket-48338-SimplePagedResults-abandon-could-happen.patch
Patch366:         0366-Ticket-48338-SimplePagedResults-abandon-could-happen.patch
Patch367:         0367-Ticket-48370-The-eq-index-does-not-get-updated-prope.patch
Patch368:         0368-Ticket-48305-perl-module-conditional-test-is-not-con.patch
Patch369:         0369-Ticket-48289-389-ds-base-ldclt-bin-killed-by-SIGSEGV.patch
Patch370:         0370-Ticket-48375-SimplePagedResults-in-the-search-error-.patch
Patch371:         0371-Ticket-48332-allow-users-to-specify-to-relax-the-FQD.patch
Patch372:         0372-Revert-Ticket-48338-SimplePagedResults-abandon-could.patch
Patch373:         0373-Ticket-48406-Avoid-self-deadlock-by-PR_Lock-conn-c_m.patch
Patch374:         0374-Ticket-196-RFE-Interpret-IPV6-addresses-for-ACIs-rep.patch
Patch375:         0375-Ticket-47788-Supplier-can-skip-a-failing-update-alth.patch
Patch376:         0376-Ticket-47964-1.2.11-Incorrect-search-result-after-re.patch
Patch377:         0377-Ticket-47788-Only-check-postop-result-if-its-a-repli.patch
Patch378:         0378-Ticket-48445-keep-alive-entries-can-break-replicatio.patch
Patch379:         0379-Ticket-48420-change-severity-of-some-messages-relate.patch
Patch380:         0380-Ticket-48808-Paged-results-search-returns-the-blank-.patch
Patch381:         0381-Ticket-48813-password-history-is-not-updated-when-an.patch
Patch382:         0382-Ticket-48854-Running-db2index-with-no-options-breaks.patch

%description
389 Directory Server is an LDAPv3 compliant server.  The base package includes
the LDAP server and command line utilities for server administration.

%package          libs
Summary:          Core libraries for 389 Directory Server
Group:            System Environment/Daemons
BuildRequires:    nspr-devel
BuildRequires:    nss-devel
BuildRequires:    svrcore-devel
%if %{use_openldap}
BuildRequires:    openldap-devel
%else
BuildRequires:    mozldap-devel
%endif
BuildRequires:    db4-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    libicu-devel
BuildRequires:    pcre-devel

%description      libs
Core libraries for the 389 Directory Server base package.  These libraries
are used by the main package and the -devel package.  This allows the -devel
package to be installed with just the -libs package and without the main package.

%package          devel
Summary:          Development libraries for 389 Directory Server
Group:            Development/Libraries
Requires:         %{name}-libs = %{version}-%{release}
Requires:         pkgconfig
Requires:         nspr-devel
Requires:         nss-devel
Requires:         svrcore-devel
%if %{use_openldap}
Requires:         openldap-devel
%else
Requires:         mozldap-devel
%endif

%description      devel
Development Libraries and headers for the 389 Directory Server base package.

%prep
%setup -q -n %{name}-%{srcver}%{?srcprerel}
cp %{SOURCE1} README.devel
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
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
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
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1
%patch242 -p1
%patch243 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1
%patch247 -p1
%patch248 -p1
%patch249 -p1
%patch250 -p1
%patch251 -p1
%patch252 -p1
%patch253 -p1
%patch254 -p1
%patch255 -p1
%patch256 -p1
%patch257 -p1
%patch258 -p1
%patch259 -p1
%patch260 -p1
%patch261 -p1
%patch262 -p1
%patch263 -p1
%patch264 -p1
%patch265 -p1
%patch266 -p1
%patch267 -p1
%patch268 -p1
%patch269 -p1
%patch270 -p1
%patch271 -p1
%patch272 -p1
%patch273 -p1
%patch274 -p1
%patch275 -p1
%patch276 -p1
%patch277 -p1
%patch278 -p1
%patch279 -p1
%patch280 -p1
%patch281 -p1
%patch282 -p1
%patch283 -p1
%patch284 -p1
%patch285 -p1
%patch286 -p1
%patch287 -p1
%patch288 -p1
%patch289 -p1
%patch290 -p1
%patch291 -p1
%patch292 -p1
%patch293 -p1
%patch294 -p1
%patch295 -p1
%patch296 -p1
%patch297 -p1
%patch298 -p1
%patch299 -p1
%patch300 -p1
%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1
%patch307 -p1
%patch308 -p1
%patch309 -p1
%patch310 -p1
%patch311 -p1
%patch312 -p1
%patch313 -p1
%patch314 -p1
%patch315 -p1
%patch316 -p1
%patch317 -p1
%patch318 -p1
%patch319 -p1
%patch320 -p1
%patch321 -p1
%patch322 -p1
%patch323 -p1
%patch324 -p1
%patch325 -p1
%patch326 -p1
%patch327 -p1
%patch328 -p1
%patch329 -p1
%patch330 -p1
%patch331 -p1
%patch332 -p1
%patch333 -p1
%patch334 -p1
%patch335 -p1
%patch336 -p1
%patch337 -p1
%patch338 -p1
%patch339 -p1
%patch340 -p1
%patch341 -p1
%patch342 -p1
%patch343 -p1
%patch344 -p1
%patch345 -p1
%patch346 -p1
%patch347 -p1
%patch348 -p1
%patch349 -p1
%patch350 -p1
%patch351 -p1
%patch352 -p1
%patch353 -p1
%patch354 -p1
%patch355 -p1
%patch356 -p1
%patch357 -p1
%patch358 -p1
%patch359 -p1
%patch360 -p1
%patch361 -p1
%patch362 -p1
%patch363 -p1
%patch364 -p1
%patch365 -p1
%patch366 -p1
%patch367 -p1
%patch368 -p1
%patch369 -p1
%patch370 -p1
%patch371 -p1
%patch372 -p1
%patch373 -p1
%patch374 -p1
%patch375 -p1
%patch376 -p1
%patch377 -p1
%patch378 -p1
%patch379 -p1
%patch380 -p1
%patch381 -p1
%patch382 -p1

%build
%if %{use_openldap}
OPENLDAP_FLAG="--with-openldap"
%endif
%{?with_tmpfiles_d: TMPFILES_FLAG="--with-tmpfiles-d=%{with_tmpfiles_d}"}
%configure --enable-autobind --with-selinux $OPENLDAP_FLAG $TMPFILES_FLAG

# Generate symbolic info for debuggers
export XCFLAGS=$RPM_OPT_FLAGS

%ifarch x86_64 ppc64 ia64 s390x sparc64
export USE_64=1
%endif

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT 

make DESTDIR="$RPM_BUILD_ROOT" install

mkdir -p $RPM_BUILD_ROOT/var/log/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lib/%{pkgname}
mkdir -p $RPM_BUILD_ROOT/var/lock/%{pkgname}

#remove libtool and static libs
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/%{pkgname}/plugins/*.la

# make sure perl scripts have a proper shebang 
sed -i -e 's|#{{PERL-EXEC}}|#!/usr/bin/perl|' $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/script-templates/template-*.pl

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{pkgname}
/sbin/ldconfig
/sbin/chkconfig --add %{pkgname}-snmp
# restart the snmp subagent if needed
/sbin/service %{pkgname}-snmp condrestart > /dev/null 2>&1
instbase="%{_sysconfdir}/%{pkgname}"
# echo posttrans - upgrading - looking for instances in $instbase
# find all instances
instances="" # instances that require a restart after upgrade
ninst=0 # number of instances found in total
for dir in $instbase/slapd-* ; do
# echo dir = $dir
    if [ ! -d "$dir" ] ; then continue ; fi
    case "$dir" in *.removed) continue ;; esac
    basename=`basename $dir`
    inst=`echo $basename | sed -e 's/slapd-//g'`
#   echo found instance $inst - getting status
    if /sbin/service %{pkgname} status $inst >/dev/null 2>&1 ; then
#      echo instance $inst is running
       instances="$instances $inst"
    else
#      echo instance $inst is not running
       :
    fi
    ninst=`expr $ninst + 1`
done
if [ $ninst -eq 0 ] ; then
    exit 0 # have no instances to upgrade - just skip the rest
fi
# shutdown all instances
# echo shutting down all instances . . .
/sbin/service %{pkgname} stop > /dev/null 2>&1
# do the upgrade
# echo upgrading instances . . .
%{_sbindir}/setup-ds.pl -l /dev/null -u -s General.UpdateMode=offline > /dev/null 2>&1
# restart instances that require it
for inst in $instances ; do
#   echo restarting instance $inst
    /sbin/service %{pkgname} start $inst >/dev/null 2>&1
done
exit 0

%preun
if [ $1 = 0 ]; then # Final removal
        /sbin/service %{pkgname} stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del %{pkgname}
        /sbin/service %{pkgname}-snmp stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del %{pkgname}-snmp
fi

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then # Final removal
    rm -rf /var/run/%{pkgname}
fi

%files
%defattr(-,root,root,-)
%doc LICENSE EXCEPTION LICENSE.GPLv2
%dir %{_sysconfdir}/%{pkgname}
%dir %{_sysconfdir}/%{pkgname}/schema
%config(noreplace)%{_sysconfdir}/%{pkgname}/schema/*.ldif
%dir %{_sysconfdir}/%{pkgname}/config
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/slapd-collations.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/certmap.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/ldap-agent.conf
%config(noreplace)%{_sysconfdir}/%{pkgname}/config/template-initconfig
%config(noreplace)%{_sysconfdir}/sysconfig/%{pkgname}
%{_datadir}/%{pkgname}
%{_sysconfdir}/rc.d/init.d/%{pkgname}
%{_sysconfdir}/rc.d/init.d/%{pkgname}-snmp
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/%{pkgname}/libns-dshttpd.so*
%{_libdir}/%{pkgname}/perl
%dir %{_libdir}/%{pkgname}/plugins
%{_libdir}/%{pkgname}/plugins/*.so
%dir %{_localstatedir}/lib/%{pkgname}
%dir %{_localstatedir}/log/%{pkgname}
%dir %{_localstatedir}/lock/%{pkgname}
%{_mandir}/man1/*
%{_mandir}/man8/*

%files devel
%defattr(-,root,root,-)
%doc LICENSE EXCEPTION LICENSE.GPLv2 README.devel
%{_includedir}/%{pkgname}
%{_libdir}/%{pkgname}/libslapd.so
%{_libdir}/pkgconfig/*

%files libs
%defattr(-,root,root,-)
%doc LICENSE EXCEPTION LICENSE.GPLv2 README.devel
%dir %{_libdir}/%{pkgname}
%{_libdir}/%{pkgname}/libslapd.so.*

%changelog
* Fri Jun  3 2016 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-75
- Release 1.2.11.15-75
- Resolves: #1335108 - Paged results search returns the blank list of entries (DS 48808)
- Resolves: #1342614 - password history is not updated when an admin resets the password (DS 48813)
- Resolves: #1342382 - Running db2index with no options breaks replication (DS 48854)

* Thu Mar  3 2016 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-74
- Release 1.2.11.15-74
- Resolves: #1313258 - change severity of some messages related to "keep alive" entries (DS 48420)

* Fri Feb 12 2016 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-73
- Release 1.2.11.15-73
- Resolves: #1294770 - Supplier can skip a failing update, although it should retry (DS 47788)
- Resolves: #1298496 - slapd process crashes on entry modification (DS 47964)
- Resolves: #1307152 - keep alive entries can break replication (DS 48445)

* Mon Jan 18 2016 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-72
- Release 1.2.11.15-72
- Resolves: #1292649 - allow users to specify to relax the FQDN constraint (DS 48332)
- Resolves: #1294770 - Supplier can skip a failing update, although it should retry (DS 47788)
- Resolves: #1296694 - ns-slapd crash in ipa context - c_mutex lock memory corruption and self locks (DS 48406, DS 48338 reverted)
- Resolves: #1297385 - Interpret IPV6 addresses for ACIs, replication, and chaining (DS 196)

* Thu Dec 10 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-71
- Release 1.2.11.15-71
- Resolves: #1284791 - 389-ds-base: ldclt -e randomauthid Segmentation fault. (DS 48289)
- Resolves: #1290243 - SimplePagedResults -- in the search error case, simple paged results slot was not released (DS 48375)

* Tue Dec  8 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-70
- Release 1.2.11.15-70
- Resolves: #1259959 - perl module conditional test is not conditional when checking SELinux policies - fixing a regression (DS 48305)
- Resolves: #1282457 - The 'eq' index does not get updated properly when deleting and re-adding attributes in the same ldapmodify operation (DS 48370)

* Wed Nov 18 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-69
- Release 1.2.11.15-69
- Resolves: #1247792 - SimplePagedResults -- abandon could happen between the abandon check and sending results -- Fixing a regression introduced in 1.2.11.15-68 (DS 48338)

* Fri Nov  6 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-68
- Release 1.2.11.15-68
- Resolves: #1278585 - deadlock in mep delete post op (DS 47976) 
- Resolves: #1247792 - SimplePagedResults -- abandon could happen between the abandon check and sending results (DS 48338)

* Tue Nov  3 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-67
- Release 1.2.11.15-67
- Resolves: #1234431 - Man pages and help for remove-ds.pl doesn't display "-a" option (DS 48245)
- Resolves: #1236148 - Slow replication when deleting large  quantities of multi-valued attributes (DS 48195)
- Resolves: #1236156 - Avoid using regex in ACL if possible (DS 48175)
- Resolves: #1236656 - Dynamic nsMatchingRule changes had no effect on the attrinfo thus following reindexing, as well. (DS 48212)
- Resolves: #1240451 - Individual abandoned simple paged results request has no chance to be cleaned up (DS 48192)
- Resolves: #1244970 - Crash during retro changelog trimming (DS 48206)
- Resolves: #1245237 - winsync lastlogon attribute not syncing between DS and AD. (DS 48232)
- Resolves: #1246165 - verify_db.pl doesn't verify DB specified by -a option (DS 48215)
- Resolves: #1247812 - logconv autobind handling regression caused by 47446 (DS 48231)
- Resolves: #1253406 - wrong password check if passwordInHistory is decreased. (DS 48228)
- Resolves: #1255290 - db2index creates index entry from deleted records (DS 48252)
- Resolves: #1259959 - perl module conditional test is not conditional when checking SELinux policies (DS 48305)
- Resolves: #1260622 - ns-slapd - LOGINFO:Unable to remove file (DS 48304)
- Resolves: #1265851 - Double free while adding entries (1.2.11 only) (DS 48287)
- Resolves: #1273552 - Deadlock between two MODs on the same entry between entry cache and backend lock (DS 47978)

* Thu Oct 15 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-66
- Release 1.2.11.15-66
- Resolves: #1270002 - cleanallruv should completely clean changelog (DS 48208)
- Resolves: #1267405 - many attrlist_replace errors in connection with cleanallruv (DS 48283)

* Tue Oct  6 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-65
- Release 1.2.11.15-65
- Resolves: #1259383 - Fractional replication evaluates several times the same CSN (DS 48266)

* Fri Oct  2 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-64
- Release 1.2.11.15-64
- Resolves: #1247792 - ns-slapd crashing frequently cause is unknown (DS 48192)
- Resolves: #1267296 - pagedresults - when timed out, search results could have been already freed. (DS 48299)

* Thu Oct  1 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-63
- Release 1.2.11.15-63
- Resolves: #1247792 - ns-slapd crashing frequently cause is unknown (DS 48192)
- Resolves: #1259383 - Fractional replication evaluates several times the same CSN (DS 48266 48284)

* Fri Sep  4 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-62
- Release 1.2.11.15-62
- Resolves: #1259546 - regression - COS cache doesn't properly mark vattr cache as invalid when there are multiple suffixes (DS 47981)

* Fri Aug 28 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-61
- Release 1.2.11.15-61
- Resolves: #1251288 - Replication not working for "delete: attr"

* Tue Jun  9 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-60
- Release 1.2.11.15-60
- Resolves: #1228402 - Individual abandoned simple paged results request has no chance to be cleaned up (DS 48192)

* Fri Jun  5 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-59
- Release 1.2.11.15-59
- Resolves: #1211006 - start/stop/restart-dirsrv utilities should ignore admin-serv directory (DS 48148)
- Resolves: #1203338 - ns-slapd double free or corruption crash (DS 48149)
- Resolves: #1228402 - Individual abandoned simple paged results request has no chance to be cleaned up (DS 48192)

* Tue Jun  2 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-58
- Release 1.2.11.15-58
- Resolves: #1223068 - Regression introduced by the simple paged results fixes. (DS 48146)
- Resolves: #1203338 - ns-slapd double free or corruption crash (DS 48149)

* Tue May 26 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-57
- Release 1.2.11.15-57
- Resolves: #1223068 - ldapdelete fails with -r option to delete a sub suffix (DS 48146)
- Resolves: #1219990 - bind on db chained to AD returns err=32 (DS 48183)
- Resolves: #1219208 - cleanAllRUV task limit not being enforced correctly (DS 48158)

* Tue May 12 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-56
- Release 1.2.11.15-56
- Resolves: #1219218 - fix coverity issues (DS 48151)

* Tue May 12 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-55
- Release 1.2.11.15-55
- Resolves: #1118285 - Lowering the log level of "Configured SSL version range" message (1.2.11 only) (DS 48180)
- Resolves: #1211006 - start/stop/restart-dirsrv utilities should ignore admin-serv directory (DS 48148)
- Resolves: #1219208 - Remove cleanAllRUV task limit of 4 (DS 48158)
- Resolves: #1219218 - Improve CleanAllRUV logging (DS 48151)

* Tue May  5 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-54
- Release 1.2.11.15-54
- Resolves: #1207983 - disable writing unhashed#user#password to changelog (DS 561)
- Resolves: #1207024 - IPA Replicate creation fails with error "Update failed! Status: [10 Total update abortedLDAP error: Referral]" (DS 47942)
- Resolves: #1211077 - nsslapd-ndn-cache-enabled returns 1 or 0 instead of "on" or "off" (DS 408)
- Resolves: #1211006 - start/stop/restart-dirsrv utilities should ignore admin-serv directory (DS 48148)
- Resolves: #1210996 - Disable SSL v3, by default [389-ds-base-1.2.11 only] (DS 47928)
- Resolves: #1214074 - Need a way to abort a cleanallruv abort task (DS 48154)
- Resolves: #1212657 - Password is not correctly passed to perl command line tools if it contains shell special characters. (DS 48143)
- Resolves: #1218341 - ns-slapd crash related to paged results (DS 48146)

* Fri Mar 20 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-53
- Release 1.2.11.15-53
- Resolves: #1202502 - memory leak in new_passwdPolicy (1.2.11 only) (DS 48135)
- Resolves: #1202062 - Non tombstone entry which dn starting with "nsuniqueid=...," cannot be deleted (DS 48133)

* Thu Feb 19 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-52
- Release 1.2.11.15-52
- Resolves: #1193235 - Fix coverity issues and compiler warnings - 2014/12/16, 2014/11/24, 2015/2/18 (DS 47965)

* Wed Feb 18 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-51
- Release 1.2.11.15-51
- Resolves: #1193235 - Fix coverity issues and compiler warnings - 2014/12/16, 2014/11/24, 2015/2/18 (DS 47965)
- Resolves: #1171308 - Don't add unhashed password mod if we don't have an unhashed value (DS 47752)
- Resolves: #1167976 - memberof skip nested groups breaks the plugin (DS 47963)
- Resolves: #1185025 - ldclt needs to support SSL Version range (DS 47996)
- Resolves: #1183820 - Windows Sync accidentally cleared raw_entry (DS 47989)
- Resolves: #1155569 - nsslapd-db-locks modify not taking into account. (DS 47934)
- Resolves: #1145072 - Bad manipulation of passwordhistory (DS 47905)
- Resolves: #1144092 - During schema reload sometimes the search  returns no results (DS 47973)
- Resolves: #1145374 - WinSync - manual replica refresh removes AD-only member values from DS and AD in groups (DS 47884)
- Resolves: #1193243 - ldbm_usn_init: Valgrind reports Invalid read / SIGSEGV (DS 47659)
- Resolves: #1150368 - provide enabled ciphers as search result (DS 47880)
- Resolves: #1153739 - Add SSL/TLS version info to the access log (DS 47945)
- Resolves: #1118285 - Disable SSL v3, by default [389-ds-base-1.2.11 only] (DS 47928)
- Resolves: #1193241 - logconv.pl -- support parsing/showing/reporting different protocol versions (DS 47949)
- Resolves: #1179763 - COS cache doesn't properly mark vattr cache as  invalid when there are multiple suffixes (DS 47981)
- Resolves: #1175868 - Incorrect assumption in ndn cache (DS 547)
- Resolves: #1159124 - perl scripts not returning expected error code (DS 47962)
- Resolves: #1115960 - Nested COS definitions can be incorrectly  processed (DS 47980)
- Resolves: #1175868 - Backport of Normalized DN Cache (DS 408)
- Resolves: #1174892 - During delete operation do not refresh cache entry if it is a tombstone (DS 47750)
- Resolves: #1174892 - Need to refresh cache entry after called betxn postop plugins (DS 47750)
- Resolves: #1193235 - Fix coverity issues (2014/12/16) (DS 47965)
- Resolves: #1193235 - Fix coverity issues (2014/11/24) (DS 47965)
- Resolves: #1169974 - Account lockout attributes incorrectly updated after failed SASL Bind (DS 47970)
- Resolves: #1169975 - Fix coverity issue (DS 47969)
- Resolves: #1169975 - COS memory leak when rebuilding the cache (DS 47969)
- Resolves: #1170706 - cos_cache_build_definition_list does not stop during server shutdown (DS 47967)
- Resolves: #1167976 - skip nested groups breaks memberof fixup task (DS 47963)
- Resolves: #1167976 - RFE - memberOf - add option to skip nested group lookups during delete operations (DS 47963)
- Resolves: #1171357 - Bind DN tracking unable to write to internalModifiersName without special permissions (DS 47950)
- Resolves: #1162704 - Memory leak in password admin if the admin entry does not exist (DS 47958)
- Resolves: #1162704 - PasswordAdminDN attribute is not properly returned to client (DS 47952)
- Resolves: #1145379 - Fix backport issue to 1.2.11 (DS 47900)
- Resolves: #1145379 - Server fails to start if password admin is set (DS 47900)
- Resolves: #1145379 - Adding an entry with an invalid password as rootDN is incorrectly rejected (DS 47900)
- Resolves: #1141735 - ldclt: assertion failure with -e "add,counteach" -e "object=<ldif file>,rdn=uid:test[A=INCRNNOLOOP(0;24 (DS 47907)

* Tue Jan 20 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-50
- Release 1.2.11.15-50
- Resolves: #1130990 - Problem with single value attribute MMR replication (DS 47915, DS 569)

* Fri Jan  9 2015 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-49
- Release 1.2.11.15-49
- Resolves: #1168150 - CVE-2014-8105: information disclosure through 'cn=changelog' subtree
- Resolves: #1130990 - Problem with single value attribute MMR replication (DS 47915)
- Resolves: #1136882 - default nsslapd-sasl-max-buffer-size should be 2MB (DS 47457)
- Resolves: #1161909 - ACI's are replaced by "ACI_ALL" after editing goup of ACI's including invalid one (DS 47953)

* Fri Oct 24 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-48
- Release 1.2.11.15-48
- Resolves: #1154766 - ns-slapd segfault in libslapd.so.0.0.0 (#47889)

* Mon Sep 29 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-47
- Release 1.2.11.15-47
- Resolves: #1138745 - Memory leak during Reliab15 execution (#47750)

* Fri Sep 12 2014 Nathan Kinder <nkinder@redhat.com> - 1.2.11.15-46
- Release 1.2.11.15-46
- Resolves: #1138745 - Memory leak during Reliab15 execution

* Thu Sep 11 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-45
- Release 1.2.11.15-45
- Resolves: #1112702 - Broken dereference control with the FreeIPA 4.0 ACIs (#47885)

* Tue Sep  9 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-44
- Release 1.2.11.15-44
- Resolves: #1079098 - Simultaneous adding a user and binding as the user could fail in the password policy check (DS 47748) - Simple bind hangs after enabling password policy

* Fri Sep  5 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-43
- Release 1.2.11.15-43
- Resolves: #1112702 - Broken dereference control with the FreeIPA 4.0 ACIs (#47885)

* Thu Aug 21 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-42
- Release 1.2.11.15-42
- Resolves: #1129660 - Adding users to user group throws Internal server error.

* Wed Aug 20 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-41
- Release 1.2.11.15-41
- Resolves: #1130252 - dirsrv not running with old openldap (DS 47875)

* Mon Aug 18 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-40
- Release 1.2.11.15-40
- Resolves: #1130252 - dirsrv not running with old openldap (DS 47875)
- Resolves: #1103287 - logconv.pl memory continually grows (DS 47446)
- Resolves: #1121596 - Deleting attribute present in nsslapd-allowed-to-delete-attrs returns Operations error (DS 443)
- Resolves: #1109381 - winsync doesn't sync DN valued attributes if DS DN value doesn't exist (DS 415)
- Resolves: #1128759 - Performance degradation with scope ONE after some load (DS 47874)
- Resolves: #1127612 - Filter AND with only one clause should be optimized (DS 47872)
- Resolves: #1014111 - repl-monitor fails to convert "*" to default values (DS 47862)

* Tue Aug 05 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-39
- Release 1.2.11.15-39
- Resolves: #1123863
  EMBARGOED CVE-2014-3562 - unauthenticated information disclosure (Bug 1123477)
- Resolves: #1123863
  High contention on computed attribute lock (DS 616)
- Resolves: #1062763
  single valued attribute replicated ADD does not work (DS 47692)
- Resolves: #1121596
  Deleting attribute present in nsslapd-allowed-to-delete-attrs returns Operations error (DS 443)
- Resolves: #1014111
  Repl-monitor.pl ignores the provided connection parameters (DS 47862)
- Resolves: #1115281
  New defects found in 389-ds-base-1.2.11 (DS 47863)
- Resolves: #1112729
  paged results control is not working in some cases when we have a subsuffix. (DS 47824)

* Tue Jul 01 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-38
- Release 1.2.11.15-38
- Resolves: bug 1080185 - revert - Creating a glue fails if one above level is a conflict or missing (DS 47750;Patch233)

* Tue Jul 01 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-37
- Release 1.2.11.15-37
- Resolves: bug 1113606 - server restart wipes out index config if there is a default index (DS 47831)
- Resolves: bug 1112702 - Broken dereference control with the FreeIPA 4.0 ACIs (DS 47821)
- Resolves: bug 1080185 - Creating a glue fails if one above level is a conflict or missing (DS 47750)

* Mon Jun 23 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-36
- Release 1.2.11.15-36
- Resolves: bug 1088171 - revert - 7-bit check plugin does not work for userpassword attribute (DS 47423)

* Fri Jun 20 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-35
- Release 1.2.11.15-35
- Resolves: Bug 1111404 - 1.2.11 branch: coverity errors (DS 47820)

* Mon Jun 16 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-34
- Release 1.2.11.15-34
- Resolves: bug 1109952 - memory leak in ldapsearch filter objectclass=* (DS 47780)
- Resolves: bug 1109443 - Server hangs in cos_cache when adding a user entry (DS 47649)
- Resolves: bug 1109333 - 389 Server crashes if uniqueMember is invalid syntax and memberOf plugin is enabled. (DS 47793)
- Resolves: bug 1109335 - Parent numsubordinate count can be incorrectly updated if an error occurs (DS 47782)
- Resolves: bug 1109337 - Nested tombstones become orphaned after purge (DS 47767)
- Resolves: bug 1109352 - Tombstone purging can crash the server if the backend is stopped/disabled (DS 47766)
- Resolves: bug 1109356 - Coverity issue in 1.3.3 (DS 47740)
- Resolves: bug 1109358 - A tombstone entry is deleted by ldapdelete (DS 47731)
- Resolves: bug 1109361 - rsa_null_sha should not be enabled by default (DS 47637)
- Resolves: bug 1109363 - valgrind - value mem leaks, uninit mem usage (DS 47455)
- Resolves: bug 1109373 - provide default syntax plugin (DS 47369)
- Resolves: bug 1109377 - Environment variables are not passed when DS is started via service (DS 47693)
- Resolves: bug 1109379 - changelog iteration should ignore cleaned rids when getting the minCSN (DS 47627)
- Resolves: bug 1109381 - winsync doesn't sync DN valued attributes if DS DN value doesn't exist (DS 415)
- Resolves: bug 1109384 - logconv.pl man page missing -m,-M,-B,-D (DS 47447)
- Resolves: bug 1109387 - IDL-style can become mismatched during partial restoration
- Resolves: bug 1028344 - Slow ldapmodify operation time for large quantities of multi-valued attribute values (DS 346)
- Resolves: bug 985270  - [RFE] Add Password adminstrators to RHDS 9 as in http://directory.fedoraproject.org/wiki/Password_Administrator (DS 417, 458, 47522)
- Resolves: bug 1070720 - rsearch filter error on any search filter (DS 47722)
- Resolves: bug 1095847 - CoS cache re-scanning severely impacts performance (DS 47762)
- Resolves: bug 1103287 - logconv.pl memory continually grows (DS 47446)
- Resolves: bug 1106917 - managed entry plugin fails to update member  pointer on modrdn operation (DS 47813)
- Resolves: bug 1048987 - memory leak in ldapsearch filter objectclass=* (DS 47780)
- Resolves: bug 1077895 - Memory leak with proxy auth control (DS 47743)
- Resolves: bug 1079098 - Simultaneous adding a user and binding as the user could fail in the password policy check (DS 47748)
- Resolves: bug 1080185 - Creating a glue fails if one above level is a conflict or missing (DS 47750)
- Resolves: bug 1083272 - RHEL6.6 389-ds-base slapd segfault during ipa-replica-instal (DS 47448)
- Resolves: bug 1086454 - ACI warnings in error log (DS 47670)
- Resolves: bug 1086889 - empty modify returns LDAP_INVALID_DN_SYNTAX (DS 47772)
- Resolves: bug 1086901 - mem leak in do_bind when there is an error (DS 47773)
- Resolves: bug 1086903 - mem leak in do_search - rawbase not freed upon certain error (DS 47774)
- Resolves: bug 1086907 - Performing deletes during tombstone purging results in operation errors (DS 47771)
- Resolves: bug 1088171 - 7-bit check plugin does not work for userpassword attribute (DS 47423)
- Resolves: bug 1090176 - #481 breaks possibility to reassemble memberuid list (DS 47770)
- Resolves: bug 1092097 - A replicated MOD fails (Unwilling to perform) if it targets a tombstone (DS 47787)
- Resolves: bug 1094277 - IPA Server Slow Performance, high CPU usage of ns-slapd (DS 47426)
- Resolves: bug 1097002 - Problem with deletion while replicated (DS 47764)
- Resolves: bug 1098653 - db2bak.pl error with changelogdb (DS 47804)
- Resolves: bug 1103337 - find a way to remove replication plugin errors messages "changelog iteration code returned a dummy entry with csn %s, skipping ..." (DS 47809)
- Resolves: bug 1001037 - WinSync removes User must change password flag on the Window side (DS 47492)
- Resolves: bug 1004876 - idlistscanlimit per index/type/value (DS 47504)
- Resolves: bug 1008021 - Self entry access ACI not working properly (DS 47331)
- Resolves: bug 1009122 - replication stops with excessive clock skew (DS 47516)
- Resolves: bug 1012699 - DSUtil.pm needs to check $res variable (DS 422)
- Resolves: bug 1013133 - logconv.pl - RFE - track bind info (DS 356)
- Resolves: bug 1013134 - Improve memory management in logconv.pl (DS 419)
- Resolves: bug 1013135 - logconv.pl tool removes the access logs contents if "-M" is is not correctly used (DS 471)
- Resolves: bug 1013138 - logconv.pl should handle microsecond timing (DS 539)
- Resolves: bug 1013140 - logconv.pl -m not working for all stats (DS 47336)
- Resolves: bug 1013141 - logconv.pl missing stats for starttls, ldapi, and autobind (DS 611)
- Resolves: bug 1013142 - logconv.pl -m time calculation is wrong (DS 47341)
- Resolves: bug 1013152 - add etimes to per second/minute stats (DS 47348)
- Resolves: bug 1013160 - Indexed search are logged with 'notes=U' in the access logs (DS 47354)
- Resolves: bug 1013161 - improve logconv.pl performance with large access logs (DS 47387)
- Resolves: bug 1013162 - logconv warning - Use of comma-less variable list is deprecated (DS 47461)
- Resolves: bug 1013163 - logconv.pl uses /var/tmp for BDB temp files (DS 47501)
- Resolves: bug 1013164 - Fix various issues with logconv.pl (DS 47520)
- Resolves: bug 1013165 - logconv: some stats do not work across server restarts (DS 47533)
- Resolves: bug 1014111 - [RFE - RHDS9] CLI report to monitor replication (DS 47538)
- Resolves: bug 1014351 - Coverity fixes - 12023, 12024, and 12025 (DS 47540)
- Resolves: bug 1016717 - memory leak in range searches (DS 47517)
- Resolves: bug 1022500 - Winsync plugin segfault during incremental backoff (DS 47581)
- Resolves: bug 1024337 - Overflow in nsslapd-disk-monitoring-threshold on i686 (DS 47638)
- Resolves: bug 1026956 - 1.2.11.29 crash when removing entries from cache (DS 47577)
- Resolves: bug 1027496 - Replication Failures related to skipped entries due to cleaned rids (DS 47585)
- Resolves: bug 1031222 - hard coded limit of 64 masters in agreement and changelog code (DS 47587)
- Resolves: bug 1032315 - attrcrypt fails to find unlocked key (DS 47596)
- Resolves: bug 1032317 - entries with empty objectclass attribute value can be hidden (DS 47591)
- Resolves: bug 1034265 - 7-bit check plugin not checking MODRDN operation (DS 47641)
- Resolves: bug 1044106 - logconv: failed logins: Use of uninitialized value in numeric comparison at logconv.pl line 949 (DS 47550)
- Resolves: bug 1044108 - logconv: -V does not produce unindexed search report (DS 47551)
- Resolves: bug 1049029 - Windows Sync group issues (DS 47642)
- Resolves: bug 1053232 - modify-delete userpassword (DS 47678)
- Resolves: bug 1053766 - ldapdelete returns non-leaf entry error while trying to remove a leaf entry (DS 47736)
- Resolves: bug 1057805 - Size returned by slapi_entry_size is not accurate (DS 47677)
- Resolves: bug 1060385 - Logconv.pl with an empty access log gives lots of errors (DS 47713)
- Resolves: bug 1062763 - single valued attribute replicated ADD does not work (DS 47692)
- Resolves: bug 1070583 - rhds91 389-ds-base-1.2.11.15-31.el6_5.x86_64 crash in db4 _ (DS 47729)
- Resolves: bug 1073530 - Enrolling a host into IdM/IPA always takes two attempts (IPA 3377, DS 47704)
- Resolves: bug 1074076 - e_uniqueid fails to set if an entry is a conflict entry (DS 47735)
- Resolves: bug 1074305 - Under heavy stress, failure of turning a tombstone into glue (DS 47737)

* Mon May 19 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-33
- Release 1.2.11.15-33
- Resolves: bug 1044218 - fix memleak caused by 47347 (DS 47623)
- Resolves: bug 1071707 - rhds91 389-ds-base-1.2.11.15-31.el6_5 crash on paged searches followed by simple srch (DS 47707)

* Tue Mar 11 2014 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-32
- Release 1.2.11.15-32
- Resolves: bug 1074848 - EMBARGOED CVE-2014-0132 389-ds-base: 389-ds: flaw in parsing authzid can lead to privilege escalation [rhel-6.6] (Ticket 47739 - directory server is insecurely misinterpreting authzid on a SASL/GSSAPI bind)

* Mon Dec  2 2013 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-31
- Resolves: bug 1033405 - regression in ipa due to patch for ns-slapd stuck in DS_Sleep

* Mon Nov  4 2013 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-30
- Resolves: bug 1024977 CVE-2013-4485 389-ds-base: DoS due to improper handling of ger attr searches

* Tue Oct 15 2013 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-29
- Bump version to 1.2.11.15-29
- Resolves: bug 1008013:  DS91: ns-slapd stuck in DS_Sleep

* Tue Oct 8 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-28
- Bump version to 1.2.11.15-28
- Resolves: Bug 1016038 - Users from AD sub OU does not sync to IPA (ticket 47488)

* Mon Sep 30 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-27
- Bump version to 1.2.11.15-27
- Resolves: Bug 1013735 - CLEANALLRUV doesnt run across all replicas (ticket 47509)

* Fri Sep 27 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-26
- Bump version to 1.2.11.15-26
- Resolves: Bug 947583 - ldapdelete returns non-leaf entry error while trying to remove a leaf entry (ticket 47534)

* Thu Sep 26 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-25
- Bump version to 1.2.11.15-25
- Resolves: Bug 1006846 - 2Master replication with SASL/GSSAPI auth broken (ticket 47523)
- Resolves: Bug 1007452 - Under specific values of nsDS5ReplicaName, replication may get broken or updates (ticket 47489)

* Tue Sep 17 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-24
- Bump version to 1.2.11.15-24
- Resolves: Bug 982325 - Overflow in nsslapd-disk-monitoring-threshold; Changed CONFIG_INT to CONFIG_LONG for nsslapd-disk-monioring-threshold (ticket 47427)

* Wed Aug 28 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-23
- Bump version to 1.2.11.15-23
- Resolves: Bug 1000632 - CVE-2013-4283 389-ds-base: ns-slapd crash due to bogus DN
- Resolves: Bug 1002260 - server fails to start after upgrade(schema error) (ticket 47318)

* Wed Aug 07 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-22
- Bump version to 1.2.11.15-22
- Resolves: Bug 923909 - 389-ds-base cannot handle Kerberos tickets with PAC (ticket 632)
- Resolves: Bug 928159 - CVE-2013-1897 389-ds: unintended information exposure when rootdse is enabled
- Resolves: Bug 947583 - ldapdelete returns non-leaf entry error while trying to remove a leaf entry (ticket 47367)
- Resolves: Bug 951616 - error syncing group if group member user is not synced (ticket 47327)
- Resolves: Bug 953052 - DESC should not be empty as per RFC 2252 (ldapv3) (ticket 47376)
- Resolves: Bug 957305 - DS instance crashes under a high load (ticket 47349)
- Resolves: Bug 957864 - Simple paged results should support async search (ticket 47347)
- Resolves: Bug 958522 - loading an entry from the database should use str2entry_fast (ticket 531)
- Resolves: Bug 962885 - RHEL 6.2 to 6.4 ipa upgrade selinuxusermap data not replicating (ticket 47362)
- Resolves: Bug 963234 - When integrating with Red Hat IDM/DS, an LDAP protocol error is thrown (ticket 47361)
- Resolves: Bug 966781 - new ldap connections can block ldaps and ldapi connections (ticket 47359)
- Resolves: Bug 968383 - Wrong error code return when using EXTERNAL SASL and untrusted certificate (ticket 580)
- Resolves: Bug 968503 - flush_ber error sending back start_tls response will deadlock (ticket 47375)
- Resolves: Bug 969210 - make listen backlog size configurable (ticket 47377)
- Resolves: Bug 970995 - RHDS not shutting down when disk monitoring threshold is reached to half. (ticket 47385)
- Resolves: Bug 971033 - connections attribute in cn=snmp,cn=monitor is counted twice (ticket 47383)
- Resolves: Bug 971966 - 389 DS Replication failures due to Fractional updates (ticket 47386)
- Resolves: Bug 972976 - ldbm errors when adding/modifying/deleting entries (ticket 47392)
- Resolves: Bug 973583 - ns-slapd instance crashed with signal 11 SIGSEGV (ticket 47391)
- Resolves: Bug 974361 - Account policy plugin fails to lock user when policy is created for individual users to lock based to createtimestamp. (ticket 47397)
- Resolves: Bug 974719 - rhds90 crash on tombstone modrdn (ticket 47396)
- Resolves: Bug 974875 - Attributes fail to be encrypted/decrypted properly when replicated (ticket 47393)
- Resolves: Bug 975243 - DS9 still observes altStateAttrName as createTimestamp when attribute is removed from the account policy (ticket 47395)
- Resolves: Bug 975250 - Changelog deadlock replication failures with DNA (ticket 47410)
- Resolves: Bug 976546 - Attribute names are incorrect in search results (ticket 47402)
- Resolves: Bug 979169 - allow setting db deadlock rejection policy (ticket 47409)
- Resolves: Bug 979435 - Replication problem with add-delete requests on single-value (ticket 47424)
- Resolves: Bug 979515 - CVE-2013-2219 Directory Server: ACLs inoperative in some search scenarios
- Resolves: Bug 982325 - Overflow in nsslapd-disk-monitoring-threshold (ticket 47427)
- Resolves: Bug 983091 - Memory leak in 389-ds-base 1.2.11.15 (ticket 47428)
- Resolves: Bug 986131 - Very large entryusn values after enabling the USN plugin and the lastusn value is negative. (ticket 47435)
- Resolves: Bug 986424 - fix recent compiler warnings (ticket 47378)
- Resolves: Bug 986857 - Disk Monitoring not checking filesystem with logs (ticket 47441)
- Resolves: Bug 987703 - memleaks in set_krb5_creds (ticket 47421)
- Resolves: Bug 988562 - deadlock after adding and deleting entries (ticket 47449)
- Resolves: Bug 989692 - Sorting with attributes in ldapsearch gives incorrect result (ticket 543)

* Wed Aug 07 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-21
This patch is found broken and duplicated.  Getting rid of it in 1.2.11.15-22.
  commit 2b3a50d55707ffa281c922ec188850576b757934
  Author: Mark Reynolds <mreynolds@redhat.com>
  Date:   Tue Jul 23 10:28:45 2013 -0400
  Add patch 0049 for Tickets-47427-47441

* Fri Jul 26 2013 Mark Reynolds <mreynolds@redhat.com> - 1.2.11.15-20
- Resolves: Bug 984970 - Overflow in nsslapd-disk-monitoring-threshold(part 5 limits not displayed correctly). (ticket 47427)

* Thu Jul 25 2013 Mark Reynolds <mreynolds@redhat.com> - 1.2.11.15-19
- Resolves: Bug 984970 - Overflow in nsslapd-disk-monitoring-threshold(part 4). (ticket 47427)

* Thu Jul 25 2013 Mark Reynolds <mreynolds@redhat.com> - 1.2.11.15-19
- Bump version to 1.2.11.15-19
- Resolves: Bug 984970 - Overflow in nsslapd-disk-monitoring-threshold(part 3). (ticket 47427)

* Tue Jul 23 2013 Mark Reynolds <mreynolds@redhat.com> - 1.2.11.15-19
- Bump version to 1.2.11.15-19
- Resolves: Bug 982325 - Overflow in nsslapd-disk-monitoring-threshold(part 2). (ticket 47427)
- Resolves: Bug 986857 - Disk Monitoring not checking filesystem with logs (ticket 47741)

* Mon Jul 15 2013 Mark Reynolds <mreynolds@redhat.com> - 1.2.11.15-18
- Bump version to 1.2.11.15-18
- Resolves: Bug 970995 - DS not shutting down when disk monitoring threshold is reached to half. (Ticket 47385)
- Resolves: Bug 982325 - Overflow in nsslapd-disk-monitoring-threshold. (ticket 47427)

* Wed Apr 10 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-14
- Resolves: Bug 921937 - ns-slapd crashes sporadically with segmentation fault in libslapd.so (ticket 627)
- Resolves: Bug 923503 - cleanAllRUV task fails to cleanup config upon completion (ticket 623)

* Thu Mar 28 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-13
bump version to 1.2.11.15-13
- Resolves: Bug 923503 - cleanAllRUV task fails to cleanup config upon completion (ticket 623)
- Resolves: Bug 923502 - Coverity issue 13091
- Resolves: Bug 923407 - Deadlock in DNA plug-in (ticket 634)
- Resolves: Bug 921937 - ns-slapd crashes sporadically with segmentation fault in libslapd.so (ticket 627)
- Resolves: Bug 923504 - crash in aci evaluation (ticket 628)
- Resolves: Bug 928159 - unintended information exposure when anonymous access is set to rootdse (ticket 47308)

* Fri Feb 22 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-12
- Resolves: Bug 910581 - dse.ldif is 0 length after server kill or machine kill
- Resolves: Bug 908861 - Error messages encountered when using POSIX winsync
- Resolves: Bug 907985 - DNA: use event queue for config update only at the start up
- Resolves: Bug 830334 - Invalid chaining config triggers a disk full error and shutdown
- Resolves: Bug 906583 - DS returns error 20 when replacing values of a multi-valued attribute  (only when replication is enabled)
- Resolves: Bug 906005 - Valgrind reports memleak in modify_update_last_modified_attr
- Resolves: Bug 905825 - PamConfig schema not updated during upgrade
- Resolves: Bug 913215 - ns-slapd segfaults while trying to delete a tombstone entry
- Resolves: Bug 913229 - unauthenticated denial of service vulnerability in handling of LDAPv3 control data

* Mon Jan 21 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-11
- Resolves: Bug 896256 - updating package touches configuration files

* Tue Jan 08 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-10
- Resolves: Bug 889083 - For modifiersName/internalModifiersName feature, internalModifiersname is not working for DNA plugin

* Fri Jan 04 2013 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-9
- Resolves: Bug 891930 - DNA plugin no longer reports additional info when range is depleted

* Tue Dec 18 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-8
- Resolves: Bug 887855 - RootDN Access Control plugin is missing after upgrade from RHEL63 to RHEL64

* Fri Dec 07 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.11.15-7
- Resolves: Bug 830355 - [RFE] improve cleanruv functionality 
- Resolves: Bug 876650 - Coverity revealed defects 
- Ticket #20 - [RFE] Allow automember to work on entries that have already been added (Bug 768084)
- Resolves: Bug 834074 - [RFE] Disable replication agreements
- Resolves: Bug 878111 - ns-slapd segfaults if it cannot rename the logs 

* Thu Nov 29 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-6
- Resolves: Bug 880305 - spec file missing dependencies for x86_64 6ComputeNode
-   use perl-Socket6 on RHEL6

* Tue Nov 27 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-5
- Resolves: Bug 880305 - spec file missing dependencies for x86_64 6ComputeNode

* Fri Nov 16 2012 Noriko Hosoi <nhoso@redhat.com> - 1.2.11.15-4
- Resolves: Bug 868841 - Newly created users with organizationalPerson objectClass fails to sync from AD to DS with missing attribute error
- Resolves: Bug 868853 - Winsync: DS error logs report wrong version of Windows AD when winsync is configured.
- Resolves: Bug 875862 - crash in DNA if no dnamagicregen is specified
- Resolves: Bug 876694 - RedHat Directory Server crashes (segfaults) when moving ldap entry
- Resolves: Bug 876727 - Search with a complex filter including range search is slow
- Ticket #495 - internalModifiersname not updated by DNA plugin (Bug 834053)

* Mon Nov  5 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-3
- Resolves: Bug 870158 - slapd entered to infinite loop during new index addition
- Resolves: Bug 870162 - Cannot abandon simple paged result search
- c970af0 Coverity defects
- 1ac087a Fixing compiler warnings in the posix-winsync plugin
- 2f960e4 Coverity defects
- Ticket #491 - multimaster_extop_cleanruv returns wrong error codes

* Tue Oct  9 2012 Noriko Hosoi<nhosoi@redhat.com> - 1.2.11.15-2
- Resolves: Bug 834063 [RFE] enable attribute that tracks when a password was last set on an entry in the LDAP store; Ticket #478 passwordTrackUpdateTime stops working with subtree password policies 
- Resolves: Bug 847868 [RFE] support posix schema for user and group sync; Ticket #481 expand nested posix groups
- Resolves: Bug 860772 Change on SLAPI_MODRDN_NEWSUPERIOR is not evaluated in acl 
- Resolves: Bug 863576 Dirsrv deadlock locking up IPA
- Resolves: Bug 864594 anonymous limits are being applied to directory manager

* Tue Sep 25 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.15-1
- Resolves: Bug 856657 dirsrv init script returns 0 even when few or all instances fail to start
- Resolves: Bug 858580 389 prevents from adding a posixaccount with userpassword after schema reload

* Fri Sep 14 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.14-1
- Resolves: Bug 852202 Ipa master system initiated more than a dozen simultaneous replication sessions, shut itself down and wiped out its db
- Resolves: Bug 855438 CLEANALLRUV task gets stuck on winsync replication agreement

* Tue Sep  4 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.13-1
- Resolves: Bug 847868 [RFE] support posix schema for user and group sync
-  fix upgrade issue with plugin config schema
-  posix winsync has default plugin precedence of 25

* Fri Aug 31 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.11.12-1
- Resolves: Bug 800051 Rebase 389-ds-base to 1.2.11
- Resolves: Bug 742054 SASL/PLAIN binds do not work 
- Resolves: Bug 742381 MOD operations with chained delete/add get back error 53 on backend config
- Resolves: Bug 746642 [RFE] define pam_passthru service per subtree
- Resolves: Bug 757836 logconv.pl restarts count on conn=0 instead of conn=1
- Resolves: Bug 768084 [RFE] Allow automember to work on entries that have already been added
- Resolves: Bug 782975 krbExtraData is being null modified and replicated on each ssh login
- Resolves: Bug 803873 Sync with group attribute containing () fails
- Resolves: Bug 818762 winsync should not delete entry that appears to be out of scope
- Resolves: Bug 830001 unhashed#user#password visible after changing password [rhel-6.4]
- Resolves: Bug 830256 Audit log - clear text password in user changes
- Resolves: Bug 830331 ns-slapd exits/crashes if /var fills up
- Resolves: Bug 830334 Invalid chaining config triggers a disk full error and shutdown
- Resolves: Bug 830335 restore of replica ldif file on second master after deleting two records shows only 1 deletion
- Resolves: Bug 830336 db deadlock return should not log error
- Resolves: Bug 830337 usn + mmr = deletions are not replicated
- Resolves: Bug 830338 Change DS to purge ticket from krb cache in case of authentication error
- Resolves: Bug 830340 Make the CLEANALLRUV task one step
- Resolves: Bug 830343 managed entry sometimes doesn't delete the managed entry
- Resolves: Bug 830344 [RFE] Improve replication agreement status messages
- Resolves: Bug 830346 ADD operations not in audit log
- Resolves: Bug 830347 389 DS does not support multiple paging controls on a single connection
- Resolves: Bug 830348 Slow shutdown when you have 100+ replication agreements
- Resolves: Bug 830349 cannot use & in a sasl map search filter
- Resolves: Bug 830353 valgrind reported memleaks and mem errors
- Resolves: Bug 830355 [RFE] improve cleanruv functionality
- Resolves: Bug 830356 coverity 12625-12629 - leaks, dead code, unchecked return
- Resolves: Bug 832560 [abrt] 389-ds-base-1.2.10.6-1.fc16: slapi_attr_value_cmp: Process /usr/sbin/ns-slapd was killed by signal 11 (SIGSEGV)
- Resolves: Bug 833202 transaction retries need to be cache aware
- Resolves: Bug 833218 ldapmodify returns Operations error
- Resolves: Bug 833222 memberOf attribute and plugin behaviour between sub-suffixes
- Resolves: Bug 834046 [RFE] Add nsTLS1 attribute to schema and objectclass nsEncryptionConfig
- Resolves: Bug 834047 Fine Grained Password policy: if passwordHistory is on, deleting the password fails.
- Resolves: Bug 834049 [RFE] Add schema for DNA plugin
- Resolves: Bug 834052 [RFE] limiting Directory Manager (nsslapd-rootdn) bind access by source host (e.g. 127.0.0.1)
- Resolves: Bug 834053 [RFE] Plugins - ability to control behavior of modifyTimestamp/modifiersName
- Resolves: Bug 834054 Should only update modifyTimestamp/modifiersName on MODIFY ops
- Resolves: Bug 834056 Automembership plugin fails in a MMR setup, if data and config area mixed in the plugin configuration
- Resolves: Bug 834057 ldap-agent crashes on start with signal SIGSEGV
- Resolves: Bug 834058 [RFE] logconv.pl : use of getopts to parse commandline options
- Resolves: Bug 834060 passwordMaxFailure should lockout password one sooner - and should be configurable to avoid regressions
- Resolves: Bug 834061 [RFE] RHDS: Implement SO_KEEPALIVE in network calls.
- Resolves: Bug 834063 [RFE] enable attribute that tracks when a password was last set on an entry in the LDAP store
- Resolves: Bug 834064 dnaNextValue gets incremented even if the user addition fails
- Resolves: Bug 834065 Adding Replication agreement should complain if required nsds5ReplicaCredentials not supplied
- Resolves: Bug 834074 [RFE] Disable replication agreements
- Resolves: Bug 834075 logconv.pl reporting unindexed search with different search base than shown in access logs
- Resolves: Bug 835238 Account Usability Control Not Working
- Resolves: Bug 836386 slapi_ldap_bind() doesn't check bind results
- Resolves: Bug 838706 referint modrdn not working if case is different
- Resolves: Bug 840153 Impossible to rename entry (modrdn) with Attribute Uniqueness plugin enabled
- Resolves: Bug 841600 Referential integrity plug-in does not work when update interval is not zero
- Resolves: Bug 842437 dna memleak reported by valgrind
- Resolves: Bug 842438 Report during startup if nsslapd-cachememsize is too small
- Resolves: Bug 842440 memberof performance enhancement
- Resolves: Bug 842441 "Server is unwilling to perform" when running ldapmodify on nsds5ReplicaStripAttrs
- Resolves: Bug 847868 [RFE] support posix schema for user and group sync
- Resolves: Bug 850683 nsds5ReplicaEnabled can be set with any invalid values.
- Resolves: Bug 852087 [RFE] add attribute nsslapd-readonly so we can reference it in acis
- Resolves: Bug 852088 server to server ssl client auth broken with latest openldap
- Resolves: Bug 852839 variable dn should not be used in ldbm_back_delete

* Thu Jun 28 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-20
- Resolves: Bug 835238 - Account Usability Control Not Working

* Wed Jun 20 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-19
- Resolves: Bug 834096 - slapi_attr_value_cmp: Process /usr/sbin/ns-slapd was killed by signal 11 (SIGSEGV)

* Tue Jun 12 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-18
- Resolves: Bug 830001 - unhashed#user#password visible after changing password
-- patch 0020 disallows users' direct modify on unhashed#user#password

* Mon Jun 11 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-17
- Resolves: Bug 830001 - unhashed#user#password visible after changing password
-- patch 0019 fixes deref issue.

* Fri Jun 08 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-16
- Resolves: Bug 830001 - unhashed#user#password visible after changing password
- Resolves: Bug 830256 - Audit log - clear text password in user changes

* Tue May 22 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-15
- Resolves: Bug 824014 - DS Shuts down intermittently

* Fri May 18 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-14
- Resolves: Bug 819643 - Database RUV could mismatch the one in changelog under the stress
-- patch 0015 fixes a small memleak in previous patch

* Thu May 17 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-13
- Resolves: Bug 822700 - Bad DNs in ACIs can segfault ns-slapd

* Mon May 14 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-12
- Resolves: Bug 819643 - Database RUV could mismatch the one in changelog under the stress
- Resolves: Bug 821542 - letters in object's cn get converted to lowercase when renaming object

* Thu May 10 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-11
- Resolves: Bug 819643 - Database RUV could mismatch the one in changelog under the stress
- 1.2.10.2-10 was built from the private branch

* Wed May  9 2012 Noriko Hosoi <nhosoi@redhat.com> - 1.2.10.2-10
- Resolves: Bug 819643 - Database RUV could mismatch the one in changelog under the stress

* Thu May  3 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-9
- Resolves: Bug 815991 - crash in ldap_initialize with multiple threads
-  previous fix was still crashing in ldclt

* Mon Apr 30 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-8
- Resolves: Bug 815991 - crash in ldap_initialize with multiple threads

* Tue Apr 24 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-7
- Resolves: Bug 813964 - IPA dirsvr seg-fault during system longevity test

* Tue Apr 10 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-6
- Resolves: Bug 811291 - [abrt] 389-ds-base-1.2.10.4-2.fc16: index_range_read_ext: Process /usr/sbin/ns-slapd was killed by signal 11 (SIGSEGV)
- typo in previous patch

* Tue Apr 10 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-5
- Resolves: Bug 811291 - [abrt] 389-ds-base-1.2.10.4-2.fc16: index_range_read_ext: Process /usr/sbin/ns-slapd was killed by signal 11 (SIGSEGV)

* Wed Mar 21 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-4
- Resolves: Bug 803930 - ipa not starting after upgade because of missing data
- get rid of posttrans - move update code to post

* Tue Mar 13 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-3
- Resolves: Bug 800215 - Certain CMP operations hang or cause ns-slapd to crash 

* Tue Mar  6 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-2
- Resolves: Bug 800215 - Certain CMP operations hang or cause ns-slapd to crash 
- Resolves: Bug 800217 - fix valgrind reported issues

* Thu Feb 23 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.2-1
- Resolves: Bug 766989 - Rebase 389-ds-base to 1.2.10
- Resolves: Bug 796770 - crash when replicating orphaned tombstone entry

* Tue Feb 14 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.1-1
- Resolves: Bug 766989 - Rebase 389-ds-base to 1.2.10
- Resolves: Bug 790491 - 389 DS Segfaults during replica install in FreeIPA

* Mon Feb 13 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10.0-1
- Resolves: Bug 766989 - Rebase 389-ds-base to 1.2.10

* Mon Feb  6 2012 Rich Megginson <rmeggins@redhat.com> - 1.2.10-0.11.rc2
- Resolves: Bug 766989 - Rebase 389-ds-base to 1.2.10

* Mon Dec 19 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.16-1
- Bug 759301 - Incorrect entryUSN index under high load in replicated environment
- Bug 743979 - Add slapi_rwlock API and use POSIX rwlocks
- WARNING - patches 0030 and 0031 remove and add back the file configure
- this is necessary because the merge commit to "rebase" RHEL-6 to 1.2.9.6
- seriously messed up configure - so in order to add the patch for 743979
- which also touched configure, the file had to be removed and added back
- also note that the commit for the RHEL-6 branch to remove configure does
- not work - the way patch works, it has to match every line exactly in
- order to remove the file, and because the merge commit messed things
- up, it doesn't work
- So, DO NOT TOUCH 0030-remove-configure-to-get-rid-of-merge-conflict.patch
- BECAUSE IT IS HAND CRAFTED and not generated by git format-patch
- if you must regenerate this file,
- git format-patch ...args... to generate a file in patch format
- remove all of the patch matches (all the lines beginning with -)
- get the 1.2.9.6 version of configure from the source tarball
- wc -l configure to get the number of lines in the file
- sed 's/^/-/' configure >> thefile.patch
- edit thefile.patch to have the right number of lines and have the
- patch commands in the correct place
- PROFIT!!!

* Mon Nov 28 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.15-1
- Bug 752577 - crash when simple paged fails to send entry to client
- Bug 757897 - rhds81 modrn operation and 100% cpu use in replication
- Bug 757898 - Fix Coverity (11104) Resource leak: ids_sasl_user_to_entry (slapd/saslbind.c)

* Tue Nov  8 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.14-1
- Bug 752155 - Use restorecon after creating init script lock file

* Thu Oct  6 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.13-1
- Bug 742381 - part3 - MOD operations with chained delete/add get
-  back error 53 on backend config

* Mon Oct  3 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.12-2
- add the actual patch commands for the new patch files

* Mon Oct  3 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.12-1
- Bug 742661 - allow resource limits to be set for paged searches
-  independently of limits for other searches/operations
- Bug 742381 - part2 - MOD operations with chained delete/add get
-  back error 53 on backend config
- Bug 742382 - allow nsslapd-idlistscanlimit to be set dynamically and per-user
- Bug 742381 - MOD operations with chained delete/add get back
-  error 53 on backend config
- Bug 739959 - Allow separate fractional attrs for incremental and total protocols

* Fri Sep 16 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.11-1
- Bug 739196 - Consolidate DS and DS replication bits in one package in RHEL 6.2
- There were two patches in ds-replication for RHEL 6.2 that were added post
- rebase - the two patches for 722292 - these are now in the 389-ds-base package
- and have been cherry-picked to the RHEL-6 internal branch

* Wed Sep  7 2011 Nathan Kinder <nkinder@redhat.com> - 1.2.9.10-1
- Bug 736137 - renaming a managed entry does not update mepmanagedby

* Thu Sep  1 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.9-1
- Bug 735217 - simple paged search + ip/dns based ACI hangs server

* Wed Aug 31 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.8-1
- Bug 733443 - large targetattr list with syntax errors cause server to crash or hang
- Bug 734267 - upgradednformat failed to add RDN value - subtree and user account lockout policies implemented?
- Bug 733434 - passwordisglobalpolicy attribute brakes TLS chaining
- Bug 733442 - Ignore an error 32 in this case since we're adding a new AutoMember definition
- Bug 733440 - RFE: add option to allow server to start with an expired certificate

* Wed Aug 24 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.7-1
- not released internally

* Wed Aug 10 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.6-1
- Bug 728510 - Run dirsync after sending updates to AD
- Bug 729717 - Fatal error messages when syncing deletes from AD
- Bug 729369 - upgrade DB to upgrade from entrydn to entryrdn format is not working.
- Bug 729378 - delete user subtree container in AD + modify password in DS == DS crash
- Bug 723937 - Slapi_Counter API broken on  32-bit F15
-   fixed again - separate tests for atomic ops and atomic bool cas

* Mon Aug  8 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.5-1
- Bug 727511 - ldclt SSL search requests are failing with "illegal error number -1" error
-  Fix another coverity NULL deref in previous patch

* Thu Aug  4 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.4-1
- Bug 727511 - ldclt SSL search requests are failing with "illegal error number -1" error
-  Fix coverity NULL deref in previous patch

* Wed Aug  3 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.3-1
- Bug 727511 - ldclt SSL search requests are failing with "illegal error number -1" error
-  previous patch broke build on el5

* Wed Aug  3 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.2-1
- Bug 727511 - ldclt SSL search requests are failing with "illegal error number -1" error

* Tue Aug  2 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.1-2
- Bug 723937 - Slapi_Counter API broken on  32-bit F15
-   fixed to use configure test for GCC provided 64-bit atomic functions

* Wed Jul 27 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.9.1-1
- Bug 663752 - Cert renewal for attrcrypt and encchangelog
-   this was "re-fixed" due to a deadlock condition with cl2ldif task cancel
- Bug 725953 - Winsync: DS entries fail to sync to AD, if the User's CN entry contains a comma
- Bug 725743 - Make memberOf use PRMonitor for it's operation lock
- Bug 725542 - Instance upgrade fails when upgrading 389-ds-base package
- Bug 723937 - Slapi_Counter API broken on  32-bit F15
- look for separate openldap ldif library
- Split automember regex rules into separate entries
- writing Inf file shows SchemaFile = ARRAY(0xhexnum)
- add support for ldif files with changetype: add
- Bug 703703 - setup-ds-admin.pl asks for legal agreement to a non-existant file
- Bug 713209 - Update sudo schema
- Bug 719069 - clean up compiler warnings in 389-ds-base 1.2.9

* Wed Jul 27 2011 Nathan Kinder <nkinder@redhat.com> - 1.2.8.7-1
- Bug 726136 - memberOf plug-in can deadlock when used with other plug-ins
- Bug 725912 - Instance upgrade fails when upgrading 389-ds-base package

* Mon Jul 11 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.6-1
- Bug 720452 - RDN with % can cause crashes or missing entries
- Bug 720051 - RSA Authentication Server timeouts when using simple paged results on RHDS 8.2.
- Bug 720458 - Directory Server 8.2 logs "Netscape Portable Runtime error -5961 (TCP connection reset by peer.)" to error log whereas Directory Server 8.1 did not
- Bug 720459 - Update sudo schema

* Fri Jul  1 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.5-1
- Bug 718351 - Intensive updates on masters could break the consumer's cache
- Bug 714298 - unresponsive LDAP service when deleting vlv on replica

* Tue Jun 21 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.4-3
- Bug 714298 - unresponsive LDAP service when deleting vlv on replica - memleak in previous patch

* Mon Jun 20 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.4-2
- Bug 714298 - unresponsive LDAP service when deleting vlv on replica

* Fri Jun 17 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.4-1
- Bug 706209 - LEGAL: RHEL6.1 License issue for 389-ds-base package
- Bug 713317 - Cert renewal for attrcrypt and encchangelog
- Bug 711266 - DS can not restart after create a new objectClass has entryusn attribute
- Bug 712167 - ns-slapd segfaults using suffix referrals
- Bug 709868 - only allow FIPS approved cipher suites in FIPS mode
- Bug 711516 - Support upgrade from Red Hat Directory Server
- Bug 711241 - memory leak found by reliab12
- Bug 711265 - Cannot disable SSLv3 and use TLS only
- Bug 711513 - slapd stops responding

* Wed May 18 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.3-4
- Resolves: Bug 705172 - 389-ds should only be supported and supplied in channels for i386 and x86_64 Server distributions - RHEL 6.1 0day Advisory
- use ix86 macro instead of hardcoded i386 etc.

* Wed May 18 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.3-3
- Resolves: Bug 705172 - 389-ds should only be supported and supplied in channels for i386 and x86_64 Server distributions - RHEL 6.1 0day Advisory
- cannot use wildcard in ExclusiveArch

* Wed May 18 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.3-2
- Resolves: Bug 705172 - 389-ds should only be supported and supplied in channels for i386 and x86_64 Server distributions - RHEL 6.1 0day Advisory

* Mon May  2 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.3-1
- Resolves: Bug 697663 - memory leak: entryusn value is leaked when an entry is deleted
- Resolves: Bug 699458 - windows sync can lose old multi-valued attribute values when a new value is added
- Resolves: Bug 700215 - ldclt core dumps
- Resolves: Bug 700665 - Linked attributes callbacks access free'd pointers after close
- Resolves: Bug 701057 - userpasswd not replicating

* Thu Apr 14 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.2-1
- 389-ds-base-1.2.8.2
- Bug 696407 - If an entry with a mixed case RDN is turned to be
-    a tombstone, it fails to assemble DN from entryrdn

* Fri Apr  8 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.1-1
- 389-ds-base-1.2.8.1
- Bug 693962 - Full replica push loses some entries with multi-valued RDNs

* Tue Apr  5 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.0-2
- added srcver because the version from the source is now
- different than the source in the package

* Tue Apr  5 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8.0-1
- 389-ds-base-1.2.8.0
- Bug 693523 - Unable to change schema online
- Bug 693520 - matching rules do not inherit from superior attribute type
- Bug 693522 - nsMatchingRule does not work with multiple values
- Bug 693519 - cannot use localized matching rules
- Bug 693516 - Segfault on index update during full replication push on 1.2.7.5

* Tue Mar 29 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.9.rc4
- Bug 668385 - DS pipe log script is executed as many times as the dirsrv service is restarted
- bump version to 1.2.8.rc4 - bump ds console version to 1.2.5

* Mon Mar 28 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.8.rc2
- Bug 690536 - Double free in dse_add()

* Tue Mar 22 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.7.rc2
- 389-ds-base-1.2.8 release candidate 2 - git tag 389-ds-base-1.2.8.rc2
- Bug 689908 - (cov#10610) Fix Coverity NULL pointer dereferences
- Bug 689895 - ns-newpwpolicy.pl needs to use the new DN format
- Bug 689889 - RFE: allow fine grained password policy duration attributes
-              in days, hours, minutes, as well
- Bug 688730 - Exported tombstone cannot be imported correctly
- Bug 684349 - slapd crashing when traffic replayed
- Bug 682897 - Allow maxlogsize to be set if logmaxdiskspace is -1
- introduce the concept of the srcprerel - with rc2, we did not rebase
- the source, we are still using the .rc1 source tarball, so we use
- srcprerel of .rc1 but package pre-release is .rc2

* Wed Mar  2 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.6.rc1
- 389-ds-base-1.2.8 release candidate 1 - git tag 389-ds-base-1.2.8.rc1
- Resolves: Bug 680575 - Rebase 389-ds-base to pick the latest features and fixes 
- Resolves: Bug 681720 - setup-ds-admin.pl - improve hostname validation
- Resolves: Bug 681611 - RFE: allow fine grained password policy duration attributes in 
-     days, hours, minutes, as well
- Resolves: Bug 681550 - setup-ds-admin.pl --debug does not log to file
- Resolves: Bug 681379 - ns-slapd segfaults if I have more than 100 DBs
- Resolves: Bug 680290 - setup-ds.pl should set SuiteSpotGroup automatically
- Resolves: Bug 681351 - crash in ldap-agent when using OpenLDAP
- Resolves: Bug 681332 - modifying attr value crashes the server, which is supposed to
-     be indexed as substring type, but has octetstring syntax
- Resolves: Bug 680305 - ds-logpipe.py script is failing to validate "-s" and
-     "--serverpid" options with "-t".

* Mon Feb 28 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.5.a3
- Bug 676598 - 389-ds-base multilib: file conflicts
- split off libs into a separate -libs package
- remove old crufty fedora-ds stuff

* Thu Feb 24 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.4.a3
- do not create /var/run/dirsrv - setup will create it instead
- remove the fedora-ds initscript upgrade stuff - we do not support that anymore
- convert the remaining lua stuff to plain old shell script

* Wed Feb  9 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.3.a3
- 1.2.8.a3 release - git tag 389-ds-base-1.2.8.a3
- Bug 675320 - empty modify operation with repl on or lastmod off will crash server
- Bug 675265 - preventryusn gets added to entries on a failed delete
- Bug 677774 - added support for tmpfiles.d
- Bug 666076 - dirsrv crash (1.2.7.5) with multiple simple paged result search
es
- Bug 672468 - Don't use empty path elements in LD_LIBRARY_PATH
- Bug 671199 - Don't allow other to write to rundir
- Bug 678646 - Ignore tombstone operations in managed entry plug-in
- Bug 676053 - export task followed by import task causes cache assertion
- Bug 677440 - clean up compiler warnings in 389-ds-base 1.2.8
- Bug 675113 - ns-slapd core dump in windows_tot_run if oneway sync is used
- Bug 676689 - crash while adding a new user to be synced to windows
- Bug 604881 - admin server log files have incorrect permissions/ownerships
- Bug 668385 - DS pipe log script is executed as many times as the dirsrv serv
ice is restarted
- Bug 675853 - dirsrv crash segfault in need_new_pw()

* Thu Feb  3 2011 Rich Megginson <rmeggins@redhat.com> - 1.2.8-0.2.a2
- 1.2.8.a2 release - git tag 389-ds-base-1.2.8.a2
- Errata Patches in patch files
- Bug 666076 - dirsrv crash (1.2.7.5) with multiple simple paged result searches
- Bug 671199 - Don't allow other to write to rundir
- Bug 672468 - Don't use empty path elements in LD_LIBRARY_PATH
- bugs fixed in released code
- Bug 674430 - Improve error messages for attribute uniqueness
- Bug 616213 - insufficient stack size for HP-UX on PA-RISC
- Bug 615052 - intrinsics and 64-bit atomics code fails to compile
-    on PA-RISC
- Bug 151705 - Need to update Console Cipher Preferences with new ciphers
- Bug 668862 - init scripts return wrong error code
- Bug 670616 - Allow SSF to be set for local (ldapi) connections
- Bug 667935 - DS pipe log script's logregex.py plugin is not redirecting the 
-    log output to the text file
- Bug 668619 - slapd stops responding
- Bug 624547 - attrcrypt should query the given slot/token for
-    supported ciphers
- Bug 646381 - Faulty password for nsmultiplexorcredentials does not give any 
-    error message in logs

* Fri Jan 21 2011 Nathan Kinder <nkinder@redhat.com> - 1.2.8-0.1.a1
- 1.2.8-0.1.a1 release
- many bug fixes

* Fri Dec 17 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7.5-1
- 1.2.7.5 release - git tag 389-ds-base-1.2.7.5
- Bug 663597 - Memory leaks in normalization code

* Fri Dec 10 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7.4-1
- 1.2.7.4 release - git tag 389-ds-base-1.2.7.4
- Bug 661792 - Valid managed entry config rejected

* Wed Dec  8 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7.3-1
- 1.2.7.3 release - git tag 389-ds-base-1.2.7.3
- Bug 658312 - Invalid free in Managed Entry plug-in
- Bug 641944 - Don't normalize non-DN RDN values

* Fri Dec  3 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7.2-1
- 1.2.7.2 release - git tag 389-ds-base-1.2.7.2
- Bug 659456 - Incorrect usage of ber_printf() in winsync code
- Bug 658309 - Process escaped characters in managed entry mappings
- Bug 197886 - Initialize return value for UUID generation code
- Bug 658312 - Allow mapped attribute types to be quoted
- Bug 197886 - Avoid overflow of UUID generator

* Tue Nov 23 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7.1-1
- 1.2.7.1 release - git tag 389-ds-base-1.2.7.1
- Bug 656515 - Allow Name and Optional UID syntax for grouping attributes
- Bug 656392 - Remove calls to ber_err_print()
- Bug 625950 - hash nsslapd-rootpw changes in audit log

* Tue Nov 16 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-1
- the 1.2.7 release
- remove the ds-replication sub-package - there will be a new package for it
- remove the selinux policy - dirsrv policy will be provided by the base OS

* Wed Nov  3 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.7.a5
- create ds-replication sub package

* Tue Nov  2 2010 Kevin Wright <kwright@redhat.com> - 1.2.7-0.6.a4
- bumped the version to get it to build in brew

* Mon Nov  1 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.5.a4
- 1.2.7.a4 release - git tag 389-ds-base-1.2.7.a4
- Bug 647932 - multiple memberOf configuration adding memberOf where there is 
no member
- Bug 491733 - dbtest crashes
- Bug 606545 - core schema should include numSubordinates
- Bug 638773 - permissions too loose on pid and lock files
- Bug 189985 - Improve attribute uniqueness error message
- Bug 619623 - attr-unique-plugin ignores requiredObjectClass on modrdn operat
ions
- Bug 619633 - Make attribute uniqueness obey requiredObjectClass

* Wed Oct 27 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.4.a3
- 1.2.7.a3 release - a2 was never released - this is a rebuild to pick up
- Bug 644608 - RHDS 8.1->8.2 upgrade fails to properly migrate ACIs
- Adding the ancestorid fix code to ##upgradednformat.pl.

* Fri Oct 22 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.3.a3
- 1.2.7.a3 release - a2 was never released
- Bug 644608 - RHDS 8.1->8.2 upgrade fails to properly migrate ACIs
- Bug 629681 - Retro Changelog trimming does not behave as expected
- Bug 645061 - Upgrade: 06inetorgperson.ldif and 05rfc4524.ldif
-              are not upgraded in the server instance schema dir

* Tue Oct 19 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.2.a2
- 1.2.7.a2 release - a1 was the OpenLDAP testday release
- git tag 389-ds-base-1.2.7.a2
- added openldap support on platforms that use openldap with moznss
- for crypto (F-14 and later)
- many bug fixes
- Account Policy Plugin (keep track of last login, disable old accounts)

* Fri Oct  8 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.7-0.1.a1
- added openldap support

* Wed Sep 29 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6.1-3
- bump rel to rebuild again

* Mon Sep 27 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6.1-2
- bump rel to rebuild

* Thu Sep 23 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6.1-1
- This is the 1.2.6.1 release - git tag 389-ds-base-1.2.6.1
- Bug 634561 - Server crushes when using Windows Sync Agreement
- Bug 635987 - Incorrect sub scope search result with ACL containing ldap:///self
- Bug 612264 - ACI issue with (targetattr='userPassword')
- Bug 606920 - anonymous resource limit- nstimelimit - also applied to "cn=directory manager"
- Bug 631862 - crash - delete entries not in cache + referint

* Thu Aug 26 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-1
- This is the final 1.2.6 release

* Tue Aug 10 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.11.rc7
- 1.2.6 release candidate 7
- git tag 389-ds-base-1.2.6.rc7
- Bug 621928 - Unable to enable replica (rdn problem?) on 1.2.6 rc6

* Mon Aug  2 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.10.rc6
- 1.2.6 release candidate 6
- git tag 389-ds-base-1.2.6.rc6
- Bug 617013 - repl-monitor.pl use cpu upto 90%
- Bug 616618 - 389 v1.2.5 accepts 2 identical entries with different DN formats
- Bug 547503 - replication broken again, with 389 MMR replication and TCP errors
- Bug 613833 - Allow dirsrv_t to bind to rpc ports
- Bug 612242 - membership change on DS does not show on AD
- Bug 617629 - Missing aliases in new schema files
- Bug 619595 - Upgrading sub suffix under non-normalized suffix disappears
- Bug 616608 - SIGBUS in RDN index reads on platforms with strict alignments
- Bug 617862 - Replication: Unable to delete tombstone errors
- Bug 594745 - Get rid of dirsrv_lib_t label

* Wed Jul 14 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.9.rc3
- make selinux-devel explicit Require the base package in order
- to comply with Fedora Licensing Guidelines

* Thu Jul  1 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.8.rc3
- 1.2.6 release candidate 3
- git tag 389-ds-base-1.2.6.rc3
- Bug 603942 - null deref in _ger_parse_control() for subjectdn
- 609256  - Selinux: pwdhash fails if called via Admin Server CGI
- 578296  - Attribute type entrydn needs to be added when subtree rename switch is on
- 605827 - In-place upgrade: upgrade dn format should not run in setup-ds-admin.pl
- Bug 604453 - SASL Stress and Server crash: Program quits with the assertion failure in PR_Poll
- Bug 604453 - SASL Stress and Server crash: Program quits with the assertion failure in PR_Poll
- 606920 - anonymous resource limit - nstimelimit - also applied to "cn=directory manager"

* Wed Jun 16 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.7.rc2
- 1.2.6 release candidate 2

* Mon Jun 14 2010 Nathan Kinder <nkinder@redhat.com> - 1.2.6-0.6.rc1
- install replication session plugin header with devel package

* Wed Jun  9 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.5.rc1
- 1.2.6 release candidate 1

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.2.6-0.4.a4.1
- Mass rebuild with perl-5.12.0

* Wed May 26 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.4.a4
- 1.2.6.a4 release

* Wed Apr  7 2010 Nathan Kinder <nkinder@redhat.com> - 1.2.6-0.4.a3
- 1.2.6.a3 release
- add managed entries plug-in
- many bug fixes
- moved selinux subpackage into base package

* Fri Apr  2 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.6-0.3.a2
- rebuild for icu 4.4

* Tue Mar  2 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.6-0.2.a2
- 1.2.6.a2 release
- add support for matching rules
- many bug fixes

* Thu Jan 14 2010 Nathan Kinder <nkinder@redhat.com> - 1.2.6-0.1.a1
- 1.2.6.a1 release
- Added SELinux policy and subpackages

* Tue Jan 12 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.5-1
- 1.2.5 final release

* Mon Jan  4 2010 Rich Megginson <rmeggins@redhat.com> - 1.2.5-0.5.rc4
- 1.2.5.rc4 release

* Thu Dec 17 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.5-0.4.rc3
- 1.2.5.rc3 release

* Mon Dec  7 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.5-0.3.rc2
- 1.2.5.rc2 release

* Wed Dec  2 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.5-0.2.rc1
- 1.2.5.rc1 release

* Thu Nov 12 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.5-0.1.a1
- 1.2.5.a1 release

* Thu Oct 29 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.4-1
- 1.2.4 release
- resolves bug 221905 - added support for Salted MD5 (SMD5) passwords - primarily for migration
- resolves bug 529258 - Make upgrade remove obsolete schema from 99user.ldif

* Mon Sep 14 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.3-1
- 1.2.3 release
- added template-initconfig to %files
- %posttrans now runs update to update the server instances
- servers are shutdown, then restarted if running before install
- scriptlets mostly use lua now to pass data among scriptlet phases

* Tue Sep 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.2.2-2
- rebuild with new openssl to fix dependencies

* Tue Aug 25 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.2-1
- backed out - added template-initconfig to %files - this change is for the next major release
- bump version to 1.2.2
- fix reopened 509472 db2index all does not reindex all the db backends correctly
- fix 518520 -  pre hashed salted passwords do not work
- see https://bugzilla.redhat.com/show_bug.cgi?id=518519 for the list of
- bugs fixed in 1.2.2

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.2.1-5
- rebuilt with new openssl

* Wed Aug 19 2009 Noriko Hosoi <nhosoi@redhat.com> - 1.2.1-4
- added template-initconfig to %files

* Wed Aug 12 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.1-3
- added BuildRequires pcre

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 18 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.1-1
- change name to 389
- change version to 1.2.1
- added initial support for numeric string syntax
- added initial support for syntax validation
- added initial support for paged results including sorting

* Tue Apr 28 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.0-4
- final release 1.2.0
- Resolves: bug 475338 - LOG: the intenal type of maxlogsize, maxdiskspace and minfreespace should be 64-bit integer
- Resolves: bug 496836 - SNMP ldap-agent on Solaris: Unable to open semaphore for server: 389
- CVS tag: FedoraDirSvr_1_2_0 FedoraDirSvr_1_2_0_20090428

* Mon Apr  6 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.0-3
- re-enable ppc builds

* Thu Apr  2 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.0-2
- exclude ppc builds - needs extensive porting work

* Mon Mar 30 2009 Rich Megginson <rmeggins@redhat.com> - 1.2.0-1
- new release 1.2.0
- Made devel package depend on mozldap-devel
- only create run dir if it does not exist
- CVS tag: FedoraDirSvr_1_2_0_RC1 FedoraDirSvr_1_2_0_RC1_20090330

* Thu Oct 30 2008 Noriko Hosoi <nhosoi@redhat.com> - 1.1.3-7
- added db4-utils to Requires for verify-db.pl

* Mon Oct 13 2008 Noriko Hosoi <nhosoi@redhat.com> - 1.1.3-6
- Enabled LDAPI autobind

* Thu Oct  9 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.3-5
- updated update to patch bug463991-bdb47.patch

* Thu Oct  9 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.3-4
- updated patch bug463991-bdb47.patch

* Mon Sep 29 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.3-3
- added patch bug463991-bdb47.patch
- make ds work with bdb 4.7

* Wed Sep 24 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.3-2
- rolled back bogus winsync memory leak fix

* Tue Sep 23 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.3-1
- winsync api improvements for modify operations

* Fri Jun 13 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.2-1
- This is the 1.1.2 release.  The bugs fixed can be found here
- https://bugzilla.redhat.com/showdependencytree.cgi?id=452721
- Added winsync-plugin.h to the devel subpackage

* Fri Jun  6 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.1-2
- bump rev to rebuild and pick up new version of ICU

* Fri May 23 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.1-1
- 1.1.1 release candidate - several bug fixes

* Wed Apr 16 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.0.1-4
- fix bugzilla 439829 - patch to allow working with NSS 3.11.99 and later

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.0.1-3
- add patch to allow server to work with NSS 3.11.99 and later
- do NSS_Init after fork but before detaching from console

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.0.1-3
- add Requires for versioned perl (libperl.so)

* Wed Feb 27 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.0.1-2
- previous fix for 434403 used the wrong patch
- this is the right one

* Wed Feb 27 2008 Rich Megginson <rmeggins@redhat.com> - 1.1.0.1-1
- Resolves bug 434403 - GCC 4.3 build fails
- Rolled new source tarball which includes Nathan's fix for the struct ucred
- NOTE: Change version back to 1.1.1 for next release
- this release was pulled from CVS tag FedoraDirSvr110_gcc43

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-5
- Autorebuild for GCC 4.3

* Thu Dec 20 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-4
- This is the GA release of Fedora DS 1.1
- Removed version numbers for BuildRequires and Requires
- Added full URL to source tarball

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.1.0-3
- Rebuild for deps

* Wed Nov  7 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-2.0
- This is the beta2 release
- new file added to package - /etc/sysconfig/dirsrv - for setting
- daemon environment as is usual in other linux daemons

* Thu Aug 16 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.2
- fix build breakage due to open()
- mock could not find BuildRequires: db4-devel >= 4.2.52
- mock works if >= version is removed - it correctly finds db4.6

* Fri Aug 10 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.1
- Change pathnames to use the pkgname macro which is dirsrv
- get rid of cvsdate in source name

* Fri Jul 20 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-0.3.20070720
- Added Requires for perldap, cyrus sasl plugins
- Removed template-migrate* files
- Added perl module directory
- Removed install.inf - setup-ds.pl can now easily generate one

* Mon Jun 18 2007 Nathan Kinder <nkinder@redhat.com> - 1.1.0-0.2.20070320
- added requires for mozldap-tools

* Tue Mar 20 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-0.1.20070320
- update to latest sources
- added migrateTo11 to allow migrating instances from 1.0.x to 1.1
- ldapi support
- fixed pam passthru plugin ENTRY method

* Fri Feb 23 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-0.1.20070223
- Renamed package to fedora-ds-base, but keep names of paths/files/services the same
- use the shortname macro (fedora-ds) for names of paths, files, and services instead
- of name, so that way we can continue to use e.g. /etc/fedora-ds instead of /etc/fedora-ds-base
- updated to latest sources

* Tue Feb 13 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-0.1.20070213
- More cleanup suggested by Dennis Gilmore
- This is the fedora extras candidate based on cvs tag FedoraDirSvr110a1

* Fri Feb  9 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.el4.20070209
- latest sources
- added init scripts
- use /etc as instconfigdir

* Wed Feb  7 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.el4.20070207
- latest sources
- moved all executables to _bindir

* Mon Jan 29 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.el4.20070129
- latest sources
- added /var/tmp/fedora-ds to dirs

* Fri Jan 26 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-8.el4.20070125
- added logconv.pl
- added slapi-plugin.h to devel package
- added explicit dirs for /var/log/fedora-ds et. al.

* Thu Jan 25 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-7.el4.20070125
- just move all .so files into the base package from the devel package

* Thu Jan 25 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-6.el4.20070125
- Move the plugin *.so files into the main package instead of the devel
- package because they are loaded directly by name via dlopen

* Fri Jan 19 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-5.el4.20070125
- Move the script-templates directory to datadir/fedora-ds

* Fri Jan 19 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-4.el4.20070119
- change mozldap to mozldap6

* Fri Jan 19 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-3.el4.20070119
- remove . from cvsdate define

* Fri Jan 19 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-2.el4.20070119
- Having a problem building in Brew - may be Release format

* Fri Jan 19 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1.el4.cvs20070119
- Changed version to 1.1.0 and added Release 1.el4.cvs20070119
- merged in changes from Fedora Extras candidate spec file

* Mon Jan 15 2007 Rich Megginson <rmeggins@redhat.com> - 1.1-0.1.cvs20070115
- Bump component versions (nspr, nss, svrcore, mozldap) to their latest
- remove unneeded patches

* Tue Jan 09 2007 Dennis Gilmore <dennis@ausil.us> - 1.1-0.1.cvs20070108
- update to a cvs snapshot
- fedorafy the spec 
- create -devel subpackage
- apply a patch to use mozldap not mozldap6
- apply a patch to allow --prefix to work correctly

* Mon Dec 4 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-16
- Fixed the problem where the server would crash upon shutdown in dblayer
- due to a race condition among the database housekeeping threads
- Fix a problem with normalized absolute paths for db directories

* Tue Nov 28 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-15
- Touch all of the ldap/admin/src/scripts/*.in files so that they
- will be newer than their corresponding script template files, so
- that make will rebuild them.

* Mon Nov 27 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-14
- Chown new schema files when copying during instance creation

* Tue Nov 21 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-13
- Configure will get ldapsdk_bindir from pkg-config, or $libdir/mozldap6

* Tue Nov 21 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-12
- use eval to sed ./configure into ../configure

* Tue Nov 21 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-11
- jump through hoops to be able to run ../configure

* Tue Nov 21 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-10
- Need to make built dir in setup section

* Tue Nov 21 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-9
- The template scripts needed to use @libdir@ instead of hardcoding
- /usr/lib
- Use make DESTDIR=$RPM_BUILD_ROOT install instead of % makeinstall
- do the actual build in a "built" subdirectory, until we remove
- the old script templates

* Thu Nov 16 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-8
- Make replication plugin link with libdb

* Wed Nov 15 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-7
- Have make define LIBDIR, BINDIR, etc. for C code to use
- especially for create_instance.h

* Tue Nov 14 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-6
- Forgot to checkin new config.h.in for AC_CONFIG_HEADERS

* Tue Nov 14 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-5
- Add perldap as a Requires; update sources

* Thu Nov 9 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-4
- Fix ds_newinst.pl
- Remove obsolete #defines

* Thu Nov 9 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-3
- Update sources; rebuild to populate brew yum repo with dirsec-nss

* Tue Nov 7 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-2
- Update sources

* Thu Nov 2 2006 Rich Megginson <rmeggins@redhat.com> - 1.0.99-1
- initial revision
