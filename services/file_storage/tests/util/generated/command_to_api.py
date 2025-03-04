# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates. All rights reserved.

SDK_client_map = {
    "fs.add_export_lock": "oci.file_storage.FileStorageClient.add_export_lock",
    "fs.add_file_system_lock": "oci.file_storage.FileStorageClient.add_file_system_lock",
    "fs.add_filesystem_snapshot_policy_lock": "oci.file_storage.FileStorageClient.add_filesystem_snapshot_policy_lock",
    "fs.add_mount_target_lock": "oci.file_storage.FileStorageClient.add_mount_target_lock",
    "fs.add_outbound_connector_lock": "oci.file_storage.FileStorageClient.add_outbound_connector_lock",
    "fs.add_replication_lock": "oci.file_storage.FileStorageClient.add_replication_lock",
    "fs.add_snapshot_lock": "oci.file_storage.FileStorageClient.add_snapshot_lock",
    "fs.cancel_downgrade_shape_mount_target": "oci.file_storage.FileStorageClient.cancel_downgrade_shape_mount_target",
    "fs.change_file_system_compartment": "oci.file_storage.FileStorageClient.change_file_system_compartment",
    "fs.change_filesystem_snapshot_policy_compartment": "oci.file_storage.FileStorageClient.change_filesystem_snapshot_policy_compartment",
    "fs.change_mount_target_compartment": "oci.file_storage.FileStorageClient.change_mount_target_compartment",
    "fs.change_outbound_connector_compartment": "oci.file_storage.FileStorageClient.change_outbound_connector_compartment",
    "fs.change_replication_compartment": "oci.file_storage.FileStorageClient.change_replication_compartment",
    "fs.create_export": "oci.file_storage.FileStorageClient.create_export",
    "fs.create_file_system": "oci.file_storage.FileStorageClient.create_file_system",
    "fs.create_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.create_filesystem_snapshot_policy",
    "fs.create_mount_target": "oci.file_storage.FileStorageClient.create_mount_target",
    "fs.create_outbound_connector": "oci.file_storage.FileStorageClient.create_outbound_connector",
    "fs.create_quota_rule": "oci.file_storage.FileStorageClient.create_quota_rule",
    "fs.create_replication": "oci.file_storage.FileStorageClient.create_replication",
    "fs.create_snapshot": "oci.file_storage.FileStorageClient.create_snapshot",
    "fs.delete_export": "oci.file_storage.FileStorageClient.delete_export",
    "fs.delete_file_system": "oci.file_storage.FileStorageClient.delete_file_system",
    "fs.delete_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.delete_filesystem_snapshot_policy",
    "fs.delete_mount_target": "oci.file_storage.FileStorageClient.delete_mount_target",
    "fs.delete_outbound_connector": "oci.file_storage.FileStorageClient.delete_outbound_connector",
    "fs.delete_quota_rule": "oci.file_storage.FileStorageClient.delete_quota_rule",
    "fs.delete_replication": "oci.file_storage.FileStorageClient.delete_replication",
    "fs.delete_replication_target": "oci.file_storage.FileStorageClient.delete_replication_target",
    "fs.delete_snapshot": "oci.file_storage.FileStorageClient.delete_snapshot",
    "fs.detach_clone": "oci.file_storage.FileStorageClient.detach_clone",
    "fs.estimate_replication": "oci.file_storage.FileStorageClient.estimate_replication",
    "fs.get_export": "oci.file_storage.FileStorageClient.get_export",
    "fs.get_export_set": "oci.file_storage.FileStorageClient.get_export_set",
    "fs.get_file_system": "oci.file_storage.FileStorageClient.get_file_system",
    "fs.get_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.get_filesystem_snapshot_policy",
    "fs.get_mount_target": "oci.file_storage.FileStorageClient.get_mount_target",
    "fs.get_outbound_connector": "oci.file_storage.FileStorageClient.get_outbound_connector",
    "fs.get_quota_rule": "oci.file_storage.FileStorageClient.get_quota_rule",
    "fs.get_replication": "oci.file_storage.FileStorageClient.get_replication",
    "fs.get_replication_target": "oci.file_storage.FileStorageClient.get_replication_target",
    "fs.get_snapshot": "oci.file_storage.FileStorageClient.get_snapshot",
    "fs.list_export_sets": "oci.file_storage.FileStorageClient.list_export_sets",
    "fs.list_exports": "oci.file_storage.FileStorageClient.list_exports",
    "fs.list_file_systems": "oci.file_storage.FileStorageClient.list_file_systems",
    "fs.list_filesystem_snapshot_policies": "oci.file_storage.FileStorageClient.list_filesystem_snapshot_policies",
    "fs.list_mount_targets": "oci.file_storage.FileStorageClient.list_mount_targets",
    "fs.list_outbound_connectors": "oci.file_storage.FileStorageClient.list_outbound_connectors",
    "fs.list_quota_rules": "oci.file_storage.FileStorageClient.list_quota_rules",
    "fs.list_replication_targets": "oci.file_storage.FileStorageClient.list_replication_targets",
    "fs.list_replications": "oci.file_storage.FileStorageClient.list_replications",
    "fs.list_snapshots": "oci.file_storage.FileStorageClient.list_snapshots",
    "fs.pause_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.pause_filesystem_snapshot_policy",
    "fs.remove_export_lock": "oci.file_storage.FileStorageClient.remove_export_lock",
    "fs.remove_file_system_lock": "oci.file_storage.FileStorageClient.remove_file_system_lock",
    "fs.remove_filesystem_snapshot_policy_lock": "oci.file_storage.FileStorageClient.remove_filesystem_snapshot_policy_lock",
    "fs.remove_mount_target_lock": "oci.file_storage.FileStorageClient.remove_mount_target_lock",
    "fs.remove_outbound_connector_lock": "oci.file_storage.FileStorageClient.remove_outbound_connector_lock",
    "fs.remove_replication_lock": "oci.file_storage.FileStorageClient.remove_replication_lock",
    "fs.remove_snapshot_lock": "oci.file_storage.FileStorageClient.remove_snapshot_lock",
    "fs.schedule_downgrade_shape_mount_target": "oci.file_storage.FileStorageClient.schedule_downgrade_shape_mount_target",
    "fs.toggle_quota_rules": "oci.file_storage.FileStorageClient.toggle_quota_rules",
    "fs.unpause_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.unpause_filesystem_snapshot_policy",
    "fs.update_export": "oci.file_storage.FileStorageClient.update_export",
    "fs.update_export_set": "oci.file_storage.FileStorageClient.update_export_set",
    "fs.update_file_system": "oci.file_storage.FileStorageClient.update_file_system",
    "fs.update_filesystem_snapshot_policy": "oci.file_storage.FileStorageClient.update_filesystem_snapshot_policy",
    "fs.update_mount_target": "oci.file_storage.FileStorageClient.update_mount_target",
    "fs.update_outbound_connector": "oci.file_storage.FileStorageClient.update_outbound_connector",
    "fs.update_quota_rule": "oci.file_storage.FileStorageClient.update_quota_rule",
    "fs.update_replication": "oci.file_storage.FileStorageClient.update_replication",
    "fs.update_snapshot": "oci.file_storage.FileStorageClient.update_snapshot",
    "fs.upgrade_shape_mount_target": "oci.file_storage.FileStorageClient.upgrade_shape_mount_target",
    "fs.validate_key_tabs": "oci.file_storage.FileStorageClient.validate_key_tabs",
}
