#
# $Id: autofs.spec,v 1.11 2003/12/04 15:41:32 raven Exp $
#
Summary: A tool for automatically mounting and unmounting filesystems
Name: autofs
Version: 5.0.5
Release: 123%{?dist}
Epoch: 1
License: GPLv2+
Group: System Environment/Daemons
URL: http://wiki.autofs.net/
Source: ftp://ftp.kernel.org/pub/linux/daemons/autofs/v5/autofs-%{version}.tar.bz2
Patch1: autofs-5.0.5-fix-included-map-read-fail-handling.patch
Patch2: autofs-5.0.5-refactor-ldap-sasl-bind.patch
Patch3: autofs-5.0.4-add-mount-wait-parameter.patch
Patch4: autofs-5.0.5-special-case-cifs-escapes.patch
Patch5: autofs-5.0.5-fix-libxml2-workaround-configure.patch
Patch6: autofs-5.0.5-more-code-analysis-corrections.patch
Patch7: autofs-5.0.5-fix-backwards-ifndef-INET6.patch
Patch8: autofs-5.0.5-fix-stale-init-for-file-map-instance.patch
Patch9: autofs-5.0.5-fix-ext4-fsck-at-mount.patch
Patch10: autofs-5.0.5-dont-use-master_lex_destroy-to-clear-parse-buffer.patch
Patch11: autofs-5.0.5-make-documentation-for-set-log-priority-clearer.patch
Patch12: autofs-5.0.5-fix-timeout-in-connect_nb.patch
Patch13: autofs-5.0.5-fix-pidof-init-script-usage.patch
Patch14: autofs-5.0.5-check-for-path-mount-location-in-generic-module.patch
Patch15: autofs-5.0.5-dont-fail-mount-on-access-fail.patch
Patch16: autofs-5.0.5-fix-rpc-large-export-list.patch
Patch17: autofs-5.0.5-dont-connect-at-ldap-lookup-module-init.patch
Patch18: autofs-5.0.5-fix-reconnect-get-base-dn.patch
Patch19: autofs-5.0.5-fix-random-selection-option.patch
Patch20: autofs-5.0.5-fix-disable-timeout.patch
Patch21: autofs-5.0.5-fix-strdup-return-value-check.patch
Patch22: autofs-5.0.5-fix-get-qdn-fail.patch
Patch23: autofs-5.0.5-fix-ampersand-escape-in-auto-smb.patch
Patch24: autofs-5.0.5-make-nfs4-default-for-redhat-replicated-selection.patch
Patch25: autofs-5.0.5-add-autofs_ldap_auth_conf-man-page.patch
Patch26: autofs-5.0.5-fix-random-selection-for-host-on-different-network.patch
Patch27: autofs-5.0.5-make-redhat-init-script-more-lsb-compliant.patch
Patch28: autofs-5.0.5-add-sasl-mutex-callbacks.patch
Patch29: autofs-5.0.5-fix-parse_sun-module-init.patch
Patch30: autofs-5.0.5-dont-check-null-cache-on-expire.patch
Patch31: autofs-5.0.5-fix-null-cache-race.patch
Patch32: autofs-5.0.5-fix-cache_init-on-source-re-read.patch
Patch33: autofs-5.0.5-fix-negative-cache-included-map-lookup.patch
Patch34: autofs-5.0.5-remove-state-machine-timed-wait.patch
Patch35: autofs-5.0.5-add-locality-as-valid-ldap-master-map-attribute.patch
Patch36: autofs-5.0.5-fix-remount-locking.patch
Patch37: autofs-5.0.5-fix-restart.patch
Patch38: autofs-5.0.5-always-read-file-maps-mount-lookup-map-read-fix.patch
Patch39: autofs-5.0.5-add-external-bind-method.patch
Patch40: autofs-5.0.5-add-simple-bind-auth.patch
Patch41: autofs-5.0.5-fix-add-simple-bind-auth.patch
Patch42: autofs-5.0.5-use-weight-only-for-server-selection.patch
Patch43: autofs-5.0.5-fix-isspace-wild-card-substition.patch
Patch44: autofs-5.0.5-add-lsb-force-reload-and-try-restart.patch
Patch45: autofs-5.0.5-include-ip-address-in-debug-logging.patch
Patch46: autofs-5.0.5-mount-using-address-for-rr.patch
Patch47: autofs-5.0.5-fix-direct-map-not-updating-on-reread.patch
Patch48: autofs-5.0.5-include-krb5-library.patch
Patch49: autofs-5.0.5-remove-ERR_remove_state-openssl-call.patch
Patch50: autofs-5.0.5-fix-next-task-list-update.patch
Patch51: autofs-5.0.5-fix-stale-map-read.patch
Patch52: autofs-5.0.5-fix-null-cache-clean.patch
Patch53: autofs-5.0.5-automount-8-man-page-correction.patch
Patch54: autofs-5.0.5-dont-hold-lock-for-simple-mounts.patch
Patch55: autofs-5.0.5-fix-prune-cache-valid-check.patch
Patch56: autofs-5.0.5-fix-map-source-check-in-file-lookup.patch
Patch57: autofs-5.0.5-wait-for-master-source-mutex.patch
Patch58: autofs-5.0.5-auto-adjust-ldap-page-size.patch
Patch59: autofs-5.0.5-fix-paged-ldap-map-read.patch
Patch60: autofs-5.0.5-add-base64-password-encode.patch
Patch61: autofs-5.0.5-add-dump-maps-option.patch
Patch62: autofs-5.0.5-reset-negative-status-on-cache-prune.patch
Patch63: autofs-5.0.5-fix-wildcard-map-entry-match.patch
Patch64: autofs-5.0.5-fix-sasl-bind-host-name-selection.patch
Patch65: autofs-5.0.5-fix-sanity-checks-for-brackets-in-server-name.patch
Patch66: autofs-5.0.5-mapent-becomes-negative-during-lookup.patch
Patch67: autofs-5.0.5-check-each-dc-server.patch
Patch68: autofs-5.0.5-fix-null-cache-deadlock.patch
Patch69: autofs-5.0.5-replace-gplv3-code.patch
Patch70: autofs-5.0.6-fix-paged-query-more-results-check.patch
Patch71: autofs-5.0.6-fix-dumpmaps-not-reading-maps.patch
Patch72: autofs-5.0.6-improve-mount-location-error-reporting.patch
Patch73: autofs-5.0.6-code-analysis-fixes-1.patch
Patch74: autofs-5.0.6-fix-improve-mount-location-error-reporting.patch
Patch75: autofs-5.0.5-fix-ipv6-name-for-lookup.patch
Patch76: autofs-5.0.5-fix-libtirpc-ipv6-check.patch
Patch77: autofs-5.0.6-fix-ipv6-name-for-lookup-fix.patch
Patch78: autofs-5.0.6-fix-ipv6-name-lookup-check.patch
Patch79: autofs-5.0.6-fix-ipv6-rpc-calls.patch
Patch80: autofs-5.0.6-fix-ipv6-configure-check.patch
Patch81: autofs-5.0.6-add-sss-lookup-module.patch
Patch82: autofs-5.0.6-teach-automount-about-sss-source.patch
Patch83: autofs-5.0.6-fix-fix-map-source-check-in-file-lookup.patch
Patch84: autofs-5.0.6-fix-init-script-usage-message.patch
Patch85: autofs-5.0.6-ignore-duplicate-exports-in-auto-net.patch
Patch86: autofs-5.0.6-fix-submount-shutdown-race.patch
Patch87: autofs-5.0.6-fix-wait-for-master-source-mutex.patch
Patch88: autofs-5.0.6-fix-fix-wait-for-master-source-mutex.patch
Patch89: autofs-5.0.6-add-kernel-verion-check-function.patch
Patch90: autofs-5.0.6-add-function-to-check-mount-nfs-version.patch
Patch91: autofs-5.0.6-reinstate-singleton-mount-probe.patch
Patch92: autofs-5.0.6-rework-error-return-handling-in-rpc-code.patch
Patch93: autofs-5.0.6-catch-EHOSTUNREACH-and-bail-out-early.patch
Patch94: autofs-5.0.6-fix-function-to-check-mount_nfs-version.patch
Patch95: autofs-5.0.6-fix-rework-error-return-handling-in-rpc-code.patch
Patch96: autofs-5.0.6-allow-MOUNT_WAIT-to-override-probe.patch
Patch97: autofs-5.0.6-improve-UDP_RPC-timeout-handling.patch
Patch98: autofs-5.0.6-use-strtok_r-in-linux_version_code.patch
Patch99: autofs-5.0.6-fix-sss-wildcard-match.patch
Patch100: autofs-5.0.6-fix-dlopen-error-handling-in-sss-module.patch
Patch101: autofs-5.0.6-fix-configure-string-length-tests.patch
Patch102: autofs-5.0.5-add-nobind-option.patch
Patch103: autofs-5.0.5-dont-bind-nfs-mount-if-nobind-is-set.patch
Patch104: autofs-5.0.6-update-timeout-function-to-not-return-timeout.patch
Patch105: autofs-5.0.6-move-timeout-to-map_source.patch
Patch106: autofs-5.0.6-report-map-not-read-when-debug-logging.patch
Patch107: autofs-5.0.5-fix-mountd-vers-retry.patch
Patch108: autofs-5.0.6-fix-initialization-in-rpc-create_client.patch
Patch109: autofs-5.0.6-fix-libtirpc-name-clash.patch
Patch110: autofs-5.0.6-fix-nfs4-contacts-portmap.patch
Patch111: autofs-5.0.6-fix-get_nfs_info-incorrectly-fails.patch
Patch112: autofs-5.0.7-fix-ipv6-proximity-calculation.patch
Patch113: autofs-5.0.5-fix-expire-race.patch
Patch114: autofs-5.0.6-fix-remount-deadlock.patch
Patch115: autofs-5.0.6-fix-umount-recovery-of-busy-direct-mount.patch
Patch116: autofs-5.0.6-fix-offset-mount-point-directory-removal.patch
Patch117: autofs-5.0.5-remove-move-mount-code.patch
Patch118: autofs-5.0.6-fix-remount-of-multi-mount.patch
Patch119: autofs-5.0.6-fix-device-ioctl-alloc-path-check.patch
Patch120: autofs-5.0.6-refactor-lookup-hosts-module.patch
Patch121: autofs-5.0.6-remove-cache-update-from-parse_mount.patch
Patch122: autofs-5.0.6-add-function-to-delete-offset-cache-entry.patch
Patch123: autofs-5.0.6-allow-update-of-multi-mount-offset-entries.patch
Patch124: autofs-5.0.6-add-hup-signal-handling-to-hosts-map.patch
Patch125: autofs-5.0.6-fix-offset-dir-removal.patch
Patch126: autofs-5.0.7-include-usage-in-usage-message.patch
Patch127: autofs-5.0.7-dont-wait-forever-to-restart.patch
Patch128: autofs-5.0.5-add-timeout-option-description-to-man-page.patch
Patch129: autofs-5.0.5-fix-null-map-entry-order-handling.patch
Patch130: autofs-5.0.6-documentation-fix-some-typos-and-misleading-comments.patch
Patch131: autofs-5.0.7-make-description-of-default-MOUNT_WAIT-setting-clear.patch
Patch132: autofs-5.0.7-allow-non-root-user-to-check-status.patch
Patch133: autofs-5.0.5-destroy-the-socket-when-rpc_ping_proto-failed-for-NFSv4.patch
Patch134: autofs-5.0.7-fix-map-entry-duplicate-offset-detection.patch
Patch135: autofs-5.0.7-fix-nobind-man-page-description.patch
Patch136: autofs-5.0.6-add-piddir-to-configure.patch
Patch137: autofs-5.0.5-fix-submount-offset-delete.patch
Patch138: autofs-5.0.7-fix-init-script-status-return.patch
Patch139: autofs-5.0.6-fix-segfault-in-get_query_dn.patch
Patch140: autofs-5.0.5-use-numeric-protocol-ids-instead-of-protoent-structs.patch
Patch141: autofs-5.0.5-fix-recursive-mount-deadlock.patch
Patch142: autofs-5.0.5-increase-file-map-read-buffer-size.patch
Patch143: autofs-5.0.6-dont-use-pthread_rwlock_tryrdlock.patch
Patch144: autofs-5.0.7-fix-master-map-mount-options-matching.patch
Patch145: autofs-5.0.7-fix-master-map-bogus-keywork-match.patch
Patch146: autofs-5.0.6-mount_nfs.so-to-honor-explicit-NFSv4-requests.patch
Patch147: autofs-5.0.5-mount_nfs.so-fix-port-0-option-behavior-v3.patch
Patch148: autofs-5.0.7-check-for-protocol-option.patch
Patch149: autofs-5.0.7-dont-probe-rdma-mounts.patch
Patch150: autofs-5.0.7-probe-each-nfs-version-in-turn-for-singleton-mounts.patch
Patch151: autofs-5.0.7-use-ulimit-max-open-files-if-greater-than-internal-maximum.patch
Patch152: autofs-5.0.6-fix-not-bind-mounting-local-filesystem.patch
Patch153: autofs-5.0.7-fix-interface-address-null-check.patch
Patch154: autofs-5.0.7-improve-timeout-option-description.patch
Patch155: autofs-5.0.7-make-dump-maps-check-for-duplicate-indirect-mounts.patch
Patch156: autofs-5.0.7-fix-dumpmaps-multi-output.patch
Patch157: autofs-5.0.7-try-and-cleanup-after-dumpmaps.patch
Patch158: autofs-5.0.7-teach-dumpmaps-to-output-simple-key-value-pairs.patch
Patch159: autofs-5.0.7-syncronize-handle_mounts-shutdown.patch
Patch160: autofs-5.0.7-fix-wildcard-multi-map-regression.patch
Patch161: autofs-5.0.7-fix-fix-wildcard-multi-map-regression.patch
Patch162: autofs-5.0.7-only-probe-specific-nfs-version-when-requested.patch
Patch163: autofs-5.0.5-expire-thread-use-pending-mutex.patch
Patch164: autofs-5.0.7-fix-get_nfs_info-probe.patch
Patch165: autofs-5.0.7-fix-crash-due-to-thread-unsafe-use-of-libldap.patch
Patch166: autofs-5.0.8-fix-options-compare.patch
Patch167: autofs-5.0.8-fix-fix-options-compare.patch
Patch168: autofs-5.0.8-fix-negative-status-being-reset-on-map-read.patch
Patch169: autofs-5.0.8-get_nfs_info-should-query-portmapper-if-port-is-not-given.patch
Patch170: autofs-5.0.8-fix-ipv6-link-local-address-handling.patch
Patch171: autofs-5.0.8-fix-deadlock-in-init-ldap-connection.patch
Patch172: autofs-5.0.8-extend-libldap-serialization.patch
Patch173: autofs-5.0.6-fix-segmentation-fault-in-do_remount_indirect.patch
Patch174: autofs-5.0.7-fix-use-cache-entry-after-free-mistake.patch
Patch175: autofs-5.0.9-check-for-non-existent-negative-entries-in-lookup_ghost.patch
Patch176: autofs-5.0.9-fix-reset-flex-scan-buffer-on-init.patch
Patch177: autofs-5.0.9-fix-fix-negative-status-being-reset-on-map-read.patch

