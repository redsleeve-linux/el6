###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

# keep around ready for later user
## global alphatag rc4

Name: rgmanager
Summary: Open Source HA Resource Group Failover for Red Hat Cluster
Version: 3.0.12.1
Release: 26%{?alphatag:.%{alphatag}}%{?dist}.3
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/cluster/wiki/
Source0: https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.bz2
Patch0: bz690191_rgmanager_improve_exclusive_prioritization_handling.patch
Patch1: bz716231_fix_bad_passing_of_sfl_failure_up.patch
Patch2: bz692895_fix_segfault_on_config_reload.patch
Patch3: bz673167_make_handling_of_failed_services_consistent.patch
Patch4: bz697446-fix_race_in_shutdown_vs_notification.patch
Patch5: bz697446-2-fix_segfault_caused_by_unref_race.patch
Patch6: bz723925-add_disabled_configuration_option.patch
Patch7: bz734730-fix_uninitialized_variable.patch
Patch8: bz741607-clean_up_dbus_concurrency.patch
Patch9: bz741607-2-block_signals_when_dealing_with_dbus.patch
Patch10: bz635152-resolve_rare_deadlock.patch
Patch11: bz727326-fix_clusvcadm_message_when_run_with_f.patch
Patch12: bz743218-add_extra_service_status_call.patch
Patch13: bz743218-2-avoid_duplicate_restart_of_service.patch
Patch14: bz743218-3-fix_call_to_service_status.patch
Patch15: bz743218-4-fix_tiny_memory_leak_in_sl_service_status.patch
Patch16: bz743218-5-fix_dependency_issue_related_to_ordering.patch
Patch17: bz744824-fix_dependency_restart_bug_in_cp_mode.patch
Patch18: bz745226-add_f_to_clusvcadm_man_page.patch
Patch19: bz796272-retry_when_config_is_out_of_sync.patch
Patch20: bz803474.patch
Patch21: bz799505-rgmanager_add_simple_locking_over_cpg.patch
Patch22: bz799505-2-rgmanager_merge_upstream_cpglockd.patch
Patch23: bz799505-3-rgmanager_sync_cpglock_bits_with_upstream.patch
Patch24: bz799505-4-rgmanager_sync_cpglock_bits_with_upstream.patch
Patch25: bz799505-5-rgmanager_start_cpglockd_automatically_when_rrp_mode.patch
Patch26: bz799505-6-rgmanager_add_a_utility_to_dump_the_cpglockd_state.patch
Patch27: bz799505-7-allow_c_to_take_a_1_or_0_argument_to_respectively.patch
Patch28: bz799505-8-cleanup_and_exit_if_we_receive_a_sigterm.patch
Patch29: bz799505-9-add_a_simple_init_script_for_cpglockd_the_rgmanager.patch
Patch30: bz799505-10-update_makefile_for_cpglockd_init_script.patch
Patch31: bz799505-11-cleanup_the_makefile_and_add_support_to_the_cpglockd.patch
Patch32: bz799505-12-cpglockd_cleanup_startup_init_scripts_and_drop_code.patch
Patch33: bz799505-13-cpglockd_fix_pid_file_creation_and_check_if_daemon_is.patch
Patch34: bz799505-14-cpglockd_fix_a_startup_race_condition.patch
Patch35: bz799505-15-rgmanager_cleanup_binary_linking_and_include_dirs.patch
Patch36: bz799505-16-cpglock_drop_unused_define.patch
Patch37: bz799505-17-cpglockd_make_network_comm_endian_free.patch
Patch38: bz799505-18-clean_up_the_pid_file_when_exiting_after_running_with.patch
Patch39: bz799505-19-cpglockd_use_standard_logging_infrastructure.patch
Patch40: bz799505-20-cpglockd_refuse_to_shutdown_if_clients_are_connected.patch
Patch41: bz799505-21-rgmanager_transmogrify_states_to_expected_values.patch
Patch42: bz799505-22-rgmanager_die_hard_if_we_cpglockd_dies.patch
Patch43: bz799505-23-convert_all_remaining_calls_to_printf_and_perror_for.patch
Patch44: bz799505-24-if_we_see_a_join_message_from_ourselves,_move.patch
Patch45: bz799505-25-cpglockd_show_that_we_are_alive_while_waiting_for.patch
Patch46: bz799505-26-fix_operation_when_quorum_is_lost_nak_all_pending.patch
Patch47: bz799505-27-rgmanager_fix_cpglockd_vs_rgmanager_startup_race.patch
Patch48: bz799505-28-print_cpg_mcast_joined_return_value_and_errno_if_it.patch
Patch49: bz799505-29-add_some_additional_debugging_logging_for_try_locks.patch
Patch50: bz799505-30-set_m_owner_nodeid_to_the_our_node_id_when_naking.patch
Patch51: bz799505-31-copy_lock_messages_before_swapping_bytes_because_we.patch
Patch52: bz799505-32-rgmanager_fix_conditional_check_for_cpglockd_startup.patch
Patch53: bz799505-33-work_around_a_fenced_hang_delay_that_can_result_in_us.patch
Patch54: bz799505-34-poll_for_fenced_node_updates_less_aggressively_while.patch
Patch55: bz799505-35-replace_printf_and_fprintf_calls_with_logt_print_in.patch
Patch56: bz799505-36-increment_the_recovered_locks_count_when_a_client_is.patch
Patch57: bz799505-37-rgmanager_retry_connection_to_cpglockd.patch
Patch58: bz799505-38-rgmanager_add_man_page_for_cpglockd_update.patch
Patch59: bz799505-39-install_the_new_cpglockd_man_page.patch
Patch60: bz807165-fix_dependent_service_handling_during_recovery.patch
Patch61: bz799505-fix_a_hang_triggered_when_fencing_completes_in.patch
Patch62: bz825375-fix_a_crash_when_dbus_notifications_are.patch
Patch63: bz861157-fix_for_deadlock.patch
Patch64: bz853251-ocf_not_installed_is_ok_if_we_stop_when_stopped.patch
Patch65: bz831648-randomize_node_list_when_relocating_with_no.patch
Patch66: bz861157-fix_return_code_when_a_service_would_deadlock.patch
Patch67: bz879031-update_status_after_resource_recovery.patch
Patch68: bz983296-fix_potential_unlocked_memory_access.patch
Patch69: bz983296-2-fix_for_double_pthread_mutex_unlock_calls.patch
Patch70: bz983296-3-don_t_destroy_locked_mutexes.patch
Patch71: bz983296-4-fix_unlikely_null_ptr_deref.patch
Patch72: bz862075-delay_recovery_when_rgmanager_dies_unexpectedly.patch
Patch73: bz952729-clusvcadm_if_service_doesn_t_exist,_try.patch
Patch74: bz1018079-don_t_crash_if_a_resource_agent_does_not.patch
Patch75: bz1033162-fix_rg_test_exit_status_on_failures.patch
Patch76: bz1036652-resrules_make_expand_time_buffer_less.patch
Patch77: bz1053739-fix_error_logging_when_building_the_resource.patch
Patch78: bz982820-add_an_option_to_reboot_on_pid_exhaustion.patch
Patch79: bz1079207-fix_potential_null_ptr_deref_in_clustat.patch
Patch80: bz1128877-log_a_warning_when_the_non_critical_flag_is.patch
Patch81: bz1151199-don_t_restart_locally_if_failover_domain.patch
Patch82: bz1197122-don_t_relocate_a_service_if_policy_should_prevent_it.patch
Patch83: bz1128877-log_more_errors_during_resource_loading.patch
Patch84: bz1278943-fix_bash_syntax_error_in_clunfslock.patch
Patch85: bz1278943-2-clunfslock_copy_state_info_if_it_exists.patch
Patch86: bz1128877-turn_down_log_level_on_debug_message.patch
Patch87: bz1335412-rgmanager-Re-init-the-resource-tree-when-quorum-is-r.patch
Patch88: bz1335412-2-re_init_the_vf_key_callbacks_after_losing_and.patch
Patch89: bz1335412-3-forget_that_we_were_transition_master_on.patch
Patch90: bz1335412-4-fix_missing_function_prototype.patch
Patch91: bz1343345-check_for_null_when_attempting_to_access_the_member_list.patch
Patch92: bz1344640-exit_more_gracefully_if_cman_stops_first.patch

