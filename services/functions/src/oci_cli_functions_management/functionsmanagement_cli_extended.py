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

import click
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from services.functions.src.oci_cli_functions_management.generated import functionsmanagement_cli


BUCKET_NAME_HELP = 'The name of the Object Storage bucket.'
NAMESPACE_HELP = 'The Object Storage namespace.'
OBJECT_NAME_HELP = 'The name of the Object Storage object.'
OBJECT_VERSION_ID_HELP = 'VersionId used to identify a particular version of the object.'
FUNCTIONS_RUNTIME_NAME_HELP = 'The name of the FunctionsRuntime this function is associated with.'
FUNCTIONS_RUNTIME_VERSION_ID_HELP = 'The OCID of the FunctionsRuntime version used when runtime config type is MANUAL.'
RUNTIME_CONFIG_HELP = 'The runtime configuration type to use for this archive function. Accepted values are: FUNCTION_UPDATE, MANUAL.'
HANDLER_HELP = 'The function handler that is executed when the function is invoked.'
ARCHIVE_FILE_HELP = 'Path to the .zip or .jar archive file of the function code.'
IMAGE_HELP = 'The full path to the Docker image for a container-image function.'
IMAGE_DIGEST_HELP = 'An optional digest for the Docker image.'
PBF_LISTING_ID_HELP = 'The OCID of the pre-built function listing.'
PROVISIONED_CONCURRENCY_HELP = 'Provisioned concurrency configuration for this function.'
ARCHIVE_FUNCTION_GROUP_HELP = 'Commands for functions created from archive sources.'
OBJECT_STORAGE_ARCHIVE_GROUP_HELP = 'Commands for functions using an archive stored in Object Storage.'
DIRECT_ARCHIVE_GROUP_HELP = 'Commands for functions using a directly provided archive file.'

RUNTIME_CONFIG_FUNCTION_UPDATE = 'FUNCTION_UPDATE'
RUNTIME_CONFIG_MANUAL = 'MANUAL'


FUNCTION_COMPLEX_TYPES = {
    'config': {'module': 'functions', 'class': 'dict(str, string)'},
    'provisioned-concurrency': {'module': 'functions', 'class': 'FunctionProvisionedConcurrencyConfig'},
    'failure-destination': {'module': 'functions', 'class': 'FailureDestinationDetails'},
    'success-destination': {'module': 'functions', 'class': 'SuccessDestinationDetails'},
    'trace-config': {'module': 'functions', 'class': 'FunctionTraceConfig'},
    'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'},
    'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}
}


def _safe_pop(command_group, command_name):
    if command_name in command_group.commands:
        command_group.commands.pop(command_name)


def _pop_function_command_if_present(attr_name):
    if hasattr(functionsmanagement_cli, attr_name):
        _safe_pop(functionsmanagement_cli.function_group, getattr(functionsmanagement_cli, attr_name).name)


def _normalize_provisioned_concurrency(kwargs):
    if 'provisioned_concurrency' in kwargs:
        kwargs['provisioned_concurrency_config'] = kwargs.pop('provisioned_concurrency')


def _invoke_create(ctx, kwargs, source_details):
    _normalize_provisioned_concurrency(kwargs)
    kwargs['source_details'] = json.dumps(source_details)
    ctx.invoke(functionsmanagement_cli.create_function, **kwargs)


def _invoke_update(ctx, kwargs, source_details=None):
    _normalize_provisioned_concurrency(kwargs)
    if source_details is not None:
        kwargs['source_details'] = json.dumps(source_details)
    ctx.invoke(functionsmanagement_cli.update_function, **kwargs)


def _add_if_present(payload, payload_key, value):
    if value is not None:
        payload[payload_key] = value


