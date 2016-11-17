# -*- rpm-spec -*-

# If neither fedora nor rhel was defined, try to guess them from %{dist}
%if !0%{?rhel} && !0%{?fedora}
%{expand:%(echo "%{?dist}" | \
  sed -ne 's/^\.el\([0-9]\+\).*/%%define rhel \1/p')}
%{expand:%(echo "%{?dist}" | \
  sed -ne 's/^\.fc\?\([0-9]\+\).*/%%define fedora \1/p')}
%endif

# Default to skipping autoreconf.  Distros can change just this one line
# (or provide a command-line override) if they backport any patches that
# touch configure.ac or Makefile.am.
%{!?enable_autotools:%define enable_autotools 1}

# A client only build will create a libvirt.so only containing
# the generic RPC driver, and test driver and no libvirtd
# Default to a full server + client build
%define client_only        0

# Now turn off server build in certain cases

# RHEL-5 builds are client-only for s390, ppc
%if 0%{?rhel} == 5
%ifnarch %{ix86} x86_64 ia64
%define client_only        1
%endif
%endif

# Disable all server side drivers if client only build requested
%if %{client_only}
%define server_drivers     0
%else
%define server_drivers     1
%endif

# Always build with dlopen'd modules
%define with_driver_modules 0

# Now set the defaults for all the important features, independent
# of any particular OS

# First the daemon itself
%define with_libvirtd      0%{!?_without_libvirtd:%{server_drivers}}
%define with_avahi         0%{!?_without_avahi:%{server_drivers}}

# Then the hypervisor drivers that run in libvirtd
%define with_xen           0%{!?_without_xen:%{server_drivers}}
%define with_qemu          0%{!?_without_qemu:%{server_drivers}}
%define with_lxc           0%{!?_without_lxc:%{server_drivers}}
%define with_uml           0%{!?_without_uml:%{server_drivers}}
%define with_libxl         0%{!?_without_libxl:%{server_drivers}}

%define with_qemu_tcg      %{with_qemu}
# Change if we ever provide qemu-kvm binaries on non-x86 hosts
%ifarch %{ix86} x86_64
%define with_qemu_kvm      %{with_qemu}
%else
%define with_qemu_kvm      0
%endif

# Then the hypervisor drivers that run outside libvirtd, in libvirt.so
%define with_openvz        0%{!?_without_openvz:1}
%define with_vbox          0%{!?_without_vbox:1}
%define with_vmware        0%{!?_without_vmware:1}
%define with_phyp          0%{!?_without_phyp:1}
%define with_esx           0%{!?_without_esx:1}
%define with_hyperv        0%{!?_without_hyperv:1}
%define with_xenapi        0%{!?_without_xenapi:1}
%define with_parallels     0%{!?_without_parallels:1}

# Then the secondary host drivers, which run inside libvirtd
%define with_network          0%{!?_without_network:%{server_drivers}}
%define with_storage_fs       0%{!?_without_storage_fs:%{server_drivers}}
%define with_storage_lvm      0%{!?_without_storage_lvm:%{server_drivers}}
%define with_storage_iscsi    0%{!?_without_storage_iscsi:%{server_drivers}}
%define with_storage_disk     0%{!?_without_storage_disk:%{server_drivers}}
%define with_storage_mpath    0%{!?_without_storage_mpath:%{server_drivers}}
%if 0%{?fedora} >= 16
%define with_storage_rbd      0%{!?_without_storage_rbd:%{server_drivers}}
%else
%define with_storage_rbd      0
%endif
%if 0%{?fedora} >= 17
%define with_storage_sheepdog 0%{!?_without_storage_sheepdog:%{server_drivers}}
%else
%define with_storage_sheepdog 0
%endif
%define with_numactl          0%{!?_without_numactl:%{server_drivers}}
%define with_selinux          0%{!?_without_selinux:%{server_drivers}}

# A few optional bits off by default, we enable later
%define with_polkit        0%{!?_without_polkit:0}
%define with_capng         0%{!?_without_capng:0}
%define with_netcf         0%{!?_without_netcf:0}
%define with_udev          0%{!?_without_udev:0}
%define with_hal           0%{!?_without_hal:0}
%define with_yajl          0%{!?_without_yajl:0}
%define with_nwfilter      0%{!?_without_nwfilter:0}
%define with_libpcap       0%{!?_without_libpcap:0}
%define with_macvtap       0%{!?_without_macvtap:0}
%define with_libnl         0%{!?_without_libnl:0}
%define with_audit         0%{!?_without_audit:0}
%define with_dtrace        0%{!?_without_dtrace:0}
%define with_cgconfig      0%{!?_without_cgconfig:0}
%define with_sanlock       0%{!?_without_sanlock:0}
%define with_systemd       0%{!?_without_systemd:0}
%define with_numad         0%{!?_without_numad:0}
%define with_firewalld     0%{!?_without_firewalld:0}
%define with_libssh2_transport 0%{!?_without_libssh2_transport:0}

# Non-server/HV driver defaults which are always enabled
%define with_python        0%{!?_without_python:1}
%define with_sasl          0%{!?_without_sasl:1}


# Finally set the OS / architecture specific special cases

# Xen is available only on i386 x86_64 ia64
%ifnarch %{ix86} x86_64 ia64
%define with_xen 0
%define with_libxl 0
%endif

# Numactl is not available on s390[x] and ARM
%ifarch s390 s390x %{arm}
%define with_numactl 0
%endif

# RHEL doesn't ship OpenVZ, VBox, UML, PowerHypervisor,
# VMWare, libxenserver (xenapi), libxenlight (Xen 4.1 and newer),
# or HyperV.
%if 0%{?rhel}
%define with_openvz 0
%define with_vbox 0
%define with_uml 0
%define with_phyp 0
%define with_vmware 0
%define with_xenapi 0
%define with_libxl 0
%define with_hyperv 0
%define with_parallels 0
%endif

# Fedora 17 / RHEL-7 are first where we use systemd. Although earlier
# Fedora has systemd, libvirt still used sysvinit there.
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%define with_systemd 1
%endif

# Fedora 18 / RHEL-7 are first where firewalld support is enabled
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%define with_firewalld 1
%endif

# RHEL-5 has restricted QEMU to x86_64 only and is too old for LXC
%if 0%{?rhel} == 5
%define with_qemu_tcg 0
%ifnarch x86_64
%define with_qemu 0
%define with_qemu_kvm 0
%endif
%define with_lxc 0
%endif

# RHEL-6 has restricted QEMU to x86_64 only, stopped including Xen
# on all archs. Other archs all have LXC available though
%if 0%{?rhel} >= 6
%define with_qemu_tcg 0
%ifnarch x86_64
%define with_qemu 0
%define with_qemu_kvm 0
%endif
%define with_xen 0
%endif

# Fedora doesn't have any QEMU on ppc64 until FC16 - only ppc
%if 0%{?fedora} && 0%{?fedora} < 16
%ifarch ppc64
%define with_qemu 0
%endif
%endif

# Fedora doesn't have new enough Xen for libxl until F16
%if 0%{?fedora} && 0%{?fedora} < 16
%define with_libxl 0
%endif

# PolicyKit was introduced in Fedora 8 / RHEL-6 or newer
%if 0%{?fedora} >= 8 || 0%{?rhel} >= 6
%define with_polkit    0%{!?_without_polkit:1}
%endif

# libcapng is used to manage capabilities in Fedora 12 / RHEL-6 or newer
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%define with_capng     0%{!?_without_capng:1}
%endif

# netcf is used to manage network interfaces in Fedora 12 / RHEL-6 or newer
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%define with_netcf     0%{!?_without_netcf:%{server_drivers}}
%endif

# udev is used to manage host devices in Fedora 12 / RHEL-6 or newer
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%define with_udev     0%{!?_without_udev:%{server_drivers}}
%else
%define with_hal       0%{!?_without_hal:%{server_drivers}}
%endif

# Enable yajl library for JSON mode with QEMU
%if 0%{?fedora} >= 13 || 0%{?rhel} >= 6
%define with_yajl     0%{!?_without_yajl:%{server_drivers}}
%endif

# Enable sanlock library for lock management with QEMU
# Sanlock is available only on x86_64 for RHEL-6 on all arches after that
%if 0%{?fedora} >= 16
%define with_sanlock 0%{!?_without_sanlock:%{server_drivers}}
%endif
%if 0%{?rhel} == 6
%ifarch x86_64
%define with_sanlock 0%{!?_without_sanlock:%{server_drivers}}
%endif
%endif
%if 0%{?rhel} >= 7
%define with_sanlock 0%{!?_without_sanlock:%{server_drivers}}
%endif

# Disable some drivers when building without libvirt daemon.
# The logic is the same as in configure.ac
%if ! %{with_libvirtd}
%define with_network 0
%define with_qemu 0
%define with_lxc 0
%define with_uml 0
%define with_hal 0
%define with_udev 0
%define with_storage_fs 0
%define with_storage_lvm 0
%define with_storage_iscsi 0
%define with_storage_mpath 0
%define with_storage_rbd 0
%define with_storage_sheepdog 0
%define with_storage_disk 0
%endif

%if %{with_qemu} || %{with_lxc} || %{with_uml}
%define with_nwfilter 0%{!?_without_nwfilter:%{server_drivers}}
# Enable libpcap library
%define with_libpcap  0%{!?_without_libpcap:%{server_drivers}}
%define with_macvtap  0%{!?_without_macvtap:%{server_drivers}}

# numad is used to manage the CPU and memory placement dynamically,
# it's not available on s390[x] and ARM.
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
%ifnarch s390 s390x %{arm}
%define with_numad    0%{!?_without_numad:%{server_drivers}}
%endif
%endif
%endif

%if %{with_macvtap}
%define with_libnl 1
%endif

%if 0%{?fedora} >= 11 || 0%{?rhel} >= 5
%define with_audit    0%{!?_without_audit:1}
%endif

%if 0%{?fedora} >= 13 || 0%{?rhel} >= 6
%define with_dtrace 1
%endif

# Pull in cgroups config system
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%if %{with_qemu} || %{with_lxc}
%define with_cgconfig 0%{!?_without_cgconfig:1}
%endif
%endif

%if %{with_udev} || %{with_hal}
%define with_nodedev 1
%else
%define with_nodedev 0
%endif

%if %{with_netcf}
%define with_interface 1
%else
%define with_interface 0
%endif

%if %{with_storage_fs} || %{with_storage_mpath} || %{with_storage_iscsi} || %{with_storage_lvm} || %{with_storage_disk}
%define with_storage 1
%else
%define with_storage 0
%endif


# Force QEMU to run as non-root
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%define qemu_user  qemu
%define qemu_group  qemu
%else
%define qemu_user  root
%define qemu_group  root
%endif


# The RHEL-5 Xen package has some feature backports. This
# flag is set to enable use of those special bits on RHEL-5
%if 0%{?rhel} == 5
%define with_rhel5  1
%else
%define with_rhel5  0
%endif

Summary: Library providing a simple virtualization API
Name: libvirt
Version: 0.10.2
Release: 60%{?dist}%{?extra_release}.0
License: LGPLv2+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://libvirt.org/

%if %(echo %{version} | grep -o \\. | wc -l) == 3
%define mainturl stable_updates/
%endif
Source: http://libvirt.org/sources/%{?mainturl}libvirt-%{version}.tar.gz

