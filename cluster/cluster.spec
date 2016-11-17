###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2012 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

# main (empty) package
# http://www.rpm.org/max-rpm/s1-rpm-subpack-spec-file-changes.html

# keep around ready for later user
## global alphatag rc4

Name: cluster
Summary: Red Hat Cluster
Version: 3.0.12.1
Release: 78%{?alphatag:.%{alphatag}}%{?dist}.0
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/cluster/wiki/
Source0: https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.bz2
Patch0: gfs2_reported_uuid_should_be_lowercase.patch
Patch1: gfs2_edit_savemeta_does_not_save_all_leaf_blocks_for_large_dirs.patch
Patch2: gfs2_grow_fix_growing_of_full_filesystem.patch
Patch3: dlm_controld_clear_waiting_plocks_for_closed_files.patch
Patch4: gfs2_fsck_segfault_in_pass1b.patch
Patch5: gfs2_edit_add_compression_to_savemeta_and_restoremeta.patch
Patch6: cman_tool_fix_typo_in_man_page.patch
Patch7: gfs2_edit_fix_savemeta_compression_for_older_zlibs.patch
Patch8: gfs2_fsck_only_rebuilds_one_missing_journal_at_a_time.patch
Patch9: cman_fix_ttl_default_if_no_value_is_specified.patch
Patch10: gfs2_add_tunegfs2.patch
Patch11: bz680930-1-ccs_add_dynamic_relaxng_schema_generation.patch
Patch12: bz680930-2-ccs_relax_requirements_on_fas_and_ras.patch
Patch13: bz680930-3-ccs_special_case_service_and_vm_relaxng.patch
Patch14: bz720668-gfs2_mkfs_handle_gfs2_creation_on_regular_files.patch
Patch15: bz706141-gfs2_mounts_doubled_up_in_mtab.patch
Patch16: bz719124-gfs2_tunegfs2_ensure_we_dont_try_to_open_a_null_device.patch
Patch17: bz719126-gfs2_tunegfs2_fix_usage_message.patch
Patch18: bz719135-gfs2_tunegfs2_fix_label_locktable_setting_code.patch
Patch19: bz723925-config_add_disabled_flag_to_rm_element.patch
Patch20: bz728230-1-cman_preconfig_fix_segfault_if_we_cannot_determine_cluster_name.patch
Patch21: bz728230-2-cman_preconfig_print_error_if_cluster_name_is_too_long.patch
Patch22: bz728230-3-cman_preconfig_fix_printing_if_cluster_name_is_too_long.patch
Patch23: bz726065-config-fix_escaping_of_xml_special_characters.patch
Patch24: bz695795-cman_fix_handling_of_transport_in_cman_totem_preconfig.patch
Patch25: bz695795-2-cman_fix_handling_of_transport_when_altname_is_specified.patch
Patch26: bz729071-gfs2_mount_fix_mounting_of_regular_files_with_-o_loop.patch
Patch27: bz731775-dlm_controld_fix_plock_dev_write_no_op.patch
Patch28: bz732635-cman_default_rrp_mode_should_be_passive.patch
Patch29: bz680930-4-ccs_fix_handling_of_tempdir.patch
Patch30: bz732991_dlm_controld_quiet_mkdir_eexist_message.patch
Patch31: bz733345_config_allow_cman_to_configure_uid_gid_for_corosync_ipc.patch
Patch32: bz733424_config_invalidate_ccs_update_schema_cache_on_errors.patch
Patch33: bz735906-cman_fix_multicast_address_in_cman_5_man_page.patch
Patch34: bz735912-cman_default_to_2_different_mcast_addresses_in_rrp_mode_and_set_rrp_problem_count_threshold.patch
Patch35: bz735917-cman_improve_cman_qdiskd_interactions.patch
Patch36: bz733345-2_config_fix_copying_uidgid_trees_to_corosync.patch
Patch37: bz739682_dlm_controld_fix_man_page_example_formatting.patch
Patch38: bz740385-cman_allow_late_close_of_stderr_file_descriptor_and_free_resources.patch
Patch39: bz663397-1-fenced_full_check_for_member_changes.patch
Patch40: bz663397-2-dlm_controld_full_check_for_member_changes.patch
Patch41: bz663397-3-gfs_controld_full_check_for_member_changes.patch
Patch42: bz675723-1-fsck.gfs2_Make_functions_use_sdp_rather_than_sbp.patch
Patch43: bz675723-2-fsck.gfs2_Change_if_to_if.patch
Patch44: bz675723-3-libgfs1_Add_gfs1_variable_to_superblock_structure.patch
Patch45: bz675723-4-libgfs2_Make_check_sb_and_read_sb_operate_on_gfs1.patch
Patch46: bz675723-5-libgfs2_move_gfs1_structures_to_libgfs2.patch
Patch47: bz675723-6-fsck.gfs2_Check_for_blocks_wrongly_inside_resource_groups.patch
Patch48: bz675723-7-fsck.gfs2_Rename_check_leaf_to_check_ealeaf_block.patch
Patch49: bz675723-8-fsck.gfs2_fsck.gfs2_Delete_vestigial_buffer_head_in_check_leaf.patch
Patch50: bz675723-9-fsck.gfs2_fsck.gfs2_Rename_nlink_functions_to_be_intuitive.patch
Patch51: bz675723-10-fsck.gfs2_fsck.gfs2_Sync_di_nlink_adding_links_for_lost_found.patch
Patch52: bz675723-11-fsck.gfs2_fsck.gfs2_Make_dir_entry_count_32_bits.patch
Patch53: bz675723-12-fsck.gfs2_get_rid_of_triple_negative_logic.patch
Patch54: bz675723-13-dirent_repair_needs_to_mark_the_buffer_as_modified.patch
Patch55: bz675723-14-fsck.gfs2_fsck.gfs2_Ask_to_reclaim_unlinked_meta_per_rgrp_only.patch
Patch56: bz675723-15-fsck.gfs2_fsck.gfs2_Refactor_add_dotdot_function_in_lost_found.patch
Patch57: bz675723-16-libgfs2_libgfs2_Use___FUNCTION___rather_than___FILE__.patch
Patch58: bz675723-17-fsck.gfs2_fsck.gfs2_Don_t_stop_invalidating_blocks_on_invalid.patch
Patch59: bz675723-18-fsck.gfs2_fsck.gfs2_Find_and_clear_duplicate_leaf_blocks_refs.patch
Patch60: bz675723-19-fsck.gfs2_fsck.gfs2_Move_check_num_ptrs_from_metawalk_to_pass1.patch
Patch61: bz675723-20-fsck.gfs2_fsck.gfs2_Duplicate_ref_processing_for_leaf_blocks.patch
Patch62: bz675723-21-fsck.gfs2_fsck.gfs2_split_check_leaf_blks_to_be_more_readable.patch
Patch63: bz675723-22-fsck.gfs2_Shorten_output.patch
Patch64: bz675723-23-fsck.gfs2_Make_output_messages_more_sensible.patch
Patch65: bz675723-24-fsck.gfs_pass2_Refactor_function_set_dotdot_dir.patch
Patch66: bz675723-25-fsck.gfs2_pass2_Delete_extended_attributes_with_inode.patch
Patch67: bz675723-26-fsck.gfs2_pass2_Don_t_delete_invalid_inode_metadata.patch
Patch68: bz675723-27-fsck.gfs2_pass3_Refactor_mark_and_return_parent.patch
Patch69: bz675723-28-fsck.gfs2_misc_cosmetic_changes.patch
Patch70: bz675723-29-fsck.gfs2_Don_t_use_old_leaf_if_it_was_a_duplicate.patch
Patch71: bz675723-30-fsck.gfs2_Add_find_remove_dup_free_block_if_notdup.patch
Patch72: bz675723-31-fsck.gfs2_don_t_free_prev_rgrp_list_repairing_rgrps.patch
Patch73: bz675723-32-libgfs2_eliminate_gfs1_readi_in_favor_of_gfs2_readi.patch
Patch74: bz675723-33-libgfs2_Mark_buffer_modified_adding_a_new_GFS1_block.patch
Patch75: bz675723-34-libgfs2_Use_dinode_buffer_to_map_gfs1_dinode_blocks.patch
Patch76: bz675723-35-libgfs2_move_block_map_functions_to_fsck.gfs2.patch
Patch77: bz675723-36-libgfs2_eliminate_gfs1_rindex_read.patch
Patch78: bz675723-37-libgfs2_combine_ri_update_and_gfs1_ri_update.patch
Patch79: bz675723-38-libgfs2_combine_gfs_inode_read_and_gfs_inode_get.patch
Patch80: bz675723-39-libgfs2_move_gfs1_functions_from_edit_to_libgfs2.patch
Patch81: bz675723-40-gfs2_edit_savemeta_save_inode_data_backward_for_gfs1.patch
Patch82: bz675723-41-libgfs2_expand_capabilities_to_operate_on_gfs1.patch
Patch83: bz675723-42-fsck.gfs2_Combine_block_and_char_device_inode_types.patch
Patch84: bz675723-43-fsck.gfs2_four_step_duplicate_elimination_process.patch
Patch85: bz675723-44-fsck.gfs2_Add_ability_to_check_gfs1_file_systems.patch
Patch86: bz675723-45-fsck.gfs2_Remove_bad_inodes_from_duplicate_tree.patch
Patch87: bz675723-46-fsck.gfs2_Handle_duplicate_reference_to_dinode_blocks.patch
Patch88: bz675723-47-fsck.gfs2_Bad_extended_attributes_not_deleted_properly.patch
Patch89: bz675723-48-libgfs2_Make_rebuild_functions_not_re_read_ip.patch
Patch90: bz675723-49-fsck.gfs2_Shorten_debug_output.patch
Patch91: bz675723-50-fsck.gfs2_Increment_link_count_reporting_wrong_dinode.patch
Patch92: bz675723-51-fsck.gfs2_system_dinodes_take_priority_over_user.patch
Patch93: bz675723-52-fsck.gfs2_Recognize_partially_gfs2_converted_dinodes.patch
Patch94: bz675723-53-fsck.gfs2_Print_step_2_duplicate_debug_msg_first.patch
Patch95: bz675723-54-fsck.gfs2_pass1c_counts_percentage_backward.patch
Patch96: bz675723-55-fsck.gfs2_Speed_up_rangecheck_functions.patch
Patch97: bz675723-56-libgfs2_Make_in_core_rgrps_use_rbtree.patch
Patch98: bz675723-57-fsck.gfs2_Fix_memory_leaks.patch
Patch99: bz675723-58-Change_man_pages_and_gfs2_convert_messages_to_include_GFS.patch
Patch100: bz675723-59-gfs2_edit_Fix_memory_leaks.patch
Patch101: bz675723-60-fsck.gfs2_Journals_not_properly_checked.patch
Patch102: bz675723-61-fsck.gfs2_Rearrange_block_types_to_group_all_inode_types.patch
Patch103: bz675723-62-fsck.gfs2_Fix_initialization_error_return_codes.patch
Patch104: bz675723-63-fsck.gfs2_Don_t_use_strerror_for_libgfs2_errors.patch
Patch105: bz675723-64-fsck.gfs2_Fix_memory_leak_in_initialize.c.patch
Patch106: bz675723-65-fsck.gfs2_Add_return_code_checks_and_initializations.patch
Patch107: bz675723-66-libgfs2_Fix_null_pointer_dereference_in_linked_leaf_search.patch
Patch108: bz745161-libgfs2_Dont_count_sentinel_dirent_as_an_entry.patch
Patch109: bz769400-mkfs.gfs2_Improve_error_messages.patch
Patch110: bz753300-gfs_controld_dont_ignore_dlmc_fs_register_error.patch
Patch111: bz749864-gfs2_edit_savemeta_get_rid_of_slow_mode.patch
Patch112: bz749864-gfs2_edit_savemeta_report_save_statistics_more_often.patch
Patch113: bz749864-gfs2_edit_savemeta_fix_block_range_checking.patch
Patch114: bz749864-gfs2_edit_restoremeta_sync_changes_on_a_regular_basis.patch
Patch115: bz742595-gfs2_utils_gfs2_grow_fails_to_grow_a_filesystem_with_less_than_3_RGs.patch
Patch116: bz742293-gfs2_utils_Improve_error_messages.patch
Patch117: bz745538-qdisk-5-ping-example-missing-w.patch
Patch118: bz740552-config-make-altname-validation-position-indipendent.patch
Patch119: bz733298-config-drastically-improve-cman-rrp-configuration.patch
Patch120: bz759603-cman-improve-quorum-timer-handling.patch
Patch121: bz678372-1-qdiskd-make-multipath-issues-go-away.patch
Patch122: bz678372-2-allocate-port-in-cnxman-socket-for-qdiskd.patch
Patch123: bz678372-3-qdisk-small-tiny-little-cleanup.patch
Patch124: bz750314-fenced_fix_handling_of_startup_partition_merge.patch
Patch125: bz750314-2-dlm_controld_fix_handling_of_startup_partition_merge.patch
Patch126: bz803510-fsck.gfs2_fix_handling_of_eattr_indirect_blocks.patch
Patch127: bz804938-config_update_relax_ng_schema_to_include_totem_miss_count_const.patch
Patch128: bz806002-cman_init_fix_start_sequence_error_handling.patch
Patch129: bz808441-man_update_fenced_8_to_reflect_limitation_xml_dtd_validation.patch
Patch130: bz745538-2-qdisk-5-ping-example-missing-w.patch
Patch131: bz819787_cman_notifyd_deliver_cluster_status_on_startup.patch
Patch132: bz814807_qdiskd_allow_master_to_failover_quickly_when_using_master_wins.patch
Patch133: bz785866_config_fix_type_in_schema.patch
Patch134: bz786118_cman_preconfig_allow_host_aliases_as_valid_cluster_nodenames.patch
Patch135: bz839241-1-cman_fix_data_copy_and_memory_leak_when_reloading_config.patch
Patch136: bz839241-2-cman_fix_data_copy_and_memory_leak_when_reloading_config.patch
Patch137: bz821016-1-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld.patch
Patch138: bz821016-2-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld.patch
Patch139: bz821016-3-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld.patch
Patch140: bz842370_cman_init_allow_dlm_hash_table_sizes_to_be_tunable_at_startup.patch
Patch141: bz838047_qdiskd_restrict_master_wins_mode_to_2_node_cluster.patch
Patch142: bz845341_fenced_fix_log_file_mode.patch
Patch143: bz838945-fsck.gfs2_fix_buffer_overflow_in_get_lockproto_table.patch
Patch144: bz847234-1-use_new_corosync_confdb_api_to_remove_string_limit.patch
Patch145: bz847234-2-ccs_do_not_truncate_lists.patch
Patch146: bz853180-gfs_controld_fenced_fix_ignore_nolock_for_mounted_nolock_fs.patch
Patch147: bz797952-1-fence_node_libfence_status.patch
Patch148: bz797952-2-fenced_fence_check_delay.patch
Patch149: bz797952-3-fence_check_add_script_and_man_page.patch
Patch150: bz857299-cman_init_allow_dlm_tcp_port_to_be_configurable_via_cman_init_script.patch
Patch151: bz854032-cman_init_increase_default_shutdown_timeouts.patch
Patch152: bz803477-fsck.gfs2_soften_the_messages_when_reclaiming_freemeta_blocks.patch
Patch153: bz861340-fenced_silence_dbus_error.patch
Patch154: bz509056-1_cman_init_make_sure_we_start_after_fence_sanlockd.patch
Patch155: bz509056-2_checkquorum.wdmd_add_integration_script_with_wdmd.patch
Patch156: bz862847-mkfs.gfs2_check_locktable_more_strictly_for_valid_chars.patch
Patch157: bz857952-fenced_get_the_cman_fd_before_each_poll.patch
Patch158: bz860048-fsck.gfs2_check_for_formal_inode_number_mismatch.patch
Patch159: bz887787_cman_prevent_libcman_from_causing_sigpipe_when_corosync_is_down.patch
Patch160: bz888053-1-gfs2_convert-mark-rgrp-bitmaps-dirty-when-converting.patch
Patch161: bz888053-2-gfs2_convert-mark-buffer-dirty-when-switching-dirs-f.patch
Patch162: bz888053-3-gfs2_convert-remember-number-of-blocks-when-converti.patch
Patch163: bz888053-4-gfs2_convert-Use-proper-header-size-when-reordering-.patch
Patch164: bz888053-5-gfs2_convert-calculate-height-1-for-small-files-that.patch
Patch165: bz888053-6-gfs2_convert-clear-out-old-di_mode-before-setting-it.patch
Patch166: bz888053-7-gfs2_convert-mask-out-proper-bits-when-identifying-s.patch
Patch167: bz888053-8-fsck.gfs2-Detect-and-fix-mismatch-in-GFS1-formal-ino.patch
Patch168: bz509056-3_build_ship_checkquorum.wdmd_non_executable.patch
Patch169: bz886585-gfs2_grow_report_bad_return_codes_on_error.patch
Patch170: bz902920-01-libgfs2_Add_readahead_for_rgrp_headers.patch
Patch171: bz902920-02-fsck_Speed_up_reading_of_dir_leaf_blocks.patch
Patch172: bz902920-03-libgfs2_externalize_dir_split_leaf.patch
Patch173: bz902920-04-libgfs2_allow_dir_split_leaf_to_receive_a_leaf_buffer.patch
Patch174: bz902920-05-libgfs2_let_dir_split_leaf_receive_a__broken__lindex.patch
Patch175: bz902920-06-fsck.gfs2_Move_function_find_free_blk_to_util.c.patch
Patch176: bz902920-07-fsck.gfs2_Split_out_function_to_make_sure_lost_found_exists.patch
Patch177: bz902920-08-fsck.gfs2_Check_for_formal_inode_mismatch_when_adding_to_lost_found.patch
Patch178: bz902920-09-fsck.gfs2_shorten_some_debug_messages_in_lost_found.patch
Patch179: bz902920-10-fsck.gfs2_Move_basic_directory_entry_checks_to_separate_function.patch
Patch180: bz902920-11-fsck.gfs2_Add_formal_inode_check_to_basic_dirent_checks.patch
Patch181: bz902920-12-fsck.gfs2_Add_new_function_to_check_dir_hash_tables.patch
Patch182: bz902920-13-fsck.gfs2_Special_case__..__when_processing_bad_formal_inode_number.patch
Patch183: bz902920-14-fsck.gfs2_Move_function_to_read_directory_hash_table_to_util.c.patch
Patch184: bz902920-15-fsck.gfs2_Misc_cleanups_from_upstream.patch
Patch185: bz902920-16-fsck.gfs2_Verify_dirent_hash_values_correspond_to_proper_leaf_block.patch
Patch186: bz902920-17-fsck.gfs2_re
Patch187: bz902920-18-fsck.gfs2_fix_leaf_blocks,_don_t_try_to_patch_the_hash_table.patch
Patch188: bz902920-19-fsck.gfs2_check_leaf_depth_when_validating_leaf_blocks.patch
Patch189: bz902920-20-fsck.gfs2_small_cleanups.patch
Patch190: bz902920-21-fsck.gfs2_reprocess_inodes_when_blocks_are_added.patch
Patch191: bz902920-22-fsck.gfs2_Remove_redundant_leaf_depth_check.patch
Patch192: bz902920-23-fsck.gfs2_link_dinodes_that_only_have_extended_attribute_problems.patch
Patch193: bz902920-24-fsck.gfs2_Add_clarifying_message_to_duplicate_processing.patch
Patch194: bz902920-25-fsck.gfs2_separate_function_to_calculate_metadata_block_header_size.patch
Patch195: bz902920-26-fsck.gfs2_Rework_the__undo__functions.patch
Patch196: bz902920-27-fsck.gfs2_Check_for_interrupt_when_resolving_duplicates.patch
Patch197: bz902920-28-fsck.gfs2_Consistent_naming_of_struct_duptree_variables.patch
Patch198: bz902920-29-fsck.gfs2_Keep_proper_counts_when_duplicates_are_found.patch
Patch199: bz902920-30-fsck.gfs2_print_metadata_block_reference_on_data_errors.patch
Patch200: bz902920-31-fsck.gfs2_print_block_count_values_when_fixing_them.patch
Patch201: bz902920-32-fsck.gfs2_Do_not_invalidate_metablocks_of_dinodes_with_invalid_mode.patch
Patch202: bz902920-33-fsck.gfs2_Log_when_unrecoverable_data_block_errors_are_encountered.patch
Patch203: bz902920-34-fsck.gfs2_don_t_remove_buffers_from_the_list_when_errors_are_found.patch
Patch204: bz902920-35-fsck.gfs2_Don_t_flag_GFS1_non
Patch205: bz902920-36-fsck.gfs2_externalize_check_leaf.patch
Patch206: bz902920-37-fsck.gfs2_pass2_check_leaf_blocks_when_fixing_hash_table.patch
Patch207: bz902920-38-fsck.gfs2_standardize_check_metatree_return_codes.patch
Patch208: bz902920-39-fsck.gfs2_don_t_invalidate_files_with_duplicate_data_block_refs.patch
Patch209: bz902920-40-fsck.gfs2_check_for_duplicate_first_references.patch
Patch210: bz902920-41-fsck.gfs2_When_flagging_a_duplicate_reference,_show_valid_or_invalid.patch
Patch211: bz902920-42-fsck.gfs2_major_duplicate_reference_reform.patch
Patch212: bz902920-43-fsck.gfs2_Remove_all_bad_eattr_blocks.patch
Patch213: bz902920-44-fsck.gfs2_Remove_unused_variable.patch
Patch214: bz902920-45-fsck.gfs2_double
Patch215: bz902920-46-fsck.gfs2_Trivial_typo_fix.patch
Patch216: bz902920-47-fsck.gfs2_Stop__undo__process_when_error_data_block_is_reached.patch
Patch217: bz902920-48-fsck.gfs2_Don_t_allocate_leaf_blocks_in_pass1.patch
Patch218: bz902920-49-fsck.gfs2_take_hash_table_start_boundaries_into_account.patch
Patch219: bz902920-50-fsck.gfs2_delete_all_duplicates_from_unrecoverable_damaged_dinodes.patch
Patch220: bz963657-init.d_gfs2_work_around_nested_mount_points_umount_bug.patch
Patch221: bz984085-1-fsck.gfs2_fix_some_log_messages.patch
Patch222: bz984085-2-fsck.gfs2_Fix_directory_link_on_relocated_directory_dirents.patch
Patch223: bz984085-3-fsck.gfs2_Fix_infinite_loop_in_pass1b_caused_by_duplicates_in_hash_table.patch
Patch224: bz984085-4-fsck.gfs2_don_t_check_newly_created_lost+found_in_pass2.patch
Patch225: bz984085-5-fsck.gfs2_avoid_negative_number_in_leaf_depth.patch
Patch226: bz984085-6-fsck.gfs2_Detect_and_fix_duplicate_references_in_hash_tables.patch
Patch227: bz985796-fsck.gfs2_Dont_rely_on_cluster_conf_when_rebuilding_sb.patch
Patch228: bz871603-ccs_tool_fix_example_fence_device_help.patch
Patch229: bz874538-libccs_dont_use_unitialized_value_in_xpathlite.patch
Patch230: bz888318-qdiskd_change_log_level_for_token_error_message.patch
Patch231: bz893925-1-cman_fenced_fix_killing_on_2node_cluster_suffering_brief_outage.patch
Patch232: bz893925-2-cman_fenced_fix_killing_on_2node_cluster_suffering_brief_outage.patch
Patch233: bz896191-config_fix_cluster_conf_man_page_logging_default.patch
Patch234: bz920358-qdiskd_do_not_count_missed_updates_from_offline_nodes.patch
Patch235: bz982670-cman_create_destroy_lockfile_on_restart_etc.patch
Patch236: bz889564-gfs_controld_avoid_mismatching_messages_with_old-cgs.patch
Patch237: bz888857-fenced_dlm_controld_gfs_controld_use_cluster_dead_for_corosync_connections.patch
Patch238: bz987508-1-libgfs2_Fix_pointer_arithmetic_in_gfs2_quota_change.patch
Patch239: bz987508-2-gfs2_edit_fix_a_segfault_with_file_names_255_bytes.patch
Patch240: bz987508-3-gfs2_edit_Clean_up_some_magic_offsets.patch
Patch241: bz987508-4-gfs2_edit_display_pointer_offsets_for_directory_dinodes.patch
Patch242: bz987508-5-gfs2_edit_Add_new_option_to_print_all_bitmaps_for_an_rgrp.patch
Patch243: bz987508-6-gfs2_edit_print_formal_inode_numbers_and_hash_value_on_dir_display.patch
Patch244: bz989647-fsck_gfs2_Add_ability_to_detect_journal_inode_indirect_block_corruption.patch
Patch245: bz996233-1-gfs2_tool_Update_etc_mtab_with_metafs_mounts_handle_interrupts.patch
Patch246: bz996233-2-libgfs2_check_return_code_of_rename.patch
Patch247: bz996233-3-libgfs2_Correct_error_message_in_mtab_update_code.patch
Patch248: bz996233-4-libgfs2_Set_umask_before_calling_mkstemp.patch
Patch249: bz1007970-mkfs_gfs2_Add_missing_K_option.patch
Patch250: bz1059269-fenced_keep_manual_fifo_open.patch
Patch251: bz1059853-libgfs2_Fix_up_remove_mtab_entry.patch
Patch252: bz1062742-fsck_gfs2_Check_and_repair_per_node_contents_such_as_quota_changeX.patch
Patch253: bz1053668-1-libgfs2_patch_to_update_gfs1_superblock_correctly.patch
Patch254: bz1053668-2-gfs2_utils_check_and_fix_bad_dinode_pointers_in_gfs1_sb.patch
Patch255: bz1081517-fsck_gfs2_Log_to_syslog_on_start_and_exit.patch
Patch256: bz1081523-1-gfs2_edit_Add_a_savemeta_file_metadata_header.patch
Patch257: bz1081523-2-gfs2_edit_Fix_loop_arithmetic_in_restore_data.patch
Patch258: bz1081523-3-gfs2_edit_Ensure_all_leaf_blocks_in_per_node_are_saved.patch
Patch259: bz1081523-4-gfs2_edit_Reinstate_a_check_for_system_dinodes.patch
Patch260: bz979313-qdisk_check_cman_wait_return.patch
Patch261: bz980575-libccs_read_logging_attributes_correctly.patch
Patch262: bz1029210-qdisk_quorum_init_complete_after_tko_up_cycles.patch
Patch263: bz1035929-config_fix_typos_and_phrasing_in_defaults_file.patch
Patch264: bz1074551-ccs_tool_fix_crash_using_verbose.patch
Patch265: bz981043-man_mention_cluster_conf_html_schema_in_man_page.patch
Patch266: bz994234-fenced_remove_mention_of_skip_undefined_feature.patch
Patch267: bz981043-doc_update_cluster_conf_html.patch
Patch268: bz1080174-mount_gfs2_Don_t_leave_mount_group_if_mount_returns_EBUSY.patch
Patch269: bz843160-dlm_controld_Adjust_fence_time_comparison.patch
Patch270: bz886016-man_update_fence_node_options.patch
Patch271: bz982305-1-fenced_wait_for_ringid.patch
Patch272: bz982305-2-gfs_controld_Fix_first_recovery_case.patch
Patch273: bz982305-3-gfs_controld_Fix_first_recovery_case2.patch
Patch274: bz982820-rgmanager_add_reboot_on_pid_exhaustion_attr.patch
Patch275: bz1149516-1-fsck_gfs2_fix_broken_i_goal_values_in_inodes.patch
Patch276: bz1149516-2-gfs2_convert_use_correct_i_goal_values_instead_of_zeros_for_inodes.patch
Patch277: bz1149516-3-fsck_gfs2_Reprocess_nodes_if_anything_changed_addendum_1_of_2.patch
Patch278: bz1149516-4-fsck_gfs2_addendum_to_fix_broken_i_goal_values_in_inodes_addendum_2_of_2.patch
Patch279: bz1121693-libgfs2_Use_a_matching_context_mount_option_in_mount_gfs2_meta.patch
Patch280: bz1133724-logt_fix_race_when_reopening_logfiles.patch
Patch281: bz1087286-xml-ccs_update_schema-be-verbose-about-extraction-fa.patch
Patch282: bz1095418-qdiskd_heuristics_needed_for_3nodes_or_more.patch
Patch283: bz1095657-daemons_better_logging_if_receive_start_fails.patch
Patch284: bz1099223-qdisk_enable_master_wins_if_votes_1.patch
Patch285: bz1111500-cman_fix_manpage_altname_text.patch
Patch286: bz1142947-cman_fix_message_for_non-2node_clusters.patch
Patch287: bz1121693-libgfs2_Make_sure_secontext_gets_freed.patch
Patch288: bz1233535-dlm_controld_retry_uevent_on_error.patch
Patch289: bz1234443-gfs_controld_retry_uevent_on_error.patch
Patch290: bz1238754-fsck_gfs2_replace_recent_i_goal_fixes_with_simple_logic.patch
Patch291: bz1206149-1-fsck_gfs2_Change_duptree_structure_to_have_generic_flags.patch
Patch292: bz1206149-2-fsck_gfs2_Detect_fix_and_clone_duplicate_block_refs_within_a_dinode.patch
Patch293: bz1077890-fenced_delay_kill_due_to_stateful_merge.patch
Patch294: bz1171241-libcman_dont_segv_if_dev_zero_doesnt_exist.patch
Patch295: bz1193169-cman_improve_node_name_matching.patch
Patch296: bz1206188-cman_delete_tempfile_if_ccs_validate_fails.patch
Patch297: bz1243944-gfs_show_more_than_128_fs.patch
Patch298: bz1245232-qdiskd_fix_leak_in_unaligned_write.patch
Patch299: bz1245232-qdiskd_fix_memcpy_in_unaligned_write.patch
Patch300: bz1257732-qdiskd_watch_for_other_nodes_leaving_during_master_election.patch
Patch301: bz1252991-fenced_remove_fencedevice_attributes_from_-S.patch
Patch302: bz1221728-schema_add_rrp_attributes.patch
Patch303: bz1297165-proper_vote_check.patch
Patch304: bz1202817-gfs2_utils_Add_the_glocktop_utility.patch


## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: perl python
BuildRequires: glibc-kernheaders glibc-devel
BuildRequires: libxml2-devel ncurses-devel
BuildRequires: corosynclib-devel >= 1.4.1-9
BuildRequires: openaislib-devel >= 1.1.1-1
# BuildRequires: openldap-devel perl(ExtUtils::MakeMaker)
BuildRequires: dbus-devel zlib-devel

ExclusiveArch: i686 x86_64 %{arm}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .gfs2_reported_uuid_should_be_lowercase
%patch1 -p1 -b .gfs2_edit_savemeta_does_not_save_all_leaf_blocks_for_large_dirs
%patch2 -p1 -b .gfs2_grow_fix_growing_of_full_filesystem
%patch3 -p1 -b .dlm_controld_clear_waiting_plocks_for_closed_files
%patch4 -p1 -b .gfs2_fsck_segfault_in_pass1b
%patch5 -p1 -b .gfs2_edit_add_compression_to_savemeta_and_restoremeta
%patch6 -p1 -b .cman_tool_fix_typo_in_man_page
%patch7 -p1 -b .gfs2_edit_fix_savemeta_compression_for_older_zlibs
%patch8 -p1 -b .gfs2_fsck_only_rebuilds_one_missing_journal_at_a_time
%patch9 -p1 -b .cman_fix_ttl_default_if_no_value_is_specified
%patch10 -p1 -b .gfs2_add_tunegfs2
%patch11 -p1 -b .bz680930-1-ccs_add_dynamic_relaxng_schema_generation
%patch12 -p1 -b .bz680930-2-ccs_relax_requirements_on_fas_and_ras
%patch13 -p1 -b .bz680930-3-ccs_special_case_service_and_vm_relaxng
%patch14 -p1 -b .bz720668-gfs2_mkfs_handle_gfs2_creation_on_regular_files
%patch15 -p1 -b .bz706141-gfs2_mounts_doubled_up_in_mtab
%patch16 -p1 -b .bz719124-gfs2_tunegfs2_ensure_we_dont_try_to_open_a_null_device
%patch17 -p1 -b .bz719126-gfs2_tunegfs2_fix_usage_message
%patch18 -p1 -b .bz719135-gfs2_tunegfs2_fix_label_locktable_setting_code
%patch19 -p1 -b .bz723925.1
%patch20 -p1 -b .bz728230-1-cman_preconfig_fix_segfault_if_we_cannot_determine_cluster_name
%patch21 -p1 -b .bz728230-2-cman_preconfig_print_error_if_cluster_name_is_too_long
%patch22 -p1 -b .bz728230-3-cman_preconfig_fix_printing_if_cluster_name_is_too_long
%patch23 -p1 -b .bz726065-config-fix_escaping_of_xml_special_characters
%patch24 -p1 -b .bz695795-cman_fix_handling_of_transport_in_cman_totem_preconfig
%patch25 -p1 -b .bz695795-2-cman_fix_handling_of_transport_when_altname_is_specified
%patch26 -p1 -b .bz729071-gfs2_mount_fix_mounting_of_regular_files_with_-o_loop
%patch27 -p1 -b .bz731775-dlm_controld_fix_plock_dev_write_no_op
%patch28 -p1 -b .bz732635-cman_default_rrp_mode_should_be_passive
%patch29 -p1 -b .bz680930-4-ccs_fix_handling_of_tempdir
%patch30 -p1 -b .bz732991_dlm_controld_quiet_mkdir_eexist_message
%patch31 -p1 -b .bz733345_config_allow_cman_to_configure_uid_gid_for_corosync_ipc
%patch32 -p1 -b .bz733424_config_invalidate_ccs_update_schema_cache_on_errors
%patch33 -p1 -b .bz735906-cman_fix_multicast_address_in_cman_5_man_page
%patch34 -p1 -b .bz735912-cman_default_to_2_different_mcast_addresses_in_rrp_mode_and_set_rrp_problem_count_threshold
%patch35 -p1 -b .bz735917-cman_improve_cman_qdiskd_interactions
%patch36 -p1 -b .bz733345-2_config_fix_copying_uidgid_trees_to_corosync
%patch37 -p1 -b .bz739682_dlm_controld_fix_man_page_example_formatting
%patch38 -p1 -b .bz740385-cman_allow_late_close_of_stderr_file_descriptor_and_free_resources
%patch39 -p1 -b .bz663397-1-fenced_full_check_for_member_changes
%patch40 -p1 -b .bz663397-2-dlm_controld_full_check_for_member_changes
%patch41 -p1 -b .bz663397-3-gfs_controld_full_check_for_member_changes
%patch42 -p1 -b .bz675723-1-fsck.gfs2_Make_functions_use_sdp_rather_than_sbp
%patch43 -p1 -b .bz675723-2-fsck.gfs2_Change_if_to_if
%patch44 -p1 -b .bz675723-3-libgfs1_Add_gfs1_variable_to_superblock_structure
%patch45 -p1 -b .bz675723-4-libgfs2_Make_check_sb_and_read_sb_operate_on_gfs1
%patch46 -p1 -b .bz675723-5-libgfs2_move_gfs1_structures_to_libgfs2
%patch47 -p1 -b .bz675723-6-fsck.gfs2_Check_for_blocks_wrongly_inside_resource_groups
%patch48 -p1 -b .bz675723-7-fsck.gfs2_Rename_check_leaf_to_check_ealeaf_block
%patch49 -p1 -b .bz675723-8-fsck.gfs2_fsck.gfs2_Delete_vestigial_buffer_head_in_check_leaf
%patch50 -p1 -b .bz675723-9-fsck.gfs2_fsck.gfs2_Rename_nlink_functions_to_be_intuitive
%patch51 -p1 -b .bz675723-10-fsck.gfs2_fsck.gfs2_Sync_di_nlink_adding_links_for_lost_found
%patch52 -p1 -b .bz675723-11-fsck.gfs2_fsck.gfs2_Make_dir_entry_count_32_bits
%patch53 -p1 -b .bz675723-12-fsck.gfs2_get_rid_of_triple_negative_logic
%patch54 -p1 -b .bz675723-13-dirent_repair_needs_to_mark_the_buffer_as_modified
%patch55 -p1 -b .bz675723-14-fsck.gfs2_fsck.gfs2_Ask_to_reclaim_unlinked_meta_per_rgrp_only
%patch56 -p1 -b .bz675723-15-fsck.gfs2_fsck.gfs2_Refactor_add_dotdot_function_in_lost_found
%patch57 -p1 -b .bz675723-16-libgfs2_libgfs2_Use___FUNCTION___rather_than___FILE__
%patch58 -p1 -b .bz675723-17-fsck.gfs2_fsck.gfs2_Don_t_stop_invalidating_blocks_on_invalid
%patch59 -p1 -b .bz675723-18-fsck.gfs2_fsck.gfs2_Find_and_clear_duplicate_leaf_blocks_refs
%patch60 -p1 -b .bz675723-19-fsck.gfs2_fsck.gfs2_Move_check_num_ptrs_from_metawalk_to_pass1
%patch61 -p1 -b .bz675723-20-fsck.gfs2_fsck.gfs2_Duplicate_ref_processing_for_leaf_blocks
%patch62 -p1 -b .bz675723-21-fsck.gfs2_fsck.gfs2_split_check_leaf_blks_to_be_more_readable
%patch63 -p1 -b .bz675723-22-fsck.gfs2_Shorten_output
%patch64 -p1 -b .bz675723-23-fsck.gfs2_Make_output_messages_more_sensible
%patch65 -p1 -b .bz675723-24-fsck.gfs_pass2_Refactor_function_set_dotdot_dir
%patch66 -p1 -b .bz675723-25-fsck.gfs2_pass2_Delete_extended_attributes_with_inode
%patch67 -p1 -b .bz675723-26-fsck.gfs2_pass2_Don_t_delete_invalid_inode_metadata
%patch68 -p1 -b .bz675723-27-fsck.gfs2_pass3_Refactor_mark_and_return_parent
%patch69 -p1 -b .bz675723-28-fsck.gfs2_misc_cosmetic_changes
%patch70 -p1 -b .bz675723-29-fsck.gfs2_Don_t_use_old_leaf_if_it_was_a_duplicate
%patch71 -p1 -b .bz675723-30-fsck.gfs2_Add_find_remove_dup_free_block_if_notdup
%patch72 -p1 -b .bz675723-31-fsck.gfs2_don_t_free_prev_rgrp_list_repairing_rgrps
%patch73 -p1 -b .bz675723-32-libgfs2_eliminate_gfs1_readi_in_favor_of_gfs2_readi
%patch74 -p1 -b .bz675723-33-libgfs2_Mark_buffer_modified_adding_a_new_GFS1_block
%patch75 -p1 -b .bz675723-34-libgfs2_Use_dinode_buffer_to_map_gfs1_dinode_blocks
%patch76 -p1 -b .bz675723-35-libgfs2_move_block_map_functions_to_fsck.gfs2
%patch77 -p1 -b .bz675723-36-libgfs2_eliminate_gfs1_rindex_read
%patch78 -p1 -b .bz675723-37-libgfs2_combine_ri_update_and_gfs1_ri_update
%patch79 -p1 -b .bz675723-38-libgfs2_combine_gfs_inode_read_and_gfs_inode_get
%patch80 -p1 -b .bz675723-39-libgfs2_move_gfs1_functions_from_edit_to_libgfs2
%patch81 -p1 -b .bz675723-40-gfs2_edit_savemeta_save_inode_data_backward_for_gfs1
%patch82 -p1 -b .bz675723-41-libgfs2_expand_capabilities_to_operate_on_gfs1
%patch83 -p1 -b .bz675723-42-fsck.gfs2_Combine_block_and_char_device_inode_types
%patch84 -p1 -b .bz675723-43-fsck.gfs2_four_step_duplicate_elimination_process
%patch85 -p1 -b .bz675723-44-fsck.gfs2_Add_ability_to_check_gfs1_file_systems
%patch86 -p1 -b .bz675723-45-fsck.gfs2_Remove_bad_inodes_from_duplicate_tree
%patch87 -p1 -b .bz675723-46-fsck.gfs2_Handle_duplicate_reference_to_dinode_blocks
%patch88 -p1 -b .bz675723-47-fsck.gfs2_Bad_extended_attributes_not_deleted_properly
%patch89 -p1 -b .bz675723-48-libgfs2_Make_rebuild_functions_not_re_read_ip
%patch90 -p1 -b .bz675723-49-fsck.gfs2_Shorten_debug_output
%patch91 -p1 -b .bz675723-50-fsck.gfs2_Increment_link_count_reporting_wrong_dinode
%patch92 -p1 -b .bz675723-51-fsck.gfs2_system_dinodes_take_priority_over_user
%patch93 -p1 -b .bz675723-52-fsck.gfs2_Recognize_partially_gfs2_converted_dinodes
%patch94 -p1 -b .bz675723-53-fsck.gfs2_Print_step_2_duplicate_debug_msg_first
%patch95 -p1 -b .bz675723-54-fsck.gfs2_pass1c_counts_percentage_backward
%patch96 -p1 -b .bz675723-55-fsck.gfs2_Speed_up_rangecheck_functions
%patch97 -p1 -b .bz675723-56-libgfs2_Make_in_core_rgrps_use_rbtree
%patch98 -p1 -b .bz675723-57-fsck.gfs2_Fix_memory_leaks
%patch99 -p1 -b .bz675723-58-Change_man_pages_and_gfs2_convert_messages_to_include_GFS
%patch100 -p1 -b .bz675723-59-gfs2_edit_Fix_memory_leaks
%patch101 -p1 -b .bz675723-60-fsck.gfs2_Journals_not_properly_checked
%patch102 -p1 -b .bz675723-61-fsck.gfs2_Rearrange_block_types_to_group_all_inode_types
%patch103 -p1 -b .bz675723-62-fsck.gfs2_Fix_initialization_error_return_codes
%patch104 -p1 -b .bz675723-63-fsck.gfs2_Don_t_use_strerror_for_libgfs2_errors
%patch105 -p1 -b .bz675723-64-fsck.gfs2_Fix_memory_leak_in_initialize.c
%patch106 -p1 -b .bz675723-65-fsck.gfs2_Add_return_code_checks_and_initializations
%patch107 -p1 -b .bz675723-66-libgfs2_Fix_null_pointer_dereference_in_linked_leaf_search
%patch108 -p1 -b .bz745161-libgfs2_Dont_count_sentinel_dirent_as_an_entry
%patch109 -p1 -b .bz769400-mkfs.gfs2_Improve_error_messages
%patch110 -p1 -b .bz753300-gfs_controld_dont_ignore_dlmc_fs_register_error
%patch111 -p1 -b .bz749864-gfs2_edit_savemeta_get_rid_of_slow_mode
%patch112 -p1 -b .bz749864-gfs2_edit_savemeta_report_save_statistics_more_often
%patch113 -p1 -b .bz749864-gfs2_edit_savemeta_fix_block_range_checking
%patch114 -p1 -b .bz749864-gfs2_edit_restoremeta_sync_changes_on_a_regular_basis
%patch115 -p1 -b .bz742595-gfs2_utils_gfs2_grow_fails_to_grow_a_filesystem_with_less_than_3_RGs
%patch116 -p1 -b .bz742293-gfs2_utils_Improve_error_messages
%patch117 -p1 -b .bz745538-qdisk-5-ping-example-missing-w
%patch118 -p1 -b .bz740552-config-make-altname-validation-position-indipendent
%patch119 -p1 -b .bz733298-config-drastically-improve-cman-rrp-configuration
%patch120 -p1 -b .bz759603-cman-improve-quorum-timer-handling
%patch121 -p1 -b .bz678372-1-qdiskd-make-multipath-issues-go-away
%patch122 -p1 -b .bz678372-2-allocate-port-in-cnxman-socket-for-qdiskd
%patch123 -p1 -b .bz678372-3-qdisk-small-tiny-little-cleanup
%patch124 -p1 -b .bz750314-fenced_fix_handling_of_startup_partition_merge
%patch125 -p1 -b .bz750314-2-dlm_controld_fix_handling_of_startup_partition_merge
%patch126 -p1 -b .bz803510-fsck.gfs2_fix_handling_of_eattr_indirect_blocks
%patch127 -p1 -b .bz804938-config_update_relax_ng_schema_to_include_totem_miss_count_const
%patch128 -p1 -b .bz806002-cman_init_fix_start_sequence_error_handling
%patch129 -p1 -b .bz808441-man_update_fenced_8_to_reflect_limitation_xml_dtd_validation
%patch130 -p1 -b .bz745538-2-qdisk-5-ping-example-missing-w
%patch131 -p1 -b .bz819787_cman_notifyd_deliver_cluster_status_on_startup
%patch132 -p1 -b .bz814807_qdiskd_allow_master_to_failover_quickly_when_using_master_wins
%patch133 -p1 -b .bz785866_config_fix_type_in_schema
%patch134 -p1 -b .bz786118_cman_preconfig_allow_host_aliases_as_valid_cluster_nodenames
%patch135 -p1 -b .bz839241-1-cman_fix_data_copy_and_memory_leak_when_reloading_config
%patch136 -p1 -b .bz839241-2-cman_fix_data_copy_and_memory_leak_when_reloading_config
%patch137 -p1 -b .bz821016-1-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld
%patch138 -p1 -b .bz821016-2-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld
%patch139 -p1 -b .bz821016-3-cman_init_allow_sysconfig_cman_to_pass_options_to_dlm_controld
%patch140 -p1 -b .bz842370_cman_init_allow_dlm_hash_table_sizes_to_be_tunable_at_startup
%patch141 -p1 -b .bz838047_qdiskd_restrict_master_wins_mode_to_2_node_cluster
%patch142 -p1 -b .bz845341_fenced_fix_log_file_mode
%patch143 -p1 -b .bz838945-fsck.gfs2_fix_buffer_overflow_in_get_lockproto_table
%patch144 -p1 -b .bz847234-1-use_new_corosync_confdb_api_to_remove_string_limit
%patch145 -p1 -b .bz847234-2-ccs_do_not_truncate_lists
%patch146 -p1 -b .bz853180-gfs_controld_fenced_fix_ignore_nolock_for_mounted_nolock_fs
%patch147 -p1 -b .bz797952-1-fence_node_libfence_status
%patch148 -p1 -b .bz797952-2-fenced_fence_check_delay
%patch149 -p1 -b .bz797952-3-fence_check_add_script_and_man_page
%patch150 -p1 -b .bz857299-cman_init_allow_dlm_tcp_port_to_be_configurable_via_cman_init_script
%patch151 -p1 -b .bz854032-cman_init_increase_default_shutdown_timeouts
%patch152 -p1 -b .bz803477-fsck.gfs2_soften_the_messages_when_reclaiming_freemeta_blocks
%patch153 -p1 -b .bz861340-fenced_silence_dbus_error
%patch154 -p1 -b .bz509056-1_cman_init_make_sure_we_start_after_fence_sanlockd
%patch155 -p1 -b .bz509056-2_checkquorum.wdmd_add_integration_script_with_wdmd
%patch156 -p1 -b .bz862847-mkfs.gfs2_check_locktable_more_strictly_for_valid_chars
%patch157 -p1 -b .bz857952-fenced_get_the_cman_fd_before_each_poll
%patch158 -p1 -b .bz860048-fsck.gfs2_check_for_formal_inode_number_mismatch
%patch159 -p1 -b .bz887787_cman_prevent_libcman_from_causing_sigpipe_when_corosync_is_down
%patch160 -p1 -b .bz888053-1-gfs2_convert-mark-rgrp-bitmaps-dirty-when-converting
%patch161 -p1 -b .bz888053-2-gfs2_convert-mark-buffer-dirty-when-switching-dirs-f
%patch162 -p1 -b .bz888053-3-gfs2_convert-remember-number-of-blocks-when-converti
%patch163 -p1 -b .bz888053-4-gfs2_convert-Use-proper-header-size-when-reordering-
%patch164 -p1 -b .bz888053-5-gfs2_convert-calculate-height-1-for-small-files-that
%patch165 -p1 -b .bz888053-6-gfs2_convert-clear-out-old-di_mode-before-setting-it
%patch166 -p1 -b .bz888053-7-gfs2_convert-mask-out-proper-bits-when-identifying-s
%patch167 -p1 -b .bz888053-8-fsck.gfs2-Detect-and-fix-mismatch-in-GFS1-formal-ino
%patch168 -p1 -b .bz509056-3_build_ship_checkquorum.wdmd_non_executable
%patch169 -p1 -b .bz886585-gfs2_grow_report_bad_return_codes_on_error
%patch170 -p1 -b .bz902920-01-libgfs2_Add_readahead_for_rgrp_headers
%patch171 -p1 -b .bz902920-02-fsck_Speed_up_reading_of_dir_leaf_blocks
%patch172 -p1 -b .bz902920-03-libgfs2_externalize_dir_split_leaf
%patch173 -p1 -b .bz902920-04-libgfs2_allow_dir_split_leaf_to_receive_a_leaf_buffer
%patch174 -p1 -b .bz902920-05-libgfs2_let_dir_split_leaf_receive_a__broken__lindex
%patch175 -p1 -b .bz902920-06-fsck.gfs2_Move_function_find_free_blk_to_util.c
%patch176 -p1 -b .bz902920-07-fsck.gfs2_Split_out_function_to_make_sure_lost_found_exists
%patch177 -p1 -b .bz902920-08-fsck.gfs2_Check_for_formal_inode_mismatch_when_adding_to_lost_found
%patch178 -p1 -b .bz902920-09-fsck.gfs2_shorten_some_debug_messages_in_lost_found
%patch179 -p1 -b .bz902920-10-fsck.gfs2_Move_basic_directory_entry_checks_to_separate_function
%patch180 -p1 -b .bz902920-11-fsck.gfs2_Add_formal_inode_check_to_basic_dirent_checks
%patch181 -p1 -b .bz902920-12-fsck.gfs2_Add_new_function_to_check_dir_hash_tables
%patch182 -p1 -b .bz902920-13-fsck.gfs2_Special_case__..__when_processing_bad_formal_inode_number
%patch183 -p1 -b .bz902920-14-fsck.gfs2_Move_function_to_read_directory_hash_table_to_util.c
%patch184 -p1 -b .bz902920-15-fsck.gfs2_Misc_cleanups_from_upstream
%patch185 -p1 -b .bz902920-16-fsck.gfs2_Verify_dirent_hash_values_correspond_to_proper_leaf_block
%patch186 -p1 -b .bz902920-17-fsck.gfs2_re
%patch187 -p1 -b .bz902920-18-fsck.gfs2_fix_leaf_blocks,_don_t_try_to_patch_the_hash_table
%patch188 -p1 -b .bz902920-19-fsck.gfs2_check_leaf_depth_when_validating_leaf_blocks
%patch189 -p1 -b .bz902920-20-fsck.gfs2_small_cleanups
%patch190 -p1 -b .bz902920-21-fsck.gfs2_reprocess_inodes_when_blocks_are_added
%patch191 -p1 -b .bz902920-22-fsck.gfs2_Remove_redundant_leaf_depth_check
%patch192 -p1 -b .bz902920-23-fsck.gfs2_link_dinodes_that_only_have_extended_attribute_problems
%patch193 -p1 -b .bz902920-24-fsck.gfs2_Add_clarifying_message_to_duplicate_processing
%patch194 -p1 -b .bz902920-25-fsck.gfs2_separate_function_to_calculate_metadata_block_header_size
%patch195 -p1 -b .bz902920-26-fsck.gfs2_Rework_the__undo__functions
%patch196 -p1 -b .bz902920-27-fsck.gfs2_Check_for_interrupt_when_resolving_duplicates
%patch197 -p1 -b .bz902920-28-fsck.gfs2_Consistent_naming_of_struct_duptree_variables
%patch198 -p1 -b .bz902920-29-fsck.gfs2_Keep_proper_counts_when_duplicates_are_found
%patch199 -p1 -b .bz902920-30-fsck.gfs2_print_metadata_block_reference_on_data_errors
%patch200 -p1 -b .bz902920-31-fsck.gfs2_print_block_count_values_when_fixing_them
%patch201 -p1 -b .bz902920-32-fsck.gfs2_Do_not_invalidate_metablocks_of_dinodes_with_invalid_mode
%patch202 -p1 -b .bz902920-33-fsck.gfs2_Log_when_unrecoverable_data_block_errors_are_encountered
%patch203 -p1 -b .bz902920-34-fsck.gfs2_don_t_remove_buffers_from_the_list_when_errors_are_found
%patch204 -p1 -b .bz902920-35-fsck.gfs2_Don_t_flag_GFS1_non
%patch205 -p1 -b .bz902920-36-fsck.gfs2_externalize_check_leaf
%patch206 -p1 -b .bz902920-37-fsck.gfs2_pass2_check_leaf_blocks_when_fixing_hash_table
%patch207 -p1 -b .bz902920-38-fsck.gfs2_standardize_check_metatree_return_codes
%patch208 -p1 -b .bz902920-39-fsck.gfs2_don_t_invalidate_files_with_duplicate_data_block_refs
%patch209 -p1 -b .bz902920-40-fsck.gfs2_check_for_duplicate_first_references
%patch210 -p1 -b .bz902920-41-fsck.gfs2_When_flagging_a_duplicate_reference,_show_valid_or_invalid
%patch211 -p1 -b .bz902920-42-fsck.gfs2_major_duplicate_reference_reform
%patch212 -p1 -b .bz902920-43-fsck.gfs2_Remove_all_bad_eattr_blocks
%patch213 -p1 -b .bz902920-44-fsck.gfs2_Remove_unused_variable
%patch214 -p1 -b .bz902920-45-fsck.gfs2_double
%patch215 -p1 -b .bz902920-46-fsck.gfs2_Trivial_typo_fix
%patch216 -p1 -b .bz902920-47-fsck.gfs2_Stop__undo__process_when_error_data_block_is_reached
%patch217 -p1 -b .bz902920-48-fsck.gfs2_Don_t_allocate_leaf_blocks_in_pass1
%patch218 -p1 -b .bz902920-49-fsck.gfs2_take_hash_table_start_boundaries_into_account
%patch219 -p1 -b .bz902920-50-fsck.gfs2_delete_all_duplicates_from_unrecoverable_damaged_dinodes
%patch220 -p1 -b .bz963657-init.d_gfs2_work_around_nested_mount_points_umount_bug
%patch221 -p1 -b .bz984085-1-fsck.gfs2_fix_some_log_messages
%patch222 -p1 -b .bz984085-2-fsck.gfs2_Fix_directory_link_on_relocated_directory_dirents
%patch223 -p1 -b .bz984085-3-fsck.gfs2_Fix_infinite_loop_in_pass1b_caused_by_duplicates_in_hash_table
%patch224 -p1 -b .bz984085-4-fsck.gfs2_don_t_check_newly_created_lost+found_in_pass2
%patch225 -p1 -b .bz984085-5-fsck.gfs2_avoid_negative_number_in_leaf_depth
%patch226 -p1 -b .bz984085-6-fsck.gfs2_Detect_and_fix_duplicate_references_in_hash_tables
%patch227 -p1 -b .bz985796-fsck.gfs2_Dont_rely_on_cluster_conf_when_rebuilding_sb
%patch228 -p1 -b .bz871603-ccs_tool_fix_example_fence_device_help
%patch229 -p1 -b .bz874538-libccs_dont_use_unitialized_value_in_xpathlite
%patch230 -p1 -b .bz888318-qdiskd_change_log_level_for_token_error_message
%patch231 -p1 -b .bz893925-1-cman_fenced_fix_killing_on_2node_cluster_suffering_brief_outage
%patch232 -p1 -b .bz893925-2-cman_fenced_fix_killing_on_2node_cluster_suffering_brief_outage
%patch233 -p1 -b .bz896191-config_fix_cluster_conf_man_page_logging_default
%patch234 -p1 -b .bz920358-qdiskd_do_not_count_missed_updates_from_offline_nodes
%patch235 -p1 -b .bz982670-cman_create_destroy_lockfile_on_restart_etc
%patch236 -p1 -b .bz889564-gfs_controld_avoid_mismatching_messages_with_old-cgs
%patch237 -p1 -b .bz888857-fenced_dlm_controld_gfs_controld_use_cluster_dead_for_corosync_connections
%patch238 -p1 -b .bz987508-1-libgfs2_Fix_pointer_arithmetic_in_gfs2_quota_change
%patch239 -p1 -b .bz987508-2-gfs2_edit_fix_a_segfault_with_file_names_255_bytes
%patch240 -p1 -b .bz987508-3-gfs2_edit_Clean_up_some_magic_offsets
%patch241 -p1 -b .bz987508-4-gfs2_edit_display_pointer_offsets_for_directory_dinodes
%patch242 -p1 -b .bz987508-5-gfs2_edit_Add_new_option_to_print_all_bitmaps_for_an_rgrp
%patch243 -p1 -b .bz987508-6-gfs2_edit_print_formal_inode_numbers_and_hash_value_on_dir_display
%patch244 -p1 -b .bz989647-fsck_gfs2_Add_ability_to_detect_journal_inode_indirect_block_corruption
%patch245 -p1 -b .bz996233-1-gfs2_tool_Update_etc_mtab_with_metafs_mounts_handle_interrupts
%patch246 -p1 -b .bz996233-2-libgfs2_check_return_code_of_rename
%patch247 -p1 -b .bz996233-3-libgfs2_Correct_error_message_in_mtab_update_code
%patch248 -p1 -b .bz996233-4-libgfs2_Set_umask_before_calling_mkstemp
%patch249 -p1 -b .bz1007970-mkfs_gfs2_Add_missing_K_option
%patch250 -p1 -b .bz1059269-fenced_keep_manual_fifo_open
%patch251 -p1 -b .bz1059853-libgfs2_Fix_up_remove_mtab_entry
%patch252 -p1 -b .bz1062742-fsck_gfs2_Check_and_repair_per_node_contents_such_as_quota_changeX
%patch253 -p1 -b .bz1053668-1-libgfs2_patch_to_update_gfs1_superblock_correctly
%patch254 -p1 -b .bz1053668-2-gfs2_utils_check_and_fix_bad_dinode_pointers_in_gfs1_sb
%patch255 -p1 -b .bz1081517-fsck_gfs2_Log_to_syslog_on_start_and_exit
%patch256 -p1 -b .bz1081523-1-gfs2_edit_Add_a_savemeta_file_metadata_header
%patch257 -p1 -b .bz1081523-2-gfs2_edit_Fix_loop_arithmetic_in_restore_data
%patch258 -p1 -b .bz1081523-3-gfs2_edit_Ensure_all_leaf_blocks_in_per_node_are_saved
%patch259 -p1 -b .bz1081523-4-gfs2_edit_Reinstate_a_check_for_system_dinodes
%patch260 -p1 -b .bz979313-qdisk_check_cman_wait_return.patch
%patch261 -p1 -b .bz980575-libccs_read_logging_attributes_correctly.patch
%patch262 -p1 -b .bz1029210-qdisk_quorum_init_complete_after_tko_up_cycles.patch
%patch263 -p1 -b .bz1035929-config_fix_typos_and_phrasing_in_defaults_file.patch
%patch264 -p1 -b .bz1074551-ccs_tool_fix_crash_using_verbose.patch
%patch265 -p1 -b .bz981043-man_mention_cluster_conf_html_schema_in_man_page.patch
%patch266 -p1 -b .bz994234-fenced_remove_mention_of_skip_undefined_feature.patch
%patch267 -p1 -b .bz981043-doc_update_cluster_conf_html.patch
%patch268 -p1 -b .bz1080174-mount_gfs2_Don_t_leave_mount_group_if_mount_returns_EBUSY
%patch269 -p1 -b .bz843160-dlm_controld_Adjust_fence_time_comparison.patch
%patch270 -p1 -b .bz886016-man_update_fence_node_options.patch
%patch271 -p1 -b .bz982305-1-fenced_wait_for_ringid.patch
%patch272 -p1 -b .bz982305-2-gfs_controld_Fix_first_recovery_case.patch
%patch273 -p1 -b .bz982305-3-gfs_controld_Fix_first_recovery_case2.patch
%patch274 -p1 -b .bz982820-rgmanager_add_reboot_on_pid_exhaustion_attr.patch
%patch275 -p1 -b .bz1149516-1-fsck_gfs2_fix_broken_i_goal_values_in_inodes
%patch276 -p1 -b .bz1149516-2-gfs2_convert_use_correct_i_goal_values_instead_of_zeros_for_inodes
%patch277 -p1 -b .bz1149516-3-fsck_gfs2_Reprocess_nodes_if_anything_changed_addendum_1_of_2
%patch278 -p1 -b .bz1149516-4-fsck_gfs2_addendum_to_fix_broken_i_goal_values_in_inodes_addendum_2_of_2
%patch279 -p1 -b .bz1121693-libgfs2_Use_a_matching_context_mount_option_in_mount_gfs2_meta
%patch280 -p1 -b .bz1133724-logt_fix_race_when_reopening_logfiles.patch
%patch281 -p1 -b .bz1087286-xml-ccs_update_schema-be-verbose-about-extraction-fa.patch
%patch282 -p1 -b .bz1095418-qdiskd_heuristics_needed_for_3nodes_or_more.patch
%patch283 -p1 -b .bz1095657-daemons_better_logging_if_receive_start_fails.patch
%patch284 -p1 -b .bz1099223-qdisk_enable_master_wins_if_votes_1.patch
%patch285 -p1 -b .bz1111500-cman_fix_manpage_altname_text.patch
%patch286 -p1 -b .bz1142947-cman_fix_message_for_non-2node_clusters.patch
%patch287 -p1 -b .bz1121693-libgfs2_Make_sure_secontext_gets_freed
%patch288 -p1 -b .bz1233535-dlm_controld_retry_uevent_on_error.patch
%patch289 -p1 -b .bz1234443-gfs_controld_retry_uevent_on_error.patch
%patch290 -p1 -b .bz1238754-fsck_gfs2_replace_recent_i_goal_fixes_with_simple_logic
%patch291 -p1 -b .bz1206149-1-fsck_gfs2_Change_duptree_structure_to_have_generic_flags
%patch292 -p1 -b .bz1206149-2-fsck_gfs2_Detect_fix_and_clone_duplicate_block_refs_within_a_dinode
%patch293 -p1 -b .bz1077890-fenced_delay_kill_due_to_stateful_merge.patch
%patch294 -p1 -b .bz1171241-libcman_dont_segv_if_dev_zero_doesnt_exist.patch
%patch295 -p1 -b .bz1193169-cman_improve_node_name_matching.patch
%patch296 -p1 -b .bz1206188-cman_delete_tempfile_if_ccs_validate_fails.patch
%patch297 -p1 -b .bz1243944-gfs_show_more_than_128_fs.patch
%patch298 -p1 -b .bz1245232-qdiskd_fix_leak_in_unaligned_write.patch
%patch299 -p1 -b .bz1245232-qdiskd_fix_memcpy_in_unaligned_write.patch
%patch300 -p1 -b .bz1257732-qdiskd_watch_for_other_nodes_leaving_during_master_election.patch
%patch301 -p1 -b .bz1252991-fenced_remove_fencedevice_attributes_from_-S.patch
%patch302 -p1 -b .bz1221728-schema_add_rrp_attributes.patch
%patch303 -p1 -b .bz1297165-proper_vote_check.patch
%patch304 -p1 -b .bz1202817-gfs2_utils_Add_the_glocktop_utility


