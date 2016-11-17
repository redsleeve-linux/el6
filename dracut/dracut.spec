# Variables must be defined
%define with_switch_root	1
%define with_nbd		1

# switchroot provided by util-linux-ng in F-12+
%if 0%{?fedora} > 11 || 0%{?rhel} >= 6
%define with_switch_root 0
%endif
# nbd in Fedora only
%if 0%{?rhel} >= 6
%define with_nbd 0
%endif

Name: dracut
Version: 004
Release: 409%{?dist}.2
Summary: Initramfs generator using udev
Group: System Environment/Base
License: GPLv2+
URL: http://apps.sourceforge.net/trac/dracut/wiki

Source0: http://www.kernel.org/pub/linux/utils/boot/dracut/dracut-%{version}.tar.bz2
Patch1: 0001-init-fixed-emergency_shell-argument-parsing.patch
Patch2: 0002-mdraid-prefer-etc-mdadm.conf-over-etc-mdadm-mdadm.co.patch
Patch3: 0003-base-fix-selinux-handling-if-.autorelabel-is-present.patch
Patch4: 0004-Add-a-check-file-for-multipath.patch
Patch5: 0005-fixed-permissions-for-the-check-files.patch
Patch6: 0006-beautified-man-pages.patch
Patch7: 0007-init-dashified.patch
Patch8: 0008-dasd_mod-changed-prio-of-cmdline-hook-to-be-executed.patch
Patch9: 0009-test-iSCSI-fixed-test-script.patch
Patch10: 0010-rootfs-block-strip-ro-rw-options-from-fstab-options.patch
Patch11: 0011-zfcp-install-s390utils-script-rather-than-local-one.patch
Patch12: 0012-add-preliminary-IPv6-support.patch
Patch13: 0013-Move-multipath-scan-earlier.-It-must-go-before-any-o.patch
Patch14: 0014-make-nfs4-work.patch
Patch15: 0015-nfs-suppress-error-message-about-missing-passwd.patch
Patch16: 0016-Fixed-Move-multipath-scan-earlier.-It-must-go-before.patch
Patch17: 0017-add-etc-dracut.conf.d.patch
Patch18: 0018-dracut.conf-added-add_dracutmodules.patch
Patch19: 0019-removed-cdrom-hack-for-live-CDs.patch
Patch20: 0020-nfs4-rpc.idmapd-does-not-accept-parameters-anymore.patch
Patch21: 0021-fix-selinux-disabled-state.patch
Patch22: 0022-s390-_cio_free-needs-seq.patch
Patch23: 0023-fix-lib64-check.patch
Patch24: 0024-mount-root-do-not-pollute-init-arguments.patch
Patch25: 0025-selinux-fix-selinux-0-handling.patch
Patch26: 0026-fix-IFS-restoring.patch
Patch27: 0027-dracut-removed-local-not-inside-of-function.patch
Patch28: 0028-mount-root-skip-comments.patch
Patch29: 0029-mount-root-also-filter-defaults-from-mount-options.patch
Patch30: 0030-dracut-add-check-if-we-can-write-to-the-output-image.patch
Patch31: 0031-Use-multipath-if-it-s-installed-and-being-used-for-t.patch
Patch32: 0032-parse-kernel.sh-must-have-a-shebang.patch
Patch33: 0033-kernel-modules-add-keyboard-kernel-modules.patch
Patch34: 0034-udev-rules-choose-between-several-firmware-upload-to.patch
Patch35: 0035-add-readonly-overlay-support-for-dmsquash.patch
Patch36: 0036-dmsquash-live-use-getsize64-instead-of-getsize.patch
Patch37: 0037-Fix-boot-with-user-suspend-and-no-resume-kernel-argu.patch
Patch38: 0038-Pass-init-argument-s-to-real-init.patch
Patch39: 0039-dmsquash-live-root-use-blockdev-with-getsz.patch
Patch40: 0040-rpmversion-install-add-shebang.patch
Patch41: 0041-dracut-do-a-full-ldconfig-in-the-initramfs.patch
Patch42: 0042-dracut-move-ldconfig-after-include.patch
Patch43: 0043-test-use-ldconfig-processing-for-roots-as-well.patch
Patch44: 0044-xen-try-harder-to-locate-xen-detect.patch
Patch45: 0045-silence-xen-detect-detection.patch
Patch46: 0046-kernel-modules-installkernel-force-install-some-modu.patch
Patch47: 0047-lvm_scan-use-ignoremonitoring-rather-than-monitor-n.patch
Patch48: 0048-Add-dcb-support-to-dracut-s-FCoE-support-rh563794.patch
Patch49: 0049-fcoe-soft-install-fcoe-bins.patch
Patch50: 0050-lvm-lvm_scan.sh-silence-lvm-version-check.patch
Patch51: 0051-dracut.spec-remove-libselinux-libsepol-requirement.patch
Patch52: 0052-updated-NEWS-moved-tag-005.patch
Patch53: 0053-dracut.8-fixed-LUKS-paragraph.patch
Patch54: 0054-dracut.8-add-information-which-parameter-can-be-spec.patch
Patch55: 0055-dmraid-parse-different-error-messages.patch
Patch56: 0056-init-add-hacky-cdrom-polling-mechanism.patch
Patch57: 0057-add-module-btrfs.patch
Patch58: 0058-teach-dmsquash-live-root-to-use-rootflags.patch
Patch59: 0059-init-trigger-with-action-add.patch
Patch60: 0060-add-missing-paragraph-for-add-drivers.patch
Patch61: 0061-manpage-addition-for-kernel-drivers.patch
Patch62: 0062-dracut-add_drivers-from-the-command-line-should-add-.patch
Patch63: 0063-AUTHORS-updated.patch
Patch64: 0064-kernel-modules-hardcode-sr_mod.patch
Patch65: 0065-kernel-modules-only-remove-ocfs2-if-all-filesystems-.patch
Patch66: 0066-dracut.spec-add-btrfs-module.patch
Patch67: 0067-Use-pigz-for-gzipping-if-available.patch
Patch68: 0068-nfs-fixed-nsswitch.conf-parsing.patch
Patch69: 0069-network-removed-bogus-udev-rules.patch
Patch70: 0070-network-correct-rules-for-multiple-nics.patch
Patch71: 0071-nfs-add-missing-nfsidmap-libs.patch
Patch72: 0072-udev-rules-be-more-careful-about-md-devices-and-blki.patch
Patch73: 0073-dracut-lib-turn-of-shell-debug-mode-in-strstr-and-ge.patch
Patch74: 0074-mdraid-try-to-start-container-childs-manually-with-m.patch
Patch75: 0075-init-fix-cdrom-polling-loop.patch
Patch76: 0076-init-do-not-redirect-to.patch
Patch77: 0077-loginit-turn-off-debugging.patch
Patch78: 0078-run-qemu-add-usr-libexec-qemu-kvm-to-search.patch
Patch79: 0079-add-rd_retry-kernel-command-line-parameter.patch
Patch80: 0080-dracut.spec-removed-e2fsprogs-requirement.patch
Patch81: 0081-NEWS-update.patch
Patch82: 0082-Needs-btrfsctl-not-btrfs-module.patch
Patch83: 0083-btfrs-load-btrfs-module-and-updated-NEWS.patch
Patch84: 0084-kernel-modules-add-more-hardcoded-modules.patch
Patch85: 0085-dracut.conf-use-as-default-for-config-variables.patch
Patch86: 0086-znet-use-ccw-init-and-ccw-rules-from-s390utils-in-dr.patch
Patch87: 0087-znet-renamed-rd_CCW-to-rd_ZNET.patch
Patch88: 0088-fcoe-add-sbin-vconfig-and-the-8021q-kernel-module.patch
Patch89: 0089-dracut.8-fix-rd_LVM_LV-description.patch
Patch90: 0090-plymouth-only-display-luksname-and-device-for-multip.patch
Patch91: 0091-dracut.spec-remove-elfutils-libelf-requirement.patch
Patch92: 0092-use-grep-directly-without-nm-to-drop-binutils-requir.patch
Patch93: 0093-plymouth-plymouth-populate-initrd-get-rid-of-awk.patch
Patch94: 0094-dracut-get-rid-of-the-file-command.patch
Patch95: 0095-90mdraid-dracut-functions-fix-md-raid-hostonly-detec.patch
Patch96: 0096-40network-parse-ip-opts.sh-add-ip-auto6-to-valid-opt.patch
Patch97: 0097-40network-dhclient-script-be-more-verbose.patch
Patch98: 0098-40network-ifup-be-more-verbose.patch
Patch99: 0099-95fcoe-fcoe-up-wait_for_if_up.patch
Patch100: 0100-get-rid-of-rdnetdebug.patch
Patch101: 0101-selinux-loadpolicy.sh-exit-for-selinux-0.patch
Patch102: 0102-dracut-functions-check-if-specific-dracut-module-is-.patch
Patch103: 0103-dracut-functions-beautified-warnings.patch
Patch104: 0104-multipath-simplify-and-install-wwids-rhbz-595719.patch
Patch105: 0105-multipath-remove-multipath-udev-rules-if-no-multipat.patch
Patch106: 0106-Just-look-for-cryptroot-instead-of-sbin-cryptroot.patch
Patch107: 0107-Have-cryptroot-ask-load-dm_crypt-if-needed.patch
Patch108: 0108-90crypt-crypto_LUKS-identifier-corrected.patch
Patch109: 0109-plymouth-cryptroot-ask.sh-beautify-password-prompt.patch
Patch110: 0110-iscsi-add-support-for-multiple-netroot-iscsi.patch
Patch111: 0111-lvm-install-lvm-mirror-and-snaphot-libs.patch
Patch112: 0112-network-depend-on-ifcfg-if-etc-sysconfig-network-scr.patch
Patch113: 0113-crypt-install-more-aes-modules.patch
Patch114: 0114-network-strip-pxelinux-hardware-type-field-from-BOOT.patch
Patch115: 0115-fixed-ip-dhcp6.patch
Patch116: 0116-dracut.8-add-note-about-putting-IPv6-addresses-in-br.patch
Patch117: 0117-dracut.8-changed-IPv6-addresses-to-the-documentation.patch
Patch118: 0118-fips-fixes-copy-paste-error-for-check.patch
Patch119: 0119-crypt-add-fpu-kernel-module.patch
Patch120: 0120-Write-rules-for-symlinks-to-dev-.udev-rules.d-for-la.patch
Patch121: 0121-dracut-functions-set-LANG-C-for-ldd-output-parsing.patch
Patch122: 0122-dracut-functions-use-LC_ALL-C-rather-than-LANG-C.patch
Patch123: 0123-dmsquash-resume-do-not-name-the-dev-.udev-rules-like.patch
Patch124: 0124-dmsquash-live-mount-live-image-at-dev-.initramfs-liv.patch
Patch125: 0125-fcoe-moved-fcoeup-to-initqueue-udev-timeouts.patch
Patch126: 0126-dmsquash-live-depend-on-dm-module.patch
Patch127: 0127-dm-load-dm_mod-if-device-mapper-not-in-proc-misc.patch
Patch128: 0128-dmsquash-live-do-not-umount-dev-.initramfs-live-for-.patch
Patch129: 0129-plymouth-depend-on-crypt-if-cryptsetup-exists.patch
Patch130: 0130-crypt-assemble-70-luks.rules-dynamically.patch
Patch131: 0131-crypt-removed-default-70-luks.rules.patch
Patch132: 0132-crypt-parse-crypt.sh-fix-end-label-for-luks-udev-rul.patch
Patch133: 0133-crypt-wait-for-all-rd_LUKS_UUID-disks-to-appear.patch
Patch134: 0134-mknod-with-mode-and-set-umask-for-the-rest.patch
Patch135: 0135-lvm-wait-for-all-rd_LVM_LV-and-rd_LVM_VG-specified-t.patch
Patch136: 0136-fcoe-add-sleeps-to-fcoe-up.patch
Patch137: 0137-init-do-not-umask.patch
Patch138: 0138-selinux-fixed-error-handling-for-load-policy.patch
Patch139: 0139-crypt-strip-luks-from-rd_LUKS_UUID.patch
Patch140: 0140-dracut-functions-filter_kernel_modules-search-in-ext.patch
Patch141: 0141-mkinitrd-do-not-call-dracut-in-host-only-mode.patch
Patch142: 0142-dm-install-all-md-dm-kernel-modules.patch
Patch143: 0143-dmraid-switch-to-rd_NO_MDIMSM-if-no-mdadm-installed.patch
Patch144: 0144-add-96insmodpost-dracut-module.patch
Patch145: 0145-.rules-honor-DM_UDEV_DISABLE_OTHER_RULES_FLAG.patch
Patch146: 0146-mdraid-parse-md.sh-create-new-rules-then-mv-to-old-o.patch
Patch147: 0147-dracut-functions-filter_kernel_modules-search-in-ext.patch
Patch148: 0148-mkinitrd-dracut.sh-add-force.patch
Patch149: 0149-multipath-install-install-the-complete-etc-multipath.patch
Patch150: 0150-multipath-install-by-default-but-run-only-if-wwids-a.patch
Patch151: 0151-fcoe-add-EDD-parsing.patch
Patch152: 0152-network-add-iBFT-interface-configuration.patch
Patch153: 0153-fcoe-parse-fcoe.sh-removed-second-else.patch
Patch154: 0154-add-97biosdevname-dracut-module.patch
Patch155: 0155-fips-install-.hmac-files-for-cryptsetup-and-libs.patch
Patch156: 0156-base-install-less-optionally.patch
Patch157: 0157-fips-add-aes-xts-module.patch
Patch158: 0158-multipath-use-new-B-parameter.patch
Patch159: 0159-biosdevname-unbashify-parse-biosdevname.sh.patch
Patch160: 0160-dracut-functions-write-to-HOME-dracut.log-instead-of.patch
Patch161: 0161-add-dracut-html-documentation.patch
Patch162: 0162-dracut-rhel6.xml-update.patch
Patch163: 0163-parse-biosdevname-put-parenthesis-around-BIOSDEVNAME.patch
Patch164: 0164-dracut-functions-check-if-logfile-dir-is-writable.patch
Patch165: 0165-dracut-functions-add-date-to-logfile-messages.patch
Patch166: 0166-dracut-log-more-messages.patch
Patch167: 0167-dracut.spec-add-logrotate-file.patch
Patch168: 0168-fix-install-execution-bit.patch
Patch169: 0169-fips-add-xts-gf128mul-to-FIPSMODULES.patch
Patch170: 0170-dracut-functions-fail-instmods-for-fips-module.patch
Patch171: 0171-suppress-modprobe-errors-on-builtins-credits-to-Kay-.patch
Patch172: 0172-fix-installation-of-modules.builtin.bin.patch
Patch173: 0173-fips-do-not-load-tcrypt-with-noexit-parameter.patch
Patch174: 0174-fips-installkernel-turn-off-hostonly-mode-for-fipsmo.patch
Patch175: 0175-fips-fips.sh-unbashify-if-clause.patch
Patch176: 0176-fips-install-fipscheck.patch
Patch177: 0177-install-.hmac-files-if-present.patch
Patch178: 0178-fips-hardcode-install-of-libcrypto.-and-libssl.patch
Patch179: 0179-fips-only-trigger-udev-if-boot-device-is-not-yet-pre.patch
Patch180: 0180-plymouth-execute-emergency-script-first.patch
Patch181: 0181-crypt-fix-emergency-script-generation.patch
Patch182: 0182-lvm-move-emergency-script-from-00-to-90.patch
Patch183: 0183-selinux-on-failure-die-rather-than-sleep.patch
Patch184: 0184-base-dracut-lib.sh-fix-die.patch
Patch185: 0185-init-turn-off-e-mode-in-emergency.patch
Patch186: 0186-init-die-if-.die-is-present.patch
Patch187: 0187-init-display-emergency-warning-with-warn-instead-of-.patch
Patch188: 0188-init-cause-a-kernel-panic-rather-than-sleep-forever-.patch
Patch189: 0189-dracut-make-i-include-SOURCE-TARGET-work-for-files-t.patch
Patch190: 0190-rdblacklist-rdinsmodpost-rdloaddriver-accept-comma-s.patch
Patch191: 0191-add-caps-module-to-drop-capabilities.patch
Patch192: 0192-fips-fixed-boot-dev-handling.patch
Patch193: 0193-iscsi-add-additional-hardcoded-modules.patch
Patch194: 0194-dracut-fix-path-to-strip-kernel-modules.patch
Patch195: 0195-fips-add-rd.fips.skipkernel-boot-option.patch
Patch196: 0196-dracut.8-add-fips-documentation.patch
Patch197: 0197-fcoe-parse-fcoe.sh-s-source-.-g.patch
Patch198: 0198-dracut.spec-update.patch
Patch199: 0199-fips-moved-to-pre-pivot-to-support-boot-in.patch
Patch200: 0200-fips-make-fips-work-with-encrypted-root-and-seperate.patch
Patch201: 0201-fips-set-e-has-no-effect-if-we-use.patch
Patch202: 0202-fips-use-small-settle-loop-to-get-boot.patch
Patch203: 0203-fips-also-support-FIPS-on-separate-LVM-partition.patch
Patch204: 0204-fcoe-moved-edd-detection-to-settled-initqueue.patch
Patch205: 0205-iscsi-set-initiator-from-ibft-if-possible.patch
Patch206: 0206-network-only-require-bootdev-for-netroot-dhcp-or-net.patch
Patch207: 0207-dracut-fips-pre_un_link-binaries-if-fips-module-was-.patch
Patch208: 0208-let-rpc-user-own-var-lib-rpcbind.patch
Patch209: 0209-mdraid-do-not-call-mdadm-I-with-no-degraded.patch
Patch210: 0210-mdraid-mdraid_start.sh-removed-local-in-non-function.patch
Patch211: 0211-fixed-testsuite.patch
Patch212: 0212-correct-module-name.patch
Patch213: 0213-skip-condition-fixed.patch
Patch214: 0214-don-t-overwrite-ifname.patch
Patch215: 0215-network-net-genrules.sh-also-honor-rename-events.patch
Patch216: 0216-network-parse-ip-opts.sh-fix-ifname-for-ibft-with-al.patch
Patch217: 0217-doc-clarify-iscsi_firmware-parameter-usage.patch
Patch218: 0218-iscsi-find-iscsi-kernel-modules-by-symbol-names.patch
Patch219: 0219-Makefile-add-rpm-and-syncheck-target.patch
Patch220: 0220-inc-TEST-disk-size.patch
Patch221: 0221-99base-add-timeout-queue.patch
Patch222: 0222-90mdraid-move-force-assembly-to-timeout-initqueue.patch
Patch223: 0223-lvm-use-sysinit-if-lvm-version-v2.02.65.patch
Patch224: 0224-90lvm-lvm_scan.sh-fixed-lvm-version-parsing.patch
Patch225: 0225-90lvm-lvm_scan.sh-use-partial-to-force-assembly-inco.patch
Patch226: 0226-95fstab-sys-mount-all-etc-fstab.sys-volumes-before-s.patch
Patch227: 0227-01fips-installkernel-add-dm-mod-and-dm-crypt-to-the-.patch
Patch228: 0228-99base-selinux-loadpolicy.sh-execute-chrooted-comman.patch
Patch229: 0229-modules.d-90dm-install-libdevmapper-event-for-90dm.patch
Patch230: 0230-90dm-dm-pre-udev.sh-load-dm-mirror-module.patch
Patch231: 0231-iscsi-bnx2i.patch
Patch232: 0232-modules.d-90dm-use-dmsetup-to-find-lib-dir.patch
Patch233: 0233-90mdraid-65-md-incremental-imsm.rules-incremental-ru.patch
Patch234: 0234-selinux-loadpolicy-hide-info-message-if-selinux-is-d.patch
Patch235: 0235-95fcoe-support-bnx2fc.patch
Patch236: 0236-95iscsi-parse-iscsiroot.sh-fixed-iscsi_tcp-module-lo.patch
Patch237: 0237-90mdraid-mdadm_auto.sh-incrementally-autoassemble.patch
Patch238: 0238-mdraid-lvm-order-timeout-queue-execution.patch
Patch239: 0239-dm-lvm-dmraid-cleanup-installation.patch
Patch240: 0240-network-allow-multiple-ip-autoconf-options.patch
Patch241: 0241-dm-dmsquash-live-check-for-dmsetup.patch
Patch242: 0242-02fips-aesni-add-fips-with-aesni-intel.patch
Patch243: 0243-create-var-log.patch
Patch244: 0244-99base-selinux-loadpolicy.sh-use-F-for-restorecon.patch
Patch245: 0245-dracut-lib.sh-add-killproc.patch
Patch246: 0246-iscsi-kill-iscsiuio.patch
Patch247: 0247-10redhat-i18n-optionally-install-console_init.patch
Patch248: 0248-95fcoe-fcoe-up-load-8021q-module-before-fipvlan.patch
Patch249: 0249-TEST-40-NBD-relax-check-for-fsoptions.patch
Patch250: 0250-fcoe-iscsi-udevadm-settle-after-module-loading.patch
Patch251: 0251-iscsi-install-iscsi_boot_sysfs-kernel-module.patch
Patch252: 0252-99base-dracut-lib.sh-fixed-killproc.patch
Patch253: 0253-95iscsi-hardcode-modprobe-a-bunch-of-iscsi-offload-k.patch
Patch254: 0254-45ifcfg-write-ifcfg.sh-check-for-existance-of-tmp-ne.patch
Patch255: 0255-40network-ifup-increase-RDRETRY-if-we-do-dhcp-to-wai.patch
Patch256: 0256-40network-ifup-add-brd-to-ip-addr-add.patch
Patch257: 0257-95iscsi-iscsiroot-unset-used-variables-before-starti.patch
Patch258: 0258-Revert-90mdraid-mdadm_auto.sh-incrementally-autoasse.patch
Patch259: 0259-dracut-only-source-install-if-available.patch
Patch260: 0260-90mdraid-mdcontainer_start.sh-do-not-start-with-I.patch
Patch261: 0261-90mdraid-65-md-incremental-imsm.rules-do-not-depend-.patch
Patch262: 0262-test-TEST-12-RAID-DEG-refine-test.patch
Patch263: 0263-dracut.8-fixed-FILES-section.patch
Patch264: 0264-fcoe-do-not-require-vconfig.patch
Patch265: 0265-redirect-udevadm-settle-output-to-dev-null.patch
Patch266: 0266-lsinitrd-update-to-upstream-version.patch
Patch267: 0267-50plymouth-plymouth-pretrigger.sh-respect-primary-co.patch
Patch268: 0268-dracut-add-omit-driver.patch
Patch269: 0269-lsinitrd-require-file-and-test-for-xz.patch
Patch270: 0270-99base-init-mount-with-sane-defaults.patch
Patch271: 0271-99base-dracut-lib.sh-wait_for_if_up-increase-wait-ti.patch
Patch272: 0272-90kernel-modules-installkernel-fixed-module-filterin.patch
Patch273: 0273-iscsiroot-whitespace-cleanup.patch
Patch274: 0274-iscsi-add-support-for-interface-binding.patch
Patch275: 0275-TEST-12-RAID-DEG-start-with-fresh-copies-of-the-test.patch
Patch276: 0276-TEST-40-NBD-add-check-for-nbd-server-binary.patch
Patch277: 0277-TEST-50-MULTINIC-refine-error-message.patch
Patch278: 0278-iscsi-parse-iscsiroot.sh-don-t-fail-for-netroot-iscs.patch
Patch279: 0279-iscsi-iscsiroot-fixed-iface.iscsi_ifacename-param.patch
Patch280: 0280-iscsi-iscsiroot-do-not-check-for-interfaces.patch
Patch281: 0281-use-git-to-apply-specfile-patches.patch
Patch282: 0282-mdraid-fix-raid-assembly-for-timeout.patch
Patch283: 0283-Revert-99base-init-mount-with-sane-defaults.patch
Patch284: 0284-fips-set-boot-as-symlink-to-sysroot-boot-if-no-boot-.patch
Patch285: 0285-dmsquash-live-enable-live-boot-with-netroot-iscsi.patch
Patch286: 0286-strip-kernel-modules-in-the-initramfs-by-default.patch
Patch287: 0287-dracut-functions-create-relative-symlinks-in-the-ini.patch
Patch288: 0288-fcoe-fcoe-up-sleep-for-3s-to-allow-dcb-negotiation.patch
Patch289: 0289-Document-rd_retry-parameter-and-set-default-to-40-se.patch
Patch290: 0290-Convert-MAC-addresses-to-lowercase-with-tr.patch
Patch291: 0291-dmsquash-live-dmsquash-live-root-add-no_eject-parame.patch
Patch292: 0292-network-parse-ip-opts.sh-relax-bootdev-handling.patch
Patch293: 0293-network-netroot-activate-debug-output-for-rddebug.patch
Patch294: 0294-network-netroot-only-netroot-for-bootdev-if-present.patch
Patch295: 0295-network-netroot-don-t-copy-empty-dhcp-files.patch
Patch296: 0296-nfs-install-don-t-install-nss3.so.patch
Patch297: 0297-testsuite-fixups.patch
Patch298: 0298-dracut.spec-add-02-fips.conf-with-do_strip-no.patch
Patch299: 0299-dracut-only-warn-not-error-if-we-don-t-strip.patch
Patch300: 0300-dmsquash-live-parse-dmsquash-live.sh-fixed-typo.patch
Patch301: 0301-add-VLAN-support.patch
Patch302: 0302-kernel-modules-installkernel-adding-scsi_dh_alua-to-.patch
Patch303: 0303-dracut.sh-create-the-initramfs-non-world-readable.patch
Patch304: 0304-base-initqueue-exit-0.patch
Patch305: 0305-dracut-unset-LD_LIBRARY_PATH-and-GREP_OPTIONS.patch
Patch306: 0306-add-mkinitrd-man-page.patch
Patch307: 0307-add-bonding.patch
Patch308: 0308-lvm-add-yes-to-lvchange.patch
Patch309: 0309-crypt-add-support-for-keyfiles-in-the-initramfs.patch
Patch310: 0310-Start-iscsi-regardless-of-network-if-requested.patch
Patch311: 0311-Install-multipath-module-only-when-root-is-multipath.patch
Patch312: 0312-fips-handle-checksum-checks-for-RHEV-kernels.patch
Patch313: 0313-dracut-add-xhci-hcd-driver.patch
Patch314: 0314-Improve-lsinitrd-and-add-lsinitrd-manpage.patch
Patch315: 0315-git2spec.pl-format-patch-on-RHEL-6-does-not-understa.patch
Patch316: 0316-plymouth-remove-cryptroot-ask.sh-which-is-provided-b.patch
Patch317: 0317-fips-update-kernel-module-list.patch
Patch318: 0318-fips-cope-with-module-aliases-when-checking-modules.patch
Patch319: 0319-rootfs-block-mount-root.sh-make-v-really-local-and-u.patch
Patch320: 0320-base-install-poweroff-and-reboot-and-set-aliases-wit.patch
Patch321: 0321-dracut.8-add-bond-and-bridge-documentation.patch
Patch322: 0322-network-rename-interfaces-properly.patch
Patch323: 0323-crypt-cryptroot-ask.sh-do-not-use-getargbool.patch
Patch324: 0324-fcoe-use-f-fcoe-for-fipvlan.patch
Patch325: 0325-fcoe-honor-autovlan-yes.patch
Patch326: 0326-selinux-give-emergency-shell-if-selinux-failed.patch
Patch327: 0327-crypt-cryptroot-ask-negate-rd_NO_CRYPTTAB.patch
Patch328: 0328-add-etc-redhat-fips.patch
Patch329: 0329-rename-etc-redhat-fips-to-etc-system-fips.patch
Patch330: 0330-network-fixed-ibft-parsing.patch
Patch331: 0331-do-not-turn-off-biosdevname-if-not-given-on-kernel-c.patch
Patch332: 0332-ldd-redirect-error-to-dev-null.patch
Patch333: 0333-fcoe-add-link-retry-100-to-fipvlan-call.patch
Patch334: 0334-network-ifname-genrules.sh-fixed-DRIVERS-udev-condit.patch
Patch335: 0335-fips-install-etc-system-fips-and-additional-hmac-fil.patch
Patch336: 0336-fips-fix-RHEV-vmlinuz-check.patch
Patch337: 0337-multipath-add-rd_NO_MULTIPATH-option.patch
Patch338: 0338-dracut-create-all-hookdirs.patch
Patch339: 0339-network-parse-ifname.sh-define-parse_ifname_opts.patch
Patch340: 0340-base-init-create-dev-btrfs-control.patch
Patch341: 0341-base-init-set-the-firmware-loading-timeout-to-600.patch
Patch342: 0342-git2spec.pl-no-signature.patch
Patch343: 0343-kernel-modules-installkernel-s-blk_init_queue-blk_cl.patch
Patch344: 0344-iscsi-parse-iscsiroot.sh-call-iscsistart-regardless.patch
Patch345: 0345-dracut.conf.5-add-install_items-to-man-page.patch
Patch346: 0346-rootfs-block-add-support-for-the-rootfallback-kernel.patch
Patch347: 0347-dracut-precreate-initqueue-hook-dirs.patch
Patch348: 0348-rootfs-block-install-it-s-initqueue-timeout-not-init.patch
Patch349: 0349-add-kate-and-emacs-per-directory-config-files.patch
Patch350: 0350-fcoe-support-multiple-fcoe-parameters.patch
Patch351: 0351-parse-ip-opts-fixed-ibft-parsing.patch
Patch352: 0352-init-remove-debug-log-pipe-if-loginit-process-killed.patch
Patch353: 0353-iscsi-parse-iscsiroot.sh-honor-blacklist-for-modprob.patch
Patch354: 0354-iscsi-iscsiroot-call-iscsiroot-in-the-background-onl.patch
Patch355: 0355-proper-debug-for-netroot-and-ifup.patch
Patch356: 0356-dracut-lib-error-out-on-empty-parm-for-parse_iscsi_r.patch
Patch357: 0357-iscsiroot-start-iscsistart-in-the-background.patch
Patch358: 0358-fips-add-drbg-kernel-module.patch
Patch359: 0359-lvm-also-install-etc-lvm-lvm_hostname.conf.patch
Patch360: 0360-dracut.logrotate-remove-yearly-and-increase-size.patch
Patch361: 0361-ifcfg-write-ifcfg.sh-write-vlan-ifcfg-files.patch
Patch362: 0362-crypt-cryptroot-ask.sh-handle-crypttab-without-endin.patch
Patch363: 0363-fips-nss-softokn-freebl-has-its-own-dracut-module-no.patch
Patch364: 0364-45ifcfg-write-ifcfg.sh-clarify-DHCPV6-case.patch
Patch365: 0365-network-netroot-setup-interface-correctly-before-bai.patch
Patch366: 0366-ifcfg-write-ifcfg.sh-if-a-lease-file-is-found-BOOTPR.patch
Patch367: 0367-ifcfg-write-ifcfg.sh-copy-over-all-dhcp-lease-files.patch
Patch368: 0368-netroot-do-not-bail-out-early.patch
Patch369: 0369-TEST-40-NBD-check-for-nbd-kernel-module.patch
Patch370: 0370-base-init-don-t-exit-the-main-loop-with-waiting-jobs.patch
Patch371: 0371-ifcfg-write-ifcfg.sh-use-the-correct-interface-name-.patch
Patch372: 0372-ifcfg-write-ifcfg.sh-do-not-source-net.-.override-if.patch
Patch373: 0373-ifcfg-write-ifcfg.sh-depend-on-dhcpopts-for-dhcp-mod.patch
Patch374: 0374-Add-hyperv-keyboard-kernel-module-for-Hyper-V-Gen2-V.patch
Patch375: 0375-Defer-modprobe-of-HW-modules-until-udev-is-running.patch
Patch376: 0376-iscsi-kill-iscsistart-after-10-seconds.patch
Patch377: 0377-iscsi-install-timeout-jobs-for-every-iscsi-netroot.patch
Patch378: 0378-iscsi-start-iscsi-only-for-iscsi-netroot.patch
Patch379: 0379-.dir-locals.el-fixup.patch
Patch380: 0380-lvm-install-all-lvm_-.conf-files-from-etc-lvm.patch
Patch381: 0381-network-move-ibft-parsing-to-own-script-before-main-.patch
Patch382: 0382-ibft-correct-device-name.patch
Patch383: 0383-network-remove-ibft-parsing-from-parse-ip-opts.patch
Patch384: 0384-dracut-functions-degrade-message-about-optional-miss.patch
Patch385: 0385-lvm-optionally-install-thin-tools.patch
Patch386: 0386-base-add-hostname-hostname-kernel-cmdline-parameter.patch
Patch387: 0387-crypt-add-drbg-kernel-module.patch
Patch388: 0388-crypt-installkernel-add-all-kernel-modules-regardles.patch
Patch389: 0389-dracut-set-pipefail-in-the-final-initramfs-creation-.patch
Patch390: 0390-plymouth-add-hyperv_fb-kernel-module.patch
Patch391: 0391-network-ifup-create-bond-interface-if-it-does-not-ye.patch
Patch392: 0392-dracut-use-cpio-with-R-root-root-rather-than-R-0-0.patch
Patch393: 0393-network-handle-macaddr-and-mtu.patch
Patch394: 0394-network-handle-multiple-vlan-parameters.patch
Patch395: 0395-dracut.8-mention-vlan-can-be-specified-multiple-time.patch
Patch396: 0396-nfs-install-also-add-group-nobody-for-rpc.idmapd.patch
Patch397: 0397-wait_for_if_up-check-for-UP-rather-than-state-UP.patch
Patch398: 0398-add-more-hyperv-kernel-modules.patch
Patch399: 0399-dracut-add-strglob.patch
Patch400: 0400-network-net-genrules.sh-add-physical-vlan-network-in.patch
Patch401: 0401-network-ifup-use-the-correct-interface-name-for-the-.patch
Patch402: 0402-iscsiroot-for-iscsi_firmware-retry-if-iscsistart-N-f.patch
Patch403: 0403-fix-typo.patch
Patch404: 0404-dracut.spec-remove-trailing-whitespace.patch
Patch405: 0405-network-ifup-fix-vlan-get_vid.patch
Patch406: 0406-plymouth-plymouth-pretrigger.sh-also-trigger-acpi-su.patch
Patch407: 0407-crypt-installkernel-install-more-crypto-modules.patch
Patch408: 0408-iscsi-iscsiroot-don-t-evaluate-iscsistart-N-return-v.patch
Patch409: 0409-iscsi-iscsistart-b-does-not-like-to-be-started-in-pa.patch


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
# no "provides", because dracut does not offer
# all functionality of the obsoleted packages
Obsoletes: mkinitrd <= 6.0.93
Obsoletes: mkinitrd-devel <= 6.0.93
Obsoletes: nash <= 6.0.93
Obsoletes: libbdevid-python <= 6.0.93
%endif

