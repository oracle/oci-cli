# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

import base64
import json
import os
import tempfile
import unittest

import click

from tests import util
from services.functions.src.oci_cli_functions_management import functionsmanagement_cli_extended as functions_ext


# pytest -s services/functions/tests/unit/test_functions_extended.py
class TestFunctions(unittest.TestCase):

    def _assert_output_contains(self, command, expected):
        result = util.invoke_command(command)
        for item in expected:
            assert item in result.output
        return result

    def _assert_output_does_not_contain(self, command, unexpected):
        result = util.invoke_command(command)
        for item in unexpected:
            assert item not in result.output
        return result

    def _required_options(self, command):
        return sorted('--' + option.name.replace('_', '-') for option in command.params if getattr(option, 'required', False))

    def test_fn(self):
        result = self._assert_output_contains(
            ['fn'],
            [
                'application',
                'function',
                'pbf-listing',
                'pbf-listing-version',
                'runtime',
                'runtime-version',
                'trigger',
                'work-request',
                'work-request-error',
                'work-request-log-entry'
            ]
        )
        assert 'functions-runtime' not in result.output
        assert 'functions-runtime-version' not in result.output
        assert 'work-request-management' not in result.output

    def test_fn_application(self):
        self._assert_output_contains(
            ['fn', 'application'],
            ['create', 'delete', 'update', 'list', 'get', 'change-compartment']
        )

    def test_application_create(self):
        result = util.invoke_command(['fn', 'application', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--display-name' in result.output
        assert '--compartment-id' in result.output
        assert '--subnet-ids' in result.output
        result = util.invoke_command(['fn', 'application', 'create', '--config'])
        assert 'Error: Option \'--config\' requires an argument' in result.output

    def test_application_delete(self):
        result = util.invoke_command(['fn', 'application', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_application_update(self):
        result = util.invoke_command(['fn', 'application', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output
        result = util.invoke_command(['fn', 'application', 'update', '--config'])
        assert 'Error: Option \'--config\' requires an argument' in result.output

    def test_application_list(self):
        result = util.invoke_command(['fn', 'application', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_application_get(self):
        result = util.invoke_command(['fn', 'application', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_application_change_compartment(self):
        result = util.invoke_command(['fn', 'application', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--application-id' in result.output

    def test_fn_function(self):
        self._assert_output_contains(
            ['fn', 'function'],
            ['create', 'delete', 'update', 'list', 'get', 'invoke']
        )

    def test_function_create_group(self):
        self._assert_output_contains(
            ['fn', 'function', 'create'],
            ['archive-function', 'container-function', 'pbf-function']
        )

    def test_function_update_group(self):
        self._assert_output_contains(
            ['fn', 'function', 'update'],
            ['archive-function', 'container-function', 'pbf-function']
        )

    def test_function_create_archive_object_storage_fn_update_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'archive-function', 'object-storage', 'fn-update-runtime-config'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--bucket-name', '--namespace', '--object-name', '--functions-runtime-name']:
            assert option in result.output

    def test_function_create_archive_object_storage_manual_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'archive-function', 'object-storage', 'manual-runtime-config'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--bucket-name', '--namespace', '--object-name', '--functions-runtime-name', '--functions-runtime-version-id']:
            assert option in result.output

    def test_function_create_archive_direct_archive_fn_update_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'archive-function', 'direct-archive', 'fn-update-runtime-config'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--archive-file', '--functions-runtime-name']:
            assert option in result.output

    def test_function_create_archive_direct_archive_manual_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'archive-function', 'direct-archive', 'manual-runtime-config'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--archive-file', '--functions-runtime-name', '--functions-runtime-version-id']:
            assert option in result.output

    def test_function_create_container_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'container-function'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--image']:
            assert option in result.output

    def test_function_create_pbf_required_options(self):
        result = util.invoke_command(['fn', 'function', 'create', 'pbf-function'])
        assert 'Error: Missing option(s)' in result.output
        for option in ['--application-id', '--display-name', '--memory-in-mbs', '--pbf-listing-id']:
            assert option in result.output

    def test_function_update_archive_required_options(self):
        update_archive_command = functions_ext.function_update_group.commands['archive-function']
        update_archive_options = [option.opts[0] for option in update_archive_command.params if option.opts]

        for option in [
            '--bucket-name',
            '--namespace',
            '--object-name',
            '--object-version-id',
            '--functions-runtime-name',
            '--functions-runtime-version-id',
            '--archive-file',
            '--runtime-config'
        ]:
            assert option in update_archive_options

        assert '--archive-file' not in self._required_options(update_archive_command)
        assert '--runtime-config' not in self._required_options(update_archive_command)

        result = util.invoke_command(['fn', 'function', 'update', 'archive-function', '--help'])
        assert 'object-storage' not in result.output
        assert 'direct-archive' not in result.output
        assert 'fn-update-runtime-config' not in result.output
        assert 'manual-runtime-config' not in result.output

    def test_function_update_archive_runtime_validation(self):
        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--functions-runtime-name', 'java17.ol9'
        ])
        assert 'Must specify --runtime-config when using --functions-runtime-name or --functions-runtime-version-id.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--functions-runtime-version-id', 'runtime-version-id'
        ])
        assert 'Must specify --runtime-config when using --functions-runtime-name or --functions-runtime-version-id.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--runtime-config', 'FUNCTION_UPDATE'
        ])
        assert 'Must specify --functions-runtime-name when --runtime-config is FUNCTION_UPDATE.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--runtime-config', 'MANUAL'
        ])
        assert 'Must specify --functions-runtime-version-id when --runtime-config is MANUAL.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--runtime-config', 'manual'
        ])
        assert 'invalid choice' not in result.output
        assert 'Must specify --functions-runtime-version-id when --runtime-config is MANUAL.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--generate-full-command-json-input'
        ])
        assert result.exit_code == 0
        assert 'functionId' in result.output

    def test_function_update_archive_source_validation(self):
        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--bucket-name', 'bucket'
        ])
        assert 'Must specify --bucket-name, --namespace and --object-name together when using Object Storage archive options.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--object-version-id', 'version'
        ])
        assert 'Must specify --bucket-name, --namespace and --object-name together when using Object Storage archive options.' in result.output

        result = util.invoke_command([
            'fn', 'function', 'update', 'archive-function',
            '--function-id', 'fnid',
            '--archive-file', '/tmp/function.zip',
            '--bucket-name', 'bucket',
            '--namespace', 'namespace',
            '--object-name', 'object'
        ])
        assert 'Cannot specify --archive-file with Object Storage archive options' in result.output

    def test_function_update_container_and_pbf_options(self):
        container_command = functions_ext.function_update_group.commands['container-function']
        pbf_command = functions_ext.function_update_group.commands['pbf-function']

        result = util.invoke_command(['fn', 'function', 'update', 'container-function', '--generate-full-command-json-input'])
        assert result.exit_code == 0
        assert 'functionId' in result.output

        result = util.invoke_command(['fn', 'function', 'update', 'pbf-function', '--generate-full-command-json-input'])
        assert result.exit_code == 0
        assert 'functionId' in result.output

        assert '--image' not in self._required_options(container_command)

        pbf_options = [option.opts[0] for option in pbf_command.params if option.opts]
        assert '--pbf-listing-id' not in pbf_options

    def test_function_extended_commands_generate_param_json_input(self):
        for command in [
            ['fn', 'function', 'create', 'container-function'],
            ['fn', 'function', 'create', 'pbf-function'],
            ['fn', 'function', 'update', 'archive-function'],
            ['fn', 'function', 'update', 'container-function'],
            ['fn', 'function', 'update', 'pbf-function']
        ]:
            result = util.invoke_command(command + ['--generate-param-json-input', 'config'])
            assert result.exit_code == 0
            assert 'string' in result.output

            result = util.invoke_command(command + ['--generate-param-json-input', 'provisioned-concurrency'])
            assert result.exit_code == 0
            assert 'strategy' in result.output

    def test_function_delete(self):
        result = util.invoke_command(['fn', 'function', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output

    def test_function_list(self):
        result = util.invoke_command(['fn', 'function', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--application-id' in result.output

    def test_function_get(self):
        result = util.invoke_command(['fn', 'function', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output

    def test_function_invoke(self):
        result = util.invoke_command(['fn', 'function', 'invoke'])
        assert 'Error: Missing option(s)' in result.output
        assert '--function-id' in result.output
        assert '--body' in result.output
        assert '--file' in result.output
        result = util.invoke_command(['fn', 'function', 'invoke', '--fn-intent', 'x'])
        assert "Error: Invalid value for '--fn-intent': invalid choice: x. (choose from httprequest, cloudevent)" in result.output
        result = util.invoke_command(['fn', 'function', 'invoke', '--fn-invoke-type', 'x'])
        assert "Error: Invalid value for '--fn-invoke-type': invalid choice: x. (choose from detached, sync)" in result.output

    def test_fn_runtime(self):
        self._assert_output_contains(['fn', 'runtime'], ['get', 'list'])

    def test_fn_runtime_version(self):
        self._assert_output_contains(['fn', 'runtime-version'], ['get', 'list'])

    def test_fn_work_request(self):
        result = self._assert_output_contains(['fn', 'work-request'], ['get', 'list'])
        assert 'cancel' not in result.output

    def test_fn_work_request_error(self):
        self._assert_output_contains(['fn', 'work-request-error'], ['list'])

    def test_fn_work_request_log_entry(self):
        result = self._assert_output_contains(['fn', 'work-request-log-entry'], ['list'])
        assert 'list-work-request-logs' not in result.output

    def test_fn_pbf_listing(self):
        self._assert_output_contains(['fn', 'pbf-listing'], ['get', 'list'])

    def test_fn_pbf_listing_get(self):
        result = util.invoke_command(['fn', 'pbf-listing', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--pbf-listing-id' in result.output

    def test_fn_pbf_listing_version(self):
        self._assert_output_contains(['fn', 'pbf-listing-version'], ['get', 'list'])

    def test_fn_pbf_listing_version_get(self):
        result = util.invoke_command(['fn', 'pbf-listing-version', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--pbf-listing-version-id' in result.output

    def test_fn_pbf_listing_version_list(self):
        result = util.invoke_command(['fn', 'pbf-listing-version', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--pbf-listing-id' in result.output

    def test_fn_trigger(self):
        self._assert_output_contains(['fn', 'trigger'], ['list'])

    def test_archive_update_omits_empty_archive_source_details(self):
        object_storage_payload = functions_ext._build_archive_source_details(
            functions_ext._build_object_storage_archive_details({
                'bucket_name': None,
                'namespace': None,
                'object_name': None,
                'object_version_id': None
            }, include_if_empty=False),
            functions_ext._build_fn_update_runtime_config({'functions_runtime_name': 'python312.ol9'}),
            {'handler': None}
        )
        assert object_storage_payload == {
            'sourceType': 'ARCHIVE',
            'runtimeConfig': {
                'runtimeConfigType': 'FUNCTION_UPDATE',
                'functionsRuntimeName': 'python312.ol9'
            }
        }

        direct_archive_payload = functions_ext._build_archive_source_details(
            functions_ext._build_direct_archive_details({'archive_file': None}, include_if_empty=False),
            functions_ext._build_fn_update_runtime_config({'functions_runtime_name': 'python312.ol9'}),
            {'handler': None}
        )
        assert direct_archive_payload == {
            'sourceType': 'ARCHIVE',
            'runtimeConfig': {
                'runtimeConfigType': 'FUNCTION_UPDATE',
                'functionsRuntimeName': 'python312.ol9'
            }
        }

    def test_update_archive_function_builds_object_storage_payload(self):
        update_archive_command = functions_ext.function_update_group.commands['archive-function']
        captured = {}

        class DummyCtx(click.Context):
            def invoke(self, command, **kwargs):
                captured['command'] = command.name
                captured['kwargs'] = kwargs

        with DummyCtx(update_archive_command, obj={
            'debug': False,
            'parameter_aliases': {},
            'parameter_lookup_heirarchy': [],
            'generate_full_command_json_input': None,
            'generate_param_json_input': None,
            'default_values_from_file': {}
        }):
            functions_ext.update_archive_function.callback(
                function_id='fnid',
                bucket_name='bucket',
                namespace='namespace',
                object_name='function.zip',
                object_version_id='version',
                archive_file=None,
                runtime_config='MANUAL',
                functions_runtime_name=None,
                functions_runtime_version_id='runtime-version-id',
                handler='handler.entrypoint',
                memory_in_mbs=1024,
                provisioned_concurrency=None
            )

        source_details = json.loads(captured['kwargs']['source_details'])
        assert source_details == {
            'sourceType': 'ARCHIVE',
            'archiveSourceDetails': {
                'archiveSourceType': 'OBJECT_STORAGE_ARCHIVE',
                'bucketName': 'bucket',
                'namespace': 'namespace',
                'objectName': 'function.zip',
                'objectVersionId': 'version'
            },
            'runtimeConfig': {
                'runtimeConfigType': 'MANUAL',
                'functionsRuntimeVersionId': 'runtime-version-id'
            },
            'handler': 'handler.entrypoint'
        }
        assert captured['kwargs']['function_id'] == 'fnid'

    def test_update_archive_function_builds_direct_archive_payload(self):
        update_archive_command = functions_ext.function_update_group.commands['archive-function']
        captured = {}

        class DummyCtx(click.Context):
            def invoke(self, command, **kwargs):
                captured['command'] = command.name
                captured['kwargs'] = kwargs

        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
            temp_zip.write(b'ZIP_BYTES')
            zip_path = temp_zip.name

        try:
            with DummyCtx(update_archive_command, obj={
                'debug': False,
                'parameter_aliases': {},
                'parameter_lookup_heirarchy': [],
                'generate_full_command_json_input': None,
                'generate_param_json_input': None,
                'default_values_from_file': {}
            }):
                functions_ext.update_archive_function.callback(
                    function_id='fnid',
                    bucket_name=None,
                    namespace=None,
                    object_name=None,
                    object_version_id=None,
                    archive_file=zip_path,
                    runtime_config='FUNCTION_UPDATE',
                    functions_runtime_name='python312.ol9',
                    functions_runtime_version_id=None,
                    handler=None,
                    memory_in_mbs=1024,
                    provisioned_concurrency=None
                )
        finally:
            os.remove(zip_path)

        source_details = json.loads(captured['kwargs']['source_details'])
        assert source_details == {
            'sourceType': 'ARCHIVE',
            'archiveSourceDetails': {
                'archiveSourceType': 'DIRECT_ARCHIVE',
                'archiveFile': base64.b64encode(b'ZIP_BYTES').decode('utf-8')
            },
            'runtimeConfig': {
                'runtimeConfigType': 'FUNCTION_UPDATE',
                'functionsRuntimeName': 'python312.ol9'
            }
        }

    def test_direct_archive_file_encodes_zip_and_jar_paths(self):
        with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
            temp_zip.write(b'ZIP_BYTES')
            zip_path = temp_zip.name
        with tempfile.NamedTemporaryFile(suffix='.jar', delete=False) as temp_jar:
            temp_jar.write(b'JAR_BYTES')
            jar_path = temp_jar.name
        try:
            from_zip = functions_ext._build_direct_archive_details({'archive_file': zip_path})
            assert from_zip == {
                'archiveSourceType': 'DIRECT_ARCHIVE',
                'archiveFile': base64.b64encode(b'ZIP_BYTES').decode('utf-8')
            }

            from_file_uri = functions_ext._build_direct_archive_details({'archive_file': 'file://' + zip_path})
            assert from_file_uri == {
                'archiveSourceType': 'DIRECT_ARCHIVE',
                'archiveFile': base64.b64encode(b'ZIP_BYTES').decode('utf-8')
            }

            from_jar = functions_ext._build_direct_archive_details({'archive_file': jar_path})
            assert from_jar == {
                'archiveSourceType': 'DIRECT_ARCHIVE',
                'archiveFile': base64.b64encode(b'JAR_BYTES').decode('utf-8')
            }
        finally:
            os.remove(zip_path)
            os.remove(jar_path)

    def test_direct_archive_file_rejects_invalid_path_and_extension(self):
        try:
            functions_ext._build_direct_archive_details({'archive_file': '/tmp/non-existent-function-archive.zip'})
            assert False, 'Expected UsageError for missing archive file'
        except click.UsageError as error:
            assert "does not exist" in str(error)

        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_txt:
            temp_txt.write(b'NOT_ARCHIVE')
            txt_path = temp_txt.name
        try:
            functions_ext._build_direct_archive_details({'archive_file': txt_path})
            assert False, 'Expected UsageError for unsupported archive extension'
        except click.UsageError as error:
            assert 'must be a .zip or .jar file' in str(error)
        finally:
            os.remove(txt_path)

    def test_pbf_update_does_not_send_source_details(self):
        pbf_command = functions_ext.function_update_group.commands['pbf-function']
        captured = {}

        class DummyCtx(click.Context):
            def invoke(self, command, **kwargs):
                captured['command'] = command.name
                captured['kwargs'] = kwargs

        with DummyCtx(pbf_command, obj={
            'debug': False,
            'parameter_aliases': {},
            'parameter_lookup_heirarchy': [],
            'generate_full_command_json_input': None,
            'generate_param_json_input': None,
            'default_values_from_file': {}
        }):
            functions_ext.update_pbf_function.callback(
                function_id='fnid',
                memory_in_mbs=1024,
                provisioned_concurrency=None
            )

        assert 'source_details' not in captured['kwargs']
        assert captured['kwargs']['function_id'] == 'fnid'
        assert captured['kwargs']['memory_in_mbs'] == 1024