## runtime

Requires(post): chkconfig
Requires(preun): initscripts
Requires(preun): chkconfig
Requires: chkconfig initscripts 
Requires: cman dbus
Requires: resource-agents >= 3.9.1-1
Obsoletes: resource-agents < 3.9.1

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: clusterlib-devel >= 3.0.0-1
BuildRequires: libxml2-devel ncurses-devel slang-devel
BuildRequires: dbus-devel
BuildRequires: corosynclib-devel

ExclusiveArch: i686 x86_64

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .bz690191_rgmanager_improve_exclusive_prioritization_handling
%patch1 -p1 -b .bz716231_fix_bad_passing_of_sfl_failure_up
%patch2 -p1 -b .bz692895_fix_segfault_on_config_reload
%patch3 -p1 -b .bz673167_make_handling_of_failed_services_consistent
%patch4 -p1 -b .bz697446.1
%patch5 -p1 -b .bz697446.2
%patch6 -p1 -b .bz723925.1
%patch7 -p1 -b .bz734730.1
%patch8 -p1 -b .bz741607.1
%patch9 -p1 -b .bz741607.2
%patch10 -p1 -b .bz635152.1
%patch11 -p1 -b .bz727326.1
%patch12 -p1 -b .bz743218.1
%patch13 -p1 -b .bz743218.2
%patch14 -p1 -b .bz743218.3
%patch15 -p1 -b .bz743218.4
%patch16 -p1 -b .bz743218.5
%patch17 -p1 -b .bz744824.1
%patch18 -p1 -b .bz745226.1
%patch19 -p1 -b .bz796272.1
%patch20 -p1 -b .bz803474.1
%patch21 -p1 -b .bz799505.1
%patch22 -p1 -b .bz799505.2
%patch23 -p1 -b .bz799505.3
%patch24 -p1 -b .bz799505.4
%patch25 -p1 -b .bz799505.5
%patch26 -p1 -b .bz799505.6
%patch27 -p1 -b .bz799505.7
%patch28 -p1 -b .bz799505.8
%patch29 -p1 -b .bz799505.9
%patch30 -p1 -b .bz799505.10
%patch31 -p1 -b .bz799505.11
%patch32 -p1 -b .bz799505.12
%patch33 -p1 -b .bz799505.13
%patch34 -p1 -b .bz799505.14
%patch35 -p1 -b .bz799505.15
%patch36 -p1 -b .bz799505.16
%patch37 -p1 -b .bz799505.17
%patch38 -p1 -b .bz799505.18
%patch39 -p1 -b .bz799505.19
%patch40 -p1 -b .bz799505.20
%patch41 -p1 -b .bz799505.21
%patch42 -p1 -b .bz799505.22
%patch43 -p1 -b .bz799505.23
%patch44 -p1 -b .bz799505.24
%patch45 -p1 -b .bz799505.25
%patch46 -p1 -b .bz799505.26
%patch47 -p1 -b .bz799505.27
%patch48 -p1 -b .bz799505.28
%patch49 -p1 -b .bz799505.29
%patch50 -p1 -b .bz799505.30
%patch51 -p1 -b .bz799505.31
%patch52 -p1 -b .bz799505.32
%patch53 -p1 -b .bz799505.33
%patch54 -p1 -b .bz799505.34
%patch55 -p1 -b .bz799505.35
%patch56 -p1 -b .bz799505.36
%patch57 -p1 -b .bz799505.37
%patch58 -p1 -b .bz799505.38
%patch59 -p1 -b .bz799505.39
%patch60 -p1 -b .bz807165.1
%patch61 -p1 -b .bz799505.40
%patch62 -p1 -b .bz825375.1
%patch63 -p1 -b .bz861157.1
%patch64 -p1 -b .bz853251.1
%patch65 -p1 -b .bz831648.1
%patch66 -p1 -b .bz861157.1
%patch67 -p1 -b .bz879031.1
%patch68 -p1 -b .bz983296.1
%patch69 -p1 -b .bz983296.2
%patch70 -p1 -b .bz983296.3
%patch71 -p1 -b .bz983296.4
%patch72 -p1 -b .bz862075.1
%patch73 -p1 -b .bz952729.1
%patch74 -p1 -b .bz1018079.1
%patch75 -p1 -b .bz1033162.1
%patch76 -p1 -b .bz1036652.1
%patch77 -p1 -b .bz1053739.1
%patch78 -p1 -b .bz982820.1
%patch79 -p1 -b .bz1079207.1
%patch80 -p1 -b .bz1128877.1
%patch81 -p1 -b .bz1151199.1
%patch82 -p1 -b .bz1197122.1
%patch83 -p1 -b .bz1128877.1
%patch84 -p1 -b .bz1278943.1
%patch85 -p1 -b .bz1278943.2
%patch86 -p1 -b .bz1128877.2
%patch87 -p1 -b .bz1335412.1
%patch88 -p1 -b .bz1335412.2
%patch89 -p1 -b .bz1335412.3
%patch90 -p1 -b .bz1335412.4
%patch91 -p1 -b .bz1343345.1
%patch92 -p1 -b .bz1344640.1