Requires: bash
Requires: bzip2
Requires: coreutils
Requires: cpio
Requires: dash
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: gzip
Requires: initscripts >= 8.63-1
Requires: kbd
Requires: mktemp >= 1.5-5
Requires: module-init-tools >= 3.7-9
Requires: mount
Requires: plymouth >= 0.8.0-0.2009.29.09.19.1
Requires: plymouth-scripts
Requires: sed
Requires: tar
Requires: udev
Requires: util-linux-ng >= 2.16
Requires: which
Requires: file

%if ! 0%{?with_switch_root}
Requires: util-linux-ng >= 2.16
BuildArch: noarch
%endif

BuildRequires: docbook-style-xsl docbook-dtds libxslt
BuildRequires: dash bash git

%description
dracut is a new, event-driven initramfs infrastructure based around udev.

%package network
Summary: Dracut modules to build a dracut initramfs with network support
Requires: %{name} = %{version}-%{release}
Requires: dhclient rpcbind nfs-utils
Requires: iscsi-initiator-utils
%if %{with_nbd}
Requires: nbd
%endif
Requires: net-tools iproute
Requires: bridge-utils

%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%package fips
Summary: Dracut modules to build a dracut initramfs with an integrity check
Requires: %{name} = %{version}-%{release}
Requires: hmaccalc fipscheck
%if 0%{?rhel} > 5
# For Alpha 3, we want nss instead of nss-softokn
Requires: nss
%else
Requires: nss-softokn
%endif
Requires: nss-softokn-freebl >= 3.14.3-22.el6_6

