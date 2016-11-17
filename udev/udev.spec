%define debug true
%define udev_scriptdir /lib/udev
%define firmwaredir /lib/firmware

Summary: A userspace implementation of devfs
Name: udev
Version: 147
Release: 2.73%{?dist}.2
License: GPLv2
Group: System Environment/Base
Provides: udev-persistent = %{version}-%{release}
Obsoletes: udev-persistent < 0:030-5
Obsoletes: udev-extras < 20090618
Provides: udev-extras = 20090618-1
Source: ftp://ftp.kernel.org/pub/linux/utils/kernel/hotplug/%{name}-%{version}.tar.bz2

Patch1: 0001-cdrom_id-Still-check-profiles-even-if-there-is-no-me.patch
Patch2: 0002-cdrom_id-remove-deprecated-device-matches.patch
Patch3: 0003-cdrom_id-open-non-mounted-optical-media-with-O_EXCL.patch
Patch4: 0004-cdrom_id-remove-debugging-code.patch
Patch5: 0005-cdrom_id-retry-to-open-the-device-if-EBUSY.patch
Patch6: 0006-cdrom_id-check-mount-state-in-retry-loop.patch
Patch7: 0007-cdrom_id-always-set-ID_CDROM-regardless-if-we-can-ru.patch
Patch8: 0008-replace-add-change-with-remove.patch
Patch9: 0009-cdrom_id-Fix-uninitialized-variables.patch
Patch10: 0010-cdrom_id-Fix-uninitialized-buffers.patch

Patch20: udev-147-cdrom_id-20110209.patch
Patch21: udev-147-idrac.patch

Patch101:  udev-141-cpu-online.patch
Patch102:  udev-147-modem-modeswitch.patch
Patch103:  udev-147-wwn.patch
Patch104:  udev-147-virtio.patch
Patch105:  udev-147-layer3.patch
Patch107:  udev-147-Decrease-buffer-size-when-advancing-past-NUL-byte.patch
Patch108:  udev-147-Use-UTIL_LINE_SIZE-not-UTIL_PATH_SIZE-to-truncate-pr.patch
Patch109:  udev-147-Increase-UTIL_LINE_SIZE-from-2048-to-16384.patch
Patch111:  udev-147-selinux-preserve.patch
Patch112:  udev-147-xvd_cdrom.patch
Patch114:  udev-147-virtual.patch
Patch115:  udev-147-modprobe-hack.patch
Patch118:  udev-147-no-usb_id-err.patch
Patch119:  udev-147-virtio-blk-patch_id.patch
Patch120:  udev-147-changer-symlink.patch
Patch121:  udev-147-virtio-blk-by-id.patch
Patch123:  udev-147-rule_gen.patch
Patch124:  udev-147-rule_gen2.patch
Patch125:  udev-147-scsi-id-2.patch

Patch200: udev.git-5539f624.patch
Patch201: udev.git-c4f6dcc4a5c774c4c5c60c7024d59081deecc7f8.patch
Patch202: udev.git-484e1b2d11b9b89418589d885a625e647881933b.patch
Patch203: udev.git-847b4f84c671e98f29f22d8e3e0d70a231d71a7b.patch
Patch204: udev.git-0c7377880974e6eadac7a3ae9e35d339546dde0d.patch
Patch205: udev-147-cdrom-virt.patch
Patch206: udev-147-scsi_id-raw.patch
Patch207: udev.git-1d67ec16c44711bbfb50ac7dd8bb2fb6e64a80f3.patch
Patch208: udev.git-d5a01cb8b31bd0791d1617c56d4c669a02018bd7.patch

Patch210: udev-shproperty.patch

# keyboard related patches
Patch300: 0300-README.keymap.txt-small-clarification.patch
Patch308: 0308-keymap-Add-Acer-Aspire-1810T.patch
Patch309: 0309-keymap-add-Samsung-N130.patch
Patch310: 0310-95-keymap.rules-Run-on-change-events-too.patch
Patch311: 0311-keymap-handle-atkbd-force_release-quirk.patch
Patch312: 0312-keymap-fix-findkeyboards.patch
Patch316: 0316-add-Samsung-R70-R71-keymap.patch
Patch317: 0317-keymap-Add-hotkey-quirk-for-Acer-Aspire-One-AO531h-A.patch
Patch318: 0318-keymap-Add-Logitech-S510-USB-keyboard.patch
Patch320: 0320-keymap-add-Acer-TravelMate-8471.patch
Patch321: 0321-keymap-Add-Acer-Aspire-1810TZ.patch
Patch322: 0322-keymap-Add-OLPC-XO-key-mappings.patch
Patch323: 0323-keymap-Fix-typo-in-compal-rules.patch
Patch324: 0324-keymap-Add-LG-X110.patch
Patch325: 0325-keymap-Lenovo-Thinkpad-USB-Keyboard-with-Tracepoint.patch
Patch326: 0326-keymap-Add-Fujitsu-Amilo-Li-1718.patch
Patch327: 0327-keymap-Document-force-release.patch
Patch328: 0328-keymap-Samsung-R70-R71-force-release-quirk.patch
Patch329: 0329-build-keymap-create-subdir.patch
Patch331: 0331-keymap-support-for-the-Samsung-N140-keyboard.patch
Patch332: 0332-keymap-move-force-release-directory.patch
Patch333: 0333-extras-keymap-check-keymaps.sh-Ignore-comment-only-l.patch
Patch334: 0334-keymap-Fix-invalid-map-line.patch
Patch335: 0335-keymap-include-linux-limits.h.patch
Patch336: 0336-keymap-linux-input.h-get-absolute-include-path-from-.patch
Patch338: 0338-keymap-Add-Dell-Inspiron-1011-Mini-10.patch
Patch339: 0339-Fix-brightness-keys-on-MSI-Wind-U-100.patch
Patch340: 0340-keymap-Add-support-for-Gateway-AOA110-AOA150-clones.patch
Patch341: 0341-keymap-Fix-LG-X110.patch
Patch342: 0342-Force-key-release-for-volume-keys-on-Dell-Studio-155.patch
Patch343: 0343-keymap-Add-Toshiba-Satellite-M30X.patch
Patch345: 0345-keymap-Add-Samsung-Q210-P210-force-release-quirk.patch
Patch346: 0346-keymap-Add-Fujitsu-Amilo-1848-u-force-release-quirk.patch
Patch349: 0349-keymap-Add-Acer-TravelMate-6593G-and-Acer-Aspire-164.patch
Patch350: 0350-keymap-Fix-another-key-for-Acer-TravelMate-6593.patch
Patch351: 0351-Fix-Keymapping-for-upcoming-Dell-Laptops.patch
Patch352: 0352-Add-new-Dell-touchpad-keycode.patch
Patch353: 0353-Revert-special-casing-0xD8-to-latitude-XT-only.patch
Patch354: 0354-Fix-Dell-Studio-1558-volume-keys-not-releasing.patch
Patch355: 0355-Add-support-for-another-Dell-touchpad-toggle-key.patch
Patch357: 0357-keymap-Unite-laptop-models-needing-common-volume-key.patch
Patch358: 0358-keymap-Add-force-release-quirk-for-Coolbox-QBook-270.patch
Patch359: 0359-keymap-Add-force-release-quirk-for-Mitac-8050QDA.patch
Patch361: 0361-Fix-volume-keys-not-releasing-for-Pegatron-platform.patch
Patch363: 0363-keymap-Fix-Bluetooth-key-on-Acer-TravelMate-4720.patch
Patch365: 0365-keymap-Add-keymap-and-force-release-quirk-for-Samsun.patch
Patch366: 0366-keymap-Add-keymap-quirk-of-WebCam-key-for-MSI-netboo.patch
Patch372: 0372-Fix-wlan-key-on-Inspirion-1210.patch
Patch375: 0375-Fix-wlan-key-on-Inspiron-910.patch
Patch376: 0376-Fix-wlan-key-on-Inspiron-1010-1110.patch
Patch380: 0380-extras-keymap-add-Samsung-N210-to-keymap-rules.patch
Patch385: 0385-Fix-stuck-volume-key-presses-for-Toshiba-Satellite-U.patch
Patch387: 0387-keymap-Add-support-for-IBM-branded-USB-devices.patch
Patch388: 0388-keymap-Add-Logitech-Cordless-Wave-Pro.patch
Patch389: 0389-keymap-Find-alternate-Lenovo-module.patch
Patch390: 0390-keymap-Add-Lenovo-ThinkPad-SL-Series-extra-buttons.patch
Patch391: 0391-Fix-volume-keys-not-releasing-on-Mivvy-G310.patch
Patch393: 0393-keymap-Generalize-Samsung-keymaps.patch
Patch394: 0394-keymap-Add-force-release-quirks-for-a-lot-more-Samsu.patch
Patch396: 0396-Add-keymap-for-Lenovo-IdeaPad-S10-3.patch
Patch397: 0397-keymap-Add-Onkyo-PC.patch
Patch398: 0398-keymap-Add-HP-G60.patch
Patch399: 0399-keymap-Fix-Sony-VAIO-VGN-SZ2HP-B.patch
Patch400: 0400-keymap-Fix-Acer-TravelMate-4720.patch
Patch402: 0402-keymap-Add-Lenovo-Y550.patch
Patch404: 0404-keymap-Add-alternate-MSI-vendor-name.patch
Patch409: 0409-keymap-Apply-force-release-rules-to-all-Samsung-mode.patch
Patch410: 0410-keymap-Add-Toshiba-Satellite-U500.patch
Patch412: 0412-keymap-Add-Sony-Vaio-VGN71.patch
Patch413: 0413-keymap-Add-some-more-Sony-Vaio-VGN-models.patch
Patch414: 0414-keymap-Add-force-release-for-HP-touchpad-off.patch
Patch415: 0415-extras-keymap-Make-touchpad-buttons-consistent.patch
Patch416: 0416-keymap-Add-release-quirks-for-two-Zepto-Znote-models.patch
Patch417: 0417-keymap-Fix-struck-Touchpad-key-on-Dell-Latitude-E-se.patch
Patch418: 0418-keymap-Fix-struck-Touchpad-key-on-Dell-Precision-M-s.patch

Patch500: udev.git-5c3ebbf35a2c101e0212c7066f0d65e457fcf40c.patch
Patch501: udev.git-c54b43e2c233e724f840c4f6a0a81bdd549e40bb.patch
Patch502: udev-147-modeswitch.patch
Patch504: udev-147-iosched.patch
Patch505: udev.git-e48e2912023b5600d291904b0f7b0017387e8cb2.patch
Patch506: udev.git-135f3e8d0b4b4968908421b677c9ef2ba860b71d.patch
Patch507: udev.git-00f34bc435f51decab266f2e9a7be223df15c87e.patch
Patch508: udev.git-851dd4ddc5aeb1ee517145d9e3334c2017595321.patch