%build
./configure \
  --sbindir=%{_sbindir} \
  --initddir=%{_sysconfdir}/rc.d/init.d \
  --libdir=%{_libdir} \
  --disable_kernel_check

##CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}
CFLAGS="$(echo '%{optflags}')" make -C rgmanager all

%install
rm -rf %{buildroot}
make -C rgmanager install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cp rgmanager/init.d/cpglockd.init.defaults \
  %{buildroot}%{_sysconfdir}/sysconfig/cpglockd

%clean
rm -rf %{buildroot}

%description
Red Hat Resource Group Manager provides high availability of critical server
applications in the event of planned or unplanned system downtime.

%post
/sbin/chkconfig --add rgmanager
/sbin/chkconfig --add cpglockd

%preun
if [ "$1" = 0 ]; then
	/sbin/service rgmanager stop >/dev/null 2>&1
	/sbin/chkconfig --del rgmanager
	/sbin/chkconfig --del cpglockd
fi

%files
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence rgmanager/README rgmanager/errors.txt
%{_sysconfdir}/rc.d/init.d/rgmanager
%{_sysconfdir}/rc.d/init.d/cpglockd
%{_sbindir}/clu*
%{_sbindir}/rgmanager
%{_sbindir}/rg_test
%{_sbindir}/cpglockd
%{_sbindir}/cpglockdump
%{_datadir}/cluster
%{_mandir}/man8/clu*
%{_mandir}/man8/rgmanager*
%{_mandir}/man8/cpglockd*
%config(noreplace) %{_sysconfdir}/sysconfig/cpglockd