%description fips
This package requires everything which is needed to build an
all purpose initramfs with dracut, which does an integrity check.

%package fips-aesni
Summary: Dracut modules to build a dracut initramfs with an integrity check with aesni-intel
Requires: %{name}-fips = %{version}-%{release}

%description fips-aesni
This package requires everything which is needed to build an
all purpose initramfs with dracut, which does an integrity check
and adds the aesni-intel kernel module.

%package caps
Summary: Dracut modules to build a dracut initramfs which drops capabilities
Requires: %{name} = %{version}-%{release}
Requires: libcap

%description caps
This package requires everything which is needed to build an
all purpose initramfs with dracut, which drops capabilities.

%package generic
Summary: Metapackage to build a generic initramfs with dracut
Requires: %{name} = %{version}-%{release}
Requires: %{name}-network = %{version}-%{release}

%description generic
This package requires everything which is needed to build a generic
all purpose initramfs with dracut.


%package kernel
Summary: Metapackage to build generic initramfs with dracut with only kernel modules
Requires: %{name} = %{version}-%{release}

%description kernel
This package requires everything which is needed to build a initramfs with all
kernel modules and firmware files needed by dracut modules.

%package tools
Summary: Dracut tools to build the local initramfs
Requires: %{name} = %{version}-%{release}
Requires: coreutils cryptsetup-luks device-mapper
Requires: diffutils dmraid findutils gawk grep lvm2
Requires: module-init-tools sed
Requires: cpio gzip