# pre-patches for amd parser series.
Patch400: autofs-5.0.6-fix-kernel-verion-check-of-version-components.patch
Patch401: autofs-5.0.5-fix-submount-shutdown-wait.patch
Patch402: autofs-5.0.7-fix-submount-tree-not-all-expiring.patch
Patch403: autofs-5.0.7-fix-fcntl-return-check.patch
Patch404: autofs-5.0.7-fix-spawn_umount-return-check-in-mount_bind-lookup_init.patch
Patch405: autofs-5.0.7-fix-check-mkdir_path-in-mount_bind-mount_mount.patch
Patch406: autofs-5.0.7-fix-a-couple-of-compiler-warnings.patch
Patch407: autofs-5.0.8-fix-max-declaration.patch
Patch408: autofs-5.0.7-depricate-nosymlink-pseudo-option.patch
Patch409: autofs-5.0.7-add-symlink-pseudo-option.patch
Patch410: autofs-5.0.7-setup-program-map-env-from-macro-table.patch
Patch411: autofs-5.0.7-add-short-host-name-standard-marco-variable.patch
Patch412: autofs-5.0.7-allow-use-of-hosts-map-in-maps.patch
Patch413: autofs-5.0.8-fix-symlink-fail-message-in-mount_bind-c.patch
Patch414: autofs-5.0.7-add-std-vars-to-program-map-invocation.patch
Patch415: autofs-5.0.8-check-for-existing-offset-mount-before-mounting.patch
Patch416: autofs-5.0.8-remove-macro-debug-prints.patch
Patch417: autofs-5.0.8-fix-cache-readlock-not-taken-on-lookup.patch
Patch418: autofs-5.0.7-fix-potential-null-dereference-in-lookup_mount.patch
Patch419: autofs-5.0.7-add-null-check-in-read_one.patch
Patch420: autofs-5.0.6-duplicate-parent-options-for-included-maps.patch
Patch421: autofs-5.0.7-lib-defaults-use-WITH_LDAP-conditional-around-LDAP-types.patch
Patch422: autofs-5.0.5-fix-out-of-order-locking-in-readmap.patch
Patch423: autofs-5.0.5-fix-master-map-source-server-unavialable-handling.patch
Patch424: autofs-5.0.7-dont-fail-on-master-map-self-include.patch
Patch425: autofs-5.0.6-fix-LDAP-result-leaks-on-error-paths.patch
Patch426: autofs-5.0.6-fix-fix-LDAP-result-leaks-on-error-paths.patch
Patch427: autofs-5.0.6-dont-retry-ldap-connect-if-not-required.patch
Patch428: autofs-5.0.7-add-null-check-in-parse_server_string.patch
Patch429: autofs-5.0.6-fix-result-null-check-in-read_one_map.patch
Patch430: autofs-5.0.5-fix-simple-bind-without-SASL-support.patch
Patch431: autofs-5.0.7-fix-compilation-of-lookup_ldap_c-without-sasl.patch
Patch432: autofs-5.0.8-fix-undefined-authtype_requires_creds-err-if-ldap-en.patch
Patch433: autofs-5.0.7-fix-several-off-by-one-errors.patch
Patch434: autofs-5.0.7-fix-leaked-ldap-percent-hack-allocation-in-lookup_one.patch
Patch435: autofs-5.0.8-pass-map_source-as-function-paramter-where-possible.patch
Patch436: autofs-5.0.8-check-for-bind-onto-self-in-mount_bind-c.patch
Patch437: autofs-5.0.8-fix-symlink-expire.patch
Patch438: autofs-5.0.8-fix-master-map-type-check.patch
Patch439: autofs-5.0.7-add-mapent-null-check-in-lookup-nisplus-lookup_mount.patch
Patch440: autofs-5.0.8-dont-clobber-mapent-for-negative-cache.patch
Patch441: autofs-5.0.7-fix-bad-mkdir-permission-on-create.patch
Patch442: autofs-5.0.8-fix-macro_addvar-and-move-init-to-main-thread.patch
Patch443: autofs-5.0.7-fix-file-descriptor-leak-when-reloading-the-daemon.patch
Patch444: autofs-5.0.8-change-walk_tree-to-take-ap.patch
Patch445: autofs-5.0.8-add-negative-cache-lookup-to-hesiod-lookup.patch
Patch446: autofs-5.0.7-fix-use-get_proximity-without-libtirpc.patch
Patch447: autofs-5.0.7-fix-incorrect-value-reference-in-parse_line.patch
Patch448: autofs-5.0.7-document-allowed-map-sources-in-auto_master.patch
Patch449: autofs-5.0.8-fix-external-env-configure.patch
Patch450: autofs-5.0.8-make-autofs-5-consistent-with-auto-master-5.patch
Patch451: autofs-5.0.8-fix-map-source-with-type-lookup.patch
Patch452: autofs-5.0.8-fix-fix-map-source-with-type-lookup.patch
Patch453: autofs-5.0.8-fix-lookup_nss_mount-map-lookup.patch
Patch454: autofs-5.0.8-dont-ignore-null-cache-entries-on-multi-mount-umount.patch
Patch455: autofs-5.0.8-fix-inconsistent-error-returns-in-handle_packet_missing_direct.patch
Patch456: autofs-5.0.8-simple-coverity-fixes.patch
Patch457: autofs-5.0.8-remove-stale-debug-message.patch
Patch458: autofs-5.0.8-fixes-for-samples-auto_master.patch
Patch459: autofs-5.0.8-fix-variable-substitution-description.patch
Patch460: autofs-5.0.8-fix-append-options-description-in-README_v5-release.patch
Patch461: autofs-5.0.9-fix-mistake-in-assignment.patch
Patch462: autofs-5.0.7-add-pgrp-check-in-do_spawn.patch
Patch463: autofs-5.0.8-use-open-instead-of-access.patch
Patch464: autofs-5.0.7-document-browse-option-in-man-page.patch
Patch465: autofs-5.0.7-add-null-check-in-extract_version.patch
Patch466: autofs-5.0.7-add-debug-alert-for-waitpid-in-check_nfs_mount_version.patch
Patch467: autofs-5.0.7-fix-incorrect-name-in-test.patch
Patch468: autofs-5.0.7-fix-parse-buffer-initialization.patch
Patch469: autofs-5.0.5-remove-master_mutex_unlock-leftover.patch
Patch470: autofs-5.0.8-dont-reset-errno.patch
Patch471: autofs-5.0.6-fix-typo-in-libtirpc-file-name.patch

# amd parser series
Patch500: autofs-5.0.9-amd-lookup-move-get_proximity-to-parse_subs-c.patch
Patch501: autofs-5.0.9-amd-lookup-use-flags-in-map_source-for-format.patch
Patch502: autofs-5.0.9-amd-lookup-rework-config-handling.patch
Patch503: autofs-5.0.9-amd-lookup-add-conf-handling-for-amd-maps.patch
Patch504: autofs-5.0.9-amd-lookup-split-config-into-init-and-config-settings.patch
Patch505: autofs-5.0.9-amd-lookup-update-man-page-autofs-config-description.patch
Patch506: autofs-5.0.9-amd-lookup-add-amd-config-descriptions-to-config.patch
Patch507: autofs-5.0.9-amd-lookup-fix-lofs-mounting.patch
Patch508: autofs-5.0.9-amd-lookup-add-merge_options-function.patch
Patch509: autofs-5.0.9-amd-lookup-add-expandamdent-function.patch
Patch510: autofs-5.0.9-amd-lookup-add-external-mounts-tracking-functions.patch
Patch511: autofs-5.0.9-amd-lookup-add-amd-global-macro-vars.patch
Patch512: autofs-5.0.9-amd-lookup-add-selector-handling-functions.patch
Patch513: autofs-5.0.9-amd-lookup-add-parse_amd-c.patch
Patch514: autofs-5.0.9-amd-lookup-add-parent-prefix-handling.patch
Patch515: autofs-5.0.9-amd-lookup-add-lookup-vars.patch
Patch516: autofs-5.0.9-amd-lookup-add-selector-handling.patch
Patch517: autofs-5.0.9-amd-lookup-add-cut-handling.patch
Patch518: autofs-5.0.9-amd-lookup-add-handling-of-amd-maps-in-the-master-map.patch
Patch519: autofs-5.0.9-amd-lookup-add-cache-partial-match-functions.patch
Patch520: autofs-5.0.9-amd-lookup-fix-expire-of-amd-nfs-mounts.patch
Patch521: autofs-5.0.9-amd-lookup-add-lofs-ext-and-xfs-fs-types.patch
Patch522: autofs-5.0.9-amd-lookup-add-key-matching-helper-function.patch
Patch523: autofs-5.0.9-amd-lookup-update-lookup-file-to-handle-amd-keys.patch
Patch524: autofs-5.0.9-amd-lookup-update-lookup-yp-to-handle-amd-keys.patch
Patch525: autofs-5.0.9-amd-lookup-update-lookup-program-to-handle-amd-keys.patch
Patch526: autofs-5.0.9-amd-lookup-update-lookup-nisplus-to-handle-amd-keys.patch
Patch527: autofs-5.0.8-amd-lookup-update-lookup-ldap-to-handle-amd-keys.patch
Patch528: autofs-5.0.8-amd-lookup-update-lookup-hesiod-to-handle-amd-keys.patch
Patch529: autofs-5.0.9-amd-lookup-add-handling-of-unhandled-options.patch
Patch530: autofs-5.0.9-amd-lookup-use-config-map_type-if-type-is-not-given.patch
Patch531: autofs-5.0.9-amd-lookup-update-man-pages.patch
Patch532: autofs-5.0.9-amd-lookup-add-remopts-handling.patch
Patch533: autofs-5.0.9-amd-lookup-add-nfsl-and-linkx-fs-types.patch
Patch534: autofs-5.0.9-amd-lookup-add-search_path-handling.patch
Patch535: autofs-5.0.9-amd-lookup-fix-host-mount-lookup.patch
Patch536: autofs-5.0.9-amd-lookup-fix-host-mount-naming.patch
Patch537: autofs-5.0.9-amd-lookup-check-for-required-options-for-mounts.patch
Patch538: autofs-5.0.9-amd-lookup-add-cdfs-fs-type.patch
Patch539: autofs-5.0.9-amd-lookup-dont-umount-admin-mounted-external-mounts.patch
Patch540: autofs-5.0.9-amd-lookup-skip-sss-source-for-amd-lookups.patch
Patch541: autofs-5.0.9-amd-lookup-allow-exec-to-be-used-by-amd-maps-in-master-map.patch
Patch542: autofs-5.0.9-amd-lookup-fix-amd-entry-not-found-at-expire.patch
Patch543: autofs-5.0.9-amd-lookup-fix-prefix-not-set-on-mount-reconnect.patch
Patch544: autofs-5.0.9-amd-lookup-add-REDAME-amd-maps.patch
Patch545: autofs-5.0.9-amd-lookup-fix-autofs_use_lofs-value-in-config.patch
Patch546: autofs-5.0.9-amd-lookup-fix-expire-of-external-mounts.patch
Patch547: autofs-5.0.9-amd-lookup-try-to-use-external-mounts-for-real-mounts.patch
Patch548: autofs-5.0.9-amd-lookup-add-ufs-fs-type.patch
Patch549: autofs-5.0.9-amd-lookup-fix-old-conf-handling.patch
Patch550: autofs-5.0.9-amd-lookup-try-to-use-external-mounts-for-nfs-mounts.patch
Patch551: autofs-5.0.9-amd-lookup-update-changelog.patch
Patch552: autofs-5.1.0-beta1-fix-wildcard-key-lookup.patch
Patch553: autofs-5.1.0-beta1-fix-out-of-order-amd-timestamp-lookup.patch
Patch554: autofs-5.1.0-beta1-fix-ldap-default-schema-config.patch
Patch555: autofs-5.1.0-beta1-fix-ldap-default-master-map-name-config.patch
Patch556: autofs-5.1.0-beta1-fix-map-format-init-in-lookup_init.patch
Patch557: autofs-5.1.0-beta1-fix-incorrect-max-key-length-in-defaults-get_hash.patch
Patch558: autofs-5.1.0-beta1-fix-xfn-sets-incorrect-lexer-state.patch
Patch559: autofs-5.1.0-beta1-fix-old-style-key-lookup.patch
Patch560: autofs-5.1.0-beta1-fix-expire-when-server-not-responding.patch
Patch561: autofs-5.1.0-beta1-fix-ldap_uri-config-update.patch
Patch562: autofs-5.1.0-beta1-fix-typo-in-conf_load_autofs_defaults.patch
Patch563: autofs-5.1.0-beta1-fix-hash-on-config-option-add-and-delete.patch
Patch564: autofs-5.1.0-beta1-add-plus-to-path-match-pattern.patch
Patch565: autofs-5.1.0-beta1-fix-multi-entry-ldap-option-handling.patch
Patch566: autofs-5.1.0-beta1-cleanup-options-in-amd_parse-c.patch
Patch567: autofs-5.1.0-beta1-allow-empty-value-for-some-map-options.patch
Patch568: autofs-5.1.0-beta1-allow-empty-value-in-macro-selectors.patch

Patch600: autofs-5.1.0-add-serialization-to-sasl-init.patch
Patch601: autofs-5.1.0-dont-allocate-dev_ctl_ops-too-early.patch

# Coverity motivated fixes, mainly for the new amd parser code
Patch602: autofs-5.1.0-fix-leak-in-cache_push_mapent.patch
Patch603: autofs-5.1.0-fix-config-entry-read-buffer-not-checked.patch
Patch604: autofs-5.1.0-fix-FILE-pointer-check-in-defaults_read_config.patch
Patch605: autofs-5.1.0-fix-memory-leak-in-conf_amd_get_log_options.patch
Patch606: autofs-5.1.0-fix-signed-comparison-in-inet_fill_net.patch
Patch607: autofs-5.1.0-fix-buffer-size-checks-in-get_network_proximity.patch
Patch608: autofs-5.1.0-fix-leak-in-get_network_proximity.patch
Patch609: autofs-5.1.0-fix-buffer-size-checks-in-merge_options.patch
Patch610: autofs-5.1.0-check-amd-lex-buffer-len-before-copy.patch
Patch611: autofs-5.1.0-add-return-check-in-ldap-check_map_indirect.patch
Patch612: autofs-5.1.0-check-host-macro-is-set-before-use.patch
Patch613: autofs-5.1.0-check-options-length-before-use-in-parse_amd_c.patch
Patch614: autofs-5.1.0-fix-some-out-of-order-evaluations-in-parse_amd_c.patch
Patch615: autofs-5.1.0-fix-copy-and-paste-error-in-dup_defaults_entry.patch
Patch616: autofs-5.1.0-fix-leak-in-parse_mount.patch
Patch617: autofs-5.1.0-add-mutex-call-return-check-in-defaults_c.patch

# more amd format map fixes
Patch618: autofs-5.1.0-force-disable-browse-mode-for-amd-format-maps.patch
Patch619: autofs-5.1.0-fix-hosts-map-options-check-in-lookup_amd_instance.patch

Patch620: autofs-5.1.0-fix-mem-leak-in-create_client.patch
Patch621: autofs-5.1.0-fix-memory-leak-in-get_exports.patch

Patch622: autofs-5.1.0-fix-memory-leak-in-get_defaults_entry.patch
Patch623: autofs-5.1.0-fix-out-of-order-clearing-of-options-buffer.patch
Patch624: autofs-5.1.0-fix-reset-amd-lexer-scan-buffer.patch
Patch625: autofs-5.1.0-ignore-multiple-commas-in-options-strings.patch

Patch626: autofs-5.1.0-make-negative-cache-update-consistent-for-all-lookup-modules.patch
Patch627: autofs-5.1.0-ensure-negative-cache-isnt-updated-on-remount.patch
Patch628: autofs-5.1.0-dont-add-wildcard-to-negative-cache.patch
Patch629: autofs-5.1.0-fix-fix-master-map-type-check.patch
Patch630: autofs-5.1.0-fix-typo-in-update_hosts_mounts.patch
Patch631: autofs-5.1.0-fix-hosts-map-update-on-reload.patch
Patch632: autofs-5.1.0-add-a-prefix-to-program-map-stdvars.patch
Patch633: autofs-5.1.0-add-config-option-to-force-use-of-program-map-stdvars.patch
Patch634: autofs-5.1.0-fix-incorrect-check-in-parse_mount.patch
Patch635: autofs-5.0.7-fix-fix-map-entry-duplicate-offset-detection.patch
Patch636: autofs-5.1.0-handle-duplicates-in-multi-mounts.patch
Patch637: autofs-5.1.0-fix-macro-usage-in-lookup_program_c.patch

# Add autofs re-init series + supporting bug fixes + ldap bind fix

# Series 1 - series2 dependency, to minimize back port changes
Patch638: autofs-5.1.1-fix-left-mount-count-return.patch
Patch639: autofs-5.1.1-fix-return-handling-in-sss-lookup-module.patch
Patch640: autofs-5.1.1-move-query-dn-calculation-from-do_bind-to-do_connect.patch
Patch641: autofs-5.1.1-make-do_connect-return-a-status.patch
Patch642: autofs-5.1.1-make-connect_to_server-return-a-status.patch
Patch643: autofs-5.1.1-make-find_dc_server-return-a-status.patch
Patch644: autofs-5.1.1-make-find_server-return-a-status.patch
Patch645: autofs-5.1.1-fix-return-handling-of-do_reconnect-in-ldap-module.patch