Patch1: libvirt-Support-virtio-disk-hotplug-in-JSON-mode.patch
Patch2: libvirt-Support-password-expiry-and-connected-in-the-QEMU-driver.patch
Patch3: libvirt-Support-seamless-migration-of-SPICE-graphics-clients.patch
Patch4: libvirt-Emit-graphics-events-when-a-SPICE-client-connects-disconnects.patch
Patch5: libvirt-Switch-to-private-redhat-namespace-for-QMP-I-O-error-reason.patch
Patch6: libvirt-Disable-KSM-on-domain-startup.patch
Patch7: libvirt-screenshot-Implement-multiple-screen-support.patch
Patch8: libvirt-daemon-Modify-init-script-to-detect-upstart-managed-libvirtd.patch
Patch9: libvirt-qemu-fix-virtio-macvtap-migration-from-6.3-to-older-hosts.patch
Patch10: libvirt-blockjob-add-qemu-capabilities-related-to-block-jobs.patch
Patch11: libvirt-qemu-wait-for-SPICE-to-migrate.patch
Patch12: libvirt-lxc-Correctly-report-active-cgroups.patch
Patch13: libvirt-network-backend-for-virNetworkUpdate-of-interface-list.patch
Patch14: libvirt-Fix-start-of-containers-with-custom-root-filesystem.patch
Patch15: libvirt-Correct-checking-of-virStrcpyStatic-return-value.patch
Patch16: libvirt-conf-Rename-life-cycle-actions-to-event-actions.patch
Patch17: libvirt-conf-Add-on_lockfailure-event-configuration.patch
Patch18: libvirt-locking-Add-const-char-parameter-to-avoid-ugly-typecasts.patch
Patch19: libvirt-locking-Pass-hypervisor-driver-name-when-acquiring-locks.patch
Patch20: libvirt-locking-Add-support-for-lock-failure-action.patch
Patch21: libvirt-locking-Implement-lock-failure-action-in-sanlock-driver.patch
Patch22: libvirt-conf-Add-support-for-startupPolicy-for-USB-devices.patch
Patch23: libvirt-qemu-Introduce-qemuFindHostdevUSBDevice.patch
Patch24: libvirt-qemu-Add-option-to-treat-missing-USB-devices-as-success.patch
Patch25: libvirt-qemu-Implement-startupPolicy-for-USB-passed-through-devices.patch
Patch26: libvirt-Add-MIGRATABLE-flag-for-virDomainGetXMLDesc.patch
Patch27: libvirt-qemu-Make-save-restore-with-USB-devices-usable.patch
Patch28: libvirt-conf-Mark-missing-optional-USB-devices-in-domain-XML.patch
Patch29: libvirt-security-also-parse-user-group-names-instead-of-just-IDs-for-DAC-labels.patch
Patch30: libvirt-doc-update-description-about-security-labels-on-formatdomain.html.patch
Patch31: libvirt-util-extend-virGetUserID-and-virGetGroupID-to-support-names-and-IDs.patch
Patch32: libvirt-security-update-user-and-group-parsing-in-security_dac.c.patch
Patch33: libvirt-doc-update-description-about-user-group-in-qemu.conf.patch
Patch34: libvirt-fix-kvm_pv_eoi-with-kvmclock.patch
Patch35: libvirt-Change-qemuSetSchedularParameters-to-use-AFFECT_CURRENT.patch
Patch36: libvirt-Fix-handling-of-itanium-arch-name-in-QEMU-driver.patch
Patch37: libvirt-Add-a-qemu-capabilities-cache-manager.patch
Patch38: libvirt-Switch-over-to-use-cache-for-building-QEMU-capabilities.patch
Patch39: libvirt-Remove-probing-of-flags-when-launching-QEMU-guests.patch
Patch40: libvirt-Remove-probing-of-machine-types-when-canonicalizing-XML.patch
Patch41: libvirt-Remove-probing-of-CPU-models-when-launching-QEMU-guests.patch
Patch42: libvirt-Make-qemuCapsProbeMachineTypes-qemuCapsProbeCPUModels-static.patch
Patch43: libvirt-Remove-xenner-support.patch
Patch44: libvirt-Refactor-guest-init-to-support-qemu-system-i386-binary-too.patch
Patch45: libvirt-Add-a-qemuMonitorGetVersion-method-for-QMP-query-version-command.patch
Patch46: libvirt-Add-a-qemuMonitorGetMachines-method-for-QMP-query-machines-command.patch
Patch47: libvirt-Add-a-qemuMonitorGetCPUDefinitions-method-for-QMP-query-cpu-definitions-command.patch
Patch48: libvirt-Add-a-qemuMonitorGetCommands-method-for-QMP-query-commands-command.patch
Patch49: libvirt-Add-a-qemuMonitorGetEvents-method-for-QMP-query-events-command.patch
Patch50: libvirt-Add-a-qemuMonitorGetObjectTypes-method-for-QMP-qom-list-types-command.patch
Patch51: libvirt-Add-a-qemuMonitorGetObjectProps-method-for-QMP-device-list-properties-command.patch
Patch52: libvirt-Add-a-qemuMonitorGetTargetArch-method-for-QMP-query-target-command.patch
Patch53: libvirt-Remove-some-unused-includes-in-QEMU-code.patch
Patch54: libvirt-Move-command-event-capabilities-detection-out-of-QEMU-monitor-code.patch
Patch55: libvirt-Fix-regression-starting-QEMU-instances-without-query-events.patch
Patch56: libvirt-Refactor-qemuCapsParseDeviceStr-to-work-from-data-tables.patch
Patch57: libvirt-Fix-QEMU-test-with-1.2.0-help-output.patch
Patch58: libvirt-Ignore-error-from-query-cpu-definitions.patch
Patch59: libvirt-Fix-potential-deadlock-when-agent-is-closed.patch
Patch60: libvirt-Fix-rare-deadlock-in-QEMU-monitor-callbacks.patch
Patch61: libvirt-Convert-virLXCMonitor-to-use-virObject.patch
Patch62: libvirt-Remove-pointless-virLXCProcessMonitorDestroy-method.patch
Patch63: libvirt-Simplify-some-redundant-locking-while-unref-ing-objects.patch
Patch64: libvirt-Fix-deadlock-in-handling-EOF-in-LXC-monitor.patch
Patch65: libvirt-Avoid-bogus-I-O-event-errors-when-closing-the-QEMU-monitor.patch
Patch66: libvirt-qemu-Fix-parsing-of-x86-CPU-models.patch
Patch67: libvirt-python-keep-consistent-handling-of-Python-integer-conversion.patch
Patch68: libvirt-esx-Fix-and-improve-esxListAllDomains-function.patch
Patch69: libvirt-virsh-block-SIGINT-while-getting-BlockJobInfo.patch
Patch70: libvirt-Revert-Use-XDG-Base-Directories-instead-of-storing-in-home-directory.patch
Patch71: libvirt-doc-Sort-out-the-relationship-between-vcpu-vcpupin-and-emulatorpin.patch
Patch72: libvirt-conf-Ignore-vcpupin-for-not-onlined-vcpus-when-parsing.patch
Patch73: libvirt-conf-Initialize-the-pinning-policy-for-vcpus.patch
Patch74: libvirt-qemu-Create-or-remove-cgroup-when-doing-vcpu-hotpluging.patch
Patch75: libvirt-qemu-Initialize-cpuset-for-hotplugged-vcpu-as-def-cpuset.patch
Patch76: libvirt-conf-Ignore-emulatorpin-if-vcpu-placement-is-auto.patch
Patch77: libvirt-qemu-Ignore-def-cpumask-if-emulatorpin-is-specified.patch
Patch78: libvirt-Avoid-straying-cpuset.patch
Patch79: libvirt-conf-fix-virDevicePCIAddressEqual-args.patch
Patch80: libvirt-conf-virDomainDeviceInfoCopy-utility-function.patch
Patch81: libvirt-qemu-reorganize-qemuDomainChangeNet-and-qemuDomainChangeNetBridge.patch
Patch82: libvirt-Add-support-for-SUSPEND_DISK-event.patch
Patch83: libvirt-node_memory-Add-new-parameter-field-to-tune-the-new-sysfs-knob.patch
Patch84: libvirt-daemon-Fix-removing-abstract-namespaces.patch
Patch85: libvirt-tests-Fix-domain-events-python-test.patch
Patch86: libvirt-conf-Fix-crash-with-cleanup.patch
Patch87: libvirt-qemu-Clear-async-job-when-p2p-migration-fails-early.patch
Patch88: libvirt-qemu-Pin-the-emulator-when-only-cpuset-is-specified.patch
Patch89: libvirt-qemu-Correctly-wait-for-spice-to-migrate.patch
Patch90: libvirt-qemu-Fixed-default-machine-detection-in-qemuCapsParseMachineTypesStr.patch
Patch91: libvirt-conf-Make-tri-state-feature-options-more-universal.patch
Patch92: libvirt-conf-Add-support-for-HyperV-Enlightenment-features.patch
Patch93: libvirt-qemu-Add-support-for-HyperV-Enlightenment-feature-relaxed.patch
Patch94: libvirt-network-Set-to-NULL-after-virNetworkDefFree.patch
Patch95: libvirt-qemu-Always-format-CPU-topology.patch
Patch96: libvirt-qemu-Don-t-fail-without-emulatorpin-or-cpumask.patch
Patch97: libvirt-qemu-Allow-migration-with-host-USB-devices.patch
# The following patch is RHEL-only as it was reverted upstream by 23f5e74
Patch98: libvirt-qemu-Do-not-require-hostuuid-in-migration-cookie.patch
Patch99: libvirt-network-free-null-newDef-if-network-fails-to-start.patch
Patch100: libvirt-migrate-v2-use-VIR_DOMAIN_XML_MIGRATABLE-when-available.patch
Patch101: libvirt-qemu-Avoid-holding-the-driver-lock-in-trivial-snapshot-API-s.patch
Patch102: libvirt-storage-list-more-file-types.patch
Patch103: libvirt-storage-treat-aio-like-raw-at-parse-time.patch
Patch104: libvirt-storage-match-RNG-to-supported-driver-types.patch
Patch105: libvirt-storage-use-enum-for-default-driver-type.patch
Patch106: libvirt-storage-use-enum-for-disk-driver-type.patch
Patch107: libvirt-storage-use-enum-for-snapshot-driver-type.patch
Patch108: libvirt-storage-don-t-probe-non-files.patch
Patch109: libvirt-storage-get-entire-metadata-chain-in-one-call.patch
Patch110: libvirt-storage-don-t-require-caller-to-pre-allocate-metadata-struct.patch
Patch111: libvirt-storage-remember-relative-names-in-backing-chain.patch
Patch112: libvirt-storage-make-it-easier-to-find-file-within-chain.patch
Patch113: libvirt-storage-cache-backing-chain-while-qemu-domain-is-live.patch
Patch114: libvirt-storage-use-cache-to-walk-backing-chain.patch
Patch115: libvirt-blockjob-remove-unused-parameters-after-previous-patch.patch
Patch116: libvirt-blockjob-manage-qemu-block-commit-monitor-command.patch
Patch117: libvirt-blockjob-wire-up-online-qemu-block-commit.patch
Patch118: libvirt-blockjob-implement-shallow-commit-flag-in-qemu.patch
Patch119: libvirt-blockjob-refactor-qemu-disk-chain-permission-grants.patch
Patch120: libvirt-blockjob-properly-label-disks-for-qemu-block-commit.patch
Patch121: libvirt-blockjob-avoid-segv-on-early-error.patch
Patch122: libvirt-blockjob-accommodate-early-RHEL-backport-naming.patch
Patch123: libvirt-virsh-Fix-segfault-of-snapshot-list.patch
Patch124: libvirt-network-always-create-dnsmasq-hosts-and-addnhosts-files-even-if-empty.patch
Patch125: libvirt-network-don-t-allow-multiple-default-portgroups.patch
Patch126: libvirt-selinux-Use-raw-contexts.patch
Patch127: libvirt-selinux-add-security-selinux-function-to-label-tapfd.patch
Patch128: libvirt-selinux-Use-raw-contexts-2.patch
Patch129: libvirt-selinux-fix-wrong-tapfd-relablling.patch
Patch130: libvirt-selinux-remove-unused-variables-in-socket-labelling.patch
Patch131: libvirt-selinux-relabel-tapfd-in-qemuPhysIfaceConnect.patch
Patch132: libvirt-storage-let-format-probing-work-on-root-squash-NFS.patch
Patch133: libvirt-snapshot-sanity-check-when-reusing-file-for-snapshot.patch
Patch134: libvirt-blockjob-add-qemu-capabilities-related-to-block-jobs_1.patch
Patch135: libvirt-blockjob-react-to-active-block-copy.patch
Patch136: libvirt-blockjob-return-appropriate-event-and-info.patch
Patch137: libvirt-blockjob-support-pivot-operation-on-cancel.patch
Patch138: libvirt-blockjob-make-drive-reopen-safer.patch
Patch139: libvirt-blockjob-implement-block-copy-for-qemu.patch
Patch140: libvirt-blockjob-allow-for-existing-files-in-block-copy.patch
Patch141: libvirt-blockjob-allow-mirroring-under-SELinux-and-cgroup.patch
Patch142: libvirt-blockjob-relabel-entire-existing-chain.patch
Patch143: libvirt-xml-omit-domain-name-from-comment-if-it-contains-double-hyphen.patch
Patch144: libvirt-cpu-Add-recently-added-cpu-feature-flags.patch
Patch145: libvirt-esx-Update-version-checks-for-vSphere-5.1.patch
Patch146: libvirt-qemu-Add-helper-to-prepare-cpumap-for-affinity-setting.patch
Patch147: libvirt-qemu-Keep-the-affinity-when-creating-cgroup-for-emulator-thread.patch
Patch148: libvirt-qemu-Prohibit-chaning-affinity-of-domain-process-if-placement-is-auto.patch
Patch149: libvirt-network-fix-networkValidate-check-for-default-portgroup-and-vlan.patch
Patch150: libvirt-qemu-fix-attach-detach-of-netdevs-with-matching-mac-addrs.patch
Patch151: libvirt-snapshot-improve-snapshot-list-error-message.patch
Patch152: libvirt-virsh-Remove-flags-from-nodesuspend.patch
Patch153: libvirt-virsh-Fix-POD-syntax.patch
Patch154: libvirt-xml-print-uuids-in-the-warning.patch
Patch155: libvirt-blockjob-support-both-RHEL-and-upstream-qemu-drive-mirror.patch
Patch156: libvirt-sanlock-Introduce-user-and-group-conf-variables.patch
Patch157: libvirt-esx-Fix-connection-to-ESX-5.1.patch
Patch158: libvirt-cpu-Fix-definition-of-flag-smap.patch
Patch159: libvirt-util-do-a-better-job-of-matching-up-pids-with-their-binaries.patch
Patch160: libvirt-qemu-Fix-EmulatorPinInfo-without-emulatorpin.patch
Patch161: libvirt-qemu-Report-errors-from-iohelper.patch
Patch162: libvirt-build-fix-linking-with-systemtap-probes.patch
Patch163: libvirt-iohelper-fdatasync-at-the-end.patch
Patch164: libvirt-net-update-docs-s-domain-network.patch
Patch165: libvirt-cpu-Add-newly-added-cpu-flags.patch
Patch166: libvirt-cpu-Add-AMD-Opteron-G5-cpu-model.patch
Patch167: libvirt-cpu-Add-Intel-Haswell-cpu-model.patch
Patch168: libvirt-snapshot-new-XML-for-external-system-checkpoint.patch
Patch169: libvirt-snapshot-improve-disk-align-checking.patch
Patch170: libvirt-snapshot-populate-new-XML-info-for-qemu-snapshots.patch
Patch171: libvirt-snapshot-merge-pre-snapshot-checks.patch
Patch172: libvirt-qemu-Fix-possible-race-when-pausing-guest.patch
Patch173: libvirt-qemu-Clean-up-snapshot-retrieval-to-use-the-new-helper.patch
Patch174: libvirt-qemu-Split-out-domain-memory-saving-code-to-allow-reuse.patch
Patch175: libvirt-snapshot-Add-flag-to-enable-creating-checkpoints-in-live-state.patch
Patch176: libvirt-snapshot-qemu-Add-async-job-type-for-snapshots.patch
Patch177: libvirt-snapshot-qemu-Rename-qemuDomainSnapshotCreateActive.patch
Patch178: libvirt-snapshot-qemu-Add-support-for-external-checkpoints.patch
Patch179: libvirt-snapshot-qemu-Remove-restrictions-preventing-external-checkpoints.patch
Patch180: libvirt-iohelper-Don-t-report-errors-on-special-FDs.patch
Patch181: libvirt-esx-Yet-another-connection-fix-for-5.1.patch
Patch182: libvirt-qemu-Don-t-corrupt-pointer-in-qemuDomainSaveMemory.patch
Patch183: libvirt-build-place-attributes-in-correct-location.patch
Patch184: libvirt-Introduce-new-VIR_DOMAIN_EVENT_SUSPENDED_API_ERROR-event.patch
Patch185: libvirt-qemu-Emit-event-if-cont-fails.patch
Patch186: libvirt-virsh-make-escape-parsing-common.patch
Patch187: libvirt-virsh-add-snapshot-create-as-memspec-support.patch
Patch188: libvirt-qemu-Fix-domain-ID-numbering-race-condition.patch
Patch189: libvirt-qemu-Allow-migration-to-be-cancelled-at-prepare-phase.patch
Patch190: libvirt-AbortJob-Fix-documentation.patch
Patch191: libvirt-util-Improve-error-reporting-from-absolutePathFromBaseFile-helper.patch
Patch192: libvirt-storage-fix-broken-backing-chain.patch
Patch193: libvirt-nodeinfo-Add-check-and-workaround-to-guarantee-valid-cpu-topologies.patch
Patch194: libvirt-nodeinfotest-Add-test-data-for-2-processor-host-with-broken-NUMA.patch
Patch195: libvirt-nodeinfotest-Add-test-data-from-a-AMD-bulldozer-machine.patch
Patch196: libvirt-virsh-save-report-an-error-if-XML-file-can-t-be-read.patch
Patch197: libvirt-virsh-fix-uninitialized-variable-in-cmdSnapshotEdit.patch
Patch198: libvirt-qemu-allow-larger-discrepency-between-memory-currentMemory-in-domain-xml.patch
Patch199: libvirt-Add-note-about-numeric-domain-names-to-manpage.patch
Patch200: libvirt-Use-virNetServerRun-instead-of-custom-main-loop.patch
Patch201: libvirt-qemu-fix-RBD-attach-regression.patch
Patch202: libvirt-qemu-Stop-recursive-detection-of-image-chains-when-an-image-is-missing.patch
Patch203: libvirt-Fix-exiting-of-libvirt_lxc-program-on-container-quit.patch
Patch204: libvirt-snapshot-qemu-Add-support-for-external-inactive-snapshots.patch
Patch205: libvirt-conf-Fix-private-symbols-exported-by-files-in-conf.patch
Patch206: libvirt-snapshot-qemu-Fix-detection-of-external-snapshots-when-deleting.patch
Patch207: libvirt-snapshot-require-user-to-supply-external-memory-file-name.patch
Patch208: libvirt-snapshot-add-two-more-filter-sets-to-API.patch
Patch209: libvirt-snapshot-add-virsh-back-compat-support-for-new-filters.patch
Patch210: libvirt-snapshot-implement-new-filter-sets.patch
Patch211: libvirt-snapshot-expose-location-through-virsh-snapshot-info.patch
Patch212: libvirt-sanlock-Retry-after-EINPROGRESS.patch
Patch213: libvirt-storage-fix-logical-volume-cloning.patch
Patch214: libvirt-cpu-Add-Intel-Haswell-cpu-model-fix-previous-downstream-definition.patch
Patch215: libvirt-virsh-Report-error-when-taking-a-snapshot-with-empty-memspec-argument.patch
Patch216: libvirt-lxc-Don-t-crash-if-no-security-driver-is-specified-in-libvirt_lxc.patch
Patch217: libvirt-lxc-Avoid-segfault-of-libvirt_lxc-helper-on-early-cleanup-paths.patch
Patch218: libvirt-Fix-uninitialized-variable-in-virLXCControllerSetupDevPTS.patch
Patch219: libvirt-storage-fix-device-detach-regression-with-cgroup-ACLs.patch
Patch220: libvirt-storage-Fix-bug-of-fs-pool-destroying.patch
Patch221: libvirt-qemu-fix-a-crash-when-save-file-can-t-be-opened.patch
Patch222: libvirt-bitmap-fix-typo-to-use-UL-type-of-integer-constant-in-virBitmapIsAllSet.patch
Patch223: libvirt-virsh-Rewrite-cmdDomDisplay.patch
Patch224: libvirt-network-fix-crash-when-portgroup-has-no-name.patch
Patch225: libvirt-util-capabilities-detection-for-dnsmasq.patch
Patch226: libvirt-util-new-virSocketAddrIsPrivate-function.patch
Patch227: libvirt-network-use-dnsmasq-bind-dynamic-when-available.patch
Patch228: libvirt-storage-fix-scsi-detach-regression-with-cgroup-ACLs.patch
Patch229: libvirt-libssh2_session-support-DSS-keys-as-well.patch
Patch230: libvirt-virsh-fix-error-messages-in-iface-bridge.patch
Patch231: libvirt-virsh-check-the-return-value-of-virStoragePoolGetAutostart.patch
Patch232: libvirt-conf-check-the-return-value-of-virXPathNodeSet.patch
Patch233: libvirt-conf-snapshot-check-return-value-of-virDomainSnapshotObjListNum.patch
Patch234: libvirt-util-fix-virBitmap-allocation-in-virProcessInfoGetAffinity.patch
Patch235: libvirt-virsh-use-correct-sizeof-when-allocating-cpumap.patch
Patch236: libvirt-rpc-don-t-destroy-xdr-before-creating-it-in-virNetMessageEncodeHeader.patch
Patch237: libvirt-virsh-do-timing-even-for-unusable-connections.patch
Patch238: libvirt-conf-fix-uninitialized-variable-in-virDomainListSnapshots.patch
Patch239: libvirt-Fix-error-handling-in-virSecurityManagerGetMountOptions.patch
Patch240: libvirt-conf-prevent-crash-with-no-uuid-in-cephx-auth-secret.patch
Patch241: libvirt-conf-fix-virDomainNetGetActualDirect-and-BridgeName.patch
Patch242: libvirt-virsh-Report-errors-if-arguments-of-the-schedinfo-command-are-incorrect.patch
Patch243: libvirt-systemd-require-dbus-service.patch
Patch244: libvirt-qemu-Don-t-free-PCI-device-if-adding-it-to-activePciHostdevs-fails.patch
Patch245: libvirt-util-Slightly-refactor-PCI-list-functions.patch
Patch246: libvirt-qemu-Fix-memory-and-FD-leak-on-PCI-device-detach.patch
Patch247: libvirt-util-Do-not-keep-PCI-device-config-file-open.patch
Patch248: libvirt-node_memory-Improve-the-docs.patch
Patch249: libvirt-node_memory-Do-not-fail-if-there-is-parameter-unsupported.patch
Patch250: libvirt-node_memory-Fix-bug-of-node_memory_tune.patch
Patch251: libvirt-qemu-eliminate-bogus-error-log-when-changing-netdev-s-bridge.patch
Patch252: libvirt-remote-Avoid-the-thread-race-condition.patch
Patch253: libvirt-storage-Error-out-earlier-if-the-volume-target-path-already-exists.patch
Patch254: libvirt-dnsmasq-Fix-parsing-of-the-version-number.patch
Patch255: libvirt-qemu-Restart-CPUs-with-valid-async-job-type-when-doing-external-snapshots.patch
Patch256: libvirt-examples-Fix-balloon-event-callback.patch
Patch257: libvirt-util-Don-t-fail-virGetGroupIDByName-when-group-not-found.patch
Patch258: libvirt-util-Don-t-fail-virGetUserIDByName-when-user-not-found.patch
Patch259: libvirt-util-rework-error-reporting-in-virGet-User-Group-IDByName.patch
Patch260: libvirt-util-Fix-warning-message-in-previous-patch.patch
Patch261: libvirt-network-prevent-dnsmasq-from-listening-on-localhost.patch
Patch262: libvirt-sanlock-Re-add-lockspace-unconditionally.patch
Patch263: libvirt-Fix-virsh-create-example.patch
Patch264: libvirt-docs-fix-some-typos-in-examples.patch
Patch265: libvirt-network-don-t-require-private-addresses-if-dnsmasq-uses-SO_BINDTODEVICE.patch
Patch266: libvirt-util-add-missing-error-log-messages-when-failing-to-get-netlink-VFINFO.patch
Patch267: libvirt-util-fix-functions-that-retrieve-SRIOV-VF-info.patch
Patch268: libvirt-util-fix-botched-check-for-new-netlink-request-filters.patch
Patch269: libvirt-blockjob-fix-memleak-that-prevented-block-pivot.patch
Patch270: libvirt-sanlock-Chown-lease-files-as-well.patch
Patch271: libvirt-snapshot-conf-Make-virDomainSnapshotIsExternal-more-reusable.patch
Patch272: libvirt-snapshot-qemu-Separate-logic-blocks-with-newlines.patch
Patch273: libvirt-snapshot-qemu-Fix-segfault-and-vanishing-snapshots-when-redefining.patch
Patch274: libvirt-snapshot-qemu-Allow-redefinition-of-external-snapshots.patch
Patch275: libvirt-util-Prepare-helpers-for-unpriv_sgio-setting.patch
Patch276: libvirt-qemu-Add-a-hash-table-for-the-shared-disks.patch
Patch277: libvirt-docs-Add-docs-and-rng-schema-for-new-XML-tag-sgio.patch
Patch278: libvirt-conf-Parse-and-format-the-new-XML.patch
Patch279: libvirt-qemu-set-unpriv_sgio-when-starting-domain-and-attaching-disk.patch
Patch280: libvirt-qemu-Check-if-the-shared-disk-s-cdbfilter-conflicts-with-others.patch
Patch281: libvirt-qemu-Relax-hard-RSS-limit.patch
Patch282: libvirt-qemu_agent-Remove-agent-reference-only-when-disposing-it.patch
Patch283: libvirt-Add-RESUME-event-listener-to-qemu-monitor.patch
Patch284: libvirt-storage-Fix-lvcreate-parameter-for-backingStore.patch
Patch285: libvirt-qemu-Don-t-return-success-if-creation-of-snapshot-save-file-fails.patch
Patch286: libvirt-qemu-Reject-attempts-to-create-snapshots-with-names-containig.patch
Patch287: libvirt-rpc-Fix-crash-on-error-paths-of-message-dispatching.patch
Patch288: libvirt-xen-Resolve-resource-leak-with-cpuset.patch
Patch289: libvirt-schema-Make-the-cpuset-type-reusable-across-schema-files.patch
Patch290: libvirt-schemas-Add-schemas-for-more-CPU-topology-information-in-the-caps-XML.patch
Patch291: libvirt-conf-Split-out-NUMA-topology-formatting-to-simplify-access-to-data.patch
Patch292: libvirt-capabilities-Switch-CPU-data-in-NUMA-topology-to-a-struct.patch
Patch293: libvirt-capabilities-Add-additional-data-to-the-NUMA-topology-info.patch
Patch294: libvirt-test-Add-support-for-thread-and-core-information-for-the-test-driver.patch
Patch295: libvirt-xen-Initialize-variable-before-using.patch
Patch296: libvirt-xen-Actually-fix-the-uninitialized-variable.patch
Patch297: libvirt-spice-Properly-reserve-tlsPort-when-no-port-specified.patch
Patch298: libvirt-qemu_agent-Ignore-expected-EOFs.patch
Patch299: libvirt-qemu-nicer-error-message-if-live-disk-snapshot-unsupported.patch
Patch300: libvirt-qemu-Destroy-domain-on-decompression-binary-error.patch
Patch301: libvirt-qemu-Run-lzop-with-ignore-warn.patch
Patch302: libvirt-Don-t-ignore-return-value-of-qemuProcessKill.patch
Patch303: libvirt-Fix-race-condition-when-destroying-guests.patch
Patch304: libvirt-Log-warning-if-storage-magic-matches-but-version-does-not.patch
Patch305: libvirt-Add-lots-of-debugging-to-storage-file-probing-code.patch
Patch306: libvirt-Fix-probing-of-QED-file-format.patch
Patch307: libvirt-util-add-virendian.h-macros.patch
Patch308: libvirt-util-use-new-virendian.h-macros.patch
Patch309: libvirt-storage-rearrange-functions.patch
Patch310: libvirt-storage-prepare-for-refactoring.patch
Patch311: libvirt-storage-refactor-metadata-lookup.patch
Patch312: libvirt-storage-don-t-follow-backing-chain-symlinks-too-eagerly.patch
Patch313: libvirt-storage-test-backing-chain-traversal.patch
Patch314: libvirt-qemu-check-backing-chains-even-when-cgroup-is-omitted.patch
Patch315: libvirt-python-Fix-bindings-for-virDomainSnapshotGet-Domain-Connect.patch
Patch316: libvirt-qemu-Add-checking-in-helpers-for-sgio-setting.patch
Patch317: libvirt-qemu-Merge-qemuCheckSharedDisk-into-qemuAddSharedDisk.patch
Patch318: libvirt-qemu-Record-names-of-domain-which-uses-the-shared-disk-in-hash-table.patch
Patch319: libvirt-qemu-Update-shared-disk-table-when-reconnecting-qemu-process.patch
Patch320: libvirt-qemu-Move-the-shared-disk-adding-and-sgio-setting-prior-to-attaching.patch
Patch321: libvirt-qemu-Remove-the-shared-disk-entry-if-the-operation-is-ejecting-or-updating.patch
Patch322: libvirt-qemu-Fix-the-memory-leak.patch
Patch323: libvirt-Fix-crash-changing-CDROM-media.patch
Patch324: libvirt-qemu-Avoid-NULL-dereference-in-qemuSharedDiskEntryFree.patch
Patch325: libvirt-qemu-do-not-set-unpriv_sgio-if-neither-supported-nor-requested.patch
Patch326: libvirt-Use-size_t-instead-of-int-for-virDomainDefPtr-struct.patch
Patch327: libvirt-util-add-VIR_-APPEND-INSERT-DELETE-_ELEMENT.patch
Patch328: libvirt-qemu-Fix-QMP-detection-of-QXL-graphics.patch
Patch329: libvirt-qemu-add-qemu-vga-devices-caps-and-one-cap-to-mark-them-usable.patch
Patch330: libvirt-conf-add-optional-attribte-primary-to-video-model-element.patch
Patch331: libvirt-qemu-use-newer-device-video-device-in-qemu-commandline.patch
Patch332: libvirt-tests-add-one-device-video-device-testcase.patch
Patch333: libvirt-qemu-Detect-VGA_QXL-capability-correctly.patch
Patch334: libvirt-qemu-Support-ram-bar-size-for-qxl-devices.patch
Patch335: libvirt-conf-Don-t-leak-primary-video-property-on-error.patch
Patch336: libvirt-storage-lvm-Don-t-overwrite-lvcreate-errors.patch
Patch337: libvirt-storage-lvm-lvcreate-fails-with-allocation-0-don-t-do-that.patch
Patch338: libvirt-storage-Cleanup-logical-volume-creation-code.patch
Patch339: libvirt-docs-Clarify-semantics-of-sparse-storage-volumes.patch
Patch340: libvirt-storage-Fix-memory-leak-with-regfree-reg-call.patch
Patch341: libvirt-storage-Resource-resource-leak-using-tmp_vols.patch
Patch342: libvirt-interface-Resolve-resource-leak-wth-tmp_iface_objs.patch
Patch343: libvirt-locking-Resolve-resource-leaks-on-non-error-path.patch
Patch344: libvirt-selinux-Resolve-resource-leak-using-the-default-disk-label.patch
Patch345: libvirt-storage-Resolve-resource-leaks-with-cmd-processing.patch
Patch346: libvirt-domain_conf-Resolve-resource-leaks-found-by-Valgrind.patch
Patch347: libvirt-qemu_command-Resolve-resource-leaks-found-by-Valgrind.patch
Patch348: libvirt-storage-Need-to-add-virCommandFree.patch
Patch349: libvirt-qemu-Fix-startupPolicy-regression.patch
Patch350: libvirt-util-retry-NLM_F_REQUEST-with-different-values-of-IFLA_EXT_MASK.patch
Patch351: libvirt-security_manager-Don-t-manipulate-domain-XML-in-virDomainDefGetSecurityLabelDef.patch
Patch352: libvirt-security-Don-t-add-seclabel-of-type-none-if-there-s-already-a-seclabel.patch
Patch353: libvirt-libvirt_private.syms-Correctly-export-seclabel-APIs.patch
Patch354: libvirt-security_manager.c-Append-seclabel-iff-generated.patch
Patch355: libvirt-rpc-Fix-client-crash-when-server-drops-connection.patch
Patch356: libvirt-storage-Fix-volume-cloning-for-logical-volume.patch
Patch357: libvirt-qemu-Allow-migration-over-IPv6.patch
Patch358: libvirt-qemu-set-IPv6-migration-capability-when-dump-guest-core-is-present.patch
Patch359: libvirt-remote-Don-t-call-NULL-closeFreeCallback.patch
Patch360: libvirt-libvirt-Increase-connection-reference-count-for-callbacks.patch
Patch361: libvirt-virsh-Unregister-the-connection-close-notifier-upon-termination.patch
Patch362: libvirt-virsh-Move-cmdConnect-from-virsh-host.c-to-virsh.c.patch
Patch363: libvirt-virsh-Register-and-unregister-the-close-callback-also-in-cmdConnect.patch
Patch364: libvirt-rpc-Fix-connection-close-callback-race-condition-and-memory-corruption-crash.patch
Patch365: libvirt-tests-Fix-qemumonitorjsontest-deadlock-when-the-machine-is-under-load.patch
Patch366: libvirt-Avoid-use-of-free-d-memory-in-auto-destroy-callback.patch
Patch367: libvirt-Fix-crash-in-QEMU-auto-destroy-with-transient-guests.patch
Patch368: libvirt-daemon-fix-leak-after-listing-volumes.patch
Patch369: libvirt-Don-t-try-to-add-non-existant-devices-to-ACL.patch
Patch370: libvirt-Avoid-spamming-logs-with-cgroups-warnings.patch
Patch371: libvirt-audit-properly-encode-device-path-in-cgroup-audit.patch
Patch372: libvirt-qemu-Set-correct-migrate-host-in-client_migrate_info.patch
Patch373: libvirt-qemu-Fix-crash-in-migration-of-graphics-less-guests.patch
Patch374: libvirt-Fix-F_DUPFD_CLOEXEC-operation-args.patch
Patch375: libvirt-cgroup-be-robust-against-cgroup-movement-races.patch
Patch376: libvirt-virsocket-Introduce-virSocketAddrIsWildcard.patch
Patch377: libvirt-qemuDomainMigrateGraphicsRelocate-Use-then-new-virSocketAddrIsWildcard.patch
Patch378: libvirt-virSocketAddrIsWildcard-Use-IN6_IS_ADDR_UNSPECIFIED-correctly.patch
Patch379: libvirt-libvirt-lxc-don-t-mkdir-when-selinux-is-disabled.patch
Patch380: libvirt-Don-t-mount-selinux-fs-in-LXC-if-selinux-is-disabled.patch
Patch381: libvirt-virsh-don-t-print-null-in-vol-name-and-vol-pool.patch
Patch382: libvirt-virsh-Fix-docs-for-virsh-setmaxmem.patch
Patch383: libvirt-qemu-Remove-managed-save-flag-from-VM-when-starting-with-force-boot.patch
Patch384: libvirt-qemu-Don-t-update-count-of-vCPUs-if-hot-unplug-has-failed.patch
Patch385: libvirt-conf-net-Fix-deadlock-if-assignment-of-network-def-fails.patch
Patch386: libvirt-RPC-Support-up-to-16384-cpus-on-the-host-and-4096-in-the-guest.patch
Patch387: libvirt-conf-don-t-fail-to-parse-boot-when-parsing-a-single-device.patch
Patch388: libvirt-conf-Allow-for-non-contiguous-device-boot-orders.patch
Patch389: libvirt-qemuDomainChangeGraphics-Check-listen-address-change-by-listen-type.patch
Patch390: libvirt-build-Fix-build-with-Werror.patch
Patch391: libvirt-qemuDomainBlockStatsFlags-Guard-disk-lookup-with-a-domain-job.patch
Patch392: libvirt-qemu-Don-t-fail-to-shutdown-domains-with-unresponsive-agent.patch
Patch393: libvirt-qemu-Wrap-controllers-code-into-dummy-loop.patch
Patch394: libvirt-qemu-Add-controllers-in-specified-order.patch
Patch395: libvirt-tests-Add-test-for-controller-order.patch
Patch396: libvirt-bandwidth-Attach-sfq-to-leaf-node.patch
Patch397: libvirt-bandwidth-Create-hierarchical-shaping-classes.patch
Patch398: libvirt-remote-Forbid-default-session-connections-when-using-ssh-transport.patch
Patch399: libvirt-remote-Fix-client-crash-when-URI-path-is-empty-when-using-ssh.patch
Patch400: libvirt-udev-fix-crash-in-libudev-logging.patch
Patch401: libvirt-iscsi-don-t-leak-portal-string-when-starting-a-pool.patch
Patch402: libvirt-storage-Avoid-double-virCommandFree-in-virStorageBackendLogicalDeletePool.patch
Patch403: libvirt-manual-Fix-copy-paste-errors.patch
Patch404: libvirt-esx-Support-virtualHW-version-9.patch
Patch405: libvirt-manual-Add-info-about-migrateuri-in-virsh-manual.patch
Patch406: libvirt-conf-Fix-cpumask-leak-in-virDomainDefFree.patch
Patch407: libvirt-qemu-Avoid-leaking-uri-in-qemuMigrationPrepareDirect.patch
Patch408: libvirt-Document-that-runtime-changes-may-be-lost-after-S4-suspend.patch
Patch409: libvirt-virsh-iface-bridge-Ignore-delay-if-stp-is-turned-off.patch
Patch410: libvirt-virsh-Obey-pool-or-uuid-spec-when-creating-volumes.patch
Patch411: libvirt-Add-method-for-checking-if-a-string-is-probably-a-log-message.patch
Patch412: libvirt-Convert-QEMU-driver-to-use-virLogProbablyLogMessage.patch
Patch413: libvirt-util-escapes-special-characters-in-VIR_LOG_REGEX.patch
Patch414: libvirt-qemu-Move-QEMU-log-reading-into-a-separate-function.patch
Patch415: libvirt-qemu-Ignore-libvirt-logs-when-reading-QEMU-error-output.patch
Patch416: libvirt-logging-Make-log-regexp-more-compact-and-readable.patch
Patch417: libvirt-qemu-Do-not-report-unsafe-migration-for-local-files.patch
Patch418: libvirt-Plug-leak-in-virCgroupMoveTask.patch
Patch419: libvirt-Fix-invalid-read-in-virCgroupGetValueStr.patch
Patch420: libvirt-pci-initialize-virtual_functions-array-pointer-to-avoid-segfault.patch
Patch421: libvirt-node-device-driver-update-driver-name-during-dumpxml.patch
Patch422: libvirt-qemu-Don-t-force-port-0-for-SPICE.patch
Patch423: libvirt-qemu-refactor-graphics-code-to-not-hardcode-a-single-display.patch
Patch424: libvirt-qemu-graphics-support-for-simultaneous-one-of-each-sdl-vnc-spice.patch
Patch425: libvirt-qemu-Don-t-miss-errors-when-changing-graphics-passwords.patch
Patch426: libvirt-qemu-Allow-seamless-migration-for-domains-with-multiple-graphics.patch
Patch427: libvirt-qemu_migration-Move-waiting-for-SPICE-migration.patch
Patch428: libvirt-util-refactor-iptables-command-construction-into-multiple-steps.patch
Patch429: libvirt-net-support-set-public-ip-range-for-forward-mode-nat.patch
Patch430: libvirt-net-add-support-for-specifying-port-range-for-forward-mode-nat.patch
Patch431: libvirt-qemu_migrate-Dispose-listen-address-if-set-from-config.patch
Patch432: libvirt-qemu-Remove-maximum-cpu-limit-when-setting-processor-count-using-the-API.patch
Patch433: libvirt-qemu_agent-Introduce-helpers-for-agent-based-CPU-hot-un-plug.patch
Patch434: libvirt-virsh-domain-Refactor-cmdVcpucount-and-fix-output-on-inactive-domains.patch
Patch435: libvirt-API-Introduce-VIR_DOMAIN_VCPU_AGENT-for-agent-based-CPU-hot-un-plug.patch
Patch436: libvirt-qemu-Implement-request-of-vCPU-state-using-the-guest-agent.patch
Patch437: libvirt-qemu-Implement-support-for-VIR_DOMAIN_VCPU_AGENT-in-qemuDomainSetVcpusFlags.patch
Patch438: libvirt-qemuDomainGetVcpusFlags-Initialize-ncpuinfo.patch
Patch439: libvirt-Fix-commit-29c1e913e459058c12d02b3f4b767b3dd428a498.patch
Patch440: libvirt-qemu-Make-qemuMigrationIsAllowed-more-reusable.patch
Patch441: libvirt-qemu-Cancel-migration-if-guest-encoutners-I-O-error-while-migrating.patch
Patch442: libvirt-qemu-Forbid-migration-of-machines-with-I-O-errors.patch
Patch443: libvirt-migration-Make-erroring-out-on-I-O-error-controllable-by-flag.patch
Patch444: libvirt-migration-Don-t-propagate-VIR_MIGRATE_ABORT_ON_ERROR.patch
Patch445: libvirt-Paused-domain-should-remain-paused-after-migration.patch
Patch446: libvirt-qemu-new-vnc-display-sharing-policy-caps-flag.patch
Patch447: libvirt-conf-add-sharePolicy-attribute-to-graphics-element-for-vnc.patch
Patch448: libvirt-qemu-add-share-policy-to-qemu-commandline.patch
Patch449: libvirt-virsh-distinguish-errors-between-missing-argument-and-wrong-option.patch
Patch450: libvirt-virsh-fix-incorrect-argument-errors-for-long-options.patch
Patch451: libvirt-virsh-Resolve-Coverity-MISSING_BREAK.patch
Patch452: libvirt-virnetdev-Need-to-initialize-pciConfigAddr.patch
Patch453: libvirt-qemu-fix-double-free-in-qemuMigrationPrepareDirect.patch
Patch454: libvirt-sec_manager-Refuse-to-start-domain-with-unsupported-seclabel.patch
Patch455: libvirt-usb-don-t-spoil-decimal-addresses.patch
Patch456: libvirt-storage-return-1-when-fs-pool-can-t-be-mounted.patch
Patch457: libvirt-conf-avoid-NULL-deref-for-pmsuspended-domain-state.patch
Patch458: libvirt-libvirt-Define-domain-crash-event-types.patch
Patch459: libvirt-qemu-refactor-processWatchdogEvent.patch
Patch460: libvirt-qemu-expose-qemuProcessShutdownOrReboot.patch
Patch461: libvirt-qemu-Implement-oncrash-events-when-guest-panicked.patch
Patch462: libvirt-qemu-Implement-oncrash-coredump-events-when-guest-panicked.patch
Patch463: libvirt-conf-fix-a-memory-leak-when-parsing-nat-port-XML-nodes.patch
Patch464: libvirt-security_manager-fix-comparison.patch
Patch465: libvirt-qemu-Prevent-crash-of-libvirtd-without-guest-agent-configuration.patch
Patch466: libvirt-qemu-Fix-double-free-of-returned-JSON-array-in-qemuAgentGetVCPUs.patch
Patch467: libvirt-qemu_agent-Add-support-for-appending-arrays-to-commands.patch
Patch468: libvirt-Add-support-for-locking-domain-s-memory-pages.patch
Patch469: libvirt-qemu-Implement-support-for-locking-domain-s-memory-pages.patch
Patch470: libvirt-qemu-Check-for-realtime-mlock-on-off-support.patch
Patch471: libvirt-qemu-Move-memory-limit-computation-to-a-reusable-function.patch
Patch472: libvirt-util-new-virCommandSetMax-MemLock-Processes-Files.patch
Patch473: libvirt-qemu-Set-RLIMIT_MEMLOCK-when-memoryBacking-locked-is-used.patch
Patch474: libvirt-Add-Gluster-protocol-as-supported-network-disk-backend.patch
Patch475: libvirt-qemu-Add-support-for-gluster-protocol-based-network-storage-backend.patch
Patch476: libvirt-tests-Add-tests-for-gluster-protocol-based-network-disks-support.patch
Patch477: libvirt-virsh-fix-change-media-bug-on-disk-block-type.patch
Patch478: libvirt-Fix-patches-for-multiple-graphics-and-spice-migration.patch
Patch479: libvirt-Revert-qemu-Remove-maximum-cpu-limit-when-setting-processor-count-using-the-API.patch
Patch480: libvirt-Remove-VIR_DOMAIN_SHUTDOWN_CRASHED-from-public-API.patch
Patch481: libvirt-Rename-VIR_DOMAIN_PAUSED_GUEST_PANICKED-to-VIR_DOMAIN_PAUSED_CRASHED.patch
Patch482: libvirt-Improve-LXC-startup-error-reporting.patch
Patch483: libvirt-qemu-Take-error-path-if-acquiring-of-job-fails-in-qemuDomainSaveInternal.patch
Patch484: libvirt-util-improve-user-lookup-helper.patch
Patch485: libvirt-util-add-virGetGroupList.patch
Patch486: libvirt-util-make-virSetUIDGID-async-signal-safe.patch
Patch487: libvirt-Fix-potential-deadlock-across-fork-in-QEMU-driver.patch
Patch488: libvirt-security-framework-for-driver-PreFork-handler.patch
Patch489: libvirt-security_dac-compute-supplemental-groups-before-fork.patch
Patch490: libvirt-security-fix-deadlock-with-prefork.patch
Patch491: libvirt-Split-TLS-test-into-two-separate-tests.patch
Patch492: libvirt-Avoid-re-generating-certs-every-time.patch
Patch493: libvirt-Change-data-passed-into-TLS-test-cases.patch
Patch494: libvirt-Fix-validation-of-CA-certificate-chains.patch
Patch495: libvirt-Fix-parallel-runs-of-TLS-test-suites.patch
Patch496: libvirt-tests-Fix-parallel-runs-of-TLS-test-suites.patch
Patch497: libvirt-virnettlscontext-Resolve-Coverity-warnings-UNINIT.patch
Patch498: libvirt-Fix-qemuProcessReadLog-with-non-zero-offset.patch
Patch499: libvirt-virSecurityManagerGenLabel-Skip-seclabels-without-model.patch
Patch500: libvirt-bitmap-add-virBitmapCountBits.patch
Patch501: libvirt-virbitmap-Refactor-virBitmapParse-to-avoid-access-beyond-bounds-of-array.patch
Patch502: libvirt-virbitmaptest-Add-test-for-out-of-bounds-condition.patch
Patch503: libvirt-network-allow-vlan-in-type-hostdev-networks.patch
Patch504: libvirt-python-fix-bindings-that-don-t-raise-an-exception.patch
Patch505: libvirt-storage-Update-pool-metadata-after-adding-removing-resizing-volume.patch
Patch506: libvirt-storage-Fix-coverity-warning.patch
Patch507: libvirt-storage-Fix-the-use-after-free-memory-bug.patch
Patch508: libvirt-network-permit-upstream-forwarding-of-unqualified-DNS-names.patch
Patch509: libvirt-security-provide-supplemental-groups-even-when-parsing-label.patch
Patch510: libvirt-qemu-Remove-hostdev-entry-when-freeing-the-depending-network-entry.patch
Patch511: libvirt-virsh-Correct-DESCRIPTION-for-virsh-help-blockcopy.patch
Patch512: libvirt-Add-nat-element-to-forward-network-schemas.patch
Patch513: libvirt-build-more-workarounds-for-if_bridge.h.patch
Patch514: libvirt-migration-do-not-restore-labels-on-failed-migration.patch
Patch515: libvirt-qemu-use-default-machine-type-if-missing-it-in-qemu-command-line.patch
Patch516: libvirt-qemu-don-t-leak-vm-on-failure.patch
Patch517: libvirt-virDomainDefParseXML-set-the-argument-of-virBitmapFree-to-NULL-after-calling-virBitmapFree.patch
Patch518: libvirt-tests-files-named-.-invalid.xml-should-fail-validation.patch
Patch519: libvirt-tests-use-portable-shell-code.patch
Patch520: libvirt-Add-test-for-the-nodemask-double-free-crash.patch
Patch521: libvirt-Fix-crash-in-remoteDispatchDomainMemoryStats.patch
Patch522: libvirt-Introduce-APIs-for-splitting-joining-strings.patch
Patch523: libvirt-Rename-virKillProcess-to-virProcessKill.patch
Patch524: libvirt-Rename-virPid-Abort-Wait-to-virProcess-Abort-Wait.patch
Patch525: libvirt-Rename-virCommandTranslateStatus-to-virProcessTranslateStatus.patch
Patch526: libvirt-Move-virProcessKill-into-virprocess.-h-c.patch
Patch527: libvirt-Move-virProcess-Kill-Abort-TranslateStatus-into-virprocess.-c-h.patch
Patch528: libvirt-Include-process-start-time-when-doing-polkit-checks.patch
Patch529: libvirt-Add-support-for-using-3-arg-pkcheck-syntax-for-process.patch
Patch530: libvirt-qemu-Fix-seamless-SPICE-migration.patch
Patch531: libvirt-libvirt-guests-status-return-non-zero-when-stopped.patch
Patch532: libvirt-qemu-Drop-qemuDomainMemoryLimit.patch
Patch533: libvirt-docs-Discourage-users-to-set-hard_limit.patch
Patch534: libvirt-docs-Clean-09adfdc62de2b-up.patch
Patch535: libvirt-qemuSetupMemoryCgroup-Handle-hard_limit-properly.patch
Patch536: libvirt-qemuBuildCommandLine-Fall-back-to-mem-balloon-if-there-s-no-hard_limit.patch
Patch537: libvirt-virNetDevBandwidthEqual-Make-it-more-robust.patch
Patch538: libvirt-qemu_hotplug-Allow-QoS-update-in-qemuDomainChangeNet.patch
Patch539: libvirt-qemu-generate-correct-name-for-hostdev-network-devices.patch
Patch540: libvirt-Fix-race-in-starting-transient-VMs.patch
Patch541: libvirt-qemuDomainDestroyFlags-Don-t-allow-vm-to-disappear-while-executing-API.patch
Patch542: libvirt-python-return-dictionary-without-value-in-case-of-no-blockjob.patch
Patch543: libvirt-remote-fix-regression-in-event-deregistration.patch
Patch544: libvirt-Add-virtio-scsi-to-fallback-models-of-scsi-controller.patch
Patch545: libvirt-qemu-Avoid-operations-on-NULL-monitor-if-VM-fails-early.patch
Patch546: libvirt-qemu-Do-not-access-stale-data-in-virDomainBlockStats.patch
Patch547: libvirt-qemu-Avoid-using-stale-data-in-virDomainGetBlockInfo.patch
Patch548: libvirt-qemu-Fix-job-usage-in-qemuDomainBlockJobImpl.patch
Patch549: libvirt-qemu-Fix-job-usage-in-qemuDomainBlockCopy.patch
Patch550: libvirt-qemu-Fix-job-usage-in-virDomainGetBlockIoTune.patch
Patch551: libvirt-Don-t-crash-if-a-connection-closes-early.patch
Patch552: libvirt-Really-don-t-crash-if-a-connection-closes-early.patch
Patch553: libvirt-Block-info-query-Add-check-for-transient-domain.patch
Patch554: libvirt-network-only-prevent-forwarding-of-DNS-requests-for-unqualified-names.patch
Patch555: libvirt-network-change-default-of-forwardPlainNames-to-yes.patch
Patch556: libvirt-sanlock-Truncate-domain-names-longer-than-SANLK_NAME_LEN.patch
Patch557: libvirt-Remove-contiguous-CPU-indexes-assumption.patch
Patch558: libvirt-qemu-monitor-Fix-error-message-and-comment-when-getting-cpu-info.patch
Patch559: libvirt-qemu-monitor-Filter-out-thread-ids-of-CPUS-that-were-unplugged.patch
Patch560: libvirt-qemu-monitor-Fix-invalid-parentheses.patch
Patch561: libvirt-virNetClientSetTLSSession-Restore-original-signal-mask.patch
Patch562: libvirt-doc-schema-Add-basic-documentation-for-the-virtual-RNG-device-support.patch
Patch563: libvirt-conf-Add-support-for-RNG-device-configuration-in-XML.patch
Patch564: libvirt-conf-Add-RNG-device-ABI-compatibility-check.patch
Patch565: libvirt-qemu-Implement-support-for-default-random-backend-for-virtio-rng.patch
Patch566: libvirt-qemu-Implement-support-for-EGD-backend-for-virtio-rng.patch
Patch567: libvirt-docs-domain-dev-urandom-isn-t-a-valid-rng-patch.patch
Patch568: libvirt-tests-Add-tests-for-virtio-rng-device-handling.patch
Patch569: libvirt-docs-Fix-attribute-name-for-virtio-rng-backend.patch
Patch570: libvirt-rng-restrict-passthrough-names-to-known-good-files.patch
Patch571: libvirt-Resolve-valgrind-error.patch
Patch572: libvirt-Fix-crash-parsing-RNG-device-specification.patch
Patch573: libvirt-rng-allow-default-device-in-RNG-grammar.patch
Patch574: libvirt-virtio-rng-Add-rate-limiting-options-for-virtio-RNG.patch
Patch575: libvirt-qemu_caps-Enable-virtio-rng-for-RHEL-6.6-qemu-kvm-downstream.patch
Patch576: libvirt-audit-Audit-resources-used-by-VirtIO-RNG.patch
Patch577: libvirt-virtio-rng-Remove-double-space-in-error-message.patch
Patch578: libvirt-doc-fix-XML-for-the-RNG-device-example.patch
Patch579: libvirt-conf-Don-t-crash-on-invalid-chardev-source-definition-of-RNGs-and-other.patch
Patch580: libvirt-conf-Fix-XML-formatting-of-RNG-device-info.patch
Patch581: libvirt-libvirt-fix-error-message-when-connection-can-t-be-opened.patch
Patch582: libvirt-conf-fix-error-for-parallel-port-mismatch.patch
Patch583: libvirt-virsh-clarify-vol-down-up-load-description.patch
Patch584: libvirt-virsh-fix-doc-typos.patch
Patch585: libvirt-util-use-string-libvirt-to-prefix-error-message-instead-of-libvir.patch
Patch586: libvirt-docs-use-MiB-s-instead-of-Mbps-for-migration-speed.patch
Patch587: libvirt-schema-require-target-path-in-storage-pool-xml.patch
Patch588: libvirt-schema-make-source-optional-in-volume-XML.patch
Patch589: libvirt-Add-qxl-ram-size-to-ABI-stability-check.patch
Patch590: libvirt-qemu-fix-default-spice-password-setting.patch
Patch591: libvirt-Expose-ownership-ID-parsing.patch
Patch592: libvirt-Make-qemuOpenFile-aware-of-per-VM-DAC-seclabel.patch
Patch593: libvirt-Use-qemuOpenFile-in-qemu_driver.c.patch
Patch594: libvirt-virsh-Fix-heading-in-manpage.patch
Patch595: libvirt-qemu-Change-the-default-unix-monitor-timeout.patch
Patch596: libvirt-qemu-fix-live-pinning-to-memory-node-on-NUMA-system.patch
Patch597: libvirt-qemu-Clean-up-qemuDomainSetNumaParameters.patch
Patch598: libvirt-virsh-snapshot-Reject-no-metadata-together-with-print-xml.patch
Patch599: libvirt-snapshot-Mention-disk-only-snapshots-in-error-message.patch
Patch600: libvirt-qemu-snapshot-Report-better-error-message-if-migration-isn-t-allowed.patch
Patch601: libvirt-qemu-snapshot-Remove-memory-image-if-external-checkpoint-fails.patch
Patch602: libvirt-virsh-snapshot-Fix-XPath-query-to-determine-snapshot-state.patch
Patch603: libvirt-conf-Check-if-number-of-vCPUs-fits-in-the-storage-variable.patch
Patch604: libvirt-conf-Improve-error-messages-if-parsing-of-vCPU-count-fails.patch
Patch605: libvirt-qemu-snapshot-Don-t-kill-access-to-disk-if-snapshot-creation-fails.patch
Patch606: libvirt-qemu-Un-mark-volume-as-mirrored-copied-if-blockjob-copy-fails.patch
Patch607: libvirt-qemu-blockjob-Fix-limit-of-bandwidth-for-block-jobs-to-supported-value.patch
Patch608: libvirt-virsh-Fix-typo-in-docs.patch
Patch609: libvirt-virsh-domain-Report-errors-on-invalid-holdtime-value-for-cmdSendKey.patch
Patch610: libvirt-qemu-Don-t-update-count-of-vCPUs-if-hot-plug-fails-silently.patch
Patch611: libvirt-virsh-man-Mention-that-volumes-need-to-be-in-storage-pool-for-undefine.patch
Patch612: libvirt-Disable-nwfilter-driver-when-running-unprivileged.patch
Patch613: libvirt-storage-reduce-number-of-stat-calls.patch
Patch614: libvirt-Ignore-missing-files-on-pool-refresh.patch
Patch615: libvirt-sanlock-add-missing-test-command-in-virt-sanlock-cleanup.in.patch
Patch616: libvirt-virt-sanlock-cleanup-Fix-augtool-usage.patch
Patch617: libvirt-conf-Fix-typo-in-error-message-in-ABI-stability-check.patch
Patch618: libvirt-qemu-Improve-error-when-setting-invalid-count-of-vcpus-via-agent.patch
Patch619: libvirt-doc-Clarify-usage-of-SELinux-baselabel.patch
Patch620: libvirt-selinux-Don-t-mask-errors-of-virSecuritySELinuxGenNewContext.patch
Patch621: libvirt-qemu-Return-meaningful-error-when-qemu-dies-early.patch
Patch622: libvirt-sanlock-Forbid-VIR_DOMAIN_LOCK_FAILURE_IGNORE.patch
Patch623: libvirt-Remove-the-redundant-parentheses-in-migrate-help.patch
Patch624: libvirt-virt-xml-validate-add-missing-schemas.patch
Patch625: libvirt-tools-add-missing-interface-type-and-update-man-page.patch
Patch626: libvirt-qemu-Don-t-require-a-block-or-file-when-looking-for-an-alias.patch
Patch627: libvirt-virDomainReboot-Document-that-migration-might-be-unsafe.patch
Patch628: libvirt-interface-list-all-interfaces-with-flags-0.patch
Patch629: libvirt-Fix-the-syntax-check-failure.patch
Patch630: libvirt-Crash-of-libvirtd-by-unprivileged-user-in-virConnectListAllInterfaces.patch
Patch631: libvirt-qemuDomainObjStart-Warn-on-corrupted-image.patch
Patch632: libvirt-QoS-make-tc-filters-match-all-traffic.patch
Patch633: libvirt-conf-add-support-for-booting-from-redirected-USB-devices.patch
Patch634: libvirt-Add-redirdevs-to-ABI-stability-check.patch
Patch635: libvirt-Fix-incorrect-values-in-redirdev-ABI-check-error.patch
Patch636: libvirt-virSecurityLabelDefParseXML-Don-t-parse-label-on-model-none.patch
Patch637: libvirt-storage-Skip-inactive-lv-volumes.patch
Patch638: libvirt-Check-for-existence-of-interface-prior-to-setting-terminate-flag.patch
Patch639: libvirt-storage-Avoid-forward-declaration-of-virStorageVolDelete.patch
Patch640: libvirt-storage-Don-t-update-pool-available-allocation-if-buildVol-fails.patch
Patch641: libvirt-conf-Report-errors-on-cputune-parameter-parsing.patch
Patch642: libvirt-Treat-zero-cpu-shares-as-a-valid-value.patch
Patch643: libvirt-Show-the-real-cpu-shares-value-in-live-XML.patch
Patch644: libvirt-nwfilter-Remove-error-report-in-virNWFilterDHCPSnoopEnd.patch
Patch645: libvirt-conf-introduce-generic-ISA-address.patch
Patch646: libvirt-conf-add-support-for-panic-device.patch
Patch647: libvirt-qemu-add-support-for-device-pvpanic.patch
Patch648: libvirt-PanicCheckABIStability-Need-to-check-for-existence.patch
Patch649: libvirt-use-virBitmapFree-instead-of-VIR_FREE-for-cpumask.patch
Patch650: libvirt-Properly-free-vcpupin-info-for-unplugged-CPUs.patch
Patch651: libvirt-Save-domain-status-after-cpu-hotplug.patch
Patch652: libvirt-Document-behavior-of-setvcpus-during-guest-boot.patch
Patch653: libvirt-qemu-Use-maximum-guest-memory-size-when-getting-NUMA-placement-advice.patch
Patch654: libvirt-qemu-Properly-format-the-uuid-string-in-error-messages.patch
Patch655: libvirt-qemu-Split-out-code-to-generate-SPICE-command-line.patch
Patch656: libvirt-qemu-Improve-handling-of-channels-when-generating-SPICE-command-line.patch
Patch657: libvirt-qemu-Split-out-SPICE-port-allocation-into-a-separate-function.patch
Patch658: libvirt-qemu-Do-sensible-auto-allocation-of-SPICE-port-numbers.patch
Patch659: libvirt-qemu-fix-failure-to-start-with-spice-graphics-and-no-tls.patch
Patch660: libvirt-qemu-Do-not-ignore-address-for-USB-disks.patch
Patch661: libvirt-qemu-pass-usb-and-usb-hubs-earlier-so-USB-disks-with-static-address-are-handled-properly.patch
Patch662: libvirt-qemu-refactor-qemuDomainCheckDiskPresence-for-only-disk-presence-check.patch
Patch663: libvirt-qemu-add-helper-functions-for-diskchain-checking.patch
Patch664: libvirt-qemu-check-presence-of-each-disk-and-its-backing-file-as-well.patch
Patch665: libvirt-conf-add-startupPolicy-attribute-for-harddisk.patch
Patch666: libvirt-qemu-support-to-drop-disk-with-optional-startupPolicy.patch
Patch667: libvirt-qemu-Avoid-overflow-when-setting-migration-speed.patch
Patch668: libvirt-qemu-Avoid-overflow-when-setting-migration-speed-on-inactive-domains.patch
Patch669: libvirt-caps-Add-helpers-to-convert-NUMA-nodes-to-corresponding-CPUs.patch
Patch670: libvirt-qemu-Set-cpuset.cpus-for-domain-process.patch
Patch671: libvirt-qemu-Unbreak-p2p-migration-with-complete-migration-URI.patch
Patch672: libvirt-maint-don-t-lose-error-on-canceled-migration.patch
Patch673: libvirt-virsh-suppress-aliases-in-group-help.patch
Patch674: libvirt-qemu-export-disk-snapshot-support-in-capabilities.patch
Patch675: libvirt-qemu-extract-guest-capabilities-initialization.patch
Patch676: libvirt-qemu-add-unit-tests-for-the-capabilities-xml.patch
Patch677: libvirt-qemu-properly-quit-migration-with-abort_on_error.patch
Patch678: libvirt-conf-restrict-external-snapshots-to-backing-store-formats.patch
Patch679: libvirt-qemu-don-t-check-for-backing-chains-for-formats-w-o-snapshot-support.patch
Patch680: libvirt-qemu-don-t-call-virFileExists-for-network-type-disks.patch
Patch681: libvirt-net-Change-argument-type-of-virNetworkObjIsDuplicate.patch
Patch682: libvirt-net-Move-creation-of-dnsmasq-hosts-file-to-function-starting-dnsmasq.patch
Patch683: libvirt-net-Re-use-checks-when-creating-transient-networks.patch
Patch684: libvirt-network-prevent-a-few-invalid-configuration-combinations.patch
Patch685: libvirt-network-disallow-bandwidth-mac-for-bridged-macvtap-hostdev-networks.patch
Patch686: libvirt-virsh-domain-Fix-cmdSetvcpus-error-message.patch
Patch687: libvirt-spice-detect-if-qemu-can-disable-file-transfer.patch
Patch688: libvirt-spice-expose-the-QEMU-disable-file-transfer-option.patch
Patch689: libvirt-qemu_caps-detect-if-qemu-can-disable-file-transfer-for-spice.patch
Patch690: libvirt-Device-Attach-Detach-Document-S4-limitations.patch
Patch691: libvirt-storageVolCreateXMLFrom-Allow-multiple-accesses-to-origvol.patch
Patch692: libvirt-LSN-2014-0003-Don-t-expand-entities-when-parsing-XML.patch
Patch693: libvirt-virSecuritySELinuxSetFileconHelper-Don-t-fail-on-read-only-NFS.patch
Patch694: libvirt-storage-Resolve-issues-in-failure-path.patch
Patch695: libvirt-interface-Introduce-netcfInterfaceObjIsActive.patch
Patch696: libvirt-interface-dump-inactive-xml-when-interface-isn-t-active.patch
Patch697: libvirt-qemu-add-host-pci-multidomain-capability.patch
Patch698: libvirt-qemu-specify-domain-in-host-side-PCI-addresses-when-needed-supported.patch
Patch699: libvirt-util-fix-virFileOpenAs-return-value-and-resulting-error-logs.patch
Patch700: libvirt-qemu-check-actual-netdev-type-rather-than-config-netdev-type-during-init.patch
Patch701: libvirt-Fix-parsing-of-bond-interface-XML.patch
Patch702: libvirt-qemuSetupCgroup-Fix-reference-to-cgroup.patch
Patch703: libvirt-apibuild-Disallow-returns-return-decription.patch
Patch704: libvirt-ESX-Add-support-for-virtualHW-version-10.patch
Patch705: libvirt-storage-Ensure-qemu-img-resize-size-arg-is-a-512-multiple.patch
Patch706: libvirt-qemu-Adjust-size-for-qcow2-qed-if-not-on-sector-boundary.patch
Patch707: libvirt-sanlock-code-movement-in-virLockManagerSanlockAcquire.patch
Patch708: libvirt-sanlock-don-t-fail-with-unregistered-domains.patch
Patch709: libvirt-sanlock-avoid-leak-in-acquire.patch
Patch710: libvirt-networkStartNetwork-Be-more-verbose.patch
Patch711: libvirt-network_conf-Expose-virNetworkDefFormatInternal.patch
Patch712: libvirt-Avoid-crash-when-LXC-start-fails-with-no-interface-target.patch
Patch713: libvirt-lxc_process-Avoid-passing-NULL-iface-iname.patch
Patch714: libvirt-network-Introduce-network-hooks.patch
Patch715: libvirt-bridge_driver.h-Fix-build-without-network.patch
Patch716: libvirt-networkRunHook-Run-hook-only-if-possible.patch
Patch717: libvirt-conf-clarify-what-is-returned-for-actual-bandwidth-and-vlan.patch
Patch718: libvirt-conf-handle-null-pointer-in-virNetDevVlanFormat.patch
Patch719: libvirt-conf-make-virDomainNetDefFormat-a-public-function.patch
Patch720: libvirt-conf-re-situate-bandwidth-element-in-interface.patch
Patch721: libvirt-conf-new-function-virDomainActualNetDefContentsFormat.patch
Patch722: libvirt-Slightly-refactor-hostdev-parsing-formating.patch
Patch723: libvirt-conf-output-actual-netdev-status-in-interface-XML.patch
Patch724: libvirt-network-include-plugged-interface-XML-in-plugged-network-hook.patch
Patch725: libvirt-network-don-t-even-call-networkRunHook-if-there-is-no-network.patch
Patch726: libvirt-udev-consider-the-device-a-CDROM-when-ID_CDROM-1.patch
Patch727: libvirt-Add-support-for-timestamping-QEMU-logs.patch
Patch728: libvirt-Detect-msg-timestamp-capability-from-QEMU-help-output.patch
Patch729: libvirt-qemu-Avoid-leak-in-qemuDomainCheckRemoveOptionalDisk.patch
Patch730: libvirt-Return-right-error-code-for-baselineCPU.patch
Patch731: libvirt-Add-a-port-allocator-class.patch
Patch732: libvirt-Avoid-integer-wrap-on-remotePortMax-in-QEMU-driver.patch
Patch733: libvirt-Followup-fix-for-integer-wraparound-in-port-allocator.patch
Patch734: libvirt-Don-t-spam-logs-with-port-0-must-be-in-range-errors.patch
Patch735: libvirt-qemu-Avoid-assigning-unavailable-migration-ports.patch
Patch736: libvirt-qemu-Make-migration-port-range-configurable.patch
Patch737: libvirt-qemu-Fix-augeas-support-for-migration-ports.patch
Patch738: libvirt-qemu-clean-up-migration-ports-when-migration-cancelled.patch
Patch739: libvirt-qemuDomainObjBeginJobInternal-Return-2-for-temporary-failures.patch
Patch740: libvirt-qemu-Make-qemuProcess-Start-Stop-CPUs-easier-to-follow.patch
Patch741: libvirt-qemu-Ignore-temporary-job-errors-when-checking-migration-status.patch
Patch742: libvirt-qemu-Send-migrate_cancel-when-aborting-migration.patch
Patch743: libvirt-remote-Don-t-leak-priv-tls-object-on-connection-failure.patch
Patch744: libvirt-Fix-invalid-read-in-virNetSASLSessionClientStep-debug-log.patch
Patch745: libvirt-Tie-SASL-callbacks-lifecycle-to-virNetSessionSASLContext.patch
Patch746: libvirt-fix-leak-in-memoryStats-with-older-python.patch
Patch747: libvirt-hooks-let-virCommand-do-the-error-reporting.patch
Patch748: libvirt-SELinux-don-t-fail-silently-when-no-label-is-present.patch
Patch749: libvirt-qemu-Add-qemuDomainReleaseDeviceAddress-to-remove-any-address.patch
Patch750: libvirt-qemu-Separate-disk-device-removal-into-a-standalone-function.patch
Patch751: libvirt-qemu-Separate-controller-removal-into-a-standalone-function.patch
Patch752: libvirt-qemu-Separate-net-device-removal-into-a-standalone-function.patch
Patch753: libvirt-qemu-Separate-host-device-removal-into-a-standalone-function.patch
Patch754: libvirt-Add-VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED-event.patch
Patch755: libvirt-examples-Handle-VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED-event.patch
Patch756: libvirt-Clarify-virDomainDetachDeviceFlags-documentation.patch
Patch757: libvirt-Add-virDomainDefFindDevice-for-looking-up-a-device-by-its-alias.patch
Patch758: libvirt-qemu-Add-support-for-DEVICE_DELETED-event.patch
Patch759: libvirt-qemu-Remove-devices-only-after-DEVICE_DELETED-event.patch
Patch760: libvirt-qemu-Emit-VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED-events.patch
Patch761: libvirt-Add-function-to-find-a-needle-in-a-string-array.patch
Patch762: libvirt-util-Non-existent-string-array-does-not-contain-any-string.patch
Patch763: libvirt-conf-Make-error-reporting-in-virDomainDefFindDevice-optional.patch
Patch764: libvirt-qemu-Introduce-qemuMonitorGetDeviceAliases.patch
Patch765: libvirt-qemu-Unplug-devices-that-disappeared-when-libvirtd-was-down.patch
Patch766: libvirt-qemu-Finish-device-removal-in-the-original-thread.patch
Patch767: libvirt-qemu-Process-DEVICE_DELETED-event-in-a-separate-thread.patch
Patch768: libvirt-qemu-Remove-interface-backend-only-after-frontend-is-gone.patch
Patch769: libvirt-qemu-Remove-disk-backend-only-after-frontend-is-gone.patch
Patch770: libvirt-qemu-Return-in-from-qemuDomainRemove-Device.patch
Patch771: libvirt-Fix-crash-when-saving-a-domain-with-type-none-dac-label.patch
Patch772: libvirt-Initialize-threading-error-layer-in-LXC-controller.patch
Patch773: libvirt-formatdomain.html.in-Document-implementation-limitation-of-QoS.patch
Patch774: libvirt-Fix-error-in-qemuDomainSetNumaParamsLive.patch
Patch775: libvirt-cpu-Add-new-Broadwell-CPU-model.patch
Patch776: libvirt-docs-publish-correct-enum-values.patch
Patch777: libvirt-qemu-blockcopy-Don-t-remove-existing-disk-mirror-info.patch
Patch778: libvirt-qemu-fix-guestfwd-chardev-option-back-how-it-was.patch
Patch779: libvirt-Add-invariant-TSC-cpu-flag.patch
Patch780: libvirt-Fix-segfault-when-starting-a-domain-with-no-cpu-definition.patch
Patch781: libvirt-qemu-copy-Accept-format-parameter-when-copying-to-a-non-existing-img.patch
Patch782: libvirt-Bind-connection-close-callback-APIs-to-python-binding.patch
Patch783: libvirt-qemu-Factor-out-body-of-qemuDomainGetMetadata-for-universal-use.patch
Patch784: libvirt-qemu-Factor-out-body-of-qemuDomainSetMetadata-for-universal-use.patch
Patch785: libvirt-conf-Factor-out-setting-of-metadata-to-simplify-code.patch
Patch786: libvirt-util-Add-helper-to-convert-libxml2-nodes-to-a-string.patch
Patch787: libvirt-conf-Add-support-for-requesting-of-XML-metadata-via-the-API.patch
Patch788: libvirt-conf-allow-to-add-XML-metadata-using-the-virDomainSetMetadata-api.patch
Patch789: libvirt-conf-Avoid-false-positive-of-uninitialized-variable-use.patch
Patch790: libvirt-lib-Don-t-force-the-key-argument-when-deleting-metadata.patch
Patch791: libvirt-test-Add-metadata-support-into-the-test-drivera.patch
Patch792: libvirt-tests-Add-metadata-tests.patch
Patch793: libvirt-conf-Don-t-corrupt-metadata-on-OOM.patch
Patch794: libvirt-Ignore-additional-fields-in-iscsiadm-output.patch
Patch795: libvirt-conf-net-Fix-helper-for-applying-new-network-definition.patch
Patch796: libvirt-blockjob-wait-for-pivot-to-complete.patch
Patch797: libvirt-virsh-Introduce-macros-to-reject-mutually-exclusive-arguments.patch
Patch798: libvirt-virsh-domain-Add-live-config-current-logic-to-cmdAttachDisk.patch
Patch799: libvirt-virsh-domain-Add-live-config-current-logic-to-cmdDetachDevice.patch
Patch800: libvirt-virsh-domain-Add-live-config-current-logic-to-cmdDetachDisk.patch
Patch801: libvirt-virsh-Use-inactive-definition-when-removing-disk-from-config.patch
Patch802: libvirt-virsh-domain-Add-live-config-current-logic-to-cmdAttachDevice.patch
Patch803: libvirt-conf-Fix-backport-of-metadata-API-code.patch
Patch804: libvirt-conf-Always-format-seclabel-s-model.patch
Patch805: libvirt-Fix-blkdeviotune-for-shutoff-domain.patch
Patch806: libvirt-rpc-message-related-sizes-enlarged.patch
Patch807: libvirt-Increase-the-size-of-REMOTE_MIGRATE_COOKIE_MAX-to-REMOTE_STRING_MAX.patch
Patch808: libvirt-Fix-max-stream-packet-size-for-old-clients.patch
Patch809: libvirt-Adjust-legacy-max-payload-size-to-account-for-header-information.patch
Patch810: libvirt-rpc-Correct-the-wrong-payload-size-checking.patch
Patch811: libvirt-network-make-networkCreateInterfacePool-more-robust.patch
Patch812: libvirt-metadata-track-title-edits-across-libvirtd-restart.patch
Patch813: libvirt-cpu-separate-host-model-and-host-passthrough.patch
Patch814: libvirt-Don-t-include-non-migratable-features-in-host-model.patch
Patch815: libvirt-Don-t-add-dhcp-hosts-to-hostsfile-twice.patch
Patch816: libvirt-Revert-qemu-export-disk-snapshot-support-in-capabilities.patch
Patch817: libvirt-qemu-allow-restore-with-non-migratable-XML-input.patch
Patch818: libvirt-qemu-Introduce-qemuDomainDefCheckABIStability.patch
Patch819: libvirt-Make-ABI-stability-issue-easier-to-debug.patch
Patch820: libvirt-domain_conf-fix-domain-deadlock.patch
Patch821: libvirt-CVE-2014-3633-qemu-blkiotune-Use-correct-definition-when-looking-up-disk.patch
Patch822: libvirt-CVE-2014-7823-dumpxml-security-hole-with-migratable-flag.patch
Patch823: libvirt-sanlock-Avoid-freeing-uninitialized-value.patch
Patch824: libvirt-virsh-Print-cephx-and-iscsi-usage.patch
Patch825: libvirt-Fix-bug-with-loading-bridge-name-for-active-domain-during-libvirtd-start.patch
Patch826: libvirt-conf-Fix-even-implicit-labels.patch
Patch827: libvirt-tests-Add-test-cases-for-previous-commit.patch
Patch828: libvirt-networkValidate-Disallow-bandwidth-in-portgroups-too.patch
Patch829: libvirt-qemu-Fix-checking-of-ABI-stability-when-restoring-external-checkpoints.patch
Patch830: libvirt-qemu-Use-migratable-XML-definition-when-doing-external-checkpoints.patch
Patch831: libvirt-qemu-Fix-memleak-after-commit-59898a88ce8431bd3ea249b8789edc2ef9985827.patch
Patch832: libvirt-qemu-blkiotune-Avoid-accessing-non-existing-disk-configuration.patch
Patch833: libvirt-qemu-Fix-build-error-introduced-in-653137eb957a278b556c6226424aad5395a.patch
Patch834: libvirt-qemu-snapshot-Use-better-check-when-reverting-external-snapshots.patch
Patch835: libvirt-virsh-domain-Use-global-constant-for-XML-file-size-limit.patch
Patch836: libvirt-selinux-Avoid-label-reservations-for-type-none.patch
Patch837: libvirt-Clean-up-chardev-sockets-on-QEMU-shutdown.patch
Patch838: libvirt-Don-t-include-LIBS-in-libvirt.pc.in-file.patch
Patch839: libvirt-qemu-save-domain-state-to-XML-after-reboot.patch
Patch840: libvirt-virsh-Honour-q-in-domblklist-vcpupin-and-emulatorpin.patch
Patch841: libvirt-virsh-domain-Flip-logic-in-cmdSetvcpus.patch
Patch842: libvirt-Fix-possible-memory-leak-in-util-virxml.c.patch
Patch843: libvirt-esx_vi-fix-possible-segfault.patch
Patch844: libvirt-sasl-Fix-authentication-when-using-PLAIN-mechanism.patch
Patch845: libvirt-Fix-leak-in-x86UpdateHostModel.patch
Patch846: libvirt-nwfilter-utility-function-virNWFilterVarValueEqual.patch
Patch847: libvirt-qemu-support-live-update-of-an-interface-s-filter.patch
Patch848: libvirt-qemu-Update-fsfreeze-status-on-domain-state-transitions.patch
Patch849: libvirt-virsh-Fix-semantics-of-config-for-update-device-command.patch
Patch850: libvirt-virsh-Don-t-use-legacy-API-if-current-is-used-on-device-hot-un-plug.patch
Patch851: libvirt-qemu-Avoid-double-serial-output-with-RHEL-6-qemu.patch
Patch852: libvirt-storage-Check-the-partition-name-against-provided-name.patch
Patch853: libvirt-qemu-Don-t-unconditionally-delete-file-in-qemuOpenFileAs.patch
Patch854: libvirt-conf-Don-t-mangle-vcpu-placement-randomly.patch
Patch855: libvirt-conf-Don-t-format-actual-network-definition-in-migratable-XML.patch
Patch856: libvirt-network-don-t-allow-multiple-portgroups-with-the-same-name-in-a-network.patch
Patch857: libvirt-build-fix-build-with-latest-rawhide-kernel-headers.patch
Patch858: libvirt-sanlock-Don-t-spam-logs-with-target-pid-not-found.patch
Patch859: libvirt-nwfilter-fix-crash-when-adding-non-existing-nwfilter.patch
Patch860: libvirt-util-more-verbose-error-when-failing-to-create-macvtap-device.patch
Patch861: libvirt-qemu-Keep-QEMU-host-drive-prefix-in-BlkIoTune.patch
Patch862: libvirt-qemu-Fix-name-comparison-in-qemuMonitorJSONBlockIoThrottleInfo.patch
Patch863: libvirt-virsh-fix-typos-in-virsh-man-page.patch
Patch864: libvirt-schemas-Allow-all-generic-elements-and-attributes-for-all-interfaces.patch
Patch865: libvirt-RNG-Allow-multiple-parameters-to-be-passed-to-an-interface-filter.patch
Patch866: libvirt-qemu_domain-fix-startup-policy-for-disks.patch
Patch867: libvirt-Create-directory-for-lease-files-if-it-s-missing.patch
Patch868: libvirt-qemu-cgroup-Properly-set-up-vcpu-pinning.patch
Patch869: libvirt-cgroup-Add-accessors-for-cpuset.memory_migrate.patch
Patch870: libvirt-qemu-Fix-possible-crash.patch
Patch871: libvirt-qemu-Migrate-memory-on-numatune-change.patch
Patch872: libvirt-qemu-fix-crash-when-removing-filterref-from-interface-with-update-device.patch
Patch873: libvirt-nwfilter-Fix-rule-priority-problem.patch
Patch874: libvirt-qemuProcessHook-Call-qemuProcessInitNumaMemoryPolicy-only-when-needed.patch
Patch875: libvirt-RHEL-Avoid-memory-leak-when-virCgroupSetCpusetMemoryMigrate-fails.patch
Patch876: libvirt-qemu-cgroup-Fix-memory-leak-when-there-s-no-vCPU-pinning.patch
Patch877: libvirt-util-set-MAC-address-for-VF-via-netlink-message-to-PF-VF-when-possible.patch
Patch878: libvirt-util-set-macvtap-physdev-online-when-macvtap-is-set-online.patch
Patch879: libvirt-daemon-Suppress-logging-of-VIR_ERR_NO_DOMAIN_METADATA.patch
Patch880: libvirt-Allow-source-for-type-block-to-have-no-dev.patch
Patch881: libvirt-qemu-event-Properly-handle-spice-events.patch
Patch882: libvirt-qemu-event-Clean-up-VNC-monitor-handling.patch
Patch883: libvirt-qemu-split-out-cpuset.mems-setting.patch
Patch884: libvirt-qemu-leave-restricting-cpuset.mems-after-initialization.patch
Patch885: libvirt-virNetDev-Replace-Restore-MacAddress-Fix-memory-leak.patch
Patch886: libvirt-util-make-virNetDev-Replace-Restore-MacAddress-public-functions.patch
Patch887: libvirt-util-don-t-use-netlink-to-save-set-mac-for-macvtap-passthrough-802.1Qbh.patch
Patch888: libvirt-qemu-fix-hotplugging-cpus-with-strict-memory-pinning.patch
Patch889: libvirt-storage-Track-successful-creation-of-LV-for-removal.patch
Patch890: libvirt-qemu-snapshot-Fix-return-value-of-external-checkpoint-with-no-disks.patch
Patch891: libvirt-qemu-snapshot-Fix-modification-of-vm-object-without-job.patch
Patch892: libvirt-virsh-domain-Add-live-config-current-logic-to-cmdAttachInterface.patch
Patch893: libvirt-RHEL-virsh-remove-duplicate-config-for-virsh-update-device.patch
Patch894: libvirt-Update-ESX-driver-to-always-use-privateData.patch
Patch895: libvirt-esx-Simplify-VI-vSphere-API-and-VMware-product-version-handling.patch
Patch896: libvirt-conf-net-Correctly-switch-how-to-format-address-fields.patch
Patch897: libvirt-qemu-Refuse-to-create-snapshot-of-a-disk-without-source.patch
Patch898: libvirt-Build-all-binaries-with-PIE.patch
Patch899: libvirt-Enable-full-RELRO-mode.patch
Patch900: libvirt-Don-t-duplicate-compiler-warning-flags-when-linking.patch
Patch901: libvirt-Simplify-RELRO_LDFLAGS.patch
Patch902: libvirt-Fix-AM_LDFLAGS-typo.patch
Patch903: libvirt-Pass-AM_LDFLAGS-to-driver-modules-too.patch
Patch904: libvirt-RHEL-Enable-RELRO-for-python-modules.patch
Patch905: libvirt-vmx-Relax-virtualHW.version-check.patch
Patch906: libvirt-qemu-snapshot-Don-t-leak-XML-definition-and-forget-to-unlock-job.patch
Patch907: libvirt-qemu-Fix-formatting-flags-in-qemuDomainSaveImageOpen.patch
Patch908: libvirt-network-Resolve-some-issues-around-vlan-copying.patch
Patch909: libvirt-network-fix-connections-count-in-case-of-allocate-failure.patch
Patch910: libvirt-network-consolidate-connection-count-updates-for-device-pool.patch
Patch911: libvirt-network-consolidated-info-log-for-all-network-allocate-free-operations.patch
Patch912: libvirt-util-increase-libnl-buffer-size.patch
Patch913: libvirt-util-reduce-debug-log-in-virPCIGetVirtualFunctions.patch
Patch914: libvirt-util-improve-error-reporting-in-virNetDevVPortProfileGetStatus.patch
Patch915: libvirt-util-add-missing-newline.patch
Patch916: libvirt-util-eliminate-bogus-error-log-in-virNetDevVPortProfileGetStatus.patch
Patch917: libvirt-util-clean-up-and-expand-802.1QbX-negotiation-logging.patch
Patch918: libvirt-util-report-the-MAC-address-that-couldn-t-be-set.patch
Patch919: libvirt-util-reset-MAC-address-of-macvtap-passthrough-physdev-after-disassociate.patch
Patch920: libvirt-bitmap-add-way-to-find-next-clear-bit.patch
Patch921: libvirt-Introduce-virBitmapIsBitSet.patch
Patch922: libvirt-util-Introduce-flags-field-for-macvtap-creation.patch
Patch923: libvirt-virnetdevmacvlan.c-Introduce-mutex-for-macvlan-creation.patch
Patch924: libvirt-util-keep-use-a-bitmap-of-in-use-macvtap-devices.patch
Patch925: libvirt-qemu-Don-t-compare-host-passthrough-CPU-to-host-CPU.patch
Patch926: libvirt-qemu-Always-format-model-for-host-model-CPUs.patch
Patch927: libvirt-util-avoid-getting-stuck-on-macvtapN-name-created-outside-libvirt.patch