%description tools
This package contains tools to assemble the local initrd and host configuration.

%prep
%setup -q -n %{name}-%{version}

%if %{defined PATCH1}
git init
git config user.email "dracut-maint@redhat.com"
git config user.name "Fedora dracut team"
git add .
git commit -a -q -m "%{version} baseline."

# Apply all the patches.
git am -p1 %{patches}
%endif

chmod 0755 modules.d/*/check
# make rpmlint happy
chmod 0755 modules.d/*/install
chmod 0755 modules.d/*/installkernel
chmod 0755 modules.d/*/*.sh

%build
make WITH_SWITCH_ROOT=0%{?with_switch_root}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sbindir=/sbin \
     sysconfdir=/etc mandir=%{_mandir} WITH_SWITCH_ROOT=0%{?with_switch_root}

echo %{name}-%{version}-%{release} > $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/10rpmversion/dracut-version
rm $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/01fips/check
rm $RPM_BUILD_ROOT/%{_datadir}/dracut/modules.d/02fips-aesni/check

mkdir -p $RPM_BUILD_ROOT/boot/dracut
mkdir -p $RPM_BUILD_ROOT/var/lib/dracut/overlay
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
touch $RPM_BUILD_ROOT%{_localstatedir}/log/dracut.log

%if 0%{?fedora} <= 12 && 0%{?rhel} < 6
rm $RPM_BUILD_ROOT/sbin/mkinitrd
rm $RPM_BUILD_ROOT/sbin/lsinitrd
%endif

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 0644 dracut.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/dracut