%build
./configure \
  --sbindir=%{_sbindir} \
  --initddir=%{_sysconfdir}/rc.d/init.d \
  --libdir=%{_libdir} \
  --without_bindings \
  --without_rgmanager \
  --disable_kernel_check

##CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}
CFLAGS="$(echo '%{optflags}')" make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fix up
# /etc/sysconfig/cman
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cp cman/init.d/cman.init.defaults \
   %{buildroot}%{_sysconfdir}/sysconfig/cman
# logrotate name
mv %{buildroot}%{_sysconfdir}/logrotate.d/cluster \
	%{buildroot}%{_sysconfdir}/logrotate.d/cman
# remove static libraries
find %{buildroot} -name "*.a" -exec rm {} \;
# fix library permissions or fedora strip helpers won't work.
find %{buildroot} -name "lib*.so.*" -exec chmod 0755 {} \;
# fix lcrso permissions or fedora strip helpers won't work.
find %{buildroot} -name "*.lcrso" -exec chmod 0755 {} \;
# remove docs
rm -rf %{buildroot}/usr/share/doc/cluster
# cleanup perl bindings bits
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -empty -exec rm -f {} \;
find %{buildroot} -type f -name CCS.so -exec chmod 755 {} \;

%clean
rm -rf %{buildroot}