Patch10001:   libvirt-VIR_ALLOC_N-causes-alignment-warnings.patch
Patch10002:   libvirt-Rewrite-keycode-map-to-avoid-a-struct.patch
Source10003:  libvirt-Avoid-casts-between-unsigned-char-and-struct-nlmsghdr.patch
Source10004:  libvirt-Disable-cast-align-warnings-in-various-places.patch
Patch10005:   libvirt-Minimal-CPU-parser-for-armhf.patch
Source10006:  libvirt-viratomic.patch

# All runtime requirements for the libvirt package (runtime requrements
# for subpackages are listed later in those subpackages)

# The client side, i.e. shared libs and virsh are in a subpackage
Requires: %{name}-client = %{version}-%{release}

# Used by many of the drivers, so turn it on whenever the
# daemon is present
%if %{with_libvirtd}
# for modprobe of pci devices
Requires: module-init-tools
# for /sbin/ip & /sbin/tc
Requires: iproute
%if %{with_avahi}
Requires: avahi-libs
%endif
%endif
%if %{with_network}
Requires: dnsmasq >= 2.41
Requires: radvd
%endif
%if %{with_network} || %{with_nwfilter}
Requires: iptables
Requires: iptables-ipv6
%endif
%if %{with_nwfilter}
Requires: ebtables
%endif
# needed for device enumeration
%if %{with_hal}
Requires: hal
%endif
%if %{with_udev}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
Requires: systemd >= 185
%else
Requires: udev >= 145
%endif
%endif
%if %{with_polkit}
%if 0%{?fedora} >= 12 || 0%{?rhel} >=6
# For CVE-2013-4311
Requires: polkit >= 0.96-5
%else
Requires: PolicyKit >= 0.6
%endif
%endif
%if %{with_storage_fs}
Requires: nfs-utils
# For mkfs
Requires: util-linux-ng
# For pool-build probing for existing pools
BuildRequires: libblkid-devel >= 2.17
# For glusterfs
%if 0%{?fedora} >= 11
Requires: glusterfs-client >= 2.0.1
%endif
%endif
%if %{with_qemu}
# From QEMU RPMs
Requires: /usr/bin/qemu-img
# For image compression
Requires: gzip
Requires: bzip2
Requires: lzop
Requires: xz
%else
%if %{with_xen}
# From Xen RPMs
Requires: /usr/sbin/qcow-create
%endif
%endif
%if %{with_storage_lvm}
# For LVM drivers
Requires: lvm2
%endif
%if %{with_storage_iscsi}
# For ISCSI driver
Requires: iscsi-initiator-utils
%endif
%if %{with_storage_disk}
# For disk driver
Requires: parted
Requires: device-mapper
%endif
%if %{with_storage_mpath}
# For multipath support
Requires: device-mapper
%endif
%if %{with_storage_rbd}
# For RBD support
Requires: ceph
%endif
%if %{with_cgconfig}
Requires: libcgroup
%endif
%ifarch %{ix86} x86_64 ia64
# For virConnectGetSysinfo
Requires: dmidecode
%endif
# For service management
%if %{with_systemd}
Requires(post): systemd-units
Requires(post): systemd-sysv
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif
%if %{with_numad}
Requires: numad
%endif
# libvirtd depends on 'messagebus' service
Requires: dbus

# All build-time requirements
BuildRequires: git
%if 0%{?enable_autotools}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
%endif
BuildRequires: python-devel
%if %{with_systemd}
BuildRequires: systemd-units
%endif
%if %{with_xen}
BuildRequires: xen-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: xhtml1-dtds
BuildRequires: libxslt
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: gettext
BuildRequires: libtasn1-devel
BuildRequires: gnutls-devel
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
# for augparse, optionally used in testing
BuildRequires: augeas
%endif
%if %{with_hal}
BuildRequires: hal-devel
%endif
%if %{with_udev}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires: systemd-devel >= 185
%else
BuildRequires: libudev-devel >= 145
%endif
BuildRequires: libpciaccess-devel >= 0.10.9
%endif
%if %{with_yajl}
BuildRequires: yajl-devel
%endif
%if %{with_sanlock}
# make sure libvirt is built with new enough sanlock on
# distros that have it; required for on_lockfailure
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
BuildRequires: sanlock-devel >= 2.4
%else
BuildRequires: sanlock-devel >= 1.8
%endif
%endif
%if %{with_libpcap}
BuildRequires: libpcap-devel
%endif
%if %{with_libnl}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires: libnl3-devel
%else
BuildRequires: libnl-devel
%endif
%endif
%if %{with_avahi}
BuildRequires: avahi-devel
%endif
%if %{with_selinux}
BuildRequires: libselinux-devel
%endif
%if %{with_network}
BuildRequires: dnsmasq >= 2.41
BuildRequires: iptables
BuildRequires: iptables-ipv6
BuildRequires: radvd
%endif
%if %{with_nwfilter}
BuildRequires: ebtables
%endif
BuildRequires: module-init-tools
%if %{with_sasl}
BuildRequires: cyrus-sasl-devel
%endif
%if %{with_polkit}
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
# For CVE-2013-4311
BuildRequires: polkit-devel >= 0.96-5
%else
BuildRequires: PolicyKit-devel >= 0.6
%endif
%endif
%if %{with_storage_fs}
# For mount/umount in FS driver
BuildRequires: util-linux
%endif
%if %{with_qemu}
# From QEMU RPMs
BuildRequires: /usr/bin/qemu-img
%else
%if %{with_xen}
# From Xen RPMs
BuildRequires: /usr/sbin/qcow-create
%endif
%endif
%if %{with_storage_lvm}
# For LVM drivers
BuildRequires: lvm2
%endif
%if %{with_storage_iscsi}
# For ISCSI driver
BuildRequires: iscsi-initiator-utils
%endif
%if %{with_storage_disk}
# For disk driver
BuildRequires: parted-devel
%if 0%{?rhel} == 5
# Broken RHEL-5 parted RPM is missing a dep
BuildRequires: e2fsprogs-devel
%endif
%endif
%if %{with_storage_mpath}
# For Multipath support
%if 0%{?rhel} == 5
# Broken RHEL-5 packaging has header files in main RPM :-(
BuildRequires: device-mapper
%else
BuildRequires: device-mapper-devel
%endif
%if %{with_storage_rbd}
BuildRequires: ceph-devel
%endif
%endif
%if %{with_numactl}
# For QEMU/LXC numa info
BuildRequires: numactl-devel
%endif
%if %{with_capng}
BuildRequires: libcap-ng-devel >= 0.5.0
%endif
%if %{with_phyp} || %{with_libssh2_transport}
%if %{with_libssh2_transport}
BuildRequires: libssh2-devel >= 1.3.0
%else
BuildRequires: libssh2-devel
%endif
%endif

%if %{with_netcf}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires: netcf-devel >= 0.2.2
%else
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 6
BuildRequires: netcf-devel >= 0.1.8
%else
BuildRequires: netcf-devel >= 0.1.4
%endif
%endif
%endif
%if %{with_esx}
%if 0%{?fedora} >= 9 || 0%{?rhel} >= 6
BuildRequires: libcurl-devel
%else
BuildRequires: curl-devel
%endif
%endif
%if %{with_hyperv}
BuildRequires: libwsman-devel >= 2.2.3
%endif
%if %{with_audit}
BuildRequires: audit-libs-devel
%endif
%if %{with_dtrace}
# we need /usr/sbin/dtrace
BuildRequires: systemtap-sdt-devel
%endif

%if %{with_storage_fs}
# For mount/umount in FS driver
BuildRequires: util-linux
# For showmount in FS driver (netfs discovery)
BuildRequires: nfs-utils
%endif

%if %{with_firewalld}
# Communication with the firewall daemon uses DBus
BuildRequires: dbus-devel
%endif

# Fedora build root suckage
BuildRequires: gawk

# For storage wiping with different algorithms
BuildRequires: scrub

%if %{with_numad}
BuildRequires: numad
%endif

Provides: bundled(gnulib)

%description
Libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). The main package includes
the libvirtd server exporting the virtualization support.

%package client
Summary: Client side library and utilities of the libvirt library
Group: Development/Libraries
Requires: readline
Requires: ncurses
# So remote clients can access libvirt over SSH tunnel
# (client invokes 'nc' against the UNIX socket on the server)
Requires: nc
# Needed by libvirt-guests init script.
Requires: gettext
# Needed by virt-pki-validate script.
Requires: gnutls-utils
# Needed for probing the power management features of the host.
Requires: pm-utils
%if %{with_sasl}
Requires: cyrus-sasl
# Not technically required, but makes 'out-of-box' config
# work correctly & doesn't have onerous dependencies
Requires: cyrus-sasl-md5
%endif
%if %{with_libssh2_transport}
Requires: libssh2 >= 1.3.0
%endif

%description client
Shared libraries and client binaries needed to access to the
virtualization capabilities of recent versions of Linux (and other OSes).

%package devel
Summary: Libraries, includes, etc. to compile with the libvirt library
Group: Development/Libraries
Requires: %{name}-client = %{version}-%{release}
Requires: pkgconfig
%if %{with_xen}
Requires: xen-devel
%endif


%description devel
Includes and documentations for the C library providing an API to use
the virtualization capabilities of recent versions of Linux (and other OSes).

%if %{with_sanlock}
%package lock-sanlock
Summary: Sanlock lock manager plugin for QEMU driver
Group: Development/Libraries
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
Requires: sanlock >= 2.4
%else
Requires: sanlock >= 1.8
%endif
#for virt-sanlock-cleanup require augeas
Requires: augeas
Requires: %{name} = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}

%description lock-sanlock
Includes the Sanlock lock manager plugin for the QEMU
driver
%endif

%if %{with_python}
%package python
Summary: Python bindings for the libvirt library
Group: Development/Libraries
Requires: %{name}-client = %{version}-%{release}

%description python
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).
%endif

%prep
%setup -q

# Patches have to be stored in a temporary file because RPM has
# a limit on the length of the result of any macro expansion;
# if the string is longer, it's silently cropped
%{lua:
    tmp = os.tmpname();
    f = io.open(tmp, "w+");
    count = 0;
    for i, p in ipairs(patches) do
        f:write(p.."\n");
        count = count + 1;
    end;
    f:close();
    print("PATCHCOUNT="..count.."\n")
    print("PATCHLIST="..tmp.."\n")
}

git init -q
git config user.name rpm-build
git config user.email rpm-build
git config gc.auto 0
git add .
git commit -q -a --author 'rpm-build <rpm-build>' \
           -m '%{name}-%{version} base'

COUNT=$(grep '\.patch$' $PATCHLIST | wc -l)
if [ $COUNT -ne $PATCHCOUNT ]; then
    echo "Found $COUNT patches in $PATCHLIST, expected $PATCHCOUNT"
    exit 1
fi
if [ $COUNT -gt 0 ]; then
    xargs git am <$PATCHLIST || exit 1
fi
echo "Applied $COUNT patches"
rm -f $PATCHLIST
%ifarch %{arm}
cp %{SOURCE10003} .
patch -p0 < %{SOURCE10003}
cp %{SOURCE10004} .
patch -p0 < %{SOURCE10004}
cp %{SOURCE10006} .
patch -p0 < %{SOURCE10006}
%endif

%build
%if ! %{with_xen}
%define _without_xen --without-xen
%endif

%if ! %{with_qemu}
%define _without_qemu --without-qemu
%endif

%if ! %{with_openvz}
%define _without_openvz --without-openvz
%endif

%if ! %{with_lxc}
%define _without_lxc --without-lxc
%endif

%if ! %{with_vbox}
%define _without_vbox --without-vbox
%endif

%if ! %{with_xenapi}
%define _without_xenapi --without-xenapi
%endif

%if ! %{with_libxl}
%define _without_libxl --without-libxl
%endif

%if ! %{with_sasl}
%define _without_sasl --without-sasl
%endif

%if ! %{with_avahi}
%define _without_avahi --without-avahi
%endif

%if ! %{with_phyp}
%define _without_phyp --without-phyp
%endif

%if ! %{with_esx}
%define _without_esx --without-esx
%endif

%if ! %{with_hyperv}
%define _without_hyperv --without-hyperv
%endif

%if ! %{with_vmware}
%define _without_vmware --without-vmware
%endif

%if ! %{with_parallels}
%define _without_parallels --without-parallels
%endif

%if ! %{with_polkit}
%define _without_polkit --without-polkit
%endif

%if ! %{with_python}
%define _without_python --without-python
%endif

%if ! %{with_libvirtd}
%define _without_libvirtd --without-libvirtd
%endif

%if ! %{with_uml}
%define _without_uml --without-uml
%endif

%if %{with_rhel5}
%define _with_rhel5_api --with-rhel5-api
%endif

%if ! %{with_network}
%define _without_network --without-network
%endif

%if ! %{with_storage_fs}
%define _without_storage_fs --without-storage-fs
%endif

%if ! %{with_storage_lvm}
%define _without_storage_lvm --without-storage-lvm
%endif

%if ! %{with_storage_iscsi}
%define _without_storage_iscsi --without-storage-iscsi
%endif

%if ! %{with_storage_disk}
%define _without_storage_disk --without-storage-disk
%endif

%if ! %{with_storage_mpath}
%define _without_storage_mpath --without-storage-mpath
%endif

%if ! %{with_storage_rbd}
%define _without_storage_rbd --without-storage-rbd
%endif

%if ! %{with_storage_sheepdog}
%define _without_storage_sheepdog --without-storage-sheepdog
%endif

%if ! %{with_numactl}
%define _without_numactl --without-numactl
%endif

%if ! %{with_numad}
%define _without_numad --without-numad
%endif

%if ! %{with_capng}
%define _without_capng --without-capng
%endif

%if ! %{with_netcf}
%define _without_netcf --without-netcf
%endif

%if ! %{with_selinux}
%define _without_selinux --without-selinux
%endif

%if ! %{with_hal}
%define _without_hal --without-hal
%endif

%if ! %{with_udev}
%define _without_udev --without-udev
%endif

%if ! %{with_yajl}
%define _without_yajl --without-yajl
%endif

%if ! %{with_sanlock}
%define _without_sanlock --without-sanlock
%endif

%if ! %{with_libpcap}
%define _without_libpcap --without-libpcap
%endif

%if ! %{with_macvtap}
%define _without_macvtap --without-macvtap
%endif

%if ! %{with_audit}
%define _without_audit --without-audit
%endif

%if ! %{with_dtrace}
%define _without_dtrace --without-dtrace
%endif