echo 'do_strip=no' > $RPM_BUILD_ROOT/etc/dracut.conf.d/02-fips.conf
> $RPM_BUILD_ROOT/etc/system-fips

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS dracut-rhel6.html
/sbin/dracut
%if 0%{?with_switch_root}
/sbin/switch_root
%endif
%if 0%{?fedora} > 12 || 0%{?rhel} >= 6
/sbin/mkinitrd
/sbin/lsinitrd
%endif
%dir %{_datadir}/dracut
%{_datadir}/dracut/dracut-functions
%config(noreplace) /etc/dracut.conf
%dir /etc/dracut.conf.d
%config(noreplace) /etc/logrotate.d/dracut
%{_mandir}/man1/lsinitrd.1*
%{_mandir}/man8/mkinitrd.8*
%{_mandir}/man8/dracut.8*
%{_mandir}/man5/dracut.conf.5*
%{_datadir}/dracut/modules.d/00dash
%{_datadir}/dracut/modules.d/10redhat-i18n
%{_datadir}/dracut/modules.d/10rpmversion
%{_datadir}/dracut/modules.d/50plymouth
%{_datadir}/dracut/modules.d/60xen
%{_datadir}/dracut/modules.d/90btrfs
%{_datadir}/dracut/modules.d/90crypt
%{_datadir}/dracut/modules.d/90dm
%{_datadir}/dracut/modules.d/90dmraid
%{_datadir}/dracut/modules.d/90dmsquash-live
%{_datadir}/dracut/modules.d/90kernel-modules
%{_datadir}/dracut/modules.d/90lvm
%{_datadir}/dracut/modules.d/90mdraid
%{_datadir}/dracut/modules.d/90multipath
%{_datadir}/dracut/modules.d/95debug
%{_datadir}/dracut/modules.d/95fstab-sys
%{_datadir}/dracut/modules.d/95resume
%{_datadir}/dracut/modules.d/95rootfs-block
%{_datadir}/dracut/modules.d/95dasd
%{_datadir}/dracut/modules.d/95dasd_mod
%{_datadir}/dracut/modules.d/95zfcp
%{_datadir}/dracut/modules.d/95znet
%{_datadir}/dracut/modules.d/95terminfo
%{_datadir}/dracut/modules.d/95udev-rules
%{_datadir}/dracut/modules.d/95uswsusp
%{_datadir}/dracut/modules.d/96insmodpost
%{_datadir}/dracut/modules.d/97biosdevname
%{_datadir}/dracut/modules.d/98syslog
%{_datadir}/dracut/modules.d/99base
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log

%files network
%defattr(-,root,root,0755)
%doc README HACKING TODO COPYING AUTHORS NEWS
%{_datadir}/dracut/modules.d/40network
%{_datadir}/dracut/modules.d/95fcoe
%{_datadir}/dracut/modules.d/95iscsi
%{_datadir}/dracut/modules.d/95nbd
%{_datadir}/dracut/modules.d/95nfs
%{_datadir}/dracut/modules.d/45ifcfg

%files fips
%defattr(-,root,root,0755)
%doc COPYING
%{_datadir}/dracut/modules.d/01fips
%config(noreplace) /etc/dracut.conf.d/02-fips.conf
%config(missingok) /etc/system-fips

%files fips-aesni
%defattr(-,root,root,0755)
%doc COPYING
%{_datadir}/dracut/modules.d/02fips-aesni

%files caps
%defattr(-,root,root,0755)
%doc COPYING
%{_datadir}/dracut/modules.d/02caps

%files kernel
%defattr(-,root,root,0755)
%doc README.kernel

%files generic
%defattr(-,root,root,0755)
%doc README.generic

%files tools
%defattr(-,root,root,0755)
%doc COPYING NEWS
%{_mandir}/man8/dracut-gencmdline.8*
%{_mandir}/man8/dracut-catimages.8*
/sbin/dracut-gencmdline
/sbin/dracut-catimages
%dir /boot/dracut
%dir /var/lib/dracut
%dir /var/lib/dracut/overlay

%changelog
* Fri Apr 29 2016 Harald Hoyer <harald@redhat.com> - 004-409.2
- rebuild for z
Resolves: rhbz#1322209

* Fri Apr 29 2016 Harald Hoyer <harald@redhat.com> - 004-409.1
- cannot start multiple "iscsistart -b" in parallel
Resolves: rhbz#1322209

* Thu Apr 07 2016 Harald Hoyer <harald@redhat.com> - 004-409
- don't handle "iscsistart -N" exit value
  start iscsistart -b more reliably in the background
Resolves: rhbz#1324340

* Wed Apr 06 2016 Harald Hoyer <harald@redhat.com> - 004-408
- add more kernel modules for crypt
Resolves: rhbz#1322893
- trigger acpi subsystem before running plymouth
Resolves: rhbz#1218130

* Thu Mar 10 2016 Harald Hoyer <harald@redhat.com> - 004-406
- network/ifup: fix vlan get_vid()
Resolves: rhbz#1111358

* Thu Mar 10 2016 Harald Hoyer <harald@redhat.com> - 004-405
- iscsiroot: fixed typo
Resolves: rhbz#1111358

* Thu Mar 10 2016 Harald Hoyer <harald@redhat.com> - 004-403
- network/ifup: use the correct interface name for the vlan parent
- iscsiroot: for iscsi_firmware retry, if iscsistart -N fails
Resolves: rhbz#1111358

* Mon Mar 07 2016 Harald Hoyer <harald@redhat.com> 004-401
- generate udev rules for the physical interface of vlans
Resolves: rhbz#1111358

* Thu Feb 18 2016 Harald Hoyer <harald@redhat.com> 004-400
- backport the strglob function
Resolves: rhbz#1309298

* Tue Jan 19 2016 Harald Hoyer <harald@redhat.com> 004-399
- add hyper kernel modules
Resolves: rhbz#1298445 rhbz#1223315
- fix ifcfg generation
Resolves: rhbz#1261893
- support multiple vlan definitions
Resolves: rhbz#1111358
- support setting of MTU via ip=..:ibft:<mtu>
Resolves: rhbz#1076465
- use cpio -R root:root rather than cpio -R 0:0
Resolves: rhbz#1049763
- fail hard if final image could not be written
Resolves: rhbz#1252449
- create correct bonding interface
Resolves: rhbz#1263013

* Tue Jun 23 2015 Harald Hoyer <harald@redhat.com> 004-388
- add drbg kernel module for crypto
Resolves: rhbz#1233683

* Fri Jun 05 2015 Harald Hoyer <harald@redhat.com> 004-387
- add parameter to set the hostname
Resolves: rhbz#1226905

* Wed Jun 03 2015 Harald Hoyer <harald@redhat.com> 004-386
- add lvm thin tools
Resolves: rhbz#1226905

* Thu May 28 2015 Harald Hoyer <harald@redhat.com> 004-384
- fix vlan with iBFT
Resolves: rhbz#1111358

* Thu May 21 2015 Harald Hoyer <harald@redhat.com> 004-381
- lvm: install all lvm_*.conf files from /etc/lvm
Resolves: rhbz#1130565

* Fri May 08 2015 Harald Hoyer <harald@redhat.com> 004-380
- load iSCSI modules after udevd is started for firmware
  loading
Resolves: rhbz#1213077
- add the hyperv-keyboard kernel module for Hyper-V Gen2 VM
Resolves: rhbz#1205095
- starting iscsistart in parallel has problems, if on the same
  network interface
Resolves: rhbz#1209406

* Tue Mar 17 2015 Harald Hoyer <harald@redhat.com> 004-374
- more ifcfg write fixes
Resolves: rhbz#1198117

* Tue Mar 03 2015 Harald Hoyer <harald@redhat.com> 004-371
- start iscistart in the background
Resolves: rhbz#1191721 rhbz#1176671
- require nss-softokn-freebl >= 3.14.3-22.el6_6
  and remove libfreebl3* inclusion as nss-softokn-freebl
  has its own dracut module