## Runtime and subpackages section

# main empty package
%description
Red Hat Cluster

## subpackages

%package -n cman
Group: System Environment/Base
Summary: Red Hat Cluster Manager
Requires(post): chkconfig
Requires(preun): initscripts
Requires(preun): chkconfig
Requires: corosync >= 1.4.1-10
Requires: openais >= 1.1.1-1
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: ricci >= 0.15.0-4 modcluster >= 0.15.0-3
Requires: fence-agents >= 3.1.5-1
Requires: fence-virt >= 0.2.3-1
Requires: clusterlib = %{version}-%{release}
Obsoletes: dlm-pcmk < 3.0.12-26
Provides: dlm-pcmk = %{version}
Obsoletes: gfs-pcmk < 3.0.12-26
Provides: gfs-pcmk = %{version}
Obsoletes: resource-agents < 3.9.2-1
Requires: /usr/bin/xsltproc

%description -n cman
Red Hat Cluster Manager

%post -n cman
/sbin/chkconfig --add cman
ccs_update_schema > /dev/null 2>&1 ||:

# make sure to stop cman always as last
%preun -n cman
if [ "$1" = 0 ]; then
	/sbin/service cman stop >/dev/null 2>&1
	/sbin/chkconfig --del cman
fi

%files -n cman
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence doc/*.txt
%doc doc/cman_notify_template.sh doc/cluster_conf.html
# %doc config/plugins/ldap/*.ldif
%dir %{_sysconfdir}/cluster
%{_sysconfdir}/rc.d/init.d/cman
%dir %{_sysconfdir}/cluster/cman-notify.d
%config(noreplace) %{_sysconfdir}/logrotate.d/cman
%config(noreplace) %{_sysconfdir}/sysconfig/cman
%{_sbindir}/ccs*
%{_sbindir}/cman*
# %{_sbindir}/confdb2ldif
%{_sbindir}/dlm_controld
%{_sbindir}/dlm_tool
%{_sbindir}/fence*
%{_sbindir}/gfs_control
%{_sbindir}/gfs_controld
%{_sbindir}/group*
%{_sbindir}/*qdisk*
/usr/libexec/*
%dir %{_datadir}/cluster
%{_datadir}/cluster/cluster.rng
%{_datadir}/cluster/checkquorum
%{_datadir}/cluster/checkquorum.wdmd
%dir %{_datadir}/cluster/relaxng
%{_datadir}/cluster/relaxng/cluster.rng.in.head
%{_datadir}/cluster/relaxng/cluster.rng.in.tail
# %{perl_vendorarch}/*
%dir /var/log/cluster
%dir /var/lib/cluster
%dir /var/run/cluster
%{_mandir}/man5/*
%{_mandir}/man8/ccs*
%{_mandir}/man8/checkquorum.8.gz
%{_mandir}/man8/cman*
# %{_mandir}/man8/confdb2ldif*
%{_mandir}/man8/dlm_tool*
%{_mandir}/man8/dlm_controld.8.gz
%{_mandir}/man8/fence*
%{_mandir}/man8/gfs_control.*
%{_mandir}/man8/gfs_controld.8.gz
%{_mandir}/man8/group*
%{_mandir}/man8/*qdisk*
# %{_mandir}/man3/*.3pm.gz

%package -n clusterlib
Group: System Environment/Libraries
Summary: The Red Hat Cluster libraries
Conflicts: cman < 3.0.3-1
Provides: cmanlib = %{version}
Obsoletes: cmanlib < 3.0.0-5.alpha4

%description -n clusterlib
The Red Hat Cluster libraries package

%files -n clusterlib
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%config(noreplace) %{_sysconfdir}/udev/rules.d/*-dlm.rules
%{_libdir}/libcman.so.*
%{_libdir}/libccs*.so.*
%{_libdir}/libdlm*.so.*
%{_libdir}/libfence*.so.*
%{_libdir}/liblogthread*.so.*

%post -n clusterlib -p /sbin/ldconfig

%postun -n clusterlib -p /sbin/ldconfig

%package -n clusterlib-devel
Group: Development/Libraries
Summary: The Red Hat Cluster libraries development package
Requires: clusterlib = %{version}-%{release}
Requires: pkgconfig
Provides: cman-devel = %{version}
Obsoletes: cman-devel < 3.0.0-5.alpha4
Provides: cmanlib-devel = %{version}
Obsoletes: cmanlib-devel < 3.0.0-5.alpha4

%description -n clusterlib-devel
The Red Hat Cluster libraries development package

%files -n clusterlib-devel
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_libdir}/libcman.so
%{_libdir}/libccs*.so
%{_libdir}/libdlm*.so
%{_libdir}/libfence*.so
%{_libdir}/liblogthread*.so
%{_includedir}/ccs.h
%{_includedir}/libcman.h
%{_includedir}/libdlm*.h
%{_includedir}/libfence.h
%{_includedir}/libfenced.h
%{_includedir}/liblogthread.h
%{_mandir}/man3/*3.gz
%{_libdir}/pkgconfig/*.pc

%package -n gfs2-utils
Group: System Environment/Kernel
Summary: Utilities for managing the global filesystem (GFS2)
Requires(post): chkconfig
Requires(preun): initscripts
Requires(preun): chkconfig
Requires: file

%description -n gfs2-utils
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
filesystems.

%post -n gfs2-utils
/sbin/chkconfig --add gfs2

%preun -n gfs2-utils
if [ "$1" = 0 ]; then
	/sbin/service gfs2 stop >/dev/null 2>&1
	/sbin/chkconfig --del gfs2
fi

%files -n gfs2-utils
%defattr(-,root,root,-)
%doc doc/COPYRIGHT doc/README.licence doc/COPYING.*
%{_sysconfdir}/rc.d/init.d/gfs2
/sbin/*.gfs2
%{_sbindir}/glocktop
%{_sbindir}/*gfs2*
%{_mandir}/man8/*gfs2*
%{_mandir}/man8/glocktop*

%changelog
* Mon Sep 05 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 3.0.12.1-78.0
- Added patch from Jacco
- add ARM architectures

* Thu Jan 28 2016 Andrew Price <anprice@redhat.com> - 3.0.12.1-78
- gfs2-utils: Add the glocktop utility
  Resolves: rhbz#1202817

* Tue Jan 12 2016 Ken Gaillot <kgaillot@redhat.com> - 3.0.12.1-77
- cman: Properly check for votes when node names aren't specified
  Resolves: rhbz#1297165

* Thu Nov 25 2015 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-75
- libfence: Remove fencedevice params from fence_node -S so that asking for
  status does not shut down a node if action= is set
  Resolves: rhbz#1252991
- schema: add RRP attributes for <token> section
  Resolves: rhbz#1221728

* Mon Nov 23 2015 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-75
- fenced: Delay killing a node if there's a stateful merge after a short outage
  Resolves: rhbz#1077890
- cman_tool: Don't segfault if /dev/zero doesn't exist
  Resolves: rhbz#1171241
- cman: Improve node-name matching algorithm
  Resolves: rhbz#1193169
- cman: Delete temp file if ccs_validation fails
  Resolves: rhbz#1206188
- dlm_controld: reconnect uevent socket on error
  Resolves: rhbz#1221815
- gfs_controld: reconnect uevent socket on error
  Resolves: rhbz#1225583
- groupd: Show more than 128 mount groups or lockspaces
  Resolves: rhbz#1243944
- qdiskd: fix memory leak in unaligned write path
  Resolves: rhbz#1245232
- qdiskd: fix memory copy in unaligned write path
  Resolves: rhbz#1245232
- qdiskd: Watch for other nodes leaving during a master re-election
  Resolves: rhbz#1257732
 

* Mon Nov 02 2015 Andrew Price <anprice@redhat.com> - 3.0.12.1-74
- fsck.gfs2: replace recent i_goal fixes with simple logic
  Resolves: rhbz#1238754
- fsck.gfs2: Change duptree structure to have generic flags
- fsck.gfs2: Detect, fix and clone duplicate block refs within a dinode
  Resolves: rhbz#1206149

* Mon Jul 06 2015 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-73.1
- gfs_controld: Retry uevent recv() and reconnect uevent socket on error
  Resolves: rhbz#1234443
- dlm_controld: Retry uevent recv() and reconnect uevent socket on error
  Resolves: rhbz#1233535 

* Thu Mar 05 2015 Andrew Price <anprice@redhat.com> - 3.0.12.1-73
- libgfs2: Make sure secontext gets freed (addendum)
  Resolves: #1121693

* Tue Mar 3 2015 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-72
- xml: ccs_update_schema: be verbose about extraction fail
  Resolves rhbz#1087286
- qdiskd: warn if no heuristics defied for >2 node clusters
  Resolves: rhbz#1095418
- *_controld: better logging if receive_start fails
  Resolves: rhbz#1095657
- qdiskd: Enable master_wins if votes=1
  Resolves: rbhz#1099223
- cman: fix cman.5 man page to indicate only 1 altname is allowed
  Resolves: rhbz#1111500
- cman: Slight fix to message issued for invalid two_node clusters
  Resolves: rhbz#1142947

* Thu Feb 26 2015 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-71
- liblogthread: fix potential race when reopening logfiles
  Resolves: rhbz#1133724

* Tue Feb 24 2015 Andrew Price <anprice@redhat.com> - 3.0.12.1-70
- libgfs2: Use a matching context mount option in mount_gfs2_meta
  Resolves: rhbz#1121693

* Tue Jan 20 2015 Andrew Price <anprice@redhat.com> - 3.0.12.1-69
- fsck.gfs2: fix broken i_goal values in inodes
- gfs2_convert: use correct i_goal values instead of zeros for inodes
- fsck.gfs2: Reprocess nodes if anything changed - addendum 1 of 2
- fsck.gfs2: addendum to fix broken i_goal values in inodes - addendum 2 of 2
  Resolves: rhbz#1149516

* Thu Jul 03 2014 Ryan McCabe <rmccabe@redhat.com> - 3.0.12.1-68
- config: add new <rm> attribute "reboot_on_pid_exhaustion" to the schema

* Mon Jun 23 2014 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-67
- dlm_controld: Adjust fence time comparison
  Resolves: #rhbz843160
- man: update fence_node options
  Resolves: #rhbz886016
- fenced: Wait for ringid
  gfs_controld: Fix first recovery case
  Resolves: #rhbz982305

* Mon Jun 16 2014 Andrew Price <anprice@redhat.com> - 3.0.12.1-66
- mount.gfs2: Don't leave mount group if mount returns EBUSY
  Resolves: rhbz#1080174

* Mon Jun 16 2014 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-65
- doc: update cluster_conf.html to latest version.
  Resolves: rhbz#981043

* Mon Jun 16 2014 Christine Caulfield <ccaulfie@redhat.com> - 3.0.12.1-64
- qdisk: Check cman_wait() return value and report errors
  Resolves: rhbz#979313
- libccs: Read daemon logging attributes correctly
  Resolves: rhbz#980575
- qdisk: Quorum init complete after tko_up cycles, not tko
  Resolves: rhbz#1029210
- config: Fix typos and phrasing in defaults file
  Resolves: rhbz#1035929
- ccs_tool: Fix crash using --verbose
  Resolves: rhbz#1074551
- manpage: Mention cluster.conf.html schema in man page
  Resolves: rhbz#981043
- fenced: Remove mention of skip_undefined feature as it is not supported
  Resolves: rhbz#994234

* Mon Jun 09 2014 Andrew Price <anprice@redhat.com> - 3.0.12.1-63
- gfs2_edit: Add a savemeta file metadata header
- gfs2_edit: Fix loop arithmetic in restore_data
- gfs2_edit: Ensure all leaf blocks in per_node are saved
- gfs2_edit: Reinstate a check for system dinodes
  Resolves: rhbz#1081523

* Tue May 20 2014 Andrew Price <anprice@redhat.com> - 3.0.12.1-62
- fsck.gfs2: Log to syslog on start and exit
  Resolves: rhbz#1081517

* Sat Apr 12 2014 Andrew Price <anprice@redhat.com> - 3.0.12.1-61
- libgfs2: Fix up remove_mtab_entry
  Resolves: rhbz#1059853
- fsck.gfs2: Check and repair per_node contents such as quota_changeX
  Resolves: rhbz#1062742
- libgfs2: patch to update gfs1 superblock correctly
- gfs2-utils: check and fix bad dinode pointers in gfs1 sb
  Resolves: rhbz#1053668

* Thu Apr 3 2014 Chrissie Caulfield <ccaulfie@redhat.com> - 3.0.12.1-60
- fenced: keep manual ACk fifo open for longer and also make fenced_external()
  write to it.
  Resolves: rhbz#1059269

* Mon Sep 16 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-59
- mkfs.gfs2: Add missing 'K' option
  Resolves: rhbz#1007970

* Fri Aug 16 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-58
- libgfs2: Set umask before calling mkstemp
  Resolves: rhbz#996233

* Thu Aug 15 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-57
- gfs2_tool: Update /etc/mtab with metafs mounts, handle interrupts (3 patches)
  Resolves: rhbz#996233

* Wed Aug 07 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-56
- fsck.gfs2: Add ability to detect journal inode indirect block corruption
  Resolves: rhbz#989647

* Thu Jul 25 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-55
- Remove .patch from some patch tmp file names
- gfs2_edit: Fix bug and add functions from upstream (6 patches)
  Resolves: rhbz#987508

* Tue Jul 23 2013 Chrissie Caulfield <ccaulfie@redhat.com> - 3.0.12.1-54
- cman: Use correct patch to create and destroy lockfile on restart

* Fri Jul 19 2013 Chrissie Caulfield <ccaulfie@redhat.com> - 3.0.12.1-53
- ccs_tool: Fix example fence device in "ccs_tool create" help
  Resolves: rhbz#871603
- libccs: don't use uninitialized value in xpathlite
  Resolves: rhbz#874538
- qdiskd: change log level for an error message
  Resolves: rhbz#888318
- fenced/dlm_controld/gfs_controld: use cluster_dead for corosync connections
  Resolves: rhbz#888857
- gfs_controld: avoid mismatching messages with old cgs
  Resolves: rhbz#889564
- cman|fenced: Fix node killing in case of a 2node cluster that suffers brief network out
  Resolves: rhbz#893925
- config: fix cluster.conf man page to reflect correct syslog_facility default
  Resolves: rhbz#896191
- qdiskd: Do not count missed updates from offline nodes
  Resolves: rhbz#920358
- cman: create and destroy lockfile on restart
  Resolves: rhbz#982670

* Thu Jul 18 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-52
- fsck.gfs2: Handle multiple occurrences of one leaf in a directory hash table (6 patches)
  Resolves: rhbz#984085
- fsck.gfs2: Don't rely on cluster.conf when rebuilding sb
  resolves: rhbz#985796

* Mon Jul 08 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-51
- init.d/gfs2: Work around nested mount points umount bug
  Resolves: rhbz#963657

* Fri Jun 14 2013 Andrew Price <anprice@redhat.com> - 3.0.12.1-50
- gfs2_grow: report bad return codes on error
  Resolves: rhbz#886585
- fsck.gfs2: fix misplaced directory leaf blocks (50 patches)
  Resolves: rhbz#902920

* Mon Jan  7 2013 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-49
- build: ship checkquorum.wdmd non executable
  Resolves: rhbz#509056

* Thu Jan  3 2013 Bob Peterson <rpeterso@redhat.com> - 3.0.12.1-48
- After converting a GFS1 file system with gfs2_convert errors were detected with fsck.gfs2
  Resolves: rhbz#888053

* Thu Dec 20 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-47
- cman: prevent libcman from causing SIGPIPE when corosync is down
  Resolves: rhbz#887787

* Thu Oct 30 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-46
- fsck.gfs2: Check for formal inode number mismatch
  Resolves: rhbz#860048

* Thu Oct 25 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-45
- fenced: get the cman fd before each poll
  Resolves: rhbz#857952

* Mon Oct 15 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-44
- mkfs.gfs2: Check locktable more strictly for valid chars
  Resolves: rhbz#862847

* Wed Oct 10 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-43
- cman init: make sure we start after fence_sanlockd and warn users
- checkquorum.wdmd: add integration script with wdmd
  (requires wdmd >= 2.6)
  Resolves: rhbz#509056

* Mon Oct  8 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-42
- fenced: silence dbus error
  Resolves: rhbz#861340

* Tue Sep 25 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-41
- fsck.gfs2: soften the messages when reclaiming freemeta blocks
  Resolves: rhbz#803477

* Tue Sep 18 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-40
- cman init: increase default shutdown timeouts
  Resolves: rhbz#854032

* Fri Sep 14 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-39
- cman init: allow dlm tcp port to be configurable via cman init script
  Resolves: rhbz#857299

* Fri Sep  7 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-38
- Add support for fence_check
  Resolves: rhbz#797952

* Mon Sep  3 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-37
- gfs_controld, fenced: fix ignore_nolock for mounted nolock fs
  Resolves: rhbz#853180

* Tue Aug 21 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-36
- Requires corosync 1.4.1-10 for runtime
  Related: rhbz#847234

* Tue Aug 21 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-35
- config: use new corosync confdb api to remove string lenght limit
  Resolves: rhbz#847234
- Update requirements on newer corosync
  Related: rhbz#847234

* Wed Aug 16 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-34
- fsck.gfs2: Fix buffer overflow in get_lockproto_table
  Resolves: rhbz#838945

* Wed Aug 15 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-33
- qdiskd: allow master to failover quickly when using master_wins
  Resolves: rhbz#814807
- config: Fix typo in schema
  Resolves: rhbz#785866
- cman-preconfig: allow host aliases as valid cluster nodenames
  Resolves: rhbz#786118
- cman: fix data copy and memory leak when reloading config
  Resolves: rhbz#839241
- cman init: allow sysconfig/cman to pass options to dlm_controld
  Resolves: rhbz#821016
- cman init: allow dlm hash table sizes to be tunable at startup
  Resolves: rhbz#842370
- qdiskd: restrict master_wins to 2 node cluster
  Resolves: rhbz#838047
- fenced: fix log file mode
  Resolves: rhbz#845341

* Tue May  8 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-32
- Fix qdisk(5) man page example
  Resolves: rhbz#745538
- cman notifyd: deliver cluster status on startup
  Resolves: rhbz#819787

* Mon Apr  2 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-31
- man: update fenced.8 to reflect a limitation in XML/DTD implementation
  Resolves: rhbz#808441

* Fri Mar 30 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-30
- config: update relax ng schema to include totem miss_count_const
  Resolves: rhbz#804938
- cman init: fix start sequence error handling
  Resolves: rhbz#806002

* Fri Mar 23 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-29
- fsck.gfs2: Fix handling of eattr indirect blocks
  Resolves: rhbz#803510

* Wed Mar  7 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-28
- config: drastically improve cman RRP configuration handling
  Resolves: rhbz#733298

* Thu Mar 01 2012 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-27
- fenced: fix handling of startup partition merge
  dlm_controld: fix handling of startup partition merge
  Resolves: rhbz#750314

* Mon Feb 20 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-26
- Fix qdisk(5) man page example
  Resolves: rhbz#745538
- config: make altname validation position indipendent
  Resolves: rhbz#740552
- config: drastically improve cman RRP configuration handling
  Resolves: rhbz#733298
- cman: Improve quorum timer handling how quorum timers work
  Resolves: rhbz#759603
- qdiskd: Make multipath issues go away
  Resolves: rhbz#678372

* Fri Feb 17 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-25
- gfs_controld: don't ignore dlmc_fs_register error
  Resolves: rhbz#753300
- gfs2_edit savemeta: crosswrite four patches from upstream (4 patches)
  Resolves: rhbz#749864
- gfs2_utils: gfs2_grow fails to grow a filesystem with less than 3 RGs
  Resolves: rhbz#742595
- gfs2_utils: Improve error messages
  Resolves: rhbz#742293

* Mon Feb 06 2012 Andrew Price <anprice@redhat.com> - 3.0.12.1-24
- fsck.gfs2: add ability to fix GFS (gfs1) file systems (66 patches)
  Resolves: rhbz#675723
- libgfs2: Don't count sentinel dirent as an entry
  Resolves: rhbz#745161
- mkfs.gfs2: Improve error messages
  Resolves: rhbz#769400

* Fri Sep 30 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-23
- fenced/dlm_controld/gfs_controld: full check for member changes
  Resolves: rhbz#663397

* Fri Sep 23 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-22
- cman: allow late close of stderr file descriptor and free resources
  Resolves: rhbz#740385

* Tue Sep 20 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-21
- dlm_controld: fix man page example formatting
  Resolves: rhbz#739682

* Mon Sep 19 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-20
- cman: fix copying uidgid trees to corosync
  Resolves: rhbz#733345

* Fri Sep  9 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-19
- cman: fix multicast address in cman.5 man page
  Resolves: rhbz#735906
- cman: default to 2 different mcast addresses in RRP mode and set
  rrp_problem_count_threshold
  cman now requires corosync > 1.4.1-3 for RRP operations
  Resolves: rhbz#735912
- cman: improve cman/qdisk interactions
  * cman: do better logging/error reports/checking of the quorum API usage
  * qdiskd: allow qdiskd to update device name in cman
  * qdiskd: perform better error checking at startup
  Resolves: rhbz#735917

* Mon Sep  5 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-18
- config: invalidate ccs_update_schema cache if we received traps/signals
  Resolves: rhbz#733424

* Thu Sep  1 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-17
- config: allow cman to configure uid/gid for corosync IPC
  Resolves: rhbz#733345

* Tue Aug 30 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-16
- dlm_controld: quiet mkdir EEXIST message
  Resolves: rhbz#732991

* Mon Aug 29 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-15
- config: fix handling of temporary directory in ccs_update_schema
  Resolves: rhbz#680930

* Wed Aug 24 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-14
- cman: make RRP mode passive the default
  Resolves: rhbz#732635

* Mon Aug 22 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-13
- dlm_controld: fix plock dev_write no op
  Resolves: rhbz#731775

* Fri Aug 19 2011 Andrew Price <anprice@redhat.com> - 3.0.12.1-12
- mount.gfs2: Fix mounting of regular files with -o loop
  Resolves: rhbz#729071

* Thu Aug 18 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-11
- cman: fix handling of transport configuration when altname is specified
  Resolves: rhbz#695795

* Mon Aug  8 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-10
- cman: fix handling of transport configuration in cman/totem preconfig
  Resolves: rhbz#695795

* Fri Aug  5 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-9
- cman: print error if clustername is too long or not configured at all
  Resolves: rhbz#728230
- config: fix escaping of xml special characters
  Resolves: rhbz#726065

* Tue Aug 02 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12.1-8
- config: Add 'disabled' flag to rm element
  Related: rhbz#723925

* Tue Jul 26 2011 Andrew Price <anprice@redhat.com> - 3.0.12.1-7
- mkfs.gfs2: Handle gfs2 creation on regular files
  Resolves: rhbz#720668
- mount.gfs2: gfs2 mounts doubled up in mtab
  Resolves: rhbz#706141
- tunegfs2: Ensure we don't try to open a null device
  Resolves: rhbz#719124
- tunegfs2: Fix usage message
  Resolves: rhbz#719126
- tunegfs2: Fix label/locktable setting code
  Resolves: rhbz#719135

* Tue Jul 12 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-6
- ccs: add dynamic relaxng schema generation
- spec file update:
  * Add Requires: /usr/bin/xsltproc
  * Bump Requires: for fence-agents and fence-virt
  * Obsolets resource-agents that do not provide xsl/relaxng infrastructure
  * ship %{_datadir}/cluster/relaxng
  Resolves: rhbz#680930

* Thu Jun 23 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-5
- tunegfs2: gfs2-utils should include tunegfs2
  (gfs2_add_tunegfs2.patch)
  Resolves: rhbz#704178

* Mon Jun 20 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-4
- fsck.gfs2 only rebuilds one missing journal at a time
  (gfs2_fsck_only_rebuilds_one_missing_journal_at_a_time.patch)
  Resolves: rhbz#683104
- cman: fix ttl default if no value is specified
  (cman_fix_ttl_default_if_no_value_is_specified.patch)
  Resolves: rhbz#713977

* Thu Jun 16 2011 Andrew Price <anprice@redhat.com> - 3.0.12.1-3
- gfs2_edit: Fix savemeta compression for older zlibs
  (gfs2_edit_fix_savemeta_compression_for_older_zlibs.patch)
  Resolves: rhbz#702313

* Tue Jun 14 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-2
- Reported UUID from 'gfs2_edit -p sb' should be lower-case
  (gfs2_reported_uuid_should_be_lowercase.patch)
  Resolves: rhbz#694823
- gfs2_edit savemeta doesn't save all leaf blocks for large dirs
  (gfs2_edit_savemeta_does_not_save_all_leaf_blocks_for_large_dirs.patch)
  Resolves: rhbz#679566
- gfs2_grow: fix growing of full filesystems
  (gfs2_grow_fix_growing_of_full_filesystem.patch)
  Resolves: rhbz#707091
- dlm_controld: clear waiting plocks for closed files
  (dlm_controld_clear_waiting_plocks_for_closed_files.patch)
  Resolves: rhbz#678585
- fsck.gfs2: segfault in pass1b
  (gfs2_fsck_segfault_in_pass1b.patch)
  Resolves: rhbz#679080
- gfs2_edit: Add compression to savemeta and restoremeta
  (gfs2_edit_add_compression_to_savemeta_and_restoremeta.patch)
  (add BuildRequires: zlib-devel)
  Resolves: rhbz#702313
- cman_tool: fix typo in man page
  (cman_tool_fix_typo_in_man_page.patch)
  Resolves: rhbz#691400

* Tue Jun 14 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12.1-1
- Rebase package on top of new upstream
- spec file update:
  * update spec file copyright date
  * drop all patches
  * update and clean configure and build section.
  Resolves: rhbz#707115

* Tue Mar 22 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-41
- gfs2_convert: exits with success without doing anything
  (gfs2_convert_exists_with_success_without_doing_anything_part2.patch)
  Resolves: rhbz#688734

* Mon Mar 21 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-40
- gfs2_convert: exits with success without doing anything
  (gfs2_convert_exists_with_success_without_doing_anything.patch)
  Resolves: rhbz#688734

* Fri Mar 18 2011 Lon Hohberger <lhh@redhat.com> - 3.0.12-39
- config: Add DRBD 0.8.3 metadata back to schema
  (add_drbd_0_8_3_metadata_back_to_schema.patch)
  Resolves: rhbz#680172

* Fri Mar 18 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-38
- qdiskd: Fix bad timer check
  (qdiskd_fix_bad_timer_check.patch)
  Resolves: rhbz#688154
- cman init: increase the default timeout waiting for quorum
  (cman_init_increase_default_timeout_waiting_for_quorum.patch)
  Resolves: rhbz#688201

* Tue Mar 15 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-37
- cman-preconfig: allow cman to configure corosync multicast ttl
  (cman_preconfig_allow_cman_to_configure_multicast_ttl.patch)
  Resolves: rhbz#684020

* Tue Mar  8 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-36
- Fix race condition at startup that affects dlm based applications
  (dlm_controld_always_return_error_if_daemon_is_not_ready_to_operate.patch)
  (cman_init_wait_for_dlm_controld_to_be_fully_operational_before_proceeding.patch)
  Resolves: rhbz#595725

* Mon Feb 28 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-35
- config_xml: stop leaking memory on config reload
  (config_stop_leaking_memory_on_config_reload.patch)
  Resolves: rhbz#680155

* Wed Feb 23 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-34
- fenced: don't ignore victim_done messages for reduced victims
  (fenced_do_not_ignore_victim_done_messages_for_reduced_victims.patch)
  Resolves: rhbz#678704

* Fri Feb  4 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-33
- qdiskd: Fix auto-vote calculation loop
  (qdiskd_fix_auto_vote_calculation_loop.patch)
  Resolves: rhbz#663433

* Fri Feb  4 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-32
- gfs2_edit enhancements:
  * gfs2_edit: handle corrupt file systems better
    (gfs2_edit_handle_corrupt_filesystems_better.patch)
  * gfs2_edit: print large block numbers better
    (gfs2_edit_print_large_block_numbers_better.patch)
  * gfs2_edit: has problems printing gfs1 journals
    (gfs2_edit_has_problems_printing_gfs1_journals.patch)
  * gfs2_edit: add -d option for printing journal details
    (gfs2_edit_add_d_option_for_printing_journal_details.patch)
  * gfs2_edit: Fix error message on blockalloc when outside bitmap
    (gfs2_edit_fix_error_message_blockalloc_when_outside_bitmap.patch)
  * gfs2_edit: fix careless compiler warning
    (gfs2_edit_fix_careless_compiler_warning.patch)
  * gfs2_edit: Fix bitmap editing function
    (gfs2_edit_fix_bitmap_editing_function.patch)
  * gfs2_edit: fix segfault in set_bitmap when block is in rgrp
    (gfs2_edit_fix_segfault_in_set_bitmap_when_block_is_rgrp.patch)
  Resolves: rhbz#674843
- fenced: emit dbus signals to be handled by foghorn package for SNMP traps
  (fenced_send_dbus_signals_when_node_is_fenced.patch)
  (fenced_update_fenced_man_page_with_q_option.patch)
  (build_allow_dbus_notification_code_to_be_disabled.patch)
  Resolves: rhbz#592964
- config: Update relax ng schema 
  (config_update_schema_2.patch)
- doc: Update cluster_conf.html to match schema
  (doc_update_cluster_conf_html.patch)
  Resolves: rhbz#618705

* Thu Feb  3 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-31
- fsck.gfs2: can't repair rgrps resulting from gfs_grow->gfs2_convert
  (fsck_gfs2_cannot_repair_rgrps_resulting_from_gfs_grow_plus_gfs2_convert.patch)
  Resolves: rhbz#576640
- qdisk: Informational syslog message indicating label overrides device
  (qdiskd_info_syslog_msg_when_lavel_overriders_device.patch)
  Resolves: rhbz#635413
- Integrate watchdog with cluster to reboot nodes under specific heuristics
  (cman_add_checkquorum_script_for_self_fencing_part1.patch)
  (cman_add_checkquorum_script_for_self_fencing_part2.patch)
  Resolves: rhbz#560700

* Fri Jan 28 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-30
- mkfs.gfs2 segfaults with 18.55TB and -b512
  (gfs2_mkfs_segfaults_with_18.55T_and_b512.patch)
  Resolves: rhbz#624535
- fsck.gfs2: reports master/root dinodes as unused and fixes the bitmap
  (gfs2_fsck_reports_master_root_dinodes_as_unused_and_fixes_bitmap.patch)
  Resolves: rhbz#663037

* Wed Jan 19 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-29
- ccs_tool: deprecate editing capabilities
  (ccs_tool_deprecate_editing_capabilities.patch)
  Resolves: rhbz#614885

* Fri Jan 14 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-28
- cman init: do not include wrong default file
  (cman_init_do_not_include_wrong_default_config_file.patch)
  Resolves: rhbz#669340

* Thu Jan 13 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-27
- gfs_controld: fix plock owner in unmount
  (gfs_controld_fix_plock_owner_in_umount.patch)
  Resolves: rhbz#624822
- mkfs.gfs2 should support discard request generation
  (gfs2_mkfs_should_support_discard_request_generation.patch)
  Resolves: rhbz#656956
- ccs_tool: completely remove references to update/upgrades
  (ccs_tool_man_page_shows_removed_update_upgrade_subcommands.patch)
  Resolves: rhbz#577874
- cman: allow users to configure transport method
  (cman_does_not_allow_user_to_select_transport_mechanism.patch)
  Resolves: rhbz#657041
- cman_tool: display meaningful translation of corosync exit code
  (cman_tool_display_meaningful_translation_of_corosync_exit_codes.patch)
  Resolves: rhbz#617247
- cman_tool: handle "another instance running" error code
  (cman_tool_handle_another_instance_is_running_error_code.patch)
  Related: rhbz#617247, rhbz#617234
- cman init: check if corosync is already running
  (cman_init_check_if_corosync_is_running.patch)
- cman: handle INT and TERM signals correctly
  (cman_handle_int_and_term_signals_correctly.patch)
  Resolves: rhbz#617234
- cman init: add support for "nocluster" kernel cmdline to not start at boot
  (cman_init_add_support_for_nocluster_kernel_cmdline.patch)
  Resolves: rhbz#563901
- cman: Make qdiskd exit if removed from configuration
  (cman_make_qdiskd_exit_if_removed_from_config.patch)
  Resolves: rhbz#620679
- cman: Update cman_tool version section in man page
  (cman_update_cman_tool_version_section_in_man_page.patch)
  Resolves: rhbz#619874
- config: Add missing qdiskd options
  (config_add_missing_qdiskd_options.patch)
  Resolves: rhbz#645830
- qdisk: Assume 1 vote if not specified in cluster.conf
  (qdiskd_should_assume_1_vote_if_not_specified.patch)
  Resolves: rhbz#663433
- config: Fix broken fence_egenera options
  (fence_egenera_add_missing_options_in_cluster_rng.patch)
  Resolves: rhbz#629017
- cman: Make qdiskd heuristics time out
  (cman_make_qdisk_heuristics_time_out.patch)
  Resolves: rhbz#636243

* Thu Jan  6 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-26
- Drop dlm-pcmk and gfs-pcmk variants of dlm_controld and gfs_controld
  that are now replaced by pacemaker + cman support.
  Resolves: rhbz#649021

* Thu Oct 21 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-25
- dlm_controld: fix plock owner syncing
  (dlm_controld_fix_plock_owner_syncing.patch)
  Resolves: rhbz#617306
- dlm_controld: fix plock signature in stored message
  (dlm_controld_fix_plock_signature_in_stored_message.patch)
  Resolves: rhbz#623816
- dlm_controld: ignore plocks until checkpoint time
  (dlm_controld_ignore_plocks_until_checkpoint_time.patch)
  Resolves: rhbz#623810
- gfs_controld: fix plock owner syncing
  (gfs_controld_fix_plock_owner_syncing.patch)
  Resolves: rhbz#617306
- fenced: use post_join_delay after cluster join
  (fenced_use_post_join_delay_after_cluster_join.patch)
  Resolves: rhbz#624844
- gfs2_edit enhancements:
  * gfs2_edit: better printing of directory leaf information
    (gfs2_edit_better_printing_of_dir_leaf_information.patch)
  * gfs2_edit: print hex numbers in lower-case
    (gfs2_edit_print_hex_numbers_in_lower_case.patch)
  * gfs2_edit: negative block numbers don't jump a negative amount
    (gfs2_edit_negative_block_numbers_dont_jump_a_negative_amount.patch)
  * gfs2_edit: tiny (stuffed) files had user data saved with savemeta
    (gfs2_edit_tiny_files_had_user_data_saved_with_savemeta.patch)
  * gfs2_edit: give meaningful feedback for savemeta and restoremeta
    (gfs2_edit_give_meaningful_feedback_for_savemeta_and_restoremeta.patch)
  * gfs2_edit: Fix memory leak in savemeta option
    (gfs2_edit_fix_memory_leak_in_savemeta_option.patch)
  * gfs2_edit: Split extended display functions into extended.c
    (gfs2_edit_split_extended_display_functions_into_extended_c.patch)
  * gfs2_edit: Move more functions to extended.c
    (gfs2_edit_move_more_functions_to_extended_c.patch)
  * gfs2_edit: Extend individual field printing/editing
    (gfs2_edit_extend_individual_field_printing_editing.patch)
  * gfs2_edit: fix page down on rindex
    (gfs2_edit_fix_page_down_on_rindex.patch)
  * gfs2_edit: print field names in right column
    (gfs2_edit_print_field_names_in_right_column.patch)
  * gfs2_edit: display block allocation on rgrps and bitmaps
    (gfs2_edit_display_block_allocation_on_rgrps_and_bitmaps.patch)
  * gfs2_edit: fix extended.h to not double-include
    (gfs2_edit_fix_extended_h_to_not_double_include.patch)
  Resolves: rhbz#634623
- gfs2_convert: corrupts file system when directory has di_height 3
  (gfs2_convert_corrupts_file_system_when_directory_has_di_height_3.patch)
  Resolves: rhbz#630005

* Tue Oct 05 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-24
- GFS2: fsck.gfs2 seems to process large files twice
  (fsck_gfs2_seems_to_process_large_files_twice.patch)
  Resolves: rhbz#621313
- fsck.gfs2 segfaults if journals are missing
  (fsck_gfs2_segfaults_if_journals_are_missing.patch)
  Resolves: rhbz#622576
- fsck.gfs2 truncates directories with more than 100,000 entries
  (fsck_gfs2_truncates_directories_with_more_than_100,000_entries.patch)
  Resolves: rhbz#628013
- Updating /proc/mounts and /etc/mtab with mount args for GFS2 fs
  (updating_proc_mounts_and_etc_mtab_with_mount_args_for_gfs2_fs.patch)
  Resolves: rhbz#632595
- cman init: fix "stop remove" operation
  (cman_init_fix_stop_remove_operation.patch)
  cman: Calculate expected_votes correctly after leave remove
  (cman_calculate_expected_votes_correctly_after_leave_remove.patch)
  Resolves: rhbz#634718
- gfs2_convert: gfs2_convert doesn't resume after interrupted conversion
  (gfs2_convert_doesn_t_resume_after_interrupted_conversion.patch)
  Resolves: rhbz#637913
- cman: fix startup race condition when configs are different across nodes
  (cman_fix_startup_race_condition_when_configs_are_different_across_nodes.patch)
  Resolves: rhbz#639018

* Tue Aug 17 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-23
- gfs2-utils: fsck.gfs2 deletes directories if they get too big
  (gfs2_fsck_do_not_delete_directories_if_they_get_too_big.patch)
  Resolves: rhbz#624691

* Fri Aug 13 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-22
- gfs2-utils: mkfs can't fsync device with 32MB RGs
  (gfs2_utils_mkfs_can_t_fsync_device_with_32mb_rgs.patch)
  Resolves: rhbz#622844

* Thu Aug 05 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-21
- cman: do not propagate old configurations around
  (cman_do_not_propagate_old_configurations_around.patch)
  cman: Clarify man page on config distribution
  (cman_clarify_man_page_on_config_distribution.patch)
  Resolves: rhbz#619680

* Wed Jul 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-20
- Fix regression in "Fix fsck.gfs2 unaligned access on ia64" that
  affects all 32bit systems.
  Rename fsck_gfs2_unaligned_access_on_ia64.patch to
  fsck_gfs2_unaligned_access_on_ia64_part1.patch
  (fsck_gfs2_unaligned_access_on_ia64_part2.patch)
  Resolves: rhbz#608154

* Tue Jul 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-19
- dlm_controld/gfs_controld: make default plock_ownership 0
  Use the simpler, safer, and more reliable option as default.
  (controld_make_default_plock_ownership_0.patch)
  Resolves: rhbz#618303
- dlm_controld: fix plock checkpoint signatures
  (dlm_controld_fix_plock_checkpoint_signatures.patch)
  Resolves: rhbz#618806
- dlm_controld: fix plock owner in checkpoints
  (dlm_controld_fix_plock_owner_in_checkpoints.patch)
  Resolves: rhbz#618814
- cman: fix consensus calculation
  Bump Requires: corosync to 1.2.3-17 to guarantee that corosync
  is at the minimal version for this fix to work.
  (cman_fix_consensus_calculation.patch)
  Resolves: rhbz#618534

* Tue Jul 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-18
- Fix several issues related to cluster config reload operation
  including checks that would allow the config to be downgraded
  and extra spurious config reload notifications.
  (cman_config_reload_fix_part1.patch)
  (cman_config_reload_fix_part2.patch)
  (cman_config_reload_fix_part3.patch)
  (cman_config_reload_fix_part4.patch)
  (cman_config_reload_fix_part5.patch)
  (cman_config_reload_fix_part6.patch)
  Resolves: rhbz#617161, rhbz#617163
- Fix logging configuration reload operations
  (cman_preconfig_handle_logging_reload_operation_part1.patch)
  (cman_preconfig_handle_logging_reload_operation_part2.patch)
  Resolves: rhbz#615202

* Fri Jul 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-17
- cman init: allow startup options to fenced
  (cman_init_allow_startup_options_to_fenced.patch)
  Resolves: rhbz#617566

* Fri Jul 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-16
- cman: Check for new configs only once per second to avoid 100% cpu spin
  (cman_check_config_only_once_per_sec.patch)
  Resolves: rhbz#616222

* Thu Jul 22 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-15
- cman: Recalculate quorum on quorum device vote changes
  (cman_recalculate_quorum_on_quorum_device_vote_changes.patch)
  Resolves: rhbz#606989

* Mon Jul 19 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-14
- cman: Recalculate quorum on config change
  (recalculate_quorum_on_config_change.patch)
  Resolves: rhbz#606989
- config: Add tomcat-6 resource agent to schema
  (add_tomcat_6_resource_agent_to_schema.patch)
  doc: Add tomcat-6 to cluster_conf.html
  (add_tomcat_6_to_cluster_conf_html.patch)
  Resolves: rhbz#614127
- config: Add missing cman_label
  (add_missing_cman_label.patch)
  config: Add doc for cman_label attribute
  (add_doc_for_cman_label_attribute.patch)
  Resolves: rhbz#615509
- config: Allow multiple logging_daemon tags
  (allow_multiple_logging_daemon_tags.patch)
  Resolves: rhbz#614961
- cman config: copy all logging objects to the top level tree
  (config_copy_all_logging_objects_to_the_top_level_tree.patch)
  Resolves: rhbz#615202

* Mon Jul 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-13
- Add autogenerated cluster_conf.html
  (doc_autogen_cluster_conf_html_part1.patch)
  (doc_autogen_cluster_conf_html_part2.patch)
  Resolves: rhbz#593015
- Update relax ng schema
  (config_update_schema.patch)
  Related: rhbz#595547, rhbz#593015
- Fix patch file naming
  Related: rhbz#553383, rhbz#606368, rhbz#609978, rhbz#612097

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-12
- Fix gfs2 init script to be more LSB compliant
  (gfs2_init_lsb_compliant.patch)
  Resolves: rhbz#553383

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-11
- Add /etc/sysconfig/cman example file with extensive documentation
  of options that can be passed to the init script.
  (cman_sysconfig_part1.patch from upstream)
  (cman_sysconfig_part2.patch rhel6 specific)
  Resolves: rhbz#606368

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-10
- Add cman_tool version -S to man page
  (cman_tool_config_reload_man_page.patch)
  Resolves: rhbz#609978
- Fix cman init script to be more LSB compliant
  (cman_init_lsb_compliant.patch)
  Resolves: rhbz#612097

* Mon Jun 28 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-9
- Update gfs2_convert man page
  (gfs2_convert_manpage_update.patch)
  Resolves: rhbz#601315
- Don't return 0 if gfs2_edit restoremeta fails
  (gfs2_edit_restoremeta_should_not_return_0_on_failure.patch)
  Resolves: rhbz#607321
- Fix fsck.gfs2 unaligned access on ia64
  (fsck_gfs2_unaligned_access_on_ia64.patch)
  Resolves: rhbz#608154

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-8
- Add missing components to cluster schema
  (config_add_missing_resource_docs_to_schema.patch)
- Clean up recursion in cluster schema
  (config_clean_up_recursion_in_schema.patch)
  Resolves: rhbz#604298

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-7
- Ensure cman recalculates quorum on configuration reload
  (cman_recalculate_expected_votes_on_config_reload.patch)
  Resolves: rhbz#606989

* Fri May 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-6
- Fix device name and mount point in utils
  (gfs2_fix_device_name_and_mount_point_in_utils.patch)
  Resolves: rhbz#597002

* Fri May 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-5
- Fix dlm_controld wrong fencing time comparison (part2):
  Rename dlm_controld_wrong_fencing_time_comparison.patch to
  dlm_controld_wrong_fencing_time_comparison_part1.patch
  Add dlm_controld_wrong_fencing_time_comparison_part2.patch
  Resolves: rhbz#594511

* Thu May 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-4
- cman: fix quorum recalculation when a node is externally killed
  (cman_fix_quorum_recalculation.patch)
  Resolves: rhbz#596046
- rpmdiff automatic test tool found 2 issues:
  * add missing man pages for cman_notify, dlm_controld.pcmk and
    gfs_controld.pcmk, and update the spec file to ship them
    in the correct subpackages.
  (add_missing_man_pages.patch)
  * cman, dlm-pcmk, gfs-pcmk should have a tigher Requires on cluster
    libraries.
  Resolves: rhbz#594111

* Tue May 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-3
- Fix dlm_controld wrong fencing time comparison
  (dlm_controld_wrong_fencing_time_comparison.patch)
  Resolves: rhbz#594511
- Fix ccs_tool create -n
  (fix_ccs_tool_create.patch)
  Resolves: rhbz#594626

* Tue May 18 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-2
- Fix cman init script stop action to wait for corosync daemon to shutdown
  (cman_init_wait_for_corosync_shutdown.patch)
  Resolves: rhbz#592103
- fenced: use cpg ringid
  (fenced_use_cpg_ringid.patch)
  Update Requires/BuildRequires on corosync + cpg ringid patch.
  Resolves: rhbz#584140
- fix changelog entries from 3.0.12-1 (missing bugzilla entries)

* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- Rebase on top of new upstream bug fix only release:
  * drop all bug fix patches.
  * refresh patches with official SHA1 git commits from RHEL6
    upstream branch:
    - disable_ldap_loader_support.patch
    - support_only_xmlconfig_loader.patch
    - disable_fence_xvmd_support.patch
  * rename cman_use_hashed_cluster_id_part4.patch to
    cman_use_hash_cluster_id_by_default.patch.
  * Addresses the following issues:
    from 3.0.11 release:
  Resolves: rhbz#581047, rhbz#576330, rhbz#582017, rhbz#583945
  Resolves: rhbz#581038
    from 3.0.12 release:
  Resolves: rhbz#589823, rhbz#586100, rhbz#585083, rhbz#587079
  Resolves: rhbz#590000
  * Rebase:
  Resolves: rhbz#582322
- Stop build on ppc and ppc64.
  Resolves: rhbz#590980
- cman should only load OpenAIS checkpoint service by default
  (cman_only_load_ckpt_service_by_default.patch)
  Resolves: rhbz#568407

* Wed Apr  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-5
- Fix ccs_tool man page
  (fix_ccs_tool_man_page.patch)
  Resolves: rhbz#577874
- dlm_controld: add plock checkpoint signatures
  (dlm_controld_add_plock_checkpoint_signatures.patch)
  Resolves: rhbz#578625
- dlm_controld: set last_plock_time for ownership operations
  (dlm_controld_set_last_plock_time_for_ownership_ops.patch)
  (gfs_controld_set_last_plock_time_for_ownership_ops.patch)
  Resolves: rhbz#578626
- dlm_controld: don't skip unlinking checkpoint
  (dlm_controld_do_not_skip_unlinking_checkpoint.patch)
  Resolves: rhbz#578628
- gfs2_convert segfaults when converting fs of blocksize 512 bytes
  (gfs2_convert_fix_segfault_with_512bytes_bs.patch)
  Resolves: rhbz#579621
- gfs2_convert uses too much memory for jdata conversion
  (gfs2_convert_uses_too_much_memory_for_jdata_conversion.patch)
  Resolves: rhbz#579623
- Fix conversion of gfs1 CDPNs
  (gfs2_convert_fix_conversion_of_gfs1_cdpns.patch)
  Resolves: rhbz#579625
- gfs2_convert: Doesn't convert indirectly-pointed eattrs correctly
  (gfs2_convert_does_not_convert_eattrs_correctly.patch)
  Resolves: rhbz#579626

* Fri Mar 26 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-4
- Fix weakness in clusterid generation by using non-crypto hashing.
  part1-3 are he upstream generic implemetation.
  part4 turns it on specifically for RHEL-6 as the change breaks
  micro rolling upgrades.
  (cman_use_hashed_cluster_id_part1.patch)
  (cman_use_hashed_cluster_id_part2.patch)
  (cman_use_hashed_cluster_id_part3.patch)
  (cman_use_hashed_cluster_id_part4.patch)
  Resolves: rhbz#574886
- Add plock debug buffer.
  (dlm_separate_plock_debug_buffer_part1.patch)
  (dlm_separate_plock_debug_buffer_part2.patch)
  Resolves: rhbz#576322
- Add more fs_notified debugging
  (dlm_controld_add_more_fs_notified_debugging.patch)
  Resolves: rhbz#576335
- dlm_controld/gfs_controld: avoid full plock unlock when no
  resource exists
  (controld_avoid_full_plock_unlock.patch)
  Resolves: rhbz#575103

* Tue Mar 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-3
- Fix fsck.gfs2 segfault
  (gfs2_fix_segfault_osi_tree.patch)
  Resolves: rhbz#574215

* Wed Mar 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-2
- Fix gfs2_quota hadle of boundary conditions
  (gfs2_fix_quota_boundary.patch)
  Resolves: rhbz#570525
- Fix gfs_controld dm suspend event handling
  (gfs_controld_dm_suspend.patch)
  Resolves: rhbz#571806

* Mon Mar  1 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- new upstream release:
  Resolves: rhbz#566784, rhbz#555047, rhbz#556603, rhbz#561862
  Resolves: rhbz#565907, rhbz#568446, rhbz#564471, rhbz#561416
  Resolves: rhbz#553383
- upstream rebase and patch cleanup
  Resolves: rhbz#557348
- gfs2: make use of exported device topology
  (gfs2_exported_dev_topology)
  Resolves: rhbz#519491
- spec file update:
  * cman should Requires fence-virt directly
  * merge changelog from Fedora
  * re-enable cmannotifyd support and ship doc/template

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-4
- Resolves: rhbz#567884
- Do not build cluster on s390 and s390x.

* Thu Jan 14 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-3
- Add workaround for corosync IPC shutdown issue (cman-init-workaround-bz547813.patch)
- Related: rhbz#547813

* Wed Jan 13 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Drop ldapconfig loader support (PM-disable-ldap-loader-support.patch)
- Drop notifyd support (PM-disable-notifyd-support.patch)
- Support only xmlconfig loader (PM-support-only-xmlconfig-loader.patch)
- Disable support for perl bindings

* Tue Jan 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New upstream release

* Tue Jan  6 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-2
- Drop gfs-utils commodity package

* Mon Dec  7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New upstream release
- spec file update:
  * use global instead of define
  * use new Source0 url
  * use %name macro more aggressively
  * bump Requires on fence-agents
  * ship var/run/cluster and var/lib/cluster

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New upstream release
- spec file update:
  * drop BuildRequires on slang-devel.

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New upstream release
- spec file update:
  * explicitly Requires newer version of fence-agents

* Fri Oct  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-2
- spec file update:
  * gfs-pcmk now Requires dlm-pcmk

* Fri Sep 25 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New upstream release
- spec file updates:
  * drop cp_workaround patch
  * stop shipping rgmanager from cluster
  * move dlm udev rules in clusterlib where they belong
  * enable pacemaker components build
  * ship 2 new rpms: dlm-pcmk and gfs-pcmk for pacemaker integration

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-2
- Add temporary workaround to install symlinks

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-1
- New upstream release

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-20
- New upstream release
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag
  * BuildRequires and Requires corosync/openais 1.0.0-1 final.

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-19.rc4
- New upstream release
- spec file updates:
  * cman subpackage: avoid unnecessary calls to ldconfig
  * rgmanager subpackage: drop unrequired Requires: that belong to ras
  * BuildRequires and Requires corosync/openais 1.0.0.rc1

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-18.rc3
- New upstream release
- spec file updates:
  * Drop local patches.
  * Update BuildRequires and Requires: on newer corosync/openais.

* Thu Jun 11 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-17.rc2
- Update from git up to 779dd3c23ca6c56f5b3f7a8a7831bae775c85201
- spec file updates:
  * Drop BuildRequires on libvolume_id-devel that's now obsoleted
  * gfs*-utils now Requires: file
  * Add temporary patch to get rid of volume_id references in the code

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-16.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970
- spec file updates:
  * BuildRequires / Requires: latest corosync and openais
  * Update configure invokation
  * Cleanup tree fix up bits that are now upstream
  * Ship cluster.rng
  * Move fsck/mkfs gfs/gfs2 binaries in /sbin to be FHS compliant

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-15.rc1
- New upstream release.
- Update corosync/openais BuildRequires and Requires.
- Drop --corosynclibdir from configure. Libs are now in standard path.
- Update BuildRoot usage to preferred versions/names
- Drop qdisk init script. Now merged in cman init from upstream.

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14.alpha7
- New upstream release.
- Update corosync/openais BuildRequires and Requires.
- Fix gfs-utils and cman man page overlapping files.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-13.alpha7
- New upstream release.
- Drop local build fix patch.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12.alpha6
- New upstream release.
- Add missing LICENCE and COPYRIGHT files from clusterlib-devel.
- Add patch to fix build failure (already upstream).

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.alpha5
- Stop building fence and resource agents.
- cman now Requires: fence-agents.
- rgmanager now Requires: resource-agents.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.alpha5
- Fix typo in gfs-utils preun scriptlet.
- Fix gfs-utils file list.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-9.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.alpha5
- New upstream release.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.alpha4
- Update to latest stable3 code from git (e3a9ac674fa0ff025e833dcfbc8575cada369843)
- Fix Provides: version.
- Update corosync/openais BuildRequires and Requires

* Fri Feb  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha4
- Fix datadir/fence directory ownership.

* Sat Jan 31 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha4
- New upstream release.
- Fix directory ownership #483330.
- Add support pkgconfig to devel package.
- Total libraries cleanup:
  - split libraries out of cman into clusterlib.
  - merge cmanlib into clusterlib.
  - rename cman-devel into clusterlib-devel.
  - merge cmanlib-devel into clusterlib-devel.
- Comply with multiarch requirements (libraries).
- Relax BuildRequires and Requires around corosync and openais.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha3
- New upstream release

* Wed Jan 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha2
- Move all binaries where they belong. All the legacy stuff is now dead.

* Mon Jan 12 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha2
- New upstream release (retag cvs package)

* Mon Jan 12 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha2
- New upstream release

* Wed Dec 17 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha1
- New upstream release.
- Fix legacy code build.
- Fix wrong conffile attribute.

* Mon Dec 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.13-1
- New upstream release.
- Drop gnbd* packages that are now a separate project.
- Tight dependencies with corosync/openais.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.99.12-2
- Rebuild for Python 2.6

* Mon Nov  3 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.12-1
- new upstream release.
  Fix several security related issues.

* Mon Oct 20 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.11-1
- new upstream release.
- drop obsoleted patches.
- include very important gfs1 bug fix.
- include fix for fence_egenera (CVE-2008-4192).

* Wed Oct  8 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-6
- cman init: add fix from upstream for cman_tool wrong path.

* Fri Sep 26 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-5
- cman now Requires: ricci and modcluster.

* Fri Sep 26 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-4
- Split libcman.so* from cman and cman-devel into  cmanlib and cmanlib-devel
  to break a very annoying circular dependency.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-3
- The "CVS HATES ME" release.
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-2
- Retag release.
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-1
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Wed Sep 03 2008 Jesse Keating <jkeating@redhat.com> - 2.99.08-3
- Rebuild for broken deps.
- Pull in upstream patches for libvolume_id changes

* Wed Sep 03 2008 Jesse Keating <jkeating@redhat.com> - 2.99.08-2
- Rebuild for broken deps.

* Tue Aug 12 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.08-1
- New upstream release.
- Drop local patch that's part of upstream.
- Tight BR and Requires for openais to a very specific version.
- cman Requires ricci as new default config distribution system.
  (ricci changes will land soon but in the meantime this is done our side)

* Fri Aug  1 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.07-1
- New upstream release.
- Add patch to build against new headers (already part of upstream next release)
- BR on perl(ExtUtils::MakeMaker) to build perl bindings
- Fix logrotate install from upstream
- Add "clean up after perl bindings" snippet
- Update Requires for perl bindings
- Properly split man3 man pages

* Tue Jul 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.06-1
- New upstream release.
- BR on new openais for logging features.
- drop local logrotate snippet in favour of upstream one.
- cman Requires: PyOpenSSL for telnet_ssl wrapper.
- cman Requires: pexpect and net-snmp-utils for fence agents.
  Thanks to sendro on IRC for spotting the issue.
- Another cleanup round for docs

* Tue Jun 24 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.05-1
- New upstream release
- Update licence tags again after upstream relicensing to kill OSL 2.1.
- Add 2 commodity packages (gfs-utils and gnbd-utils). They both
  require external kernel modules but at least userland will stay
  automatically in sync for our users.
- BR openais 0.84 for new logsys symbols (and requires for runtime).
- Update build section to enable gfs-utils and gnbd-utils.

* Mon Jun  9 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.04-1
- New upstream release
- Update license tags after major upstream cleanup (note: rgmanager
  includes a shell script that is shipped under OSL 2.1 license).
- Update inclusion of documents to reflect updated COPYRIGHT file
  from upstream.
- Add documentation to different packages.

* Mon Jun  2 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.03-1
- New upstream release
- cman Requires telnet and ssh client
- drops some tree fix up bits that are now upstream

* Fri May 23 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-4
- Add missing OpenIPMI requires to cman for fence_ipmilan

* Thu May 22 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-3
- New kernel-headers has what we need release.
- Drop BR on kernel-devel.
- Drop cluster-dlmheaders.patch.
- Drop --kernel_* from configure invokation.
- Cleanup a few comments in the spec file.

* Tue May 20 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-2
- disable parallel build (broken upstream)
- build requires higher openais (fix ppc64 build failure)

* Mon May 19 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-1
- New upstream release
- Shut up the last few rpmlint warnings

* Wed May 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-4
- Fix typo in rgmanager Summary

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-3
- Fix rgmanager License: tag.

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-2
- Drop BR on openais as it is pulled by openais-devel.
- Change postun section to use -p /sbin/ldconfig.
- Fix rgmanager Requires.

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-1
- Initial packaging.