%changelog
* Fri Jun 10 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-26.3
- rgmanager: Exit more gracefully if cman stops first when cpg locks are used
  Resolves: rhbz#1344640

* Fri Jun 10 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-26.2
- rgmanager: Forget that we were transition master if quorum is dissolved
  rgmanager: Re-init the vf key callbacks after losing and recovering quorum
  Resolves: rhbz#bz1335412
- rgmanager: Check for NULL when attempting to access the member list
  Resolves: rhbz#bz1343345

* Fri May 13 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-26.1
- rgmanager: Reload the resource tree after quorum is regained
  if central processing is enabled.
  Resolves: rhbz#1335412

* Thu Mar 03 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-26
- rgmanager: Turn down log level on debug message
  Resolves: rhbz#1128877

* Thu Feb 04 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-25
- rgmanager: Fix bash syntax error in clunfslock
  rgmanager: clunfslock: copy state info if it exists
  Resolves: rhbz#1278943

* Wed Jan 20 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-24
- rgmanager: Log more errors during resource loading
  Resolves: rhbz#1128877

* Wed Jan 20 2016 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-23
- rgmanager: Don't relocate a service if policy should prevent it
  Resolves: rhbz#1197122

* Tue Mar 03 2015 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-22
- rgmanager: Fix potential NULL ptr deref in clustat
  Resolves: rhbz#1079207
