# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util

'''
Tests verifying that moved/renamed commands appear as expected.
'''


class TestDataIntegration(unittest.TestCase):
    def setUp(self):
        pass

    def test_connection_create_object_storage(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-object-storage'])
        assert "Error: No such command 'create-connection-create-connection-from-object-storage'." in result.output

    def test_connection_create_atp(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-atp'])
        assert "Error: No such command 'create-connection-create-connection-from-atp'." in result.output

    def test_connection_create_adwc(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-adwc'])
        assert "Error: No such command 'create-connection-create-connection-from-adwc'." in result.output

    def test_connection_create_oracle(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-oracle'])
        assert "Error: No such command 'create-connection-create-connection-from-oracle'." in result.output

    def test_connection_update_object_storage(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-object-storage'])
        assert "Error: No such command 'update-connection-update-connection-from-object-storage'." in result.output

    def test_connection_update_atp(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-atp'])
        assert "Error: No such command 'update-connection-update-connection-from-atp'." in result.output

    def test_connection_update_adwc(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-adwc'])
        assert "Error: No such command 'update-connection-update-connection-from-adwc'." in result.output

    def test_connection_update_oracle(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-oracle'])
        assert "Error: No such command 'update-connection-update-connection-from-oracle'." in result.output

    def test_data_asset_create_object_storage(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-data-asset-create-data-asset-from-object-storage'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-object-storage'." in result.output

    def test_data_asset_create_atp(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-data-asset-create-data-asset-from-atp'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-atp'." in result.output

    def test_data_asset_create_adwc(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-data-asset-create-data-asset-from-adwc'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-adwc'." in result.output

    def test_data_asset_create_oracle(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-data-asset-create-data-asset-from-oracle'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-oracle'." in result.output

    def test_data_asset_update_object_storage(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-data-asset-update-data-asset-from-object-storage'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-object-storage'." in result.output

    def test_data_asset_update_atp(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-data-asset-update-data-asset-from-atp'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-atp'." in result.output

    def test_data_asset_update_adwc(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-data-asset-update-data-asset-from-adwc'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-adwc'." in result.output

    def test_data_asset_update_oracle(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-data-asset-update-data-asset-from-oracle'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-oracle'." in result.output

    def test_connection_create(self):
        result = util.invoke_command(['data-integration', 'connection', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'name' in result.output
        assert 'identifier' in result.output

    def test_connection_update(self):
        result = util.invoke_command(['data-integration', 'connection', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'connection-key' in result.output
        assert 'model-type' in result.output
        assert 'key' in result.output
        assert 'object-version' in result.output

    def test_data_asset_create(self):
        result = util.invoke_command(['data-integration', 'data-asset', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'model-type' in result.output
        assert 'name' in result.output
        assert 'identifier' in result.output

    def test_data_asset_update(self):
        result = util.invoke_command(['data-integration', 'data-asset', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'data-asset-key' in result.output
        assert 'model-type' in result.output
        assert 'key' in result.output
        assert 'object-version' in result.output

    def test_connection_validation_delete(self):
        result = util.invoke_command(['data-integration', 'connection-validation', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'con-validation-key' in result.output

    def test_connection_validation_get(self):
        result = util.invoke_command(['data-integration', 'connection-validation', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'con-validation-key' in result.output

    def test_data_flow_validation_delete(self):
        result = util.invoke_command(['data-integration', 'data-flow-validation', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'df-validation-key' in result.output

    def test_data_flow_validation_get(self):
        result = util.invoke_command(['data-integration', 'data-flow-validation', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert 'workspace-id' in result.output
        assert 'df-validation-key' in result.output

    def test_workspace_create(self):
        result = util.invoke_command(['data-integration', 'workspace', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert 'display-name' in result.output
        assert 'compartment-id' in result.output
        assert 'is-private-network' in result.output

    def test_task_create_entity_shape(self):
        result = util.invoke_command(['data-integration', 'data-entity', 'create-entity-shape'])
        assert "Error: No such command 'create-entity-shape'." in result.output

    def test_task_create_entity_shape_old(self):
        result = util.invoke_command(['data-integration', 'data-entity', 'create-entity-shape-create-entity-shape-from-file'])
        assert "Error: No such command 'create-entity-shape-create-entity-shape-from-file'." in result.output

    def test_task_create_entity_shape_file(self):
        result = util.invoke_command(['data-integration', 'data-entity', 'create-entity-shape-from-file'])
        assert 'workspace-id' in result.output
        assert 'connection-key' in result.output
        # assert 'schema-resource-name' in result.output

    def test_task_create(self):
        result = util.invoke_command(['data-integration', 'task', 'create'])
        assert "Error: No such command 'create'." in result.output

    def test_integration_task_old_create(self):
        result = util.invoke_command(['data-integration', 'task', 'create-task-create-task-from-integration-task'])
        assert "Error: No such command 'create-task-create-task-from-integration-task'." in result.output

    def test_integration_task_create(self):
        result = util.invoke_command(['data-integration', 'task', 'create-integration-task'])
        assert 'workspace-id' in result.output
        assert 'name' in result.output
        assert 'identifier' in result.output
        assert 'registry-metadata' in result.output

    def test_data_loader_task_old_create(self):
        result = util.invoke_command(['data-integration', 'task', 'create-task-create-task-from-data-loader-task'])
        assert "Error: No such command 'create-task-create-task-from-data-loader-task'." in result.output

    def test_data_loader_task_create(self):
        result = util.invoke_command(['data-integration', 'task', 'create-data-loader-task'])
        assert 'workspace-id' in result.output
        assert 'name' in result.output
        assert 'identifier' in result.output
        assert 'registry-metadata' in result.output

    def test_task_update(self):
        result = util.invoke_command(['data-integration', 'task', 'update'])
        assert "Error: No such command 'update'." in result.output

    def test_integration_task_old_update(self):
        result = util.invoke_command(['data-integration', 'task', 'update-task-update-task-from-integration-task'])
        assert "Error: No such command 'update-task-update-task-from-integration-task'." in result.output

    def test_integration_task_update(self):
        result = util.invoke_command(['data-integration', 'task', 'update-integration-task'])
        assert 'workspace-id' in result.output
        assert 'task-key' in result.output
        assert 'key' in result.output
        assert 'object-version' in result.output

    def test_data_loader_task_old_update(self):
        result = util.invoke_command(['data-integration', 'task', 'update_task_update_task_from_data_loader_task'])
        assert "Error: No such command 'update_task_update_task_from_data_loader_task'." in result.output

    def test_data_loader_task_update(self):
        result = util.invoke_command(['data-integration', 'task', 'update-data-loader-task'])
        assert 'workspace-id' in result.output
        assert 'task-key' in result.output
        assert 'key' in result.output
        assert 'object-version' in result.output

    def test_connection_validation_create_oracle(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-data-asset-from-oracle'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-oracle'." in result.output

    def test_connection_validation_create_adwc(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-data-asset-from-adwc'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-adwc'." in result.output

    def test_connection_validation_create_atp(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-data-asset-from-atp'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-atp'." in result.output

    def test_connection_validation_create_object_storage(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-data-asset-from-object-storage'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-object-storage'." in result.output

    def test_connection_validation_update_atp(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-connection-from-atp'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-atp'." in result.output

    def test_connection_validation_update_adwc(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-connection-from-adwc'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-adwc'." in result.output

    def test_connection_validation_update_oracle(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-connection-from-oracle'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-oracle'." in result.output

    def test_connection_validation_update_object_storage(self):
        result = util.invoke_command(['data-integration', 'task', 'create-connection-validation-create-connection-from-object-storage'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-object-storage'." in result.output

    def test_task_validation_create(self):
        result = util.invoke_command(['data-integration', 'task-validation', 'create'])
        assert "Error: No such command 'create'." in result.output

    def test_integration_task_validation_old_create(self):
        result = util.invoke_command(['data-integration', 'task-validation', 'create-task-validation-create-task-validation-from-integration-task'])
        assert "Error: No such command 'create-task-validation-create-task-validation-from-integration-task'." in result.output

    def test_integration_task_validation_create(self):
        result = util.invoke_command(['data-integration', 'task-validation', 'create-from-integration-task'])
        assert 'workspace-id' in result.output

    def test_data_loader_task_validation_old_create(self):
        result = util.invoke_command(['data-integration', 'task-validation', 'create-task-validation-create-task-validation-from-data-loader-task'])
        assert "Error: No such command 'create-task-validation-create-task-validation-from-data-loader-task'." in result.output

    def test_data_loader_task_validation_create(self):
        result = util.invoke_command(['data-integration', 'task-validation', 'create-from-data-loader-task'])
        assert 'workspace-id' in result.output

    def test_mysql_connection_create_old(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-my-sql'])
        assert "Error: No such command 'create-connection-create-connection-from-my-sql'." in result.output

    def test_jdbc_connection_create_old(self):
        result = util.invoke_command(['data-integration', 'connection', 'create-connection-create-connection-from-jdbc'])
        assert "Error: No such command 'create-connection-create-connection-from-jdbc'." in result.output

    def test_mysql_connection_update_old(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-my-sql'])
        assert "Error: No such command 'update-connection-update-connection-from-my-sql'." in result.output

    def test_jdbc_connection_update_old(self):
        result = util.invoke_command(['data-integration', 'connection', 'update-connection-update-connection-from-jdbc'])
        assert "Error: No such command 'update-connection-update-connection-from-jdbc'." in result.output

    def test_mysql_data_asset_create_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'create-data-asset-create-data-asset-from-my-sql'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-my-sql'." in result.output

    def test_jdbc_data_asset_create_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'create-data-asset-create-data-asset-from-jdbc'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-jdbc'." in result.output

    def test_mysql_data_asset_update_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'update-data-asset-update-data-asset-from-my-sql'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-my-sql'." in result.output

    def test_jdbc_data_asset_update_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'update-data-asset-update-data-asset-from-jdbc'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-jdbc'." in result.output

    def test_create_task_pipeline_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'create-task-create-task-from-pipeline-task'])
        assert "Error: No such command 'create-task-create-task-from-pipeline-task'." in result.output

    def test_create_task_validation_pipeline_old(self):
        result = util.invoke_command(
            ['data-integration', 'task-validation', 'create-task-validation-create-task-validation-from-pipeline-task'])
        assert "Error: No such command 'create-task-validation-create-task-validation-from-pipeline-task'." in result.output

    def test_update_task_pipeline_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'update-task-update-task-from-pipeline-task'])
        assert "Error: No such command 'update-task-update-task-from-pipeline-task'." in result.output

    def test_create_sql_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'create-task-create-task-from-sql-task'])
        assert "Error: No such command 'create-task-create-task-from-sql-task'." in result.output

    def test_update_sql_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'update-task-update-task-from-sql-task'])
        assert "Error: No such command 'update-task-update-task-from-sql-task'." in result.output

    def test_create_amazon_s3_connection_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection', 'create-connection-create-connection-from-amazon-s3'])
        assert "Error: No such command 'create-connection-create-connection-from-amazon-s3'." in result.output

    def test_create_bicc_connection_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection', 'create-connection-create-connection-from-bicc'])
        assert "Error: No such command 'create-connection-create-connection-from-bicc'." in result.output

    def test_update_amazon_s3_connection_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection', 'update-connection-update-connection-from-amazon-s3'])
        assert "Error: No such command 'update-connection-update-connection-from-amazon-s3'." in result.output

    def test_update_bicc_connection_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection', 'update-connection-update-connection-from-bicc'])
        assert "Error: No such command 'update-connection-update-connection-from-bicc'." in result.output

    def test_create_connection_validation_from_amazon_s3_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection-validation', 'create-connection-validation-create-connection-from-amazon-s3'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-amazon-s3'." in result.output

    def test_create_connection_validation_from_bicc_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection-validation', 'create-connection-validation-create-connection-from-bicc'])
        assert "Error: No such command 'create-connection-validation-create-connection-from-bicc'." in result.output

    def test_create_connection_validation_from_fusion_app_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection-validation', 'create-connection-validation-create-data-asset-from-fusion-app'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-fusion-app'." in result.output

    def test_create_data_asset_from_fusion_app_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'create-data-asset-create-data-asset-from-fusion-app'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-fusion-app'." in result.output

    def test_update_data_asset_from_amazon_s3_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'update-data-asset-update-data-asset-from-amazon-s3'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-amazon-s3'." in result.output

    def test_update_data_asset_from_fusion_app_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'update-data-asset-update-data-asset-from-fusion-app'])
        assert "Error: No such command 'update-data-asset-update-data-asset-from-fusion-app'." in result.output

    def test_create_daily_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'create-schedule-daily-frequency-details'])
        assert "Error: No such command 'create-schedule-daily-frequency-details'." in result.output

    def test_create_hourly_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'create-schedule-hourly-frequency-details'])
        assert "Error: No such command 'create-schedule-hourly-frequency-details'." in result.output

    def test_create_monthly_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'create-schedule-monthly-frequency-details'])
        assert "Error: No such command 'create-schedule-monthly-frequency-details'." in result.output

    def test_update_daily_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'update-schedule-daily-frequency-details'])
        assert "Error: No such command 'update-schedule-daily-frequency-details'." in result.output

    def test_update_hourly_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'update-schedule-hourly-frequency-details'])
        assert "Error: No such command 'update-schedule-hourly-frequency-details'." in result.output

    def test_update_monthly_schedule_old(self):
        result = util.invoke_command(
            ['data-integration', 'schedule', 'update-schedule-monthly-frequency-details'])
        assert "Error: No such command 'update-schedule-monthly-frequency-details'." in result.output

    def test_create_dataflow_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'create-task-create-task-from-oci-dataflow-task'])
        assert "Error: No such command 'create-task-create-task-from-oci-dataflow-task'." in result.output

    def test_update_dataflow_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'update-task-update-task-from-oci-dataflow-task'])
        assert "Error: No such command 'update-task-update-task-from-oci-dataflow-task'." in result.output

    def test_create_rest_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'create-task-create-task-from-rest-task'])
        assert "Error: No such command 'create-task-create-task-from-rest-task'." in result.output

    def test_update_rest_task_old(self):
        result = util.invoke_command(
            ['data-integration', 'task', 'update-task-update-task-from-rest-task'])
        assert "Error: No such command 'update-task-update-task-from-rest-task'." in result.output

    def test_create_connection_validation_from_amazon_s3_data_asset_old(self):
        result = util.invoke_command(
            ['data-integration', 'connection-validation', 'create-connection-validation-create-data-asset-from-amazon-s3'])
        assert "Error: No such command 'create-connection-validation-create-data-asset-from-amazon-s3'." in result.output

    def test_create_data_asset_from_amazon_s3_data_asset_old(self):
        result = util.invoke_command(
            ['data-integration', 'data-asset', 'create-data-asset-create-data-asset-from-amazon-s3'])
        assert "Error: No such command 'create-data-asset-create-data-asset-from-amazon-s3'." in result.output

    def test_create_task_create_task_from_rest_task(self):
        result = util.invoke_command(['data-integration', 'task', 'create_task_create_task_from_rest_task'])
        assert "Error: No such command 'create_task_create_task_from_rest_task'." in result.output

    def test_update_task_update_task_from_rest_task(self):
        result = util.invoke_command(['data-integration', 'task', 'update_task_update_task_from_rest_task'])
        assert "Error: No such command 'update_task_update_task_from_rest_task'." in result.output