# Series 1 - additional bug fixes
Patch646: autofs-5.0.9-fix-race-accessing-qdn-in-get_query_dn.patch
Patch647: autofs-5.1.0-init-qdn-before-use.patch
Patch648: autofs-5.1.1-fix-rwlock-unlock-crash.patch
Patch649: autofs-5.1.1-fix-config-old-name-lookup.patch
Patch650: autofs-5.1.1-fix-error-handling-on-ldap-bind-fail.patch
# I need to be able to build test on my descktop, we'll need this
# for RHEL-8 anyway.
Patch651: autofs-5.1.0-fix-gcc5-complaints.patch
# Excessive map re-read regression
Patch652: autofs-5.1.1-fix-direct-mount-stale-instance-flag-reset.patch

# Series2 - add reinit method and change lookup to use reinit instead of reopen
Patch661: autofs-5.1.1-fix-missing-source-sss-in-multi-map-lookup.patch
Patch662: autofs-5.1.1-fix-update_hosts_mounts-return.patch
Patch663: autofs-5.1.1-move-check_nss_result-to-nsswitch_c.patch
Patch664: autofs-5.1.1-make-open_lookup-return-nss-status.patch
Patch665: autofs-5.1.1-fix-nsswitch-handling-when-opening-multi-map.patch
Patch666: autofs-5.1.1-add-reinit-entry-point-to-modules.patch
Patch667: autofs-5.1.1-implement-reinit-in-parse-modules.patch
Patch668: autofs-5.1.1-implement-reinit-in-file-lookup-module.patch
Patch669: autofs-5.1.1-implement-reinit-in-hesiod-lookup-module.patch
Patch670: autofs-5.1.1-implement-reinit-in-hosts-lookup-module.patch
Patch671: autofs-5.1.1-implement-reinit-in-ldap-lookup-module.patch
Patch672: autofs-5.1.1-implement-reinit-in-nisplus-lookup-module.patch
Patch673: autofs-5.1.1-implement-reinit-in-program-lookup-module.patch
Patch674: autofs-5.1.1-implement-reinit-in-sss-lookup-module.patch
Patch675: autofs-5.1.1-implement-reinit-in-yp-lookup-module.patch
Patch676: autofs-5.1.1-add-type-to-struct-lookup_mod.patch
Patch677: autofs-5.1.1-factor-out-free-multi-map-context.patch
Patch678: autofs-5.1.1-factor-out-alloc-multi-map-context.patch
Patch679: autofs-5.1.1-fix-map-format-check-in-nss_open_lookup-multi-map-module.patch
Patch680: autofs-5.1.1-implement-reinit-in-multi-lookup-module.patch
Patch681: autofs-5.1.1-change-lookup-to-use-reinit-instead-of-reopen.patch

# Aditional bug fixes
Patch682: autofs-5.1.1-fix-unbind-external-mech.patch
Patch683: autofs-5.1.1-fix-sasl-connection-concurrancy-problem.patch

Patch700: autofs-5.1.1-update-map_hash_table_size-description.patch
Patch701: autofs-5.1.1-add-configuration-option-to-use-hostname-in-mounts.patch
Patch702: autofs-5.1.1-fix-out-of-order-call-in-program-map-lookup.patch
Patch703: autofs-5.0.5-fix-lsb-service-name-in-init-script.patch
Patch704: autofs-5.0.6-fix-lsb-service-name-in-init-script-2.patch
Patch705: autofs-5.0.9-revert-special-case-cifs-escapes.patch
Patch706: autofs-5.1.0-remove-unused-offset-handling-code.patch
Patch707: autofs-5.1.0-fix-mount-as-you-go-offset-selection.patch
Patch708: autofs-5.1.0-guard-against-incorrect-umount-return.patch
Patch709: autofs-5.1.1-fix-direct-map-expire-not-set-for-initail-empty-map.patch

# Some Coverity fixes identified for recent changes
Patch710: autofs-5.1.1-fix-memory-leak-in-nisplus-lookup_reinit.patch
Patch711: autofs-5.1.1-fix-memory-leak-in-ldap-do_init.patch
Patch712: autofs-5.1.1-fix-use-after-free-in-sun-parser-parse_init.patch
Patch713: autofs-5.1.1-fix-use-after-free-in-open_lookup.patch
Patch714: autofs-5.1.1-fix-typo-in-autofs_sasl_bind.patch

Patch720: autofs-5.0.7-dont-schedule-new-alarms-after-readmap.patch

Patch730: autofs-5.1.1-always-set-direct-mounts-catatonic-at-exit.patch
Patch731: autofs-5.0.5-fix-error-handing-in-do_mount_indirect.patch
Patch732: autofs-5.0.5-check-negative-cache-much-earlier.patch
Patch733: autofs-5.1.1-log-pipe-read-errors.patch
Patch734: autofs-5.1.1-fix-handle_mounts-termination-condition-check.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, hesiod-devel, openldap-devel, bison, flex, libxml2-devel, cyrus-sasl-devel, openssl-devel module-init-tools util-linux nfs-utils e2fsprogs libtirpc-devel, libsss_autofs >= 1.8.0-5
Conflicts: cyrus-sasl-lib < 2.1.23-7
Requires: kernel >= 2.6.17
Requires: bash mktemp sed gawk textutils sh-utils grep module-init-tools /bin/ps
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
Summary(de): autofs daemon 
Summary(fr): démon autofs
Summary(tr): autofs sunucu süreci
Summary(sv): autofs-daemon

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches einschließen. 

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus. Cela
inclus les systèmes de fichiers réseau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden baðlar
ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem, að dosya
sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%description -l sv
autofs är en daemon som mountar filsystem när de använda, och senare
unmountar dem när de har varit oanvända en bestämd tid.  Detta kan
inkludera nätfilsystem, CD-ROM, floppydiskar, och så vidare.

%prep
%setup -q
echo %{version}-%{release} > .version
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

%patch400 -p1
%patch401 -p1
%patch402 -p1
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch406 -p1
%patch407 -p1
%patch408 -p1
%patch409 -p1
%patch410 -p1
%patch411 -p1
%patch412 -p1
%patch413 -p1
%patch414 -p1
%patch415 -p1
%patch416 -p1
%patch417 -p1
%patch418 -p1
%patch419 -p1
%patch420 -p1
%patch421 -p1
%patch422 -p1
%patch423 -p1
%patch424 -p1
%patch425 -p1
%patch426 -p1
%patch427 -p1
%patch428 -p1
%patch429 -p1
%patch430 -p1
%patch431 -p1
%patch432 -p1
%patch433 -p1
%patch434 -p1
%patch435 -p1
%patch436 -p1
%patch437 -p1
%patch438 -p1
%patch439 -p1
%patch440 -p1
%patch441 -p1
%patch442 -p1
%patch443 -p1
%patch444 -p1
%patch445 -p1
%patch446 -p1
%patch447 -p1
%patch448 -p1
%patch449 -p1
%patch450 -p1
%patch451 -p1
%patch452 -p1
%patch453 -p1
%patch454 -p1
%patch455 -p1
%patch456 -p1
%patch457 -p1
%patch458 -p1
%patch459 -p1
%patch460 -p1
%patch461 -p1
%patch462 -p1
%patch463 -p1
%patch464 -p1
%patch465 -p1
%patch466 -p1
%patch467 -p1
%patch468 -p1
%patch469 -p1
%patch470 -p1
%patch471 -p1

%patch500 -p1
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
%patch505 -p1
%patch506 -p1
%patch507 -p1
%patch508 -p1
%patch509 -p1
%patch510 -p1
%patch511 -p1
%patch512 -p1
%patch513 -p1
%patch514 -p1
%patch515 -p1
%patch516 -p1
%patch517 -p1
%patch518 -p1
%patch519 -p1
%patch520 -p1
%patch521 -p1
%patch522 -p1
%patch523 -p1
%patch524 -p1
%patch525 -p1
%patch526 -p1
%patch527 -p1
%patch528 -p1
%patch529 -p1
%patch530 -p1
%patch531 -p1
%patch532 -p1
%patch533 -p1
%patch534 -p1
%patch535 -p1
%patch536 -p1
%patch537 -p1
%patch538 -p1
%patch539 -p1
%patch540 -p1
%patch541 -p1
%patch542 -p1
%patch543 -p1
%patch544 -p1
%patch545 -p1
%patch546 -p1
%patch547 -p1
%patch548 -p1
%patch549 -p1
%patch550 -p1
%patch551 -p1
%patch552 -p1
%patch553 -p1
%patch554 -p1
%patch555 -p1
%patch556 -p1
%patch557 -p1
%patch558 -p1
%patch559 -p1
%patch560 -p1
%patch561 -p1
%patch562 -p1
%patch563 -p1
%patch564 -p1
%patch565 -p1
%patch566 -p1
%patch567 -p1
%patch568 -p1
%patch600 -p1
%patch601 -p1
%patch602 -p1
%patch603 -p1
%patch604 -p1
%patch605 -p1
%patch606 -p1
%patch607 -p1
%patch608 -p1
%patch609 -p1
%patch610 -p1
%patch611 -p1
%patch612 -p1
%patch613 -p1
%patch614 -p1
%patch615 -p1
%patch616 -p1
%patch617 -p1
%patch618 -p1
%patch619 -p1
%patch620 -p1
%patch621 -p1
%patch622 -p1
%patch623 -p1
%patch624 -p1
%patch625 -p1

%patch626 -p1
%patch627 -p1
%patch628 -p1
%patch629 -p1
%patch630 -p1
%patch631 -p1
%patch632 -p1
%patch633 -p1
%patch634 -p1
%patch635 -p1
%patch636 -p1
%patch637 -p1

%patch638 -p1
%patch639 -p1
%patch640 -p1
%patch641 -p1
%patch642 -p1
%patch643 -p1
%patch644 -p1
%patch645 -p1

%patch646 -p1
%patch647 -p1
%patch648 -p1
%patch649 -p1
%patch650 -p1
%patch651 -p1
%patch652 -p1

%patch661 -p1
%patch662 -p1
%patch663 -p1
%patch664 -p1
%patch665 -p1
%patch666 -p1
%patch667 -p1
%patch668 -p1
%patch669 -p1
%patch670 -p1
%patch671 -p1
%patch672 -p1
%patch673 -p1
%patch674 -p1
%patch675 -p1
%patch676 -p1
%patch677 -p1
%patch678 -p1
%patch679 -p1
%patch680 -p1
%patch681 -p1

%patch682 -p1
%patch683 -p1

%patch700 -p1
%patch701 -p1
%patch702 -p1
%patch703 -p1
%patch704 -p1
%patch705 -p1
%patch706 -p1
%patch707 -p1
%patch708 -p1
%patch709 -p1
%patch710 -p1
%patch711 -p1
%patch712 -p1
%patch713 -p1
%patch714 -p1

%patch720 -p1

%patch730 -p1
%patch731 -p1
%patch732 -p1
%patch733 -p1
%patch734 -p1

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=%{_libdir}
%configure --disable-mount-locking --enable-ignore-busy --with-libtirpc
make initdir=%{_initrddir} DONTSTRIP=1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m755 $RPM_BUILD_ROOT%{_initrddir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/autofs
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}
mkdir -p -m755 $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p -m755 $RPM_BUILD_ROOT/net
mkdir -p -m755 $RPM_BUILD_ROOT/misc

make install mandir=%{_mandir} initdir=%{_initrddir} INSTALLROOT=$RPM_BUILD_ROOT
make -C redhat
install -m 755 -d $RPM_BUILD_ROOT/misc
install -m 755 redhat/autofs.init $RPM_BUILD_ROOT%{_initrddir}/autofs
install -m 644 redhat/autofs.conf $RPM_BUILD_ROOT/etc/autofs.conf
install -m 644 redhat/autofs.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/autofs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add autofs

%postun
if [ $1 -ge 1 ] ; then
    /sbin/service autofs condrestart > /dev/null 2>&1 || :
fi

%preun
if [ "$1" = 0 ] ; then
    /sbin/service autofs stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del autofs
fi

%files
%defattr(-,root,root,-)
%doc CREDITS INSTALL COPY* README* patches/* samples/ldap* samples/autofs.schema
%{_initrddir}/autofs
%config(noreplace,missingok) /etc/auto.master
%config(noreplace,missingok) /etc/auto.misc
%config(noreplace,missingok) /etc/auto.net
%config(noreplace,missingok) /etc/auto.smb
%config(noreplace) /etc/autofs.conf
%config(noreplace) /etc/sysconfig/autofs
%config(noreplace) /etc/autofs_ldap_auth.conf
%{_sbindir}/automount
%{_mandir}/*/*
%{_libdir}/autofs/
/net
/misc

%changelog
* Wed Apr 9 2016 Ian Kent <ikent@redhat.com> - 5.0.5-123
- bz1333777 - RHEL6.7: shutdown / reboot hangs with findmnt in a readlink
  system call, doing path_walk and stuck in autofs4_wait
  - always set direct mounts catatonic at exit.
  - fix error handing in do_mount_indirect().
  - check negative cache much earlier.
  - log pipe read errors.
  - fix handle_mounts() termination condition check.
- Resolves: rhbz#1333777

* Wed Apr 6 2016 Ian Kent <ikent@redhat.com> - 5.0.5-122
- bz1233057 - Direct map does not expire if map is initially empty
  - don't schedule new alarms after readmap.
- Related: rhbz#1233057

* Tue Jan 19 2016 Ian Kent <ikent@redhat.com> - 5.0.5-121
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - Some Coverity identified fixes for recent changes for this bug.
  - fix memory leak in nisplus lookup_reinit().
  - fix memory leak in ldap do_init().
  - fix use after free in sun parser parse_init().
  - fix use after free in open_lookup().
  - fix typo in autofs_sasl_bind().
- Related: rhbz#1243525

* Mon Nov 30 2015 Ian Kent <ikent@redhat.com> - 5.0.5-120
- bz1161031 - RFE: autofs MAP_HASH_TABLE_SIZE description
  - update map_hash_table_size description.
- bz1248798 - Request to add a configuration option to force use of the map entry
  hostname for mounts
  - add configuration option to use fqdn in mounts.
- also update changelog with patches include from other bugs in rev 115 to support
  changes for bug 1243525.
  - fix left mount count return from umount_multi_triggers() (1227496).
  - fix return handling in sss lookup module (1227496).
  - move query dn calculation from do_bind() to do_connect() (1227496).
  - make do_connect() return a status (1227496).
  - make connect_to_server() return a status (1227496).
  - make find_dc_server() return a status (1227496).
  - make find_server() return a status (1227496).
  - fix return handling of do_reconnect() in ldap module (1227496).
  - fix race accessing qdn in get_query_dn() (1084254).
  - init qdn before use in get_query_dn() (1084254).
  - fix direct mount stale instance flag reset (1232074).
- bz1263505 - Heavy program map usage can lead to a hang
  - fix out of order call in program map lookup.
- bz1238605 - On every system boot automount needs a restart to access NIS map
  - fix lsb service name in init script.
- bz1097864 - Duplicate mounts created or leftovers in mtab
  - revert special case cifs escapes.
- bz1203139 - Similar but unrelated NFS exports block proper mounting of
  "parent" mount point
  - remove unused offset handling code.
  - fix mount as you go offset selection.
- bz1222522 - Parent directory in nested mount gets unmounted while the child
  remains mounted
  - guard against incorrect umount return.
- bz1233057 - Direct map does not expire if map is initially empty
  - fix direct map expire not set for initail empty map.
- Resolves: rhbz#1161031 rhbz#1248798 rhbz#1227496 rhbz#1084254 rhbz#1232074
- Resolves: rhbz#1263505 rhbz#1238605 rhbz#1097864 rhbz#1203139 rhbz#1222522
- Resolves: rhbz#1233057

* Thu Oct 8 2015 Ian Kent <ikent@redhat.com> - 5.0.5-119
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - rework sasl connection concurrancy problem patch.
- Related: rhbz#1243525

* Wed Oct 7 2015 Ian Kent <ikent@redhat.com> - 5.0.5-118
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - fix unbind external mech.
  - fix sasl connection concurrancy problem.
- Related: rhbz#1243525

* Wed Oct 7 2015 Ian Kent <ikent@redhat.com> - 5.0.5-117
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - fix error handling on ldap bind fail patch again.
- Related: rhbz#1243525

