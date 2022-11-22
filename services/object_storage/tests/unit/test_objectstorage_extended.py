# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import hashlib
import mock
import unittest
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import time_delta
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import ProgressBar
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import _get_progress_bar_label
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import _get_encryption_key_params
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import _get_source_encryption_key_params
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import _get_sse_customer_key_details
import oci_cli
from tests import util
import tempfile
import shutil
import os


class TestObjectStorage(unittest.TestCase):
    def setUp(self):
        pass

    def test_time_delta(self):
        assert time_delta(0, 34) == 'less than 1 minute'
        assert time_delta(0, 60 * 60) == '0 days 1 hour 0 mins'
        assert time_delta(1, 0) == '1 day 0 hours 0 mins'
        assert time_delta(2, 12840) == '2 days 3 hours 34 mins'

    @mock.patch('click.termui.get_terminal_size')
    def test_get_progress_bar_label(self, mock_click):
        mock_click.return_value = (40, 80)
        str_long_slash = '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0' \
                         '123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF/'
        str_long = '0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456' \
                   '789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF'
        str_normal = 'filename'
        assert _get_progress_bar_label('', str_long_slash, 'Deleted') == 'Deleted item'
        assert _get_progress_bar_label('', str_long, 'Deleted') == 'Deleted item'
        assert _get_progress_bar_label('', str_normal, 'Deleted') == 'Deleted filename'

    def test_progressbar_empty_file(self):
        total_size = 0
        bar = ProgressBar(total_size, 'Empty file!')
        bar.update(total_size)
        bar.update_label_to_end('Finished')
        assert bar._progressbar.finished

    def test_progressbar_update(self):
        total_size = 100
        bar = ProgressBar(total_size, 'Upload file!')
        bar.update(50)
        bar.update(50)
        assert bar._progressbar.finished

    def test_verify_checksum(self):
        td = tempfile.mkdtemp()
        tf = tempfile.NamedTemporaryFile(dir=td, delete=False)
        tmp_file_name = tf.name
        tf.close()
        result = util.invoke_command(['os', 'object', 'put', '--bucket-name', 'test', '--file', tmp_file_name, '--verify-checksum', '--force'])
        assert "ServiceError" in result.output
        assert "BucketNotFound" in result.output
        result = util.invoke_command(['os', 'object', 'bulk-upload', '--bucket-name', 'test', '--src-dir', td, '--verify-checksum'])
        assert "ServiceError" in result.output
        assert "BucketNotFound" in result.output
        os.unlink(tmp_file_name)
        shutil.rmtree(td)

    def test_verify_namespace_name_param(self):
        """ Checks whether all object storage commands have the namespace-name parameter """
        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            for param in command.params:
                if any(p in param.opts for p in ['-ns', '--namespace', '--namespace-name']):
                    print(command.parent.name, command.name, param.opts)
                    assert '-ns' in param.opts
                    assert '--namespace' in param.opts
                    assert '--namespace-name' in param.opts
                if any(p in param.opts for p in ['-bn', '--bucket-name']):
                    print(command.parent.name, command.name, param.opts)
                    assert '-bn' in param.opts
                    assert '--bucket-name' in param.opts

    def test_verify_encryption_key_autogen_params_hidden(self):
        """ Checks whether the auto generated sse encryption key params are masked out """
        sse_param_suffixes = ['sse-customer-algorithm', 'sse-customer-key', 'sse-customer-key-sha256']
        encryption_key_params = ['opc-' + p for p in sse_param_suffixes] + \
                                ['opc-source-' + p for p in sse_param_suffixes] + \
                                ['sse-customer-key', 'source-sse-customer-key']
        results = {}
        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            for param in command.params:
                if any(p in param.opts for p in encryption_key_params):
                    key = command.parent.name + ' ' + command.name
                    results[key] = True
        assert list(results.keys()) == []

    def test_verify_encryption_key_file_params(self):
        """ Checks whether the encryption-key-file params are present for the relevant object commands """
        # Sorted lists of commands that should support --encryption-key-file and --source-encryption-file respectively
        encryption_key_file_cmd_list = sorted([
            'object put', 'object bulk-upload', 'object get', 'object bulk-download', 'object head',
            'object copy', 'object reencrypt', 'object sync'
        ])
        source_encryption_key_file_cmd_list = sorted(['object copy', 'object reencrypt'])

        # dictionary that holds the result of parsing the various commands looking for --encryption-key-file
        encryption_key_file_results = {}
        # dictionary that holds the result of parsing the various commands looking for --source-encryption-key-file
        source_encryption_key_file_results = {}
        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            key = command.parent.name + ' ' + command.name
            for param in command.params:
                if '--encryption-key-file' in param.opts:
                    encryption_key_file_results[key] = True
                if '--source-encryption-key-file' in param.opts:
                    source_encryption_key_file_results[key] = True
        assert sorted(list(encryption_key_file_results.keys())) == encryption_key_file_cmd_list
        assert sorted(list(source_encryption_key_file_results.keys())) == source_encryption_key_file_cmd_list

    def test_verify_ssec_kms_params(self):
        """ Checks whether the opc-sse-kms-key-id params are present for the relevant object commands """
        # Sorted lists of commands that should support --opc-sse-kms-key-id
        ssec_kms_cmd_list = sorted(['object put', 'object bulk-upload', 'object copy'])

        # dictionary that holds the result of parsing the various commands looking for --opc-sse-kms-key-id
        ssec_kms_cmd_results = {}
        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            key = command.parent.name + ' ' + command.name
            for param in command.params:
                if '--opc-sse-kms-key-id' in param.opts:
                    ssec_kms_cmd_results[key] = True
        assert sorted(list(ssec_kms_cmd_results.keys())) == ssec_kms_cmd_list

    def test_get_encryption_key_params(self):
        # create a random 32 byte array to represent an AES256 key and compute its SHA256 checksum
        test_key_bytes = os.urandom(32)
        test_key_b64_str = base64.b64encode(test_key_bytes).decode("utf-8")
        test_key_sha256 = base64.b64encode(hashlib.sha256(test_key_bytes).digest()).decode("utf-8")
        # Write the base64-encoded key into a file
        td = tempfile.mkdtemp()
        tf = tempfile.NamedTemporaryFile(mode="w", dir=td, delete=False)
        tmp_file_name = tf.name
        tf.write(test_key_b64_str)
        tf.close()

        tf = open(tmp_file_name, 'r')
        params = _get_encryption_key_params(tf)

        # Verify that the required key/value pairs are present
        assert len(params) == 3
        assert 'opc_sse_customer_key_sha256' in params
        assert 'opc_sse_customer_key' in params
        assert 'opc_sse_customer_algorithm' in params
        assert params['opc_sse_customer_algorithm'] == 'AES256'
        assert params['opc_sse_customer_key'] == test_key_b64_str
        assert params['opc_sse_customer_key_sha256'] == test_key_sha256

        # Verify the JSON payload needed for 'object reencrypt'
        sse_customer_key_details = _get_sse_customer_key_details(tf)
        assert len(sse_customer_key_details) == 3
        assert 'algorithm' in sse_customer_key_details
        assert 'key' in sse_customer_key_details
        assert 'keySha256' in sse_customer_key_details

        tf.close()
        os.unlink(tmp_file_name)
        shutil.rmtree(td)

    def test_get_source_encryption_key_params(self):
        # create a random 32 byte array to represent an AES256 key and compute its SHA256 checksum
        test_key_bytes = os.urandom(32)
        test_key_b64_str = base64.b64encode(test_key_bytes).decode("utf-8")
        test_key_sha256 = base64.b64encode(hashlib.sha256(test_key_bytes).digest()).decode("utf-8")
        # Write the base64-encoded key into a file
        td = tempfile.mkdtemp()
        tf = tempfile.NamedTemporaryFile(mode="w", dir=td, delete=False)
        tmp_file_name = tf.name
        tf.write(test_key_b64_str)
        tf.close()

        tf = open(tmp_file_name, 'r')
        params = _get_source_encryption_key_params(tf)

        # Verify that the required key/value pairs are present
        assert len(params) == 3
        assert 'opc_source_sse_customer_key_sha256' in params
        assert 'opc_source_sse_customer_key' in params
        assert 'opc_source_sse_customer_algorithm' in params
        assert params['opc_source_sse_customer_algorithm'] == 'AES256'
        assert params['opc_source_sse_customer_key'] == test_key_b64_str
        assert params['opc_source_sse_customer_key_sha256'] == test_key_sha256
        tf.close()
        os.unlink(tmp_file_name)
        shutil.rmtree(td)

    def test_create_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'create-replication-policy'])
        assert "Error: Missing option(s)" in result.output
        assert "bucket-name" in result.output
        assert "destination-bucket" in result.output
        assert "destination-region" in result.output
        assert "name" in result.output

    def test_retention_rule_params(self):
        """ Checks whether the time-amount and time-unit params are present for the relevant retention-rule commands """
        # Sorted lists of commands that should support --time-amount and --time-unit
        retention_duration_cmd_list = sorted([
            'retention-rule create', 'retention-rule update'
        ])

        retention_time_amount_param_results = {}
        retention_time_unit_param_results = {}
        retention_duration_param_results = {}

        commands = oci_cli.cli_util.collect_commands(oci_cli.cli_root.cli.commands.get('os'))
        for command in commands:
            key = command.parent.name + ' ' + command.name
            if key in retention_duration_cmd_list:
                for param in command.params:
                    if '--time-amount' in param.opts:
                        retention_time_amount_param_results[key] = True
                    if '--time-unit' in param.opts:
                        retention_time_unit_param_results[key] = True
                    if '--duration' in param.opts:
                        retention_duration_param_results[key] = True
        assert sorted(list(retention_time_amount_param_results.keys())) == retention_duration_cmd_list
        assert sorted(list(retention_time_unit_param_results.keys())) == retention_duration_cmd_list
        assert len(retention_duration_param_results) == 0

    def test_create_retention_rule(self):
        result = util.invoke_command(['os', 'retention-rule', 'create'])
        assert "Error: Missing option(s)" in result.output
        assert "--bucket-name" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'create', '--bucket-name', 'b001', '--namespace-name', 'n001', '--time-amount', '1'])
        assert "UsageError: Parameter --time-unit is required" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'create', '--bucket-name', 'b001', '--namespace-name', 'n001', '--time-amount', '1', '--time-unit', 'INVALID_UNIT'])
        assert "Error: Invalid value" in result.output
        assert "invalid choice: INVALID_UNIT" in result.output

    def test_update_retention_rule(self):
        result = util.invoke_command(['os', 'retention-rule', 'update'])
        assert "Error: Missing option(s)" in result.output
        assert "--bucket-name" in result.output
        assert "--retention-rule-id" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', '1'])
        assert "UsageError: Parameter --time-unit is required" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', '1', '--time-unit', 'INVALID_UNIT'])
        assert "Error: Invalid value" in result.output
        assert "invalid choice: INVALID_UNIT" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-amount', 'abc'])
        assert "BadParameter:" in result.output
        assert "is not a valid integer" in result.output

        result = util.invoke_command(['os', 'retention-rule', 'update', '--bucket-name', 'b001', '--namespace-name', 'n001', '--retention-rule-id', 'r001', '--time-rule-locked', 'abc'])
        assert "BadParameter:" in result.output
        assert "is not in a supported datetime format" in result.output

    def test_bucket_create(self):
        result = util.invoke_command(['os', 'bucket', 'create'])
        assert "Error: Missing option(s) --name, --compartment-id" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--defined-tags', '{"Operations": {"CostCenter": 2*3}}'])
        assert "Parameter 'defined_tags' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--freeform-tags', '{"Operations": {"CostCenter": 2*3}}'])
        assert "Parameter 'freeform_tags' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--metadata', '{"Key": 2*3}'])
        assert "Parameter 'metadata' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--public-access-type', 'new-access-type'])
        assert "Error: Invalid value for '--public-access-type': invalid choice: new-access-type. (choose from NoPublicAccess, ObjectRead, ObjectReadWithoutList)" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--storage-tier', 'new-tier'])
        assert "Error: Invalid value for '--storage-tier': invalid choice: new-tier. (choose from Standard, Archive)" in result.output

        result = util.invoke_command(['os', 'bucket', 'create', '--name', 'b001', '--compartment-id', 'c001', '--versioning', 'new-version'])
        assert "Error: Invalid value for '--versioning': invalid choice: new-version. (choose from Enabled, Disabled)" in result.output

    def test_bucket_delete(self):
        result = util.invoke_command(['os', 'bucket', 'delete'])
        assert "Error: Missing option(s) --bucket-name" in result.output

    def test_bucket_get(self):
        result = util.invoke_command(['os', 'bucket', 'get'])
        assert "Error: Missing option(s) --bucket-name" in result.output

        result = util.invoke_command(['os', 'bucket', 'get', '--bucket-name', 'b001', '--fields', 'approximateCount', '--fields', 'apprxSize'])
        assert "Error: Invalid value for '--fields': invalid choice: apprxSize. (choose from approximateCount, approximateSize, autoTiering)" in result.output

    def test_bucket_list(self):
        result = util.invoke_command(['os', 'bucket', 'list'])
        assert "Error: Missing option(s) --compartment-id" in result.output

        result = util.invoke_command(['os', 'bucket', 'list', '--compartment-id', 'c001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

        result = util.invoke_command(['os', 'bucket', 'list', '--compartment-id', 'c001', '--fields', 'new-field'])
        assert "Error: Invalid value for '--fields': invalid choice: new-field. (choose from tags)" in result.output

    def test_bucket_reencrypt(self):
        result = util.invoke_command(['os', 'bucket', 'reencrypt'])
        assert "Error: Missing option(s) --bucket-name" in result.output

        result = util.invoke_command(['os', 'bucket', 'reencrypt', '--bucket-name', 'b001', '--wait-for-state', 'new-state'])
        assert "Error: Invalid value for '--wait-for-state': invalid choice: new-state. (choose from ACCEPTED, IN_PROGRESS, FAILED, COMPLETED, CANCELING, CANCELED)" in result.output

    def test_bucket_update(self):
        result = util.invoke_command(['os', 'bucket', 'update'])
        assert "Error: Missing option(s) --bucket-name" in result.output

        result = util.invoke_command(['os', 'bucket', 'update', '--name', 'b001', '--defined-tags', '{"Operations": {"CostCenter": 2*3}}'])
        assert "Parameter 'defined_tags' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'update', '--name', 'b001', '--freeform-tags', '{"Operations": {"CostCenter": 2*3}}'])
        assert "Parameter 'freeform_tags' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'update', '--name', 'b001', '--metadata', '{"Key": 2*3}'])
        assert "Parameter 'metadata' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'bucket', 'update', '--name', 'b001', '--public-access-type', 'new-access-type'])
        assert "Error: Invalid value for '--public-access-type': invalid choice: new-access-type. (choose from NoPublicAccess, ObjectRead, ObjectReadWithoutList)" in result.output

        result = util.invoke_command(['os', 'bucket', 'update', '--name', 'b001', '--versioning', 'new-version'])
        assert "Error: Invalid value for '--versioning': invalid choice: new-version. (choose from Enabled, Suspended)" in result.output

    def test_multipart_abort(self):
        result = util.invoke_command(['os', 'multipart', 'abort'])
        assert "Error: Missing option(s) --bucket-name, --object-name, --upload-id." in result.output

    def test_multipart_list(self):
        result = util.invoke_command(['os', 'multipart', 'list'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'multipart', 'list', '--bucket-name', 'b001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_object_bulk_delete(self):
        result = util.invoke_command(['os', 'object', 'bulk-delete'])
        assert "Error: Missing option(s) --bucket-name." in result.output

    def test_object_bulk_delete_versions(self):
        result = util.invoke_command(['os', 'object', 'bulk-delete-versions'])
        assert "Error: Missing option(s) --bucket-name." in result.output

    def test_object_bulk_download(self):
        result = util.invoke_command(['os', 'object', 'bulk-download'])
        assert "Error: Missing option(s) --bucket-name, --download-dir." in result.output

    def test_object_copy(self):
        result = util.invoke_command(['os', 'object', 'copy'])
        assert "Error: Missing option(s) --bucket-name, --source-object-name, --destination-bucket." in result.output

        result = util.invoke_command(['os', 'object', 'copy', '--bucket-name', 'b001', '--destination-bucket', 'b002', '--source-object-name', 'o001', '--destination-object-metadata', '{"Key": 2*3}'])
        assert "Parameter 'destination_object_metadata' must be in JSON format" in result.output

        result = util.invoke_command(['os', 'object', 'copy', '--bucket-name', 'b001', '--destination-bucket', 'b002', '--source-object-name', 'o001', '--destination-object-storage-tier', 'new-tier'])
        assert "Error: Invalid value for '--destination-object-storage-tier': invalid choice: new-tier. (choose from Standard, InfrequentAccess, Archive)" in result.output

    def test_object_delete(self):
        result = util.invoke_command(['os', 'object', 'delete'])
        assert "Error: Missing option(s) --bucket-name, --object-name." in result.output

    def test_object_get(self):
        result = util.invoke_command(['os', 'object', 'get'])
        assert "Error: Missing option(s) --bucket-name, --name, --file." in result.output

    def test_object_head(self):
        result = util.invoke_command(['os', 'object', 'head'])
        assert "Error: Missing option(s) --bucket-name, --name." in result.output

    def test_object_list(self):
        result = util.invoke_command(['os', 'object', 'list'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'object', 'list', '--bucket-name', 'b001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_object_list_object_versions(self):
        result = util.invoke_command(['os', 'object', 'list-object-versions'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'object', 'list-object-versions', '--bucket-name', 'b001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_object_put(self):
        result = util.invoke_command(['os', 'object', 'put'])
        assert "Error: Missing option(s) --bucket-name, --file." in result.output

        put_file_path = 'tests/resources/content_input.txt'
        result = util.invoke_command(['os', 'object', 'put', '--bucket-name', 'b001', '--file', put_file_path, '--metadata', '{"Key": 2*3}'])
        assert "Parameter 'metadata' must be in JSON format." in result.output

        result = util.invoke_command(['os', 'object', 'put', '--bucket-name', 'b001', '--file', put_file_path, '--storage-tier', 'new-tier'])
        assert "Error: Invalid value for '--storage-tier': invalid choice: new-tier. (choose from Standard, InfrequentAccess, Archive)" in result.output

    def test_object_reencrypt(self):
        result = util.invoke_command(['os', 'object', 'reencrypt'])
        assert "Error: Missing option(s) --bucket-name, --object-name." in result.output

    def test_object_rename(self):
        result = util.invoke_command(['os', 'object', 'rename'])
        assert "Error: Missing option(s) --bucket-name, --source-name, --new-name." in result.output

    def test_object_restore(self):
        result = util.invoke_command(['os', 'object', 'restore'])
        assert "Error: Missing option(s) --bucket-name, --name." in result.output

    def test_object_restore_status(self):
        result = util.invoke_command(['os', 'object', 'restore-status'])
        assert "Error: Missing option(s) --bucket-name, --name." in result.output

    def test_object_resume_put(self):
        result = util.invoke_command(['os', 'object', 'resume-put'])
        assert "Error: Missing option(s) --bucket-name, --file, --upload-id." in result.output

    def test_object_sync(self):
        result = util.invoke_command(['os', 'object', 'sync'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'object', 'sync', '--bucket-name', 'b001', '--src-dir', 'd001', '--metadata', '{"Key": "Value"}'])
        assert "UsageError: The specified --src-dir d001 (expanded to: d001) does not exist" in result.output

        result = util.invoke_command(['os', 'object', 'sync', '--bucket-name', 'b001', '--dest-dir', 'd001', '--metadata', '{"Key": "Value"}'])
        assert "UsageError: Option --metadata cannot be specified with --dest-dir" in result.output

        result = util.invoke_command(['os', 'object', 'sync', '--bucket-name', 'b001', '--metadata', '{"Key": "Value"}'])
        assert "UsageError: Either --src-dir or --dest-dir options must be specified" in result.output

        result = util.invoke_command(['os', 'object', 'sync', '--bucket-name', 'b001', '--storage-tier', 'new-tier'])
        assert "Error: Invalid value for '--storage-tier': invalid choice: new-tier. (choose from Standard, InfrequentAccess, Archive)" in result.output

    def test_object_update_storage_tier(self):
        result = util.invoke_command(['os', 'object', 'update-storage-tier'])
        assert "Error: Missing option(s) --bucket-name, --object-name, --storage-tier." in result.output

        result = util.invoke_command(['os', 'object', 'update-storage-tier', '--bucket-name', 'b001', '--object-name', 'o001', '--storage-tier', 'new-tier'])
        assert "Error: Invalid value for '--storage-tier': invalid choice: new-tier. (choose from Standard, InfrequentAccess, Archive)" in result.output

    def test_object_lifecycle_policy_delete(self):
        result = util.invoke_command(['os', 'object-lifecycle-policy', 'delete'])
        assert "Error: Missing option(s) --bucket-name." in result.output

    def test_object_lifecycle_policy_get(self):
        result = util.invoke_command(['os', 'object-lifecycle-policy', 'get'])
        assert "Error: Missing option(s) --bucket-name." in result.output

    def test_object_lifecycle_policy_put(self):
        result = util.invoke_command(['os', 'object-lifecycle-policy', 'put'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'object-lifecycle-policy', 'put', '--bucket-name', 'b001', '--items', '{"key": 2*3}', '--force'])
        assert "Parameter 'items' must be in JSON format." in result.output

    def test_preauth_request_create(self):
        result = util.invoke_command(['os', 'preauth-request', 'create'])
        assert "Error: Missing option(s) --bucket-name, --name, --access-type, --time-expires." in result.output

        result = util.invoke_command(['os', 'preauth-request', 'create', '--bucket-name', 'b001', '--name', 'par', '--access-type', 'new-access', '--time-expires', '2017-09-15T20:30:00.123456Z'])
        assert "Error: Invalid value for '--access-type': invalid choice: new-access." in result.output

    def test_preauth_request_delete(self):
        result = util.invoke_command(['os', 'preauth-request', 'delete'])
        assert "Error: Missing option(s) --bucket-name, --par-id." in result.output

    def test_preauth_request_get(self):
        result = util.invoke_command(['os', 'preauth-request', 'get'])
        assert "Error: Missing option(s) --bucket-name, --par-id." in result.output

    def test_preauth_request_list(self):
        result = util.invoke_command(['os', 'preauth-request', 'list'])
        assert "Error: Missing option(s) --bucket-name." in result.output

        result = util.invoke_command(['os', 'preauth-request', 'list', '--bucket-name', 'b001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_replication_create_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'create-replication-policy'])
        assert "Error: Missing option(s) --bucket-name, --name, --destination-region, --destination-bucket." in result.output

    def test_replication_delete_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'delete-replication-policy'])
        assert "Error: Missing option(s) --bucket-name, --replication-id" in result.output

    def test_replication_get_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'get-replication-policy'])
        assert "Error: Missing option(s) --bucket-name, --replication-id" in result.output

    def test_replication_list_replication_policy(self):
        result = util.invoke_command(['os', 'replication', 'list-replication-sources'])
        assert "Error: Missing option(s) --bucket-name" in result.output

        result = util.invoke_command(['os', 'replication', 'list-replication-sources', '--bucket-name', 'b001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_replication_make_bucket_writable(self):
        result = util.invoke_command(['os', 'replication', 'make-bucket-writable'])
        assert "Error: Missing option(s) --bucket-name" in result.output

    def test_retention_rule_create(self):
        result = util.invoke_command(['os', 'retention-rule', 'create'])
        assert "Error: Missing option(s) --bucket-name" in result.output

    def test_retention_rule_delete(self):
        result = util.invoke_command(['os', 'retention-rule', 'delete'])
        assert "Error: Missing option(s) --bucket-name, --retention-rule-id" in result.output

    def test_retention_rule_get(self):
        result = util.invoke_command(['os', 'retention-rule', 'get'])
        assert "Error: Missing option(s) --bucket-name, --retention-rule-id" in result.output

    def test_retention_rule_list(self):
        result = util.invoke_command(['os', 'retention-rule', 'list'])
        assert "Error: Missing option(s) --bucket-name" in result.output

    def test_retention_rule_update(self):
        result = util.invoke_command(['os', 'retention-rule', 'update'])
        assert "Error: Missing option(s) --bucket-name, --retention-rule-id" in result.output

    def test_work_request_cancel(self):
        result = util.invoke_command(['os', 'work-request', 'cancel'])
        assert "Error: Missing option(s) --work-request-id" in result.output

    def test_work_request_get(self):
        result = util.invoke_command(['os', 'work-request', 'get'])
        assert "Error: Missing option(s) --work-request-id" in result.output

    def test_work_request_list(self):
        result = util.invoke_command(['os', 'work-request', 'list'])
        assert "Error: Missing option(s) --compartment-id" in result.output

        result = util.invoke_command(['os', 'work-request', 'list', '--compartment-id', 'c001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_work_request_error_list(self):
        result = util.invoke_command(['os', 'work-request-error', 'list'])
        assert "Error: Missing option(s) --work-request-id" in result.output

        result = util.invoke_command(['os', 'work-request-error', 'list', '--work-request-id', 'wri001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output

    def test_work_request_log_entry_list(self):
        result = util.invoke_command(['os', 'work-request-log-entry', 'list'])
        assert "Error: Missing option(s) --work-request-id" in result.output

        result = util.invoke_command(['os', 'work-request-log-entry', 'list', '--work-request-id', 'wr001', '--all', '--limit', '4'])
        assert "UsageError: If you provide the --all option you cannot provide the --limit option" in result.output