- rgmanager: Log a warning when the non-critical flag is
  Resolves: rhbz#1128877
- rgmanager: Don't restart locally if failover domain
  Resolves: rhbz#1151199

* Mon Jun 23 2014 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-21
- rgmanager: Add an option to reboot on PID exhaustion
  Resolves: rhbz#982820

* Sun Jun 22 2014 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-20
- rgmanager: clusvcadm: If service doesn't exist, try
  Resolves: rhbz#952729
- rgmanager: Don't crash if a resource agent does not
  Resolves: rhbz#1018079
- rgmanager: Fix rg_test exit status on failures
  Resolves: rhbz#1033162
- rgmanager: resrules: make expand_time buffer-less
  Resolves: rhbz#1036652
- rgmanager: Fix error logging when building the resource
  Resolves: rhbz#1053739

* Wed Aug 14 2013 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-19
- rgmanager: Delay recovery when rgmanager dies unexpectedly
  Resolves: rhbz#862075

* Wed Jul 17 2013 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-18
- rgmanager: Fix potential unlocked memory access
  rgmanager: Fix for double pthread_mutex_unlock() calls
  rgmanager: Don't destroy locked mutexes
  rgmanager: Fix unlikely NULL ptr deref
  Resolves: rhbz#983296

* Tue Jan 08 2013 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-17
- Rebuild

* Tue Dec 11 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-16
- rgmanager: Update status after resource recovery
  Resolves: rhbz#879031

* Mon Oct 15 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-15
- rgmanager: Randomize node list when relocating with no
  Resolves: rhbz#831648
- rgmanager: Fix return code when a service would deadlock
  Resolves: rhbz#861157

* Fri Oct 12 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-14
- rgmanager: OCF_NOT_INSTALLED is OK if we stop when stopped
  Resolves: rhbz#853251

* Mon Oct 08 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-13
- rgmanager: Fix a crash when dbus notifications are
  Resolves: rhbz#825375
- rgmanager: Fix for deadlock
  Resolves: rhbz#861157

* Mon May 14 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-12
- cpglockd: Fix a hang triggered when fencing completes in less than 1s
  Resolves: rhbz#799505

* Fri May 04 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-11
- rgmanager: Fix dependent service handling during recovery
  Resolves: rhbz#807165

* Tue May 01 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-10
- rgmanager: Add simple locking over CPG
  Resolves: rhbz#799505

* Mon Apr 09 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-9
- rgmanager: Add CPG locking daemon for use when RRP mode is enabled

* Mon Apr 09 2012 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-8
- rgmanager: Fix a crash in find_master when central processing is enabled
  Resolves: rhbz#803474

* Thu Mar 01 2012 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-7
- rgmanager: Retry when config is out of sync
  Resolves: rhbz#796272

* Wed Feb 22 2012 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-6
- rgmanager: Resolve rare deadlock
  Resolves: rhbz#635152