def _read_archive_file_value(archive_file):
    if archive_file is None:
        return None

    archive_file_path = archive_file
    if archive_file.lower().startswith('file://'):
        archive_file_path = archive_file[len('file://'):]

    archive_file_path = os.path.expandvars(os.path.expanduser(archive_file_path))
    if not os.path.exists(archive_file_path):
        raise click.UsageError("Archive file '{}' does not exist.".format(archive_file))

    if not archive_file_path.lower().endswith(('.zip', '.jar')):
        raise click.UsageError("Archive file '{}' must be a .zip or .jar file.".format(archive_file))

    with open(archive_file_path, 'rb') as archive:
        return base64.b64encode(archive.read()).decode('utf-8')


def _build_object_storage_archive_details(kwargs, include_if_empty=True):
    archive_source_details = {'archiveSourceType': 'OBJECT_STORAGE_ARCHIVE'}

    for option_key, payload_key in [
        ('bucket_name', 'bucketName'),
        ('namespace', 'namespace'),
        ('object_name', 'objectName'),
        ('object_version_id', 'objectVersionId')
    ]:
        option_value = kwargs.pop(option_key, None)
        if option_value is not None:
            archive_source_details[payload_key] = option_value

    if not include_if_empty and len(archive_source_details) == 1:
        return None

    return archive_source_details


def _build_direct_archive_details(kwargs, include_if_empty=True):
    archive_file = _read_archive_file_value(kwargs.pop('archive_file', None))
    if archive_file is None and not include_if_empty:
        return None

    return {
        'archiveSourceType': 'DIRECT_ARCHIVE',
        'archiveFile': archive_file
    }


def _build_fn_update_runtime_config(kwargs, include_if_empty=True):
    functions_runtime_name = kwargs.pop('functions_runtime_name', None)
    if functions_runtime_name is None and not include_if_empty:
        return None

    return {
        'runtimeConfigType': 'FUNCTION_UPDATE',
        'functionsRuntimeName': functions_runtime_name
    }


def _build_manual_runtime_config(kwargs, functions_runtime_name_required, include_if_empty=True):
    functions_runtime_version_id = kwargs.pop('functions_runtime_version_id', None)
    functions_runtime_name = kwargs.pop('functions_runtime_name', None)

    if not include_if_empty and functions_runtime_name is None and functions_runtime_version_id is None:
        return None

    runtime_config = {
        'runtimeConfigType': 'MANUAL',
        'functionsRuntimeVersionId': functions_runtime_version_id
    }

    if functions_runtime_name_required or functions_runtime_name is not None:
        runtime_config['functionsRuntimeName'] = functions_runtime_name

    return runtime_config


def _get_update_archive_source_type(kwargs):
    archive_file_provided = kwargs.get('archive_file') is not None
    object_storage_option_keys = ['bucket_name', 'namespace', 'object_name', 'object_version_id']
    object_storage_options_provided = [option_key for option_key in object_storage_option_keys if kwargs.get(option_key) is not None]

    if archive_file_provided and object_storage_options_provided:
        raise click.UsageError(
            'Cannot specify --archive-file with Object Storage archive options: --bucket-name, --namespace, --object-name, --object-version-id.'
        )

    if object_storage_options_provided:
        required_object_storage_option_keys = ['bucket_name', 'namespace', 'object_name']
        missing_required_options = [
            '--' + option_key.replace('_', '-')
            for option_key in required_object_storage_option_keys
            if kwargs.get(option_key) is None
        ]
        if missing_required_options:
            raise click.UsageError(
                'Must specify --bucket-name, --namespace and --object-name together when using Object Storage archive options.'
            )
        return 'OBJECT_STORAGE_ARCHIVE'

    if archive_file_provided:
        return 'DIRECT_ARCHIVE'

    return None


def _build_update_archive_source_details(kwargs):
    archive_source_type = _get_update_archive_source_type(kwargs)

    if archive_source_type == 'OBJECT_STORAGE_ARCHIVE':
        kwargs.pop('archive_file', None)
        return _build_object_storage_archive_details(kwargs, include_if_empty=False)

    if archive_source_type == 'DIRECT_ARCHIVE':
        for option_key in ['bucket_name', 'namespace', 'object_name', 'object_version_id']:
            kwargs.pop(option_key, None)
        return _build_direct_archive_details(kwargs, include_if_empty=False)

    for option_key in ['bucket_name', 'namespace', 'object_name', 'object_version_id', 'archive_file']:
        kwargs.pop(option_key, None)
    return None