%if ! %{with_driver_modules}
%define _without_driver_modules --without-driver-modules
%endif

%if %{with_firewalld}
%define _with_firewalld --with-firewalld
%endif

%define when  %(date +"%%F-%%T")
%define where %(hostname)
%define who   %{?packager}%{!?packager:Unknown}
%define with_packager --with-packager="%{who}, %{when}, %{where}"
%define with_packager_version --with-packager-version="%{release}"

%if %{with_systemd}
# We use 'systemd+redhat', so if someone installs upstart or
# legacy init scripts, they can still start libvirtd, etc
%define init_scripts --with-init_script=systemd+redhat
%else
%define init_scripts --with-init_script=redhat
%endif

%if 0%{?enable_autotools}
autoreconf -if
%endif
%configure %{?_without_xen} \
           %{?_without_qemu} \
           %{?_without_openvz} \
           %{?_without_lxc} \
           %{?_without_vbox} \
           %{?_without_libxl} \
           %{?_without_xenapi} \
           %{?_without_sasl} \
           %{?_without_avahi} \
           %{?_without_polkit} \
           %{?_without_python} \
           %{?_without_libvirtd} \
           %{?_without_uml} \
           %{?_without_phyp} \
           %{?_without_esx} \
           %{?_without_hyperv} \
           %{?_without_vmware} \
           %{?_without_parallels} \
           %{?_without_network} \
           %{?_with_rhel5_api} \
           %{?_without_storage_fs} \
           %{?_without_storage_lvm} \
           %{?_without_storage_iscsi} \
           %{?_without_storage_disk} \
           %{?_without_storage_mpath} \
           %{?_without_storage_rbd} \
           %{?_without_storage_sheepdog} \
           %{?_without_numactl} \
           %{?_without_numad} \
           %{?_without_capng} \
           %{?_without_netcf} \
           %{?_without_selinux} \
           %{?_without_hal} \
           %{?_without_udev} \
           %{?_without_yajl} \
           %{?_without_sanlock} \
           %{?_without_libpcap} \
           %{?_without_macvtap} \
           %{?_without_audit} \
           %{?_without_dtrace} \
           %{?_without_driver_modules} \
           %{?_with_firewalld} \
           %{with_packager} \
           %{with_packager_version} \
           --with-qemu-user=%{qemu_user} \
           --with-qemu-group=%{qemu_group} \
           %{init_scripts}
make %{?_smp_mflags}
gzip -9 ChangeLog

%install
rm -fr %{buildroot}

%makeinstall SYSTEMD_UNIT_DIR=%{buildroot}%{_unitdir}
for i in domain-events/events-c dominfo domsuspend hellolibvirt openauth python xml/nwfilter systemtap
do
  (cd examples/$i ; make clean ; rm -rf .deps .libs Makefile Makefile.in)