* Mon Oct 5 2015 Ian Kent <ikent@redhat.com> - 5.0.5-116
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - fix mistake in the updated error handling on ldap bind fail patch.
- Related: rhbz#1243525

* Wed Sep 30 2015 Ian Kent <ikent@redhat.com> - 5.0.5-115
- bz1243525 - double free or corruption (fasttop) causes abort in ldap_int_tls_destroy
  - add dependent patch series.
  - add aditional bug fix patches, including updated error handling on ldap bind fail.
  - add reinit method and change lookup to use reinit instead of reopen for its shared
    libraries.
- Resolves: rhbz#1243525

* Fri Mar 13 2015 Ian Kent <ikent@redhat.com> - 5.0.5-113
- bz1201195 - autofs: MAPFMT_DEFAULT is not macro in lookup_program.c
  - fix macro usage in lookup_program.c.
- Resolves: rhbz#1201195

* Mon Feb 16 2015 Ian Kent <ikent@redhat.com> - 5.0.5-112
- bz1124083 - Autofs stopped mounting /net/hostname/mounts after seeing duplicate
  exports in the NFS server
  - fix use after free in patch to handle duplicate in multi mounts.
  - change log messages to try and make them more sensible.
- fix log entry for rev 5.0.5-111 below.
- Related: rhbz#1124083

* Thu Feb 12 2015 Ian Kent <ikent@redhat.com> - 5.0.5-111
- bz1153130 - autofs-5.0.5-109 with upgrade to RHEL 6.6 no longer recognizes
  +yp: in auto.master
  - fix fix master map type check.
- bz1156387 - autofs /net maps do not refresh list of shares exported on the
  NFS server
  - fix typo in update_hosts_mounts().
  - fix hosts map update on reload.
- bz1160446 - priv escalation via interpreter load path for program based
  automount maps
  - add a prefix to program map stdvars.
  - add config option to force use of program map stdvars.
- bz1175671 - automount segment fault in parse_sun.so for negative parser tests
  - fix incorrect check in parse_mount().
- bz1124083 - Autofs stopped mounting /net/hostname/mounts after seeing duplicate
  exports in the NFS server
  - fix fix map entry duplicate offset detection (dependednt patch).
  - handle duplicates in multi mounts.
- Resolves: rhbz#1153130 rhbz#1156387 rhbz#1160446 rhbz#1175671 rhbz#1124083

* Wed Nov 19 2014 Ian Kent <ikent@redhat.com> - 5.0.5-110
- bz1163957 - Autofs unable to mount indirect after attempt to mount wildcard
  - make negative cache update consistent for all lookup modules.
  - ensure negative cache isn't updated on remount.
  - dont add wildcard to negative cache.
- Resolves: rhbz#1163957

* Fri Aug 22 2014 Ian Kent <ikent@redhat.com> - 5.0.5-109
- bz994217 - RFE: RHEL6: Add am-utls RPM or equivalent am-utils functionality
  to other packages
  - fix memory leak in get_defaults_entry().
  - fix out of order clearing of options buffer.
  - fix reset amd lexer scan buffer.
  - ignore multiple commas in options strings.
- Related: rhnz#994217

* Thu Aug 21 2014 Ian Kent <ikent@redhat.com> - 5.0.5-108
- bz1130833 - Memory leak in get_exports
  - fix memory leak in create_client().
  - fix memory leak in get_exports().
- Resolves: rhbz#1130833

* Fri Jul 11 2014 Ian Kent <ikent@redhat.com> - 5.0.5-107
- bz994217 - RFE: RHEL6: Add am-utls RPM or equivalent am-utils functionality
  to other packages
  - force disable browse mode for amd format maps.
  - fix hosts map options check in lookup_amd_instance().
- Related: rhbz#994217

* Tue Jul 8 2014 Ian Kent <ikent@redhat.com> - 5.0.5-106
- bz994217 - RFE: RHEL6: Add am-utls RPM or equivalent am-utils functionality
  to other packages
  - Covarity motivated corrections.
    - fix leak in cache_push_mapent().
    - fix config entry read buffer not checked.
    - fix FILE pointer check in defaults_read_config().
    - fix memory leak in conf_amd_get_log_options().
    - fix signed comparison in inet_fill_net().
    - fix buffer size checks in get_network_proximity().
    - fix leak in get_network_proximity().
    - fix buffer size checks in merge_options().
    - check amd lex buffer len before copy.
    - add return check in ldap check_map_indirect().
    - check host macro is set before use.
    - check options length before use in parse_amd.c.
    - fix some out of order evaluations in parse_amd.c.
    - fix copy and paste error in dup_defaults_entry().
    - fix leak in parse_mount().
    - add mutex call return check in defaults.c.
- Related: rhbz#994217

* Thu Jun 19 2014 Ian Kent <ikent@redhat.com> - 5.0.5-105
- bz1081479 - autofs service fails to start when scheduling through satellite
  via remote command
  - dont allocate dev_ctl_ops too early.
- Resolves: rhbz#1081479

* Thu Jun 19 2014 Ian Kent <ikent@redhat.com> - 5.0.5-104
- bz1081285 - automount segfaults in tlsm_deferred_init
  - add serialization to sasl init.
- Resolves: rhbz#1081285

* Wed Jun 4 2014 Ian Kent <ikent@redhat.com> - 5.0.5-103
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - fix ldap_uri config update.
  - fix typo in conf_load_autofs_defaults().
  - fix hash on confg option add and delete.
  - add plus to path match pattern.
  - fix multi entry ldap option handling.
  - cleanup options in amd_parse.c.
  - allow empty value for some map options.
  - allow empty value in macro selectors.
- Related: rhbz#994217

* Thu May 15 2014 Ian Kent <ikent@redhat.com> - 5.0.5-102
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - fix expire when server not responding.
- Related: rhbz#994217

* Wed May 14 2014 Ian Kent <ikent@redhat.com> - 5.0.5-101
- bz1059549 - autofs negative cache not working for included map
  - fix fix negative status being reset on map read.
  - and adjust dependent patches later in series.
- Related: rhbz#1059549

* Thu May 8 2014 Ian Kent <ikent@redhat.com> - 5.0.5-100
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - once again actually change spec file revision.
- Related: rhbz#994217

* Thu May 8 2014 Ian Kent <ikent@redhat.com> - 5.0.5-99
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - actually bump revision on commit.
- Related: rhbz#994217

* Thu May 8 2014 Ian Kent <ikent@redhat.com> - 5.0.5-98
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - fix xfn sets incorrect lexer state.
  - fix old style key lookup.
- bz1083744 - autofs can ghost non-existent map entries given the right timing
  - remove patch dependence on map entry status.
- Related: rhbz#994217 rhbz#1083744

* Tue May 6 2014 Ian Kent <ikent@redhat.com> - 5.0.5-97
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - fix map format init in ldap lookup_init().
  - correct patch "fix master map source server unavialable handling"
  - fix typo in libtirpc file name.
  - fix incorrect max key length in defaults get_hash().
- Related: rhbz#994217

* Mon May 5 2014 Ian Kent <ikent@redhat.com> - 5.0.5-96
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - remove master_mutex_unlock() leftover.
  - don't reset errno.
  - fix out of order amd timestamp lookup.
  - fix ldap default schema config.
  - fix ldap default master map name config.
- Related: rhbz#994217

* Tue Apr 29 2014 Ian Kent <ikent@redhat.com> - 5.0.5-95
- bz994217 - RFE: RHEL6: Add am-utils RPM or equivalent am-utils functionality
  to other packages
  - add amd parser pre-patch series.
  - add amd parser series.
  - fix wildcard key lookup (5.1.0-beta1 patch).
- Resolves: rhbz#994217

* Tue Apr 22 2014 Ian Kent <ikent@redhat.com> - 5.0.5-94
- bz1083744 - autofs can ghost non-existent map entries given the right timing
  - fix use cache entry after free mistake.
  - check for non existent negative entries in lookup_ghost().
- bz1089576 - segfault in automount
  - fix reset flex scan buffer on init.
- Resolves: rhbz#1083744 rhbz#1089576

* Tue Apr 1 2014 Ian Kent <ikent@redhat.com> - 5.0.5-93
- bz1073197 - automount segfaults in do_remount_indirect() when
  scandir() returns -1
   - fix segmentation fault in do_remount_indirect().
- Resolves: rhbz#1073197

* Mon Mar 31 2014 Ian Kent <ikent@redhat.com> - 5.0.5-92
- bz1068999 - double free or corruption (fasttop) causes abort in
  ldap_int_tls_destroy
  - fix deadlock in init_ldap_connection().
  - extend libldap serialization.
- Resolves: rhbz#1068999

* Thu Mar 27 2014 Ian Kent <ikent@redhat.com> - 5.0.5-91
- fix changelog email address.
- bz1059549 - autofs negative cache not working for included map
  - fix negative status being reset on map read.
- bz1046164 - autofs-5.0.5-88.el6 no longer queries the portmapper for NFS
  v2/v3 mounts
  - get_nfs_info() should query portmapper if port is not given
- bz1036032 - with IPv6 link-local address parse err: invalid character "%"
  - fix ipv6 link local address handling.
-Resolves: rhbz#1059549 rhbz#1046164 rhbz#1036032

* Thu Feb 27 2014 Ian Kent <ikent@redhat.com> - 5.0.5-90
- bz1038696 - autofs-5.0.5-88.el6 breaks maps that have a -v in the options
  - fix fix options compare.
- Related: rhbz#1038696

* Fri Feb 21 2014 Ian Kent <ikent@redhat.com> - 5.0.5-89
- bz1038696 - autofs-5.0.5-88.el6 breaks maps that have a -v in the options
  - fix options compare.
- Resolves: rhbz#1038696

* Wed Oct 30 2013 Ian Kent <ikent@redhat.com> - 5.0.5-88
- bz996749 - segmentation fault in ber_memalloc_x function when running automount
  - fix crash due to thread unsafe use of libldap.
- Resolves: rhbz#996749

* Thu Oct 10 2013 Ian Kent <ikent@redhat.com> - 5.0.5-87
- bz1004129 - automounter load balancing with replicated servers broken
  by whitespace patch
  - fix get_nfs_info() probe.
- Resolves: rhbz#1004129

* Thu Sep 13 2013 Ian Kent <ikent@redhat.com> - 5.0.5-86
- bz852327 - RFE: feature to dump automount maps in native file format
  - add missing ">" to man page.
  - handle path name when when given instead of only map name.
- Related: rhbz#852327

* Thu Sep 12 2013 Ian Kent <ikent@redhat.com> - 5.0.5-85
- bz852327 - RFE: feature to dump automount maps in native file format
  - add missing ">" to usage output.
- Related: rhbz#852327

* Tue Sep 10 2013 Ian Kent <ikent@redhat.com> - 5.0.5-84
- bz1002896 - Race condition or other deadlocking issue on expire code path
  - expire thread use pending mutex.
- Resolves: rhbz#1002896

* Wed Aug 28 2013 Ian Kent <ikent@redhat.com> - 5.0.5-83
- bz852327 - RFE: feature to dump automount maps in native file format
  - add missing "\n" to usage output.
- Related: rhbz#852327

* Thu Aug 16 2013 Ian Kent <ikent@redhat.com> - 5.0.5-82
- bz859078 - NFSv4 UDP packet sent during automounting
  - only probe specific nfs version when requested
- Related: rhbz#859078

* Wed Aug 14 2013 Ian Kent <ikent@redhat.com> - 5.0.5-81
- bz852327 - RFE: feature to dump automount maps in native file format
  - update automount(8) usage message also.
- Related: rhbz#852327 

* Mon Aug 12 2013 Ian Kent <ikent@redhat.com> - 5.0.5-80
- bz994296 - "autofs reload" causes automount to stop running when multiple
  maps are removed from auto.master
  - syncronize handle_mounts() shutdown.
- bz994297 - Wildcard in nested mounts regression
  - fix wildcard multi map regression.
  - fix fix wildcard multi map regression.
- Resolves: rhbz#994296 rhbz#994297

* Wed Aug 7 2013 Ian Kent <ikent@redhat.com> - 5.0.5-79
- bz982103 - default timeout is inconsistent in the configuration file
  /etc/sysconfig/autofs
  - improve timeout option description.
- bz852327 - RFE: feature to dump automount maps in native file format
  - make dump maps check for duplicate indirect mounts.
  - fix dumpmaps multi output.
  - try and cleanup after dumpmaps.
  - teach dumpmaps to output simple key value pairs.
- Resolves: rhbz#98210 rhbz#852327

* Mon Jul 29 2013 Ian Kent <ikent@redhat.com> - 5.0.5-78
-bz903944 - autofs does not use local mounts on non-replicated entries
 - fix not bind mounting local filesystem.
- bz979929 - automount segfaults in mount_nfs.so when one of the network
  interfaces is marked DOWN
  - fix interface address null check/
- Resolves: rhbz#903944 rhbz#979929

* Thu Jul 18 2013 Ian Kent <ikent@redhat.com> - 5.0.5-77
- bz859078 - NFSv4 UDP packet sent during automounting
  - mount_nfs.so to honor explicit NFSv4 requests.
  - mount_nfs.so fix port=0 option behavior v3.
  - probe each nfs version in turn for singleton mounts.
  - check for protocol option.
- bz886623 - [autofs] Automounting NFS via RDMA fails
  - dont probe rdma mounts.
- bz974884 - RFE: Change MAX_OPEN_FILES within autofs to 40960 or tunable
  - use ulimit max open files if greater than internal maximum.
- Resolves: rhbz#859078 rhbz#886623 rhbz#974884

* Thu Jun 6 2013 Ian Kent <ikent@redhat.com> - 5.0.5-76
- bz971131 - autofs returns a syntax error when trying to pass an SELinux
  context= option in the LDAP automount config
  - fix master map mount options matching.
  - fix master map bogus keywork match.
- Resolves: rhbz#971131

* Wed Apr 22 2013 Ian Kent <ikent@redhat.com> - 5.0.5-75
- bz773127 - automount deadlock when triggering --bind mounts
  - fix recursive mount deadlock.
  - increase file map read buffer size.
  - dont use pthread_rwlock_tryrdlock().
- fix changelog entry revision number.
- Related: rhbz#773127

* Wed Mar 13 2013 Ian Kent <ikent@redhat.com> - 5.0.5-74
- bz908020 - autofs mount failures when mounting multiple nfs mounts at
  the same time.
  - use numeric protocol ids instead of protoent structs.
- Resolves: rhbz#908020

* Wed Jan 9 2013 Ian Kent <ikent@redhat.com> - 5.0.5-73
- bz892846 - segfault in get_query_dn()
  - fix segfault in get_query_dn().
- Resolves: rhbz#892846

* Wed Jan 9 2013 Ian Kent <ikent@redhat.com> - 5.0.5-72
- bz889055 - RHEL6.4 autofs initscript not LSB compliant
  - fix init script status return.
- Resolves: rhbz#889055

* Wed Jan 2 2013 Ian Kent <ikent@redhat.com> - 5.0.5-71
- bz836422 - autofs /net maps do not refresh list of shares exported on
  the NFS server
  - fix submount offset delete.
- Related: rhbz#836422

* Wed Nov 27 2012 Ian Kent <ikent@redhat.com> - 5.0.5-70
- bz880242 - autofs service status fails on rhel 6.4 with version
  autofs-5.0.5-64.el6.x86_64
  - update configure of back ported patch.
- Related: rhbz#880242

* Wed Nov 27 2012 Ian Kent <ikent@redhat.com> - 5.0.5-69
- bz880242 - autofs service status fails on rhel 6.4 with version
  autofs-5.0.5-64.el6.x86_64
  - actually add the backported patch.
- Related: rhbz#880242

* Wed Nov 27 2012 Ian Kent <ikent@redhat.com> - 5.0.5-68
- bz880242 - autofs service status fails on rhel 6.4 with version
  autofs-5.0.5-64.el6.x86_64
  - remove pid file substution patch.
  - add backported upstream patch to add piddir to configure.
- Related: rhbz#880242

* Tue Nov 27 2012 Ian Kent <ikent@redhat.com> - 5.0.5-67
- bz880242 - autofs service status fails on rhel 6.4 with version
  autofs-5.0.5-64.el6.x86_64
  - fix pid file substitution in init script.
- Resolves: rhbz#880242