def _build_update_runtime_config(ctx, kwargs):
    runtime_config_type = kwargs.pop('runtime_config', None)
    functions_runtime_name = kwargs.pop('functions_runtime_name', None)
    functions_runtime_version_id = kwargs.pop('functions_runtime_version_id', None)

    if runtime_config_type is None:
        if (functions_runtime_name is not None or functions_runtime_version_id is not None) and not _is_generating_json_skeleton(ctx):
            raise click.UsageError(
                'Must specify --runtime-config when using --functions-runtime-name or --functions-runtime-version-id.'
            )
        return None

    if runtime_config_type == RUNTIME_CONFIG_FUNCTION_UPDATE:
        if functions_runtime_name is None and not _is_generating_json_skeleton(ctx):
            raise click.UsageError('Must specify --functions-runtime-name when --runtime-config is FUNCTION_UPDATE.')
        return {
            'runtimeConfigType': RUNTIME_CONFIG_FUNCTION_UPDATE,
            'functionsRuntimeName': functions_runtime_name
        }

    if runtime_config_type == RUNTIME_CONFIG_MANUAL:
        if functions_runtime_version_id is None:
            missing_options = ['--functions-runtime-version-id']
        else:
            missing_options = []
        if missing_options and not _is_generating_json_skeleton(ctx):
            raise click.UsageError(
                'Must specify --functions-runtime-version-id when --runtime-config is MANUAL.'
            )
        runtime_config = {
            'runtimeConfigType': RUNTIME_CONFIG_MANUAL,
            'functionsRuntimeVersionId': functions_runtime_version_id
        }
        if functions_runtime_name is not None:
            runtime_config['functionsRuntimeName'] = functions_runtime_name
        return runtime_config

    return None


def _build_archive_source_details(archive_source_details, runtime_config, kwargs):
    source_details = {
        'sourceType': 'ARCHIVE'
    }

    if archive_source_details is not None:
        source_details['archiveSourceDetails'] = archive_source_details

    if runtime_config is not None:
        source_details['runtimeConfig'] = runtime_config

    handler = kwargs.pop('handler', None)
    _add_if_present(source_details, 'handler', handler)

    return source_details


def _build_container_source_details(kwargs, image_required):
    source_details = {'sourceType': 'CONTAINER_IMAGE'}

    image = kwargs.pop('image', None)
    if image_required or image is not None:
        source_details['image'] = image

    image_digest = kwargs.pop('image_digest', None)
    _add_if_present(source_details, 'imageDigest', image_digest)

    return source_details


def _is_generating_json_skeleton(ctx):
    return ctx.obj.get('generate_full_command_json_input') or ctx.obj.get('generate_param_json_input')


def _require_option_for_execution(ctx, kwargs, option_key, option_name, command_name):
    if _is_generating_json_skeleton(ctx):
        return
    if kwargs.get(option_key) is None:
        raise click.UsageError('Must specify {} when using {}.'.format(option_name, command_name))


# Remove generated function commands replaced by the preferred type-aware command hierarchy.
for attr in [
    'create_function',
    'update_function',
    'create_function_create_archive_function_source_details',
    'create_function_create_container_image_function_source_details',
    'create_function_create_pre_built_function_source_details',
    'update_function_update_archive_function_source_details',
    'update_function_update_container_image_function_source_details'
]:
    _pop_function_command_if_present(attr)