Patch600: add-xvd-detection-to-storage-rules.patch
Patch601: udev-kname.patch
Patch602: udev-nowatch-man.patch
Patch603: udev-147-path_id-cciss.patch
Patch604: udev-147-docenc.patch
Patch605: udev-147-cdrom_id-profiles.patch
Patch606: udev-147-rename-symlink-info.patch
Patch607: udev-147-max-childs.patch
Patch608: udev-147-2.43-path_id_add_scm_support.patch
Patch609: udev-147-cplusplus.patch
Patch610: udev-147-ebusy-loop-std-inquiry.patch
Patch611: udev-147-add-OPTION-log_priority-info-OPTION-log_priority-err.patch
Patch612: udev-147-udev-lock-include-missing-header.patch
Patch613: udev-147-udev-event.c-remove-unused-var.patch
Patch614: udev-147-cdrom_id-remove-unused-var-and-option.patch
Patch615: udev-147-udevd-fix-max_childs.patch
Patch616: udev-147-udevd.c-reset-log_priority-for-new-events.patch
Patch617: udev-147-removed-max-childs-message-output-devpath-and-seq-nu.patch
Patch618: udev-147-udevd-add-s-option-to-output-to-stdout-and-stderr.patch
Patch619: udev-147-syslog-to-stderr-also.patch
Patch620: udev-147-enum-realloc.patch
Patch621: udev-147-usb-id-let-QIC-157-bInterfaceSubClass-5-be-of-ID_TYP.patch
Patch622: udev-147-scsi_id-short-man.patch
Patch623: udev-147-persistent-storage-pciessd.patch
Patch624: udev-147-short-blacklist.patch
Patch625: udev-147-persistent-storage-nvme.patch
Patch626: udev-147-init-firmware.patch
Patch627: udev-147-more-workers.patch
Patch628: udev-147-idrac-rules.patch
Patch629: udev-147-modprobe-b.patch
Patch630: udev-147-modem-12d1-modeswitch.patch
Patch631: udev-147-DRIVER-modprobe.patch
Patch632: sas_path_id.patch
Patch633: udev-147-properly-handle-symlink-removal-by-change-event.patch
Patch634: udev-147-ata_id-fixup-all-8-not-only-6-bytes-of-the-fw_rev-st.patch
Patch635: udev-147-use-ata_id-for-USB-DVD-CD.patch
Patch636: udev-147-ata-id-no-blank.patch
Patch637: udev-147-workerlock-inc.patch
Patch638: 0001-scsi_id-fix-memory-leak.patch
Patch639: 0002-scsi_id-fix-file-descriptor-leak.patch
Patch640: 0003-ata_id-Support-SG_IO-version-4-interface.patch
Patch641: 0004-Run-scsi_id-and-ata_id-on-the-scsi_device-object.patch
Patch642: 0005-Use-ata_id-not-scsi_id-on-ATAPI-devices.patch
Patch643: 0006-udev-support-custom-SELinux-labels-for-device-nodes.patch
Patch644: 0007-rule_generator-prevent-creating-duplicate-entries.patch
Patch645: 0008-Fix-rule-pattern-match.patch
Patch646: 0009-Fix-possible-use-of-uninitialized-variable.patch
Patch647: 0010-udev-fibre-channel-add-support-to-NPIV-FC-virtual-in.patch
Patch648: 0011-rules-revert-bsg-use-until-the-event-ordering-proble.patch
Patch649: 0012-rules-run-ata_id-only-on-SPC-3-or-later-optical-driv.patch
Patch650: 0013-Revert-udev-fibre-channel-add-support-to-NPIV-FC-vir.patch
Patch651: 0014-udev-path-id-fibre-channel-NPIV-use-fc_vport-s-port_.patch
Patch652: 0015-core-silently-ignore-error-if-sys-class-firmware-tim.patch

Patch700: udev-nousbutils.patch

# TODO: remove patch, when binutils is fixed
# https://bugzilla.redhat.com/show_bug.cgi?id=825736
Patch9999: udev-dummy.patch

Source1: start_udev
Source3: udev-post.init
Source4: fw_unit_symlinks.sh
Source5: udev.sysconfig
Source6: 42-qemu-usb.rules
Source7: 60-alias-kmsg.rules
Source8: 01-log-block.rules

ExclusiveOS: Linux
URL: http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(pre): /bin/sh fileutils /sbin/chkconfig /sbin/service
Requires(pre): /usr/bin/stat /sbin/pidof
Requires(pre): MAKEDEV >= 0:3.11 /usr/bin/getent /usr/sbin/groupadd
Requires: hwdata

%ifarch s390 s390x
# Require s390utils-base, because it's essential on s390
Requires: s390utils-base
%endif

BuildRequires: sed libselinux-devel >= 0:1.17.9-2 flex libsepol-devel
BuildRequires: glib2-devel bison findutils MAKEDEV
BuildRequires: gperf libtool
BuildRequires: libusb-devel libacl-devel
BuildRequires: libxslt
BuildRequires: hwdata
BuildRequires: gtk-doc
%ifnarch s390 s390x
BuildRequires: usbutils >= 0.82
%else
BuildRequires: autoconf
%endif
BuildRequires: libtool >= 2.2.6
Requires: libselinux >= 0:1.17.9-2 sed
Conflicts: kernel < 0:2.6 mkinitrd <= 0:4.1.11-1 initscripts < 7.84
Requires: util-linux-ng >= 2.15.1
Obsoletes: dev <= 0:3.12-1
Provides: dev = 0:3.12-2
Obsoletes: DeviceKit < 004
Obsoletes: DeviceKit-devel < 004
Provides: DeviceKit = 004 DeviceKit-devel = 004
# hid2hci moved to udev
Conflicts: bluez < 4.47

%description
The udev package contains an implementation of devfs in 
userspace using sysfs and netlink.

%package -n libudev
Summary: Dynamic library to access udev device information
Group: System Environment/Libraries
Obsoletes: libudev0 <= 142
Provides: libudev0 = 143
License: LGPLv2+

%description -n libudev
This package contains the dynamic library libudev, which provides access
to udev device information, and an interface to search devices in sysfs.

%package -n libudev-devel
Summary: Development files for libudev
Group: Development/Libraries
Requires: udev = %{version}-%{release}
Requires: libudev = %{version}-%{release}
License: LGPLv2+

%description -n libudev-devel
This package contains the development files for the library libudev, a
dynamic library, which provides access to udev device information.

%package -n libgudev1
Summary: Libraries for adding libudev support to applications that use glib
Group: Development/Libraries
Requires: libudev >= 142
# remove the following lines for libgudev so major 1 
Provides: libgudev = 20090518
Obsoletes: libgudev <= 20090517
License: LGPLv2+
Requires: libudev = %{version}-%{release}

%description -n libgudev1
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n libgudev1-devel
Summary: Header files for adding libudev support to applications that use glib
Group: Development/Libraries
Requires: libudev-devel >= 142
Provides: libgudev-devel = 20090518
Obsoletes: libgudev-devel <= 20090517
License: LGPLv2+

Requires: libgudev1 = %{version}-%{release}

%description -n libgudev1-devel
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%prep 
%setup -q  

%patch1 -p1 -b .git1
%patch2 -p1 -b .git2
%patch3 -p1 -b .git3
%patch4 -p1 -b .git4
%patch5 -p1 -b .git5
%patch6 -p1 -b .git6
%patch7 -p1 -b .git7
%patch8 -p1 -b .git8
%patch9 -p1 -b .git9
%patch10 -p1 -b .git10

%patch20 -p1 -b .cd2011
%patch21 -p1 -b .idrac

%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch111 -p1
%patch112 -p1
%patch114 -p1
%patch115 -p1
%patch118 -p1 
%patch119 -p1 
%patch120 -p1 
%patch121 -p1 

%patch200 -p1 
%patch201 -p1 
%patch202 -p1 
%patch203 -p1 
%patch204 -p1 
%patch205 -p1  -b .virt
%patch206 -p1  -b .raw
%patch207 -p1
%patch208 -p1

%patch210 -p1 -b .shprop
%patch123 -p1  -b .rg
%patch124 -p1  -b .rg2

%patch300 -p1 -b .git300
%patch308 -p1 -b .git308
%patch309 -p1 -b .git309
%patch310 -p1 -b .git310
%patch311 -p1 -b .git311
%patch312 -p1 -b .git312
%patch316 -p1 -b .git316
%patch317 -p1 -b .git317
%patch318 -p1 -b .git318
%patch320 -p1 -b .git320
%patch321 -p1 -b .git321
%patch322 -p1 -b .git322
%patch323 -p1 -b .git323
%patch324 -p1 -b .git324
%patch325 -p1 -b .git325
%patch326 -p1 -b .git326
%patch327 -p1 -b .git327
%patch328 -p1 -b .git328
%patch329 -p1 -b .git329
%patch331 -p1 -b .git331
%patch332 -p1 -b .git332
%patch333 -p1 -b .git333
%patch334 -p1 -b .git334
%patch335 -p1 -b .git335
%patch336 -p1 -b .git336
%patch338 -p1 -b .git338
%patch339 -p1 -b .git339
%patch340 -p1 -b .git340
%patch341 -p1 -b .git341
%patch342 -p1 -b .git342
%patch343 -p1 -b .git343
%patch345 -p1 -b .git345
%patch346 -p1 -b .git346
%patch349 -p1 -b .git349
%patch350 -p1 -b .git350
%patch351 -p1 -b .git351
%patch352 -p1 -b .git352
%patch353 -p1 -b .git353
%patch354 -p1 -b .git354
%patch355 -p1 -b .git355
%patch357 -p1 -b .git357
%patch358 -p1 -b .git358
%patch359 -p1 -b .git359
%patch361 -p1 -b .git361
%patch363 -p1 -b .git363
%patch365 -p1 -b .git365
%patch366 -p1 -b .git366
%patch372 -p1 -b .git372
%patch375 -p1 -b .git375
%patch376 -p1 -b .git376
%patch380 -p1 -b .git380
%patch385 -p1 -b .git385
%patch387 -p1 -b .git387
%patch388 -p1 -b .git388
%patch389 -p1 -b .git389
%patch390 -p1 -b .git390
%patch391 -p1 -b .git391
%patch393 -p1 -b .git393
%patch394 -p1 -b .git394
%patch396 -p1 -b .git396
%patch397 -p1 -b .git397
%patch398 -p1 -b .git398
%patch399 -p1 -b .git399
%patch400 -p1 -b .git400
%patch402 -p1 -b .git402
%patch404 -p1 -b .git404
%patch409 -p1 -b .git409
%patch410 -p1 -b .git410
%patch412 -p1 -b .git412
%patch413 -p1 -b .git413
%patch414 -p1 -b .git414
%patch415 -p1 -b .git415
%patch416 -p1 -b .git416
%patch417 -p1 -b .git417
%patch418 -p1 -b .git418


%patch125 -p1  -b .id2

%patch500 -p1  -b .git500
%patch501 -p1  -b .git501
%patch502 -p1  -b .git502
%patch504 -p1  -b .git504
%patch505 -p1  -b .git505
%patch506 -p1  -b .git506
%patch507 -p1  -b .git507
%patch508 -p1  -b .git508

%patch600 -p1  -b .xen
%patch601 -p1  -b .kname
%patch602 -p1  -b .nowatchman
%patch603 -p1  -b .cciss
%patch604 -p1  -b .docenc
%patch605 -p1  -b .profiles
%patch606 -p1  -b .errinfo
%patch607 -p1  -b .maxchilds
%patch608 -p1  -b .scm
%patch609 -p1  -b .cplusplus
%patch610 -p1  -b .ebusy
%patch611 -p1
%patch612 -p1
%patch613 -p1
%patch614 -p1
%patch615 -p1
%patch616 -p1
%patch617 -p1
%patch618 -p1
%patch619 -p1
%patch620 -p1 -b .realloc
%patch621 -p1
%patch622 -p1 -b .shortman
%patch623 -p1 -b .pciessd
%patch624 -p1 -b .shortblack
%patch625 -p1 -b .nvme
%patch626 -p1
%patch627 -p1 -b .workerlock
%patch628 -p1 -b .idracrules
%patch629 -p1 -b .modb
%patch630 -p1 -b .1103278
%patch631 -p1 -b .modprobedriver
%patch632 -p1 -b .sas_path_id
%patch633 -p1
%patch634 -p1
%patch635 -p1
%patch636 -p1
%patch637 -p1 -b .workerlock2

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

%ifarch s390 s390x
%patch700 -p1 -b .nousbutils
%endif

# TODO: remove patch, when binutils is fixed
# https://bugzilla.redhat.com/show_bug.cgi?id=825736
%patch9999 -p1  -b .dummy

%build
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fPIE -DPIE"
export LDFLAGS="$LDFLAGS $RPM_OPT_FLAGS -pie -Wl,-z,relro -Wl,-z,now"
# get rid of rpath
libtoolize -f -c