* Tue Nov 20 2012 Ian Kent <ikent@redhat.com> - 5.0.5-66
- bz866338 - update the man pages to describe 'nobind' option current behaviour
  - fix nobind man page description.
- Resolves: rhbz#866338

* Tue Nov 20 2012 Ian Kent <ikent@redhat.com> - 5.0.5-65
- bz836422 - autofs /net maps do not refresh list of shares exported on
  the NFS server
  - fix map entry duplicate offset detection.
- Related: rhbz#836422

* Mon Oct 26 2012 Ian Kent <ikent@redhat.com> - 5.0.5-64
- bz868973 - autofs leaks UDP sockets when a NFSv4 server is not available
  - destroy the socket when rpc_ping_proto() failed for NFSv4.
- Resolves: rhbz#868973

* Mon Oct 15 2012 Ian Kent <ikent@redhat.com> - 5.0.5-63
- bz866396 - sssd autofs interface library packaging change
  - fix BuildRequires for latest sssd packaging.
- Resolves: rhbz#866396

* Mon Oct 15 2012 Ian Kent <ikent@redhat.com> - 5.0.5-62
- bz860184 - service autofs status should be accessible to non privileged users
  - allow non root user to check status
- revert - fix build fail, sssd requires libldb.
- Resolves: rhbz#860184
- Related: rhbz#856296

* Mon Oct 15 2012 Ian Kent <ikent@redhat.com> - 5.0.5-61
- fix build fail, sssd requires libldb.
- Related: rhbz#856296

* Mon Oct 15 2012 Ian Kent <ikent@redhat.com> - 5.0.5-60
- bz865311 - Wrong MOUNT_WAIT description in /etc/sysconfig/autofs
  - documentation fix some typos and misleading comments.
  - make description of default MOUNT_WAIT setting clear.
- Resolves: rhbz#865311

* Wed Oct 10 2012 Ian Kent <ikent@redhat.com> - 5.0.5-59
- bz856296 - Duplicate enty for the /net map cause /etc/init.d/autofs stop to
  fail
  - fix null map entry order handling.
- Resolves: rhbz#856296

* Tue Sep 25 2012 Ian Kent <ikent@redhat.com> - 5.0.5-58
- bz859947 - no --timeout option usage demonstrated in auto.master FORMAT
  options man page section
  - add timeout option description to man page.
- Resolves: rhbz#859947

* Mon Sep 24 2012 Ian Kent <ikent@redhat.com> - 5.0.5-57
- bz585059 - autofs5 init script times out before automount exits and
  incorrectly shows that autofs5 stop failed
  - dont wait forever to restart.
- bz845512 - autofs initscript Usage case problem
  - include usage in usage message.
- Resolves: rhbz#585059 rhbz#845512

* Wed Sep 19 2012 Ian Kent <ikent@redhat.com> - 5.0.5-56
- bz836422 - autofs /net maps do not refresh list of shares exported on
  the NFS server
  - fix expire race.
  - fix remount deadlock.
  - fix umount recovery of busy direct mount.
  - fix offset mount point directory removal.
  - remove move mount code.
  - fix remount of multi mount.
  - fix devce ioctl alloc path check.
  - refactor hosts lookup module.
  - remove cache update from parse_mount().
  - add function to delete offset cache entry.
  - allow update of multi mount offset entries.
  - add hup signal handling to hosts map.
  - fix offset dir removal.
- Resolves: rhbz#836422

* Thu Sep 6 2012 Ian Kent <ikent@redhat.com> - 5.0.5-55
- bz846870 - RFE: timeout option cannot be configured individually with
  multiple direct map entries
  - add nobind option.
  - dont bind nfs mount if nobind is set.
  - update ->timeout() function to not return timeout.
  - move timeout to map_source (allow per direct map timeout).
- bz822733 - Fix autofs attempting to download entire LDAP map at startup
  - report map not read when debug logging.
- bz827024 - automount segfaults during the boot-up sequence
  - fix mountd vers retry.
  - fix initialization in rpc create_client().
  - fix libtirpc name clash.
  - fix get_nfs_info() can incorrectly fail.
- bz834641 - autofs requires portmapper on server for NFSv4 mounts
  - fix nfs4 contacts portmap.
- bz819703 - The local IPv6 interface matching code should be improved
  - fix ipv6 proximity calculation.
- Resolves: rhbz#846870 rhbz#822733 rhbz#827024 rhbz#834641 rhbz#819703

* Thu Apr 5 2012 Ian Kent <ikent@redhat.com> - 5.0.5-54
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - revert fix libsss_autofs not available at build.
- Related: rhbz#683523

* Thu Apr 5 2012 Ian Kent <ikent@redhat.com> - 5.0.5-53
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - fix libsss_autofs not available at build.
- Related: rhbz#683523

* Thu Apr 5 2012 Ian Kent <ikent@redhat.com> - 5.0.5-52
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - also add BuildRequires for libsss_autofs.
- Related: rhbz#683523

* Thu Apr 5 2012 Ian Kent <ikent@redhat.com> - 5.0.5-51
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - fix configure string length tests for sss library. 
  - add BuildRequires for sssd to ensure sss support is added.
- Related: rhbz#683523

* Thu Apr 5 2012 Ian Kent <ikent@redhat.com> - 5.0.5-50
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - fix dlopen() error handling in sss module.
- Related: rhbz#683523

* Wed Apr 4 2012 Ian Kent <ikent@redhat.com> - 5.0.5-49
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - fix sss wildcard match.
- Related: rhbz#683523

* Thu Mar 22 2012 Ian Kent <ikent@redhat.com> - 5.0.5-48
- bz787595 - /bin/ls --color=auto takes very long on dir with lots of symlinks to
  automounted NFS filesystems
  - use strtok_r() in linux_version_code().
- Related: rhbz#787595

* Wed Mar 14 2012 Ian Kent <ikent@redhat.com> - 5.0.5-47
- bz787595 - /bin/ls --color=auto takes very long on dir with lots of symlinks to
  automounted NFS filesystems
  - allow MOUNT_WAIT to override probe.
  - improve UDP RPC timeout handling.
- Related: rhbz#787595

* Tue Mar 6 2012 Ian Kent <ikent@redhat.com> - 5.0.5-46
- bz787595 - /bin/ls --color=auto takes very long on dir with lots of symlinks to
  automounted NFS filesystems
  - fix rework error return handling in rpc code.
- Related: rhbz#787595

* Wed Feb 29 2012 Ian Kent <ikent@redhat.com> - 5.0.5-45
- bz787595 - /bin/ls --color=auto takes very long on dir with lots of symlinks to
  automounted NFS filesystems
  - fix function to check mount.nfs version.
- Related: rhbz#787595

* Wed Feb 29 2012 Ian Kent <ikent@redhat.com> - 5.0.5-44
- bz787595 - /bin/ls --color=auto takes very long on dir with lots of symlinks to
  automounted NFS filesystems
  - add kernel verion check function.
  - add function to check mount.nfs version.
  - reinstate singleton mount probe.
  - rework error return handling in rpc code.
  - catch EHOSTUNREACH and bail out early.
- Resolves: rhbz#787595

* Fri Feb 24 2012 Ian Kent <ikent@redhat.com> - 5.0.5-43
- bz790674 - automount deadlocking
  - fix submount shutdown race.
  - fix wait for master source mutex (+ fix).
- Resolves: rhbz#790674

* Mon Feb 20 2012 Ian Kent <ikent@redhat.com> - 5.0.5-42
- bz772946 - autofs-5.0.5-39.el6 breaks indirect NIS maps
  - fix fix map source check in file lookup.
- bz745527 - autofs init.d script does not handle improper arguments correctly
  - fix init script usage message.
- bz782169 - The /net automount map fails for some export styles
  - ignore duplicate exports in auto.net.
- bz760945 - /net and /misc should be in autofs RPM
  - add /net and /misc to files list and create during install.
- Resolves: rhbz#772946 rhbz#745527 rhbz#782169 rhbz#760945

* Wed Feb 15 2012 Ian Kent <ikent@redhat.com> - 5.0.5-41
- bz753964 - cannot automount NFSv4 over IPv6
  - fix ipv6 name for lookup.
  - fix libtirpc ipv6 check.
  - fix ipv6 name for lookup fix.
  - fix ipv6 name lookup check.
  - fix ipv6 rpc calls.
  - fix ipv6 configure check.
- bz683523 - [RFE] Use sssd (when available) for automounter map
  lookups in LDAP
  - add sss lookup module.
  - teach automount about sss source.
- Resolves: rhbz#753964 rhbz#683523

* Thu Jan 19 2012 Jeff Moyer <jmoyer@redhat.com> - 5.0.5-40
- bz772356 - autofs-5.0.5-39.el6.x86_64 fails to load some LDAP maps
  - fix improve mount location error reporting. (Ian Kent)
- Resolves: rhbz#772356

* Mon Aug 29 2011 Ian Kent <ikent@redhat.com> - 5.0.5-39
- bz732667 - Defects added by downstream patches
  - code analysis defect fixes, installment 1.
- Resolves: rhbz#732667

* Mon Aug 15 2011 Ian Kent <ikent@redhat.com> - 5.0.5-38
- bz700136 - autofs/automount 5.0.5 error in mounting expanded entry
  - improve mount location error reporting 
- Resolves: rhbz#700136

* Sun Aug 7 2011 Ian Kent <ikent@redhat.com> - 5.0.5-37
- bz704416 - RFE: automounter to dump maps
  - fix dumpmaps not reading maps.
- Related: rhbz#704416

* Fri Aug 5 2011 Ian Kent <ikent@redhat.com> - 5.0.5-36
- bz704928 - autofs should support paged results from ldap server on
  ppc64 and s390x
  - fix paged query more results check.
- Resolves: rhbz#704928

* Thu Aug 4 2011 Ian Kent <ikent@redhat.com> - 5.0.5-35
- bz725931 - Fix GPL v3 dependency in autofs.
  - replace GPLv3 with GPLv2 code for SRV record handling.
- Resolves: rhbz#725931 

* Tue Jul 19 2011 Ian Kent <ikent@redhat.com> - 5.0.5-34
- bz718927 - Lock ordering problem on re-load of direct maps
  - fix null cache deadlock.
- Resolves: rhbz#718927

* Wed Jul 6 2011 Ian Kent <ikent@redhat.com> - 5.0.5-33
- bz704228 - AD/LDAP connection using GSSAPI auth fails with Error: An invalid
  name was supplied (Hostname cannot be canonicalized)
  - check each dc server.
- Related: rhbz#704228

* Wed Jul 6 2011 Ian Kent <ikent@redhat.com> - 5.0.5-32
- bz704940 - autofs-5.0.1-0.rc2.131.el5_4.1 is missing man 8 auto.master
  - automount(8) man page correction.
- bz704929 - automount hangs with nested mounts using YP lookups
  - don't hold lock for simple mounts.
- bz703332 - autofs fails to find duplicate key after key removal
  - fix prune cache valid check.
  - fix map source check in file lookup.
- bz704933 - [RHEL 5.4] automounter dies with pthreads error
  - wait for master source mutex.
- bz704927 - autofs should support paged results from ldap server
  - auto adjust ldap page size.
  - fix paged ldap map read.
- bz704932 - [RFE] Support for encrypted secret in /etc/autofs_ldap_auth.conf
  - add base64 password encode.
- bz704416 - RFE: automounter to dump maps
  - add dump maps option.
- bz704935 - [RFE] resolve negative cache invalidation on signal to automount
  - reset negative status on cache prune.
- bz704937 - Segmentation fault when looking up '*.'
  - fix wildcard map entry match.
- bz704228 - AD/LDAP connection using GSSAPI auth fails with Error: An invalid
  name was supplied (Hostname cannot be canonicalized)
  - fix sasl bind host name selection.
- bz692816 - automount does not perform a sanity check of server name in
  configuration
  - fix sanity checks for brackets in server name.
- bz704939 - automount segfaults in lookup_mount
  - mapent becomes negative during lookup.
- Resolves: rhbz#704940 rhbz#704929 rhbz#703332 rhbz#704933 rhbz#704927
- Resolves: rhbz#704932 rhbz#704416 rhbz#704935 rhbz#704937 rhbz#704228
- Resolves: rhbz#692816 rhbz#704939

* Fri Apr 29 2011 Ian Kent <ikent@redhat.com> - 5.0.5-31
- bz700691 - autofs sometimes stops expiring mounts
  - fix next task list update race.
  - fix stale map read.
- bz700697 - autofs with null maps specified in auto.master segfaults on reload
  - fix null cache clean.
- Resolves: rhbz#700691 rhbz#700697

* Thu Feb 10 2011 Ian Kent <ikent@redhat.com> - 5.0.5-30
- bz579963 - autmount maps stored in LDAP can not be read using simple
  authenticated binds
  - remove ERR_remove_state() openssl call. 
- bz520844 - [RFE] autofs should honor admin supplied server weights in maps
  - update patch, also override proximity.
- Related: rhbz#579963 rhbz#520844

* Thu Feb 3 2011 Ian Kent <ikent@redhat.com> - 5.0.5-29
- bz579963 - autmount maps stored in LDAP can not be read using simple
  authenticated binds
  - deal with Kerberos library dependency.
- Related: rhbz#579963

* Fri Jan 28 2011 Ian Kent <ikent@redhat.com> - 5.0.5-28
- bz630954 - "service autofs reload" does not pick the updated entry
  from NIS autofs direct map
  - fix patch not actually applied.
- Related: rhbz#630954

* Fri Jan 28 2011 Ian Kent <ikent@redhat.com> - 5.0.5-27
- bz616426 - autofs initscript should implement force-reload and try-restart
  - add lsb force-reload and try-restart
- bz629359 - [RFE] Automounter debug mode should include IP addresses
  - include ip address in debug logging.
  - mount using address for DNS round robin host names.
- Resolves: rhbz#616426 rhbz#629359

* Thu Jan 20 2011 Ian Kent <ikent@redhat.com> - 5.0.5-26
- bz666340 - autofs handle isspace() char incorrectly
  - fix isspace() wild card substition.
- Resolves: rhbz#666340

* Wed Jan 19 2011 Ian Kent <ikent@redhat.com> - 5.0.5-25
- check and fix CHANGELOG hunk not applying for bz572608.
- Related: rhbz#572608

* Wed Jan 19 2011 Ian Kent <ikent@redhat.com> - 5.0.5-24
- bz572608 - autofs has unncessary wakeups
  - remove state machine timed wait.
- bz577099 - RFE: Add locality LDAP attribute to
  - add locality as valid ldap master map attribute
- bz650009 - automount hangs on startup when started with an already
  mounted cifs share
  - fix remount locking
- bz624444 - 'Restart' option does not work for autofs initd script
  - fix restart.
- bz630954 - "service autofs reload" does not pick the updated entry
  from NIS autofs direct map
  - fix direct map not updating on reread
- bz629480 - include autofs support for SASL External authentication
  using certificates
  - add external bind method
- bz579963 - autmount maps stored in LDAP can not be read using simple
  authenticated binds
  - add simple bind authentication
- bz520844 - [RFE] autofs should honor admin supplied server weights in
  maps
  - use weight only for server selection.
- Resolves: rhbz#572608 rhbz#577099 rhbz#650009 rhbz#624444 rhbz#630954
- Resolves: rhbz#629480 rhbz#579963 rhbz#520844

* Thu Jul 1 2010 Ian Kent <ikent@redhat.com> - 5.0.5-23
- bz597944 - autofs5: segfault in close_mount()
  - add mutex to serialize access to mount module handle in parse module.
  - dont check null cache on expire.
  - fix null cache race.
  - fix cache_init() on source re-read.
  - fold autofs-5.0.5-fix-memory-leak-on-reload.patch into
    fix cache_init() on source re-read patch where it belongs.
- bz594565 - If maps include both file and nis maps, included nis maps which
    worked on RHEL 5.3 no longer work on RHEL 5.4
  - fix negative cache included map lookup
- Resolves: rhhz#597944 rhbz#594565

* Thu Jun 3 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-22
- bz578128 - Service autofs initscript not LSB compliant
- bz577097 - automount aborts when it authenticates by DIGEST-MD5
- Resolves: rhbz#578128 rhbz#577097

* Thu Apr 8 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-21
-bz578677 - random server selection is not random if any host is on a different network
 - fix random selection for host on different network