Resolves: rhbz#1184142
- logrotate: remove yearly keyword
Resolves: rhbz#1005886
- let ip=ibft boot without ifname=...
Resolves: rhbz#1069275
- save vlan info in ifcfg files
Resolves: rhbz#1111358
- include /etc/lvm/lvm_hostname.conf if present
Resolves: rhbz#1130565
- handle /etc/crypttab without newline at the end of the last line
Resolves: rhbz#1085562
- copy over dhcp lease files of all interfaces and write
  correct ifcfg file
Resolves: rhbz#1198117

* Thu Feb 19 2015 Harald Hoyer <harald@redhat.com> 004-359
- fips: load drbg kernel module
Resolves: rhbz#1193528

* Fri Sep 05 2014 Harald Hoyer <harald@redhat.com> 004-356
- fixed support for multiple fcoe devices
Resolves: rhbz#1022766
- fixed iscsiroot with iscsi_firmware boot
Resolves: rhbz#1126346

* Mon Jun 02 2014 Harald Hoyer <harald@redhat.com> 004-349
- fixed patch for rootfallback
Resolves: rhbz#737687

* Wed May 28 2014 Harald Hoyer <harald@redhat.com> 004-347
- backport of the rootfallback= kernel cmdline option
Resolves: rhbz#737687
- call iscsistart regardless of network failures
Resolves: rhbz#1099603
- set the firmware loading timeout to 600
Related: rhbz#1077186
- add install_items to dracut.conf man page
Resolves: rhbz#1041484
- pickup nvme driver
Resolves: rhbz#1041484
- create  /dev/btrfs-control
Resolves: rhbz#1070676
- create all hook directories
Resolves: rhbz#1051448

* Wed Nov 27 2013 Harald Hoyer <harald@redhat.com> 004-338
- add rd_NO_MULTIPATH option
Resolves: rhbz#1034327

* Tue Nov 12 2013 Harald Hoyer <harald@redhat.com> 004-337
- fix FIPS kernel check for RHEV-H
Resolves: rhbz#1028435

* Wed Nov 06 2013 Harald Hoyer <harald@redhat.com> 004-336
- install /etc/system-fips in the initramfs
Resolves: rhbz#1012626

* Tue Oct 15 2013 Harald Hoyer <harald@redhat.com> 004-335
- fixed interface renaming
Resolves: rhbz#1019104

* Mon Oct 14 2013 Harald Hoyer <harald@redhat.com> 004-334
- fcoe: add --link-retry=100 to fipvlan call
Resolves: rhbz#1012316
- ldd: redirect error to /dev/null
- do not turn off biosdevname, if not given on kernel cmdline
Resolves: rhbz#1011508
- network: fixed ibft parsing
Resolves: rhbz#1011508

* Wed Oct 02 2013 Harald Hoyer <harald@redhat.com> 004-330
- changed /etc/redhat-fips to /etc/system-fips
Resolves: rhbz#1012626

* Tue Oct 01 2013 Harald Hoyer <harald@redhat.com> 004-329
- add /etc/redhat-fips
Resolves: rhbz#1012626

* Tue Sep 03 2013 Harald Hoyer <harald@redhat.com> 004-328
- fixed crypt: add support for keyfiles in the initramfs
Resolves: rhbz#886194

* Thu Aug 29 2013 Harald Hoyer <harald@redhat.com> 004-327
- fixed crypt: add support for keyfiles in the initramfs
Resolves: rhbz#886194
- fixed booting with iSCSI and without network config
Resolves: rhbz#910605

* Fri Aug 09 2013 Harald Hoyer <harald@redhat.com> 004-322
- fixed crypt: add support for keyfiles in the initramfs
Resolves: rhbz#886194
- fixed FIPS module checking
Resolves: rhbz#947729

* Thu Jul 18 2013 Harald Hoyer <harald@redhat.com> 004-316
- create the initramfs non-world readable
- unset LD_LIBRARY_PATH and GREP_OPTIONS
Resolves: rhbz#912299
- add mkinitrd man page
Resolves: rhbz#610462
- add bonding
Resolves: rhbz#851666
- lvm: add "--yes" to lvchange
Resolves: rhbz#720684
- crypt: add support for keyfiles in the initramfs
Resolves: rhbz#886194
- start iscsi regardless of network, if requested
Resolves: rhbz#813687
- install multipath module only, when root is multipath in generic mode
Resolves: rhbz#916144
- fips: handle checksum checks for RHEV kernels
Resolves: rhbz#947729
- add xhci-hcd driver
Resolves: rhbz#960729

* Wed Jan 09 2013 Harald Hoyer <harald@redhat.com> 004-303
- add scsi_dh_alua to the hardcoded drivers to include in the initramfs
Resolves: rhbz#890081

* Fri Oct 19 2012 Harald Hoyer <harald@redhat.com> 004-302
- add vlan support
Resolves: rhbz#858187
- fixed "LiveCD boot from iscsi targets" patch (Regression bug 863964)
Resolves: rhbz#794751

* Fri Oct 12 2012 Harald Hoyer <harald@redhat.com> 004-298
- fixed fcoe-up script for new Brocade switch
Resolves: rhbz#813057
- document "rd_retry" option in dracut(8) man page
Resolves: rhbz#823507
- convert all MAC parameter to lowercase
Resolves: rhbz#835646
- add "no_eject" option for "live_ram"
Resolves: rhbz#843105

* Thu Sep 20 2012 Harald Hoyer <harald@redhat.com> 004-287.git20120920
- enabled LiveCD boot from iscsi targets
Resolves: rhbz#794751

* Mon Sep 10 2012 Harald Hoyer <harald@redhat.com> 004-286.git20120910
- fixed fips with /boot in real root
Resolves: rhbz#850493

* Thu Jul 12 2012 Harald Hoyer <harald@redhat.com> 004-284
- Revert proc mount with restrictive options
Resolves: rhbz#831338

* Fri Apr 27 2012 Harald Hoyer <harald@redhat.com> 004-283
- fix incomplete fix for degraded raids
Resolves: rhbz#761584

* Thu Apr 19 2012 Harald Hoyer <harald@redhat.com> 004-282
- fix for iscsi interface binding
Resolves: rhbz#797158

* Mon Apr 02 2012 Harald Hoyer <harald@redhat.com> 004-281
- fix for lsinitrd and LZMA file types
Resolves: rhbz#752005

* Thu Mar 29 2012 Harald Hoyer <harald@redhat.com> 004-280
- fixed iface.iscsi_ifacename param
Resolves: rhbz#797158

* Wed Mar 28 2012 Harald Hoyer <harald@redhat.com> 004-279
- add iscsi interface binding (fixup for iscsi_firmware)
Resolves: rhbz#797158

* Wed Mar 28 2012 Harald Hoyer <harald@redhat.com> 004-278
- add iscsi interface binding
Resolves: rhbz#797158

* Mon Mar 05 2012 Harald Hoyer <harald@redhat.com> 004-273
- fixed option --omit-drivers
Resolves: rhbz#722879
- increase wait time for network interfaces to get UP to 10s
Resolves: rhbz#794863

* Thu Mar 01 2012 Harald Hoyer <harald@redhat.com> 004-271
- no vconfig requirement anymore
Resolves: rhbz#714039
- new option --omit-drivers
Resolves: rhbz#722879
- suppress udevadm settle output
Resolves: rhbz#747840
- extend lsinitrd to cope with xz images
Resolves: rhbz#752005
- respect primary console setting
Resolves: rhbz#752073

* Wed Feb 15 2012 Harald Hoyer <harald@redhat.com> 004-268
- fixed dracut manpage
Resolves: rhbz#703164
- fixed assembling of mdraid degraded arrays
Resolves: rhbz#761584
- fixed ifup to set broadcast address
Resolves: rhbz#752584
- fixed iscsiroot for multiple iscsi disks
Resolves: rhbz#752066

* Wed Feb 15 2012 Harald Hoyer <harald@redhat.com> 004-257
- fixed loading of dracut-fips-aesni module
Resolves: rhbz#788119

* Fri Nov 04 2011 Harald Hoyer <harald@redhat.com> 004-256
- increase timeout to wait for dhcp connections
Resolves: rhbz#742920
- check /tmp/net.$netif.override before sourcing it
Resolves: rhbz#696980

* Tue Oct 18 2011 Harald Hoyer <harald@redhat.com> 004-254
- fixed killproc()
Resolves: rhbz#701864
- hardcode modprobe of various iscsi offload drivers
Resolves: rhbz#737134

* Mon Oct 10 2011 Harald Hoyer <harald@redhat.com> 004-248
- 95fcoe/fcoe-up: load 8021q module before fipvlan
Resolves: rhbz#736094
- modprobe iscsi_boot_sysfs
Resolves: rhbz#737134

* Wed Sep 28 2011 Harald Hoyer <harald@redhat.com> 004-247
- add "-F" to selinux restorecon 
Resolves: rhbz#741430
- kill iscsiuio before switching root
Resolves: rhbz#701864

* Fri Sep 23 2011 Harald Hoyer <harald@redhat.com> 004-244
- add dracut-fips-aesni subpackage
Resolves: rhbz#740487 
- add /var/log in initramfs
Resolves: rhbz#701864

* Wed Sep 21 2011 Harald Hoyer <harald@redhat.com> 004-242
- fixed minimal install
Resolves: rhbz#736671

* Tue Sep 20 2011 Harald Hoyer <harald@redhat.com> 004-239
- fixed raid assembly with encrypted members
Resolves: rhbz#737593
- support bnx2fc for FCoE
Resolves: rhbz#736094
- fixed iscsi module loading
Resolves: rhbz#737479

* Fri Sep 09 2011 Harald Hoyer <harald@redhat.com> 004-235
- do not display selinux info message, if selinux is disabled
Resolves: rhbz#659076