# Remove generated flattening variants already hidden by this extended command surface.
for attr in [
    'create_function_none_provisioned_concurrency_config',
    'create_function_constant_provisioned_concurrency_config',
    'update_function_none_provisioned_concurrency_config',
    'update_function_constant_provisioned_concurrency_config',
    'create_function_none_failure_destination_details',
    'create_function_notification_failure_destination_details',
    'create_function_queue_failure_destination_details',
    'create_function_stream_failure_destination_details',
    'update_function_none_failure_destination_details',
    'update_function_notification_failure_destination_details',
    'update_function_queue_failure_destination_details',
    'update_function_stream_failure_destination_details',
    'create_function_none_success_destination_details',
    'create_function_notification_success_destination_details',
    'create_function_queue_success_destination_details',
    'create_function_stream_success_destination_details',
    'update_function_none_success_destination_details',
    'update_function_notification_success_destination_details',
    'update_function_queue_success_destination_details',
    'update_function_stream_success_destination_details'
]:
    _pop_function_command_if_present(attr)


@click.group(name='create', cls=CommandGroupWithAlias, help=functionsmanagement_cli.create_function.help)
@cli_util.help_option_group
def function_create_group():
    pass


@click.group(name='update', cls=CommandGroupWithAlias, help=functionsmanagement_cli.update_function.help)
@cli_util.help_option_group
def function_update_group():
    pass


functionsmanagement_cli.function_group.add_command(function_create_group)
functionsmanagement_cli.function_group.add_command(function_update_group)


@function_create_group.group(name='archive-function', cls=CommandGroupWithAlias, help=ARCHIVE_FUNCTION_GROUP_HELP)
@cli_util.help_option_group
def create_archive_function_group():
    pass


@create_archive_function_group.group(name='object-storage', cls=CommandGroupWithAlias, help=OBJECT_STORAGE_ARCHIVE_GROUP_HELP)
@cli_util.help_option_group
def create_archive_object_storage_group():
    pass