done
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt/lock-driver/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt/lock-driver/*.a
%if %{with_driver_modules}
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt/connection-driver/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt/connection-driver/*.a
%endif

%if %{with_network}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/lib/libvirt/dnsmasq/
# We don't want to install /etc/libvirt/qemu/networks in the main %files list
# because if the admin wants to delete the default network completely, we don't
# want to end up re-incarnating it on every RPM upgrade.
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/libvirt/networks/
cp $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu/networks/default.xml \
   $RPM_BUILD_ROOT%{_datadir}/libvirt/networks/default.xml
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu/networks/default.xml
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu/networks/autostart/default.xml
# Strip auto-generated UUID - we need it generated per-install
sed -i -e "/<uuid>/d" $RPM_BUILD_ROOT%{_datadir}/libvirt/networks/default.xml
%else
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu/networks/default.xml
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu/networks/autostart/default.xml
%endif
%if ! %{with_qemu}
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/libvirtd_qemu.aug
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
%endif
%find_lang %{name}

%if ! %{with_sanlock}
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/libvirt_sanlock.aug
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/tests/test_libvirt_sanlock.aug
%endif

%if ! %{with_lxc}
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/libvirtd_lxc.aug
rm -f $RPM_BUILD_ROOT%{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
%endif

%if ! %{with_python}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libvirt-python-%{version}
%endif

%if %{client_only}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libvirt-%{version}
%endif

%if ! %{with_libvirtd}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/nwfilter
mv $RPM_BUILD_ROOT%{_datadir}/doc/libvirt-%{version}/html \
   $RPM_BUILD_ROOT%{_datadir}/doc/libvirt-devel-%{version}/
%endif

%if ! %{with_qemu}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/qemu.conf
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/libvirtd.qemu
%endif
%if ! %{with_lxc}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/libvirt/lxc.conf
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/libvirtd.lxc
%endif
%if ! %{with_uml}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/libvirtd.uml
%endif

%clean
rm -fr %{buildroot}

%check
cd tests
make
# These 3 tests don't current work in a mock build root
for i in nodeinfotest daemon-conf seclabeltest virdrivermoduletest virbitmaptest
do
  rm -f $i
  printf 'int main(void) { return 0; }' > $i.c
  printf '#!/bin/sh\nexit 0\n' > $i
  chmod +x $i
done
make check

%pre
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
# Normally 'setup' adds this in /etc/passwd, but this is
# here for case of upgrades from earlier Fedora/RHEL. This
# UID/GID pair is reserved for qemu:qemu
getent group kvm >/dev/null || groupadd -g 36 -r kvm
getent group qemu >/dev/null || groupadd -g 107 -r qemu
getent passwd qemu >/dev/null || \
  useradd -r -u 107 -g qemu -G kvm -d / -s /sbin/nologin \
    -c "qemu user" qemu
%endif

%post

%if %{with_libvirtd}
%if %{with_network}
# We want to install the default network for initial RPM installs
# or on the first upgrade from a non-network aware libvirt only.
# We check this by looking to see if the daemon is already installed
if ! /sbin/chkconfig libvirtd && test ! -f %{_sysconfdir}/libvirt/qemu/networks/default.xml
then
    UUID=`/usr/bin/uuidgen`
    sed -e "s,</name>,</name>\n  <uuid>$UUID</uuid>," \
         < %{_datadir}/libvirt/networks/default.xml \
         > %{_sysconfdir}/libvirt/qemu/networks/default.xml
    ln -s ../default.xml %{_sysconfdir}/libvirt/qemu/networks/autostart/default.xml
fi

# All newly defined networks will have a mac address for the bridge
# auto-generated, but networks already existing at the time of upgrade
# will not. We need to go through all the network configs, look for
# those that don't have a mac address, and add one.

network_files=$( (cd %{_localstatedir}/lib/libvirt/network && \
                  grep -L "mac address" *.xml; \
                  cd %{_sysconfdir}/libvirt/qemu/networks && \
                  grep -L "mac address" *.xml) 2>/dev/null \
                | sort -u)

for file in $network_files
do
   # each file exists in either the config or state directory (or both) and
   # does not have a mac address specified in either. We add the same mac
   # address to both files (or just one, if the other isn't there)

   mac4=`printf '%X' $(($RANDOM % 256))`
   mac5=`printf '%X' $(($RANDOM % 256))`
   mac6=`printf '%X' $(($RANDOM % 256))`
   for dir in %{_localstatedir}/lib/libvirt/network \
              %{_sysconfdir}/libvirt/qemu/networks
   do
      if test -f $dir/$file
      then
         sed -i.orig -e \
           "s|\(<bridge.*$\)|\0\n  <mac address='52:54:00:$mac4:$mac5:$mac6'/>|" \
           $dir/$file
         if test $? != 0
         then
             echo "failed to add <mac address='52:54:00:$mac4:$mac5:$mac6'/>" \
                  "to $dir/$file"
             mv -f $dir/$file.orig $dir/$file
         else
             rm -f $dir/$file.orig
         fi
      fi
   done
done
%endif

%if %{with_systemd}
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl enable libvirtd.service >/dev/null 2>&1 || :
    /bin/systemctl enable cgconfig.service >/dev/null 2>&1 || :
fi
%else
%if %{with_cgconfig}
# Starting with Fedora 16/RHEL-7, systemd automounts all cgroups,
# and cgconfig is no longer a necessary service.
%if (0%{?rhel} && 0%{?rhel} < 7) || (0%{?fedora} && 0%{?fedora} < 16)
if [ "$1" -eq "1" ]; then
/sbin/chkconfig cgconfig on
fi
%endif
%endif

/sbin/chkconfig --add libvirtd
if [ "$1" -ge "1" ]; then
	/sbin/service libvirtd condrestart > /dev/null 2>&1
fi
%endif
%endif

%preun
%if %{with_libvirtd}
%if %{with_systemd}
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable libvirtd.service > /dev/null 2>&1 || :
    /bin/systemctl stop libvirtd.service > /dev/null 2>&1 || :
fi
%else
if [ $1 = 0 ]; then
    /sbin/service libvirtd stop 1>/dev/null 2>&1
    /sbin/chkconfig --del libvirtd
fi
%endif
%endif

%postun
%if %{with_libvirtd}
%if %{with_systemd}
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart libvirtd.service >/dev/null 2>&1 || :
fi
%endif
%endif

%if %{with_libvirtd}
%if %{with_systemd}
%triggerun -- libvirt < 0.9.4
%{_bindir}/systemd-sysv-convert --save libvirtd >/dev/null 2>&1 ||:

# If the package is allowed to autostart:
/bin/systemctl --no-reload enable libvirtd.service >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del libvirtd >/dev/null 2>&1 || :
/bin/systemctl try-restart libvirtd.service >/dev/null 2>&1 || :
%endif
%endif

%preun client

%if %{with_systemd}
%else
if [ $1 = 0 ]; then
    /sbin/chkconfig --del libvirt-guests
    rm -f /var/lib/libvirt/libvirt-guests
fi
%endif

%post client

/sbin/ldconfig
%if %{with_systemd}
%else
/sbin/chkconfig --add libvirt-guests
%endif

%postun client -p /sbin/ldconfig

%if %{with_systemd}
%triggerun client -- libvirt < 0.9.4
%{_bindir}/systemd-sysv-convert --save libvirt-guests >/dev/null 2>&1 ||:

# If the package is allowed to autostart:
/bin/systemctl --no-reload enable libvirt-guests.service >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del libvirt-guests >/dev/null 2>&1 || :
/bin/systemctl try-restart libvirt-guests.service >/dev/null 2>&1 || :
%endif

%if %{with_sanlock}
%post lock-sanlock
if getent group sanlock > /dev/null ; then
    chmod 0770 %{_localstatedir}/lib/libvirt/sanlock
    chown root:sanlock %{_localstatedir}/lib/libvirt/sanlock
fi
%endif

%if %{with_libvirtd}
%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README COPYING.LIB TODO
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/

%if %{with_network}
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/qemu/
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/qemu/networks/
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/qemu/networks/autostart
%endif

%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/nwfilter/
%{_sysconfdir}/libvirt/nwfilter/*.xml

%{_sysconfdir}/rc.d/init.d/libvirtd
%if %{with_systemd}
%{_unitdir}/libvirtd.service
%endif
%doc daemon/libvirtd.upstart
%config(noreplace) %{_sysconfdir}/sysconfig/libvirtd
%config(noreplace) %{_sysconfdir}/libvirt/libvirtd.conf
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 6
%config(noreplace) %{_sysconfdir}/sysctl.d/libvirtd
%else
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/sysctl.d/libvirtd
%endif
%if %{with_dtrace}
%{_datadir}/systemtap/tapset/libvirt_probes.stp
%{_datadir}/systemtap/tapset/libvirt_qemu_probes.stp
%{_datadir}/systemtap/tapset/libvirt_functions.stp
%endif
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/qemu/
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/lxc/
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/uml/
%if %{with_libxl}
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/libxl/
%endif

%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd
%if %{with_qemu}
%config(noreplace) %{_sysconfdir}/libvirt/qemu.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.qemu
%endif
%if %{with_lxc}
%config(noreplace) %{_sysconfdir}/libvirt/lxc.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.lxc
%endif
%if %{with_uml}
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.uml
%endif

%dir %{_datadir}/libvirt/

%if %{with_network}
%dir %{_datadir}/libvirt/networks/
%{_datadir}/libvirt/networks/default.xml
%endif

%ghost %dir %{_localstatedir}/run/libvirt/

%dir %attr(0711, root, root) %{_localstatedir}/lib/libvirt/images/
%dir %attr(0711, root, root) %{_localstatedir}/lib/libvirt/filesystems/
%dir %attr(0711, root, root) %{_localstatedir}/lib/libvirt/boot/
%dir %attr(0711, root, root) %{_localstatedir}/cache/libvirt/

%if %{with_qemu}
%ghost %dir %attr(0700, root, root) %{_localstatedir}/run/libvirt/qemu/
%dir %attr(0750, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/
%dir %attr(0750, %{qemu_user}, %{qemu_group}) %{_localstatedir}/cache/libvirt/qemu/
%endif
%if %{with_lxc}
%ghost %dir %{_localstatedir}/run/libvirt/lxc/
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/lxc/
%endif
%if %{with_uml}
%ghost %dir %{_localstatedir}/run/libvirt/uml/
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/uml/
%endif
%if %{with_libxl}
%ghost %dir %{_localstatedir}/run/libvirt/libxl/
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/libxl/
%endif
%if %{with_network}
%ghost %dir %{_localstatedir}/run/libvirt/network/
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/network/
%dir %attr(0755, root, root) %{_localstatedir}/lib/libvirt/dnsmasq/
%endif

%if %{with_qemu}
%{_datadir}/augeas/lenses/libvirtd_qemu.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
%endif

%if %{with_lxc}
%{_datadir}/augeas/lenses/libvirtd_lxc.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
%endif

%{_datadir}/augeas/lenses/libvirtd.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd.aug

%if %{with_polkit}
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6
%{_datadir}/polkit-1/actions/org.libvirt.unix.policy
%else
%{_datadir}/PolicyKit/policy/org.libvirt.unix.policy
%endif
%endif

%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/

%if %{with_lxc}
%attr(0755, root, root) %{_libexecdir}/libvirt_lxc
%endif

%if %{with_storage_disk}
%attr(0755, root, root) %{_libexecdir}/libvirt_parthelper
%endif

%attr(0755, root, root) %{_libexecdir}/libvirt_iohelper
%attr(0755, root, root) %{_sbindir}/libvirtd

%{_mandir}/man8/libvirtd.8*
%doc docs/*.xml
%endif

%if %{with_sanlock}
%files lock-sanlock
%defattr(-, root, root)
%if %{with_qemu}
%config(noreplace) %{_sysconfdir}/libvirt/qemu-sanlock.conf
%endif
%attr(0755, root, root) %{_libdir}/libvirt/lock-driver/sanlock.so
%{_datadir}/augeas/lenses/libvirt_sanlock.aug
%{_datadir}/augeas/lenses/tests/test_libvirt_sanlock.aug
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/sanlock
%{_sbindir}/virt-sanlock-cleanup
%{_mandir}/man8/virt-sanlock-cleanup.8*
%attr(0755, root, root) %{_libexecdir}/libvirt_sanlock_helper
%endif

%files client -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog.gz NEWS README COPYING.LIB TODO

%config(noreplace) %{_sysconfdir}/libvirt/libvirt.conf
%{_mandir}/man1/virsh.1*
%{_mandir}/man1/virt-xml-validate.1*
%{_mandir}/man1/virt-pki-validate.1*
%{_mandir}/man1/virt-host-validate.1*
%{_bindir}/virsh
%{_bindir}/virt-xml-validate
%{_bindir}/virt-pki-validate
%{_bindir}/virt-host-validate
%{_libdir}/lib*.so.*

%dir %{_datadir}/libvirt/
%dir %{_datadir}/libvirt/schemas/

%{_datadir}/libvirt/schemas/basictypes.rng
%{_datadir}/libvirt/schemas/capability.rng
%{_datadir}/libvirt/schemas/domain.rng
%{_datadir}/libvirt/schemas/domaincommon.rng
%{_datadir}/libvirt/schemas/domainsnapshot.rng
%{_datadir}/libvirt/schemas/interface.rng
%{_datadir}/libvirt/schemas/network.rng
%{_datadir}/libvirt/schemas/networkcommon.rng
%{_datadir}/libvirt/schemas/nodedev.rng
%{_datadir}/libvirt/schemas/nwfilter.rng
%{_datadir}/libvirt/schemas/secret.rng
%{_datadir}/libvirt/schemas/storageencryption.rng
%{_datadir}/libvirt/schemas/storagepool.rng
%{_datadir}/libvirt/schemas/storagevol.rng

%{_datadir}/libvirt/cpu_map.xml

%{_sysconfdir}/rc.d/init.d/libvirt-guests
%if %{with_systemd}
%{_unitdir}/libvirt-guests.service
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/libvirt-guests
%dir %attr(0755, root, root) %{_localstatedir}/lib/libvirt/

%if %{with_sasl}
%config(noreplace) %{_sysconfdir}/sasl2/libvirt.conf
%endif

%files devel
%defattr(-, root, root)

%{_libdir}/lib*.so
%dir %{_includedir}/libvirt
%{_includedir}/libvirt/*.h
%{_libdir}/pkgconfig/libvirt.pc

%dir %{_datadir}/libvirt/api/
%{_datadir}/libvirt/api/libvirt-api.xml
%{_datadir}/libvirt/api/libvirt-qemu-api.xml
%dir %{_datadir}/gtk-doc/html/libvirt/
%doc %{_datadir}/gtk-doc/html/libvirt/*.devhelp
%doc %{_datadir}/gtk-doc/html/libvirt/*.html
%doc %{_datadir}/gtk-doc/html/libvirt/*.png
%doc %{_datadir}/gtk-doc/html/libvirt/*.css

%doc docs/*.html docs/html docs/*.gif
%doc docs/libvirt-api.xml
%doc examples/hellolibvirt
%doc examples/domain-events/events-c
%doc examples/dominfo
%doc examples/domsuspend
%doc examples/openauth
%doc examples/xml
%doc examples/systemtap

%if %{with_python}
%files python
%defattr(-, root, root)

%doc AUTHORS NEWS README COPYING.LIB
%{_libdir}/python*/site-packages/libvirt.py*
%{_libdir}/python*/site-packages/libvirt_qemu.py*
%{_libdir}/python*/site-packages/libvirtmod*
%doc python/tests/*.py
%doc python/TODO
%doc examples/python
%doc examples/domain-events/events-python
%endif

%changelog
* Sat Nov 12 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 0.10.2-60.0
- Patched for building on arm.

* Wed Mar 30 2016 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-60
- util: avoid getting stuck on macvtapN name created outside libvirt (rhbz#1321637)

* Tue Mar  8 2016 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-59
- qemu: Always format model for host-model CPUs (rhbz#1307094)

* Fri Mar  4 2016 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-58
- qemu: Don't compare host-passthrough CPU to host CPU (rhbz#1307094)

* Tue Feb 16 2016 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-57
- vmx: Relax virtualHW.version check (rhbz#1300574)
- qemu: snapshot: Don't leak XML definition and forget to unlock job (rhbz#1305793)
- qemu: Fix formatting flags in qemuDomainSaveImageOpen (rhbz#1307094)
- network: Resolve some issues around vlan copying (rhbz#1300843)
- network: fix connections count in case of allocate failure (rhbz#1300843)
- network: consolidate connection count updates for device pool (rhbz#1300843)
- network: consolidated info log for all network allocate/free operations (rhbz#1300843)
- util: increase libnl buffer size (rhbz#1276478)
- util: reduce debug log in virPCIGetVirtualFunctions() (rhbz#1276478)
- util: improve error reporting in virNetDevVPortProfileGetStatus (rhbz#1276478)
- util: add missing newline (rhbz#1276478)
- util: eliminate bogus error log in virNetDevVPortProfileGetStatus (rhbz#1276478)
- util: clean up and expand 802.1QbX negotiation logging (rhbz#1276478)
- util: report the MAC address that couldn't be set (rhbz#1276478)
- util: reset MAC address of macvtap passthrough physdev after disassociate (rhbz#1276478)
- bitmap: add way to find next clear bit (rhbz#1276478)
- Introduce virBitmapIsBitSet (rhbz#1276478)
- util: Introduce flags field for macvtap creation (rhbz#1276478)
- virnetdevmacvlan.c: Introduce mutex for macvlan creation (rhbz#1276478)
- util: keep/use a bitmap of in-use macvtap devices (rhbz#1276478)

* Wed Jan 20 2016 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-56
- qemu: snapshot: Fix return value of external checkpoint with no disks (rhbz#1292312)
- qemu: snapshot: Fix modification of vm object without job (rhbz#1290647)
- virsh-domain: Add --live, --config, --current logic to cmdAttachInterface (rhbz#1229128)
- RHEL: virsh: remove duplicate --config for 'virsh update-device' (rhbz#1224037)
- Update ESX driver to always use privateData (rhbz#1213348)
- esx: Simplify VI (vSphere) API and VMware product version handling (rhbz#1213348)
- conf: net: Correctly switch how to format address fields (rhbz#1299700)
- qemu: Refuse to create snapshot of a disk without source (rhbz#1299411)
- Build all binaries with PIE (rhbz#1242156)
- Enable full RELRO mode (rhbz#1242156)
- Don't duplicate compiler warning flags when linking (rhbz#1242156)
- Simplify RELRO_LDFLAGS (rhbz#1242156)
- Fix AM_LDFLAGS typo (rhbz#1242156)
- Pass AM_LDFLAGS to driver modules too (rhbz#1242156)
- RHEL: Enable RELRO for python modules (rhbz#1242156)

* Wed Nov  4 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-55
- daemon: Suppress logging of VIR_ERR_NO_DOMAIN_METADATA (rhbz#1260864)
- Allow <source> for type=block to have no dev (rhbz#1220197)
- qemu: event: Properly handle spice events (rhbz#1236581)
- qemu: event: Clean up VNC monitor handling (rhbz#1236581)
- qemu: split out cpuset.mems setting (rhbz#1263263)
- qemu: leave restricting cpuset.mems after initialization (rhbz#1263263)
- virNetDev{Replace, Restore}MacAddress: Fix memory leak (rhbz#1251532)
- util: make virNetDev(Replace|Restore)MacAddress public functions (rhbz#1251532)
- util: don't use netlink to save/set mac for macvtap+passthrough+802.1Qbh (rhbz#1251532)
- qemu: fix hotplugging cpus with strict memory pinning (rhbz#1263263)
- storage: Track successful creation of LV for removal (rhbz#1232170)

* Tue Apr 28 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-54
- util: set MAC address for VF via netlink message to PF+VF# when possible (rhbz#1113474)
- util: set macvtap physdev online when macvtap is set online (rhbz#1113474)

* Fri Apr 10 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-53
- RHEL: Avoid memory leak when virCgroupSetCpusetMemoryMigrate fails (rhbz#1198497)
- qemu: cgroup: Fix memory leak when there's no vCPU pinning (rhbz#1198096)

* Fri Apr 10 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-52
- qemu: Keep QEMU host drive prefix in BlkIoTune (rhbz#1203633)
- qemu: Fix name comparison in qemuMonitorJSONBlockIoThrottleInfo() (rhbz#1203633)
- virsh: fix typos in virsh man page (rhbz#1130835)
- schemas: Allow all generic elements and attributes for all interfaces (rhbz#1206066)
- RNG: Allow multiple parameters to be passed to an interface filter (rhbz#1206066)
- qemu_domain: fix startup policy for disks (rhbz#1203542)
- Create directory for lease files if it's missing (rhbz#1200991)
- qemu: cgroup: Properly set up vcpu pinning (rhbz#1198096)
- cgroup: Add accessors for cpuset.memory_migrate (rhbz#1198497)
- qemu: Fix possible crash (rhbz#1198497)
- qemu: Migrate memory on numatune change (rhbz#1198497)
- qemu: fix crash when removing <filterref> from interface with update-device (rhbz#1205042)
- nwfilter: Fix rule priority problem (rhbz#1210183)
- qemuProcessHook: Call qemuProcessInitNumaMemoryPolicy only when needed (rhbz#1198645)

* Fri Mar 20 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-51
- sanlock: Don't spam logs with "target pid not found" (rhbz#1189414)
- nwfilter: fix crash when adding non-existing nwfilter (rhbz#1202703)
- util: more verbose error when failing to create macvtap device (rhbz#1186142)

* Thu Mar  5 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-50
- conf: Don't format actual network definition in migratable XML (rhbz#1186142)
- network: don't allow multiple portgroups with the same name in a network (rhbz#1115858)
- build: fix build with latest rawhide kernel headers (rhbz#1198698)

* Fri Feb  6 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-49
- nwfilter: utility function virNWFilterVarValueEqual (rhbz#1126487)
- qemu: support live update of an interface's filter (rhbz#1126487)
- qemu: Update fsfreeze status on domain state transitions (rhbz#1136251)
- virsh: Fix semantics of --config for "update-device" command (rhbz#1129112)
- virsh: Don't use legacy API if --current is used on device hot(un)plug (rhbz#1125194)
- qemu: Avoid double serial output with RHEL 6 qemu (rhbz#1162759)
- storage: Check the partition name against provided name (rhbz#1138523)
- qemu: Don't unconditionally delete file in qemuOpenFileAs (rhbz#1158036)
- conf: Don't mangle vcpu placement randomly (rhbz#1170495)

* Wed Jan 28 2015 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-48
- networkValidate: Disallow bandwidth in portgroups too (rhbz#1115292)
- qemu: Fix checking of ABI stability when restoring external checkpoints (rhbz#834196)
- qemu: Use "migratable" XML definition when doing external checkpoints (rhbz#834196)
- qemu: Fix memleak after commit 59898a88ce8431bd3ea249b8789edc2ef9985827 (rhbz#834196)
- qemu: blkiotune: Avoid accessing non-existing disk configuration (rhbz#1131821)
- qemu: Fix build error introduced in 653137eb957a278b556c6226424aad5395a (rhbz#1131821)
- qemu: snapshot: Use better check when reverting external snapshots (rhbz#1124854)
- virsh: domain: Use global constant for XML file size limit (rhbz#1134671)
- selinux: Avoid label reservations for type = none (rhbz#1138488)
- Clean up chardev sockets on QEMU shutdown (rhbz#1122367)
- Don't include @LIBS@ in libvirt.pc.in file (rhbz#1134455)
- qemu: save domain state to XML after reboot (rhbz#1169405)
- virsh: Honour -q in domblklist, vcpupin and emulatorpin (rhbz#1135171)
- virsh-domain: Flip logic in cmdSetvcpus (rhbz#1139114)
- Fix possible memory leak in util/virxml.c (rhbz#1136729)
- esx_vi: fix possible segfault (rhbz#1136729)
- sasl: Fix authentication when using PLAIN mechanism (rhbz#1171521)
- Fix leak in x86UpdateHostModel (rhbz#1144304)

* Thu Dec 11 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-47
- Revert "qemu: export disk snapshot support in capabilities" (rhbz#1149667)
- qemu: allow restore with non-migratable XML input (rhbz#1141838)
- qemu: Introduce qemuDomainDefCheckABIStability (rhbz#1141838)
- Make ABI stability issue easier to debug (rhbz#1141838)
- domain_conf: fix domain deadlock (CVE-2014-3657)
- CVE-2014-3633: qemu: blkiotune: Use correct definition when looking up disk (CVE-2014-3633)
- CVE-2014-7823: dumpxml: security hole with migratable flag (CVE-2014-7823)
- sanlock: Avoid freeing uninitialized value (rhbz#1136788)
- virsh: Print cephx and iscsi usage (rhbz#1156327)
- Fix bug with loading bridge name for active domain during libvirtd start (rhbz#1146310)
- conf: Fix even implicit labels (rhbz#1138500)
- tests: Add test cases for previous commit (rhbz#1138500)

* Tue Sep  9 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-46
- cpu: separate host-model and host-passthrough (rhbz#1138222)
- Don't include non-migratable features in host-model (rhbz#1138222)
- Don't add dhcp hosts to hostsfile twice (rhbz#1137011)

* Tue Sep  2 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-45
- metadata: track title edits across libvirtd restart (rhbz#1122205)

* Tue Aug 19 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-44
- network: make networkCreateInterfacePool more robust (rhbz#1111455)

* Fri Aug  8 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-43
- Fix blkdeviotune for shutoff domain (rhbz#1122819)
- rpc: message related sizes enlarged (rhbz#1126393)
- Increase the size of REMOTE_MIGRATE_COOKIE_MAX to REMOTE_STRING_MAX (rhbz#1126393)
- Fix max stream packet size for old clients (rhbz#1126393)
- Adjust legacy max payload size to account for header information (rhbz#1126393)
- rpc: Correct the wrong payload size checking (rhbz#1126393)

* Fri Aug  1 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-42
- conf: Fix backport of metadata API code (rhbz#1115039)
- conf: Always format seclabel's model (rhbz#1113860)

* Wed Jul 16 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-41
- Add invariant TSC cpu flag (rhbz#996772)
- Fix segfault when starting a domain with no cpu definition (rhbz#996772)
- qemu: copy: Accept 'format' parameter when copying to a non-existing img (rhbz#1113828)
- Bind connection close callback APIs to python binding (rhbz#1114619)
- qemu: Factor out body of qemuDomainGetMetadata for universal use (rhbz#1115039)
- qemu: Factor out body of qemuDomainSetMetadata for universal use (rhbz#1115039)
- conf: Factor out setting of metadata to simplify code (rhbz#1115039)
- util: Add helper to convert libxml2 nodes to a string (rhbz#1115039)
- conf: Add support for requesting of XML metadata via the API (rhbz#1115039)
- conf: allow to add XML metadata using the virDomainSetMetadata api (rhbz#1115039)
- conf: Avoid false positive of uninitialized variable use (rhbz#1115039)
- lib: Don't force the key argument when deleting metadata (rhbz#1115039)
- test: Add <metadata> support into the test drivera (rhbz#1115039)
- tests: Add metadata tests (rhbz#1115039)
- conf: Don't corrupt metadata on OOM (rhbz#1115039)
- Ignore additional fields in iscsiadm output (rhbz#1116741)
- conf: net: Fix helper for applying new network definition (rhbz#1116754)
- blockjob: wait for pivot to complete (rhbz#1119385)
- virsh: Introduce macros to reject mutually exclusive arguments (rhbz#1117177)
- virsh-domain: Add --live, --config, --current logic to cmdAttachDisk (rhbz#1117177)
- virsh-domain: Add --live, --config, --current logic to cmdDetachDevice (rhbz#1117177)
- virsh-domain: Add --live, --config, --current logic to cmdDetachDisk (rhbz#1117177)
- virsh: Use inactive definition when removing disk from config (rhbz#1117177)
- virsh-domain: Add --live, --config, --current logic to cmdAttachDevice (rhbz#1117177)

* Mon Jun 30 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-40
- formatdomain.html.in: Document implementation limitation of QoS (rhbz#980350)
- Fix error in qemuDomainSetNumaParamsLive (rhbz#857312)
- cpu: Add new Broadwell CPU model (rhbz#1100381)
- docs: publish correct enum values (rhbz#1113316)
- qemu: blockcopy: Don't remove existing disk mirror info (rhbz#1113828)
- qemu: fix guestfwd chardev option back how it was (rhbz#1112066)

* Mon Jun 23 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-39
- Fix crash when saving a domain with type none dac label (rhbz#1108590)
- Initialize threading & error layer in LXC controller (rhbz#1109120)

* Wed Jun 11 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-38
- remote: Don't leak priv->tls object on connection failure (rhbz#1099075)
- Fix invalid read in virNetSASLSessionClientStep debug log (rhbz#1100173)
- Tie SASL callbacks lifecycle to virNetSessionSASLContext (rhbz#1100173)
- fix leak in memoryStats with older python (rhbz#1099860)
- hooks: let virCommand do the error reporting (rhbz#1105397)
- SELinux: don't fail silently when no label is present (rhbz#1105954)
- qemu: Add qemuDomainReleaseDeviceAddress to remove any address (rhbz#807023)
- qemu: Separate disk device removal into a standalone function (rhbz#807023)
- qemu: Separate controller removal into a standalone function (rhbz#807023)
- qemu: Separate net device removal into a standalone function (rhbz#807023)
- qemu: Separate host device removal into a standalone function (rhbz#807023)
- Add VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED event (rhbz#807023)
- examples: Handle VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED event (rhbz#807023)
- Clarify virDomainDetachDeviceFlags documentation (rhbz#807023)
- Add virDomainDefFindDevice for looking up a device by its alias (rhbz#807023)
- qemu: Add support for DEVICE_DELETED event (rhbz#807023)
- qemu: Remove devices only after DEVICE_DELETED event (rhbz#807023)
- qemu: Emit VIR_DOMAIN_EVENT_ID_DEVICE_REMOVED events (rhbz#807023)
- Add function to find a needle in a string array (rhbz#807023)
- util: Non-existent string array does not contain any string (rhbz#807023)
- conf: Make error reporting in virDomainDefFindDevice optional (rhbz#807023)
- qemu: Introduce qemuMonitorGetDeviceAliases (rhbz#807023)
- qemu: Unplug devices that disappeared when libvirtd was down (rhbz#807023)
- qemu: Finish device removal in the original thread (rhbz#807023)
- qemu: Process DEVICE_DELETED event in a separate thread (rhbz#807023)
- qemu: Remove interface backend only after frontend is gone (rhbz#807023)
- qemu: Remove disk backend only after frontend is gone (rhbz#807023)
- qemu: Return in from qemuDomainRemove*Device (rhbz#807023)

* Fri May 23 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-37
- udev: consider the device a CDROM when ID_CDROM=1 (rhbz#1016878)
- Add support for timestamping QEMU logs (rhbz#997010)
- Detect -msg-timestamp capability from QEMU help output (rhbz#997010)
- qemu: Avoid leak in qemuDomainCheckRemoveOptionalDisk (rhbz#1014730)
- Return right error code for baselineCPU (rhbz#1097969)
- Add a port allocator class (rhbz#1018695)
- Avoid integer wrap on remotePortMax in QEMU driver (rhbz#1018695)
- Followup fix for integer wraparound in port allocator (rhbz#1018695)
- Don't spam logs with "port 0 must be in range" errors (rhbz#1018695)
- qemu: Avoid assigning unavailable migration ports (rhbz#1018695)
- qemu: Make migration port range configurable (rhbz#1018695)
- qemu: Fix augeas support for migration ports (rhbz#1018695)
- qemu: clean up migration ports when migration cancelled (rhbz#1018695)
- qemuDomainObjBeginJobInternal: Return -2 for temporary failures (rhbz#1083238)
- qemu: Make qemuProcess{Start, Stop}CPUs easier to follow (rhbz#1083238)
- qemu: Ignore temporary job errors when checking migration status (rhbz#1083238)
- qemu: Send migrate_cancel when aborting migration (rhbz#1098833)

* Thu May 15 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-36
- virSecuritySELinuxSetFileconHelper: Don't fail on read-only NFS (rhbz#1095135)
- storage: Resolve issues in failure path (rhbz#1092882)
- interface: Introduce netcfInterfaceObjIsActive (rhbz#1095774)
- interface: dump inactive xml when interface isn't active (rhbz#1095774)
- qemu: add host-pci-multidomain capability (rhbz#1092390)
- qemu: specify domain in host-side PCI addresses when needed/supported (rhbz#1092390)
- util: fix virFileOpenAs return value and resulting error logs (rhbz#851411)
- qemu: check actual netdev type rather than config netdev type during init (rhbz#1012834)
- Fix parsing of bond interface XML (rhbz#1067062)
- qemuSetupCgroup: Fix reference to cgroup (rhbz#1012846)
- apibuild: Disallow 'returns' return decription (rhbz#808463)
- ESX: Add support for virtualHW version 10 (rhbz#1089389)
- storage: Ensure 'qemu-img resize' size arg is a 512 multiple (rhbz#1002813)
- qemu: Adjust size for qcow2/qed if not on sector boundary (rhbz#1002813)
- sanlock: code movement in virLockManagerSanlockAcquire (rhbz#1088034)
- sanlock: don't fail with unregistered domains (rhbz#1088034)
- sanlock: avoid leak in acquire() (rhbz#1088034)
- networkStartNetwork: Be more verbose (rhbz#1064831)
- network_conf: Expose virNetworkDefFormatInternal (rhbz#1064831)
- Avoid crash when LXC start fails with no interface target (rhbz#1064831)
- lxc_process: Avoid passing NULL iface->iname (rhbz#1064831)
- network: Introduce network hooks (rhbz#1064831)
- bridge_driver.h: Fix build --without-network (rhbz#1064831)
- networkRunHook: Run hook only if possible (rhbz#1064831)
- conf: clarify what is returned for actual bandwidth and vlan (rhbz#1064831)
- conf: handle null pointer in virNetDevVlanFormat (rhbz#1064831)
- conf: make virDomainNetDefFormat a public function (rhbz#1064831)
- conf: re-situate <bandwidth> element in <interface> (rhbz#1064831)
- conf: new function virDomainActualNetDefContentsFormat (rhbz#1064831)
- Slightly refactor hostdev parsing / formating (rhbz#1064831)
- conf: output actual netdev status in <interface> XML (rhbz#1064831)
- network: include plugged interface XML in "plugged" network hook (rhbz#1064831)
- network: don't even call networkRunHook if there is no network (rhbz#1064831)

* Wed May  7 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-35
- qemu: export disk snapshot support in capabilities (rhbz#1081032)
- qemu: extract guest capabilities initialization (rhbz#1081032)
- qemu: add unit tests for the capabilities xml (rhbz#1081032)
- qemu: properly quit migration with abort_on_error (rhbz#1045833)
- conf: restrict external snapshots to backing store formats (rhbz#1019926)
- qemu: don't check for backing chains for formats w/o snapshot support (rhbz#1019926)
- qemu: don't call virFileExists() for network type disks (rhbz#1019926)
- net: Change argument type of virNetworkObjIsDuplicate() (rhbz#1057321)
- net: Move creation of dnsmasq hosts file to function starting dnsmasq (rhbz#1057321)
- net: Re-use checks when creating transient networks (rhbz#1057321)
- network: prevent a few invalid configuration combinations (rhbz#1057321)
- network: disallow <bandwidth>/<mac> for bridged/macvtap/hostdev networks (rhbz#1057321)
- virsh-domain: Fix cmdSetvcpus error message (rhbz#1092412)
- spice: detect if qemu can disable file transfer (rhbz#983018)
- spice: expose the QEMU disable file transfer option (rhbz#983018)
- qemu_caps: detect if qemu can disable file transfer for spice (rhbz#983018)
- Device{Attach, Detach}: Document S4 limitations (rhbz#808463)
- storageVolCreateXMLFrom: Allow multiple accesses to origvol (rhbz#1058700)
- LSN-2014-0003: Don't expand entities when parsing XML (CVE-2014-0179)

* Tue Apr 29 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-34
- nwfilter: Remove error report in virNWFilterDHCPSnoopEnd (rhbz#903480)
- conf: introduce generic ISA address (rhbz#1033984)
- conf: add support for panic device (rhbz#1033984)
- qemu: add support for -device pvpanic (rhbz#1033984)
- PanicCheckABIStability: Need to check for existence (rhbz#1033984)
- use virBitmapFree instead of VIR_FREE for cpumask (rhbz#1088165)
- Properly free vcpupin info for unplugged CPUs (rhbz#1088165)
- Save domain status after cpu hotplug (rhbz#1088703)
- Document behavior of setvcpus during guest boot (rhbz#1088748)
- qemu: Use maximum guest memory size when getting NUMA placement advice (rhbz#1011906)
- qemu: Properly format the uuid string in error messages (rhbz#947974)
- qemu: Split out code to generate SPICE command line (rhbz#953126)
- qemu: Improve handling of channels when generating SPICE command line (rhbz#953126)
- qemu: Split out SPICE port allocation into a separate function (rhbz#953126)
- qemu: Do sensible auto allocation of SPICE port numbers (rhbz#953126)
- qemu: fix failure to start with spice graphics and no tls (rhbz#953126)
- qemu: Do not ignore address for USB disks (rhbz#985166)
- qemu: pass -usb and usb hubs earlier, so USB disks with static address are handled properly (rhbz#985166)
- qemu: refactor qemuDomainCheckDiskPresence for only disk presence check (rhbz#1014730)
- qemu: add helper functions for diskchain checking (rhbz#1014730)
- qemu: check presence of each disk and its backing file as well (rhbz#1014730)
- conf: add startupPolicy attribute for harddisk (rhbz#1014730)
- qemu: support to drop disk with 'optional' startupPolicy (rhbz#1014730)
- qemu: Avoid overflow when setting migration speed (rhbz#1083483)
- qemu: Avoid overflow when setting migration speed on inactive domains (rhbz#1083483)
- caps: Add helpers to convert NUMA nodes to corresponding CPUs (rhbz#1012846)
- qemu: Set cpuset.cpus for domain process (rhbz#1012846)
- qemu: Unbreak p2p migration with complete migration URI (rhbz#1073227)
- maint: don't lose error on canceled migration (rhbz#1073227)
- virsh: suppress aliases in group help (rhbz#956968)

* Wed Apr 16 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-33
- conf: fix error for parallel port mismatch (rhbz#950830)
- virDomainReboot: Document that migration might be unsafe (rhbz#744967)
- interface: list all interfaces with flags == 0 (rhbz#884382)
- Fix the syntax-check failure (rhbz#884382)
- Crash of libvirtd by unprivileged user in virConnectListAllInterfaces (rhbz#884382)
- qemuDomainObjStart: Warn on corrupted image (rhbz#1022008)
- QoS: make tc filters match all traffic (rhbz#1084477)
- conf: add support for booting from redirected USB devices (rhbz#1035190)
- Add redirdevs to ABI stability check (rhbz#1035529)
- Fix incorrect values in redirdev ABI check error (rhbz#1035529)
- virSecurityLabelDefParseXML: Don't parse label on model='none' (rhbz#1027096)
- storage: Skip inactive lv volumes (rhbz#748282)
- Check for existence of interface prior to setting terminate flag (rhbz#903480)
- storage: Avoid forward declaration of virStorageVolDelete (rhbz#1024159)
- storage: Don't update pool available/allocation if buildVol fails (rhbz#1024159)
- conf: Report errors on cputune parameter parsing (rhbz#1040784)
- Treat zero cpu shares as a valid value (rhbz#1040784)
- Show the real cpu shares value in live XML (rhbz#1040784)

* Fri Apr 11 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-32
- virsh-snapshot: Reject --no-metadata together with --print-xml (rhbz#892508)
- snapshot: Mention disk-only snapshots in error message (rhbz#880521)
- qemu: snapshot: Report better error message if migration isn't allowed (rhbz#884926)
- qemu: snapshot: Remove memory image if external checkpoint fails (rhbz#885963)
- virsh-snapshot: Fix XPath query to determine snapshot state (rhbz#890457)
- conf: Check if number of vCPUs fits in the storage variable (rhbz#902652)
- conf: Improve error messages if parsing of vCPU count fails (rhbz#902652)
- qemu: snapshot: Don't kill access to disk if snapshot creation fails (rhbz#906639)
- qemu: Un-mark volume as mirrored/copied if blockjob copy fails (rhbz#923125)
- qemu-blockjob: Fix limit of bandwidth for block jobs to supported value (rhbz#927160)
- virsh: Fix typo in docs (rhbz#949776)
- virsh-domain: Report errors on invalid --holdtime value for cmdSendKey (rhbz#952938)
- qemu: Don't update count of vCPUs if hot-plug fails silently (rhbz#1000357)
- virsh: man: Mention that volumes need to be in storage pool for undefine (rhbz#1044790)
- Disable nwfilter driver when running unprivileged (rhbz#1029299)
- storage: reduce number of stat calls (rhbz#977706)
- Ignore missing files on pool refresh (rhbz#977706)
- sanlock: add missing test command in virt-sanlock-cleanup.in (rhbz#1000890)
- virt-sanlock-cleanup; Fix augtool usage (rhbz#1000890)
- conf: Fix typo in error message in ABI stability check (rhbz#961655)
- qemu: Improve error when setting invalid count of vcpus via agent (rhbz#1035109)
- doc: Clarify usage of SELinux baselabel (rhbz#954245)
- selinux: Don't mask errors of virSecuritySELinuxGenNewContext (rhbz#954245)
- qemu: Return meaningful error when qemu dies early (rhbz#844378)
- sanlock: Forbid VIR_DOMAIN_LOCK_FAILURE_IGNORE (rhbz#905280)
- Remove the redundant parentheses in migrate help (rhbz#927497)
- virt-xml-validate: add missing schemas (rhbz#1006699)
- tools: add missing 'interface' type and update man page (rhbz#1006699)
- qemu: Don't require a block or file when looking for an alias (rhbz#1078328)

* Tue Apr  8 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-31
- doc: schema: Add basic documentation for the virtual RNG device support (rhbz#786408)
- conf: Add support for RNG device configuration in XML (rhbz#786408)
- conf: Add RNG device ABI compatibility check (rhbz#786408)
- qemu: Implement support for default 'random' backend for virtio-rng (rhbz#786408)
- qemu: Implement support for EGD backend for virtio-rng (rhbz#786408)
- docs: domain: /dev/urandom isn't a valid rng patch (rhbz#786408)
- tests: Add tests for virtio-rng device handling (rhbz#786408)
- docs: Fix attribute name for virtio-rng backend (rhbz#786408)
- rng: restrict passthrough names to known-good files (rhbz#786408)
- Resolve valgrind error (rhbz#786408)
- Fix crash parsing RNG device specification (rhbz#786408)
- rng: allow default device in RNG grammar (rhbz#786408)
- virtio-rng: Add rate limiting options for virtio-RNG (rhbz#786408)
- qemu_caps: Enable virtio-rng for RHEL-6.6 qemu-kvm downstream (rhbz#786408)
- audit: Audit resources used by VirtIO RNG (rhbz#786408)
- virtio-rng: Remove double space in error message (rhbz#786408)
- doc: fix XML for the RNG device example (rhbz#786408)
- conf: Don't crash on invalid chardev source definition of RNGs and other (rhbz#786408)
- conf: Fix XML formatting of RNG device info (rhbz#786408)
- libvirt: fix error message when connection can't be opened (rhbz#851413)
- conf: fix error for parallel port mismatch (rhbz#950830)
- virsh: clarify vol-{down, up}load description (rhbz#955539)
- virsh: fix doc typos (rhbz#1022872)
- util: use string libvirt to prefix error message instead of libvir (rhbz#911996)
- docs: use MiB/s instead of Mbps for migration speed (rhbz#948821)
- schema: require target path in storage pool xml (rhbz#893273)
- schema: make source optional in volume XML (rhbz#893273)
- Add qxl ram size to ABI stability check (rhbz#1035134)
- qemu: fix default spice password setting (rhbz#953721)
- Expose ownership ID parsing (rhbz#963881)
- Make qemuOpenFile aware of per-VM DAC seclabel. (rhbz#869053)
- Use qemuOpenFile in qemu_driver.c (rhbz#963881)
- virsh: Fix heading in manpage (rhbz#996840)
- qemu: Change the default unix monitor timeout (rhbz#1051364)
- qemu: fix live pinning to memory node on NUMA system (rhbz#857312)
- qemu: Clean up qemuDomainSetNumaParameters (rhbz#857312)

* Tue Apr  8 2014 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-30
- Fix race in starting transient VMs (rhbz#1022924)
- qemuDomainDestroyFlags: Don't allow @vm to disappear while executing API (rhbz#1030736)
- python: return dictionary without value in case of no blockjob (rhbz#999454)
- remote: fix regression in event deregistration (rhbz#1020372)
- Add virtio-scsi to fallback models of scsi controller (rhbz#1014943)
- qemu: Avoid operations on NULL monitor if VM fails early (rhbz#1047659)
- qemu: Do not access stale data in virDomainBlockStats (CVE-2013-6458)
- qemu: Avoid using stale data in virDomainGetBlockInfo (CVE-2013-6458)
- qemu: Fix job usage in qemuDomainBlockJobImpl (CVE-2013-6458)
- qemu: Fix job usage in qemuDomainBlockCopy (rhbz#1043069)
- qemu: Fix job usage in virDomainGetBlockIoTune (CVE-2013-6458)
- Don't crash if a connection closes early (CVE-2014-1447)
- Really don't crash if a connection closes early (CVE-2014-1447)
- Block info query: Add check for transient domain (rhbz#1040507)
- network: only prevent forwarding of DNS requests for unqualified names (rhbz#1037741)
- network: change default of forwardPlainNames to 'yes' (rhbz#1037741)
- sanlock: Truncate domain names longer than SANLK_NAME_LEN (rhbz#1060557)
- Remove contiguous CPU indexes assumption (rhbz#1066473)
- qemu: monitor: Fix error message and comment when getting cpu info (rhbz#1066473)
- qemu: monitor: Filter out thread ids of CPUS that were unplugged (rhbz#1066473)
- qemu: monitor: Fix invalid parentheses (rhbz#1076719)
- virNetClientSetTLSSession: Restore original signal mask (rhbz#1078589)
- spec: Switch to "git am" for applying patches (rhbz#1076719)

* Wed Oct  9 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-29
- virNetDevBandwidthEqual: Make it more robust (rhbz#1014198)
- qemu_hotplug: Allow QoS update in qemuDomainChangeNet (rhbz#1014198)
- qemu: Generate correct name for hostdev network devices (rhbz#1001881)

* Wed Oct  2 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-28
- libvirt-guests: status: Return non-zero when stopped (rhbz#1011981)
- qemu: Drop qemuDomainMemoryLimit (rhbz#1013758)
- docs: Discourage users to set hard_limit (rhbz#1013758)
- docs: Clean 09adfdc62de2b up (rhbz#1013758)
- qemuSetupMemoryCgroup: Handle hard_limit properly (rhbz#1013758)
- qemuBuildCommandLine: Fall back to mem balloon if there's no hard_limit (rhbz#1013758)

* Wed Sep 25 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-27
- qemu: Fix seamless SPICE migration (rhbz#1009886)

* Thu Sep 19 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-26
- Fix crash in remoteDispatchDomainMemoryStats (CVE-2013-4296)
- Introduce APIs for splitting/joining strings (rhbz#1006266)
- Rename virKillProcess to virProcessKill (rhbz#1006266)
- Rename virPid{Abort, Wait} to virProcess{Abort, Wait} (rhbz#1006266)
- Rename virCommandTranslateStatus to virProcessTranslateStatus (rhbz#1006266)
- Move virProcessKill into virprocess.{h, c} (rhbz#1006266)
- Move virProcess{Kill, Abort, TranslateStatus} into virprocess.{c, h} (rhbz#1006266)
- Include process start time when doing polkit checks (rhbz#1006266)
- Add support for using 3-arg pkcheck syntax for process (CVE-2013-4311)

* Tue Sep 17 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-25
- migration: Do not restore labels on failed migration (rhbz#895826)
- qemu: Use default machine type if missing it in qemu command line (rhbz#995312)
- qemu: Don't leak vm on failure (rhbz#995312)
- virDomainDefParseXML: Set the argument of virBitmapFree to NULL after calling virBitmapFree (rhbz#1006710)
- tests: Files named '.*-invalid.xml' should fail validation (rhbz#1006710)
- tests: Use portable shell code (rhbz#1006710)
- Add test for the nodemask double free crash (rhbz#1006710)

* Fri Sep  6 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-24
- security: Provide supplemental groups even when parsing label (rhbz#964359)
- qemu: Remove hostdev entry when freeing the depending network entry (rhbz#1000973)
- virsh: Correct DESCRIPTION for virsh help blockcopy (rhbz#1002790)
- Add '<nat>' element to '<forward>' network schemas (rhbz#1004365)
- build: More workarounds for if_bridge.h (rhbz#1002735)

* Wed Aug 21 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-23
- virnettlscontext: Resolve Coverity warnings (UNINIT) (rhbz#975201)
- Fix qemuProcessReadLog with non-zero offset (rhbz#991334)
- virSecurityManagerGenLabel: Skip seclabels without model (rhbz#997818)
- bitmap: Add virBitmapCountBits (rhbz#997367)
- virbitmap: Refactor virBitmapParse to avoid access beyond bounds of array (rhbz#997367)
- virbitmaptest: Add test for out of bounds condition (rhbz#997367)
- network: Allow <vlan> in type='hostdev' networks (rhbz#999107)
- python: Fix bindings that don't raise an exception (rhbz#912170)
- storage: Update pool metadata after adding/removing/resizing volume (rhbz#965442)
- storage: Fix coverity warning (rhbz#965442)
- storage: Fix the use-after-free memory bug (rhbz#965442)
- network: Permit upstream forwarding of unqualified DNS names (rhbz#928638)

* Wed Aug 14 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-22
- virsh: Fix change-media bug on disk block type (rhbz#923053)
- Fix patches for multiple graphics and spice migration (rhbz#975751)
- Revert "qemu: Remove maximum cpu limit when setting processor count using the API" (rhbz#855296)
- Remove VIR_DOMAIN_SHUTDOWN_CRASHED from public API (rhbz#822306)
- Rename VIR_DOMAIN_PAUSED_GUEST_PANICKED to VIR_DOMAIN_PAUSED_CRASHED (rhbz#822306)
- Improve LXC startup error reporting (rhbz#903092)
- qemu: Take error path if acquiring of job fails in qemuDomainSaveInternal (rhbz#928661)
- util: Improve user lookup helper (rhbz#964359)
- util: Add virGetGroupList (rhbz#964359)
- util: Make virSetUIDGID async-signal-safe (rhbz#964359)
- Fix potential deadlock across fork() in QEMU driver (rhbz#964359)
- security: Framework for driver PreFork handler (rhbz#964359)
- security_dac: Compute supplemental groups before fork (rhbz#964359)
- security: Fix deadlock with prefork (rhbz#964359)
- Split TLS test into two separate tests (rhbz#975201)
- Avoid re-generating certs every time (rhbz#975201)
- Change data passed into TLS test cases (rhbz#975201)
- Fix validation of CA certificate chains (rhbz#975201)
- Fix parallel runs of TLS test suites (rhbz#975201)
- tests: Fix parallel runs of TLS test suites (rhbz#975201)

* Thu Jul 18 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-21
- conf: Avoid NULL deref for pmsuspended domain state (rhbz#822306)
- libvirt: Define domain crash event types (rhbz#822306)
- qemu: Refactor processWatchdogEvent (rhbz#822306)
- qemu: Expose qemuProcessShutdownOrReboot() (rhbz#822306)
- qemu: Implement 'oncrash' events when guest panicked (rhbz#822306)
- qemu: Implement 'oncrash' coredump events when guest panicked (rhbz#822306)
- conf: Fix a memory leak when parsing nat port XML nodes (rhbz#851455)
- security_manager: Fix comparison (rhbz#984793)
- qemu: Prevent crash of libvirtd without guest agent configuration (rhbz#984821)
- qemu: Fix double free of returned JSON array in qemuAgentGetVCPUs() (rhbz#984821)
- qemu_agent: Add support for appending arrays to commands (rhbz#924400)
- Add support for locking domain's memory pages (rhbz#947118)
- qemu: Implement support for locking domain's memory pages (rhbz#947118)
- qemu: Check for -realtime mlock=on|off support (rhbz#947118)
- qemu: Move memory limit computation to a reusable function (rhbz#947118)
- util: New virCommandSetMax(MemLock|Processes|Files) (rhbz#947118)
- qemu: Set RLIMIT_MEMLOCK when memoryBacking/locked is used (rhbz#947118)
- Add Gluster protocol as supported network disk backend (rhbz#849796)
- qemu: Add support for gluster protocol based network storage backend. (rhbz#849796)
- tests: Add tests for gluster protocol based network disks support (rhbz#849796)

* Mon Jul 15 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-20
- qemu: Don't force port=0 for SPICE (rhbz#975751)
- qemu: Refactor graphics code to not hardcode a single display (rhbz#975751)
- qemu: Graphics support for simultaneous one of each sdl, vnc, spice (rhbz#975751)
- qemu: Don't miss errors when changing graphics passwords (rhbz#975751)
- qemu: Allow seamless migration for domains with multiple graphics (rhbz#975751)
- qemu_migration: Move waiting for SPICE migration (rhbz#920205)
- util: Refactor iptables command construction into multiple steps (rhbz#851455)
- net: Support set public ip range for forward mode nat (rhbz#851455)
- net: Add support for specifying port range for forward mode nat (rhbz#851455)
- qemu_migrate: Dispose listen address if set from config (rhbz#971485)
- qemu: Remove maximum cpu limit when setting processor count using the API (rhbz#855296)
- qemu_agent: Introduce helpers for agent based CPU hot(un)plug (rhbz#924400)
- virsh-domain: Refactor cmdVcpucount and fix output on inactive domains (rhbz#924400)
- API: Introduce VIR_DOMAIN_VCPU_AGENT, for agent based CPU hot(un)plug (rhbz#924400)
- qemu: Implement request of vCPU state using the guest agent (rhbz#924400)
- qemu: Implement support for VIR_DOMAIN_VCPU_AGENT in qemuDomainSetVcpusFlags (rhbz#924400)
- qemuDomainGetVcpusFlags: Initialize ncpuinfo (rhbz#924400)
- Fix commit 29c1e913e459058c12d02b3f4b767b3dd428a498 (rhbz#924400)
- qemu: Make qemuMigrationIsAllowed more reusable (rhbz#972675)
- qemu: Cancel migration if guest encoutners I/O error while migrating (rhbz#972675)
- qemu: Forbid migration of machines with I/O errors (rhbz#972675)
- migration: Make erroring out on I/O error controllable by flag (rhbz#972675)
- migration: Don't propagate VIR_MIGRATE_ABORT_ON_ERROR (rhbz#972675)
- Paused domain should remain paused after migration (rhbz#972675)
- qemu: New vnc display sharing policy caps flag (rhbz#803602)
- conf: Add 'sharePolicy' attribute to graphics element for vnc (rhbz#803602)
- qemu: Add ', share=<policy>' to qemu commandline (rhbz#803602)
- virsh: Distinguish errors between missing argument and wrong option (rhbz#924596)
- virsh: Fix incorrect argument errors for long options (rhbz#924596)
- virsh: Resolve Coverity 'MISSING_BREAK' (rhbz#924596)
- virnetdev: Need to initialize 'pciConfigAddr' (rhbz#980339)
- qemu: Fix double free in qemuMigrationPrepareDirect (rhbz#977961)
- sec_manager: Refuse to start domain with unsupported seclabel (rhbz#947387)
- usb: Don't spoil decimal addresses (rhbz#981503)
- storage: Return -1 when fs pool can't be mounted (rhbz#983539)

* Mon Jul  8 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-19
- xen: Resolve resource leak with 'cpuset' (rhbz#888503)
- schema: Make the cpuset type reusable across schema files (rhbz#888503)
- schemas: Add schemas for more CPU topology information in the caps XML (rhbz#888503)
- conf: Split out NUMA topology formatting to simplify access to data (rhbz#888503)
- capabilities: Switch CPU data in NUMA topology to a struct (rhbz#888503)
- capabilities: Add additional data to the NUMA topology info (rhbz#888503)
- test: Add support for thread and core information for the test driver (rhbz#888503)
- xen: Initialize variable before using (rhbz#888503)
- xen: Actually fix the uninitialized variable (rhbz#888503)
- spice: Properly reserve tlsPort when no port specified (rhbz#913244)
- qemu_agent: Ignore expected EOFs (rhbz#892079)
- qemu: Nicer error message if live disk snapshot unsupported (rhbz#882077)
- qemu: Destroy domain on decompression binary error (rhbz#894723)
- qemu: Run lzop with '--ignore-warn' (rhbz#894723)
- Don't ignore return value of qemuProcessKill (rhbz#903238)
- Fix race condition when destroying guests (rhbz#903238)
- Log warning if storage magic matches, but version does not (rhbz#903248)
- Add lots of debugging to storage file probing code (rhbz#903248)
- Fix probing of QED file format (rhbz#903248)
- util: Add virendian.h macros (rhbz#903248)
- util: Use new virendian.h macros (rhbz#903248)
- storage: Rearrange functions (rhbz#903248)
- storage: Prepare for refactoring (rhbz#903248)
- storage: Refactor metadata lookup (rhbz#903248)
- storage: Don't follow backing chain symlinks too eagerly (rhbz#903248)
- storage: Test backing chain traversal (rhbz#903248)
- qemu: Check backing chains even when cgroup is omitted (rhbz#896013)
- python: Fix bindings for virDomainSnapshotGet{Domain,Connect} (rhbz#895882)
- qemu: Add checking in helpers for sgio setting (rhbz#908073)
- qemu: Merge qemuCheckSharedDisk into qemuAddSharedDisk (rhbz#908073)
- qemu: Record names of domain which uses the shared disk in hash table (rhbz#908073)
- qemu: Update shared disk table when reconnecting qemu process (rhbz#908073)
- qemu: Move the shared disk adding and sgio setting prior to attaching (rhbz#908073)
- qemu: Remove the shared disk entry if the operation is ejecting or updating (rhbz#908073)
- qemu: Fix the memory leak (rhbz#908073)
- Fix crash changing CDROM media (rhbz#908073)
- qemu: Avoid NULL dereference in qemuSharedDiskEntryFree (rhbz#908073)
- qemu: Do not set unpriv_sgio if neither supported nor requested (rhbz#914677)
- Use size_t instead of int for virDomainDefPtr struct (rhbz#896604)
- util: Add VIR_(APPEND|INSERT|DELETE)_ELEMENT (rhbz#896604)
- qemu: Fix QMP detection of QXL graphics (rhbz#896604)
- qemu: Add qemu vga devices caps and one cap to mark them usable (rhbz#896604)
- conf: Add optional attribte primary to video <model> element (rhbz#896604)
- qemu: Use newer -device video device in qemu commandline (rhbz#896604)
- tests: Add one -device video device testcase (rhbz#896604)
- qemu: Detect VGA_QXL capability correctly (rhbz#896604)
- qemu: Support ram bar size for qxl devices (rhbz#896604)
- conf: Don't leak 'primary' video property on error (rhbz#896604)
- storage: lvm: Don't overwrite lvcreate errors (rhbz#912179)
- storage: lvm: Lvcreate fails with allocation=0, don't do that (rhbz#912179)
- storage: Cleanup logical volume creation code (rhbz#912179)
- docs: Clarify semantics of sparse storage volumes (rhbz#912179)
- storage: Fix memory leak with regfree(reg) call. (rhbz#906299)
- storage: Resource resource leak using 'tmp_vols' (rhbz#906299)
- interface: Resolve resource leak wth 'tmp_iface_objs' (rhbz#906299)
- locking: Resolve resource leaks on non error path (rhbz#906299)
- selinux: Resolve resource leak using the default disk label (rhbz#906299)
- storage: Resolve resource leaks with cmd processing (rhbz#906299)
- domain_conf: Resolve resource leaks found by Valgrind (rhbz#906299)
- qemu_command: Resolve resource leaks found by Valgrind (rhbz#906299)
- storage: Need to add virCommandFree() (rhbz#906299)
- qemu: Fix startupPolicy regression (rhbz#896013)
- util: Retry NLM_F_REQUEST with different values of IFLA_EXT_MASK (rhbz#923963)
- security_manager: Don't manipulate domain XML in virDomainDefGetSecurityLabelDef (rhbz#923946)
- security: Don't add seclabel of type none if there's already a seclabel (rhbz#923946)
- libvirt_private.syms: Correctly export seclabel APIs (rhbz#923946)
- security_manager.c: Append seclabel iff generated (rhbz#923946)
- rpc: Fix client crash when server drops connection (rhbz#921538)
- storage: Fix volume cloning for logical volume. (rhbz#948678)
- qemu: Allow migration over IPv6 (rhbz#846013)
- qemu: Set IPv6 migration capability when dump-guest-core is present (rhbz#846013)
- remote: Don't call NULL closeFreeCallback (rhbz#911609)
- libvirt: Increase connection reference count for callbacks (rhbz#911609)
- virsh: Unregister the connection close notifier upon termination (rhbz#911609)
- virsh: Move cmdConnect from virsh-host.c to virsh.c (rhbz#911609)
- virsh: Register and unregister the close callback also in cmdConnect (rhbz#911609)
- rpc: Fix connection close callback race condition and memory corruption/crash (rhbz#911609)
- tests: Fix qemumonitorjsontest deadlock when the machine is under load (rhbz#951227)
- Avoid use of free'd memory in auto destroy callback (rhbz#950286)
- Fix crash in QEMU auto-destroy with transient guests (rhbz#950286)
- daemon: Fix leak after listing volumes (CVE-2013-1962)
- Don't try to add non-existant devices to ACL (rhbz#922153)
- Avoid spamming logs with cgroups warnings (rhbz#922153)
- audit: Properly encode device path in cgroup audit (rhbz#922203)
- qemu: Set correct migrate host in client_migrate_info (rhbz#920441)
- qemu: Fix crash in migration of graphics-less guests. (rhbz#920441)
- Fix F_DUPFD_CLOEXEC operation args (rhbz#961034)
- cgroup: Be robust against cgroup movement races (rhbz#903433)
- virsocket: Introduce virSocketAddrIsWildcard (rhbz#920441)
- qemuDomainMigrateGraphicsRelocate: Use then new virSocketAddrIsWildcard (rhbz#920441)
- virSocketAddrIsWildcard: Use IN6_IS_ADDR_UNSPECIFIED correctly (rhbz#920441)
- libvirt: lxc: Don't mkdir when selinux is disabled (rhbz#915485)
- Don't mount selinux fs in LXC if selinux is disabled (rhbz#915485)
- virsh: Don't print --(null) in vol-name and vol-pool (rhbz#924571)
- virsh: Fix docs for "virsh setmaxmem" (rhbz#924648)
- qemu: Remove managed save flag from VM when starting with --force-boot (rhbz#917510)
- qemu: Don't update count of vCPUs if hot-unplug has failed (rhbz#895424)
- conf: net: Fix deadlock if assignment of network def fails (rhbz#921777)
- RPC: Support up to 16384 cpus on the host and 4096 in the guest (rhbz#960683)
- conf: Don't fail to parse <boot> when parsing a single device (rhbz#895294)
- conf: Allow for non-contiguous device boot orders (rhbz#889961)
- qemuDomainChangeGraphics: Check listen address change by listen type (rhbz#976401)
- build: Fix build with -Werror (rhbz#976401)
- qemuDomainBlockStatsFlags: Guard disk lookup with a domain job (rhbz#916315)
- qemu: Don't fail to shutdown domains with unresponsive agent (rhbz#889635)
- qemu: Wrap controllers code into dummy loop (rhbz#870003)
- qemu: Add controllers in specified order (rhbz#870003)
- tests: Add test for controller order (rhbz#870003)
- bandwidth: Attach sfq to leaf node (rhbz#895340)
- bandwidth: Create hierarchical shaping classes (rhbz#895340)
- remote: Forbid default "/session" connections when using ssh transport (rhbz#847822)
- remote: Fix client crash when URI path is empty when using ssh (rhbz#847822)
- udev: Fix crash in libudev logging (rhbz#971904)
- iscsi: Don't leak portal string when starting a pool (rhbz#975392)
- storage: Avoid double virCommandFree in virStorageBackendLogicalDeletePool (rhbz#921387)
- manual: Fix copy-paste errors (rhbz#923613)
- esx: Support virtualHW version 9 (rhbz#955575)
- manual: Add info about migrateuri in virsh manual (rhbz#878765)
- conf: Fix cpumask leak in virDomainDefFree (rhbz#977430)
- qemu: Avoid leaking uri in qemuMigrationPrepareDirect (rhbz#977961)
- Document that runtime changes may be lost after S4 suspend (rhbz#872419)
- virsh iface-bridge: Ignore delay if stp is turned off (rhbz#892403)
- virsh: Obey pool-or-uuid spec when creating volumes (rhbz#970495)
- Add method for checking if a string is (probably) a log message (rhbz#954248)
- Convert QEMU driver to use virLogProbablyLogMessage (rhbz#954248)
- util: Escapes special characters in VIR_LOG_REGEX (rhbz#954248)
- qemu: Move QEMU log reading into a separate function (rhbz#954248)
- qemu: Ignore libvirt logs when reading QEMU error output (rhbz#954248)
- logging: Make log regexp more compact (and readable) (rhbz#954248)
- qemu: Do not report unsafe migration for local files (rhbz#913363)
- Plug leak in virCgroupMoveTask (rhbz#978352)
- Fix invalid read in virCgroupGetValueStr (rhbz#978356)
- pci: Initialize virtual_functions array pointer to avoid segfault (rhbz#980339)
- Node device driver: update driver name during dumpxml (rhbz#979330)

* Mon Jan 28 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-18
- rpc: Fix crash on error paths of message dispatching (CVE-2013-0170)
- spec: Disable libssh2 support (rhbz#513363)

* Wed Jan 23 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-17
- storage: Fix lvcreate parameter for backingStore. (rhbz#896398)
- qemu: Don't return success if creation of snapshot save file fails (rhbz#896403)
- qemu: Reject attempts to create snapshots with names containig '/' (rhbz#896403)

* Wed Jan 16 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-16
- qemu_agent: Remove agent reference only when disposing it (rhbz#892079)
- Add RESUME event listener to qemu monitor. (rhbz#894085)

* Wed Jan  9 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-15
- snapshot: conf: Make virDomainSnapshotIsExternal more reusable (rhbz#889407)
- snapshot: qemu: Separate logic blocks with newlines (rhbz#889407)
- snapshot: qemu: Fix segfault and vanishing snapshots when redefining (rhbz#889407)
- snapshot: qemu: Allow redefinition of external snapshots (rhbz#889407)
- util: Prepare helpers for unpriv_sgio setting (rhbz#878578)
- qemu: Add a hash table for the shared disks (rhbz#878578)
- docs: Add docs and rng schema for new XML tag sgio (rhbz#878578)
- conf: Parse and format the new XML (rhbz#878578)
- qemu: Set unpriv_sgio when starting domain and attaching disk (rhbz#878578)
- qemu: Check if the shared disk's cdbfilter conflicts with others (rhbz#878578)
- qemu: Relax hard RSS limit (rhbz#891653)

* Thu Jan  3 2013 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-14
- util: Add missing error log messages when failing to get netlink VFINFO (rhbz#889319)
- util: Fix functions that retrieve SRIOV VF info (rhbz#889319)
- util: Fix botched check for new netlink request filters (rhbz#889319)
- blockjob: Fix memleak that prevented block pivot (rhbz#888426)
- sanlock: Chown lease files as well (rhbz#820173)

* Wed Dec 19 2012 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-13
- network: Prevent dnsmasq from listening on localhost (rhbz#886821)
- sanlock: Re-add lockspace unconditionally (rhbz#820173)
- Fix "virsh create" example (rhbz#887187)
- docs: Fix some typos in examples (rhbz#887187)
- network: Don't require private addresses if dnsmasq uses SO_BINDTODEVICE (rhbz#882265)

* Wed Dec 12 2012 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-12
- qemu: Eliminate bogus error log when changing netdev's bridge (rhbz#885838)
- remote: Avoid the thread race condition (rhbz#866524)
- storage: Error out earlier if the volume target path already exists (rhbz#832302)
- dnsmasq: Fix parsing of the version number (rhbz#885727)
- qemu: Restart CPUs with valid async job type when doing external snapshots (rhbz#885081)
- examples: Fix balloon event callback (rhbz#884650)
- util: Don't fail virGetGroupIDByName when group not found (rhbz#883832)
- util: Don't fail virGetUserIDByName when user not found (rhbz#883832)
- util: Rework error reporting in virGet(User|Group)IDByName (rhbz#883832)
- util: Fix warning message in previous patch (rhbz#883832)

* Wed Dec  5 2012 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-11
- Fix uninitialized variable in virLXCControllerSetupDevPTS (rhbz#880064)
- storage: Fix device detach regression with cgroup ACLs (rhbz#876828)
- storage: Fix bug of fs pool destroying (rhbz#878400)
- qemu: Fix a crash when save file can't be opened (rhbz#880919)
- bitmap: Fix typo to use UL type of integer constant in virBitmapIsAllSet (rhbz#876415)
- virsh: Rewrite cmdDomDisplay (rhbz#878779)
- network: Fix crash when portgroup has no name (rhbz#879473)
- util: Capabilities detection for dnsmasq (rhbz#882265)
- util: New virSocketAddrIsPrivate function (rhbz#882265)
- network: Use dnsmasq --bind-dynamic when available (rhbz#882265)
- storage: Fix scsi detach regression with cgroup ACLs (rhbz#876828)
- libssh2_session: Support DSS keys as well (rhbz#878376)
- virsh: Fix error messages in iface-bridge (rhbz#878376)
- virsh: Check the return value of virStoragePoolGetAutostart (rhbz#878376)
- conf: Check the return value of virXPathNodeSet (rhbz#878376)
- conf: snapshot: Check return value of virDomainSnapshotObjListNum (rhbz#878376)
- util: Fix virBitmap allocation in virProcessInfoGetAffinity (rhbz#878376)
- virsh: Use correct sizeof when allocating cpumap (rhbz#878376)
- rpc: Don't destroy xdr before creating it in virNetMessageEncodeHeader (rhbz#878376)
- virsh: Do timing even for unusable connections (rhbz#878376)
- conf: Fix uninitialized variable in virDomainListSnapshots (rhbz#878376)
- Fix error handling in virSecurityManagerGetMountOptions (rhbz#878376)
- conf: Prevent crash with no uuid in cephx auth secret (rhbz#878376)
- conf: Fix virDomainNetGetActualDirect*() and BridgeName() (rhbz#881480)
- virsh: Report errors if arguments of the schedinfo command are incorrect (rhbz#882915)
- systemd: Require dbus service (rhbz#830201)
- spec: Require dbus-daemon when using libvirtd in Fedora (rhbz#830201)
- qemu: Don't free PCI device if adding it to activePciHostdevs fails (rhbz#877095)
- util: Slightly refactor PCI list functions (rhbz#877095)
- qemu: Fix memory (and FD) leak on PCI device detach (rhbz#877095)
- util: Do not keep PCI device config file open (rhbz#877095)
- node_memory: Improve the docs (rhbz#872656)
- node_memory: Do not fail if there is parameter unsupported (rhbz#872656)
- node_memory: Fix bug of node_memory_tune (rhbz#872656)

* Mon Nov 26 2012 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-10
- Add note about numeric domain names to manpage (rhbz#824253)
- Use virNetServerRun instead of custom main loop (rhbz#867246)
- qemu: Fix RBD attach regression (rhbz#878862)
- qemu: Stop recursive detection of image chains when an image is missing (rhbz#878862)
- Fix exiting of libvirt_lxc program on container quit (rhbz#879360)
- snapshot: qemu: Add support for external inactive snapshots (rhbz#876816)
- conf: Fix private symbols exported by files in conf (rhbz#876816)
- snapshot: qemu: Fix detection of external snapshots when deleting (rhbz#876816)
- snapshot: Require user to supply external memory file name (rhbz#876816)
- snapshot: Add two more filter sets to API (rhbz#876817)
- snapshot: Add virsh back-compat support for new filters (rhbz#876817)
- snapshot: Implement new filter sets (rhbz#876817)
- snapshot: Expose location through virsh snapshot-info (rhbz#876817)
- sanlock: Retry after EINPROGRESS (rhbz#820173)
- storage: Fix logical volume cloning (rhbz#879780)
- cpu: Add Intel Haswell cpu model (fix previous downstream definition) (rhbz#879282)
- virsh: Report error when taking a snapshot with empty --memspec argument (rhbz#879130)
- lxc: Don't crash if no security driver is specified in libvirt_lxc (rhbz#880064)
- lxc: Avoid segfault of libvirt_lxc helper on early cleanup paths (rhbz#880064)

* Mon Nov 19 2012 Jiri Denemark <jdenemar@redhat.com> - 0.10.2-9
- util: Improve error reporting from absolutePathFromBaseFile helper (rhbz#874860)
- storage: Fix broken backing chain (rhbz#874860)
- nodeinfo: Add check and workaround to guarantee valid cpu topologies (rhbz#874050)
- nodeinfotest: Add test data for 2 processor host with broken NUMA (rhbz#874050)
- nodeinfotest: Add test data from a AMD bulldozer machine. (rhbz#874050)
- virsh: save: Report an error if XML file can't be read (rhbz#876868)
- virsh: Fix uninitialized variable in cmdSnapshotEdit (rhbz#877303)
- qemu: Allow larger discrepency between memory & currentMemory in domain xml (rhbz#873134)

* Mon Nov 12 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-8.el6
- iohelper: Don't report errors on special FDs (rhbz#866369)
- esx: Yet another connection fix for 5.1 (rhbz#873538)
- qemu: Don't corrupt pointer in qemuDomainSaveMemory() (rhbz#873537)
- build: Place attributes in correct location (rhbz#873934)
- Introduce new VIR_DOMAIN_EVENT_SUSPENDED_API_ERROR event (rhbz#866388)
- qemu: Emit event if 'cont' fails (rhbz#866388)
- virsh: Make ,, escape parsing common (rhbz#874171)
- virsh: Add snapshot-create-as memspec support (rhbz#874171)
- qemu: Fix domain ID numbering race condition (rhbz#874330)
- qemu: Allow migration to be cancelled at prepare phase (rhbz#873792)
- AbortJob: Fix documentation (rhbz#873792)

* Mon Nov  5 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-7.el6
- sanlock: Introduce 'user' and 'group' conf variables (rhbz#820173)
- esx: Fix connection to ESX 5.1 (rhbz#865670)
- cpu: Fix definition of flag smap (rhbz#797283)
- util: Do a better job of matching up pids with their binaries (rhbz#871201)
- qemu: Fix EmulatorPinInfo without emulatorpin (rhbz#871312)
- build: Fix RPM build for non-x86 platforms (rhbz#820173)
- qemu: Report errors from iohelper (rhbz#866369)
- build: Fix linking with systemtap probes (rhbz#866369)
- iohelper: Fdatasync() at the end (rhbz#866369)
- net-update docs: S/domain/network/ (rhbz#872104)
- cpu: Add newly added cpu flags (rhbz#838127)
- cpu: Add AMD Opteron G5 cpu model (rhbz#838127)
- cpu: Add Intel Haswell cpu model (rhbz#843087)
- snapshot: New XML for external system checkpoint (rhbz#638512)
- snapshot: Improve disk align checking (rhbz#638512)
- snapshot: Populate new XML info for qemu snapshots (rhbz#638512)
- snapshot: Merge pre-snapshot checks (rhbz#638512)
- qemu: Fix possible race when pausing guest (rhbz#638512)
- qemu: Clean up snapshot retrieval to use the new helper (rhbz#638512)
- qemu: Split out domain memory saving code to allow reuse (rhbz#638512)
- snapshot: Add flag to enable creating checkpoints in live state (rhbz#638512)
- snapshot: qemu: Add async job type for snapshots (rhbz#638512)
- snapshot: qemu: Rename qemuDomainSnapshotCreateActive (rhbz#638512)
- snapshot: qemu: Add support for external checkpoints (rhbz#638512)
- snapshot: qemu: Remove restrictions preventing external checkpoints (rhbz#638512)

* Mon Oct 29 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-6.el6
- xml: Omit domain name from comment if it contains double hyphen (rhbz#868692)
- cpu: Add recently added cpu feature flags. (rhbz#797283)
- esx: Update version checks for vSphere 5.1 (rhbz#865670)
- qemu: Add helper to prepare cpumap for affinity setting (rhbz#869096)
- qemu: Keep the affinity when creating cgroup for emulator thread (rhbz#869096)
- qemu: Prohibit chaning affinity of domain process if placement is 'auto' (rhbz#870099)
- network: Fix networkValidate check for default portgroup and vlan (rhbz#868483)
- qemu: Fix attach/detach of netdevs with matching mac addrs (rhbz#862515)
- snapshot: Improve snapshot-list error message (rhbz#869100)
- virsh: Remove --flags from nodesuspend (rhbz#869508)
- virsh: Fix POD syntax (rhbz#870273)
- xml: Print uuids in the warning (rhbz#868692)
- blockjob: Support both RHEL and upstream qemu drive-mirror (rhbz#871055)

* Tue Oct 23 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-5.el6
- qemu: Clear async job when p2p migration fails early (rhbz#867412)
- qemu: Pin the emulator when only cpuset is specified (rhbz#867372)
- qemu: Correctly wait for spice to migrate (rhbz#867724)
- qemu: Fixed default machine detection in qemuCapsParseMachineTypesStr (rhbz#867764)
- conf: Make tri-state feature options more universal (rhbz#864606)
- conf: Add support for HyperV Enlightenment features (rhbz#864606)
- qemu: Add support for HyperV Enlightenment feature "relaxed" (rhbz#864606)
- network: Set to NULL after virNetworkDefFree() (rhbz#866364)
- qemu: Always format CPU topology (rhbz#866999)
- qemu: Don't fail without emulatorpin or cpumask (rhbz#867372)
- qemu: Allow migration with host USB devices (rhbz#843560)
- qemu: Do not require hostuuid in migration cookie (rhbz#863059)
- network: Free/null newDef if network fails to start (rhbz#866364)
- migrate: v2: Use VIR_DOMAIN_XML_MIGRATABLE when available (rhbz#856864)
- qemu: Avoid holding the driver lock in trivial snapshot API's (rhbz#772088)
- storage: List more file types (rhbz#772088)
- storage: Treat 'aio' like 'raw' at parse time (rhbz#772088)
- storage: Match RNG to supported driver types (rhbz#772088)
- storage: Use enum for default driver type (rhbz#772088)
- storage: Use enum for disk driver type (rhbz#772088)
- storage: Use enum for snapshot driver type (rhbz#772088)
- storage: Don't probe non-files (rhbz#772088)
- storage: Get entire metadata chain in one call (rhbz#772088)
- storage: Don't require caller to pre-allocate metadata struct (rhbz#772088)
- storage: Remember relative names in backing chain (rhbz#772088)
- storage: Make it easier to find file within chain (rhbz#772088)
- storage: Cache backing chain while qemu domain is live (rhbz#772088)
- storage: Use cache to walk backing chain (rhbz#772088)
- blockjob: Remove unused parameters after previous patch (rhbz#772088)
- blockjob: Manage qemu block-commit monitor command (rhbz#772088)
- blockjob: Wire up online qemu block-commit (rhbz#772088)
- blockjob: Implement shallow commit flag in qemu (rhbz#772088)
- blockjob: Refactor qemu disk chain permission grants (rhbz#772088)
- blockjob: Properly label disks for qemu block-commit (rhbz#772088)
- blockjob: Avoid segv on early error (rhbz#772088)
- blockjob: Accommodate early RHEL backport naming (rhbz#772088)
- virsh: Fix segfault of snapshot-list (rhbz#837544)
- network: Always create dnsmasq hosts and addnhosts files, even if empty (rhbz#868389)
- network: Don't allow multiple default portgroups (rhbz#868483)
- selinux: Use raw contexts (rhbz#851981)
- selinux: Add security selinux function to label tapfd (rhbz#851981)
- selinux: Use raw contexts 2 (rhbz#851981)
- selinux: Fix wrong tapfd relablling (rhbz#851981)
- selinux: Remove unused variables in socket labelling (rhbz#851981)
- selinux: Relabel tapfd in qemuPhysIfaceConnect (rhbz#851981)
- storage: Let format probing work on root-squash NFS (rhbz#856247)
- snapshot: Sanity check when reusing file for snapshot (rhbz#856247)
- blockjob: Add qemu capabilities related to block jobs (rhbz#856247)
- blockjob: React to active block copy (rhbz#856247)
- blockjob: Return appropriate event and info (rhbz#856247)
- blockjob: Support pivot operation on cancel (rhbz#856247)
- blockjob: Make drive-reopen safer (rhbz#856247)
- blockjob: Implement block copy for qemu (rhbz#856247)
- blockjob: Allow for existing files in block-copy (rhbz#856247)
- blockjob: Allow mirroring under SELinux and cgroup (rhbz#856247)
- blockjob: Relabel entire existing chain (rhbz#856247)

* Wed Oct 17 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-4.el6
- node_memory: Add new parameter field to tune the new sysfs knob (rhbz#840113)
- daemon: Fix removing abstract namespaces (rhbz#859331)
- tests: Fix domain-events python test (rhbz#839661)
- conf: Fix crash with cleanup (rhbz#866288)
- spec: Add runtime requirement for libssh2 (rhbz#866508)
- spec: Require newer sanlock on recent distros (rhbz#832156)
- spec: Require newer sanlock on recent distros 2 (rhbz#832156)

* Mon Oct 15 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-3.el6
- conf: Rename life cycle actions to event actions (rhbz#832156)
- conf: Add on_lockfailure event configuration (rhbz#832156)
- locking: Add const char * parameter to avoid ugly typecasts (rhbz#832156)
- locking: Pass hypervisor driver name when acquiring locks (rhbz#832156)
- locking: Add support for lock failure action (rhbz#832156)
- locking: Implement lock failure action in sanlock driver (rhbz#832156)
- conf: Add support for startupPolicy for USB devices (rhbz#843560)
- qemu: Introduce qemuFindHostdevUSBDevice (rhbz#843560)
- qemu: Add option to treat missing USB devices as success (rhbz#843560)
- qemu: Implement startupPolicy for USB passed through devices (rhbz#843560)
- Add MIGRATABLE flag for virDomainGetXMLDesc (rhbz#843560)
- qemu: Make save/restore with USB devices usable (rhbz#843560)
- conf: Mark missing optional USB devices in domain XML (rhbz#843560)
- security: Also parse user/group names instead of just IDs for DAC labels (rhbz#860519)
- doc: Update description about security labels on formatdomain.html (rhbz#860519)
- util: Extend virGetUserID and virGetGroupID to support names and IDs (rhbz#860519)
- security: Update user and group parsing in security_dac.c (rhbz#860519)
- doc: Update description about user/group in qemu.conf (rhbz#860519)
- Fix kvm_pv_eoi with kvmclock (rhbz#860971)
- Change qemuSetSchedularParameters to use AFFECT_CURRENT (rhbz#852260)
- Fix handling of itanium arch name in QEMU driver (rhbz#863115)
- Add a qemu capabilities cache manager (rhbz#863115)
- Switch over to use cache for building QEMU capabilities (rhbz#863115)
- Remove probing of flags when launching QEMU guests (rhbz#863115)
- Remove probing of machine types when canonicalizing XML (rhbz#863115)
- Remove probing of CPU models when launching QEMU guests (rhbz#863115)
- Make qemuCapsProbeMachineTypes & qemuCapsProbeCPUModels static (rhbz#863115)
- Remove xenner support (rhbz#863115)
- Refactor guest init to support qemu-system-i386 binary too (rhbz#863115)
- Add a qemuMonitorGetVersion() method for QMP query-version command (rhbz#863115)
- Add a qemuMonitorGetMachines() method for QMP query-machines command (rhbz#863115)
- Add a qemuMonitorGetCPUDefinitions method for QMP query-cpu-definitions command (rhbz#863115)
- Add a qemuMonitorGetCommands() method for QMP query-commands command (rhbz#863115)
- Add a qemuMonitorGetEvents() method for QMP query-events command (rhbz#863115)
- Add a qemuMonitorGetObjectTypes() method for QMP qom-list-types command (rhbz#863115)
- Add a qemuMonitorGetObjectProps() method for QMP device-list-properties command (rhbz#863115)
- Add a qemuMonitorGetTargetArch() method for QMP query-target command (rhbz#863115)
- Remove some unused includes in QEMU code (rhbz#863115)
- Move command/event capabilities detection out of QEMU monitor code (rhbz#863115)
- Fix regression starting QEMU instances without query-events (rhbz#863115)
- Refactor qemuCapsParseDeviceStr to work from data tables (rhbz#863115)
- Fix QEMU test with 1.2.0 help output (rhbz#863115)
- Ignore error from query-cpu-definitions (rhbz#863115)
- Fix potential deadlock when agent is closed (rhbz#859712)
- Fix (rare) deadlock in QEMU monitor callbacks (rhbz#859712)
- Convert virLXCMonitor to use virObject (rhbz#864336)
- Remove pointless virLXCProcessMonitorDestroy method (rhbz#864336)
- Simplify some redundant locking while unref'ing objects (rhbz#859712)
- Fix deadlock in handling EOF in LXC monitor (rhbz#864336)
- Avoid bogus I/O event errors when closing the QEMU monitor (rhbz#859712)
- qemu: Fix parsing of x86 CPU models (rhbz#864097)
- python: Keep consistent handling of Python integer conversion (rhbz#816609)
- esx: Fix and improve esxListAllDomains function (rhbz#864384)
- virsh: Block SIGINT while getting BlockJobInfo (rhbz#845448)
- spec: Add support for libssh2 transport (rhbz#513363)
- Revert "Use XDG Base Directories instead of storing in home directory" (rhbz#859331)
- doc: Sort out the relationship between <vcpu>, <vcpupin>, and <emulatorpin> (rhbz#855218)
- conf: Ignore vcpupin for not onlined vcpus when parsing (rhbz#855218)
- conf: Initialize the pinning policy for vcpus (rhbz#855218)
- qemu: Create or remove cgroup when doing vcpu hotpluging (rhbz#857013)
- qemu: Initialize cpuset for hotplugged vcpu as def->cpuset (rhbz#855218)
- conf: Ignore emulatorpin if vcpu placement is auto (rhbz#855218)
- qemu: Ignore def->cpumask if emulatorpin is specified (rhbz#855218)
- Avoid straying </cpuset> (rhbz#855218)
- conf: Fix virDevicePCIAddressEqual args (rhbz#805071)
- conf: VirDomainDeviceInfoCopy utility function (rhbz#805071)
- qemu: Reorganize qemuDomainChangeNet and qemuDomainChangeNetBridge (rhbz#805071)
- Add support for SUSPEND_DISK event (rhbz#839661)

* Mon Oct  8 2012 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.10.2-2.el6
- qemu: Wait for SPICE to migrate (rhbz#836135)
- lxc: Correctly report active cgroups (rhbz#860907)
- network: Backend for virNetworkUpdate of interface list (rhbz#844404)
- Fix start of containers with custom root filesystem (rhbz#861564)
- Correct checking of virStrcpyStatic() return value (rhbz#864122)

* Mon Sep 24 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.2-1.el6
- New build based on upstream release 0.10.2 (rhbz#836934)
- network: define new API virNetworkUpdate
- add support for QEmu sandbox support
- blockjob: add virDomainBlockCommit
- New APIs to get/set Node memory parameters
- new API virConnectListAllSecrets
- new API virConnectListAllNWFilters
- new API virConnectListAllNodeDevices
- new API virConnectListAllInterfaces
- new API virConnectListAllNetworks
- new API virStoragePoolListAllVolumes
- Add PMSUSPENDED life cycle event
- new API virStorageListAllStoragePools
- Add per-guest S3/S4 state configuration
- qemu: Support for Block Device IO Limits
- a lot of bug fixes, improvements and portability work

* Tue Sep 18 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.2-0rc1.el6
- New build based on upstream release candidate 1 of 0.10.2 (rhbz#836934)

* Thu Sep 13 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.1-2.el6
- Don't assume use of /sys/fs/cgroup (rhbz#842979)

* Fri Aug 31 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.1-1.el6
- New build based on upstream release 0.10.1 (rhbz#836934)
- many fixes on top of 0.10.0

* Wed Aug 29 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.0-1.el6
- New build based on upstream release 0.10.0 (rhbz#836934)
- agent: add qemuAgentArbitraryCommand() for general qemu agent command
- Introduce virDomainPinEmulator and virDomainGetEmulatorPinInfo functions
- network: use firewalld instead of iptables, when available
- network: make network driver vlan-aware
- esx: Implement network driver
- Various LXC improvements
- Add virDomainGetHostname
- a lot of bug fixes, improvements and portability work

* Thu Aug 23 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.0-0rc1.el6
- New build based on upstream snapshot 0.10.0-0rc1 (rhbz#836934)

* Wed Aug  1 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.10.0-0rc0.el6
- New build based on upstream snapshot 0.10.0-0rc0 (rhbz#836934)
- Cleanup and rebase of the few RHEL-only patches

* Fri Jul 20 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.13-3.el6
- fix the package split to be similar to 6.3 one instead of upstream

* Tue Jul  3 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.13-2.el6
- fix a package dependency problem making -1 uninstallable

* Tue Jul  3 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.13-1.el6
- first rebase for 6.4 more to come
- kvm-guest failed to start; double-close bug in libvirt (rhbz#823716)
- potential to deadlock libvirt on EPIPE (rhbz#827234)
- fix keepalive issues (rhbz#832081)
- CPU topology parsing bug on special NUMA platform (rhbz#828729)
- libvirtd will crash when tight loop of hotplug/unplug PCI device (rhbz#822373)

* Thu Jun 14 2012 Eric Blake <eblake@redhat.com> - libvirt-0.9.10-21.el6_3.1
- avoid closing uninitialized fd (rhbz#827050)
- avoid fd leak (rhbz#827050)
- command: avoid double close bugs (rhbz#827050)
- fdstream: avoid double close bug (rhbz#827050)
- command: check for fork error before closing fd (rhbz#827050)
- qemu: avoid closing fd more than once (rhbz#827050)
- Disable keepalives by default (rhbz#832184)

* Wed May 23 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-21.el6
- qemu: Rollback on used USB devices (rhbz#743671)
- qemu: Don't delete USB device on failed qemuPrepareHostdevUSBDevices (rhbz#743671)
- Revert "rpc: Discard non-blocking calls only when necessary" (rhbz#821468)

* Wed May 16 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-20.el6
- Fix virDomainDeviceInfoIsSet() to check all struct fields (rhbz#820869)
- Fix logic for assigning PCI addresses to USB2 companion controllers (rhbz#820869)
- Set a sensible default master start port for ehci companion controllers (rhbz#820869)

* Tue May 15 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-19.el6
- build: Fix the typo in configure.ac (rhbz#820461)
- qemu: Fix build when !HAVE_NUMACTL (rhbz#820461)
- usb: Fix crash when failing to attach a second usb device (rhbz#815755)
- qemu: Use the CPU index in capabilities to map NUMA node to cpu list. (rhbz#820461)
- qemu: Set memory policy using cgroup if placement is auto (rhbz#820461)

* Wed May  9 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-18.el6
- numad: Set memory policy from numad advisory nodeset (rhbz#810157)
- numad: Copy 'placement' of <numatune> to <vcpu> by default (rhbz#810157)
- numad: Always output 'placement' of <vcpu> (rhbz#810157)
- qemu: Avoid the memory allocation and freeing (rhbz#810157)
- numad: Divide cur_balloon by 1024 before passing it to numad (rhbz#810157)
- numad: Check numactl-devel if compiled with numad support (rhbz#810157)

* Wed May  9 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-17.el6
- qemu: Don't modify domain on failed blockiotune (rhbz#819014)
- qemu: Reject blockiotune if qemu too old (rhbz#819014)
- qemu: Don't use virDomainDefFormat* directly (rhbz#815503)
- qemu: Emit compatible XML when migrating a domain (rhbz#815503)
- usb: Create functions to search usb device accurately (rhbz#815755)
- qemu: Call usb search function for hostdev initialization and hotplug (rhbz#815755)
- virsh: Avoid heap corruption leading to virsh abort (rhbz#819636)
- util: Fix libvirtd startup failure due to netlink error (rhbz#816465)
- util: Allow specifying both src and dst pid in virNetlinkCommand (rhbz#816465)
- util: Function to get local nl_pid used by netlink event socket (rhbz#816465)
- util: Set src_pid for virNetlinkCommand when appropriate (rhbz#816465)
- domain_conf: Add "usbredir" to list of valid spice channels (rhbz#819498)
- domain_conf: Add "default" to list of valid spice channels (rhbz#819499)
- snapshot: Allow block devices past cgroup (rhbz#810200)
- blockjob: Allow block devices past cgroup (rhbz#810200)
- util: Avoid libvirtd crash in virNetDevTapCreate (rhbz#817234)
- python: Fix the forward_null error in Python binding codes (rhbz#771021)
- xen: Fix resource leak in xen driver (rhbz#771021)
- test: Fix resource leak in test driver (rhbz#771021)
- node: Fix resource leak in nodeinfo.c (rhbz#771021)
- virnet: Fix resource leak in virnetlink.c (rhbz#771021)
- vmx: Fix resource leak (rhbz#771021)
- qemu: Fix resource leak (rhbz#771021)
- uuid: Fix possible non-terminated string (rhbz#771021)
- node_device: Fix possible non-terminated string (rhbz#771021)

* Wed May  2 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-16.el6
- qemuOpenFile: Don't force chown on NFS (rhbz#810241)
- util: Fix crash when starting macvtap interfaces (rhbz#815270)
- qemu: Fix segfault when host CPU is empty (rhbz#817078)
- blockjob: Allow speed setting in block copy (rhbz#815791)
- blockjob: Fix block-stream bandwidth race (rhbz#815791)

* Tue May  1 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-15.el6
- qemu: Improve errors related to offline domains (rhbz#816662)
- blockjob: Check for active vm before checking blockcopy bits (rhbz#816662)
- qemu: Preserve original error during migration (rhbz#807907)
- rpc: Discard non-blocking calls only when necessary (rhbz#807907)
- qemu: Fix detection of failed migration (rhbz#807907)
- qemu: Avoid bogus error at the end of tunnelled migration (rhbz#807907)
- qemu: Make sure qemu can access its directory in hugetlbfs (rhbz#815206)
- virsh: Fix docs for list command (rhbz#814021)
- virsh: Fix and clarify the --title flag for the list command in man page (rhbz#814021)

* Tue Apr 24 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-14.el6
- blockjob: Add new API flags (rhbz#638506)
- blockjob: Add 'blockcopy' to virsh (rhbz#638506)
- blockjob: Enhance xml to track mirrors across libvirtd restart (rhbz#638506)
- blockjob: React to active block copy (rhbz#638506)
- blockjob: Add qemu capabilities related to block jobs (rhbz#638506)
- blockjob: Return appropriate event and info (rhbz#638506)
- blockjob: Support pivot operation on cancel (rhbz#638506)
- blockjob: Make drive-reopen safer (rhbz#638506)
- blockjob: Implement block copy for qemu (rhbz#638506)
- blockjob: Allow for existing files (rhbz#638506)
- blockjob: Allow mirroring under SELinux (rhbz#638506)
- blockjob: Accommodate RHEL backport names (rhbz#638506)
- virsh: Avoid strtol (rhbz#813972)
- conf: Tighten up XML integer parsing (rhbz#813972)
- snapshot: Fix memory leak on error (rhbz#782457)
- virsh: Avoid uninitialized memory usage (rhbz#814080)

* Thu Apr 19 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-13.el6
- Fix a problem in the patchset, rhbz#811497 one was applied twice in -12
- qemu, util: On restart of libvirt restart vepa callbacks (rhbz#812430)
- qemu, util: Fix netlink callback registration for migration (rhbz#812430)
- util: Only register callbacks for CREATE operations in virnetdevmacvlan.c (rhbz#812430)

* Wed Apr 18 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-12.el6
- blockjob: Add qemu capabilities related to block pull jobs (rhbz#811683)
- blockjob: Add API for async virDomainBlockJobAbort (rhbz#811683)
- blockjob: Optimize JSON event handler lookup (rhbz#811683)
- blockjob: Wire up qemu async virDomainBlockJobAbort (rhbz#811683)
- blockjob: Allow for fast-finishing job (rhbz#811683)
- virsh: Minor syntactic cleanups (rhbz#811683)
- qemu: Use consistent error when qemu binary is too old (rhbz#811683)
- blockjob: Add virsh blockpull --wait (rhbz#811683)
- qemu: Fix deadlock when qemuDomainOpenConsole cleans up a connection (rhbz#811497)
- qemu: Fix deadlock when qemuDomainOpenConsole cleans up a connection (rhbz#811497)
- qemu: Fix mem leak in qemuProcessInitCpuAffinity (rhbz#810157)
- numad: Convert node list to cpumap before setting affinity (rhbz#810157)
- numad: Ignore cpuset if placement is auto (rhbz#810157)
- conf: Do not parse cpuset only if the placement is auto (rhbz#810157)

* Wed Apr 11 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-11.el6
- test: Fix segfault in networkxml2argvtest (rhbz#810100)
- conf: Plug memory leaks on virDomainDiskDefParseXML (rhbz#575160)
- qemu_ga: Don't overwrite errors on FSThaw (rhbz#808527)
- Fix parallel build in docs/ directory (rhbz#810559)
- qemu: Make migration fail when port profile association fails on the dst host (rhbz#811026)
- Wire up <loader> to set the QEMU BIOS path (rhbz#811227)

* Thu Apr  5 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-10.el6
- python: Add new helper functions for python to C conversion (rhbz#807751)
- python: Make python APIs use these helper functions (rhbz#807751)
- python: Improve conversion validation (rhbz#807751)
- qemu_agent: Issue guest-sync prior to every command (rhbz#808527)
- qemu: Fix memory leak in virDomainGetVcpus (rhbz#808979)
- qemu: Reflect any memory rounding back to xml (rhbz#808522)
- conf: Allow fuzz in XML with cur balloon > max (rhbz#808522)
- qemu: Start nested job in qemuDomainCheckEjectableMedia (rhbz#803186)
- virsh: Clarify escape sequence (rhbz#808652)
- virsh: Plug memory leaks on failure path (rhbz#807555)
- conf: Prevent crash of libvirtd without channel target name (rhbz#808371)
- qemu: Don't leak temporary list of USB devices (rhbz#808459)
- qemu: Delete USB devices used by domain on stop (rhbz#808459)
- qemu: Build activeUsbHostdevs list on process reconnect (rhbz#808459)
- qemu: Fix virtio+macvtap migration from 6.3 to older hosts (rhbz#806633)

* Thu Mar 29 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-9.el6
- qemu: Avoid entering monitor with locked driver (rhbz#803186)
- snapshot: Don't pass NULL to QMP command creation (rhbz#807147)

* Mon Mar 26 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-8.el6
- rebuild, forgot to apply part of the patch
- spec: Add missed dependancy for numad (rhbz#769930)

* Mon Mar 26 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-7.el6
- snapshot: Make quiesce a bit safer (rhbz#804210)
- python: Avoid memory leaks on libvirt_virNodeGetMemoryStats (rhbz#770944)
- qemu: Use unlimited speed when migrating to file (rhbz#740099)
- qemu: Add support for domain cleanup callbacks (rhbz#795305)
- qemu: Avoid dangling migration-in job on shutoff domains (rhbz#795305)
- qemu: Add connection close callbacks (rhbz#795305)
- qemu: Make autodestroy utilize connection close callbacks (rhbz#795305)
- qemu: Avoid dangling migration-out job when client dies (rhbz#795305)
- python: Avoid memory leaks on libvirt_virNodeGetCPUStats (rhbz#770943)
- util: Consolidate duplicated error messages in virnetlink.c (rhbz#693842)
- python: Add virDomainGetCPUStats python binding API (rhbz#800366)
- snapshot: Add qemu capability for 'transaction' command (rhbz#782457)
- snapshot: Add atomic create flag (rhbz#782457)
- snapshot: Make offline qemu snapshots atomic (rhbz#782457)
- snapshot: Rudimentary qemu support for atomic disk snapshot (rhbz#782457)
- snapshot: Add support for qemu transaction command (rhbz#782457)
- snapshot: Wire up qemu transaction command (rhbz#782457)
- snapshot: Improve qemu handling of reused snapshot targets (rhbz#782457)
- Clarify virsh freecell manpage entry (rhbz#698521)
- Add support for event tray moved of removable disks (rhbz#575160)
- docs: Add documentation for new attribute tray of disk target (rhbz#575160)
- conf: Parse and for the tray attribute (rhbz#575160)
- qemu: Do not start with source for removable disks if tray is open (rhbz#575160)
- qemu: Prohibit setting tray status as open for block type disk (rhbz#575160)
- qemu: Update tray status while tray moved event is emitted (rhbz#575160)
- build: Fix incorrect enum declaration (rhbz#575160)
- spec: Add missed dependancy for numad (rhbz#769930)

* Mon Mar 19 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-6.el6
- cpu: Add new flag supported by qemu to the cpu definition (rhbz#767364)
- Added support for AMD Bulldozer CPU (rhbz#767364)
- graphics: Cleanup port policy (rhbz#801443)
- qemu: Reverse condition in qemuDomainCheckDiskPresence (rhbz#798938)
- cpu: Add cpu definition for Intel Sandy Bridge cpu type (rhbz#761005)
- cpu: Disable tsc-deadline feature not supported in qemu on RHEL 6.3 (rhbz#761005)
- qemu: Support numad (rhbz#769930)
- numad: Fix typo and warning (rhbz#769930)
- qemu: Use scsi-block for lun passthrough instead of scsi-disk (rhbz#782034)
- util: Make virDomainLeaseDefFree global (rhbz#802851)
- qemu: Don't 'remove' hostdev objects from domain if operation fails (rhbz#802851)
- util: Eliminate device object leaks related to virDomain*Remove*() (rhbz#802851)
- virsh: Fix invalid free (rhbz#803591)
- qemu: Eliminate memory leak in qemuDomainUpdateDeviceConfig (rhbz#802854)
- qemu: Support persistent hotplug of <hostdev> devices (rhbz#802856)
- qemu: Fix segfault when detaching non-existent network device (rhbz#802644)
- remote: Fix migration leaks (rhbz#798497)
- virsh: Trim aliases from -h output (rhbz#796526)
- Fix handling of blkio deviceWeight empty string (rhbz#804028)

* Tue Mar 13 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-5.el6
- Avoid global variable shadowed (rhbz#737726)
- Add nodeGetCPUmap() for getting available CPU IDs in a cpumap. (rhbz#737726)
- Qemu driver for virDomainGetCPUstats using cpuacct cgroup. (rhbz#737726)
- Cpu-stats command shows cpu statistics information of a domain. (rhbz#737726)
- Ensure max_id is initialized in linuxParseCPUmap() (rhbz#737726)
- rpc: Allow truncated return for virDomainGetCPUStats (rhbz#737726)
- qemu: Don't parse device twice in attach/detach (rhbz#770031)
- sanlock: Fix condition left crippled while debugging (rhbz#785736)
- sanlock: Use STREQ_NULLABLE instead of STREQ on strings that may be null (rhbz#785736)
- qemu: Fix startupPolicy for snapshot-revert (rhbz#798938)
- util: Don't overflow on errno in virFileAccessibleAs (rhbz#798938)
- blockResize: Add flag for bytes (rhbz#796526)
- docs: Use correct terminology for 1024 bytes (rhbz#796526)
- api: Add overflow error (rhbz#796526)
- util: New function for scaling numbers (rhbz#796526)
- xml: Share 'unit' in RNG (rhbz#796526)
- xml: Output memory unit for clarity (rhbz#796526)
- storage: Support more scaling suffixes (rhbz#796526)
- xml: Drop unenforced minimum memory limit from RNG (rhbz#796526)
- xml: Use long long internally, to centralize overflow checks (rhbz#796526)
- xml: Use better types for memory values (rhbz#796526)
- xml: Allow scaled memory on input (rhbz#796526)
- virsh: Add option aliases (rhbz#796526)
- virsh: Use option aliases (rhbz#796526)
- virsh: Add command aliases, and rename nodedev-detach (rhbz#796526)
- virsh: Improve storage unit parsing (rhbz#796526)
- virsh: Improve memory unit parsing (rhbz#796526)
- qemuBuildCommandLine: Don't add tlsPort if none set (rhbz#801443)
- Removed more AMD-specific features from cpu64-rhel* models (rhbz#768450)
- qemu: Support disk filenames with comma (rhbz#801970)
- cpustats: Collect VM user and sys times (miss python bindings) (rhbz#800366)
- cpustats: Report user and sys times (rhbz#800366)
- qemu: Fix (managed)save and snapshots with host mode CPU (rhbz#801160)
- qemu: Make block io tuning smarter (rhbz#770683)

* Tue Mar  6 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-4.el6
- Improve error reporting when virsh console is run without a TTY (rhbz#729940)
- pidfile: Make checking binary path in virPidFileRead optional (rhbz#729940)
- Add flags for virDomainOpenConsole (rhbz#729940)
- virsh: Add support for VIR_DOMAIN_CONSOLE_* flags (rhbz#729940)
- fdstream: Emit stream abort callback even if poll() doesnt. (rhbz#729940)
- fdstream: Add internal callback on stream close (rhbz#729940)
- util: Add helpers for safe domain console operations (rhbz#729940)
- qemu: Add ability to abort existing console while creating new one (rhbz#729940)
- Fixed service handling in specfile (rhbz#786770)
- qemu: Don't emit tls-port spice option if port is -1 (rhbz#798220)
- docs: Comments wiping supported algorithms (rhbz#725013)
- libvirt-guests: Add documentation and clean up to use virsh's improved list (rhbz#693758)
- libvirt-guests: Don't try to do a managed-save of transient guests (rhbz#693758)
- virsh: Enhance list command to ease creation of shell scripts (rhbz#693758)
- libvirt-guests: Check if URI is reachable before launching commands (rhbz#720691)
- hooks: Add support for capturing hook output (rhbz#795127)
- qemu: Add pre-migration hook (rhbz#795127)
- Support for cpu64-rhel* qemu cpu models (rhbz#768450)
- util: Add netlink event handling to virnetlink.c (rhbz#693842)
- Add de-association handling to macvlan code (rhbz#693842)
- qemu: Add ibmvscsi controller model (rhbz#782034)
- qemu: Add virtio-scsi controller model (rhbz#782034)
- conf: Add helper function to look up disk controller model (rhbz#782034)
- conf: Introduce new attribute for device address format (rhbz#782034)
- qemu: New cap flag to indicate if channel is supported by scsi-disk (rhbz#782034)
- qemu: Build command line for the new address format (rhbz#782034)
- tests: Add tests for virtio-scsi and ibmvscsi controllers (rhbz#782034)
- virsh: Two new helper functions for disk device changes (rhbz#713932)
- virsh: Use vshFindDisk and vshPrepareDiskXML in cmdDetachDisk (rhbz#713932)
- virsh: New command cmdChangeMedia (rhbz#713932)
- qemu: Require json for block jobs (rhbz#799055)
- qemu: Pass block pull backing file to monitor (rhbz#799055)
- virsh: Expose partial pull (rhbz#799055)
- libvirt-guests: Add parallel startup and shutdown of guests (rhbz#625362)
- qemu: Shared or readonly disks are always safe wrt migration (rhbz#751631)
- util: Eliminate crash in virNetDevMacVLanCreateWithVPortProfile (rhbz#693842)
- rpc: Fix client crash on connection close (rhbz#800185)
- conf: Add missing device types to virDomainDevice(Type|Def) (rhbz#691539)
- conf: Relocate virDomainDeviceDef and virDomainHostdevDef (rhbz#691539)
- conf: Reorder static functions in domain_conf.c (rhbz#691539)
- qemu: Rename virDomainDeviceInfoPtr variables to avoid confusion (rhbz#691539)
- conf: Add device pointer to args of virDomainDeviceInfoIterate callback (rhbz#691539)
- conf: Make hostdev info a separate object (rhbz#691539)
- conf: HostdevDef parse/format helper functions (rhbz#691539)
- conf: Give each hostdevdef a parent pointer (rhbz#691539)
- conf: Put subsys part of virDomainHostdevDef into its own struct (rhbz#691539)
- conf: Hostdev utility functions (rhbz#691539)
- qemu: Re-order functions in qemu_hotplug.c (rhbz#691539)
- qemu: Refactor hotplug detach of hostdevs (rhbz#691539)
- conf: Parse/format type='hostdev' network interfaces (rhbz#691539)
- qemu: Support type='hostdev' network devices at domain start (rhbz#691539)
- conf: Change virDomainNetRemove from static to global (rhbz#691539)
- qemu: Use virDomainNetRemove instead of inline code (rhbz#691539)
- qemu: Support type=hostdev network device live hotplug attach/detach (rhbz#691539)
- util: Two new pci util functions (rhbz#691539)
- util: Support functions for mac/portprofile associations on hostdev (rhbz#691539)
- util: Changes to support portprofiles for hostdevs (rhbz#691539)
- qemu: Install port profile and mac address on netdev hostdevs (rhbz#691539)
- Fix build after commit e3ba4025 (rhbz#693842)

* Tue Feb 28 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-3.el6
- storage: Allow runtime detection of scrub missing build dep (rhbz#725013)
- daemon: Plug memory leak (rhbz#795978)
- daemon: Fix logic bug with virAsprintf (rhbz#795978)
- util: Fix virFileAccessibleAs return path from parent (rhbz#795093)
- Add support for unsafe migration (rhbz#751631)
- virsh: Add --unsafe option to migrate command (rhbz#751631)
- Introduce virStorageFileIsClusterFS (rhbz#751631)
- qemu: Forbid migration with cache != none (rhbz#751631)
- qemu: Nicer error message on failed graceful destroy (rhbz#795656)
- Error out when using SPICE TLS with spice_tls=0 (rhbz#790436)
- Revert "spec: Mark directories in /var/run as ghosts" (rhbz#788985)
- Fixed URI parsing (rhbz#785164)
- virsh: Fix informational message in iface-bridge command (rhbz#797066)

* Tue Feb 21 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-2.el6
- qemu: Set capabilities based on supported monitor commands (rhbz#766958)
- qemu: Implement DomainPMSuspendForDuration (rhbz#766958)
- snapshot: Fix snapshot deletion use-after-free (rhbz#790744)
- storage: Allow runtime detection of scrub (rhbz#725013)
- qemu: Unlock monitor when connecting to dest qemu fails (rhbz#783968)
- qemu: Prevent crash of libvirtd without guest agent (rhbz#790745)
- python: Expose virDomain{G,S}etInterfaceParameters APIs in python binding (rhbz#770971)

* Tue Feb 14 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-1.el6
- Rebase to upstream 0.9.10 (rhbz#752433)
- Add support for sVirt in the LXC driver
- block rebase: add new API virDomainBlockRebase
- API: Add api to set and get domain metadata
- virDomainGetDiskErrors public API
- conf: add rawio attribute to disk element of domain XML
- Add new public API virDomainGetCPUStats()
- Introduce virDomainPMSuspendForDuration API
- resize: add virStorageVolResize() API
- Add a virt-host-validate command to sanity check HV config
- Add new virDomainShutdownFlags API
- QEMU guest agent support
- many improvements and bug fixes

* Wed Feb  8 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-0rc2.el6
- Rebase to upstream 0.9.10 release candidate 2 (rhbz#752433)

* Mon Feb  6 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.10-0rc1.el6
- Rebase to upstream 0.9.10 release candidate 1 (rhbz#752433)

* Tue Jan 17 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.9-2.el6
- Remove dependancy to dmidecode for non PC arches (rhbz#782444)

* Mon Jan  9 2012 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.9-1.el6
- Rebase to upstream 0.9.9 (rhbz#752433)

* Fri Dec 30 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.9-0rc1.el6
- Rebase to upstream 0.9.9 release candidate 1 (rhbz#752433)

* Mon Dec  8 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.8-1.el6
- Rebase to upstream 0.9.8 (rhbz#752433)
- some cleanups on the few remaining RHEL-only patches

* Mon Dec  5 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.8-0rc2.el6
- Rebase to upstream 0.9.8 release candidate 2 (rhbz#752433)

* Wed Nov  9 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-23.el6
- Revert "Set qemu migration speed unlimited when migrating to file" (rhbz#751900)

* Mon Nov  7 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-22.el6
- conf: Don't free uninitialized pointer (rhbz#751287)

* Wed Nov  2 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-21.el6
- docs: Document managed=yes of hostdev passthrough (rhbz#740686)
- ServerClient: Flush cached data (rhbz#748025)

* Wed Oct 26 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-20.el6
- qemu: Avoid leaking uninit data from hotplug to dumpxml (rhbz#747516)
- storage: Plug iscsi memory leak (rhbz#747516)

* Wed Oct 19 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-19.el6
- snapshot: Detect when qemu lacks disk-snapshot support (rhbz#747115)

* Mon Oct 17 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-18.el6
- virDomainCoreDump: Introduce VIR_DUMP_RESET flag (rhbz#632498)
- qemu: Implement VIR_DUMP_RESET (rhbz#632498)
- qemu: Check for domain being active on successful job acquire (rhbz#745734)
- Set to NULL members that have been freed to prevent crashes (rhbz#746075)
- virFDStream: Close also given errfd (fd leak) (rhbz#746075)
- qemu: Silence Coverity false positive (rhbz#739704)
- command: Avoid fd leak on failure (rhbz#739704)
- build: Add compiler attributes to virUUIDParse (rhbz#739704)
- qemu: Check for json allocation failure (rhbz#739704)
- qemu: Fix text block info parsing (rhbz#739704)
- storage: Plug memory leak on error (rhbz#739704)
- conf: Plug memory leak on error (rhbz#739704)
- qemu: Plug memory leak on migration (rhbz#739704)
- macvtap: Plug memory leak for 802.1Qbh (rhbz#739704)
- macvtap: Avoid invalid free (rhbz#739704)
- Update to require sanlock 1.8 for license compliance (rhbz#739518)
- events: Propose a separate lock for event queue (rhbz#743817)
- util: Make getaddrinfo failure nonfatal in virGetHostname (rhbz#738915)
- qemu: Make sure BeginJob is always followed by EndJob (rhbz#746268)
- pci: Fix pciDeviceListSteal on multiple devices (rhbz#733587)
- qemu: Do not reattach PCI device used by other domain when shutdown (rhbz#733587)
- qemu: Honor the orginal PCI dev properties when reattaching (rhbz#736214)
- daemon: Always advertise libvirtd service (rhbz#726616)

* Wed Oct 12 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-17.el6
- Fix deadlock when the RPC program is unknown (rhbz#743843)
- qemuDomainAttach: Initialize pidfile variable (rhbz#744548)
- storage: Do not use comma as seperator for lvs output (rhbz#727474)
- snapshot: Avoid accidental renames with snapshot-edit (rhbz#744724)

* Fri Oct  7 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-16.el6
- qemu: Enable multifunction for older qemu (rhbz#738388)
- qemu: Don't fail virDomainGetInfo if we can't update balloon info (rhbz#741217)
- qemu: Leave rerror policy at default when enospace is requested (rhbz#730909)
- snapshot: Fix virsh error message typo (rhbz#735457)
- snapshot: Let virsh edit disk snapshots (rhbz#744071)
- snapshot: Simplify redefinition of disk snapshot (rhbz#744071)

* Fri Oct  7 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-15.el6
- Add virFileLock and virFileUnlock APIs (rhbz#728153)
- Move pidfile functions into util/virpidfile.{c, h} (rhbz#728153)
- Introduce functions for checking whether a pidfile is valid (rhbz#728153)
- Add some APIs which use locking for crashsafe pidfile handling (rhbz#728153)
- Convert libvirtd to use crash-safe pidfile APIs (rhbz#728153)
- build: Fix recent build failures (rhbz#728153)
- daemon: Don't remove pidfiles in init scripts (rhbz#728153)
- daemon: Modify init script to detect upstart managed libvirtd (rhbz#728153)
- qemu: Check for outstanding async job too (rhbz#742277)
- qemu: Make PCI multifunction support more manual (rhbz#727530)
- network: Fill in bandwidth from portgroup for all forward modes (rhbz#743176)
- snapshot: Refactor virsh snapshot parent computation (rhbz#742410)
- snapshot: Better virsh handling of missing current, parent (rhbz#742410)
- qemu: Fix migration with dname (rhbz#740533)
- qemu: Correct misspelled 'enospc' option, and only use for werror (rhbz#730909)
- snapshot: Add REVERT_FORCE to API (rhbz#742615)
- snapshot: Use qemu-img on disks in use at time of snapshot (rhbz#742615)
- snapshot: Enforce REVERT_FORCE on qemu (rhbz#742615)
- init: Raise default system aio limits (rhbz#740899)

* Thu Sep 29 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-14.el6
- Fix synchronous reading of stream data (rhbz#741337)
- qemu: Add ability to set PCI device "rombar" on or off (rhbz#738095)
- virsh: Better document --copy-storage migrate options (rhbz#677220)
- virsh: Enhance documentation of commands starting jobs (rhbz#705237)
- qemu: Always remove domain object if MigratePrepare fails (rhbz#741251)
- security: Properly chown/label bidirectional and unidirectional fifos (rhbz#740478)
- qemu: Check domain status details when reconnecting monitor (rhbz#617890)
- qemu: Finish domain shutdown on reconnect (rhbz#617890)
- qemu: Avoid loop of fake reboots (rhbz#617890)
- qemu: Preserve fakeReboot flag in domain status (rhbz#617890)
- snapshot: Fix man page typos (rhbz#740686)
- docs: Document virsh nodedev-* commands (rhbz#740686)
- docs: Document node device XML (rhbz#740686)
- qemu: Add return value check (rhbz#739704)
- qemu: Check for ejected media during startup and migration (rhbz#725673)
- virsh: Update man page for cpu_shares parameter (rhbz#639591)
- virsh: Describe attach-interface parameter target (rhbz#698899)

* Mon Sep 26 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-13.el6
- Fix crash on events due to allocation errors (rhbz#737881)
- remote: Fix crash on OOM (rhbz#737881)
- Fix persistent migration config save (rhbz#738148)
- qemu: Transfer inactive XML among cookie (rhbz#738148)
- storage: Ensure the device path exists before refreshing disk pool (rhbz#611442)
- Store max migration bandwidth in qemuDomainObjPrivate struct (rhbz#740099)
- Save migration speed in qemuDomainMigrateSetMaxSpeed (rhbz#740099)
- Set qemu migration speed unlimited when migrating to file (rhbz#740099)
- Use max bandwidth from qemuDomainObjPrivate struct when migrating (rhbz#740099)
- build: Silence warning on 32-bit build (rhbz#740099)
- conf: Assign newDef of active domain as persistent conf if it is NULL (rhbz#728428)
- qemu: Avoid dereferencing a NULL pointer (rhbz#739704)
- sanlock: Fix memory leak (rhbz#739704)
- virsh: Fix regression in argv parsing (rhbz#740168)
- snapshot: Fix logic bug in qemu undefine (rhbz#735457)
- snapshot: Prepare to remove transient snapshot metadata (rhbz#735457)
- snapshot: Remove snapshot metadata on transient exit (rhbz#735457)
- snapshot: Also delete empty directory (rhbz#735457)
- virsh: Do not ignore the specified flags for cmdSaveImageDefine (rhbz#740508)
- selinux: Correctly report warning if virt_use_nfs not set (rhbz#589922)
- qemu: Properly hot-unplug drives (rhbz#696596)

* Tue Sep 20 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-12.el6
- selinux: Detect virt_use_nfs boolean set (rhbz#589922)
- virnetsocket: Pass KRB5CCNAME env variable (rhbz#737176)
- snapshot: Fix double free of qemuImgBinary (rhbz#737010)
- qemu_api: Modify apibuild.py to generate docs for QEMU APIs (rhbz#736040)
- qemu_api: Update Makefile for subdir docs (rhbz#736040)
- qemu_api: Add comments for API virDomainQemuMonitorCommand (rhbz#736040)
- qemu_api: Add override XML and C files for QEMU APIs (rhbz#736040)
- qemu_api: Update Py binding generator to generate files for QEMU APIs (rhbz#736040)
- qemu_api: Update Makefile to generate libvirtmod_qemu lib (rhbz#736040)
- qemu_api: Update libvirt spec file (rhbz#736040)
- Remove two references to files not generated (rhbz#736040)
- qemu_api: Doc improvements (rhbz#736040)
- python: Fix libvirt.py generation to include virterror info (rhbz#736040)
- snapshot: New APIs for inspecting snapshot object (rhbz#735457)
- snapshot: Use new API for less work (rhbz#735457)
- snapshot: ABI stability must include memory sizing (rhbz#735553)
- spec: Require augeas for sanlock (rhbz#738314)
- sanlock: Add missing test command in virt-sanlock-cleanup.in (rhbz#738534)
- snapshot: Tweak snapshot-create-as diskspec docs (rhbz#738411)
- qemu: Hold conn open for all threads started by qemuProcessReconnectAll (rhbz#738778)
- rpc: Convert unknown procedures to VIR_ERR_NO_SUPPORT (rhbz#738439)
- Prevent crash from dlclose() of libvirt.so (rhbz#739167)
- doc: Add statment about permissions needed to do a core dump (rhbz#738146)
- snapshot: Affect persistent xml after disk snapshot (rhbz#738676)
- snapshot: Allow disk snapshots of qcow2 disks (rhbz#738676)
- qemu: Prevent disk corruption on domain shutdown (rhbz#734773)
- qemu: Introduce shutdown reason for paused state (rhbz#734773)
- qemu: Fix shutoff reason when domain crashes (rhbz#739641)
- qemu: Properly detect crash of a rebooted domain (rhbz#739641)
- qemu: Avoid memory leak (rhbz#739704)
- remote: Avoid memory leak (rhbz#739704)
- util: Avoid memory leak (rhbz#739704)
- Fix memory leak parsing 'relabel' attribute in domain security XML (rhbz#739704)
- Don't leak memory if a cgroup is mounted multiple times (rhbz#739704)
- network: Eliminate potential memory leak on parse failure (rhbz#739704)
- virsh: doc: Fix supported driver types for attach-disk command (rhbz#738970)
- Do not log invalid operations in libvirtd logs (rhbz#590807)

* Thu Sep  8 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-11.el6
- blockinfo: Fix qemu regression in handling disk name (rhbz#736603)
- doc: Fix incorrect option in send-key (rhbz#736297)
- virsh: Fix typo in opts_send_key (rhbz#736297)
- rpc: Avoid memory leak on virNetTLSContextValidCertificate (rhbz#735650)
- tests: Avoid memory leak on testTLSSessionInit (rhbz#735650)
- qemu: Fix seamless SPICE migration with older qemu (rhbz#730753)
- snapshot: Fix regression with system checkpoints (rhbz#736682)

* Wed Sep  7 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-10.el6
- virterror: Fix error message for VIR_ERR_INVALID_ARG (rhbz#689388)
- remote: Refuse connecting to remote socket (rhbz#689388)
- Threadpool: Initialize new dynamic workers (rhbz#692663)

* Tue Sep  6 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-9.el6
- adds a missing patch in previous build (rhbz#735498)

* Tue Sep  6 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-8.el6
- qemu: Fix a regression of domain save (rhbz#735011)
- virsh: Improve send-key documentation (rhbz#699847)
- start: Allow discarding managed save (rhbz#730750)
- virsh: Support 'virsh start --force-boot' on older servers (rhbz#730750)
- maint: Fix comment typos (rhbz#730750)
- qemu: Refactor file opening (rhbz#730750)
- qemu: Detect incomplete save files (rhbz#730750)
- virsh: Avoid memory leak on cmdVolCreateAs (rhbz#735008)
- snapshot: Fix corner case on OOM during creation (rhbz#674537)
- Ensure stream is aborted when exiting console (rhbz#731673)
- following for (rhbz#731583, rhbz#731579, rhbz#731584, rhbz#731673):
- Ensure client streams are closed when marking a client for close
- Fix race condition in abort of stream
- Tweak debugging message in RPC client code
- Don't attempt to read from a stream if it is closed
- Ensure async packets never get marked for sync replies
- Ignore unused streams in virStreamAbort
- rpc: Don't close connection if program is unknown
- rpc: Fix a typo in debugging log in virNetServerProgramSendStreamData
- stream: Remove redundant reference to client while sending stream data
- Fix memory leak dispatching domain events
- Avoid use-after-free on streams, due to message callbacks
- Fix tracking of RPC messages wrt streams
- Fix parted sector size assumption (rhbz#735441)
- Fix incorrect path length check in sanlock lockspace setup (rhbz#735443)
- Fix sanlock socket security labelling (rhbz#735442)
- Remove bogus virSecurityManagerSetProcessFDLabel method (rhbz#735442)
- security: Fix build (rhbz#735442)
- Fix keymap used to talk with QEMU (rhbz#632499)
- virsh: Fix snapshot-create-as to handle arbitrary names (rhbz#735495)
- virsh: Add virsh snapshot-current --name (rhbz#735495)
- virsh: Add snapshot-parent (rhbz#735495)
- virsh: Don't reject undefine on active domain (rhbz#735495)
- virsh: Fix logic bug (rhbz#735495)
- virsh: Fix dead store (rhbz#735495)
- virsh: Tweak misleading wording (rhbz#735495)
- virsh: Concatenate qemu-monitor-command arguments (rhbz#735495)
- maint: Treat more libxml2 functions as free-like (rhbz#735495)
- xml: Add another convenience function (rhbz#735495)
- maint: Simplify lots of libxml2 clients (rhbz#735495)
- virsh: Add list --managed-save (rhbz#735495)
- virsh: Prefer unsigned flags (rhbz#735495)
- snapshot: Add snapshot-list --parent to virsh (rhbz#735495)
- qemu: Allow to undefine a running domain (rhbz#735498)
- test: Allow to undefine a running domain (rhbz#735498)
- build: Fix typo in recent test patch (rhbz#735498)
- test: Rewrite test to match change in behavior (rhbz#735498)
- virsh: Properly interleave shared stdout and stderr (rhbz#735498)
- snapshot: Better events when starting paused (rhbz#733762)
- snapshot: Fine-tune ability to start paused (rhbz#733762)
- snapshot: Expose --running and --paused in virsh (rhbz#733762)
- snapshot: Fine-tune qemu saved images starting paused (rhbz#733762)
- snapshot: Improve reverting to qemu paused snapshots (rhbz#733762)
- snapshot: Properly revert qemu to offline snapshots (rhbz#733762)
- snapshot: Fine-tune qemu snapshot revert states (rhbz#733762)
- snapshot: Properly revert qemu to offline snapshots (rhbz#733762)
- snapshot: Fine-tune qemu snapshot revert states (rhbz#733762)
- snapshot: Speed up snapshot location (rhbz#733529)
- snapshot: Avoid crash when deleting qemu snapshots (rhbz#733529)
- snapshot: Track current domain across deletion of children (rhbz#733529)
- snapshot: Simplify acting on just children (rhbz#733529)
- snapshot: Allow deletion of just snapshot metadata (rhbz#735457)
- snapshot: Let qemu discard only snapshot metadata (rhbz#735457)
- snapshot: Identify which snapshots have metadata (rhbz#735457)
- snapshot: Reflect new dumpxml and list options in virsh (rhbz#735457)
- snapshot: Identify qemu snapshot roots (rhbz#735457)
- snapshot: Allow recreation of metadata (rhbz#735457)
- snapshot: Refactor virsh snapshot creation (rhbz#735457)
- snapshot: Improve virsh snapshot-create, add snapshot-edit (rhbz#735457)
- snapshot: Add qemu snapshot creation without metadata (rhbz#735457)
- snapshot: Add qemu snapshot redefine support (rhbz#735457)
- vbox, xenapi: Add virDomainUndefineFlags (rhbz#735457)
- snapshot: Prevent stranding snapshot data on domain destruction (rhbz#735457)
- snapshot: Teach virsh about new undefine flags (rhbz#735457)
- snapshot: Refactor some qemu code (rhbz#735457)
- snapshot: Cache qemu-img location (rhbz#735457)
- snapshot: Support new undefine flags in qemu (rhbz#735457)
- snapshot: Prevent migration from stranding snapshot data (rhbz#735457)
- snapshot: Refactor domain xml output (rhbz#735553)
- snapshot: Allow full domain xml in snapshot (rhbz#735553)
- snapshot: Correctly escape generated xml (rhbz#735553)
- snapshot: Update rng to support full domain in xml (rhbz#735553)
- snapshot: Store qemu domain details in xml (rhbz#735553)
- schedinfo: Update man page about virsh schedinfo command (unknown)
- snapshot: Additions to domain xml for disks (rhbz#638510)
- snapshot: Reject transient disks where code is not ready (rhbz#638510)
- snapshot: Introduce new deletion flag (rhbz#638510)
- snapshot: Expose new delete flag in virsh (rhbz#638510)
- snapshot: Allow halting after snapshot (rhbz#638510)
- snapshot: Expose halt-after-creation in virsh (rhbz#638510)
- snapshot: Support extra state in snapshots (unknown)
- snapshot: Add <disks> to snapshot xml (rhbz#638510)
- snapshot: Also support disks by path (rhbz#638510)
- snapshot: Add virsh domblklist command (rhbz#638510)
- snapshot: Add flag for requesting disk snapshot (rhbz#638510)
- snapshot: Wire up disk-only flag to snapshot-create (rhbz#638510)
- snapshot: Reject unimplemented disk snapshot features (rhbz#638510)
- snapshot: Make it possible to audit external snapshot (rhbz#638510)
- snapshot: Wire up new qemu monitor command (rhbz#638510)
- snapshot: Wire up live qemu disk snapshots (rhbz#638510)
- snapshot: Use SELinux and lock manager with external snapshots (rhbz#638510)
- daemon: Create priority workers pool (rhbz#692663)
- qemu: Introduce job queue size limit (rhbz#692663)
- qemu: Deal with stucked qemu on daemon startup (rhbz#692663)

* Wed Aug 31 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-7.el6
- qemu: Properly label outgoing pipe for tunneled migration (rhbz#733998)
- snapshot: Forbid snapshot on autodestroy domain (rhbz#733806)

* Fri Aug 26 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-6.el6
- daemon: Move TLS initialization to virInitialize (rhbz#732893)
- Fix command test wrt gnutls initialize & fix debugging (rhbz#732893)
- qemu: Init reattaching related members pciDevice before reattach (rhbz#728203)
- qemu: error if qemu monitor command not found for BlockJob (rhbz#727502)
- virsh: error if specified bandwidth is invalid for blockjob (rhbz#727502)
- util: Only fchown newly created files in virFileOpenAs (rhbz#534010)
- screenshot: Implement multiple screen support (rhbz#710489)
- security: Rename SetSocketLabel APIs to SetDaemonSocketLabel (rhbz#731243)
- security: Introduce SetSocketLabel (rhbz#731243)
- qemu: Correctly label migration TCP socket (rhbz#731243)
- snapshot: Don't leak resources on qemu snapshot failure (rhbz#733499)
- Fix memory leak while scanning snapshots (rhbz#674537)
- qemu: Minor formatting cleanup (rhbz#674537)
- Swap virDomain and virDomainSnapshot declaration (rhbz#674537)
- snapshot: Only pass snapshot to qemu command line when reverting (rhbz#674537)
- snapshot: Track current snapshot across restarts (rhbz#674537)
- send-key: Fix scan keycode map (rhbz#733597)

* Mon Aug 22 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-5.el6
- patch problem for seamless SPICE migration (rhbz#730753)
- macvtap: Fix getPhysfn to get the PF of a direct attach network interface (rhbz#732082)
- SSL spice session can't be kept during migration (rhbz#729874)
- Storage driver should flush host cache after cloning volumes (rhbz#689416)
- Documentation for CFS bandwidth limiting cgroup (rhbz#692769)
- libvirt error message should show the uri content but not (null) (rhbz#730244)
- libvirtd.conf error causes libvirtd to exit silently (rhbz#728654)

* Mon Aug 15 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-4.el6
- Bugfix: Check stdoutWatch before removing the handler. (rhbz#730600)
- daemon: Fix regression of libvirtd reloading support (rhbz#730428)
- libvirtd.init.in: Stop/restart() - wrong return value in case of failure (rhbz#730510)
- Add API for duplicating a socket/client file descriptor (rhbz#720269)
- Add backlog parameter to virNetSocketListen (rhbz#720269)
- Support changing UNIX socket owner in virNetSocketNewListenUNIX (rhbz#720269)
- qemu: Refactor do{Tunnel, Native}Migrate functions (rhbz#720269)
- qemu: Use virNetSocket for tunneled migration (rhbz#720269)
- qemu: Use fd: protocol for migration (rhbz#720269)
- qemu: Support event_idx parameter for virtio disk and net devices (rhbz#725448)
* Mon Aug 15 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-3.el6
- Fix large files support (rhbz#728992)
- qemu: Avoid overwriting errors from virGetHostname (rhbz#729567)
- qemu: Fix -chardev udp if parameters are omitted (rhbz#689761)
- managedsave: Prohibit use on transient domains (rhbz#729714)
- nwfilter: Tolerate disappearing interfaces while instantiating filter (rhbz#729945)
- docs: Describe new virtual switch configuration in network XML docs (rhbz#643947)
- storage: Directory shouldn't be listed as type 'file' (rhbz#727088)
- virsh: Add dir type for listing volumes with vol-list (rhbz#727088)
- qemu: Avoid crash on process attach (rhbz#730615)

* Tue Aug  9 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-2.el6
- daemon: Unlink unix socket paths on shutdown (rhbz#725702)
- rpc:Fix sasl session relocking intead of unlocking it (rhbz#729198)
- network: Eliminate lag in updating dnsmasq hosts files (rhbz#727982)
- Don't mount /dev for application containers (rhbz#728835)
- support connected parameter in set_password (rhbz#707212)

* Wed Aug  3 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-1.el6
- Rebased to upstream 0.9.4 (rhbz#705814)
- The rebase also fixes the following bugs:
    rhbz#634653, rhbz#707212, rhbz#722806, rhbz#723862, rhbz#726304,
    rhbz#726398, rhbz#727047, rhbz#727094

* Fri Jul 29 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-0rc2.el6
- rebased to upstream 0.9.4 release candidate 2 (rhbz#705814)
- the rebase also fixes the following bugs:
    rhbz#667624, rhbz#669586, rhbz#682084, rhbz#707155, rhbz#707212,
    rhbz#725322, rhbz#725935, rhbz#725950

* Fri Jul 29 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-0rc1.1.el6
- add a fix for a refcounting bug leading to a crash (rhbz#723811)

* Tue Jul 26 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.4-0rc1.el6
- rebased to upstream 0.9.4 release candidate 1 (rhbz#705814)
- the rebase also fixes the following bugs:
    rhbz#603039, rhbz#632499, rhbz#632760, rhbz#643947, rhbz#678027,
    rhbz#697742, rhbz#697841, rhbz#704836, rhbz#707530, rhbz#720350,
    rhbz#720889, rhbz#721335, rhbz#722862

* Tue Jul 26 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-8.el6
- libvirt crash when running domains and vdsm is restarted (rhbz#723811)
- connect to hypervisor with unconfigured tls/tcp connection pbm (rhbz#723442)
- virsh list produced segmentation fault when libvirtd is not up (rhbz#723843)
- clientcert.pem validation failure cause libvirtd crash (rhbz#723881)

* Wed Jul 20 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-7.el6
- Fix TLS certificate checking problems (rhbz#723447)

* Wed Jul 20 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-6.el6
- Fix migration with TLS bugs (rhbz#722738 and rhbz#722748)
- assorted small fixes from upstream

* Fri Jul 15 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-5.el6
- Fix migrating domain error (rhbz#721411)

* Fri Jul 15 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-4.el6
- storage: Avoid memory leak on metadata fetching (rhbz#707155)
- graphics: Add support for action_if_connected in qemu (rhbz#707212)
- qemu: Save domain status ASAP after creating qemu process (rhbz#707894)
- bios: Add support for SGA (rhbz#711598)
- pci: Initialize state values on reattach (rhbz#713697)
- Keep consistence between code and doc on log level and usage (rhbz#716888)

* Thu Jul 14 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-3.el6
- util: Avoid duplicating virFileOpenAsNoFork in virFileOpenAs (rhbz#707257)

* Mon Jul 11 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-2.el6
- Fix mistaken order of server cert/key parameters in constructor (rhbz#719838)
- qemu: Don't chown files on NFS share if dynamic_ownership is off (rhbz#716478)
- util: Don't try to fchown files opened as non-root (rhbz#707257)

* Mon Jul  4 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-1.el6
- Rebased to upstream 0.9.3 (rhbz#705814)
- The rebase also fixes the following bugs:
    rhbz#591974, rhbz#632499, rhbz#641087, rhbz#664629, rhbz#679668,
    rhbz#682121, rhbz#693648, rhbz#693650, rhbz#693661, rhbz#698340,
    rhbz#698825, rhbz#698861, rhbz#701394, rhbz#707439, rhbz#707530,
    rhbz#715355, rhbz#716826, rhbz#717203, rhbz#718143, rhbz#712050,
    rhbz#715184

* Thu Jun 30 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.3-0rc2.el6
- Rebased to upstream 0.9.3 prerelease 2 (rhbz#705814)

* Mon Jun 20 2011 Daniel Veillard <veillard@redhat.com> - libvirt-0.9.2-1.el6
- Rebased to upstream 0.9.2 (rhbz#705814)
- The rebase also fixes the following bugs:
    rhbz#569567, rhbz#691830, rhbz#607526, rhbz#609650, rhbz#632495,
    rhbz#640603, rhbz#658713, rhbz#669549, rhbz#677229, rhbz#678548,
    rhbz#640603, rhbz#682237, rhbz#683005, rhbz#684848, rhbz#688859,
    rhbz#690695, rhbz#692355, rhbz#693203, rhbz#694516, rhbz#697650,
    rhbz#698133, rhbz#702044, rhbz#704124, rhbz#704144, rhbz#705405,
    rhbz#706869, rhbz#706883, rhbz#706966, rhbz#707173, rhbz#707257,
    rhbz#707298, rhbz#709576, rhbz#709776, rhbz#710150, rhbz#711151

* Thu May 19 2011 Jiri Denemark <jdenemar@redhat.com> - libvirt-0.9.1-1.el6
- Rebased to upstream 0.9.1 (rhbz#705814)
- The rebase also fixes the following bugs:
    rhbz#587276, rhbz#591058, rhbz#592170, rhbz#598792, rhbz#673814,
    rhbz#677228, rhbz#681458, rhbz#682237, rhbz#692745, rhbz#693932,
    rhbz#694382, rhbz#695653, rhbz#698071, rhbz#698197, rhbz#698208,
    rhbz#698490, rhbz#701305

* Mon Apr 18 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-18.el6
- network: Fix NULL dereference during error recovery (rhbz#696660)
- virsh: Fix regression in parsing optional integer (rhbz#693963)
- util: Fix crash when removing entries during hash iteration (rhbz#693385)
- Experimental libvirtd upstart job (rhbz#678084)

* Wed Apr 13 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-17.el6
- Don't return an error on failure to create blkio controller (rhbz#689030)
- Fix possible infinite loop in remote driver (rhbz#691514)
- qemu: Remove the managed state file only if restoring succeeded (rhbz#692998)
- docs: Tweak virsh restore warning (rhbz#692998)

* Wed Apr  6 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-16.el6
- nwfilter: Enable rejection of packets (rhbz#681948)
- Revert all previous error log priority hacks (rhbz#587603)
- Filter out certain expected error messages from libvirtd (rhbz#587603)
- qemu: Unlock qemu driver before return from domain save (rhbz#688774)
- Do not send monitor command after monitor meet error (rhbz#688774)
- qemu: Ignore libvirt debug messages in qemu log (rhbz#681492)
- virsh: Fix memtune's help message for swap_hard_limit (rhbz#680190)
- virsh: Fix documentation for memtune command (rhbz#680190)
- docs: Fix typo (rhbz#680190)
- Fix typo in systemtap tapset directory name (rhbz#693701)
- qemu: Ignore unusable binaries (rhbz#676563)
- qemu: Support for overriding NPROC limit (rhbz#674602)

* Tue Mar 29 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-15.el6
- Fix return value for virJSONValueFromString if it fails (rhbz#688723)
- Fix positioning to end of qemu log file (rhbz#689986)
- Initialization error of qemuCgroupData in Qemu host usb hotplug (rhbz#690183)
- 8021Qbh: Use preassociate-rr during the migration prepare stage (rhbz#684870)
- Make error reporting in libvirtd thread safe (rhbz#689374)
- Add missing dependencies (rhbz#690022)
- Fix restoring a compressed save image (rhbz#691034)
- Fix label restore bugs in qemu driver (rhbz#690737)

* Tue Mar 22 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-14.el6
- Fix delayed events when SASL is active (rhbz#624252)
- Fix ref-counting bugs (rhbz#688774)
- Log an error if on failure to connect to netlink socket (rhbz#689001)
- Log error and abort network startup when radvd isn't found (rhbz#688957)
- Add PCI sysfs reset access rights to qemu (rhbz#689002)
- Fix regression with qemu:///session URI (rhbz#684655)
- Avoid leaking PCI config fd into qemu (rhbz#687993)

* Wed Mar 16 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-13.el6
- Properly report error in virConnectDomainXMLToNative (CVE-2011-1146)
- Handle DNS over IPv6 (rhbz#687896)
- Start dnsmasq even if no dhcp ranges/hosts are specified (rhbz#687291)
- Use a separate dhcp leases file for each network (rhbz#687551)
- Fix a possible crash in storage driver (rhbz#684712)

* Tue Mar 15 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-12.el6
- Fix vram settings for qxl graphics (rhbz#673578)
- Free stream when domain shuts down while its console is open (rhbz#682741)
- Use hardcoded python path in libvirt.py (rhbz#684204)
- Add missing checks for read only connections (CVE-2011-1146)
- Eliminate potential null pointer deref when auditing macvtap devices (rhbz#642785)
- Insert error messages to avoid a quiet abortion of commands (rhbz#605660)

* Thu Mar 10 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-11.el6
- Support vram specification for qxl graphics (rhbz#673578)
- Fix parsing int options in virsh (rhbz#639587)
- Use -o encryption=on instead of -e for qemu-img (rhbz#676984)
- Support domain snapshots with current QMP (rhbz#589076)
- Update auditing support (rhbz#642785)
- Only request sound cgroup ACL when required (rhbz#680398)
- Allow fine-tuning of device ACL permissions (rhbz#683163)
- Support vhost in attach-interface (rhbz#683276)
- Don't request cgroup ACL access for /dev/net/tun (rhbz#683305)

* Mon Mar 07 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-10.el6
- Fix deadlock caused by a fix for rhbz#670848

* Fri Mar 04 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-9.el6
- Reorder nwfilter match extensions relative to state match (rhbz#678139)
- Avoid overwriting error message in qemu driver (rhbz#678870)
- Allow removing hash entries in virHashForEach (rhbz#681459)
- Avoid double close on qemu domain restore (rhbz#672725)
- Fix DomainObj refcounting/hashtable races in qemu driver (rhbz#670848)
- Fix several memory leaks (rhbz#682249)

* Thu Feb 24 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-8.el6
- Fix --all flag of virsh freecell to really show all cells (rhbz#653530)
- Add txmode attribute to interface XML for virtio backend (rhbz#629662)
- Give each virtual network bridge its own fixed MAC address (rhbz#609463)
- Fix virsh snapshot-list with --quiet option (rhbz#678833)
- Delay IFF_UP'ing 802.1Qbh interface until migration final stage (rhbz#678826)
- Fix several memory bugs (rhbz#679164)
- Fix virt-pki-validate when CERTTOOL is missing (rhbz#679153)
- Fix memory corruption in virFileAbsPath (rhbz#680281)

* Thu Feb 17 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-7.el6
- Properly escape special characters in domain names (rhbz#676908)
- Fix enum type declaration (rhbz#628940)
- Fix cleanup on VM state after failed QEMU startup (rhbz#673588)
- Fix XML generation for smartcards (rhbz#677308)
- Ignore failure of "qemu -M ?" on older qemu (rhbz#676563)
- Fix typo in setting up SPICE passwords (rhbz#677709)
- Avoid NULL dereference in virDomainMemoryStats (rhbz#677484)
- Avoid NULL dereference on error in qemu driver (rhbz#677493)
- Fix error message when saving a shutoff domain (rhbz#677547)
- Create enough volumes for mpath pool (rhbz#677231)
- Allow to delete device mapper disk partition (rhbz#611443)

* Fri Feb 11 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-6.el6
- Fix typo in parsing of spice 'auth' data (rhbz#676374)
- Fix attach-interface regression (rhbz#676686)
- Block I/O tunables via blkio cgroups controller (rhbz#632492)
- Support SCSI RAID type & lower log level for unknown types (rhbz#675771)
- Only initialize/cleanup libpciaccess once (rhbz#675698)
- Imprint all logs with version + package build information (rhbz#673226)

* Thu Feb 04 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-5.el6
- Docs for customizable x509 certificate paths for client (rhbz#629510)
- Fix tests for VNC over a unix domain socket (rhbz#651415)
- Fix problems with peer-to-peer migration (rhbz#673434)
- Fix tunneled migration broken since 0.8.7-2 (rhbz#672199)
- Update docs for cpu_shares setting (rhbz#641187)
- Fix possible hang if SASL is used (rhbz#672226)
- Cancel migration in progress when virsh gets Ctrl-C (rhbz#635353)
- Enhance virsh migrate command (rhbz#619039)
- Support for specifying AIO mode for qemu disks (rhbz#591703)
- Don't leave domain paused after restore (rhbz#670278)
- Fix possible deadlock/crash in qemu driver (rhbz#673588)
- Add shortcut for qemu HMP pass through (rhbz#628940)
- Fix error message when attach device fails (rhbz#675030)
- Support for booting from assigned PCI devices (rhbz#646895)
- Improve handling of unlimited value for memory tunables (rhbz#669069)
- Add smartcard support (rhbz#641834)
- Remove some RHEL-specific patches which are no longer required (rhbz#653985)
- Support for disabling/enabling KSM per domain (rhbz#635419)
- Add --all flag to virsh freecell command (rhbz#653530)

* Thu Jan 27 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-4.el6
- Fix event-handling data race (rhbz#671567)
- Add support for VNC over a unix domain socket (rhbz#651415)
- Support intel 'ich6' model (rhbz#648486)
- Do not use virtio-serial port 0 for generic ports (rhbz#670394)
- Set SELinux context label of pipes used for qemu migration (rhbz#667756)
- Support customizable x509 certificate paths for client (rhbz#629510)
- Round up capacity for LVM volume creation (rhbz#670529)
- Show error prompt when trying to managed save a shutoff domain (rhbz#672449)
- Report more proper error for unsupported graphics (rhbz#671319)
- Expand the man page text for virsh setmaxmem (rhbz#622534)
- Fix event-handling allocation crash (rhbz#671564)
- Require --mac to avoid detach-interface ambiguity (rhbz#671050)

* Thu Jan 20 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-3.el6
- Report error if invalid type specified for character device (rhbz#638968)
- Improve log for domain related APIs (rhbz#640202)
- Reject SDL graphic if it's not supported by qemu (rhbz#633326)
- Don't lose track of events when callbacks are slow (rhbz#624252)
- Fail if per-device boot is used but deviceboot is not supported (rhbz#670399)
- Avoid sending STOPPED event twice (rhbz#666158)
- Fix issues introduced by dependency patches for rhbz#646895

* Mon Jan 17 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-2.el6
- Fix spec file which was not fully rebased to 0.8.7 (rhbz#653985, rhbz#660706)
- Skip IB700 watchdog device when assigning PCI slots (rhbz#667091)
- Improve error reporting when parsing dhcp info (rhbz#653300)
- Don't chown saved image back to root if dynamic_ownership=0 (rhbz#661720)
- Fix core dumps if unix_sock_group is set (rhbz#623166)
- Add support for Westmere CPU model (rhbz#656248)
- Add XML config switch to enable/disable vhost-net support (rhbz#643050)
- Enable tuning of qemu network tap device "sndbuf" size (rhbz#665293)
- Support for explicit boot device ordering (rhbz#646895)
- Avoid qemu holding migration fd indefinitely (rhbz#620363)

* Sun Jan 09 2011 Jiri Denemark <jdenemar@redhat.com> - 0.8.7-1.el6
- Rebased to upstream 0.8.7 (rhbz#653985)
- The following bugs got fixed by the rebase:
    rhbz#586124, rhbz#595350, rhbz#611793, rhbz#611822, rhbz#617439,
    rhbz#620363, rhbz#626873, rhbz#627143, rhbz#628772, rhbz#639595,
    rhbz#639603, rhbz#656795, rhbz#658657, rhbz#659855, rhbz#660706,
    rhbz#664406, rhbz#665446

* Thu Dec 23 2010 Jiri Denemark <jdenemar@redhat.com> - 0.8.6-1.el6
- Rebased to upstream 0.8.6 (rhbz#653985)

* Fri Dec 10 2010 Jiri Denemark <jdenemar@redhat.com> - 0.8.1-29.el6
- spec file cleanups (rhbz#649523)
- Fix deadlock on concurrent multiple bidirectional migration (rhbz#659310)
- Fix funny error in clock-variable (rhbz#660194)
- Export host information through SMBIOS to guests (rhbz#526224)
- Ensure device is deleted from guest after unplug (rhbz#644015)
- Distinguish between QEMU domain shutdown and crash (rhbz#656845)

* Mon Nov 29 2010 Jiri Denemark <jdenemar@redhat.com> - 0.8.1-28.el6
- Fix JSON migrate_set_downtime command (rhbz#561935)
- Make SASL work over UNIX domain sockets (rhbz#641687)
- Let qemu group look below /var/lib/libvirt/qemu/ (rhbz#643407)
- Fix save/restore on root_squashed NFS (rhbz#643884)
- Fix race on multiple migration (rhbz#638285)
- Export host information through SMBIOS to guests (rhbz#526224)
- Support forcing a CDROM eject (rhbz#626305)

* Wed Aug 18 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-27
- build -26 hit a miscompilation error c.f. 624895 drop %{?_smp_mflags}
- Resolves: rhbz#620847
- Resolves: rhbz#623877

* Tue Aug 17 2010 Dave Allan <dallan@redhat.com> - 0.8.1-26
- Fix problem with capabilities XML generation
- Resolves: rhbz#620847
- Correctly reserve and release PCI slots
- Resolves: rhbz#623877

* Sun Aug 15 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-25
- fix PXE booting on the virtual network
- Resolves: rhbz#623951
- fix tunelled migration
- Resolves: rhbz#624062

* Thu Aug 12 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-24
- do not call balloon info command if balloon is desactivated
- Resolves: rhbz#617286

* Wed Aug 11 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-23
- give a way to desactivate memory balloon support
- Resolves: rhbz#617286

* Tue Aug 10 2010 Dave Allan <dallan@redhat.com> - 0.8.1-22
- Mitigate asynchronous device_del
- Resolves: rhbz#609437
- Fix PCI address allocation
- Resolves: rhbz#618484
- Make nodeinfo skip offline CPUs
- Resolves: rhbz#622515

* Tue Aug  3 2010 Dave Allan <dallan@redhat.com> - 0.8.1-21
- Fix multiple PCI device assignment bugs
- Resolves: rhbz#617116
- Fix the ACS checking in the PCI code
- Resolves: rhbz#615218
- Disable boot=on when not using KVM
- Resolves: rhbz#594068
- Don't leak delay string when freeing virInterfaceBridgeDefs
- Resolves: rhbz#620837

* Wed Jul 28 2010 Dave Allan <dallan@redhat.com> - 0.8.1-20
- Fix error message in guests init script when libvirtd isn't installed
- Resolves: rhbz#617527

* Tue Jul 27 2010 Dave Allan <dallan@redhat.com> - 0.8.1-19
- Add character device backend activating QEMU internal spice agent
- Resolves: rhbz#615757
- Make libvirt-guests initscript Fedora compliant
- Resolves: rhbz#617300

* Thu Jul 22 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-18
- Fix patch for PIIX3 slot 1 reservation, in case it's already reserved
- Resolves: rhbz#592026

* Wed Jul 21 2010 Dave Allan <dallan@redhat.com> - 0.8.1-17
- Set a stable & high MAC addr for guest TAP devices
- Resolves: rhbz#616517
- Fix bogus commit of -16 patches
- Related: rhbz#592026
- Related: rhbz#599590

* Wed Jul 21 2010 Dave Allan <dallan@redhat.com> - 0.8.1-16
- Make PCI device ordering consistent with older releases
- Resolves: rhbz#592026
- Fix libvirtd hang during concurrent bi-directional migration
- Resolves: rhbz#599590

* Wed Jul 14 2010 Dave Allan <dallan@redhat.com> - 0.8.1-15
- Add iptables rule to fixup DHCP response checksum
- Resolves: rhbz#612588

* Tue Jul 13 2010 Dave Allan <dallan@redhat.com> - 0.8.1-14
- Support virtio disk hotplug in JSON mode
- Resolves: rhbz#573946
- Fix QEMU monitor JSON crash
- Resolves: rhbz#604585
- CVE-2010-2237 CVE-2010-2238 CVE-2010-2239
- Resolves: rhbz#607817
- CVE-2010-2242 Apply a source port mapping to virtual network masquerading
- Resolves: rhbz#608049
- Fix hang if QEMU exits (almost) immediately
- Resolves: rhbz#610056
- Support new CPU models provided by qemu-kvm
- Resolves: rhbz#605830
- Fix comparison of two host CPUs
- Resolves: rhbz#611401
- Don't mess with the CPU returned by arch driver
- Resolves: rhbz#613014
- Fail when CPU type cannot be detected from XML
- Resolves: rhbz#613760
- Use -nodefconfig when probing for CPU models
- Resolves: rhbz#613764
- cpuCompare: Fix crash on unexpected CPU XML
- Resolves: rhbz#613765
- Properly report failure to create raw storage volume files
- Related: rhbz#547543
- Fix IOErrorReasonCallback python bindings
- Related: rhbz#586353
- Parthelper: canonicalize block device paths
- Related: rhbz#593785

* Wed Jun 30 2010 Dave Allan <dallan@redhat.com> - 0.8.1-13
- Don't invoke destroy callback from qemuMonitorOpen() failure paths (v2)
- Related: rhbz#609060

* Tue Jun 29 2010 Dave Allan <dallan@redhat.com> - 0.8.1-12
- Don't invoke destroy callback from qemuMonitorOpen() failure paths
- Resolves: rhbz#609060
- virFileResolveLink: guarantee an absolute path
- Resolves: rhbz#608092
- SPICE patches have translatable strings without format args
- Resolves: rhbz#608917
- No way to pass disk format type to pool-define-as nor pool-create-as
- Resolves: rhbz#597790
- Fix enforcement of direction of traffic for rules describing incoming traffic
- Resolves: rhbz#606889
- Clarify virsh help pool-create-as text
- Resolves: rhbz#609044

* Mon Jun 28 2010 Dave Allan <dallan@redhat.com> - 0.8.1-11
- Do not block during incoming migration
- Resolves: rhbz#579440
- Label serial devices
- Resolves: rhbz#585249
- parthelper: fix compilation without optimization
- Related: rhbz#593785
- Fix name/UUID uniqueness checking in storage/network
- Resolves: rhbz#593951
- Don't squash file permissions when migration fails
- Resolves: rhbz#607922
- Properly handle 'usbX' sysfs files
- Resolves: rhbz#603867
- add pool support to vol-key command & improve vol commands help
- Resolves: rhbz#598365
- document attach-disk better
- Resolves: rhbz#601143
- Config iptables to allow tftp port if network <tftp> element exists
- Resolves: rhbz#607294
- Fix failure to generate python bindings when libvirt.h.in is updated
- Related: rhbz#589465
- Allow all interface names
- Resolves: rhbz#593907
- Fix nodedevice refcounting
- Resolves: rhbz#608753
- Move nwfilter functions inside extern C and fix a locking bug
- Resolves: rhbz#597391
- Fix failure to restore qemu domains with selinux enforcing
- Resolves: rhbz#590975
- Check for presence of qemu -nodefconfig option before using it
- Resolves: rhbz#608859

* Mon Jun 21 2010 Dave Allan <dallan@redhat.com> - 0.8.1-10
- Add multiIQN XML output
- Resolves: rhbz#587700
- Fix udev node device parent-child device relationships
- Resolves: rhbz#593995
- Fix leaks in udev device add/remove
- Resolves: rhbz#595490
- Fix device destroy return value
- Resolves: rhbz#597998
- Update nodedev scsi_host data before use
- Resolves: rhbz#600048
- Display wireless devices in nodedev list
- Resolves: rhbz#604811
- Show pool and domain persistence
- Resolves: rhbz#603696
- Fix cleanup after failing to hotplug a PCI device
- Resolves: rhbz#605168
- Add '-nodefconfig' command line arg to QEMU
- Resolves: rhbz#602778
- Switch to private redhat namespace for QMP I/O error reason
- Resolves: rhbz#586353
- Improve error messages for missing drivers & unsupported functions
- Resolves: rhbz#595609
- macvtap: get interface index if not provided
- Resolves: rhbz#605187
- Fix leaks in remote code
- Resolves: rhbz#603442
- Add an optional switch --uuid to the virsh vol-pool command
- Resolves: rhbz#604929
- Change per-connection hashes to be indexed by UUIDs
- Resolves: rhbz#603494
- Run virsh from libvirt-guests script with /dev/null on stdin
- Resolves: rhbz#606314
- Increase dd block size to speed up domain save
- Resolves: rhbz#601775
- Fix reference counting bugs on qemu monitor
- Resolves: rhbz#602660
- Add missing action parameter in IO error callback
- Resolves: rhbz#607157

* Wed Jun 16 2010 Dave Allan <dallan@redhat.com> - 0.8.1-9
- Touch libvirt-guests lockfile
- Resolves: rhbz#566647
- Add qemu.conf option for clearing capabilities
- Resolves: rhbz#593903
- Add support for launching guest in paused state
- Resolves: rhbz#589465
- Add virsh vol-pool command
- Resolves: rhbz#602217
- Add vol commands to virsh man page
- Resolves: rhbz#600640
- Remove bogus migrate error messages
- Resolves: rhbz#601575


* Thu Jun 10 2010 Dave Allan <dallan@redhat.com> - 0.8.1-8
- Ensure virtio serial has stable addressing
- Resolves: rhbz#586665
- SELinux socket labelling on QEMU monitor socket for MLS
- Resolves: rhbz#593739
- Fix enumeration of partitions in disks with a trailing digit in path
- Resolves: rhbz#593785
- Enable probing of VPC disk format type
- Resolves: rhbz#597981
- Delete UNIX domain sockets upon daemon shutdown
- Resolves: rhbz#598163
- Fix Migration failure 'canonical hostname pointed to localhost'
- Resolves: rhbz#589864
- Fix up the python bindings for snapshotting
- Resolves: rhbz#591839
- Sanitize pool target paths
- Resolves: rhbz#593565
- Prevent host network conflicts
- Resolves: rhbz#594494
- Support 802.1Qbg and bh (vnlink/VEPA) (refresh)
- Resolves: rhbz#590110

* Wed May 26 2010 Dave Allan <dallan@redhat.com> - 0.8.1-7
- Fix sign extension error in libvirt's parsing of qemu options
- Resolves: rhbz#592070
- Graceful shutdown/suspend of libvirt guests on host shutdown
- Resolves: rhbz#566647
- Fix pci device hotplug
- Resolves: rhbz#572867
- Support 802.1Qbg and bh
- Resolves: rhbz#532760, rhbz#570949, rhbz#590110, rhbz#570923

* Wed May 19 2010 Dave Allan <dallan@redhat.com> - 0.8.1-6
- Support seamless migration of SPICE graphics clients (refresh)
- Resolves: rhbz#591551
- Fix swapping of PCI vendor & product names in udev backend
- Resolves: rhbz#578419
- Fix cgroup setup code to cope with root squashing NFS
- Resolves: rhbz#593193
- Fix startup error reporting race
- Resolves: rhbz#591272

* Tue May 18 2010 Dave Allan <dallan@redhat.com> - 0.8.1-5
- Don't reset user/group/security label for any files on shared filesystems
- Resolves: rhbz#578889
- Make saved state labelling ignore the dynamic_ownership parameter
- Resolves: rhbz#588562
- Fix & protect against NULL pointer dereference in monitor code
- Resolves: rhbz#591076
- Fix virFileResolveLink return value
- Resolves: rhbz#591363
- Add support for SSE4.1 and SSE4.2 CPU features
- Resolves: rhbz#592977

* Wed May 14 2010 Dave Allan <dallan@redhat.com> - 0.8.1-4
- query QEMU to get the actual allocated extent of a block device
- Resolves: rhbz#526289

* Wed May 12 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-3
- missing python bindings due to older XML api
- Resolves: rhbz#589453
- Fix two possible crashes in JSON event dispatch
- Resolves: rhbz#586353
- Fix handling of disk backing stores with cgroups
- Resolves: rhbz#581476
- virsh schedinfo --set error handling on unknow parameters
- Resolves: rhbz#586632
- Apply extra patches for nwfilter
- Resolves: rhbz#588554
- Fix hang during concurrent guest migrations
- Resolves: rhbz#582278

* Fri May  7 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-2
- Don't wipe generated iface target in active domains (588046)
- Fix LXC domain lookup and error handling (586361)
- Fix a protocol breakage introduced in libvirt-0.8.0
- Add support for nic hotplug in QEMU/KVM (589978)
- Seemless migration of spice graphics clients (589989)
- fix build with ESX support
- Resolves: rhbz#581966
- fix multilib problem (587231)

* Fri Apr 30 2010 Daniel Veillard <veillard@redhat.com> - 0.8.1-1
- Rebase to upstream 0.8.1
- Resolves: rhbz#558761

* Fri Apr 23 2010 Daniel Veillard <veillard@redhat.com> - 0.8.0-4
- Fix libvirtd startup when avahi failed to look up local host name
- CPU selection fixes
- Resolves: rhbz#581627
- fix migration poll value
- Resolves: rhbz#584928
- crash dump job caused libvirt hang
- Resolves: rhbz#580853
- Fix initial VCPU pinning in qemu driver
- Resolves: rhbz#578434
- fix cpu hotplug command names

* Tue Apr 20 2010 Daniel Veillard <veillard@redhat.com> - 0.8.0-3
- Build ESX support in
- Resolves: rhbz#581966
- a batch of network filter fixes, IBM request and upstream fixes
- Resolves: rhbz#579993
- couple of patchs to fix device handling with QMP
- Related: rhbz#563189
- fix python binding for snapshotting
- spec file fixes for nwfiler build and RHEL-5 virt-v2v specific rebuild

* Tue Apr 13 2010 Daniel P. Berrange <berrange@redhat.com> - 0.8.0-2
- Refresh SPICE patches to fix test failures
- Related: rhbz#515265, rhbz#524623, rhbz#573382
- Enable test suite during build, disabling tests that don't work in mock
- Related: rhbz#558761

* Mon Apr 12 2010 Daniel Veillard <veillard@redhat.com> - 0.8.0-1
- official 0.8.0 upstream release
- Resolves: rhbz#558761
- new patch set of patches for RHEL-6 SPICE and addons
- Enable QMP/ JSON mode in the QEMU monitor
- Resolves: rhbz#563189
- Support configuration of SPICE as a graphics protocol
- Resolves: rhbz#515265
- vnc (and spice) ticketing
- Resolves: rhbz#524623
- enable spice tls encryption in domainXML, and which channels are encrypted
- Resolves: rhbz#573382
- notification of VNC/SPICE client disconnect/connect events
- Resolves: rhbz#515268

* Wed Apr  7 2010 Daniel Veillard <veillard@redhat.com> - 0.8.0-0.pre20100407
- preview #4 for 0.8.0 rebase
- snapshot API
- domain with disk on root-squashing nfs and security driver mismatch
- Resolves: rhbz#578630
- Fail to read xml when restore domain
- Resolves: rhbz#577719
- loop "virsh cd" in virsh interactive terminal generate unknown error
- Resolves: rhbz#572380
- support setting qemu's -drive werror=stop/enospc with configuration
- Resolves: rhbz#526231

* Mon Mar 30 2010 Daniel Veillard <veillard@redhat.com> - 0.7.8-0.pre20100330
- preview #3 for 0.7.8 rebase
- kvm hpet support
- Resolves: rhbz#576973
- hook scripts support
- Resolves: rhbz#569965
- Need to add time keeping abstraction
- Resolves: rhbz#557285
- notification of guest reboot
- Resolves: rhbz#527572
- Ability to preserve RTC clock adjustments across guest reboots
- Resolves: rhbz#515273
- Notifications of guest stopping due to disk I/O errors
- Resolves: rhbz#515270
- VNC ticketing support (524623) spice still needed
- VNC client disconnect/connect events (515268) spice still needed

* Mon Mar 22 2010 Daniel Veillard <veillard@redhat.com> - 0.7.8-0.pre20100322
- preview #2 for 0.7.8 rebase
- migration max downtime API
- Resolves: rhbz#561935
- allow suspend during migration
- Resolves: rhbz#561934
- support vhost net mode at qemu startup for net devices
- Resolves: rhbz#540391
- read-only device access support for qemu
- Resolves: rhbz#556769
- LSB compliance of libvirtd init script
- Resolves: rhbz#538701
- No domain vcpu information output when using JSON monitor
- Resolves: rhbz#572051
- "qemudDomainSetMaxMemory" does not work and should be removed
- Resolves: rhbz#572146
- after setvcpus, any virsh command will be hung
- Resolves: rhbz#572193
- virsh interactive terminal crash or hung
- Resolves: rhbz#572376
- virsh hangs after core dump
- Resolves: rhbz#572544
- Fix very slow file allocation on ext3

* Fri Mar 12 2010 Daniel Veillard <veillard@redhat.com> - 0.7.8-0.pre20100312
- preview for 0.7.8 rebase
- Extra non upstream basic patch for spice and XQL
- Resolves: rhbz#515264
- Resolves: rhbz#515265
- connected virsh dies with a SIGPIPE after libvirtd restart
- Resolves: rhbz#526656
- error when running logrotate on s/390x arch
- Resolves: rhbz#547514

* Fri Mar  5 2010 Daniel Veillard <veillard@redhat.com> - 0.7.7-1
- macvtap support (rhbz#553348)
- async job handling (rhbz #515278)
- virtio channel (rhbz#515281)
- computing baseline CPU
- virDomain{Attach,Detach}DeviceFlags
- Improve libvirt error reporting for failed migrations (rhbz#528793)
- qemu driver support CPU hotplug (rhbz#533138)
- wrong (octal) device number for attaching USB devices (rhbz#549840)
- cannot save domain into root_squashing nfs export (rhbz#558763)
- assorted bug fixes and lots of cleanups

* Wed Mar  3 2010 Daniel P. Berrange <berrange@redhat.com> - 0.7.6-4
- Fix balloon parameter name handling in JSON mode (rhbz #566261)

* Fri Feb 26 2010 Daniel P. Berrange <berrange@redhat.com> - 0.7.6-3
- Fix balloon units handling in JSON mode (rhbz #566261)
- Invoke qmp_capabilities at monitor startup (rhbz #563189)

* Wed Feb 10 2010 Daniel Veillard <veillard@redhat.com> - 0.7.6-2
- enable JSON interface, desactivated by default in 0.7.6
- Resolves: rhbz#563189
- make sure cgroups are installed and that cgconfig service is on
- Resolves: rhbz#531263

* Wed Feb  3 2010 Daniel Veillard <veillard@redhat.com> - 0.7.6-1
- upstream release of 0.7.6
- Use QEmu new device adressing when possible
- Implement CPU topology support for QEMU driver
- Implement SCSI controller hotplug/unplug for QEMU
- Implement support for multi IQN
- a lot of fixes and improvements
- Resolves: rhbz#558761

* Fri Jan 22 2010 Daniel Veillard <veillard@redhat.com> - 0.7.6-0.pre20100121
- push updated prerelease version of 0.7.6 for testing in Beta1
- Resolves: rhbz#515213

* Thu Jan 21 2010 Daniel Veillard <veillard@redhat.com> - 0.7.6-0.pre20100121
- Push a prerelease version of 0.7.6 for testing in Beta1
- Allow specifying -cpu model/flags for qemu
- Resolves: rhbz#515213
- Add async qemu machine protocol to libvirt based on JSON QEmu API
- Resolves: rhbz#518701
- Allow for static PCI address assignment to all devices
- Resolves: rhbz#481924
- expose qemu's -fda fat:floppy feature (525074)
- configuration of virtual CPU topology (sockets, threads, cores) (538015)
- rewrite file chown'ing code to use security driver framework (547545 )
- cannot create a headless KVM virtual machine (548127)
- Improve virsh schedular parameters documentation (548485)
- Fail to delete a inactive pool using command "virsh pool-delete" (530985)
- virsh man page updation for using container (lxc:///) (528709)
- Command 'virsh vcpuinfo' returns libvirt error in RHEL6 with KVM (522829)
- Expose information about host CPU flags in capabilities (518062)

* Fri Jan 15 2010 Daniel P. Berrange <berrange@redhat.com> - 0.7.5-2
- Rebuild for libparted soname change (rhbz #555741)

* Wed Dec 23 2009 Daniel Veillard <veillard@redhat.com> - 0.7.5-1
- Add new API virDomainMemoryStats
- Public API and domain extension for CPU flags
- vbox: Add support for version 3.1
- Support QEMU's virtual FAT block device driver
- a lot of fixes

* Fri Nov 20 2009 Daniel Veillard <veillard@redhat.com> - 0.7.4-1
- upstream release of 0.7.4
- udev node device backend
- API to check object properties
- better QEmu monitor processing
- MAC address based port filtering for qemu
- support IPv6 and multiple addresses per interfaces
- a lot of fixes

* Thu Nov 19 2009 Daniel P. Berrange <berrange@redhat.com> - 0.7.2-6
- Really fix restore file labelling this time

* Wed Nov 11 2009 Daniel P. Berrange <berrange@redhat.com> - 0.7.2-5
- Disable numactl on s390[x]. Again.

* Wed Nov 11 2009 Daniel P. Berrange <berrange@redhat.com> - 0.7.2-4
- Fix QEMU save/restore permissions / labelling

* Thu Oct 29 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.2-3
- Avoid compressing small log files (#531030)

* Thu Oct 29 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.2-2
- Make libvirt-devel require libvirt-client, not libvirt
- Fix qemu machine types handling

* Wed Oct 14 2009 Daniel Veillard <veillard@redhat.com> - 0.7.2-1
- Upstream release of 0.7.2
- Allow to define ESX domains
- Allows suspend and resulme of LXC domains
- API for data streams
- many bug fixes

* Tue Oct 13 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-12
- Fix restore of qemu guest using raw save format (#523158)

* Fri Oct  9 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-11
- Fix libvirtd memory leak during error reply sending (#528162)
- Add several PCI hot-unplug typo fixes from upstream

* Tue Oct  6 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-10
- Create /var/log/libvirt/{lxc,uml} dirs for logrotate
- Make libvirt-python dependon on libvirt-client
- Sync misc minor changes from upstream spec

* Tue Oct  6 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-9
- Change logrotate config to weekly (#526769)

* Thu Oct  1 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-8
- Disable sound backend, even when selinux is disabled (#524499)
- Re-label qcow2 backing files (#497131)

* Wed Sep 30 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-7
- Fix USB device passthrough (#522683)

* Mon Sep 21 2009 Chris Weyl <cweyl@alumni.drew.edu> - 0.7.1-6
- rebuild for libssh2 1.2

* Mon Sep 21 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-5
- Don't set a bogus error in virDrvSupportsFeature()
- Fix raw save format

* Thu Sep 17 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-4
- A couple of hot-unplug memory handling fixes (#523953)

* Thu Sep 17 2009 Daniel Veillard <veillard@redhat.com> - 0.7.1-3
- disable numactl on s390[x]

* Thu Sep 17 2009 Daniel Veillard <veillard@redhat.com> - 0.7.1-2
- revamp of spec file for modularity and RHELs

* Tue Sep 15 2009 Daniel Veillard <veillard@redhat.com> - 0.7.1-1
- Upstream release of 0.7.1
- ESX, VBox driver updates
- mutipath support
- support for encrypted (qcow) volume
- compressed save image format for Qemu/KVM
- QEmu host PCI device hotplug support
- configuration of huge pages in guests
- a lot of fixes

* Mon Sep 14 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-0.2.gitfac3f4c
- Update to newer snapshot of 0.7.1
- Stop libvirt using untrusted 'info vcpus' PID data (#520864)
- Support relabelling of USB and PCI devices
- Enable multipath storage support
- Restart libvirtd upon RPM upgrade

* Sun Sep  6 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.1-0.1.gitg3ef2e05
- Update to pre-release git snapshot of 0.7.1
- Drop upstreamed patches

* Wed Aug 19 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.0-6
- Fix migration completion with newer versions of qemu (#516187)

* Wed Aug 19 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.0-5
- Add PCI host device hotplug support
- Allow PCI bus reset to reset other devices (#499678)
- Fix stupid PCI reset error message (bug #499678)
- Allow PM reset on multi-function PCI devices (bug #515689)
- Re-attach PCI host devices after guest shuts down (bug #499561)
- Fix list corruption after disk hot-unplug
- Fix minor 'virsh nodedev-list --tree' annoyance

* Thu Aug 13 2009 Daniel P. Berrange <berrange@redhat.com> - 0.7.0-4
- Rewrite policykit support (rhbz #499970)
- Log and ignore NUMA topology problems (rhbz #506590)

* Mon Aug 10 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.0-3
- Don't fail to start network if ipv6 modules is not loaded (#516497)

* Thu Aug  6 2009 Mark McLoughlin <markmc@redhat.com> - 0.7.0-2
- Make sure qemu can access kernel/initrd (bug #516034)
- Set perms on /var/lib/libvirt/boot to 0711 (bug #516034)

* Wed Aug  5 2009 Daniel Veillard <veillard@redhat.com> - 0.7.0-1
- ESX, VBox3, Power Hypervisor drivers
- new net filesystem glusterfs
- Storage cloning for LVM and Disk backends
- interface implementation based on netcf
- Support cgroups in QEMU driver
- QEmu hotplug NIC support
- a lot of fixes

* Fri Jul  3 2009 Daniel Veillard <veillard@redhat.com> - 0.6.5-1
- release of 0.6.5

* Fri May 29 2009 Daniel Veillard <veillard@redhat.com> - 0.6.4-1
- release of 0.6.4
- various new APIs

* Fri Apr 24 2009 Daniel Veillard <veillard@redhat.com> - 0.6.3-1
- release of 0.6.3
- VirtualBox driver

* Fri Apr  3 2009 Daniel Veillard <veillard@redhat.com> - 0.6.2-1
- release of 0.6.2

* Fri Mar  4 2009 Daniel Veillard <veillard@redhat.com> - 0.6.1-1
- release of 0.6.1

* Sat Jan 31 2009 Daniel Veillard <veillard@redhat.com> - 0.6.0-1
- release of 0.6.0

* Tue Nov 25 2008 Daniel Veillard <veillard@redhat.com> - 0.5.0-1
- release of 0.5.0

* Tue Sep 23 2008 Daniel Veillard <veillard@redhat.com> - 0.4.6-1
- release of 0.4.6

* Mon Sep  8 2008 Daniel Veillard <veillard@redhat.com> - 0.4.5-1
- release of 0.4.5

* Wed Jun 25 2008 Daniel Veillard <veillard@redhat.com> - 0.4.4-1
- release of 0.4.4
- mostly a few bug fixes from 0.4.3

* Thu Jun 12 2008 Daniel Veillard <veillard@redhat.com> - 0.4.3-1
- release of 0.4.3
- lots of bug fixes and small improvements

* Tue Apr  8 2008 Daniel Veillard <veillard@redhat.com> - 0.4.2-1
- release of 0.4.2
- lots of bug fixes and small improvements

* Mon Mar  3 2008 Daniel Veillard <veillard@redhat.com> - 0.4.1-1
- Release of 0.4.1
- Storage APIs
- xenner support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Tue Dec 18 2007 Daniel Veillard <veillard@redhat.com> - 0.4.0-1
- Release of 0.4.0
- SASL based authentication
- PolicyKit authentication
- improved NUMA and statistics support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Sun Sep 30 2007 Daniel Veillard <veillard@redhat.com> - 0.3.3-1
- Release of 0.3.3
- Avahi support
- NUMA support
- lots of assorted improvements, bugfixes and cleanups
- documentation and localization improvements

* Tue Aug 21 2007 Daniel Veillard <veillard@redhat.com> - 0.3.2-1
- Release of 0.3.2
- API for domains migration
- APIs for collecting statistics on disks and interfaces
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Tue Jul 24 2007 Daniel Veillard <veillard@redhat.com> - 0.3.1-1
- Release of 0.3.1
- localtime clock support
- PS/2 and USB input devices
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Mon Jul  9 2007 Daniel Veillard <veillard@redhat.com> - 0.3.0-1
- Release of 0.3.0
- Secure remote access support
- unification of daemons
- lots of assorted bugfixes and cleanups
- documentation and localization improvements

* Fri Jun  8 2007 Daniel Veillard <veillard@redhat.com> - 0.2.3-1
- Release of 0.2.3
- lot of assorted bugfixes and cleanups
- support for Xen-3.1
- new scheduler API

* Tue Apr 17 2007 Daniel Veillard <veillard@redhat.com> - 0.2.2-1
- Release of 0.2.2
- lot of assorted bugfixes and cleanups
- preparing for Xen-3.0.5

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 0.2.1-2.fc7
- don't require xen; we don't need the daemon and can control non-xen now
- fix scriptlet error (need to own more directories)
- update description text

* Fri Mar 16 2007 Daniel Veillard <veillard@redhat.com> - 0.2.1-1
- Release of 0.2.1
- lot of bug and portability fixes
- Add support for network autostart and init scripts
- New API to detect the virtualization capabilities of a host
- Documentation updates

* Fri Feb 23 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-4.fc7
- Fix loading of guest & network configs

* Fri Feb 16 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-3.fc7
- Disable kqemu support since its not in Fedora qemu binary
- Fix for -vnc arg syntax change in 0.9.0  QEMU

* Thu Feb 15 2007 Daniel P. Berrange <berrange@redhat.com> - 0.2.0-2.fc7
- Fixed path to qemu daemon for autostart
- Fixed generation of <features> block in XML
- Pre-create config directory at startup

* Wed Feb 14 2007 Daniel Veillard <veillard@redhat.com> 0.2.0-1.fc7
- support for KVM and QEmu
- support for network configuration
- assorted fixes

* Mon Jan 22 2007 Daniel Veillard <veillard@redhat.com> 0.1.11-1.fc7
- finish inactive Xen domains support
- memory leak fix
- RelaxNG schemas for XML configs

* Wed Dec 20 2006 Daniel Veillard <veillard@redhat.com> 0.1.10-1.fc7
- support for inactive Xen domains
- improved support for Xen display and vnc
- a few bug fixes
- localization updates

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.1.9-2
- rebuild against python 2.5

* Wed Nov 29 2006 Daniel Veillard <veillard@redhat.com> 0.1.9-1
- better error reporting
- python bindings fixes and extensions
- add support for shareable drives
- add support for non-bridge style networking
- hot plug device support
- added support for inactive domains
- API to dump core of domains
- various bug fixes, cleanups and improvements
- updated the localization

* Tue Nov  7 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-3
- it's pkgconfig not pgkconfig !

* Mon Nov  6 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-2
- fixing spec file, added %dist, -devel requires pkgconfig and xen-devel
- Resolves: rhbz#202320

* Mon Oct 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.8-1
- fix missing page size detection code for ia64
- fix mlock size when getting domain info list from hypervisor
- vcpu number initialization
- don't label crashed domains as shut off
- fix virsh man page
- blktapdd support for alternate drivers like blktap
- memory leak fixes (xend interface and XML parsing)
- compile fix
- mlock/munlock size fixes

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.7-1
- Fix bug when running against xen-3.0.3 hypercalls
- Fix memory bug when getting vcpus info from xend

* Fri Sep 22 2006 Daniel Veillard <veillard@redhat.com> 0.1.6-1
- Support for localization
- Support for new Xen-3.0.3 cdrom and disk configuration
- Support for setting VNC port
- Fix bug when running against xen-3.0.2 hypercalls
- Fix reconnection problem when talking directly to http xend

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 0.1.5-3
- patch from danpb to support new-format cd devices for HVM guests

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-2
- reactivating ia64 support

* Tue Sep  5 2006 Daniel Veillard <veillard@redhat.com> 0.1.5-1
- new release
- bug fixes
- support for new hypervisor calls
- early code for config files and defined domains

* Mon Sep  4 2006 Daniel Berrange <berrange@redhat.com> - 0.1.4-5
- add patch to address dom0_ops API breakage in Xen 3.0.3 tree

* Mon Aug 28 2006 Jeremy Katz <katzj@redhat.com> - 0.1.4-4
- add patch to support paravirt framebuffer in Xen

* Mon Aug 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-3
- another patch to fix network handling in non-HVM guests

* Thu Aug 17 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-2
- patch to fix virParseUUID()

* Wed Aug 16 2006 Daniel Veillard <veillard@redhat.com> 0.1.4-1
- vCPUs and affinity support
- more complete XML, console and boot options
- specific features support
- enforced read-only connections
- various improvements, bug fixes

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-6
- add patch from pvetere to allow getting uuid from libvirt

* Wed Aug  2 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-5
- build on ia64 now

* Thu Jul 27 2006 Jeremy Katz <katzj@redhat.com> - 0.1.3-4
- don't BR xen, we just need xen-devel

* Thu Jul 27 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-3
- need rebuild since libxenstore is now versionned

* Mon Jul 24 2006 Mark McLoughlin <markmc@redhat.com> - 0.1.3-2
- Add BuildRequires: xen-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.3-1.1
- rebuild

* Tue Jul 11 2006 Daniel Veillard <veillard@redhat.com> 0.1.3-1
- support for HVM Xen guests
- various bugfixes

* Mon Jul  3 2006 Daniel Veillard <veillard@redhat.com> 0.1.2-1
- added a proxy mechanism for read only access using httpu
- fixed header includes paths

* Wed Jun 21 2006 Daniel Veillard <veillard@redhat.com> 0.1.1-1
- extend and cleanup the driver infrastructure and code
- python examples
- extend uuid support
- bug fixes, buffer handling cleanups
- support for new Xen hypervisor API
- test driver for unit testing
- virsh --conect argument

* Mon Apr 10 2006 Daniel Veillard <veillard@redhat.com> 0.1.0-1
- various fixes
- new APIs: for Node information and Reboot
- virsh improvements and extensions
- documentation updates and man page
- enhancement and fixes of the XML description format

* Tue Feb 28 2006 Daniel Veillard <veillard@redhat.com> 0.0.6-1
- added error handling APIs
- small bug fixes
- improve python bindings
- augment documentation and regression tests

* Thu Feb 23 2006 Daniel Veillard <veillard@redhat.com> 0.0.5-1
- new domain creation API
- new UUID based APIs
- more tests, documentation, devhelp
- bug fixes

* Fri Feb 10 2006 Daniel Veillard <veillard@redhat.com> 0.0.4-1
- fixes some problems in 0.0.3 due to the change of names

* Wed Feb  8 2006 Daniel Veillard <veillard@redhat.com> 0.0.3-1
- changed library name to libvirt from libvir, complete and test the python
  bindings

* Sun Jan 29 2006 Daniel Veillard <veillard@redhat.com> 0.0.2-1
- upstream release of 0.0.2, use xend, save and restore added, python bindings
  fixed

* Wed Nov  2 2005 Daniel Veillard <veillard@redhat.com> 0.0.1-1
- created