- Resolves: rhbz#578677

* Wed Apr 7 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-20
- bz529347 - Missing man-pages.
  - add autofs_ldap_auth.conf man page.
- Resolves: rhbz#529347

* Mon Mar 29 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-19
- bz563769 - [RFE] autofs needs to wait for a network up event before starting
  - fix get query dn failure
- bz574309 - autofs cannot mount the folder name including "&"
  - fix ampersand escape in auto.smb.
- bz465463 - CRM 1203376 autofs/automount to mount nfs4 or nfs3 for mixed servers
  - make nfs4 default for RedHat replicated selection configuration.
- Resolves: rhbz#574309 rhbz#465463
- Related: rhbz#563769

* Wed Mar 3 2010 Ian Kent <kpnt@redhat.com> - 1:5.0.5-18
- bz563769 - [RFE] autofs needs to wait for a network up event before starting
  - dont connect at ldap lookup module init.
  - fix reconnect get base dn.
- bz563772 - automount cannot use rpc ping to select from list of replicated servers
  - fix random selection option.
- bz563773 - [RHEL 5] RHEL5.4 TIMEOUT=0 automount constantly unmount fileystems
  - fix disable timeout.
- bz563777 - Incorrect strdup() return value check in lib/defaults.c:get_env_string()
  - fix strdup() return value check.
- Resolves: rhbz#563769 rhbz#563772 rhbz#563773 rhbz#563777

* Tue Dec 8 2009 Ian Kent <kpnt@redhat.com> - 1:5.0.5-17
- fix memory leak on reload (bz545137).

* Thu Dec 3 2009 Ian Kent <kpnt@redhat.com> - 1:5.0.5-15
- fix rpc fail on large export list (bz543023).

* Mon Nov 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-13
- check for path mount location in generic module.
- dont fail mount on access fail.

* Wed Nov 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-11
- fix pidof init script usage.

* Mon Nov 23 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-9
- fix timeout in connect_nb().

* Mon Nov 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-7
- fix ext4 "preen" fsck at mount.
- don't use master_lex_destroy() to clear parse buffer.
- make documentation for set-log-priority clearer.

* Tue Nov 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-4
- fix included map read fail handling.
- refactor ldap sasl authentication bind to eliminate extra connect
  causing some servers to reject the request.
- add mount wait parameter to allow timeout of mount requests to
  unresponsive servers.
- special case cifs escape handling.
- fix libxml2 workaround configure.
- more code analysis corrections (and fix a typo in an init script).
- fix backwards #ifndef INET6.
- fix stale initialization for file map instance.

* Fri Sep 4 2009 Ian Kent <ikent@redhat.com> - 1:5.0.5-1
- update source to latest upstream version.
  - this is essentially a consolidation of the patches already in this rpm.
- add dist tag to match latest RHEL-5 package tag format.

* Thu Sep 3 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-39
- fix libxml2 non-thread-safe calls.
- fix direct map cache locking.
- fix patch "dont umount existing direct mount on reread" deadlock.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-34
- fix typo in patch to allow dumping core.

* Wed Jul 15 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-32
- fix an RPC fd leak.
- don't block signals we expect to dump core.
- fix pthread push order in expire_proc_direct().

* Fri Jun 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-30
- fix incorrect dclist free.
- srv lookup handle endianness.
- fix bug introduced by library reload changes which causes autofs to
  not release mount thread resources when using submounts.
- fix notify mount message path.
- try harder to work out if we created mount point at remount.
- fix double free in do_sasl_bind().
- manual umount recovery fixes.
- fix map type info parse error.

* Mon May 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-28
- use intr option as hosts mount default.
- sync kernel includes with upstream kernel.
- dont umount existing direct mount on master re-read.
- fix incorrect shutdown introduced by library relaod fixes.
- improve manual umount recovery.
- dont fail on ipv6 address when adding host.
- always read file maps multi map fix.
- always read file maps key lookup fixes.
- add support for LDAP_URI="ldap:///<domain db>" SRV RR lookup.

* Thu Apr 16 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-26
- fix lsb init script header.
- fix memory leak reading ldap master map.
- fix st_remove_tasks() locking.
- reset flex scanner when setting buffer.
- zero s_magic is valid.

* Mon Mar 30 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-24
- clear rpc client on lookup fail.

* Fri Mar 20 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-23
- fix call restorecon when misc device file doesn't exist.

* Wed Mar 18 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-22
- use misc device ioctl interface by default, if available.

* Tue Mar 17 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-21
- fix file map lookup when reading included or nsswitch sources.
  - a regression introduced by file map lookup optimisation in rev 9.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-20
- add LSB init script parameter block.

* Fri Mar 13 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-19
- another easy alloca replacements fix.

* Thu Mar 12 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-18
- fix return start status on fail.
- fix double free in expire_proc().

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-17
- fix bad token declaration in master map parser.

* Wed Feb 25 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-16
- correct mkdir command in %%install section, bz481132.

* Tue Feb 24 2009 Ian Kent <ikent@redhat.com> - 1:5.0.4-15
- fix array out of bounds accesses and cleanup couple of other alloca() calls.
- Undo mistake in copy order for submount path introduced by rev 11 patch.
- add check for alternate libxml2 library for libxml2 tsd workaround.
- add check for alternate libtirpc library for libtirpc tsd workaround.
- cleanup configure defines for libtirpc.
- add WITH_LIBTIRPC to -V status report.
- add libtirpc-devel to BuildRequires.
- add nfs mount protocol default configuration option.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ian Kent <ikent@redhat.com> - 5.0.4-10
- fix mntent.h not included before use of setmntent_r().

* Mon Feb 16 2009 Ian Kent <ikent@redhat.com> - 5.0.4-9
- fix hosts map use after free.
- fix uri list locking (again).
- check for stale SASL credentials upon connect fail.
- add "forcestart" and "forcerestart" init script options to allow
  use of 5.0.3 strartup behavior if required.
- always read entire file map into cache to speed lookups.
- make MAX_ERR_BUF and PARSE_MAX_BUF use easier to audit.
- make some easy alloca replacements.
- update to configure libtirpc if present.
- update to provide ipv6 name and address support.
- update to provide ipv6 address parsing.

* Thu Feb 5 2009 Ian Kent <ikent@redhat.com> - 5.0.4-8
- rename program map parsing bug fix patch.
- use CLOEXEC flag functionality for setmntent also, if present.

* Wed Jan 21 2009 Jeff Moyer <jmoyer@redhat.com> - 5.0.4-6
- fix a bug in the program map parsing routine

* Thu Jan 15 2009 Ian Kent <kent@redhat.com> - 5.0.4-5
- fix negative caching of non-existent keys.
- fix ldap library detection in configure.
- use CLOEXEC flag functionality if present.
- fix select(2) fd limit.
- make hash table scale to thousands of entries.

* Wed Dec 3 2008 Ian Kent <kent@redhat.com> - 5.0.4-4
- fix nested submount expire deadlock.

* Wed Nov 19 2008 Ian Kent <kent@redhat.com> - 5.0.4-3
- fix libxml2 version check for deciding whether to use workaround.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-2
- Fix tag confusion.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.4-1
- Upstream source version 5.0.4.

* Tue Nov 11 2008 Ian Kent <kent@redhat.com> - 5.0.3-32
- correct buffer length setting in autofs-5.0.3-fix-ifc-buff-size-fix.patch.

* Sun Nov 2 2008 Ian Kent <kent@redhat.com> - 5.0.3-30
- fix segv during library re-open.
- fix incorrect pthreads condition handling for expire requests.
- fix master map lexer eval order.
- fix bad alloca usage.

* Thu Oct 23 2008 Ian Kent <ikent@redhat.com> - 5.0.3-28
- don't close file handle for rootless direct mounti-mount at mount.
- wait submount expire thread completion when expire successful.
- add inadvertantly ommitted server list locking in LDAP module.

* Fri Oct 10 2008 Ian Kent <ikent@redhat.com> - 5.0.3-26
- add map-type-in-map-name fix patch to sync with upstream and RHEL.
- don't readmap on HUP for new mount.
- add NIS_PARTIAL to map entry not found check and fix use after free bug.

* Fri Sep 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-25
- fix fd leak at multi-mount non-fatal mount fail.
- fix incorrect multi-mount mountpoint calcualtion.

* Fri Sep 19 2008 Ian Kent <ikent@redhat.com> - 5.0.3-23
- add upstream bug fixes
  - bug fix for mtab check.
  - bug fix for zero length nis key.
  - update for ifc buffer handling.
  - bug fix for kernel automount handling.
- warning: I found a bunch of patches that were present but not
  being applied.
  
* Mon Aug 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-21
- add upstream bug fix patches
  - add command line option to override is running check.
  - don't use proc fs for is running check.
  - fix fail on included browse map not found.
  - fix incorrect multi source messages.
  - clear stale flag on map read.
  - fix proximity other rpc ping timeout.
  - refactor mount request vars code.
  - make handle_mounts startup condition distinct.
  - fix submount shutdown handling.
  - try not to block on expire.
  - add configuration paramter UMOUNT_WAIT.
  - fix multi mount race.
  - fix nfs4 colon escape handling.
  - check replicated list after probe.
  - add replicated server selection debug logging.
  - update replicated server selection documentation.
  - use /dev/urandom instead of /dev/random.
  - check for mtab pointing to /proc/mounts.
  - fix interface config buffer size.
  - fix percent hack heap corruption.

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.3-19
- change conflicts to requires
- fix license tag

* Mon Jun 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-18
- don't abuse the ap->ghost field on NFS mount.
- multi-map doesn't pickup NIS updates automatically.
- eliminate redundant DNS name lookups.
- mount thread create condition handling fix.
- allow directory create on NFS root.
- check direct mount path length.
- fix incorrect in check in get user info.
- fix a couple of memory leaks.

* Wed May 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-16
- update patches, documentation and comments only change.
- rename patch and add to CVS.

* Mon May 12 2008 Ian Kent <ikent@redhat.com> - 5.0.3-14
- check for nohide mounts (bz 442618).
- ignore nsswitch sources that aren't supported (bz 445880).

* Thu Apr 17 2008 Ian Kent <ikent@redhat.com> - 5.0.3-13
- fix typo in patch for incorrect pthreads condition handling patch.

* Mon Apr 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-12
- fix incorrect pthreads condition handling for mount requests.

* Sun Apr 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-11
- and another try at fixing lexer matching map type in map name.

* Sun Mar 30 2008 Ian Kent <ikent@redhat.com> - 5.0.3-10
- another try a fixing lexer matching map type in map name.

* Wed Mar 26 2008 Ian Kent <ikent@redhat.com> - 5.0.3-9
- fix lexer ambiguity in match when map type name is included in map name.

* Mon Mar 24 2008 Ian Kent <ikent@redhat.com> - 5.0.3-8
- revert miscellaneous device node related patches.
- add missing check for zero length NIS key.
- fix incorrect match of map type name when included in map name.
- update rev 7 sasl callbacks patch.

* Thu Mar 20 2008 Ian Kent <ikent@redhat.com> - 5.0.3-7
- add patch to initialize sasl callbacks unconditionally on autofs
  LDAP lookup library load.

* Mon Feb 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-6
- fix expire calling kernel more often than needed.
- fix unlink of mount tree incorrectly causing autofs mount fail.
- add miscellaneous device node interface library.
- use miscellaneous device node, if available, for active restart.
- device node and active restart fixes.
- update is_mounted to use device node ioctl, if available.

* Fri Feb 1 2008 Ian Kent <ikent@redhat.com> - 5.0.3-5
- another fix for don't fail on empty master map.

* Fri Jan 25 2008 Ian Kent <ikent@redhat.com> - 5.0.3-4
- correction to the correction for handling of LDAP base dns with spaces.
- avoid using UDP for probing NFSv4 mount requests.
- use libldap instead of libldap_r.

* Mon Jan 21 2008 Ian Kent <ikent@redhat.com> - 5.0.3-3
- catch "-xfn" map type and issue "no supported" message.
- another correction for handling of LDAP base dns with spaces.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-2
- correct configure test for ldap page control functions.

* Mon Jan 14 2008 Ian Kent <ikent@redhat.com> - 5.0.3-1
- update source to version 5.0.3.

* Fri Dec 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-25
- Bug 426401: CVE-2007-6285 autofs default doesn't set nodev in /net [rawhide]
  - use mount option "nodev" for "-hosts" map unless "dev" is explicily specified.

* Tue Dec 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-23
- Bug 397591 SELinux is preventing /sbin/rpc.statd (rpcd_t) "search" to <Unknown> (sysctl_fs_t).
  - prevent fork between fd open and setting of FD_CLOEXEC.

* Thu Dec 13 2007 Ian Kent <ikent@redhat.com> - 5.0.2-21
- Bug 421371: CVE-2007-5964 autofs defaults don't restrict suid in /net [rawhide]
  - use mount option "nosuid" for "-hosts" map unless "suid" is explicily specified.

* Thu Dec  6 2007 Jeremy Katz <katzj@redhat.com> - 1:5.0.2-19
- rebuild for new ldap

* Tue Nov 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-18
- fix schema selection in LDAP schema discovery.
- check for "*" when looking up wildcard in LDAP.
- fix couple of edge case parse fails of timeout option.
- add SEARCH_BASE configuration option.
- add random selection as a master map entry option.
- re-read config on HUP signal.
- add LDAP_URI, LDAP_TIMEOUT and LDAP_NETWORK_TIMEOUT configuration options.
- fix deadlock in submount mount module.
- fix lack of ferror() checking when reading files.
- fix typo in autofs(5) man page.
- fix map entry expansion when undefined macro is present.
- remove unused export validation code.
- add dynamic logging (adapted from v4 patch from Jeff Moyer).
- fix recursive loopback mounts (Matthias Koenig).
- add map re-load to verbose logging.
- fix handling of LDAP base dns with spaces.
- handle MTAB_NOTUPDATED status return from mount.
- when default master map, auto.master, is used also check for auto_master.
- update negative mount timeout handling.
- fix large group handling (Ryan Thomas).
- fix for dynamic logging breaking non-sasl build (Guillaume Rousse).
- eliminate NULL proc ping for singleton host or local mounts.

* Mon Sep 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-16
- add descriptive comments to config about LDAP schema discovery.
- work around segfault at exit caused by libxml2.
- fix foreground logging (also fixes shutdown needing extra signal bug).

* Wed Sep 5 2007 Ian Kent <ikent@redhat.com> - 5.0.2-15
- fix LDAP schema discovery.

* Tue Aug 28 2007 Ian Kent <ikent@redhat.com> - 5.0.2-14
- update patch to prevent failure on empty master map.
- if there's no "automount" entry in nsswitch.conf use "files" source.
- add LDAP schema discovery if no schema is configured.

* Wed Aug 22 2007 Ian Kent <ikent@redhat.com> - 5.0.2-13
- fix "nosymlink" option handling and add desription to man page.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-12
- change random multiple server selection option name to be consistent
  with upstream naming.

* Tue Aug 21 2007 Ian Kent <ikent@redhat.com> - 5.0.2-11
- don't fail on empty master map.
- add support for the "%" hack for case insensitive attribute schemas.

* Mon Jul 30 2007 Ian Kent <ikent@redhat.com> - 5.0.2-10
- mark map instances stale so they aren't "cleaned" during updates.
- fix large file compile time option.

* Fri Jul 27 2007 Ian Kent <ikent@redhat.com> - 5.0.2-9
- fix version passed to get_supported_ver_and_cost (bz 249574).

* Tue Jul 24 2007 Ian Kent <ikent@redhat.com> - 5.0.2-8
- fix parse confusion between attribute and attribute value.

* Fri Jul 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-7
- fix handling of quoted slash alone (bz 248943).

* Wed Jul 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-6
- fix wait time resolution in alarm and state queue handlers (bz 247711).

* Mon Jul 16 2007 Ian Kent <ikent@redhat.com> - 5.0.2-5
- fix mount point directory creation for bind mounts.
- add quoting for exports gathered by hosts map.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-4
- update multi map nsswitch patch.

* Mon Jun 25 2007 Ian Kent <ikent@redhat.com> - 5.0.2-3
- add missing "multi" map support.
- add multi map nsswitch lookup.