* Wed Aug 24 2011 Harald Hoyer <harald@redhat.com> 004-234
- add broadcom iscsi offload support
Resolves: rhbz#701864
- fixed dm dracut module, to no require dmraid
Resolves: rhbz#732686
- fixed md raid assembly
Resolves: rhbz#732967

* Fri Aug 05 2011 Harald Hoyer <harald@redhat.com> 004-231
- add more kernel modules for iSCSI
Resolves: rhbz#696980
- chown /var/lib/rpcbind to rpc user and make it 770
Resolves: rhbz#698160
- remove "--no-degraded" from mdadm arguments
Resolves: rhbz#698165
- remove script error in mdraid_start.sh
Resolves: rhbz#698215
- parse and mount fstab.sys
Resolves: rhbz#701309
- add "dm-mod" and "dm-crypt" to fips modules
Resolves: rhbz#707609
- set LANG=C for chrooted selinux operations
Resolves: rhbz#712254
- use "--partial" to assemble degraded lvm mirrors
Resolves: rhbz#723548
- spec file patch cleanup to resemble git repo at
http://git.kernel.org/?p=boot/dracut/dracut.git;a=shortlog;h=refs/heads/RHEL-6

* Wed Apr 27 2011 Harald Hoyer <harald@redhat.com> 004-53
- fixed "ip=ibft" (mganisin@redhat.com)
Resolves: rhbz#640979

* Mon Apr 18 2011 Harald Hoyer <harald@redhat.com> 004-52
- fips: support /boot on LVM Volume for non-encrypted root
- preunlink binaries in fips mode
Resolves: rhbz#696131
- Fixed FCoE booting with EDD information

* Wed Apr 13 2011 Harald Hoyer <harald@redhat.com> 004-50
- fips: small settle loop to wait for /boot
Resolves: rhbz#696131

* Mon Apr 11 2011 Harald Hoyer <harald@redhat.com> 004-49
- make fips work with separate boot and encrypted root
Resolves: rhbz#692843

* Fri Apr 08 2011 Harald Hoyer <harald@redhat.com> 004-48
- removed rd.fips.skipkernel and move fipscheck to a later
  point of time, where root is already mounted
Resolves: rhbz#692843

* Wed Apr 06 2011 Harald Hoyer <harald@redhat.com> 004-47
- added iscsi kernel driver
Resolves: rhbz#689694
- added rd.fips.skipkernel
Resolves: rhbz#692843

* Wed Mar 30 2011 Harald Hoyer <harald@redhat.com> 004-46
- fixed boot=UUID=<dev> for fips
Resolves: rhbz#691419

* Wed Mar 09 2011 Harald Hoyer <harald@redhat.com> 004-44
- fixed die() and emergency mode for fips
Resolves: rhbz#670925
- added dracut-caps with caps module
Resolves: rhbz#677340

* Wed Mar 02 2011 Harald Hoyer <harald@redhat.com> 004-43
- fixed "fips=0"
- fixed .hmac file installation for hostonly mode
- hardcode to include libssl.so* in fips
Resolves: rhbz#670925

* Tue Mar 01 2011 Harald Hoyer <harald@redhat.com> 004-42
- fixed instmods() for fips module
- do not load tcrypt with "noexit" parameter
Resolves: rhbz#670925

* Mon Feb 28 2011 Harald Hoyer <harald@redhat.com> 004-41
- add "xts gf128mul" to FIPSMODULES
Resolves: rhbz#670925

* Fri Feb 25 2011 Harald Hoyer <harald@redhat.com> 004-40
- fixed dracut logging
Resolves: rhbz#676018
- fixed biosdevname module
Resolves: rhbz#675118

* Wed Feb 16 2011 Harald Hoyer <harald@redhat.com> 004-39
- do not write to /tmp/dracut.log
Resolves: rhbz#676018

* Tue Feb 08 2011 Harald Hoyer <harald@redhat.com> 004-38
- fixed biosdevname module
Resolves: rhbz#675118

* Thu Feb 03 2011 Harald Hoyer <harald@redhat.com> 004-37
- add aes-xts in FIPS module
Resolves: rhbz#670925
- start multipathd with the new -B option
Resolves: rhbz#674238

* Wed Jan 26 2011 Harald Hoyer <harald@redhat.com> 004-36
- add biosdevname module
Resolves: rhbz#653901
- install .hmac files for fips
Resolves: rhbz#669438

* Wed Dec 08 2010 Harald Hoyer <harald@redhat.com> 004-35
- fixed typo
Resolves: rhbz#634013

* Wed Dec 08 2010 Harald Hoyer <harald@redhat.com> 004-34
- fix md rule generation
Resolves: rhbz#595096
- add 96insmodpost dracut module
Resolves: rhbz#645648
- add "--force" to mkinitrd
Resolves: rhbz#610466
- fix dmraid without mdadm
Resolves: rhbz#626389
- install the complete /etc/multipath directory
Resolves: rhbz#630911
- install multipath by default, but run only if wwids are present
Resolves: rhbz#636668 rhbz#642083
- removed vconfig dependency
Resolves: rhbz#645799
- install all md/dm modules
Resolves: rhbz#626389
- add fcoe=edd parameter
Resolves: rhbz#634013
- add ip=ibft parameter
Resolves: rhbz#640979

* Tue Nov 09 2010 Harald Hoyer <harald@redhat.com> 004-33
- honor DM_UDEV_DISABLE_OTHER_RULES_FLAG
Resolves: rhbz#650959

* Thu Aug 19 2010 Harald Hoyer <harald@redhat.com> 004-32
- do not call dracut with hostonly from within mkinitrd
Resolves: rhbz#624826

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 004-31
- also search in "updates"
Resolves: rhbz#622641

* Tue Aug 10 2010 Harald Hoyer <harald@redhat.com> 004-30
- search for kernel modules also in "extra" and "weak-updates"
Resolves: rhbz#622641

* Thu Jul 29 2010 Harald Hoyer <harald@redhat.com> 004-29
- strip "luks-" from rd_LUKS_UUID while processing
Resolves: rhbz#607699

* Thu Jul 29 2010 Harald Hoyer <harald@redhat.com> 004-28
- do not set strict umask
Resolves: rhbz#617526

* Tue Jul 27 2010 Harald Hoyer <harald@redhat.com> 004-27
- fixed device permission
Resolves: rhbz#617526 

* Fri Jul 23 2010 Harald Hoyer <harald@redhat.com> 004-26
- wait for LVM and crypt devices to appear
Resolves: rhbz#607699
- add sleeps to fcoe-up and move it out of udev
Resolves: rhbz#611976
- fixed selinux return code handling
Resolves: rhbz#615950

* Fri Jul 09 2010 Harald Hoyer <harald@redhat.com> 004-25
- mount live images to /dev/.initramfs/live and do not
  umount it, so that cdrom_id works in the real root
  and /dev/live is pointing to the correct device
Resolves: rhbz#605356

* Mon Jul 05 2010 Harald Hoyer <harald@redhat.com> 004-24
- removed dependency of tools, which should be installed 
  by anaconda
Resolves: rhbz#598509

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 004-23
- add vconfig requirement to dracut-network
Resolves: rhbz#608015
- fixed dhcp6 option for ip argument
Resolves: rhbz#605283

* Mon Jun 21 2010 Harald Hoyer <harald@redhat.com> 004-22
- add fpu kernel module to crypt
Resolves: rhbz#600170

* Fri Jun 11 2010 Harald Hoyer <harald@redhat.com> 004-21
- Remove requirements, which are not really needed
Resolves: rhbz#598509
- fixed copy of network config to /dev/.initramfs/ (patch 146)
Resolves: rhbz#594649
- more password beauty (patch 142)
Resolves: rhbz#561092
- support multiple iSCSI disks (patch 143)
Resolves: rbhz#580190
- fixed selinux=0 (patch 130)
Resolves: rhbz#593080
- add support for booting LVM snapshot root volume (patch 145)
Resolves: rbhz#602723
- remove hardware field from BOOTIF= (patch 148)
Resolves: rhbz#599593
- add aes kernel modules and fix crypt handling (patch 137, patch 140 and patch 147)
Resolves: rhbz#600170

* Wed Jun 02 2010 Phil Knirsch <pknirsch@redhat.com> 004-20.1
- Reverted and fixed up most of the requirement changes
Resolves: #598509

* Thu May 27 2010 Harald Hoyer <harald@redhat.com> 004-20
- fixed Requirements
- fixed autoip6 
Resolves: rhbz#538388
- fixed multipath
Resolves: rhbz#595719

* Thu May 06 2010 Harald Hoyer <harald@redhat.com> 004-19
- only display short password messages
Resolves: rhbz#561092

* Thu May 06 2010 Harald Hoyer <harald@redhat.com> 004-18
- fixed dracut manpages 
Resolves: rhbz#589109
- use ccw-init and ccw rules from s390utils
Resolves: rhbz#533494
- fixed fcoe
Resolves: rhbz#486244
- various other bugfixes seen in Fedora