- rgmanager: Fix clusvcadm message when run with -F
  Resolves: rhbz#727326
- rgmanager: Add extra service status call
  rgmanager: Avoid duplicate restart of service
  rgmanager: Fix call to service_status()
  rgmanager: Fix tiny memory leak in sl_service_status
  rgmanager: Fix dependency issue related to ordering
  Resolves: rhbz#743218
- rgmanager: Fix dependency restart bug in CP mode
  Resolves: rhbz#744824
- rgmanager: Add -F to clusvcadm man page
  Resolves: rhbz#745226

* Wed Oct 19 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-5
- rgmanager: Clean up DBus concurrency
  rgmanager: Block signals when dealing with dbus
  Resolves: rhbz#741607

* Thu Sep 08 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-4
- rgmanager: Fix segfault caused by unref race
  Resolves: rhbz#697446
- rgmanager: Fix uninitialized variable
  Resolves: rhbz#734730

* Tue Aug 02 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-3
- rgmanager: Fix race in shutdown vs. notification
  Resolves: rhbz#697446
- rgmanager: Add 'disabled' configuration option
  Resolves: rhbz#723925

* Wed Jul 13 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-2
- Improve rgmanager's exclusive prioritization handling
  Resolves: rhbz#690191
- Fix bad passing of SFL_FAILURE up
  Resolves: rhbz#716231
- Fix segfault on config reload
  Resolves: rhbz#692895
- Make handling of failed services consistent
  Resolves: rhbz#673167

* Tue Jun 21 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-1
- Rebase package on top of new upstream:
  * rgmanager: fix compiler warning in clulog.c
  * rgmanager: Add resource-defaults section
  * rgmanager: Fix clustat help & version operations
  * rgmanager: Make clustat -f not query CCS/objdb
  * rgmanager: Pause during exit if we stopped services
  * rgmanager: Fix reference count handling
- spec file update:
  * update spec file copyright date
  * drop all patches
  * update and clean configure and build section.
  * resync with fedora spec file
  Resolves: rhbz#707118
- Move rgmanager S/Lang from resource-agents to rgmanager:
  * Add versioned Requires/Obsoletes on resource-agents to avoid file conflicts
  Resolves: rhbz#693517

* Thu Feb 03 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12-11
- rgmanager: Present flags in clustat output
  (present_flags_in_clustat_output.patch)
  Resolves: rhbz#634298
- rgmanager: Fix clustat return code
  (fix_clustat_return_code.patch)
  Resolves: rhbz#621562
- rgmanager: Honor restricted FDs during migrations
  (honor_restricted_fds_during_migrations.patch)
  Resolves: rhbz#621694
- rgmanager: Add non-critical flag to resources
  (add_non_critical_flag_to_resources.patch)
  rgmanager: Add non-critical base behavior
  (add_non_critical_base_behavior.patch)
  rgmanager: Header cleanup
  (header_cleanup.patch)
  rgmanager: Use rg_strings.c for flags
  (use_rg_strings_c_for_flags.patch)
  rgmanager: Present all flags in clustat output
  (present_all_flags_in_clustat_output.patch)
  rgmanager: Mark non-critical resources disabled
  (mark_non_critical_resources_disabled.patch)
  rgmanager: Add convalesce operation
  (add_convalesce_operation.patch)
  rgmanager: Allow restart,disable recovery policy
  (allow_restart,disable_recovery_policy.patch)
  rgmanager: Ensure state is preserved across config changes
  (ensure_state_is_preserved_across_config_changes.patch)
  rgmanager: Fix handling of independent subtrees
  (fix_handling_of_independent_subtrees.patch)
  rgmanager: Do not fail service if non-critical resources fail to stop
  (do_not_fail_service_if_non_critical_resources_fail_to_stop.patch)
  rgmanager: Add -c option to man page & clusvcadm -h
  (add_c_option_to_man_page_clusvcadm_h.patch)
  rgmanager: Add independent subtree restart thresholds
  (add_independent_subtree_restart_thresholds.patch)
  rgmanager: clean up independent subtree restart handling
  (clean_up_independent_subtree_restart_handling.patch)
  rgmanager: Fix corner case in critical/non-critical handling
  (fix_corner_case_in_critical_non_critical_handling.patch)
  rgmanager: Support convalesce w/ central_processing
  (support_convalesce_w_central_processing.patch)
  Resolves: rhbz#634277