%ifarch s390 s390x
autoconf
%endif

%configure --with-selinux  --prefix=%{_prefix} --exec-prefix="" \
	   --sysconfdir=%{_sysconfdir} \
	   --sbindir="/sbin" --libexecdir=%{udev_scriptdir} \
	   --with-rootlibdir=/%{_lib} --disable-introspection \
	   --disable-debug

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sbindir}

make install DESTDIR=$RPM_BUILD_ROOT

rm -fr $RPM_BUILD_ROOT%{_docdir}/udev
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

# Deprecated, but keep the ownership
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/{rules.d,makedev.d,scripts,devices}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dev.d
mkdir -p $RPM_BUILD_ROOT%{_bindir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/scsi_id.config

# force relative symlinks
ln -sf ..%{udev_scriptdir}/scsi_id $RPM_BUILD_ROOT/sbin/scsi_id

for i in \
	rules/redhat/40-redhat.rules \
	rules/redhat/61-sas-storage.rules \
%ifarch ia64
	rules/packages/40-ia64.rules \
%endif
%ifarch ppc ppc64
	rules/packages/40-ppc.rules \
%endif
%ifarch s390 s390x
	rules/packages/40-s390.rules \
%endif
	rules/packages/40-isdn.rules \
	rules/packages/64-md-raid.rules \
	rules/packages/64-device-mapper.rules \
	rules/packages/73-idrac.rules \
	%{SOURCE6} \
	%{SOURCE7} \
	%{SOURCE8} \
	; do
	install -m 0644 "$i"  "$RPM_BUILD_ROOT%{udev_scriptdir}/rules.d/${i##*/}"
done
	
mkdir -p $RPM_BUILD_ROOT%{udev_scriptdir}/{,devices}

install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{udev_scriptdir}/fw_unit_symlinks.sh

mkdir -p $RPM_BUILD_ROOT%{_datadir}/udev
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/sbin/start_udev

mkdir -p -m 0755 $RPM_BUILD_ROOT%{firmwaredir}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/udev-post

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/udev

mkdir -p $RPM_BUILD_ROOT/var/lib/udev/makedev.d

%preun
if [ "$1" -eq 0 -a -f %{_initrddir}/udev ]; then
	if [ -x /sbin/pidof ]; then
		pid=$(/sbin/pidof -c udevd)
		if [ -n "$pid" ]; then
			kill $pid >/dev/null 2>&1 || :
		fi
	fi
	/sbin/chkconfig --del udev
fi
if [ "$1" -eq 0 ]; then
	/sbin/chkconfig --del udev-post
fi
exit 0

%pre
# to be removed after F10 EOL (and for RHEL-6)
getent group video >/dev/null || /usr/sbin/groupadd -g 39 video || :
getent group audio >/dev/null || /usr/sbin/groupadd -g 63 audio || :
# to be kept
getent group cdrom >/dev/null || /usr/sbin/groupadd -g 11 cdrom || :
getent group tape >/dev/null || /usr/sbin/groupadd -g 33 tape || :
getent group dialout >/dev/null || /usr/sbin/groupadd -g 18 dialout || :

# kill daemon if we are not in a chroot
if test -f /proc/1/exe -a -d /proc/1/root; then
	if test -x /usr/bin/stat -a "$(/usr/bin/stat -Lc '%%D-%%i' /)" = "$(/usr/bin/stat -Lc '%%D-%%i' /proc/1/root)"; then
		if test -x /sbin/udevd -a -x /sbin/pidof ; then
			/sbin/udevadm control --stop-exec-queue
			pid=$(/sbin/pidof -c udevd)
			while [ -n "$pid" ]; do
				for p in $pid; do
					kill $hard $p >/dev/null 2>&1 || :
				done
				pid=$(/sbin/pidof -c udevd)
				hard="-9"
			done
		fi
	fi
fi
exit 0

%post
# start daemon if we are not in a chroot
if test -f /proc/1/exe -a -d /proc/1/root; then
	if test "$(/usr/bin/stat -Lc '%%D-%%i' /)" = "$(/usr/bin/stat -Lc '%%D-%%i' /proc/1/root)"; then
		/sbin/udevd -d
		/sbin/udevadm control --start-exec-queue
	fi
fi
/sbin/chkconfig --add udev-post

exit 0

%triggerin -- selinux-policy
rm -f /var/lib/udev/makenode.d/*  >/dev/null 2>&1 || :

%triggerin -- MAKEDEV
rm -f /var/lib/udev/makenode.d/*  >/dev/null 2>&1 || :

%post -n libudev -p /sbin/ldconfig
%postun -n libudev -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc NEWS COPYING README TODO ChangeLog docs/* extras/keymap/README.keymap.txt
%attr(0755,root,root) /sbin/udevadm
%attr(0755,root,root) /sbin/udevd
%attr(0755,root,root) /sbin/start_udev
%attr(0755,root,root) /sbin/scsi_id
%attr(0755,root,root) %{udev_scriptdir}/scsi_id
%attr(0755,root,root) %{udev_scriptdir}/ata_id
%attr(0755,root,root) %{udev_scriptdir}/edd_id
%attr(0755,root,root) %{udev_scriptdir}/usb_id
%attr(0755,root,root) %{udev_scriptdir}/cdrom_id
%attr(0755,root,root) %{udev_scriptdir}/path_id
%attr(0755,root,root) %{udev_scriptdir}/sas_path_id
%attr(0755,root,root) %{udev_scriptdir}/hid2hci
%attr(0755,root,root) %{udev_scriptdir}/create_floppy_devices
%attr(0755,root,root) %{udev_scriptdir}/fw_unit_symlinks.sh
%attr(0755,root,root) %{udev_scriptdir}/firmware.sh
%attr(0644,root,root) %{udev_scriptdir}/rule_generator.functions
%attr(0755,root,root) %{udev_scriptdir}/write_cd_rules
%attr(0755,root,root) %{udev_scriptdir}/write_net_rules
%attr(0755,root,root) %{udev_scriptdir}/collect
%attr(0755,root,root) %{udev_scriptdir}/fstab_import
%attr(0755,root,root) %{udev_scriptdir}/keyboard-force-release.sh

%attr(0755,root,root) %dir %{udev_scriptdir}/rules.d/
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/udev-post
%attr(0755,root,root) %dir %{_sysconfdir}/udev/
%attr(0755,root,root) %dir %{_sysconfdir}/udev/rules.d/
%attr(0755,root,root) %dir %{udev_scriptdir}/
%attr(0755,root,root) %dir %{udev_scriptdir}/devices/
%attr(0755,root,root) %dir %{_sysconfdir}/udev/makedev.d/

%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/sysconfig/udev

%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/udev/udev.conf
%attr(0644,root,root) %{udev_scriptdir}/rules.d/*.rules

%ghost %config(noreplace,missingok) %attr(0644,root,root) %{_sysconfdir}/scsi_id.config

%dir %attr(0755,root,root) %{firmwaredir}
%attr(0644,root,root) %{_mandir}/man8/udev*.8*
%attr(0644,root,root) %{_mandir}/man7/udev*.7*
%attr(0644,root,root) %{_mandir}/man8/scsi_id*.8*

%dir %attr(0755,root,root) /var/lib/udev
%dir %attr(0755,root,root) /var/lib/udev/makedev.d

# Deprecated, but keep the ownership
%ghost %dir %{_sysconfdir}/udev/scripts/
%ghost %dir %{_sysconfdir}/udev/devices/
%ghost %dir %{_sysconfdir}/dev.d/

%attr(0755,root,root) %{udev_scriptdir}/modem-modeswitch
%attr(0755,root,root) %{udev_scriptdir}/pci-db
%attr(0755,root,root) %{udev_scriptdir}/usb-db
%attr(0755,root,root) %{udev_scriptdir}/keymap
%attr(0755,root,root) %{udev_scriptdir}/udev-acl
%attr(0755,root,root) %{udev_scriptdir}/v4l_id
%attr(0755,root,root) %{udev_scriptdir}/findkeyboards
%attr(0755,root,root) %{udev_scriptdir}/mpath-iosched.sh
%dir %attr(0755,root,root) %{udev_scriptdir}/keymaps
%attr(0644,root,root) %{udev_scriptdir}/keymaps/*
%dir %attr(0755,root,root) %{udev_scriptdir}/keymaps/force-release
%attr(0644,root,root) %{udev_scriptdir}/keymaps/force-release/*
%attr(0644,root,root) %{_prefix}/lib/ConsoleKit/run-seat.d/udev-acl.ck


%files -n libudev
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) /%{_lib}/libudev.so.*

%files -n libudev-devel
%defattr(0644, root, root, 0755)
%doc COPYING
%{_includedir}/libudev.h
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libudev.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/gtk-doc/html/libudev/*

%files -n libgudev1
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) %{_libdir}/libgudev-1.0.so.*

%files -n libgudev1-devel
%defattr(0644, root, root, 0755)
%doc COPYING
%attr(0755,root,root) %{_libdir}/libgudev-1.0.so
%attr(0644,root,root) %{_includedir}/gudev-1.0/gudev/*.h
%dir %attr(0755,root,root) %{_includedir}/gudev-1.0
%dir %attr(0755,root,root) %{_includedir}/gudev-1.0/gudev
%dir %{_datadir}/gtk-doc/html/gudev
%attr(0644,root,root) %{_datadir}/gtk-doc/html/gudev/*
%attr(0644,root,root) %{_libdir}/pkgconfig/gudev-1.0*

%changelog
* Tue Aug 30 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.73.2
- revert of the last patch (#1371457)

* Sun Jul 31 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.73.1
- apply permissions only on add events or when new device node is created (#1362038)

* Fri Apr 08 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.73
- ignore missing /sys/class/firmware/timeout (#1323883)

* Mon Feb 29 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.72
- merge different patch for support of NPIV FC virtual interfaces (#1032218)

* Tue Feb 09 2016 Michal Sekletar <msekleta@redhat.com> - 147.2.71
- fix bug when by-id symlinks for scsi block devices were missing "scsi" prefix (#1301039)

* Mon Feb 01 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.70
- add support to NPIV FC virtual interfaces (#1032218)

* Thu Jan 28 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.69
- actually apply previously added patch (#891669)

* Thu Jan 28 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.68
- fix possible use of uninitialized variable in scsi_id (#891669)

* Wed Jan 27 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.67
- fix existing rule matching in write_net_rules (#652499)

* Mon Jan 18 2016 Michal Sekletar <msekleta@redhat.com> - 147-2.66
- prevent creation of duplicate udev rules by write_net_rules helper (#652499)
- fix memory leak in scsi_id (#891669)
- introduce SECLABEL{selinux} for setting explicit SELinux labels on device nodes (#1015300)
- for ATA disks udev will now also create by-id/wwn-* symlinks when appropriate (#1220617)

* Tue Oct 06 2015 Harald Hoyer <harald@redhat.com> 147-2.65
- 80-drivers.rules: only make an exception for ipmi for
                    modprobe with DRIVER set
Resolves: rhbz#1268251

* Thu Oct 01 2015 Harald Hoyer <harald@redhat.com> 147-2.64
- also limit the additional modprobe locked workers
Resolves: rhbz#1170313

* Mon Jun 08 2015 Harald Hoyer <harald@redhat.com> 147-2.63
- do not erase disks with ATA commands
Resolves: rhbz#1228455

* Thu Apr 23 2015 Harald Hoyer <harald@redhat.com> 147-2.62
- add one more rule for scsi devices to use ata_id
Resolves: rhbz#1130438

* Mon Mar 02 2015 Harald Hoyer <harald@redhat.com> 147-2.61
- use ata_id for USB DVD/CD
Resolves: rhbz#1130438

* Mon Mar 02 2015 Harald Hoyer <harald@redhat.com> 147-2.60
- ata_id - fixup all 8 not only 6 bytes of the fw_rev string
Resolves: rhbz#794561
- udev: properly handle symlink removal by 'change' event
Resolves: rhbz#1018171

* Fri Feb 27 2015 Harald Hoyer <harald@redhat.com> 147-2.59
- add sas_path_id
Resolves: rhbz#907687

* Fri Feb 27 2015 Harald Hoyer <harald@redhat.com> 147-2.58
- do not print error, if /sys/class/firmware/timeout does
  not exist (yet)
Resolves: rhbz#1140336
- always call modprobe, even when a driver is bound to the device
Resolves: rhbz#1084513
- fixed for every modprobe locked worker, increase max_childs
  use ncnt instead of zcnt
Resolves: rhbz#1164960
- print warning in start_udev, if udevlog is used
Resolves: rhbz#876535

* Thu Jul 24 2014 Harald Hoyer <harald@redhat.com> 147-2.57
- fixed modem modeswitch for idVendor=="12d1"
Resolves: rhbz#1103278

* Fri Jul 11 2014 Harald Hoyer <harald@redhat.com> 147-2.56
- fixed: for every modprobe locked worker, increase max_childs
Resolves: rhbz#1028174

* Wed Jun 18 2014 Harald Hoyer <harald@redhat.com> 147-2.55
- call modprobe with "-b" to honor the blacklist
Resolves: rhbz#1091790

* Tue Jun 10 2014 Harald Hoyer <harald@redhat.com> 147-2.54
- fixed modprobe locked worker, increase max_childs
Resolves: rhbz#1028174

* Fri Jun 06 2014 Harald Hoyer <harald@redhat.com> 147-2.53
- add rule for idrac interface renaming
Resolves: rhbz#1054482
- for every modprobe locked worker, increase max_childs
Resolves: rhbz#1028174
- increase firmware timeout to 600 seconds
Resolves: rhbz#1077186
- add nvme pcie ssd scsi_id ENV
Resolves: rhbz#1020856
- scsi_id: add short option "-b" parsing
Resolves: rhbz#910168
- add  by-id (hardware serial number) for Micron PCIe SSDs
Resolves: rhbz#839172
- 80-iosched.rules: check for attributes
Resolves: rhbz#1008341

* Mon Apr 28 2014 Harald Hoyer <harald@redhat.com> 147-2.52
- document short options of scsi_id
Resolves: rhbz#910168

* Thu Oct 17 2013 Harald Hoyer <harald@redhat.com> 147-2.51
- let QIC-157 / bInterfaceSubClass(5) be of ID_TYPE="generic"
Resolves: rhbz#982902

* Fri Oct 11 2013 Harald Hoyer <harald@redhat.com> 147-2.50
- fixed segfaults in udev_enumerate_get_list_entry()
Resolves: rhbz#998237

* Fri Oct 11 2013 Harald Hoyer <harald@redhat.com> 147-2.49
- fixed segfaults in udev_enumerate_get_list_entry()
Resolves: rhbz#998237

* Fri Aug 09 2013 Harald Hoyer <harald@redhat.com> 147-2.48
- readd dummy patch for binutils bug (825736)
Resolves: rhbz#920961

* Fri Jul 26 2013 Harald Hoyer <harald@redhat.com> 147-2.47
- add OPTIONS="log_priority=<loglevel>" for debugging purposes
Resolves: rhbz#947067
- limit default udevd maximum childs
Resolves: rhbz#833172 rhbz#885978
- add scm path_id support
Resolves: rhbz#888647
- header fix for C++
Resolves: rhbz#909792
- scsi_id: retry on EBUSY
Resolves: rhbz#920961

* Tue Jan 15 2013 Harald Hoyer <harald@redhat.com> 147-2.46
- make symlink/rename failure info() only
  this can happen for multipath devices
Resolves: rhbz#838451

* Wed Jan 09 2013 Harald Hoyer <harald@redhat.com> 147-2.45
- fixed man page
Resolves: rhbz#790321

* Wed Jan 09 2013 Harald Hoyer <harald@redhat.com> 147-2.44
- fixed man page
Resolves: rhbz#790321

* Thu Oct 11 2012 Harald Hoyer <harald@redhat.com> 147-2.43
- add cciss handling to path_id
Resolves: rhbz#784697
- add kmsg alias logger
Resolves: rhbz#826396
- extend udev(7) man page about character encoding in symlinks
Resolves: rhbz#790321
- fix cdrom_id to honor feature profiles, if no medium is present
Resolves: rhbz#847925

* Thu Jun 07 2012 Harald Hoyer <harald@redhat.com> 147-2.42
- add dummy patch for binutils bug (825736)
Resolves: rhbz#829188

* Thu Mar 01 2012 Harald Hoyer <harald@redhat.com> 147-2.41
- add "nowatch" option to manpage
Resolves: rhbz#628762
- fixed return code of udev-post for "status"
Resolves: rhbz#735410
- fixed udev_device_get_devnode()
  backported cdb1d7608a2e2ba708a890eeab6e5e99409a1953
Resolves: rhbz#784648

* Fri Sep 23 2011 Harald Hoyer <harald@redhat.com> 147-2.40
- corrected xvd* udev rules, 
Resolves: rhbz#740786

* Tue Sep 20 2011 Harald Hoyer <harald@redhat.com> 147-2.39
- allow /dev/xvdN devices to be probed for metadata
Resolves: rhbz#731400

* Fri Sep 09 2011 Harald Hoyer <harald@redhat.com> 147-2.38
- fixed segfault in udev_enumerate_get_list_entry()
Resolves: rhbz#696651

* Wed Aug 10 2011 Harald Hoyer <harald@redhat.com> 147-2.37
- add requires for libgudev1 on libudev with version and release
Resolves: rhbz#727500
- change import property buffer to 16384 bytes
Resolves: rhbz#726566

* Tue Aug 02 2011 Harald Hoyer <harald@redhat.com> 147-2.36
- handle Vodafone K3565-Z 3G modem
Resolves: rhbz#632646
- update path_id to upstream version, which can handle SAS devices that 
  have no enclosure and handles iSCSI devices.
Resolves: rhbz#698540 rhbz#714951
- use IFINDEX for temporary network interface renaming
Resolves: rhbz#701265
- udev now changes the IO scheduler for all disks except sata disks to the 
  "deadline" scheduler.
Resolves: rhbz#711254

* Wed Mar 30 2011 Harald Hoyer <harald@redhat.com> 147-2.35
- workaround for broken virtual CDROM's "READ TOC"
Resolves: rhbz#687956

* Wed Feb 16 2011 Harald Hoyer <harald@redhat.com> 147-2.34
- add CFLAGS and LDFLAGS to add missing PIE and RELRO flags
Resolves: rhbz#676004
- fixed udevadm trigger segmentation fault
Resolves: rhbz#677857

* Wed Feb 09 2011 Harald Hoyer <harald@redhat.com> 147-2.33
- updated cdrom_id, to handle more virtual drives
Resolves: rhbz#660367

* Thu Feb 03 2011 Harald Hoyer <harald@redhat.com> 147-2.32
- added new page codes for scsi_id, to export ID_SERIAL_80 and ID_SERIAL_83.
Resolves: rhbz#644902
- correctly handle ENV{ACL_MANAGE}==0
Resolves: rhbz#674168

* Wed Jan 26 2011 Harald Hoyer <harald@redhat.com> 147-2.31
- fixed zero macs in 70-persistent-net.rules
Resolves: rhbz#656059
- add 42-qemu-usb.rules
Resolves: rhbz#663064
- create /dev/hugepages directory
Resolves: rhbz#667750

* Thu Dec 09 2010 Harald Hoyer <harald@redhat.com> 147-2.30
- fixed udevadm segfault, if log is set to debug
Resolves: rhbz#657360
- fixed keyboard handling for extra keys, especially volume
  control
Resolves: rhbz#617572
- quote output of 'udevadm info --query=shenv' or
                  'udevadm info --query=shproperty'
Resolves: rhbz#644330

* Tue Aug 31 2010 Harald Hoyer <harald@redhat.com> 147-2.29
- set the selinux context for "add" events, regression
  the fix for rhbz#575128 caused a lot of selinux errors like
  rhbz#603729
Resolves: rhbz#575128

* Tue Aug 31 2010 Harald Hoyer <harald@redhat.com> 147-2.28
- quirk for cisco virtual cdrom was not complete, reports
  blank media, rhbz#628962
Resolves: rhbz#624707

* Tue Aug 24 2010 Harald Hoyer <harald@redhat.com> 147-2.27
- added ID_SERIAL_RAW to scsi_id export output, which is not
  whitespace stripped
Resolves: rhbz#612173

* Wed Aug 18 2010 Harald Hoyer <harald@redhat.com> 147-2.26
- more quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#624707

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.25
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.24
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Wed Aug 11 2010 Harald Hoyer <harald@redhat.com> 147-2.23
- quirk for virtual machines, which do not report correct
  CDROM information
Resolves: rhbz#613576

* Fri Jul 23 2010 Harald Hoyer <harald@redhat.com> 147-2.22
- fixed random MAC address handling 
- honor ifcfg HWADDR settings for 70-persistent-net.rules
Resolves: rhbz#596464

* Mon Jul 12 2010 Harald Hoyer <harald@redhat.com> 147-2.21
- fix tape by-path symlinks
Resolves: rhbz#612064

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 147-2.20
- add by-id for virtio-blk devices
Resolves: rhbz#601248

* Tue Jun 29 2010 Harald Hoyer <harald@redhat.com> 147-2.19
- do not blkid blank or audio CDROMs 
Resolves: rhbz#606293
- fixed scsi changer symlink
Resolves: rhbz#603051
- suppress warnings from usb_id
Resolves: rhbz#585648
- add path_id for virtio-blk devices
Resolves: rhbz#601248
- fixed reference leak in path_id sas patch
Resolves: rhbz#537185

* Fri Jun 11 2010 Harald Hoyer <harald@redhat.com> 147-2.18
- removed obsolete arguments to configure
Resolves: rhbz#601882
- add IMPORT{db} IMPORT{cmdline} and set rd_NO_MDIMSM for noiswmd kernel cmdline option
Resolves: rhbz#589775
- add port for sas in path_id 
Resolves: rhbz#537185
- add modprobe hack to serialize modprobes
Resolves: rhbz#515413
- revert path check from 147-2.16
Resolves: rhbz#591970

* Tue Jun 08 2010 Harald Hoyer <harald@redhat.com> 147-2.17
- get path_id for virtual disks also
- Resolves: rhbz#601248

* Wed Jun 02 2010 Phil Knirsch <pknirsch@redhat.com> 147-2.16
- Added path checks for mdadm and blkid binaries in 64-md-raid.rules rules
- Resolves: rhbz#591970

* Mon Apr 26 2010 Harald Hoyer <harald@redhat.com> 147-2.15
- fix "do not mark xvd* devices as cdrom by default (rhbz#584163)"
  included patch but did not apply
- Resolves: rhbz#584163

* Thu Apr 22 2010 Harald Hoyer <harald@redhat.com> 147-2.14
- do not mark xvd* devices as cdrom by default (rhbz#584163)
- Do not rename network interfaces.
  This causes more problems, than solving the original one.
  (rhbz#565724)
- Resolves: rhbz#584163, rhbz#572681

* Thu Apr 15 2010 Harald Hoyer <harald@redhat.com> 147-2.13
- supress error message in pre/post while killing old udevd
  (rhbz#576819)
- fixed a lot of cdrom related problems (rhbz#582557, rhbz#582559)
- Resolves: rhbz#576819, rhbz#582557, rhbz#582559

* Fri Mar 19 2010 Harald Hoyer <harald@redhat.com> 147-2.12
- fixed virtio-ports rule patch (rhbz#569699)
- removed IFINDEX from renamed interfaces (rhbz#572681)
- do not reset selinux labels (rhbz#575128)
- Resolves: rhbz#572681, rhbz#569699, rhbz#575128

* Wed Mar 03 2010 Harald Hoyer <harald@redhat.com> 147-2.11
- add SCSI SAS handling to path_id (rhbz#537185)
- fixed handling of boxes with lots of disks and huge
  volume groups (rhbz#570016)
- fixed virtio-ports rule (rhbz#569699)
- Resolves: rhbz#537185, rhbz#569699, rhbz#570016

* Tue Feb 23 2010 Harald Hoyer <harald@redhat.com> 147-2.10
- add one more letter to renamed interfaces to avoid name 
  clashing (rhbz#565724)
- Resolves: rhbz#565724

* Mon Feb 22 2010 Harald Hoyer <harald@redhat.com> 147-2.9
- rename non-handled network interfaces, so that the handled
  can be renamed to their destination name (rhbz#565724)
- Resolves: rhbz#565724

* Mon Feb 22 2010 Harald Hoyer <harald@redhat.com> 147-2.8
- reverting patch for network interface renaming (rhbz#565724)
- Related: rhbz#565724

* Tue Feb 16 2010 Harald Hoyer <harald@redhat.com> 147-2.7
- fixed udev-post initscript retriggering (rhbz#566568)
- attempt to fix network interface renaming (rhbz#565724)
- Resolves: rhbz#565724, rhbz#566568

* Tue Feb 09 2010 Harald Hoyer <harald@redhat.com> 147-2.6
- ignore dev_id for all s390 network interfaces (rhbz#561017)
- Resolves: rhbz#561017

* Tue Feb 09 2010 Harald Hoyer <harald@redhat.com> 147-2.5
- ignore dev_id for layer3 s390 network interfaces (rhbz#561017)
- Resolves: rhbz#561017

* Tue Jan 26 2010 Harald Hoyer <harald@redhat.com> 147-2.4
- add symlink rule for virtio ports (rhbz#559180)
- fixed initscript
- create /dev/net/tun with 0666 in start_udev
- Export ID_WWN_VENDOR_EXTENSION and ID_WWN_WITH_EXTENSION
- Related: rhbz#543948 rhbz#515413
- Resolves: rhbz#559180

* Wed Jan 13 2010 Harald Hoyer <harald@redhat.com> 147-2.3
- rebuild with gobject-introspection (#553806)
- Resolves: rhbz#553806

* Fri Jan 08 2010 Harald Hoyer <harald@redhat.com> 147-2.2
- only require s390utils-base, rather than s390utils (#553156)
- removed non-working softlinks (partly fixes also #528883)
- Resolves: rhbz#553156

* Fri Dec 11 2009 Dennis Gregorovic <dgregor@redhat.com> - 147-2.1
- Rebuilt for RHEL 6

* Tue Nov 24 2009 Harald Hoyer <harald@redhat.com> 147-2
- require s390utils, because it's essential on s390

* Thu Nov 12 2009 Harald Hoyer <harald@redhat.com> 147-1
- version 147
- Fix upgrade from Fedora 11 with bluez installed (#533925)
- obsolete DeviceKit and DeviceKit-devel (#532961)
- fixed udev-post exit codes (#523976)
- own directory /lib/udev/keymaps (#521801)
- no more floppy modaliases (#514329)
- added one more modems to modem-modeswitch.rules (#515349)
- add NEWS file to the doc section
- automatically turn on hotplugged CPUs (rhbz#523127)
- recognize a devtmpfs on /dev (bug #528488)

* Fri Oct 09 2009 Harald Hoyer <harald@redhat.com> 147-0.1.gitdf3e07d
- pre 147 
- database format changed
- lots of potential buffer overflow fixes

* Tue Sep 29 2009 Harald Hoyer <harald@redhat.com> 145-10
- add ConsoleKit patch for ConsoleKit 0.4.1

* Fri Sep 25 2009 harald@redhat.com 145-9
- add patches to fix cdrom_id
- add patch to fix the inotify bug (bug #524752)

* Wed Sep 23 2009 harald@redhat.com 145-8
- obsolete libgudev and libgudev-devel (bug #523569)

* Mon Aug 24 2009 Karsten Hopp <karsten@redhat.com> 145-7
- drop ifnarch s390x for usbutils, as we now have usbutils for s390x

* Mon Aug 24 2009 Harald Hoyer <harald@redhat.com> 145-6
- ifnarch s390 for usbutils

* Tue Aug 04 2009 Harald Hoyer <harald@redhat.com> 145-5
- do not make extra nodes in parallel
- restorecon on /dev

* Tue Aug 04 2009 Harald Hoyer <harald@redhat.com> 145-4
- --enable-debug 
- add patch for timestamps in debugging output

* Wed Jul 29 2009 Harald Hoyer <harald@redhat.com> 145-3
- add patch from upstream git to fix bug #514086
- add version to usbutils build requirement

* Fri Jul 24 2009 Harald Hoyer <harald@redhat.com> 145-2
- fix file permissions
- remove rpath
- chkconfig --add for udev-post
- fix summaries
- add "Required-Stop" to udev-post

* Tue Jul 14 2009 Harald Hoyer <harald@redhat.com> 145-1
- version 145
- add "udevlog" kernel command line option to redirect the
  output of udevd to /dev/.udev/udev.log

* Fri Jul 03 2009 Harald Hoyer <harald@redhat.com> 143-2
- add acpi floppy modalias
- add retrigger of failed events in udev-post.init
- killall pids of udev in %%pre

* Fri Jun 19 2009 Harald Hoyer <harald@redhat.com> 143-1
- version 143

* Thu Jun 18 2009 Harald Hoyer <harald@redhat.com> 142-4
- git fix: udevadm: settle - fix timeout
- git fix: OWNER/GROUP: fix if logic
- git fix: rule-generator: cd - skip by-path links if we create by-id links
- git fix: fix possible endless loop for GOTO to non-existent LABEL
- git fix: cdrom_id: suppress ID_CDROM_MEDIA_STATE=blank for plain non-writable 
		CDROM media

* Thu Jun 18 2009 Harald Hoyer <harald@redhat.com> 142-3
- delay device-mapper changes

* Fri Jun 05 2009 Bastien Nocera <bnocera@redhat.com> 142-2
- Rebuild in dist-f12

* Fri May 15 2009 Harald Hoyer <harald@redhat.com> 142-1
- version 142
- no more libvolume_id and vol_id

* Fri Apr 17 2009 Harald Hoyer <harald@redhat.com> 141-3
- added /dev/fuse creation to start_udev

* Thu Apr 16 2009 Harald Hoyer <harald@redhat.com> 141-2
- fixed post and pre

* Tue Apr 14 2009 Harald Hoyer <harald@redhat.com> 141-1
- version 141

* Wed Apr 01 2009 Harald Hoyer <harald@redhat.com> 139-4
- double the IMPORT buffer (bug #488554)
- Resolves: rhbz#488554

* Wed Apr 01 2009 Harald Hoyer <harald@redhat.com> 139-3
- renamed modprobe /etc/modprobe.d/floppy-pnp to
  /etc/modprobe.d/floppy-pnp.conf (bug #492732 #488768)
- Resolves: rhbz#492732

* Tue Mar 03 2009 Harald Hoyer <harald@redhat.com> 139-2
- speedup of start_udev by doing make_extra_nodes in parallel to 
  the daemon start

* Fri Feb 27 2009 Harald Hoyer <harald@redhat.com> 139-1
- version 139

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 137-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Harald Hoyer <harald@redhat.com> 137-4
- fixed md change/remove event handling

* Thu Feb 05 2009 Harald Hoyer <harald@redhat.com> 137-3
- added 5 second sleep for "modprobedebug" to catch bad modules

* Fri Jan 30 2009 Harald Hoyer <harald@redhat.com> 137-2
- moved groupadd to pre section (bug #483089)

* Thu Jan 29 2009 Harald Hoyer <harald@redhat.com> 137-1
- version 137
- add vol_id patches from kzak
- dialout group has gid 18 now

* Tue Jan 20 2009 Harald Hoyer <harald@redhat.com> 136-2
- added some rule fixes, which will be in udev-137

* Tue Jan 20 2009 Harald Hoyer <harald@redhat.com> 136-1
- test for restorecon in start_udev before it is used (bug #480608)
- added groups video audio cdrom tape dialout in post
  (might be moved to MAKEDEV)
- version 136

* Tue Dec 16 2008 Harald Hoyer <harald@redhat.com> 135-3
- added sepol patch

* Tue Dec 16 2008 Harald Hoyer <harald@redhat.com> 135-2
- changed udevsettle -> udevadm settle
- added doc to libudev-devel
- added more attr and defattr
- various rpmlint fixes

* Tue Dec 02 2008 Harald Hoyer <harald@redhat.com> 135-1
- version 135

* Wed Nov 19 2008 Harald Hoyer <harald@redhat.com> 133-1
- version 133

* Mon Nov 10 2008 Harald Hoyer <harald@redhat.com> 132-1
- version 132
- added memory stick rules (bug #470096)

* Thu Oct 16 2008 Harald Hoyer <harald@redhat.com> 127-2
- added 2 patches for md raid vol_id 

* Mon Sep 01 2008 Harald Hoyer <harald@redhat.com> 127-1
- version 127

* Fri Aug 08 2008 Harald Hoyer <harald@redhat.com> 126-1
- version 126
- fixed udevadm syntax in start_udev (credits B.J.W. Polman)
- removed some manually created devices from makedev (bug #457125)

* Tue Jun 17 2008 Harald Hoyer <harald@redhat.com> 124-1.1
- readded udevcontrol, udevtrigger symlinks for Fedora 9,
  which are needed by live-cd-tools

* Thu Jun 12 2008 Harald Hoyer <harald@redhat.com> 124-1
- version 124
- removed udevcontrol, udevtrigger symlinks (use udevadm now)

* Tue Jun  3 2008 Jeremy Katz <katzj@redhat.com> - 121-2.20080516git
- Add lost F9 change to remove /dev/.udev in start_udev (#442827)

* Fri May 16 2008 Harald Hoyer <harald@redhat.com> 121-1.20080516git
- version 121 + latest git fixes

* Wed May 07 2008 Harald Hoyer <harald@redhat.com> 120-6.20080421git
- added input/hp_ilo_mouse symlink

* Tue May 06 2008 Harald Hoyer <harald@redhat.com> 120-5.20080421git
- remove /dev/.udev in start_udev (bug #442827)

* Mon Apr 21 2008 Harald Hoyer <harald@redhat.com> 120-4.20080421git
- added patches from git:
- persistent device naming: also read unpartitioned media
- scsi_id: initialize serial strings
- logging: add trailing newline to all strings
- path_id: remove subsystem whitelist
- allow setting of MODE="0000"
- selinux: more context settings
- rules_generator: net rules - always add KERNEL== match to generated rules
- cdrom_id: replace with version which also exports media properties
- vol_id: add --offset option
- udevinfo: do not replace chars when printing ATTR== matches
- Resolves: rhbz#440568

* Fri Apr 11 2008 Harald Hoyer <harald@redhat.com> 120-3
- fixed pre/preun scriptlets (bug #441941)
- removed fedora specific patch for selinux symlink handling

* Sat Apr 05 2008 Harald Hoyer <harald@redhat.com> 120-2
- removed warning about deprecated /lib/udev/devices (rhbz#440961)
- replaced /usr/bin/find with shell find function (rhbz#440961)

* Fri Apr 04 2008 Harald Hoyer <harald@redhat.com> 120-1
- version 120

* Mon Mar 17 2008 Harald Hoyer <harald@redhat.com> 118-11
- removed /var/lib/udev/rules.d again

* Fri Mar 14 2008 Harald Hoyer <harald@redhat.com> 118-10
- turned off MAKEDEV cache, until the generated shell scripts 
  create new directories

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-9
- added more support for the "modprobedebug" kernel command 
  line option, to debug hanging kernel modules

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-8
- added /etc/sysconfig/udev to configure some speedups
- added "udevnopersist" as a kernel command line, to disable
  persistent storage symlink generation

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-7
- files from /var/lib/udev/rules.d are copied to /dev/.udev/rules.d 
  at startup and back at shutdown
- persistent cd and net rules generate the files in 
  /dev/.udev/rules.d now
- added post section to symlink 70-persistent-cd.rules 70-persistent-net.rules
  from /etc/udev/rules.d to /dev/.udev/rules.d

* Thu Mar 13 2008 Harald Hoyer <harald@redhat.com> 118-6
- moved all generated files to /var/lib/udev 
  (also 70-persistent-cd.rules 70-persistent-net.rules)
- added a caching mechanism for MAKEDEV (saves some seconds on startup)
- added trigger for selinux-policy and MAKEDEV to remove the udev cache files

* Wed Feb 20 2008 Harald Hoyer <harald@redhat.com> 118-4
- made symlinks relative (rhbz#432878)
- removed the backgrounding of node creation (rhbz#381461)
- do not change sg group ownership to disk for scanners (rhbz#432602)
- attempt to fix selinux symlink bug (rhbz#345071)
- fixed URL
- made rpmlint mostly happy
- disabled static version (no static selinux lib)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 118-3
- Autorebuild for GCC 4.3

* Wed Jan 09 2008 Harald Hoyer <harald@redhat.com> 118-2
- reenabled static version

* Tue Jan 08 2008 Harald Hoyer <harald@redhat.com> 118-1
- version 118
- removed old USB compat rule (rhbz#424331)
- disabled static version

* Thu Oct 18 2007 Harald Hoyer <harald@redhat.com> 116-3
- fixed preun chkconfig
- added /sbin path to chkconfig in post section 
- patch: do not generate net rules for type > 256
- fixes glitches appearing in bz#323991

* Tue Oct 16 2007 Dennis Gilmore <dennis@ausil.us> 116-2
- sparc64 requires -fPIE not -fpie

* Mon Oct 15 2007 Harald Hoyer <harald@redhat.com> 116-1
- version 116

* Fri Oct 12 2007 Harald Hoyer <harald@redhat.com> 115-5.20071012git
- added upstream patch for rhbz#328691
- moved floppy module loading to pnp-alias in /etc/modprobe.d/floppy-pnp

* Wed Oct 10 2007 Harald Hoyer <harald@redhat.com> 115-5.20070921git
- better modprobe options for the kernel command line 'modprobedebug' option

* Fri Sep 21 2007 Harald Hoyer <harald@redhat.com> - 115-4
- more upstream fixes from git

* Thu Sep 20 2007 Harald Hoyer <harald@redhat.com> - 115-3
- some upstream fixes from git
- removed last_rule for loop rules
- added "udevinfo udevtrace" kernel command line options for better debugging

* Fri Sep 07 2007 Harald Hoyer <harald@redhat.com> - 115-2
- some upstream fixes from git
- last_rule for loop rules (speedup for live-cds/qemu with 128 loop devices)

* Fri Aug 24 2007 Harald Hoyer <harald@redhat.com> - 115-1
- version 115

* Fri Aug 24 2007 Harald Hoyer <harald@redhat.com> - 113-12
- removed /dev/tape symlink, because it's now a directory
  (bug #251755)

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 114-4
- added patch to prevent persistent net rules for virtual network interfaces,
  like vmware and vlans

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 114-3
- changed license tag
- changed to latest upstream rule ordering

* Thu Aug 16 2007 Harald Hoyer <harald@redhat.com> - 113-11
- readded firmware rule (#252983)

* Wed Aug 15 2007 Harald Hoyer <harald@redhat.com> - 113-10
- do not run vol_id on non-partition block devices (bug #251401)
- read all multiline pnp modaliases again

* Mon Aug 13 2007 Harald Hoyer <harald@redhat.com> - 114-2
- fixed isapnp rule (bug #251815)
- fix for nikon cameras (bug #251401)

* Fri Aug 10 2007 Harald Hoyer <harald@redhat.com> - 114-1
- version 114
- big rule unification and cleanup
- added persistent names for network and cdrom devices over reboot

* Wed Aug 08 2007 Harald Hoyer <harald@redhat.com> - 113-9
- added lp* to 50-udev.nodes (#251272)

* Mon Jul 30 2007 Harald Hoyer <harald@redhat.com> - 113-8
- removed "noreplace" config tag from rules (#250043)

* Fri Jul 27 2007 Harald Hoyer <harald@redhat.com> - 113-7
- major rule cleanup
- removed persistent rules from 50 and included upstream rules
- removed skip_wait from modprobe

* Fri Jul 20 2007 Harald Hoyer <harald@redhat.com> - 113-6
- kernel does not provide usb_device anymore,
  corrected the rules (#248916)

* Thu Jul 19 2007 Harald Hoyer <harald@redhat.com> - 113-5
- corrected the rule for usb devices (#248916)

* Sat Jul 14 2007 Harald Hoyer <harald@redhat.com> - 113-4
- do not collect modprobes (bug #222542), because firmware
  loading seems to depend on it.

* Mon Jul  9 2007 Harald Hoyer <harald@redhat.com> - 113-3
- speedup things a little bit

* Wed Jun 27 2007 Harald Hoyer <harald@redhat.com> - 113-2
- added more firewire symlinks (#240770)
- minor rule patches

* Tue Jun 26 2007 Harald Hoyer <harald@redhat.com> - 113-1
- version 113
- added rule for SD cards in a TI FlashMedia slot (#217070)

* Tue Jun 26 2007 Harald Hoyer <harald@redhat.com> - 106-4.1
- fixed modprobedebug option
- removed snd-powermac from the default modules (#200585)

* Wed May 02 2007 Harald Hoyer <harald@redhat.com> - 106-4
- do not skip all events on modprobe (#238385)
- Resolves: rhbz#238385

* Fri Apr 27 2007 Harald Hoyer <harald@redhat.com> - 106-3
- modprobe only on modalias (bug #238140)
- make startup messages visible again
- speedup boot process by not executing pam_console_apply while booting
- Resolves: rhbz#238140

* Wed Apr 11 2007 Harald Hoyer <harald@redhat.com> - 106-2
- create floppy device nodes with the correct selinux context (bug #235953)
- Resolves: rhbz#235953

* Wed Mar  7 2007 Harald Hoyer <harald@redhat.com> - 106-1
- version 106
- specfile cleanup
- removed pilot rule
- removed dasd_id and dasd_id rule
- provide static versions in a subpackage

* Wed Feb 21 2007 Harald Hoyer <harald@redhat.com> - 105-1
- version 105

* Tue Feb  6 2007 Harald Hoyer <harald@redhat.com> - 104-2
- moved uinput to input subdirectory (rhbz#213854)
- added USB floppy symlinks (rhbz#185171)
- fixed ZIP drive handling (rhbz#223016)
- Resolves: rhbz#213854,rhbz#185171,rhbz#223016

* Tue Jan 23 2007 Harald Hoyer <harald@redhat.com> - 104-1
- version 104
- merged changes from RHEL

* Wed Dec  6 2006 Harald Hoyer <harald@redhat.com> - 103-3
- changed DRIVER to DRIVERS 
- Resolves: rhbz#218160

* Fri Nov 10 2006 Harald Hoyer <harald@redhat.com> - 103-2
- changed SYSFS to new ATTR rules
- Resolves: rhbz#214898

* Fri Nov 10 2006 Harald Hoyer <harald@redhat.com> - 103-1
- Removed 51-hotplug.rules
- Resolves: rhbz#214277

* Wed Oct 11 2006 Harald Hoyer <harald@redhat.com> - 095-14
- skip persistent block for gnbd devices (bug #210227)

* Wed Oct  4 2006 Harald Hoyer <harald@redhat.com> - 095-13
- fixed path_id script (bug #207139)

* Tue Oct  3 2006 Jeremy Katz <katzj@redhat.com> - 095-12
- autoload mmc_block (#171687)

* Wed Sep 27 2006 Harald Hoyer <harald@redhat.com> - 095-10
- typo in xpram/slram rule (bug #205563)

* Mon Sep 25 2006 Harald Hoyer <harald@redhat.com> - 095-9
- improved error msg for firmware_helper (bug #206944)
- added xpram symlink to slram device nodes (bug #205563)
- removed infiniband rules (bug #206224)
- use newest path_id script (bug #207139)

* Tue Aug 29 2006 Harald Hoyer <harald@redhat.com> - 095-8
- fixed bug #204157

* Wed Aug 16 2006 Harald Hoyer <harald@redhat.com> - 095-7
- added udevtimeout=<timeout in seconds>
  kernel command line parameters for start_udev 
  (default is to wait forever)

* Wed Aug 16 2006 Harald Hoyer <harald@redhat.com> - 095-6
- new speedup patch for selinux (bug #202673)

* Thu Aug 10 2006 Harald Hoyer <harald@redhat.com> - 095-5
- allow long comments (bug #200244)

* Mon Aug  7 2006 Harald Hoyer <harald@redhat.com> - 095-4
- fixed CAPI device nodes (bug #139321)
- fixed bug #201422

* Wed Jul 12 2006 Harald Hoyer <harald@redhat.com> - 095-3
- more infiniband rules (bug #198501)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 095-2.1
- rebuild

* Thu Jul  6 2006 Harald Hoyer <harald@redhat.com> - 095-2
- added option to debug udev with kernel cmdline option "udevdebug"

* Wed Jul  5 2006 Harald Hoyer <harald@redhat.com> - 095-1
- version 095

* Wed Jun 14 2006 Harald Hoyer <harald@redhat.com> - 094-1
- version 094

* Sun May 21 2006 Peter Jones <pjones@redhat.com> - 092-2
- Fix typo in pam-console rule

* Thu May 18 2006 Harald Hoyer <harald@redhat.com> - 092-1
- version 092
- corrected some rules (bug #192210 #190927)

* Tue May 09 2006 Harald Hoyer <harald@redhat.com> - 091-3
- corrected some rules (bug #190927)

* Wed May 03 2006 Harald Hoyer <harald@redhat.com> - 091-2
- added subpackages libvolume_id and libvolume_id-devel

* Wed May 03 2006 Harald Hoyer <harald@redhat.com> - 091-1
- version 091

* Wed Apr 19 2006 Harald Hoyer <harald@redhat.com> - 090-1
- version 090

* Thu Apr 13 2006 Harald Hoyer <harald@redhat.com> - 089-1
- version 089
- do not force loading of parport_pc (bug #186850)
- manually load snd-powermac (bug #176761)
- added usb floppy symlink (bug #185171)
- start_udev uses udevtrigger now instead of udevstart

* Wed Mar 08 2006 Harald Hoyer <harald@redhat.com> - 084-13
- fixed pam_console rules (#182600)

* Mon Mar 06 2006 Harald Hoyer <harald@redhat.com> - 084-12
- fixed DRI permissions

* Sun Mar 05 2006 Bill Nottingham <notting@redhat.com> - 084-11
- use $ENV{MODALIAS}, not $modalias (#181494)

* Thu Mar 02 2006 Harald Hoyer <harald@redhat.com> - 084-10
- fixed cdrom rule

* Wed Mar 01 2006 Harald Hoyer <harald@redhat.com> - 084-9
- create non-enum device (cdrom, floppy, scanner, changer)
  for compatibility (random device wins)
  e.g. /dev/cdrom -> hdd /dev/cdrom-hdc -> hdc /dev/cdrom-hdd -> hdd

* Wed Mar 01 2006 Harald Hoyer <harald@redhat.com> - 084-8
- fixed ZIP drive thrashing (bz #181041 #182601)
- fixed enumeration (%%e does not work anymore) (bz #183288)

* Fri Feb 24 2006 Peter Jones <pjones@redhat.com> - 084-7
- Don't start udevd in %%post unless it's already running
- Stop udevd before chkconfig --del in %%preun

* Fri Feb 24 2006 Harald Hoyer <harald@redhat.com> - 084-6
- put back original WAIT_FOR_SYSFS rule

* Fri Feb 24 2006 Harald Hoyer <harald@redhat.com> - 084-5
- removed WAIT_FOR_SYSFS rule

* Wed Feb 22 2006 Harald Hoyer <harald@redhat.com> - 084-4
- fixed group issue with vol_id (bz #181432)
- fixed dvb permissions (bz #179993)
- added support for scsi media changer (bz #181911)
- fixed pktcdvd device creation (bz #161268)

* Tue Feb 21 2006 Florian La Roche <laroche@redhat.com> - 084-3
- also output the additional space char as part of the startup message

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 084-1.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Harald Hoyer <harald@redhat.com> - 084-1
- version 084

* Mon Feb 06 2006 Harald Hoyer <harald@redhat.com> - 078-9
- closed fd leak (bug #179980)

* Thu Jan 26 2006 Harald Hoyer <harald@redhat.com> - 078-8
- changed usb device naming

* Tue Jan 24 2006 Harald Hoyer <harald@redhat.com> - 078-7
- put WAIT_FOR_SYSFS rules in 05-udev-early.rules

* Mon Jan 23 2006 Harald Hoyer <harald@redhat.com> - 078-6
- added some WAIT_FOR_SYSFS rules
- removed warning message, if udev_db is not available

* Sun Jan 22 2006 Kristian Høgsberg <krh@redhat.com> 078-5
- Drop udev dependency (#178621).

* Wed Jan 11 2006 Harald Hoyer <harald@redhat.com> - 078-4
- removed group "video" from the rules
- fixed specfile
- load nvram, floppy, parport and lp modules in
  /etc/sysconfig/modules/udev-stw.modules until there 
  is a better solution
- fixed more floppy module loading

* Fri Dec 23 2005 Harald Hoyer <harald@redhat.com> - 078-3
- fixed floppy module loading
- added monitor socket
- fixed typo in dvb rule

* Wed Dec 21 2005 Bill Nottingham <notting@redhat.com> - 078-2
- udevstart change: allow greylisting of certain modaliases (usb, firewire)

* Wed Dec 21 2005 Harald Hoyer <harald@redhat.com> - 078-1
- version 078
- fixed symlink to pam_console.dev

* Thu Dec 15 2005 Harald Hoyer <harald@redhat.com> - 077-2
- switched back to udevstart and use active /dev/.udev/queue waiting 
  in start_udev
- removed support for old kernels
- refined some udev.rules

* Tue Dec 13 2005 Harald Hoyer <harald@redhat.com> - 077-1
- version 077
- patch to include udevstart2 in udevd and delay daemonize until queue is empty

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec 06 2005 Harald Hoyer <harald@redhat.com> - 076-1
- speedup udevd with selinux by calling matchpathcon_init_prefix()
- version 076

* Mon Nov 21 2005 Harald Hoyer <harald@redhat.com> - 075-4
- speedup udev event replay with udevstart2 

* Fri Nov 18 2005 Harald Hoyer <harald@redhat.com> - 075-3
- refined start_udev for old kernels

* Fri Nov 11 2005 Harald Hoyer <harald@redhat.com> - 075-2
- moved /etc/udev/scripts to /lib/udev
- moved /etc/udev/devices to /lib/udev/devices
- added new event replay for kernel >= 2.6.15
- added usb devices
- renamed cpu device to cpuid (bug #161538)
- changed vendor string "Onstream" to "On[sS]tream" (bug #173043)
- compiled all *_id programs statically

* Fri Nov 11 2005 Harald Hoyer <harald@redhat.com> - 075-1
- version 075

* Tue Oct 25 2005 Harald Hoyer <harald@redhat.com> - 071-1
- version 071

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-10
- removed group usb

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-9
- added libsepol-devel BuildReq
- refined persistent rules

* Mon Oct 10 2005 Harald Hoyer <harald@redhat.com> - 069-8
- corrected c&p edd_id rule, symlink for js devices
- added -lsepol

* Thu Oct 06 2005 Harald Hoyer <harald@redhat.com> - 069-7
- added edd_id

* Fri Sep 30 2005 Harald Hoyer <harald@redhat.com> - 069-6
- special handling of IEEE1394 firewire devices (bug #168093)

* Fri Sep 23 2005 Harald Hoyer <harald@redhat.com> - 069-5
- added missing path_id

* Wed Sep 21 2005 Harald Hoyer <harald@redhat.com> - 069-4
- readded volume_id now known as vol_id, bug #168883

* Thu Sep 15 2005 Bill Nottingham <notting@redhat.com> - 069-3
- fix firmware loading

* Wed Sep 14 2005 Bill Nottingham <notting@redhat.com> - 069-2
- own /lib/firmware (#167016)

* Wed Sep 14 2005 Harald Hoyer <harald@redhat.com> - 069-1
- version 069

* Thu Aug 04 2005 Harald Hoyer <harald@redhat.com> - 063-6
- compile with pie .. again... (#158935)
- fixed typo in echo (#138509)

* Tue Aug 02 2005 Harald Hoyer <harald@redhat.com> - 063-5
- fixed scsi hotplug replay

* Tue Aug 02 2005 Bill Nottingham <notting@redhat.com> - 063-5
- add rule to allow function id matching for pcmcia after loading
  modules (#164665)

* Tue Aug 02 2005 Harald Hoyer <harald@redhat.com> - 063-4
- fixed typo for tape devices and changed mode to 0660

* Thu Jul 28 2005 Harald Hoyer <harald@redhat.com> - 063-3
- changed "SYMLINK=" to "SYMLINK+="

* Sun Jul 24 2005 Bill Nottingham <notting@redhat.com> - 063-2
- don't set SEQNUM for scsi replay events (#163729)

* Tue Jul 19 2005 Bill Nottingham <notting@redhat.com> - 063-1
- update to 063
- handle the hotplug events for ieee1394, scsi, firmware

* Fri Jul 08 2005 Bill Nottingham <notting@redhat.com> - 062-2
- update to 062
- use included ata_id, build usb_id
- load modules for pci, usb, pcmcia
- ship RELEASE-NOTES in %%doc

* Thu Jul 07 2005 Harald Hoyer <harald@redhat.com> - 058-2
- compile with pie

* Fri May 20 2005 Bill Nottingham <notting@redhat.com> - 058-1
- update to 058, fixes conflict with newer kernels (#158371)

* Thu May 12 2005 Harald Hoyer <harald@redhat.com> - 057-6
- polished persistent scripts

* Thu May  5 2005 Bill Nottingham <notting@redhat.com> - 057-5
- rebuild

* Thu May  5 2005 Bill Nottingham <notting@redhat.com> - 057-4
- better check for mounted tmpfs on /dev (#156862)

* Wed Apr 27 2005 Peter Jones <pjones@redhat.com> - 057-3
- use udevstart rather than udev for udevstart.static 

* Thu Apr 21 2005 Harald Hoyer <harald@redhat.com> - 057-2
- added Inifiniband devices (bug #147035)
- fixed pam_console.dev (bug #153250)

* Mon Apr 18 2005 Harald Hoyer <harald@redhat.com> - 057-1
- version 057

* Fri Apr 15 2005 Dan Walsh <dwalsh@redhat.com> - 056-2
- Fix SELinux during creation of Symlinks

* Mon Apr 11 2005 Harald Hoyer <harald@redhat.com> - 056-1
- updated to version 056
- merged permissions in the rules file
- added udevpermconv.sh to convert old permission files

* Mon Mar 28 2005 Warren Togami <wtogami@redhat.com> - 050-10
- own default and net dirs (#151368 Hans de Goede)

* Mon Mar 07 2005 Warren Togami <wtogami@redhat.com> - 050-9
- fixed rh#150462 (udev DRI permissions)

* Wed Mar 02 2005 Harald Hoyer <harald@redhat.com> - 050-8
- fixed rh#144598

* Fri Feb 18 2005 Harald Hoyer <harald@redhat.com> - 050-6
- introducing /etc/udev/makedev.d/50-udev.nodes
- glibcstatic patch modified to let gcc4 compile udev

* Thu Feb 10 2005 Harald Hoyer <harald@redhat.com> - 050-5
- doh, reverted the start_udev devel version, which slipped in

* Thu Feb 10 2005 Harald Hoyer <harald@redhat.com> - 050-3
- fixed forgotten " in udev.rules

* Tue Jan 11 2005 Harald Hoyer <harald@redhat.com> - 050-2
- removed /dev/microcode, /dev/cpu/microcode is now the real node
- cleaned up start_udev

* Tue Jan 11 2005 Harald Hoyer <harald@redhat.com> - 050-1
- version 050
- /dev/cpu/0/microcode -> /dev/cpu/microcode

* Tue Dec 21 2004 Dan Walsh <dwalsh@redhat.com> - 048-4
- Call selinux_restore to fix labeling problem in selinux
- Fixes rh#142817

* Tue Dec 21 2004 Harald Hoyer <harald@redhat.com> - 048-3
- maybe fixed bug rh#143367

* Thu Dec 16 2004 Harald Hoyer <harald@redhat.com> - 048-2
- fixed a case where reading /proc/ide/hd?/media returns EIO
  (bug rh#142713)
- changed all device node permissions of group "disk" to 0640 
  (bug rh#110197)
- remove $udev_db with -fr in case of a directory (bug rh#142962)

* Mon Dec 13 2004 Harald Hoyer <harald@redhat.com> - 048-1
- version 048
- major specfile cleanup

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 042-1
- version 042

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 039-10
- speed improvement, scripts in rules are now executed only once,
  instead of four times

* Thu Nov 04 2004 Harald Hoyer <harald@redhat.com> - 039-9
- removed wrong SIG_IGN for SIGCHLD
- moved ide media check to script to wait for the procfs

* Wed Nov  3 2004 Jeremy Katz <katzj@redhat.com> - 039-8.FC3
- recreate lvm device nodes if needed in the trigger (#137807)

* Wed Nov 03 2004 Harald Hoyer <harald@redhat.com> - 039-6.FC3.2
- replace udev.conf by default
- LANG=C for fgrep in start_udev; turn grep into fgrep

* Tue Nov 02 2004 Harald Hoyer <harald@redhat.com> - 039-6.FC3.1
- speed up pam_console.dev
- mount pts and shm, in case of the dev trigger
- increased timeout for udevstart
- removed syslog() from signal handler (caused vmware locks)
- turned off logging, which speeds up the boot process

* Thu Oct 21 2004 Harald Hoyer <harald@redhat.com> - 039-6
- fixed typo

* Thu Oct 21 2004 Harald Hoyer <harald@redhat.com> - 039-5
- added udev-039-norm.patch, which prevents removal of hd* devices,
  because the kernel sends remove/add events, if an IDE removable device
  is close(2)ed. mke2fs, e.g. would fail in this case.

* Wed Oct 20 2004 Harald Hoyer <harald@redhat.com> - 039-4
- do not call dev.d scripts, if network interface hasn't changed 
  the name
- correct wait for dummy network devices
- removed NONBLOCK from volume-id
- do not log in udev.static, which should fix bug 136005 

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-3
- refined wait_for_sysfs for udev.static

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-2
- improved wait_for_sysfs for virtual consoles with Kay Siever's patch
- wait for ppp class
- wait for LVM dm- devices
- integrate wait_for_sys in udev.static for the initrd

* Mon Oct 18 2004 Harald Hoyer <harald@redhat.com> - 039-1
- version 039, fixes also manpage bug 135996 
- fixed glibc issue for static version (getgrnam, getpwnam) (bug 136005)
- close the syslog in every app

* Fri Oct 15 2004 Harald Hoyer <harald@redhat.com> - 038-2
- par[0-9] is now a symlink to lp
- MAKEDEV the parport devices
- now conflicts with older initscripts

* Thu Oct 14 2004 Harald Hoyer <harald@redhat.com> - 038-1
- raw device nodes are now created in directory raw
- version 038

* Wed Oct 13 2004 Harald Hoyer <harald@redhat.com> - 036-1
- better wait_for_sysfs warning messages

* Wed Oct 13 2004 Harald Hoyer <harald@redhat.com> - 035-2
- fixed double bug in start_udev (bug 135405)

* Tue Oct 12 2004 Harald Hoyer <harald@redhat.com> - 035-1
- version 035, which only improves wait_for_sysfs
- load ide modules in start_udev, until a hotplug script is available
  (bug 135260)

* Mon Oct 11 2004 Harald Hoyer <harald@redhat.com> - 034-3
- removed scary error messages from wait_for_sysfs
- symlink from nst? -> tape?
- kill udevd on update

* Fri Oct  8 2004 Harald Hoyer <harald@redhat.com> - 034-2
- check for /proc/sys/dev/cdrom/info existence in check-cdrom.sh

* Fri Oct  8 2004 Harald Hoyer <harald@redhat.com> - 034-1
- new version udev-034
- removed patches, which went upstream
- pam_console.dev link renamed to 05-pam_console.dev
- MAKEDEV.dev links renamed to 10-MAKEDEV.dev

* Thu Oct 07 2004 Harald Hoyer <harald@redhat.com> - 032-10
- added floppy madness (bug 134830)
- replay scsi events in start_udev for the devices on the adapter (bug 130746)

* Wed Oct 06 2004 Harald Hoyer <harald@redhat.com> - 032-9
- obsoleted $UDEV_LOG, use udev_log
- correct SYMLINK handling in pam_console.dev
- specfile cleanup
- added check-cdrom.sh for nice cdrom symlinks

* Mon Oct 04 2004 Harald Hoyer <harald@redhat.com> - 032-8
- added patches from Féliciano Matias for multiple symlinks (bug 134477 and 134478)
- corrected some permissions with a missing leading 0
- added z90crypt to the permissions file (bug 134448)
- corrected requires and conflicts tags
- removed /dev/log from MAKEDEV creation

* Fri Oct 01 2004 Harald Hoyer <harald@redhat.com> - 032-7
- more device nodes for those without initrd

* Thu Sep 30 2004 Harald Hoyer <harald@redhat.com> - 032-6
- prevent error message from device copying
- use already translated starting strings

* Wed Sep 29 2004 Harald Hoyer <harald@redhat.com> - 032-5
- add "fi" to start_udev
- do not create floppy devices manually (bug 133838)

* Tue Sep 28 2004 Harald Hoyer <harald@redhat.com> - 032-4
- made /etc/udev/devices/ for manual device nodes
- refined SELINUX check, if /dev is not yet mounted in start_dev

* Mon Sep 27 2004 Harald Hoyer <harald@redhat.com> - 032-3
- corrected permissions for /dev/rtc (bug 133636)
- renamed device-mapper to mapper/control (bug 133688)

* Wed Sep 22 2004 Harald Hoyer <harald@redhat.com> - 032-2
- removed option to turn off udev
- udevstart.static now symling to udev.static

* Tue Sep 21 2004 Harald Hoyer <harald@redhat.com> - 032-1
- version 032

* Mon Sep 20 2004 Harald Hoyer <harald@redhat.com> - 030-27
- simplified udev.conf
- refined close_on_exec patch
- added pam_console supply for symlinks, now gives correct permissions,
  for e.g. later plugged in cdroms
- renamed sr? to scd? (see devices.txt; k3b likes that :)

* Mon Sep 13 2004 Jeremy Katz <katzj@redhat.com> - 030-26
- require a 2.6 kernel
- prereq instead of requires MAKEDEV
- obsolete and provide dev
- add a trigger for the removal of /dev so that we set things up 

* Fri Sep 10 2004 Dan Walsh <dwalsh@redhat.com> - 030-25
- Use matchmediacon

* Fri Sep 10 2004 Harald Hoyer <harald@redhat.com> - 030-24
- check if SELINUX is not disabled before executing setfiles (bug 132099)

* Wed Sep  8 2004 Harald Hoyer <harald@redhat.com> - 030-23
- mount tmpfs with mode 0755 in start_udev

* Tue Sep  7 2004 Harald Hoyer <harald@redhat.com> - 030-22
- applied rules from David Zeuthen which read /proc directly without 
  shellscript

* Tue Sep  7 2004 Harald Hoyer <harald@redhat.com> - 030-21
- applied enumeration patch from David Zeuthen for cdrom symlinks (bug 131532)
- create /dev/ppp in start_udev (bug 131114)
- removed nvidia devices from start_udev
- check for restorecon presence in start_udev (bug 131904)

* Fri Sep  3 2004 Harald Hoyer <harald@redhat.com> - 030-20
- due to -x added to MAKEDEV specify the par and lp numbers

* Fri Sep  3 2004 Harald Hoyer <harald@redhat.com> - 030-19
- added udev-030-rhsec.patch (bug 130351)

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 030-18
- make the exact device in start_udev (and thus, require new MAKEDEV)

* Thu Sep  2 2004 Jeremy Katz <katzj@redhat.com> - 030-17
- make sure file contexts of everything in the tmpfs /dev are set right 
  when start_udev runs

* Thu Sep 02 2004 Harald Hoyer <harald@redhat.com> - 030-16
- moved %%{_sysconfdir}/hotplug.d/default/udev.hotplug to %%{_sysconfdir}/hotplug.d/default/10-udev.hotplug

* Thu Sep 02 2004 Harald Hoyer <harald@redhat.com> - 030-15
- added nvidia devices to start_udev
- added UDEV_RAMFS for backwards compat to udev.conf
- changed Group (bug 131488)
- added libselinux-devel to build requirements

* Wed Sep  1 2004 Jeremy Katz <katzj@redhat.com> - 030-14
- require MAKEDEV

* Wed Sep 1 2004 Dan Walsh <dwalsh@redhat.com> - 030-13
- Change to setfilecon if directory exists.

* Wed Sep 01 2004 Harald Hoyer <harald@redhat.com> - 030-12
- fixed start_udev

* Tue Aug 31 2004 Jeremy Katz <katzj@redhat.com> - 030-11
- use tmpfs instead of ramfs (it has xattr support now)
- change variables appropriately to TMPFS intead of RAMFS in udev.conf
- create loopN, not just loop in start_udev

* Fri Aug 27 2004 Dan Walsh <dwalsh@redhat.com> - 030-10
- Fix Patch

* Thu Aug 26 2004 Dan Walsh <dwalsh@redhat.com> - 030-9
- Cleaned up selinux patch

* Tue Aug 24 2004 Harald Hoyer <harald@redhat.com> - 030-8
- changed defaults not to remove device nodes
- added rule for net/tun
- extended start_udev to create devices, which can trigger module autoloading
- refined cloexec patch, to redirect stdin,out,err of /dev.d execed apps to /dev/null

* Mon Aug 23 2004 Harald Hoyer <harald@redhat.com> - 030-7
- removed usage of /usr/bin/seq in start_udev
- set correct permissions in start_udev
- extended the cloexec patch
- removed udev-persistent package (define with_persistent==0)
- check for /var/run/console/console.lock before calling /sbin/pam_console_setowner
- linked pam_console_setowner statically against libglib-2.0.a

* Fri Aug 20 2004 Harald Hoyer <harald@redhat.com> - 030-5
- use correct console.lock file now in pam_console_setowner

* Wed Aug 18 2004 Harald Hoyer <harald@redhat.com> - 030-4
- added the selinux patch

* Fri Jul 23 2004 Harald Hoyer <harald@redhat.com> - 030-3
- extended the cloexec patch

* Wed Jul 21 2004 Dan Walsh <dwalsh@redhat.com> - 030-2
- Close Database fd in exec processes using FD_CLOSEXEC

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 030-1
- version 030

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 029-4
- added udevstart.static 

* Wed Jul 14 2004 Harald Hoyer <harald@redhat.com> - 029-3
- put /etc/sysconfig/udev in /etc/udev/udev.conf and removed it
- made only udev.static static
- make our defaults the default values
- removed /udev

* Tue Jul  6 2004 Harald Hoyer <harald@redhat.com> - 029-1
- version 029, added udev_remove and udev_owner to udev.conf

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  8 2004 Harald Hoyer <harald@redhat.com> - 026-3
- fixed UDEV_REMOVE=no

* Tue Jun  8 2004 Harald Hoyer <harald@redhat.com> - 026-2
- udev-026
- preserve ownership of device nodes, which already exist
- do not remove device nodes if UDEV_REMOVE="no"
- added volume_id
- build with klibc

* Wed May 26 2004 Harald Hoyer <harald@redhat.com> - 025-1
- udev-025
- added ata_identify
- build nearly all with dietlibc

* Mon May 10 2004 Elliot Lee <sopwith@redhat.com> 024-6
- Turn off udevd by default for FC2

* Tue Apr 20 2004 Harald Hoyer <harald@redhat.com> - 024-5
- fixed permission for /dev/tty (FC2)

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-4
- moved the 00- files to 50-, to let the use place his files in front

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-3
- set UDEV_SELINUX to yes
- added UDEV_LOG

* Thu Apr 15 2004 Harald Hoyer <harald@redhat.com> - 024-2
- added /udev to filelist

* Wed Apr 14 2004 Harald Hoyer <harald@redhat.com> - 024-1
- update to 024
- added /etc/sysconfig/udev
- added selinux, pam_console, dbus support

* Fri Mar 26 2004 Harald Hoyer <harald@redhat.com> - 023-1
- update to 023

* Wed Mar 24 2004 Bill Nottingham <notting@redhat.com> 022-1
- update to 022

* Sun Mar 21 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- really move initscript

* Sun Feb 29 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- move chkconv to preun
- nicer url

* Wed Feb 25 2004 Harald Hoyer <harald@redhat.com> - 018-1
- changes permissions and rules

* Mon Feb 23 2004 Dan Walsh <dwalsh@redhat.com>
- Add selinux support

* Thu Feb 19 2004 Greg Kroah-Hartman <greg@kroah.com>
- add some more files to the documentation directory
- add ability to build scsi_id and make it the default

* Mon Feb 16 2004 Greg Kroah-Hartman <greg@kroah.com>
- fix up udevd build, as it's no longer needed to be build seperatly
- add udevtest to list of files
- more Red Hat sync ups.

* Thu Feb 12 2004 Greg Kroah-Hartman <greg@kroah.com>
- add some changes from the latest Fedora udev release.

* Mon Feb 2 2004 Greg Kroah-Hartman <greg@kroah.com>
- add udevsend, and udevd to the files
- add ability to build udevd with glibc after the rest is build with klibc

* Mon Jan 26 2004 Greg Kroah-Hartman <greg@kroah.com>
- added udevinfo to rpm
- added URL to spec file
- added udevinfo's man page

* Mon Jan 05 2004 Rolf Eike Beer <eike-hotplug@sf-tec.de>
- add defines to choose the init script (Redhat or LSB)

* Tue Dec 16 2003 Robert Love <rml@ximian.com>
- install the initscript and run chkconfig on it

* Sun Nov 2 2003 Greg Kroah-Hartman <greg@kroah.com>
- changes due to config file name changes

* Fri Oct 17 2003 Robert Love <rml@tech9.net>
- Make work without a build root
- Correctly install the right files
- Pass the RPM_OPT_FLAGS to gcc so we can build per the build policy
- Put some prereqs in
- Install the hotplug symlink to udev

* Mon Jul 28 2003 Paul Mundt <lethal@linux-sh.org>
- Initial spec file for udev-0.2.