* Thu Mar 25 2010 Harald Hoyer <harald@redhat.com> 004-17
- removed firmware requirements (rhbz#572634)
- add /etc/dracut.conf.d
- Resolves: rhbz#572634

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 004-16
- fixed rpmlint errors (rhbz#570547)
- removed firmware package from dracut-kernel (rhbz#572634)
- add dcb support to dracut's FCoE support (rhbz#563794)
- force install some modules in hostonly mode (rhbz#573094)
- various other bugfixes
- Resolves: rhbz#570547, rhbz#572634, rhbz#563794, rhbz#573094

* Thu Feb 18 2010 Harald Hoyer <harald@redhat.com> 004-15
- fixed "selinux=0" booting (rhbz#566376)
- fixed internal IFS handling
- Resolves: rhbz#566376

* Wed Feb 17 2010 Harald Hoyer <harald@redhat.com> 004-14
- fixed remount root (rhbz#566246)
- Resolves: rhbz#566246

* Wed Feb 17 2010 Harald Hoyer <harald@redhat.com> 004-13
- fixed multipath scanning
- fixed NFS4 (rhbz#564293)
- add /etc/dracut.conf.d config dir
- fixed selinux disabled state
- fixed s390 cio scripts
- fixed lib64 check (rhbz#562113)
- Resolves: rhbz#564293, rhbz#562113 

* Mon Feb 08 2010 Harald Hoyer <harald@redhat.com> 004-12
- add IPv6 support
- fixed multipath check
- fixed selinux autorelabel case
- Resolves: rhbz#546615 rhbz#553195

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 004-3
- fix selinux handling if .autorelabel is present
- Resolves: rhbz#557744

* Wed Jan 20 2010 Harald Hoyer <harald@redhat.com> 004-2
- fix emergency_shell argument parsing
- Related: rhbz#543948

* Fri Jan 15 2010 Harald Hoyer <harald@redhat.com> 004-1
- version 004
- Resolves: rhbz#529339 rhbz#533494 rhbz#548550 
- Resolves: rhbz#548555 rhbz#553195

* Wed Jan 13 2010 Harald Hoyer <harald@redhat.com> 003-3
- add Obsoletes of mkinitrd/nash/libbdevid-python
- Related: rhbz#543948

* Wed Jan 13 2010 Warren Togami <wtogami@redhat.com> 003-2
- nbd is Fedora only

* Fri Nov 27 2009 Harald Hoyer <harald@redhat.com> 003-1
- version 003

* Mon Nov 23 2009 Harald Hoyer <harald@redhat.com> 002-26
- add WITH_SWITCH_ROOT make flag
- add fips requirement conditional
- add more device mapper modules (bug #539656)

* Fri Nov 20 2009 Dennis Gregorovic <dgregor@redhat.com> - 002-25.1
- nss changes for Alpha 3

* Thu Nov 19 2009 Harald Hoyer <harald@redhat.com> 002-25
- add more requirements for dracut-fips (bug #539257)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-24
- put fips module in a subpackage (bug #537619)

* Tue Nov 17 2009 Harald Hoyer <harald@redhat.com> 002-23
- install xdr utils for multipath (bug #463458)

* Thu Nov 12 2009 Harald Hoyer <harald@redhat.com> 002-22
- add module 90multipath
- add module 01fips
- renamed module 95ccw to 95znet (bug #533833)
- crypt: ignore devices in /etc/crypttab (root is not in there)
- dasd: only install /etc/dasd.conf in hostonly mode (bug #533833)
- zfcp: only install /etc/zfcp.conf in hostonly mode (bug #533833)
- kernel-modules: add scsi_dh scsi_dh_rdac scsi_dh_emc (bug #527750)
- dasd: use dasdconf.sh from s390utils (bug #533833)

* Fri Nov 06 2009 Harald Hoyer <harald@redhat.com> 002-21
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Wed Nov 04 2009 Harald Hoyer <harald@redhat.com> 002-20
- fix rd_DASD argument handling (bug #531720)
- Resolves: rhbz#531720

* Tue Nov 03 2009 Harald Hoyer <harald@redhat.com> 002-19
- changed rd_DASD to rd_DASD_MOD (bug #531720)
- Resolves: rhbz#531720

* Tue Oct 27 2009 Harald Hoyer <harald@redhat.com> 002-18
- renamed lvm/device-mapper udev rules according to upstream changes
- fixed dracut search path issue

* Mon Oct 26 2009 Harald Hoyer <harald@redhat.com> 002-17
- load dm_mod module (bug #530540)

* Fri Oct 09 2009 Jesse Keating <jkeating@redhat.com> - 002-16
- Upgrade plymouth to Requires(pre) to make it show up before kernel

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-15
- s390 ccw: s/layer1/layer2/g

* Thu Oct 08 2009 Harald Hoyer <harald@redhat.com> 002-14
- add multinic support
- add s390 zfcp support
- add s390 network support

* Wed Oct 07 2009 Harald Hoyer <harald@redhat.com> 002-13
- fixed init=<command> handling
- kill loginit if "rdinitdebug" specified
- run dmsquash-live-root after udev has settled (bug #527514)

* Tue Oct 06 2009 Harald Hoyer <harald@redhat.com> 002-12
- add missing loginit helper
- corrected dracut manpage

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-11
- fixed dracut-gencmdline for root=UUID or LABEL

* Thu Oct 01 2009 Harald Hoyer <harald@redhat.com> 002-10
- do not destroy assembled raid arrays if mdadm.conf present
- mount /dev/shm 
- let udevd not resolve group and user names
- preserve timestamps of tools on initramfs generation
- generate symlinks for binaries correctly
- moved network from udev to initqueue
- mount nfs3 with nfsvers=3 option and retry with nfsvers=2
- fixed nbd initqueue-finished
- improved debug output: specifying "rdinitdebug" now logs
  to dmesg, console and /init.log
- stop udev before killing it
- add ghost /var/log/dracut.log
- dmsquash: use info() and die() rather than echo
- strip kernel modules which have no x bit set
- redirect stdin, stdout, stderr all RW to /dev/console
  so the user can use "less" to view /init.log and dmesg

* Tue Sep 29 2009 Harald Hoyer <harald@redhat.com> 002-9
- make install of new dm/lvm udev rules optionally
- correct dasd module typo

* Fri Sep 25 2009 Warren Togami <wtogami@redhat.com> 002-8
- revert back to dracut-002-5 tarball 845dd502
  lvm2 was reverted to pre-udev

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-7
- build with the correct tarball

* Wed Sep 23 2009 Harald Hoyer <harald@redhat.com> 002-6
- add new device mapper udev rules and dmeventd 
  bug 525319, 525015

* Wed Sep 23 2009 Warren Togami <wtogami@redaht.com> 002-5
- Revert back to -3, Add umount back to initrd
  This makes no functional difference to LiveCD.  See Bug #525319

* Mon Sep 21 2009 Warren Togami <wtogami@redhat.com> 002-4
- Fix LiveCD boot regression

* Mon Sep 21 2009 Harald Hoyer <harald@redhat.com> 002-3
- bail out if selinux policy could not be loaded and 
  selinux=0 not specified on kernel command line 
  (bug #524113)
- set finished criteria for dmsquash live images

* Fri Sep 18 2009 Harald Hoyer <harald@redhat.com> 002-2
- do not cleanup dmraids
- copy over lvm.conf

* Thu Sep 17 2009 Harald Hoyer <harald@redhat.com> 002-1
- version 002
- set correct PATH
- workaround for broken mdmon implementation

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-12
- removed lvm/mdraid/dmraid lock files
- add missing ifname= files

* Wed Sep 16 2009 Harald Hoyer <harald@redhat.com> 001-11
- generate dracut-version during rpm build time

* Tue Sep 15 2009 Harald Hoyer <harald@redhat.com> 001-10
- add ifname= argument for persistent netdev names
- new /initqueue-finished to check if the main loop can be left
- copy mdadm.conf if --mdadmconf set or mdadmconf in dracut.conf

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-9
- added Requires: plymouth-scripts

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-8
- plymouth: use plymouth-populate-initrd
- add add_drivers for dracut and dracut.conf
- do not mount /proc and /selinux manually in selinux-load-policy

* Wed Sep 09 2009 Harald Hoyer <harald@redhat.com> 001-7
- add scsi_wait_scan to be sure everything was scanned

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-6
- fixed several problems with md raid containers
- fixed selinux policy loading

* Tue Sep 08 2009 Harald Hoyer <harald@redhat.com> 001-5
- patch does not honor file modes, fixed them manually

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-4
- fixed mdraid for IMSM

* Mon Sep 07 2009 Harald Hoyer <harald@redhat.com> 001-3
- fixed bug, which prevents installing 61-persistent-storage.rules (bug #520109)

* Thu Sep 03 2009 Harald Hoyer <harald@redhat.com> 001-2
- fixed missing grep for md
- reorder cleanup

* Wed Sep 02 2009 Harald Hoyer <harald@redhat.com> 001-1
- version 001
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Aug 14 2009 Harald Hoyer <harald@redhat.com> 0.9-1
- version 0.9

* Thu Aug 06 2009 Harald Hoyer <harald@redhat.com> 0.8-1
- version 0.8 
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 24 2009 Harald Hoyer <harald@redhat.com> 0.7-1
- version 0.7
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 22 2009 Harald Hoyer <harald@redhat.com> 0.6-1
- version 0.6
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Fri Jul 17 2009 Harald Hoyer <harald@redhat.com> 0.5-1
- version 0.5
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Sat Jul 04 2009 Harald Hoyer <harald@redhat.com> 0.4-1
- version 0.4
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Thu Jul 02 2009 Harald Hoyer <harald@redhat.com> 0.3-1
- version 0.3
- see http://dracut.git.sourceforge.net/git/gitweb.cgi?p=dracut/dracut;a=blob_plain;f=NEWS

* Wed Jul 01 2009 Harald Hoyer <harald@redhat.com> 0.2-1
- version 0.2

* Fri Jun 19 2009 Harald Hoyer <harald@redhat.com> 0.1-1
- first release

* Thu Dec 18 2008 Jeremy Katz <katzj@redhat.com> - 0.0-1
- Initial build