@create_archive_function_group.group(name='direct-archive', cls=CommandGroupWithAlias, help=DIRECT_ARCHIVE_GROUP_HELP)
@cli_util.help_option_group
def create_archive_direct_archive_group():
    pass


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@create_archive_object_storage_group.command(name='fn-update-runtime-config', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--bucket-name', required=True, help=BUCKET_NAME_HELP)
@cli_util.option('--namespace', required=True, help=NAMESPACE_HELP)
@cli_util.option('--object-name', required=True, help=OBJECT_NAME_HELP)
@cli_util.option('--object-version-id', help=OBJECT_VERSION_ID_HELP)
@cli_util.option('--functions-runtime-name', required=True, help=FUNCTIONS_RUNTIME_NAME_HELP)
@cli_util.option('--handler', help=HANDLER_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_archive_object_storage_fn_update_runtime_config(ctx, **kwargs):
    source_details = _build_archive_source_details(
        _build_object_storage_archive_details(kwargs),
        _build_fn_update_runtime_config(kwargs),
        kwargs
    )
    _invoke_create(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@create_archive_object_storage_group.command(name='manual-runtime-config', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--bucket-name', required=True, help=BUCKET_NAME_HELP)
@cli_util.option('--namespace', required=True, help=NAMESPACE_HELP)
@cli_util.option('--object-name', required=True, help=OBJECT_NAME_HELP)
@cli_util.option('--object-version-id', help=OBJECT_VERSION_ID_HELP)
@cli_util.option('--functions-runtime-name', required=True, help=FUNCTIONS_RUNTIME_NAME_HELP)
@cli_util.option('--functions-runtime-version-id', required=True, help=FUNCTIONS_RUNTIME_VERSION_ID_HELP)
@cli_util.option('--handler', help=HANDLER_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_archive_object_storage_manual_runtime_config(ctx, **kwargs):
    source_details = _build_archive_source_details(
        _build_object_storage_archive_details(kwargs),
        _build_manual_runtime_config(kwargs, functions_runtime_name_required=True),
        kwargs
    )
    _invoke_create(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@create_archive_direct_archive_group.command(name='fn-update-runtime-config', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--archive-file', required=True, help=ARCHIVE_FILE_HELP)
@cli_util.option('--functions-runtime-name', required=True, help=FUNCTIONS_RUNTIME_NAME_HELP)
@cli_util.option('--handler', help=HANDLER_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_archive_direct_archive_fn_update_runtime_config(ctx, **kwargs):
    source_details = _build_archive_source_details(
        _build_direct_archive_details(kwargs),
        _build_fn_update_runtime_config(kwargs),
        kwargs
    )
    _invoke_create(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@create_archive_direct_archive_group.command(name='manual-runtime-config', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--archive-file', required=True, help=ARCHIVE_FILE_HELP)
@cli_util.option('--functions-runtime-name', required=True, help=FUNCTIONS_RUNTIME_NAME_HELP)
@cli_util.option('--functions-runtime-version-id', required=True, help=FUNCTIONS_RUNTIME_VERSION_ID_HELP)
@cli_util.option('--handler', help=HANDLER_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_archive_direct_archive_manual_runtime_config(ctx, **kwargs):
    source_details = _build_archive_source_details(
        _build_direct_archive_details(kwargs),
        _build_manual_runtime_config(kwargs, functions_runtime_name_required=True),
        kwargs
    )
    _invoke_create(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@function_create_group.command(name='container-function', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--image', required=True, help=IMAGE_HELP)
@cli_util.option('--image-digest', help=IMAGE_DIGEST_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_container_function(ctx, **kwargs):
    _invoke_create(ctx, kwargs, _build_container_source_details(kwargs, image_required=True))


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.create_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@function_create_group.command(name='pbf-function', help=functionsmanagement_cli.create_function.help)
@cli_util.option('--pbf-listing-id', required=True, help=PBF_LISTING_ID_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def create_pbf_function(ctx, **kwargs):
    source_details = {
        'sourceType': 'PRE_BUILT_FUNCTIONS',
        'pbfListingId': kwargs.pop('pbf_listing_id')
    }
    _invoke_create(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.update_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@function_update_group.command(name='archive-function', help=functionsmanagement_cli.update_function.help)
@cli_util.option('--bucket-name', help=BUCKET_NAME_HELP)
@cli_util.option('--namespace', help=NAMESPACE_HELP)
@cli_util.option('--object-name', help=OBJECT_NAME_HELP)
@cli_util.option('--object-version-id', help=OBJECT_VERSION_ID_HELP)
@cli_util.option('--functions-runtime-name', help=FUNCTIONS_RUNTIME_NAME_HELP)
@cli_util.option('--functions-runtime-version-id', help=FUNCTIONS_RUNTIME_VERSION_ID_HELP)
@cli_util.option('--archive-file', help=ARCHIVE_FILE_HELP)
@cli_util.option('--runtime-config', type=custom_types.CliCaseInsensitiveChoice([RUNTIME_CONFIG_FUNCTION_UPDATE, RUNTIME_CONFIG_MANUAL]), help=RUNTIME_CONFIG_HELP)
@cli_util.option('--handler', help=HANDLER_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def update_archive_function(ctx, **kwargs):
    source_details = _build_archive_source_details(
        _build_update_archive_source_details(kwargs),
        _build_update_runtime_config(ctx, kwargs),
        kwargs
    )
    _invoke_update(ctx, kwargs, source_details)


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.update_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@function_update_group.command(name='container-function', help=functionsmanagement_cli.update_function.help)
@cli_util.option('--image', help=IMAGE_HELP)
@cli_util.option('--image-digest', help=IMAGE_DIGEST_HELP)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def update_container_function(ctx, **kwargs):
    _invoke_update(ctx, kwargs, _build_container_source_details(kwargs, image_required=False))


@cli_util.copy_params_from_generated_command(functionsmanagement_cli.update_function, params_to_exclude=['source_details', 'provisioned_concurrency_config'])
@function_update_group.command(name='pbf-function', help=functionsmanagement_cli.update_function.help)
@cli_util.option('--provisioned-concurrency', type=custom_types.CLI_COMPLEX_TYPE, help=PROVISIONED_CONCURRENCY_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types=FUNCTION_COMPLEX_TYPES)
def update_pbf_function(ctx, **kwargs):
    _invoke_update(ctx, kwargs)