- rgmanager: Update last_owner on failover
  (update_last_owner_on_failover.patch)
  Resolves: rhbz#639103
- rgmanager: DBus notifications for service state changes
  (dbus_notifications_for_service_state_changes.patch)
  rgmanager: Clean up dbus notifications
  (clean_up_dbus_notifications.patch)
  rgmanager: Retry dbus if we get disconnected
  (retry_dbus_if_we_get_disconnected.patch)
  rgmanager: minor dbus cleanups
  (minor_dbus_cleanups.patch)
  rgmanager: Match fenced's option to disable DBus
  (match_fenced_s_option_to_disable_dbus.patch)
  rgmanager: allow dbus notification code to be disabled
  (allow_dbus_notification_code_to_be_disabled.patch)
  Resolves: rhbz#657756
- rgmanager: Make clufindhostname -i predictable
  (make_clufindhostname_i_predictable.patch)
  Resolves: rhbz#661881
- rgmanager: Fix nofailback when service is in 'starting' state
  (fix_nofailback_when_service_is_in_starting_state.patch)
  Resolves: rhbz#672841

* Mon Jul 12 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-10
- Add failover domain documentation and other improvements
  (man_page_improvements.patch)
  Resolves: rhbz#557563

* Mon Jul 12 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-9
- Make clulog filter correctly based on cluster.conf
  (make_clulog_filter_correctly.patch)
  Resolves: rhbz#609866

* Mon Jul 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-8
- Fix patch file naming
  Related: rhbz#612110

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-7
- Fix rgmanager init script to be more LSB compliant
  (rgmanager_init_lsb_compliant.patch)
  Resolves: rhbz#612110

* Wed Jun 30 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-6
- Fix staged upgrade
  (fix_staged_upgrade.patch)
  Resolves: rhbz#609550

* Wed Jun 30 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-5
- Fix 3.0.12-3 changelog

* Tue Jun 29 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-3
- Use sysrq-b to reboot
  (use_sysrq_b_to_reboot.patch)
  Resolves: rhbz#609181

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-2
- Pass timeouts to resource agents
  (pass_timeouts_to_resource_agents.patch)
  Resolves: rhbz#606480

* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- Rebase on top of new upstream bug fix only release:
  * drop all bug fix patches.
  * Addresses the follwing issues from 3.0.12 release:
  Resolves: rhbz#588890, rhbz#588925, rhbz#589131, rhbz#588010
  * Rebase:
  Resolves: rhbz#582350
- Stop build on ppc and ppc64.
  Resolves: rhbz#591000

* Wed Apr  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-2
- Fix 2+ simultaneous relocation crash
  (fix_2_or_more_simultaneous_relocation_crash.patch)
  Resolves: rhbz#577856
- Fix meory leaks during relocation
  (fix_memory_leaks_during_relocation.patch)
  (fix_memory_leak_during_reconfig.patch)
  Resolves: rhbz#578249

* Tue Mar  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- New upstream release
  Resolves: rhbz#569956, rhbz#569953
- spec file update:
  * update spec file copyright date
  * use bz2 tarball

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Resolves: rhbz#568011
- Do not build rgmanager on s390 and s390x.

* Tue Jan 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New upstream release

* Mon Dec  7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New upstream release
- spec file cleanup:
  * use global instead of define
  * use new Source0 url
  * use %name macro more aggressively

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New upstream release

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New upstream release

* Tue Sep  1 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- Split from cluster srpm