* Wed Jun 20 2007 Ian Kent <ikent@redhat.com> - 5.0.2-2
- include krb5.h in lookup_ldap.h (some openssl doesn't implicitly include it).
- correct initialization of local var in parse_server_string.

* Mon Jun 18 2007 Ian Kent <ikent@redhat.com> - 5.0.2-1
- Update to upstream release 5.0.2.

* Tue Jun 12 2007 Ian Kent <ikent@redhat.com> - 5.0.1-16
- add ldaps support.
  - note: it's no longer possible to have multiple hosts in an ldap map spec.
  - note: to do this you need to rely on the ldap client config.

* Thu Jun 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-14
- fix deadlock in alarm manager module.

* Sun Jun 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-12
- correct mistake in logic test in wildcard lookup.

* Mon May 7 2007 Ian Kent <ikent@redhat.com> - 5.0.1-10
- fix master map lexer to admit "." in macro values.

* Tue Apr 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-9
- upstream fix for filesystem is local check.
- disable exports access control check (bz 203277).
- fix patch to add command option for set a global mount options (bz 214684).

* Mon Apr 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-8
- add configuration variable to control appending of global options (bz 214684).
- add command option to set a global mount options string (bz 214684).

* Tue Apr 3 2007 Ian Kent <ikent@redhat.com> - 5.0.1-7
- fix "null" domain netgroup match for "-hosts" map.

* Fri Mar 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-6
- fix directory creation for browse mounts.
- fix wildcard map handling and improve nsswitch source map update.

* Fri Mar 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-5
- drop "DEFAULT_" prefix from configuration names.
- add option to select replicated server at random (instead of
  ping response time) (bz 227604).
- fix incorrect cast in directory cleanup routines (bz 231864).

* Thu Mar 8 2007 Ian Kent <ikent@redhat.com> - 5.0.1-4
- fixed numeric export match (bz 231188).

* Thu Mar 1 2007 Ian Kent <ikent@redhat.com> - 5.0.1-3
- change file map lexer to allow white-space only blank lines (bz 229434).

* Fri Feb 23 2007 Ian Kent <ikent@redhat.com> - 5.0.1-2
- update "@network" matching patch.

* Thu Feb 22 2007 Ian Kent <ikent@redhat.com> - 5.0.1-1
- update to release tar.
- fix return check for getpwuid_r and getgrgid_r.
- patch to give up trying to update exports list while host is mounted.
- fix to "@network" matching. 
- patch to check for fstab update and retry if not updated.

* Tue Feb 20 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.24
- add "condrestart" to init script (bz 228860).
- add "@network" and .domain.name export check.
- fix display map name in mount entry for "-hosts" map.

* Fri Feb 16 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.22
- fix localhost replicated mounts not working (bz 208757).

* Wed Feb 14 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.20
- correct return status from do_mkdir (bz 223480).

* Sat Feb 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.18
- update the "task done race" patch to fix a deadlock.
- added URL tag.
- removed obsoletes autofs-ldap.
- replaced init directory paths with %%{_initrddir} macro.

* Fri Feb 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.17
- make use of spaces and tabs in spec file consistent.
- escape embedded macro text in %%changelog.
- eliminate redundant %%version and %%release.
- remove redundant conditional check from %%clean.
- remove redundant exit from %%preun.
- correct %%defattr spec.
- remove empty %%doc and redundant %%dir misc lines.
- combine program module spec lines into simpler one line form.

* Tue Feb 6 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.15
- fix race when setting task done (bz 227268).

* Mon Jan 29 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.13
- make double quote handing consistent (at least as much as we can).
- fix handling of trailing white space in wildcard lookup (forward port bz 199720).
- check fqdn of each interface when matching export access list (bz 213700).

* Thu Jan 18 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.11
- correct check for busy offset mounts before offset umount (bz 222872).

* Wed Jan 17 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.9
- fix another expire regression introduced in the "mitigate manual umount"
  patch (bz 222872).

* Mon Jan 15 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.7
- ignore "winbind" if it appears in "automount" nsswitch.conf (bz 214632).

* Tue Jan 10 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.5
- remove fullstop from Summary tag.
- change Buildroot to recommended form.
- replace Prereq with Requires.

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.3
- remove redundant rpath link option (prep for move to Extras).

* Tue Jan 9 2007 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc3.1
- consolidate to rc3.
- fix typo in Fix typo in var when removing temp directory (bz 221847).

* Wed Dec 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.41
- fix nonstrict multi-mount handling (bz 219383).
- correct detection of duplicate indirect mount entries (bz 220799).

* Thu Dec 14 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.38
- update master map tokenizer to admit "slasify-colons" option.
- update location validation to accept "_" (bz 219445).
- set close-on-exec flag on open sockets (bz 215757).

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.35
- update "replace-tempnam" patch to create temp files in sane location.

* Mon Dec 11 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.34
- change mount "device" from "automount" to the map name.
- check for buffer overflow in mount_afs.c.
- replace tempnam with mkdtemp.

* Sun Dec 10 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.33
- expand export access checks to include missing syntax options.
- make "-hosts" module try to be sensitive to exports list changes.

* Thu Dec 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.32
- remove ability to use multiple indirect mount entries in master
  map (bz 218616).

* Wed Dec 6 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.29
- alter nfs4 host probing to not use portmap lookup and add options
  check for "port=" parameter (bz 208757).
- correct semantics of "-null" map handling (bzs 214800, 208091).

* Sat Nov 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.26
- fix parsing of bad mount mount point in master map (bz 215620).
- fix use after free memory access in cache.c and lookup_yp.c (bz 208091).
- eliminate use of pthread_kill to detect task completion (bz 208091).

* Sun Nov 12 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.23
- fix tokenizer to distinguish between global option and dn string (bz 214684).
- fix incorrect return from spawn.

* Wed Nov 8 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.21
- mitigate manual umount of automounts where possible.
- fix multiply recursive bind mounts.
- check kernel module version and require 5.00 or above.
- fix expire regression introduced in the "mitigate manual umount" patch.
- still more on multiply recursive bind mounts.

* Mon Oct 30 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.20
- Update patch for changed semantics of mkdir in recent kernels.
- fix macro table locking (bz 208091).
- fix nsswitch parser locking (bz 208091).
- allow only one master map read task at a time.
- fix misc memory leaks.

* Wed Oct 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.19
- deal with changed semantics of mkdir in recent kernels.

* Fri Oct 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.16
- fix get_query_dn not looking in subtree for LDAP search (missed
  econd occurance).
- allow additional common LDAP attributes in map dn.
- Resolves: rhbz#205997

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.13
- fix parsing of numeric host names in LDAP map specs (bz 205997).

* Mon Oct 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.12
- fix "-fstype=nfs4" server probing (part 2 of bz 208757).
- set close-on-exec flag on open files where possible (bz 207678).

* Fri Oct 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.11
- fix file handle leak in nsswitch parser (bz 207678).
- fix memory leak in mount and expire request processing (bz 207678).
- add additional check to prevent running of cancelled tasks.
- fix potential file handle leakage in rpc_subs.c for some failure
  cases (bz 207678).
- fix file handle leak in included map lookup (bz 207678).

* Sat Oct 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.10
- fix get_query_dn not looking in subtree for LDAP search.
- allow syntax "--timeout <secs>" for backward compatibility
  (bz 193948).
- make masked_match independent of hostname for exports comparison
  (bz 209638).

* Thu Oct 5 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.9
- fix "-fstype=nfs4" handling (bz 208757).

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.8
- review and fix master map options update for map reload.

* Wed Sep 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.7
- make default installed master map for /net use "-hosts" instead
  of auto.net.
- fix included map recursive map key lookup.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.6
- remove unused option UNDERSCORETODOT from default config files.

* Mon Sep 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.5
- fix LDAP lookup delete cache entry only if entry doesn't exist.
- add missing socket close in replicated host check (Jeff Moyer).

* Wed Sep 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.4
- fix cache entrys not being cleaned up on submount expire.

* Sun Sep 17 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.3
- fix include check full patch for file map of same name.

* Wed Sep 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.2
- fix handling of autofs specific mount options (bz 199777).

* Fri Sep 1 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc2.1
- consolidate to rc2.
- fix colon escape handling.
- fix recusively referenced bind automounts.
- update kernel patches.

* Fri Aug 25 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.17
- fix task cancelation at shutdown (more)
- fix concurrent mount and expire race with nested submounts.

* Sun Aug 20 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.16
- fix included map lookup.
- fix directory cleanup on expire.
- fix task cancelation at shutdown.
- fix included map wild card key lookup.

* Thu Aug 16 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.15
- expire individual submounts.
- add ino_index locking.
- fix nested submount expiring away when pwd is base of submount.
- more expire re-work to cope better with shutdown following cthon tests.
- allow hostname to start with numeric when validating.

* Thu Aug 7 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.14
- remove SIGCHLD handler because it is no longer needed and was
  causing expire problems.
- alter expire locking of multi-mounts to lock sub-tree instead of
  entire tree.
- review verbose message feedback and update.
- correction for expire of multi-mounts.
- spelling corrections to release notes (Jeff Moyer).
- add back sloppy mount option, removed for Connectathon testing.
- disable mtab locking again.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.13
- tidy up directory cleanup and add validation check to rmdir_path.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.12
- enable mtab locking until I can resolve the race with it.

* Thu Aug 4 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.11
- cthon fix expire of wildcard and program mounts broken by recent
  patches.

* Thu Aug 3 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.10
- cthon corrections for shutdown patch below and fix shutdown expire.

* Wed Aug 2 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.9
- cthon fix some shutdown races.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.8
- Fix compile error.

* Thu Jul 27 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.7
- cthon fix expire of various forms of nested mounts.

* Mon Jul 24 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.6
- cthon more parser corrections and attempt to fix multi-mounts
  with various combinations of submounts (still not right).

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.5
- Add conflicts kernel < 2.6.17.
- Fix submount operation broken by connectathon updates.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.4
- Correction to host name validation test for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.3
- More code cleanup and corrections for connectathon tests.

* Wed Jul 19 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.2
- Code cleanup and fixes for connectathon tests.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.1-0.rc1.1
- Update version label to avoid package update problems.

* Thu Jul 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-8
- add cacheing of negative lookups to reduce unneeded map
  lookups (bz 197746 part 2).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:5.0.0_beta6-7.1
- rebuild

* Tue Jul 11 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-7
- correct directory cleanup in mount modules.
- merge key and wildcard LDAP query for lookups (bz 197746).

* Sat Jul 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-6
- correct test for libhesiod.

* Fri Jul 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-5
- correct auto.net installed as auto.smb.
- update LDAP auth - add autodectect option.

* Wed Jul 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-4
- correct shutdown log message print.
- correct auth init test when no credentials required.

* Tue Jul 4 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-3
- correct test for existence of auth config file.

* Mon Jul 3 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-2
- merge LDAP authentication update for GSSAPI (Jeff Moyer).
- update default auth config to add options documenetation (Jeff Moyer).
- workaround segfaults at exit after using GSSAPI library.
- fix not checking return in init_ldap_connection (jeff Moyer).

* Thu Jun 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta6-1
- consolidate to beta6, including:
  - mode change update for config file.
  - correction to get_query_dn fix from beta5-4.

* Wed Jun 28 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-6
- cleanup defaults_read_config (Jeff Moyer).

* Tue Jun 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-5
- allow global macro defines to override system macros.
- correct spelling error in default config files missed by
  previous update.
- misc correctness and a memory leak fix.

* Mon Jun 26 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-4
- correct spelling error in default config.
- fix default auth config not being installed.
- change LDAP query method as my test db was incorrect.
- change ldap defaults code to handle missing auth config.
- fix mistake in parsing old style LDAP specs.
- update LDAP so that new query method also works for old syntax.

* Fri Jun 23 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-3
- lookup_init cleanup and fix missed memory leak.
- use nis map order to check if update is needed.
- fix couple of memory leaks in lookup_yp.c.
- fix pasre error in replicated server module.

* Wed Jun 21 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-2
- Add openssl-devel to the BuildRequires, as it is needed for the LDAP
  authentication bitsi also.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta5-1
- promote to beta5.

* Tue Jun 20 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-14
- fix directory cleanup at exit.

* Mon Jun 19 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-13
- Change LDAP message severity from crit to degug (bz# 183893).
- Corrections to INSTALL and README.v5.release.
- Add patch to fix segv on overlength map keys in file maps (Jeff Moter).
- Add patch to restrict scanning of /proc to pid directories only (Jeff Moyer).

* Thu Jun 15 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-12
- Change BuildPrereq to BuildRequires as per the package guidelines.
- Add libxml2-devel to the BuildRequires, as it is needed for the LDAP
  authentication bits.

* Wed Jun 14 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-11
- add export access list matching to "hosts" lookup module (bz # 193585).

* Tue Jun 13 2006 Jeff Moyer <jmoyer@redhat.com> - 5.0.0_beta4-10
- Add a BuildPrereq for cyrus-sasl-devel

* Tue Jun 13 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-9
- move autofs4 module loading back to init script (part bz # 194061).

* Mon Jun 12 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-8
- fix handling of master map entry update (bz # 193718).
- fix program map handling of invalid multi-mount offsets.

* Sat Jun 10 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-7
- fix context init error (introduced by memory leak patch).

* Fri Jun 9 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-6
- add free for working var in get_default_logging.
- add inialisation for kver in autofs_point struct.
- fix sources list corruption in check_update_map_sources.
- fix memory leak in walk_tree.
- fix memory leak in rpc_portmap_getport and rpc_ping_proto.
- fix memory leak in initialisation of lookup modules.

* Wed Jun 8 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-5
- misc fixes for things found while investigating map re-read problem.

* Wed Jun 7 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-4
- check base of offset mount tree is not a mount before umounting
  its offsets.
- fix replicated mount parse for case where last name in list
  fails lookup.
- correct indirect mount expire broken by the wildcard lookup fix.
- fix up multi-mount handling when wildcard map entry present.

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-3
- correct config names in default.c (jpro@bas.ac.uk).

* Mon Jun 5 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-2
- re-instate v4 directory cleanup (bz# 193832 again).
- backout master map lookup changes made to beta3.
- change default master map from /etc/auto.master to auto.master
  so that we always use nsswitch to locate master map.
- change default installed master map to include "+auto.master"
  to pickup NIS master map (all bz# 193831 again).

* Fri Jun 2 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta4-1
- update to beta4.
- should address at least bzs 193798, 193770, 193831 and
  possibly 193832.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-6
- add back test for nested mount in program map lookup.
  - I must have commented this out for a reason. I guess we'll
    find out soon enough.

* Mon May 29 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-5
- fix handling of autofs filesystem mount fail on init.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-4
- updated hesiod patch.

* Sat May 27 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-3
- update hesiod module (Jeff Moyer).
  - add mutex to protect against overlapping mount requests.
  - update return from mount request to give more sensible NSS_*
    values.

* Fri May 26 2006 Jeff Moyer <jmoyer@redhat.com> - 1:5.0.0_beta3-2
- Fix the install permissions for auto.master and auto.misc.

* Thu May 25 2006 Ian Kent <ikent@redhat.com> - 5.0.0_beta3-1
- update source to version 5.0.0_beta3.
- add patch to remove extra debug print.
- add patch to
  - fix memory alloc error in nis lookup module.
  - add "_" to "." mapname translation to nis lookup module.
- add patch to add owner pid to mount list struct.
- add patch to disable NFSv4 when probing hosts (at least foe now).
- add patch to fix white space handling in replicated server selection code.
- add patch to prevent striping of debug info macro patch (Jeff Moyer).
- add patch to add sanity checks on rmdir_path and unlink (Jeff Moyer).
- add patch to fix e2fsck error code check (Jeff Moyer).

* Tue May 16 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-23
- add patch to ignore the "bg" and "fg" mount options as they
  aren't relevant for autofs mounts (bz #184386).

* Tue May 2 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-20
- add patch to use "cifs" instead of smbfs and escape speces
  in share names (bz #163999, #187732).

* Tue Apr 11 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-18
- Add patch to allow customization of arguments to the
  autofs-ldap-auto-master program (bz #187525).
- Add patch to escap "#" characters in exports from auto.net
  program mount (bz#178304).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:4.1.4-16.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Feb 1 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.2
- Add more general patch to translate "_" to "." in map names. (bz #147765)

* Mon Jan 25 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16.1
- Add patch to use LDAP_DEPRICATED compile option. (bz #173833)

* Mon Jan 17 2006 Ian Kent <ikent@redhat.com> - 1:4.1.4-16
- Replace check-is-multi with more general multi-parse-fix.
- Add fix for premature return when waiting for lock file.
- Update copyright declaration for reentrant-syslog source.
- Add patch for configure option to disable locking during mount.
  But don't disable locking by default.
- Add ability to handle automount schema used in Sun directory server.
- Quell compiler warning about getsockopt parameter.
- Quell compiler warning about yp_order parameter.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 17 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-14
- Removed the /misc entry from the default auto.master.  auto.misc has
  an entry for the cdrom device, and the preferred method of mounting the
  cd is via udev/hal.

* Mon Nov  7 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-13
- Changed to sort -k 1, since that should be the same as +0.

* Thu Nov  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-12
- The sort command no longer accepts options of the form "+0".  This broke
  auto.net, so the option was removed.  Fixes bz #172111.

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-11
- Check the return code of is_local_addr in get_best_mount. (bz #169523)

* Wed Oct 26 2005  <jmoyer@redhat.com> - 1:4.1.4-10
- Fix some bugs in the parser
- allow -net instead of /etc/auto.net
- Fix a buffer overflow with large key lengths
- Don't allow autofs to unlink files, only to remove directories
- change to the upstream reentrant syslog patch from the band-aid deferred
  syslog patch.
- Get rid of the init script patch that hard-coded the release to redhat.
  This should be handled properly by all red hat distros.

* Wed May  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-8
- Add in the deferred syslog patch.  This fixes a hung automounter issue
  related to unsafe calls to syslog in signal handler context.

* Tue May  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-7
- I reversed the checking for multimount entries, breaking those configs!
  This update puts the code back the way it was before I broke it.

* Tue Apr 26 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-6
- Fix a race between mounting a share and updating the cache in the parent
  process.  If the mount completed first, the parent would not expire the
  stale entry, leaving it first on the list.  This causes map updates to not
  be recognized (well, worse, they are recognized after the first expire, but
  not subsequent ones).  Fixes a regression, bug #137026 (rhel3 bug).

* Fri Apr 15 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.4-5
- Fixed regression with -browse not taking effect.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-4
- Finish up with the merge breakage.
- Temporary fix for the multimount detection code.  It seems half-baked.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-3
- Fix up the one-auto-master patch.  My "improvements" had side-effects.

* Wed Apr 13 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.4-2
- Import 4.1.4 and merge.

* Mon Apr  4 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-123
- Add in an error case that was omitted in the multi-over patch.
- Update our auto.net to reflect the changes that went into 4.1.4_beta2.
  This fixes a problem seen by at least one customer where a malformed entry
  appeared first in the multimount list, thus causing the entire multimount
  to be ignored.  This new auto.net places that entry at the end, purely by
  luck, but it fixes the problem in this one case.

* Thu Mar 31 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-119
- Merge in the multi-over patch.  This resolves an issue whereby multimounts
  (such as those used for /net) could be processed in the wrong order,
  resulting in directories not showing up in a multimount tree.  The fix
  is to process these directories in order, shortest to longer path.

* Wed Mar 23 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-115
- Fixed regression causing any entries after a wildcard in an
  indirect map to be ignored. (bz #151668).
- Fixed regression which caused local hosts to be mount instead
  of --bind local directories. (bz #146887)

* Thu Mar 17 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-111
- Fixed one off bug in the submount-variable-propagation patch.
  (bz #143074)
- Fixed a bug in the init script which wouldn't find the -browse
  option if it was preceded by another option. (fz #113494)

* Mon Feb 28 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-100
- When using ldap if auto.master doesn't exist we now check for auto_master.
  Addresses bz #130079
- When using an auto.smb map we now remove the leading ':' from the path which
  caused mount to fail in the past.  Addresses bz #147492
- Autofs now checks /etc/nsswitch.conf to determine in what order files & nis
  are checked when looking up autofs submount maps which don't specify a
  maptype.  Addresses IT #57612.

* Mon Feb 14 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-99
- Change Copyright to License in the spec file so it will build.

* Fri Feb 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-98
- Program maps can repeat the last character of output.  Fix this.  
  Addresses bz #138606
- Return first entry when there are duplicate keys in a map.  Addresses
  bz #140108.
- Propagate custom map variables to submounts.  Fixes bz #143074.
- Create a sysconfig variable to control whether we source only one master
  map (the way sun does), or source all maps found (which is the default for
  backwards compatibility).  Addresses bz #143126.
- Revised version of the get_best_mount patch. (#146887) cfeist@redhat.com
  The previous patch introduced a regression.  Non-replicated mounts would
  not have the white space stripped from the entry and the mount would fail.
- Handle comment characters in the middle of the automount line in
  /etc/nsswitch.conf.  Addresses bz #127457.

* Wed Feb  2 2005 Chris Feist <cfeist@redhat.com> - 1:4.1.3-94
- Stop automount from pinging hosts if there is only one host (#146887)

* Wed Feb  2 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-90
- Fix potential double free in cache_release.  This bug showed up in a
  multi-map setup.  Two calls to cache_release would result in a SIGSEGV,
  and the automount process would never exit.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-82
- Fixed documentation so users know that any local mounts override
  any other weighted mount.

* Mon Jan 24 2005 Chris Feist <cfeist@redhat.com> - 1:4.3-80
- Added a variable to determine if we created the directory or not
  so we don't accidently remove a directory that we didn't create when
  we stop autofs.  (bz #134399)

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-76
- Fix the large program map patch.

* Tue Jan 11 2005 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-75
- Fix some merging breakages that caused the package not to build.

* Thu Jan  6 2005  <jmoyer@redhat.com> - 1:4.1.3-74
- Add in the map expiry patch
- Bring in other patches that have been committed to other branches. This 
  version should now contain all fixes we have to date
- Merge conflicts due to map expiry changes

* Fri Nov 19 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-57
- Pass a socket into clntudp_bufcreate so that we don't use up additional 
  reserved ports.  This patch, along with the socket leak fix, addresses
  bz #128966.

* Wed Nov 17 2004  <jmoyer@redhat.com> - 1:4.1.3-56
- Somehow the -browse patch either didn't get committed or got reverted.
  Fixed.

* Tue Nov 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-55
- Fix program maps so that they can have gt 4k characters. (Neil Horman)
  Addresses bz #138994.
- Add a space after the colon here "Starting automounter:" in init script.
  Fixes bz #138513.

* Mon Nov 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-53
- Make autofs understand -[no]browse.  Addresses fz #113494.

* Thu Nov 11 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-48
- Fix the umount loop device function in the init script.

* Wed Oct 27 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-34
- Added a patch to fix the automounter failing on ldap maps
  when it couldn't get the whole map.  (ie. when the search
  limit was lower than the number of results)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-32
- Fixed the use of +ypmapname so the maps included with +ypmapname
  are used in the correct order.  (In the past the '+' entries
  were always processed after local entries.)

* Thu Oct 21 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-31
- Fixed the duplicate map detection code to detect if maps try
  to mount on top of existing maps. 

* Wed Oct 20 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-29
- Fixed a problem with backwards compatability. Specifying local
  maps without '/etc/' prepended to them now works. (bz #136038)

* Fri Oct 15 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-28
- Fixed a bug which caused directories to never be unmounted. (bz #134403)

* Thu Oct 14 2004 Chris Feist <cfeist@redhat.com> - 1:4.1.3-27
- Fixed an error in the init script which caused duplicate entries to be
  displayed when asking for autofs status.

* Fri Oct  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-22
- Comment out map expiry (and related) patch for an FC3 build.

* Thu Sep 23 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-21
- Make local options apply to all maps in a multi-map entry.

* Tue Sep 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-20
- Merged my and Ian's socket leak fixes into one, smaller patch. Only
  partially addresses bz #128966.
- Fix some more echo lines for internationalization. bz #77820
- Revert the only one auto.master patch until we implement the +auto_master
  syntax.  Temporarily addresses bz #133055.

* Thu Sep  2 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-18
- Umount loopback filesystems under automount points when stopping the 
  automounter.
- Uncomment the map expiry patch.
- change a close to an fclose in lookup_file.c

* Tue Aug 31 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-17
- Add patch to support parsing nsswitch.conf to determine map sources.
- Disable this patch, and Ian's map expiry patch for a FC build.

* Tue Aug 24 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-16
- Version 3 of Ian's map expiry changes.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-15
- Fix a socket leak in the rpc_subs, causing mounts to fail since we are 
  running out of port space fairly quickly.

* Wed Aug 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-14
- New map expiry patch from Ian.
- Fix a couple signal races.  No known problem reports of these, but they
  are holes, none-the-less.

* Tue Aug 10 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-13
- Only read one auto.master map (instead of concatenating all found sources).
- Uncomment Ian's experimental mount expiry patch.

* Fri Aug  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-12
- Add a sysconfig entry to disable direct map support, and set this to 
  1 by default.
- Disable the beta map expiry logic so I can build into a stable distro.
- Add defaults for all of the sysconfig variables to the init script so 
  we don't trip over user errors (i.e. deleting /etc/sysconfig/autofs).

* Wed Aug  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-11
- Add beta map expiry code for wider testing. (Ian Kent)
- Fix check for ghosting option.  I forgot to check for it in DAEMONOPTIONS.
- Remove STRIPDASH from /etc/sysconfig/autofs

* Mon Jul 12 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-10
- Add bad chdir patch from Ian Kent.
- Add a typo fix for the mtab lock file.
- Nuke the stripdash patch.  It didn't solve a problem.

* Tue Jun 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-9
- Bump revison for inclusion in RHEL 3.

* Mon Jun 21 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-8
- Change icmp ping to an rpc ping.  (Ian Kent)
- Fix i18n patch
  o Remove the extra \" from one echo line.
  o Use echo -e if we are going to do a \n in the echo string.

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107463

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- Fixed i18n bug #107461

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jun  5 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-4
- Perform an icmp ping request before rpc_pings, since the rpc clnt_create
  function has a builtin default timeout of 60 seconds.  This could result
  in a long delay when a server in a replicated mount setup is down.
- For non-replicated server entries, ping a host before attempting to mount.
  (Ian Kent)
- Change to %%configure.
- Put version-release into .version to allow for automount --version to
  print exact info.
- Nuke my get-best-mount patch which always uses the long timeout.  This
  should no longer be needed.
- Put name into changelog entries to make them consistent.  Add e:n-v-r
  into Florian's entry.
- Stop autofs before uninstalling

* Sat Jun 05 2004 Florian La Roche <Florian.LaRoche@redhat.de> - 1:4.1.3-3
- add a preun script to remove autofs

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-2
- Incorporate patch from Ian which fixes an infinite loop seen by those
  running older versions of the kernel patches (triggered by non-strict mounts
  being the default).

* Tue Jun  1 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.3-1
- Update to upstream 4.1.3.

* Thu May  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-6
- The lookup_yp module only dealt with YPERR_KEY, all other errors were 
  treated as success.  As a result, if the ypdomain was not bound, the 
  subprocess that starts mounts would SIGSEGV.  This is now fixed.
- Option parsing in the init script was not precise enough, sometimes matching
  filesystem options to one of --ghost, --timeout, --verbose, or --debug.  
  The option-parsing patch addresses this issue by making the regexp's much
  more precise.
- Ian has rolled a third version of the replicated mount fixes.

* Tue May  4 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-5
- Ian has a new fix for replicated server and multi-mounts.  Updated the 
  patch for testing.  Still beta.  (Ian Kent)

* Mon May  3 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-4
- Fix broken multi-mounts.  test patch.  (Ian Kent)

* Tue Apr 20 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-3
- Fix a call to spawnl which forgot to specify a lock file. (nphilipp)

* Wed Apr 14 2004  <jmoyer@redhat.com> - 1:4.1.2-2
- Pass --libdir= to ./configure so we get this right on 64 bit platforms that 
  support backwards compat.

* Wed Apr 14 2004  Jeff Moyer <jmoyer@redhat.com> - 1:4.1.2-1
- Change hard-coded paths in the spec file to the %%{_xxx} variety.
- Update to upstream 4.1.2.
- Add a STRIPDASH option to /etc/sysconfig/autofs which allows for
  compatibility with the Sun automounter options specification syntax in
  auto.master.  See /etc/sysconfig/autofs for more information.  Addresses
  bug 113950.

* Tue Apr  6 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-6
- Add the /etc/sysconfig/autofs file, and supporting infrastructure in 
  the init script.
- Add support for UNDERSCORE_TO_DOT for those who want it.
- We no longer own /net.  Move it to the filesystem package.

* Tue Mar 30 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-5
- Clarify documentation on direct maps.
- Send automount daemons a HUP signal during reload.  This tells them to 
  re-read maps (otherwise they use a cached version.  Patch from the autofs
  maintainer.

* Mon Mar 22 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-4
- Fix init script to print out failures where appropriate.
- Build the automount daemon as a PIE.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-3
- Fix bug in get_best_mount, whereby if there is only one option, we 
  choose nothing.  This is primarily due to the fact that we pass 0 in to
  the get_best_mount function for the long timeout parameter.  So, we
  timeout trying to contact our first and only server, and never retry.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-2
- Prevent startup if a mountpoint is already mounted.

* Thu Mar 18 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.1-1
- Update to 4.1.1, as it fixes problems with wildcards that people are 
  seeing quite a bit.

* Wed Mar 17 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-8
- Fix ldap init code to parse server name and options correctly.

* Tue Mar 16 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-7
- Moved the freeing of ap.path to cleanup_exit, as we would otherwise 
  reference an already-freed variable.

* Mon Mar 15 2004 Jeff Moyer <jmoyer@redhat.com> - 1:4.1.0-6
- add %%config(noreplace) for auto.* config files.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-5
- make the init script only recognize redhat systems.  Nalin seems to remember
  some arcane build system error that can be caused if we don't do this.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-4
- comment out /net and /misc from the default auto.master.  /net is important
  since in a default shipping install, we can neatly co-exist with amd.

* Wed Mar 10 2004 Jeff Moyer <jmoyer@redhat.com> 1:4.1.0-3
- Ported forward Red Hat's patches from 3.1.7 that were not already present
  in 4.1.0.
- Moving autofs from version 3.1.7 to 4.1.0

* Mon Sep 29 2003 Ian Kent <raven@themaw.net>
- Added work around for O(1) patch oddity.

* Sat Aug 17 2003 Ian Kent <raven@themaw.net>
- Fixed tree mounts.
- Corrected transciption error in autofs4-2.4.18 kernel module

* Sun Aug 10 2003 Ian Kent <raven@themaw.net>
- Checked and merged most of the RedHat v3 patches
- Fixed kernel module handling wu-ftpd login problem (again)

* Thu Aug 7 2003 Ian Kent <raven@themaw.net>
- Removed ineffective lock stuff
- Added -n to bind mount to prevent mtab update error
- Added retry to autofs umount to clean matb after fail
- Redirected messages from above to debug log and added info message
- Fixed autofs4 module reentrancy, pwd and chroot handling

* Wed Jul 30 2003 Ian Kent <raven@themaw.net>
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Fixed autofs directory removal on failure of autofs mount
- Fixed lock file wait function overlapping calls to (u)mount

* Sun Jul 27 2003 Ian Kent <raven@themaw.net>
- Implemented LDAP direct map handling for nisMap and automountMap schema
- Fixed autofs4 ghosting patch for 2.4.19 and above (again)
- Added locking to fix overlapping internal calls to (u)mount 
- Added wait for mtab~ to improve tolerance of overlapping external calls to (u)mount
- Fixed ghosted directory removal after failed mount attempt

* Wed May 28 2003 Ian Kent <raven@themaw.net>
- Cleaned up an restructured my added code
- Corrected ghosting problem with 2.4.19 and above
- Added autofs4 ghosting patch for 2.4.19 and above
- Implemented HUP signal to force update of ghosted maps

* Mon Mar 23 2002 Ian Kent <ian.kent@pobox.com>
- Add patch to implement directory ghosting and direct mounts
- Add patch to for autofs4 module to support ghosting

* Wed Jan 17 2001 Nalin Dahyabhai <nalin@redhat.com>
- use -fPIC instead of -fpic for modules and honor other RPM_OPT_FLAGS

* Tue Feb 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- enable hesiod support over libbind

* Fri Aug 13 1999 Cristian Gafton <gafton@redhat.com>
- add patch from rth to avoid an infinite loop
