# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import division
from __future__ import print_function
import arrow
import base64
import click
import hashlib
import math
import os
import os.path
import stat
import sys
import six  # noqa: F401
import services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager  # noqa: F401,E402
from oci import exceptions
from oci.object_storage.transfer import constants
from oci_cli.cli_util import render, render_response, parse_json_parameter, help_option, help_option_group, build_client, wrap_exceptions, filter_object_headers, get_param, copy_help_from_generated_code, stream_page_object
from oci.object_storage import UploadManager, MultipartObjectAssembler
from oci_cli.file_filters import BaseFileFilterCollection
from oci_cli.file_filters import SingleTypeFileFilterCollection
from retrying import retry
from oci_cli import retry_utils
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager import TransferManager, TransferManagerConfig, WorkPoolTaskCallback, WorkPoolTaskErrorCallback, WorkPoolTaskSuccessCallback, WorkPoolTaskCallbacksContainer
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli import custom_types  # noqa: F401
from oci_cli.custom_types import BulkPutOperationOutput, BulkGetOperationOutput, BulkDeleteOperationOutput
from services.object_storage.src.oci_cli_object_storage.generated import objectstorage_cli
from oci_cli import cli_util
from mimetypes import guess_type
import oci_cli.cli_root as cli_root
import oci_cli.final_command_processor as final_command_processor
from oci_cli import cli_exceptions
from oci.retry import RetryStrategyBuilder


def is_python2():
    return sys.version_info[0] < 3


# For namespace parameter within object storage commands, if not explicitly provided we make a SDK API call to
# get the parameter. This removes the requirement for the parameter to be a required parameter.
# Is this an object storage command? Check if the first level command is 'os' [oci os]
def cli_util_func(ctx, param_name):
    if param_name in ['namespace-name', 'namespace']:
        cert_bundle = None
        if 'cert_bundle' in ctx.obj:
            cert_bundle = ctx.obj['cert_bundle']
        if not cert_bundle and 'default_values_from_file' in ctx.obj:
            default_values_from_file = ctx.obj['default_values_from_file']
            if 'cert_bundle' in default_values_from_file:
                ctx.obj['cert_bundle'] = default_values_from_file['cert_bundle']
            elif 'cert-bundle' in default_values_from_file:
                ctx.obj['cert_bundle'] = default_values_from_file['cert-bundle']
        client = build_client('object_storage', 'object_storage', ctx)
        try:
            namespace = client.get_namespace().data
        except Exception as e:
            raise cli_exceptions.RequiredValueNotAvailableInternallyOrUserInputError(
                'Unable to retrieve namespace internally. '
                'Please provide the namespace using the option "--{}".'.format(param_name))
        return namespace


# Since almost all object storage commands require the namespace parameter and it can be obtained via an SDK
# API call, this function goes through all the object storage commands and makes the namespace parameter as
# Optional. It also updates the help text for the parameter
def remove_namespace_required_objectstorage():
    if not cli_root.cli.commands.get('os', None):
        return
    commands = cli_util.collect_commands(cli_root.cli.commands.get('os'))
    for command in commands:
        for param in command.params:
            if param.name in ['namespace_name', 'namespace', 'ns']:
                param.required = False
                if param.help.endswith(' [required]'):
                    # Remove ' [required]'
                    param.help = ' '.join(param.help.split(' ')[:-1])
                    # Add help text
                    param.help = param.help + " If not provided, this parameter will be obtained " \
                                              "internally using a call to 'oci os ns get'"


cli_util.SERVICE_FUNCTIONS_TO_EXECUTE['os'] = cli_util_func
final_command_processor.SERVICE_FUNCTIONS_TO_EXECUTE.append(remove_namespace_required_objectstorage)

OBJECT_LIST_PAGE_SIZE = 100
OBJECT_VERSION_LIST_PAGE_SIZE = 100
OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS = 1000

MAX_MULTIPART_SIZE = 10000
MEBIBYTE = constants.MEBIBYTE

OBJECT_GET_CHUNK_SIZE = MEBIBYTE

OBJECT_PUT_DISPLAY_HEADERS = {
    "etag",
    "opc-content-md5",
    "last-modified",
    "opc-multipart-md5"
}

SSE_PARAMS = ['opc_sse_customer_algorithm', 'opc_sse_customer_key', 'opc_sse_customer_key_sha256']
SOURCE_SSE_PARAMS = [hdr.replace('opc_', 'opc_source_') for hdr in SSE_PARAMS]
SSE_REENCRYPT_OBJECT_PARAMS = ['sse_customer_key', 'source_sse_customer_key']
SSE_ALGORITHM = "AES256"


INCLUDE_EXCLUDE_PATTERN = r"""
*: Matches everything

?: Matches any single character

[sequence]: Matches any character in sequence

[!sequence]: Matches any character not in sequence
"""

objectstorage_cli.get_namespace.short_help = 'Gets the name of the namespace for the user'
objectstorage_cli.namespace_group.help = """
A namespace is a logical entity that serves as a top-level container for all buckets and objects, allowing you to control bucket naming within your tenancy. Each tenancy is provided one unique and uneditable namespace that is global, spanning all regions and compartments. While bucket names must be unique within your namespace, bucket names within your namespace can duplicate bucket names used in the namespaces of other tenants.


Namespace metadata stores the compartment assignments for resources created by the Amazon S3 Compatibility API and the Swift API. By default, resources created by the Amazon S3 Compatibility and Swift APIs are stored in the root compartment of the tenancy.
"""

get_param(objectstorage_cli.get_namespace_metadata, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.update_namespace_metadata, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_object_lifecycle_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_object_lifecycle_policy, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.get_object_lifecycle_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.get_object_lifecycle_policy, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.put_object_lifecycle_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.put_object_lifecycle_policy, 'bucket_name').opts.extend(['-bn'])

objectstorage_cli.bucket_group.commands.pop(objectstorage_cli.head_bucket.name)
get_param(objectstorage_cli.create_bucket, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_bucket, 'bucket_name').opts.extend(['--name', '-bn'])
get_param(objectstorage_cli.delete_bucket, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.get_bucket, 'bucket_name').opts.extend(['--name', '-bn'])
get_param(objectstorage_cli.get_bucket, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.list_buckets, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.update_bucket, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.update_bucket, 'bucket_name').opts.extend(['--name', '-bn'])
get_param(objectstorage_cli.copy_object, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.copy_object, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.reencrypt_bucket, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.reencrypt_bucket, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.reencrypt_object, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.reencrypt_object, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.reencrypt_object, 'object_name').opts.extend(['-on', '--name'])

objectstorage_cli.object_group.commands.pop(objectstorage_cli.copy_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.get_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.head_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_objects.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.put_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.restore_objects.name)
objectstorage_cli.os_root_group.commands.pop(objectstorage_cli.multipart_upload_group.name)

get_param(objectstorage_cli.make_bucket_writable, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.make_bucket_writable, 'bucket_name').opts.extend(['--bucket', '-bn'])

get_param(objectstorage_cli.create_replication_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.create_replication_policy, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.delete_replication_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_replication_policy, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.get_replication_policy, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.get_replication_policy, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.list_replication_policies, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.list_replication_policies, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.list_replication_sources, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.list_replication_sources, 'bucket_name').opts.extend(['--bucket', '-bn'])

get_param(objectstorage_cli.delete_object, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.delete_object, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_object, 'object_name').opts.extend(['--name'])
get_param(objectstorage_cli.rename_object, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.rename_object, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.rename_object, 'new_obj_if_match_e_tag').opts.extend(['--new-if-match'])
get_param(objectstorage_cli.rename_object, 'new_obj_if_none_match_e_tag').opts.extend(['--new-if-none-match'])
get_param(objectstorage_cli.rename_object, 'source_name').opts.extend(['--name'])
get_param(objectstorage_cli.rename_object, 'src_obj_if_match_e_tag').opts.extend(['--src-if-match'])

get_param(objectstorage_cli.create_preauthenticated_request, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.create_preauthenticated_request, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.create_preauthenticated_request, 'object_name').opts.extend(['-on'])
get_param(objectstorage_cli.delete_preauthenticated_request, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.delete_preauthenticated_request, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.get_preauthenticated_request, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.get_preauthenticated_request, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.list_preauthenticated_requests, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.list_preauthenticated_requests, 'namespace_name').opts.extend(['--namespace', '-ns'])

get_param(objectstorage_cli.create_retention_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.create_retention_rule, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.update_retention_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.update_retention_rule, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.get_retention_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.get_retention_rule, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.list_retention_rules, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.list_retention_rules, 'bucket_name').opts.extend(['--bucket', '-bn'])
get_param(objectstorage_cli.delete_retention_rule, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.delete_retention_rule, 'bucket_name').opts.extend(['--bucket', '-bn'])

cli_util.rename_command(objectstorage_cli, objectstorage_cli.os_root_group, objectstorage_cli.namespace_group, "ns")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.namespace_group, objectstorage_cli.get_namespace_metadata, "get-metadata")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.namespace_group, objectstorage_cli.update_namespace_metadata, "update-metadata")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.os_root_group, objectstorage_cli.preauthenticated_request_group, "preauth-request")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.work_request_log_entry_group, objectstorage_cli.list_work_request_logs, "list")

objectstorage_cli.os_root_group.help = "Object Storage Service CLI"
objectstorage_cli.os_root_group.short_help = "Object Storage Service"

objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_object_versions.name)

cli_util.override_command_short_help_and_help(objectstorage_cli.get_bucket, u"""Gets the current representation of the given bucket in the given Object Storage namespace. \n[Command Reference](getBucket)

Bucket  summary  includes  the  'namespace',  'name',  'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields.""")
cli_util.update_param_help(objectstorage_cli.get_bucket, 'fields', """This parameter can only include 'approximateCount' (approximate number of objects) and 'approximateSize' (total approximate size in bytes of all objects). For example '--fields approximateCount --fields approximateSize'.""", append=False)


@objectstorage_cli.object_group.command(name='list-object-versions', help=u"""Lists the object versions in a bucket.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.option('--namespace', '--namespace-name', '-ns', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket', '--bucket-name', '-bn', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--prefix', help=u"""The string to use for matching against the start of object names in a list query.""")
@cli_util.option('--start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--delimiter', help=u"""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@cli_util.option('--fields', default='name,size,timeCreated,md5', show_default=True, help=u"""Object summary in list of objects includes the 'name' field. This parameter can also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time) and 'timeModified' (object modification date and time). Value of this parameter should be a comma-separated, case-insensitive list of those field names. For example 'name,etag,timeCreated,md5,timeModified' Allowed values are: name, size, etag, timeCreated, md5, timeModified""")
@cli_util.option('--start-after', help=u"""Object names returned by a list query must be greater than this parameter.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ObjectVersionCollection'})
@cli_util.wrap_exceptions
def list_object_versions(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, prefix, start, end, limit, delimiter, fields, start_after, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    elif not all_pages and limit is None:
        limit = 100

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if prefix is not None:
        kwargs['prefix'] = prefix
    if start is not None:
        kwargs['start'] = start
    if end is not None:
        kwargs['end'] = end
    if limit is not None:
        kwargs['limit'] = limit
    if delimiter is not None:
        kwargs['delimiter'] = delimiter
    if fields is not None:
        kwargs['fields'] = fields
    if start_after is not None:
        kwargs['start_after'] = start_after
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    client = cli_util.build_client('object_storage', 'object_storage', ctx)

    all_items = []
    prefixes = list()

    remaining_item_count = limit
    keep_paginating_for_all = True

    # if the user explicitly sets limit to 0 we will still call the service once with limit=0
    fetched_at_least_once = False
    while (not all_pages and (remaining_item_count > 0 or not fetched_at_least_once)) or (all_pages and keep_paginating_for_all):
        fetched_at_least_once = True

        if all_pages:
            if page_size:
                kwargs['limit'] = page_size
            else:
                kwargs['limit'] = OBJECT_VERSION_LIST_PAGE_SIZE
        else:
            if page_size:
                kwargs['limit'] = min(page_size, remaining_item_count)
            else:
                kwargs['limit'] = min(remaining_item_count, OBJECT_VERSION_LIST_PAGE_SIZE)

        response = client.list_object_versions(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )

        if response.data.prefixes is not None:
            for prefix in response.data.prefixes:
                if prefix not in prefixes:
                    prefixes.append(prefix)

        items = response.data.items
        next_page = response.headers.get('opc-next-page')
        all_items.extend(items)

        if next_page:
            if remaining_item_count:
                remaining_item_count -= len(items)
            kwargs['page'] = next_page
        else:
            keep_paginating_for_all = False
            remaining_item_count = 0

    metadata = {'prefixes': prefixes}

    if response.headers.get('opc-next-page'):
        metadata['opc-next-page'] = response.headers.get('opc-next-page')

    render(all_items, metadata, ctx, display_all_headers=True)


@objectstorage_cli.object_group.command(name='list')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--prefix', help='Only object names that begin with this prefix will be returned.')
@cli_util.option('--start', help='Only object names greater or equal to this parameter will be returned.')
@cli_util.option('--end', help='Only object names less than this parameter will be returned.')
@cli_util.option('--limit', type=click.INT, help='The maximum number of items to return. [default: 100]')
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                 "delimiter character (after an optionally specified prefix) are returned. "
                 "Scanned objects whose names contain the delimiter have part of their name "
                 "up to the last occurrence of the delimiter (after the optional prefix) "
                 "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                 "character at this time.")
@cli_util.option('--fields', default='name,size,timeCreated,md5', show_default=True, help="Object summary in list of objects includes the 'name' field. This parameter may also include "
                 "'size' (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields. "
                 "Value of this parameter should be a comma separated, case-insensitive list of those field names.")
@cli_util.option('--stream-output', 'stream_output', is_flag=True, help="""Print output to stdout as it is fetched so the full response is not stored in memory. This only works with --all.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[ObjectSummary]'})
@wrap_exceptions
def object_list(ctx, from_json, namespace, bucket_name, prefix, start, end, limit, delimiter, fields, all_pages, page_size, stream_output):
    """
    Lists the objects in a bucket.

    Example:
        oci os object list -ns mynamespace -bn mybucket --fields name,size,timeCreated
    """
    if all_pages and limit is not None:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    elif not all_pages and limit is None:
        limit = 100
    if stream_output and all_pages is None:
        raise click.UsageError('The --stream-output option requires --all.')
    client = build_client('object_storage', 'object_storage', ctx)

    args = {
        'fields': fields,
        'opc_client_request_id': ctx.obj['request_id']
    }
    if start:
        args['start'] = start

    if delimiter is not None:
        args['delimiter'] = delimiter

    if end is not None:
        args['end'] = end

    if prefix is not None:
        args['prefix'] = prefix

    all_objects = []
    prefixes = list()

    remaining_item_count = limit
    keep_paginating_for_all = True
    page_index = 1
    previous_page_has_data = False

    # if the user explicitly sets limit to 0 we will still call the service once with limit=0
    fetched_at_least_once = False
    while (not all_pages and (remaining_item_count > 0 or not fetched_at_least_once)) or (all_pages and keep_paginating_for_all):
        fetched_at_least_once = True

        if all_pages:
            if page_size:
                args['limit'] = page_size
            else:
                args['limit'] = OBJECT_LIST_PAGE_SIZE
        else:
            if page_size:
                args['limit'] = min(page_size, remaining_item_count)
            else:
                args['limit'] = min(remaining_item_count, OBJECT_LIST_PAGE_SIZE)

        response = client.list_objects(
            namespace,
            bucket_name,
            **args
        )

        if response.data.prefixes is not None:
            for prefix in response.data.prefixes:
                if prefix not in prefixes:
                    prefixes.append(prefix)

        if stream_output:
            previous_page_has_data = stream_page_object(page_index=page_index,
                                                        call_result=response,
                                                        previous_page_has_data=previous_page_has_data,
                                                        data_key="objects")

            page_index += 1

        else:
            objects = response.data.objects
            all_objects.extend(objects)

        next_start = response.data.next_start_with

        if next_start:
            if remaining_item_count:
                remaining_item_count -= len(objects)
            args['start'] = next_start
        else:
            keep_paginating_for_all = False
            remaining_item_count = 0

    metadata = {'prefixes': prefixes}

    if response.data.next_start_with:
        metadata['next-start-with'] = response.data.next_start_with

    if stream_output:
        # we've already printed everything
        print("  \"prefixes\": " + str(metadata['prefixes']))
        print("}")
        if ctx.obj['debug']:
            print("", file=sys.stderr)
    else:
        render(all_objects, metadata, ctx, display_all_headers=True)


@objectstorage_cli.object_group.command(name='put')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--file', type=click.File(mode='rb'), required=True,
                 help="The file to load as the content of the object, or '-' to read from STDIN.")
@cli_util.option('--name',
                 help='The name of the object. Default value is the filename excluding the path. Required if reading object from STDIN.')
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--content-md5', help=u"""The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message:
     "The computed MD5 of the request body (ACTUAL_MD5) does not match the Content-MD5 header (HEADER_MD5)"
""")
@cli_util.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@cli_util.option('--content-type', help=u"""The optional Content-Type header that defines the standard MIME type format of the object. Content type defaults to \'application/octet-stream\' if not specified in the PutObject call. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.""")
@cli_util.option('--content-language', help=u"""The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.""")
@cli_util.option('--content-encoding', help=u"""The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.""")
@cli_util.option('--force', is_flag=True, help='If the object name already exists, overwrite the existing object without a confirmation prompt.')
@cli_util.option('--no-overwrite', is_flag=True, help='If the object name already exists, do not overwrite the existing object.')
@cli_util.option('--no-multipart', is_flag=True,
                 help='Do not use multipart uploads to upload the file in parts. By default files above 128 MiB will be uploaded in multiple parts, then combined server-side.')
@cli_util.option('--part-size', type=click.INT,
                 help='Part size (in MiB) to use when uploading objects using multipart upload operations. The default part size is 128 MiB.')
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, 1000), default=None,
                 help='If the object will be uploaded in multiple parts, this option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads or --no-multipart. Defaults to 3 and the maximum is 1000.')
@cli_util.option('--verify-checksum', is_flag=True, help='Verify the checksum of the uploaded object with the local file.')
@cli_util.option('--content-disposition', help=u"""The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.""")
@cli_util.option('--cache-control', help=u"""The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.""")
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}}, output_type={'module': 'object_storage', 'class': 'ObjectSummary'})
@wrap_exceptions
def object_put(ctx, from_json, namespace, bucket_name, name, file, if_match, content_md5, metadata, content_type, content_language, content_encoding, force, no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count, verify_checksum, content_disposition, cache_control, encryption_key_file):
    """
    Creates a new object or overwrites an existing one.

    The object can be uploaded as a single part or as multiple parts. Below are the rules for whether an object will be uploaded via single or multipart upload (listed in order of precedence):

        * If the object is being uploaded from STDIN, it will be uploaded as a multipart upload (if the object content is smaller than --part-size, default for STDIN is 10 MiB, the multipart upload may contain only one part, but it will still use the MultipartUpload API)

        * If the --no-multipart flag is specified, the object will be uploaded as a single part regardless of size (specifying --no-multipart when uploading from STDIN will result in an error)

        * If the object is larger than --part-size, it will be uploaded as multiple parts

        * If the object is empty it will be uploaded as a single part

    Example:
        oci os object put -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt --metadata '{"key1":"value1","key2":"value2"}'
    """
    # explicitly disallow retries for object put because we may not be able to re-read the input source
    no_retry = ctx.obj['no_retry']
    ctx.obj['no_retry'] = True

    client = build_client('object_storage', 'object_storage', ctx)

    client_request_id = ctx.obj['request_id']
    kwargs = {'opc_client_request_id': client_request_id}
    part_size_mib = constants.DEFAULT_PART_SIZE

    if parallel_upload_count is not None:
        if disable_parallel_uploads:
            raise click.UsageError('The option --parallel-upload-count is not applicable when using the --disable-parallel-uploads flag.')
        if no_multipart:
            raise click.UsageError('The option --parallel-upload-count is not applicable when using the --no-multipart flag.')

    # default object name is filename without path
    if not name:
        if not hasattr(file, 'name') or file.name == '<stdin>':
            raise click.UsageError('Option "--name" must be provided when reading object from stdin')

        name = os.path.basename(file.name)

    if part_size is not None and no_multipart:
        raise click.UsageError('The option --part-size is not applicable when using the --no-multipart flag.')

    if not force:
        etag = get_object_etag(client, namespace, bucket_name, name, client_request_id, if_match)

        if etag is None:
            # Object does not exist, so make sure that the put fails if one is created in the meantime.
            kwargs['if_none_match'] = '*'
        else:
            kwargs['if_match'] = etag
            if no_overwrite:
                click.echo('The object already exists and was not overwritten', file=sys.stderr)
                ctx.exit(0)
            if not click.confirm("WARNING: This object already exists. Are you sure you want to overwrite it?"):
                ctx.abort()

    if if_match is not None:
        kwargs['if_match'] = if_match

    if content_md5 is not None:
        kwargs['content_md5'] = content_md5

    if metadata is not None:
        kwargs['metadata'] = parse_json_parameter("metadata", metadata, default={})

    if content_type is not None:
        # If content type is set to auto, then the CLI will guess the content type of the file.
        # If we read the contents from stdin, we use name attribute to find the content_type.
        # If a file path is given, we use the file name to guess the content_type.
        if content_type == 'auto':
            kwargs['content_type'], _ = guess_type(name) if file.name == '<stdin>' else guess_type(file.name)
        else:
            kwargs['content_type'] = content_type

    if content_language is not None:
        kwargs['content_language'] = content_language

    if content_encoding is not None:
        kwargs['content_encoding'] = content_encoding

    if part_size is not None:
        kwargs['part_size'] = part_size * MEBIBYTE
        part_size_mib = part_size * MEBIBYTE

    if content_disposition is not None:
        kwargs['content_disposition'] = content_disposition

    if cache_control is not None:
        kwargs['cache_control'] = cache_control

    total_size = os.fstat(file.fileno()).st_size

    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            kwargs.update(sse_args)

    if math.ceil(total_size / part_size_mib) > MAX_MULTIPART_SIZE:
        part_size = math.ceil(math.ceil(total_size / MAX_MULTIPART_SIZE) / MEBIBYTE)
        kwargs['part_size'] = part_size * MEBIBYTE

    size_qualifies_for_multipart = UploadManager._use_multipart(total_size, part_size) if part_size else UploadManager._use_multipart(total_size)

    ma = None

    if not hasattr(file, 'name') or file.name == '<stdin>':
        if no_multipart:
            raise click.UsageError('The --no-multipart flag is not valid when taking input from STDIN.')

        # For data coming from standard in, stream it up to Object Storage. This handles both being put in as here string (<<<)
        # and data being piped in.
        #
        # As an aside, for the here string the total size is known, but for data being piped its not determinable (without reading
        # all the data off)

        upload_manager = UploadManager(client)

        if disable_parallel_uploads:
            upload_manager.allow_parallel_uploads = False

        if parallel_upload_count:
            upload_manager.parallel_process_count = parallel_upload_count

        # The total_size won't be accurate for pipes, so give the bar some arbitrary size. If the
        # progress bar gets full, we'll rotate it back to the beginning
        if stat.S_ISFIFO(os.fstat(file.fileno()).st_mode):
            if part_size:
                total_size = part_size * MEBIBYTE * 3
            else:
                total_size = constants.STREAMING_DEFAULT_PART_SIZE * 3

        bar = ProgressBar(total_size, 'Uploading object part')
        kwargs['progress_callback'] = bar.update_indeterminate_size

        response = upload_manager.upload_stream(namespace, bucket_name, name, sys.stdin, **kwargs)

        # Close the bar, but make sure that we end up at 100% (otherwise we could end on something like 33%, which looks odd)
        if bar:
            bar.update(total_size)
            bar.render_finish()
    elif total_size == 0 or no_multipart or not size_qualifies_for_multipart:
        if parallel_upload_count is not None:
            click.echo(
                'Warning: File is being uploaded as a single part so --parallel-upload-count will be ignored.',
                file=sys.stderr)

        # if file is empty, progress_callback will never be called (no bytes will be read), so dont show progress bar
        bar = None
        if total_size > 0:
            bar = ProgressBar(total_size, 'Uploading object')
            kwargs['progress_callback'] = bar.update

        try:
            upload_manager = UploadManager(client, allow_multipart_uploads=False)
            response = upload_manager.upload_file(namespace, bucket_name, name, file.name, **kwargs)
        except Exception as e:
            if not no_retry and retry_utils.retry_on_timeouts_connection_internal_server_and_throttles(e):
                response = SingleUploadRetry(client, namespace, bucket_name, name, file.name, bar, total_size, **kwargs).retrying_upload_file_call()
            else:
                if bar:
                    bar.render_finish()
                raise e

        if bar:
            bar.render_finish()
    else:
        if 'content_md5' in kwargs:
            click.echo(
                'Warning: The --content-md5 option cannot be used with multipart uploads. It will be ignored.',
                file=sys.stderr)

        if disable_parallel_uploads:
            kwargs['allow_parallel_uploads'] = False

        if parallel_upload_count is not None:
            kwargs['parallel_process_count'] = parallel_upload_count

        UploadManager._add_adapter_to_service_client(client, not disable_parallel_uploads, parallel_upload_count)

        ma = MultipartObjectAssembler(client,
                                      namespace,
                                      bucket_name,
                                      name,
                                      **kwargs)
        ma.new_upload()
        click.echo('Upload ID: {}'.format(ma.manifest["uploadId"]), file=sys.stderr)
        ma.add_parts_from_file(file.name)
        click.echo('Split file into {} parts for upload.'.format(len(ma.manifest["parts"])), file=sys.stderr)

        # 60 retries - with exponential sleep time and a max wait of 60 secs.
        retry_strategy = RetryStrategyBuilder(retry_max_wait_between_calls_seconds=60).add_max_attempts(60)\
            .no_total_elapsed_time() \
            .add_service_error_check() \
            .get_retry_strategy()

        with ProgressBar(total_size, 'Uploading object') as bar:
            try:
                ma.upload(retry_strategy=retry_strategy, progress_callback=bar.update)
            except RuntimeError as re:
                if 'thread' in str(re) or 'Thread' in str(re):
                    raise Exception('Cannot start that many threads, please reduce the parallel-upload-count. The default is 3.')
                else:
                    raise re
            except Exception as e:
                if not no_retry and retry_utils.retry_on_timeouts_connection_internal_server_and_throttles(e) and file.name != '<stdin>':
                    RetryResumeUpload(ma, ma.manifest["uploadId"], total_size, bar).retrying_resume_multipart_upload()
                else:
                    raise e
        response = ma.commit(retry_strategy=retry_strategy)

    display_headers = filter_object_headers(response.headers, OBJECT_PUT_DISPLAY_HEADERS)
    render(None, display_headers, ctx, display_all_headers=True)
    is_not_multipart = not size_qualifies_for_multipart or no_multipart

    if verify_checksum:
        multipart_hash = cli_util.verify_checksum(file.name, is_not_multipart, ma)
        message, match = cli_util.get_checksum_message(response.headers, multipart_hash)
        click.echo(message, file=sys.stderr)
        exit(0 if match else 1)


@objectstorage_cli.object_group.command(name='bulk-upload')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='Object Storage namespace.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--src-dir', required=True, help='The directory which contains files to upload. Files in the directory and all subdirectories will be uploaded.', type=click.UNPROCESSED)
@cli_util.option('--object-prefix', help='A prefix to apply to the names of all files being uploaded')
@cli_util.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. This will be applied to all files being uploaded. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@cli_util.option('--content-type', help='The content type to apply to all files being uploaded. If content type is set to auto, then the CLI will guess the content type of the file.')
@cli_util.option('--content-language', help='The content language to apply to all files being uploaded.')
@cli_util.option('--content-encoding', help='The content encoding to apply to all files being uploaded.')
@cli_util.option('--overwrite', is_flag=True, help="""If a file being uploaded already exists in Object Storage with the same name, overwrite the existing object in Object Storage without a confirmation prompt. If neither this flag nor --no-overwrite is specified, you will be prompted each time an object with the same name would be overwritten.

Specifying this flag will also allow for faster uploads as the CLI will not initially check whether or not the files with the same name already exist in Object Storage.""")
@cli_util.option('--no-overwrite', is_flag=True, help='If a file being uploaded already exists in Object Storage with the same name, do not overwite the object. If neither this flag nor --overwrite is specified, you will be prompted each time an object with the same name would be overwritten.')
@cli_util.option('--no-multipart', is_flag=True,
                 help='Do not use multipart uploads to upload the file in parts. By default, files above 128 MiB will be uploaded in multiple parts, then combined server-side. This applies to all files being uploaded')
@cli_util.option('--part-size', type=click.INT,
                 help='Part size (in MiB) to use if uploading via multipart upload operations. This applies to all files which will be uploaded in multiple parts. Part size must be greater than 10 MiB')
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='[DEPRECATED] This option is no longer used. If a file in the directory will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel. This applies to all files being uploaded in multiple parts')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, 1000), default=10, show_default=True,
                 help='The number of parallel operations to perform. Decreasing this value will make bulk uploads less resource intensive but they may take longer. Increasing this value may improve bulk upload times, but the upload process will consume more system resources and network bandwidth. The maximum is 1000.')
@cli_util.option('--verify-checksum', is_flag=True, help='Verify the checksum of the uploaded object with the local file.')
@cli_util.option('--include', multiple=True, help="""Only upload files which match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--exclude', multiple=True, help="""Only upload files which do not match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--dry-run', is_flag=True, help="""Prints the list of files to be uploaded.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@wrap_exceptions
def object_bulk_put(ctx, from_json, namespace, bucket_name, src_dir, object_prefix, metadata, content_type, content_language, content_encoding, overwrite, no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count, verify_checksum, include, exclude, encryption_key_file, dry_run):
    """
    Uploads all files in a given directory and all subdirectories.


    \b
    Examples
    ========

    \b
    Upload all files from a given directory
    -----------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory

    \b
    Upload all files and prefix the object names in Object Storage
    --------------------------------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory --object-prefix my-prefix/

    In the above example command, all files uploaded to Object Storage will have their object names prefixed with
    "my-prefix/". This will allow you to further group uploaded files together or potentially avoid name collisions
    when uploading files.

    \b
    Forcing object overwrite to resolve object name collision
    ----------------------------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory --overwrite

    \b
    If a file being uploaded already exists in Object Storage with the same name, it can be overwritten without a prompt by
    using the --overwrite flag. Specifying --overwrite will also allow for faster uploads as the CLI will not
    initially check whether or not the files already exist in Object Storage with the same name.

    \b
    Prevent object overwrite to resolve object name collision
    ----------------------------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory --no-overwrite

    \b
    If a file being uploaded already exists in Object Storage with the same name, it can be preserved (not overwritten) without a
    prompt by using the --no-overwrite flag.
    """
    # there is existing retry logic for bulk_put so we don't want the Python SDK level retries to interfere / overlap with that
    ctx.obj['no_retry'] = True
    auto_content_type = False

    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided.')

    expanded_directory = os.path.expandvars(os.path.expanduser(src_dir))
    if not os.path.exists(expanded_directory):
        raise click.UsageError('The specified --src-dir {} (expanded to: {}) does not exist'.format(src_dir, expanded_directory))

    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, None)

    if part_size is not None and no_multipart:
        raise click.UsageError('The option --part-size is not applicable when using the --no-multipart flag.')

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together.')

    client = build_client('object_storage', 'object_storage', ctx)
    client_request_id = ctx.obj['request_id']

    base_kwargs = {'opc_client_request_id': client_request_id}
    if metadata is not None:
        base_kwargs['metadata'] = parse_json_parameter("metadata", metadata, default={})
    if content_type is not None:
        # If content type is set to auto, then the CLI will guess the content type of the file
        if content_type == 'auto':
            auto_content_type = True
        else:
            base_kwargs['content_type'] = content_type
    if content_language is not None:
        base_kwargs['content_language'] = content_language
    if content_encoding is not None:
        base_kwargs['content_encoding'] = content_encoding
    if part_size is not None:
        base_kwargs['part_size'] = part_size * MEBIBYTE

    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            base_kwargs.update(sse_args)

    output = BulkPutOperationOutput()

    # Progress bar which we can reuse over and over again
    reusable_progress_bar = ProgressBar(0, '')

    transfer_manager = TransferManager(
        client,
        TransferManagerConfig(
            max_object_storage_requests=parallel_upload_count,
            max_object_storage_multipart_requests=parallel_upload_count,
            max_multipart_files_to_process=parallel_upload_count,
            use_multipart_uploads=(not no_multipart)
        )
    )
    head_object_results = {}

    # If we need to check for overwrites then we'll need to make HEAD object calls. We can queue these up in the
    # transfer_manager to be processed by the worker pool in the background so we potentially have to wait less per loop iteration.
    # This window variable controls how much (how many objects) we should look ahead by so that we make sure that all the HEAD requests
    # don't monopolise the processes in the transfer_manager's underlying pool of work
    parallel_head_object_look_ahead_window = int(parallel_upload_count / 2)

    for dir_name, subdir_list, file_list in os.walk(expanded_directory):
        for idx, file in enumerate(file_list):
            full_file_path = os.path.join(dir_name, file)

            if file_filter_collection:
                if file_filter_collection.get_action(full_file_path) == BaseFileFilterCollection.EXCLUDE:
                    continue
            if dry_run:
                print(full_file_path)
                continue

            object_name = normalize_object_name_path_for_object_storage(full_file_path[len(expanded_directory):])
            if is_python2():
                object_name = object_name.decode("utf-8")

            # If we start with a leading path separator (/), strip that from the object name so we get a hierarchy like:
            #    <subfolder1>/<subfolder2>/<object>
            # Rather than:
            #    /<subfolder1>/<subfolder2>/<object>
            if object_name[0] == '/':
                object_name = object_name[1:]

            if object_prefix:
                object_name = u'{}{}'.format(object_prefix, object_name)

            # If content type is set to auto, then the CLI will guess the content type of the file
            if auto_content_type:
                base_kwargs['content_type'], _ = guess_type(object_name)
            try:
                if not overwrite:
                    if len(file_list) > (idx + parallel_head_object_look_ahead_window):
                        for i in range(parallel_head_object_look_ahead_window):
                            look_ahead_file_path = os.path.join(dir_name, file_list[idx + i])
                            look_ahead_object_name = normalize_object_name_path_for_object_storage(look_ahead_file_path[len(expanded_directory):])
                            if look_ahead_object_name[0] == '/':
                                look_ahead_object_name = look_ahead_object_name[1:]
                            if object_prefix:
                                look_ahead_object_name = u'{}{}'.format(object_prefix, look_ahead_object_name)

                            if look_ahead_object_name not in head_object_results:
                                head_object_kwargs = {
                                    'namespace_name': namespace,
                                    'bucket_name': bucket_name,
                                    'object_name': look_ahead_object_name,
                                    'opc_client_request_id': client_request_id
                                }
                                head_object_results[look_ahead_object_name] = transfer_manager.head_object(WorkPoolTaskCallbacksContainer(), **head_object_kwargs)
                    if is_python2():
                        object_name = object_name.encode("utf-8")

                    # Pull the result from the future (this will block until the result is available) or, if we don't have a future, just make a request
                    if object_name in head_object_results:
                        head_object = head_object_results.pop(object_name).result()
                    else:
                        head_object = _make_retrying_head_object_call(client, namespace, bucket_name, object_name, client_request_id)
                    if is_python2():
                        object_name = object_name.decode("utf-8")

                    if head_object is None:
                        # Object does not exist, so make sure that the put fails if one is created in the meantime.
                        base_kwargs['if_none_match'] = '*'
                    else:
                        if no_overwrite:
                            output.add_skipped(object_name)
                            continue

                        base_kwargs['if_match'] = head_object.headers['etag']
                        if not click.confirm(u'WARNING: {} already exists. Are you sure you want to overwrite it?'.format(object_name)):
                            output.add_skipped(object_name)
                            continue

                with open(full_file_path, 'rb') as file_object:
                    file_size = os.fstat(file_object.fileno()).st_size

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': u'Uploaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Uploaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                error_callback_kwargs = {'failed_item': object_name}
                success_callback_kwargs = {'uploaded_object': object_name}

                add_to_uploaded_objects_callback = WorkPoolTaskSuccessCallback(output.add_uploaded, **success_callback_kwargs)
                add_to_upload_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], success_callbacks=[add_to_uploaded_objects_callback], error_callbacks=[add_to_upload_failures_callback])

                if ctx.obj['debug']:
                    click.echo('Uploading {}'.format(full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Uploading'))

                if not ctx.obj['debug']:
                    base_kwargs['multipart_part_completion_callback'] = BulkOperationMultipartUploadProgressBar(reusable_progress_bar, file_size, _get_progress_bar_label(None, object_name, 'Uploading part for')).update

                if is_python2():
                    object_name = object_name.encode("utf-8")

                transfer_manager.upload_object(callbacks_container, namespace, bucket_name, object_name, full_file_path, file_size, verify_checksum, **base_kwargs)

                # These can vary per request, so remove them if they exist so we have a blank slate for the next iteration
                base_kwargs.pop('if_none_match', None)
                base_kwargs.pop('if_match', None)
                base_kwargs.pop('multipart_part_completion_callback', None)
            except Exception as e:
                # Don't let one failure here (either HEADing to see if the object exists, or actaully uploading the object)
                # fail the entire batch, but store the error for output later
                output.add_failure(object_name, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo(u'Failed to upload {}'.format(object_name), file=sys.stderr)
    if dry_run:
        sys.exit(0)

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


def get_object_etag(client, namespace, bucket_name, name, client_request_id, if_match):
    """Returns the etag for the specified object, or None if it doesn't exist."""
    kwargs = {'opc_client_request_id': client_request_id}
    etag = None

    if if_match is not None:
        kwargs['if_match'] = if_match
    try:
        response = client.head_object(namespace, bucket_name, name, **kwargs)
        etag = response.headers['etag']
    except exceptions.ServiceError as e:
        if e.status != 404:
            raise

    return etag


@objectstorage_cli.object_group.command(name='get')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--name', required=True, help='The name of the object.')
@cli_util.option('--file', type=click.File(mode='wb', lazy=False), required=True,
                 help="The name of the file that will receive the object content, or '-' to write to STDOUT.")
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--if-none-match', help='The entity tag to avoid matching.')
@cli_util.option('--range',
                 help='Byte range to fetch. Follows https://tools.ietf.org/html/rfc7233#section-2.1. Example: bytes=2-10')
@cli_util.option('--multipart-download-threshold', type=click.IntRange(128, None), help='Objects larger than this size (in MiB) will be downloaded in multiple parts. The minimum allowable threshold is 128 MiB.')
@cli_util.option('--part-size', type=click.IntRange(128, None), help='Part size (in MiB) to use when downloading an object in multiple parts. The minimum allowable size is 128 MiB.')
@cli_util.option('--parallel-download-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform when downloading an object in multiple parts. Decreasing this value will make multipart downloads less resource intensive but they may take longer. Increasing this value may improve download times, but the download process will consume more system resources and network bandwidth.')
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--http-response-content-disposition', help=u"""This value will be used in Content-Disposition header of the response.""")
@cli_util.option('--http-response-cache-control', help=u"""This value will be used in Cache-Control header of the response.""")
@cli_util.option('--http-response-content-type', help=u"""This value will be used in Content-Type header of the response.""")
@cli_util.option('--http-response-content-language', help=u"""This value will be used in Content-Language header of the response.""")
@cli_util.option('--http-response-content-encoding', help=u"""This value will be used in Content-Encoding header of the response""")
@cli_util.option('--http-response-expires', help=u"""This value will be used in Expires header of the response""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_get(ctx, from_json, namespace, bucket_name, name, file, version_id, if_match, if_none_match, range, multipart_download_threshold, part_size, parallel_download_count, encryption_key_file, http_response_content_disposition, http_response_cache_control, http_response_content_type, http_response_content_language, http_response_content_encoding, http_response_expires):
    """
    Gets the metadata and body of an object.

    Example:
        oci os object get -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt
    """
    # No defaulting of the file so that we don't inadvertently overwrite the same file or stream each time
    if range and multipart_download_threshold:
        raise click.UsageError("Cannot specify both the --range and --multipart-download-threshold parameters")

    encryption_key_params = {}
    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            encryption_key_params = sse_args

    client = build_client('object_storage', 'object_storage', ctx)

    head_object = client.head_object(namespace, bucket_name, name, opc_client_request_id=ctx.obj['request_id'],
                                     **encryption_key_params)
    if not head_object:
        raise click.ClickException('The specified object does not exist')

    object_size_bytes = 0
    if 'Content-Length' in head_object.headers:
        object_size_bytes = int(head_object.headers['Content-Length'])

    if not part_size:
        part_size = 128 * MEBIBYTE
    else:
        part_size = part_size * MEBIBYTE

    # if outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>':
        bar = ProgressBar(total_bytes=object_size_bytes, label='Downloading object')

    # If we aren't doing multipart, or we are doing multipart but there would only be a single part
    if not multipart_download_threshold or (multipart_download_threshold and part_size >= object_size_bytes):
        response = client.get_object(
            namespace,
            bucket_name,
            name,
            if_match=if_match,
            if_none_match=if_none_match,
            range=range,
            opc_client_request_id=ctx.obj['request_id'],
            version_id=version_id,
            http_response_content_disposition=http_response_content_disposition,
            http_response_cache_control=http_response_cache_control,
            http_response_content_type=http_response_content_type,
            http_response_content_language=http_response_content_language,
            http_response_content_encoding=http_response_content_encoding,
            http_response_expires=http_response_expires,
            **encryption_key_params
        )

        # Stream using the raw urllib3.HTTPResponse, since using the Requests response
        # will automatically try to decode.
        for chunk in response.data.raw.stream(OBJECT_GET_CHUNK_SIZE, decode_content=False):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)

    else:
        transfer_manager = TransferManager(client, TransferManagerConfig(max_object_storage_requests=parallel_download_count, max_object_storage_multipart_requests=parallel_download_count))

        get_object_multipart_kwargs = {
            'namespace': namespace,
            'bucket_name': bucket_name,
            'object_name': name,
            'if_match': if_match,
            'if_none_match': if_none_match,
            'request_id': ctx.obj['request_id'],
            'part_size': part_size,
            'multipart_download_threshold': multipart_download_threshold,
            'total_size': object_size_bytes,
            'version_id': version_id,
            'http_response_content_disposition': http_response_content_disposition,
            'http_response_cache_control': http_response_cache_control,
            'http_response_content_type': http_response_content_type,
            'http_response_content_language': http_response_content_language,
            'http_response_content_encoding': http_response_content_encoding,
            'http_response_expires': http_response_expires
        }
        get_object_multipart_kwargs.update(encryption_key_params)

        if not ctx.obj['debug'] and bar:
            get_object_multipart_kwargs['chunk_written_callback'] = bar.update
            bar.update(1)  # Dummy update to make the bar show up (otherwise it won't until the first thread/process writes the first part to disk)

        get_multipart_task = transfer_manager.get_object_multipart(WorkPoolTaskCallbacksContainer(), file, **get_object_multipart_kwargs)
        get_multipart_task.result()  # This will throw an exception if there was an error
        transfer_manager.wait_for_completion()

    if bar:
        bar.render_finish()


@objectstorage_cli.object_group.command(name='bulk-download')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--prefix', help='Retrieve all objects with the given prefix. Omit this parameter to get all objects in the bucket')
@cli_util.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                 "delimiter character (after an optionally specified prefix) are returned. "
                 "Scanned objects whose names contain the delimiter have part of their name "
                 "up to the last occurrence of the delimiter (after the optional prefix) "
                 "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                 "character at this time.")
@cli_util.option('--download-dir', required=True, help='The directory where retrieved objects will be placed as files. This directory will be created if it does not exist.')
@cli_util.option('--overwrite', is_flag=True, help='If a file with the same name as an object already exists in the download directory, overwrite it. If neither this flag nor --no-overwrite is specified, you will be prompted each time a file would be overwritten.')
@cli_util.option('--no-overwrite', is_flag=True, help='If a file with the same name as an object already exists in the download directory, do not overwite it. If neither this flag nor --overwrite is specified, you will be prompted each time a file would be overwritten')
@cli_util.option('--parallel-operations-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform. Decreasing this value will make bulk downloads less resource intensive but they may take longer. Increasing this value may improve bulk download times, but the upload process will consume more system resources and network bandwidth.')
@cli_util.option('--multipart-download-threshold', type=click.IntRange(128, None), help='Objects larger than this size (in MiB) will be downloaded in multiple parts. The minimum allowable threshold is 128 MiB.')
@cli_util.option('--part-size', type=click.IntRange(128, None), help='Part size (in MiB) to use when downloading an object in multiple parts. The minimum allowable size is 128 MiB.')
@cli_util.option('--include', multiple=True, help="""Only download objects which match the provided pattern. Patterns are taken relative to the DOWNLOAD directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--exclude', multiple=True, help="""Only download objects which do not match the provided pattern. Patterns are taken relative to the DOWNLOAD directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--dry-run', is_flag=True, help="""Prints the list of files to be downloaded.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_get(ctx, from_json, namespace, bucket_name, prefix, delimiter, download_dir, overwrite, no_overwrite, include, exclude, parallel_operations_count, multipart_download_threshold, part_size, encryption_key_file, dry_run):
    """
    Downloads all objects which match the given prefix to a given directory.


    \b
    Examples
    ========

    \b
    Download all objects in the bucket
    ------------------------------
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory

    \b
    Download all objects that match a given prefix
    ----------------------------------------------
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory --prefix myprefix

    \b
    You can download all objects that match a given prefix by specifying the --prefix flag. In the above example, "--prefix myprefix" would
    match object names such as myPrefix_textfile1.txt, myPrefix_myImage.png etc.

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, then you
    can download objects at a given level (and all sub levels) by specifying a prefix:

    \b
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory --prefix level1/level2/

    \b
    This will download all objects of the form level1/level2/<object name>, level1/level2/leve3/<object name>,
    level1/level2/leve3/level4/<object name> etc.

    \b
    Limiting downloaded objects using a prefix and delimiter
    --------------------------------------------------------
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory --prefix level1/level2/ --delimiter /

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, and you only
    want to download objects at a given level of the hierarchy, e.g. example everything of the form level1/level2/<object name> but not
    level1/level2/leve3/<object name> or any other sub-levels, you can specify a prefix and delimiter. Currently the only supported delimiter
    is /

    \b
    Overwriting or skipping files
    ------------------------------
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory --overwrite
    oci os object bulk-download -ns mynamespace -bn mybucket --download-dir path/to/download/directory --no-overwrite

    \b
    If files with the same name as the objects being downloaded already exist in the download directory, you can opt to overwrite them with the
    --overwrite option, or preserve them with the --no-overwrite option.
    """
    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided.')

    if not part_size:
        part_size = 128 * MEBIBYTE
    else:
        part_size = part_size * MEBIBYTE

    client = build_client('object_storage', 'object_storage', ctx)

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together.')

    expanded_directory = os.path.expandvars(os.path.expanduser(download_dir))
    if not os.path.exists(expanded_directory):
        os.makedirs(expanded_directory)

    kwargs = {
        'client': client,
        'request_id': ctx.obj['request_id'],
        'namespace': namespace,
        'bucket_name': bucket_name,
        'prefix': prefix,
        'start': None,
        'end': None,
        'limit': OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
        'delimiter': delimiter,
        'fields': 'name,size'
    }
    keep_paginating = True
    ask_overwrite = True

    encryption_key_params = {}
    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            encryption_key_params = sse_args

    output = BulkGetOperationOutput()

    # Progress bar which we can reuse over and over again
    reusable_progress_bar = ProgressBar(0, '')

    transfer_manager = TransferManager(client, TransferManagerConfig(max_object_storage_requests=parallel_operations_count))
    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, prefix)

    while keep_paginating:
        list_objects_response = retrying_list_objects_single_page(**kwargs)
        next_start = list_objects_response.data.next_start_with
        to_download = []

        if next_start is not None and not overwrite and not no_overwrite and ask_overwrite:
            if click.confirm("You are downloading more than 1000 objects, do you want to overwrite all?"):
                overwrite = True
            ask_overwrite = False

        # Process the current batch and write to disk
        for obj in list_objects_response.data.objects:
            object_name = obj.name

            # If the object name starts with the path separator (account for Unix and Windows paths) then remove it when we
            # do the joining to create a full file name, otherwise we could get an unexpected result
            if object_name[0] == '/' or object_name[0] == '\\':
                full_file_path = os.path.join(expanded_directory, object_name[1:])
            else:
                full_file_path = os.path.join(expanded_directory, object_name)

            if file_filter_collection:
                if file_filter_collection.get_action(full_file_path) == BaseFileFilterCollection.EXCLUDE:
                    continue

            if os.path.exists(full_file_path):
                if no_overwrite:
                    output.add_skipped(object_name)
                    continue

                if not overwrite and not dry_run:
                    confirm = click.prompt(u'WARNING: {} already exists. Are you sure you want to overwrite it? [y/N/yes to (a)ll]'.format(object_name), default='N', type=custom_types.CliCaseInsensitiveChoice(["Y", "N", "A"]))
                    if confirm == 'N':
                        output.add_skipped(object_name)
                        continue
                    elif confirm == 'A':
                        overwrite = True

            dl_obj = {
                "name": obj.name,
                "size": obj.size,
                "full_file_path": full_file_path
            }
            to_download.append(dl_obj)
            list_objects_response = None
        if dry_run:
            for obj in to_download:
                click.echo(click.style("{}").format(obj['name']))
            sys.exit(0)
        for obj in to_download:
            object_name = obj['name']
            object_size = obj['size']
            full_file_path = obj['full_file_path']

            directory_for_file = os.path.dirname(full_file_path)
            if not os.path.exists(directory_for_file):
                os.makedirs(directory_for_file)

            try:
                get_object_kwargs = {
                    'namespace': namespace,
                    'bucket_name': bucket_name,
                    'object_name': object_name.encode("utf-8") if is_python2() else object_name,
                    'full_file_path': full_file_path,
                    'request_id': ctx.obj['request_id']
                }
                get_object_kwargs.update(encryption_key_params)

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': u'Downloaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Downloaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                error_callback_kwargs = {'failed_item': object_name}
                add_to_download_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], error_callbacks=[add_to_download_failures_callback])

                if ctx.obj['debug']:
                    click.echo(u'Downloading {} to {}'.format(object_name, full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Downloading'))

                # If it's not multipart, or it is but we would only have a single part then just download it, otherwise do a multipart get
                # If the part size is somehow not known then use a multipart download by default (the multipart download will
                # try and figure out the size via a HEAD and then take the appropriate action based on the size and threshold)
                if not multipart_download_threshold or (multipart_download_threshold and (object_size is not None and part_size >= object_size)):
                    transfer_manager.get_object(callbacks_container, **get_object_kwargs)
                else:
                    if object_size:
                        multipart_callback_reference = BulkOperationMultipartUploadProgressBar(reusable_progress_bar, object_size, _get_progress_bar_label(None, object_name, 'Downloading part for')).update

                        get_object_kwargs['total_size'] = object_size
                        if not ctx.obj['debug']:
                            get_object_kwargs['chunk_written_callback'] = multipart_callback_reference
                            get_object_kwargs['part_completed_callback'] = multipart_callback_reference
                    else:
                        multipart_callback_reference = BulkOperationMultipartUploadProgressBar(reusable_progress_bar, 5 * part_size, _get_progress_bar_label(None, object_name, 'Downloading part for')).update

                        # Since we don't know the total here, give some arbitrary size and the task will update it later
                        if not ctx.obj['debug']:
                            get_object_kwargs['chunk_written_callback'] = multipart_callback_reference
                            get_object_kwargs['part_completed_callback'] = multipart_callback_reference

                    get_object_kwargs['part_size'] = part_size
                    get_object_kwargs['multipart_download_threshold'] = multipart_download_threshold

                    get_object_kwargs.pop('full_file_path')

                    transfer_manager.get_object_multipart(callbacks_container, full_file_path, **get_object_kwargs)
            except Exception as e:
                # Don't let one get failure fail the entire batch, but store the error for output later
                output.add_failure(object_name, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo(u'Failed to download {}'.format(object_name), file=sys.stderr)

        # Keep going if we have more pages
        kwargs['start'] = next_start
        keep_paginating = (next_start is not None)

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


@objectstorage_cli.object_group.command(name='head')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--name', required=True, help='The name of the object.')
@cli_util.option('--version-id', help=u"""VersionId used to identify a particular version of the object""")
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--if-none-match', help='The entity tag to avoid matching.')
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_head(ctx, from_json, namespace, bucket_name, name, version_id, if_match, if_none_match, encryption_key_file):
    """
    Gets the user-defined metadata and entity tag for an object.

    Example:
        oci os object head -ns mynamespace -bn mybucket --name myfile.txt
    """
    encryption_key_params = {}
    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            encryption_key_params = sse_args

    client = build_client('object_storage', 'object_storage', ctx)
    response = client.head_object(
        namespace,
        bucket_name,
        name,
        if_match=if_match,
        if_none_match=if_none_match,
        opc_client_request_id=ctx.obj['request_id'],
        version_id=version_id,
        **encryption_key_params)

    render(None, response.headers, ctx, display_all_headers=True)


@objectstorage_cli.object_group.command(name='bulk-delete')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--prefix', help='Delete all objects with the given prefix. Omit this parameter to delete all objects in the bucket.')
@cli_util.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                 "delimiter character (after an optionally specified prefix) are deleted. "
                 "Scanned objects whose names contain the delimiter have part of their name "
                 "up to the last occurrence of the delimiter (after the optional prefix) "
                 "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                 "character at this time.")
@cli_util.option('--dry-run', is_flag=True, help='Displays a list of objects which would be deleted by this command, if it were run without --dry-run. If --dry-run is passed, no objects will actually be deleted.')
@cli_util.option('--force', is_flag=True, help='Do not ask for confirmation prior to performing the bulk delete.')
@cli_util.option('--parallel-operations-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform. Decreasing this value will make bulk deletes less resource intensive but they may take longer. Increasing this value may improve bulk delete times, but the upload process will consume more system resources and network bandwidth.')
@cli_util.option('--include', multiple=True, help="""Only delete objects which match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--exclude', multiple=True, help="""Only download objects which do not match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_delete(ctx, from_json, namespace, bucket_name, prefix, delimiter, dry_run, force, include, exclude, parallel_operations_count):
    """
    Deletes all objects in a bucket which match the provided criteria.


    \b
    Examples
    ========

    \b
    Deleting all objects in the bucket
    ----------------------------------
    oci os object bulk-delete -ns mynamespace -bn mybucket

    \b
    Delete all objects that match a given prefix
    --------------------------------------------
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --prefix myprefix

    \b
    You can delete all objects that match a given prefix by specifying the --prefix flag. In the above example, "--prefix myprefix" would
    match object names such as myprefix_textfile1.txt, myprefix_myImage.png etc.

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, then you
    can delete objects at a given level (and all sub levels) by specifying a prefix:

    \b
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/

    \b
    This will delete all objects of the form level1/level2/<object name>, level1/level2/leve3/<object name>,
    level1/level2/leve3/level4/<object name> etc.

    \b
    Limiting deleted objects using a prefix and delimiter
    -----------------------------------------------------
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter /

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, and you only
    want to delete objects at a given level of the hierarchy, e.g. example everything of the form level1/level2/<object name> but not
    level1/level2/leve3/<object name> or any other sub-levels, you can specify a prefix and delimiter. Currently the only supported delimiter
    is /

    \b
    Previewing what would be deleted
    ----------------------------
    oci os object bulk-delete -ns mynamespace -bn mybucket --dry-run
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --dry-run
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter / --dry-run

    \b
    For any bulk-delete command you can get a list of all objects which would be deleted, but without actually deleting them, by using the --dry-run
    flag

    \b
    Do not prompt for delete
    ------------------------
    oci os object bulk-delete -ns mynamespace -bn mybucket --force
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --force
    oci os object bulk-delete -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter / --force

    \b
    By default, the bulk-delete command will prompt you prior to deleting objects. To suppress this prompt, pass the --force option.
    """
    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    client = build_client('object_storage', 'object_storage', ctx)

    output = BulkDeleteOperationOutput()

    # When deleting objects, since the items (probably) don't exist on local disk there is no base directory to reference. However, here we
    # use the bucket name as a fake base directory
    file_filter_collection = _get_file_filter_collection(bucket_name, include, exclude, prefix)

    if dry_run:
        list_all_objects_responses = retrying_list_objects(
            client=client,
            request_id=ctx.obj['request_id'],
            namespace=namespace,
            bucket_name=bucket_name,
            prefix=prefix,
            start=None,
            end=None,
            limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
            delimiter=delimiter,
            fields='name',
            retrieve_all=True
        )

        for response in list_all_objects_responses:
            for obj in response.data.objects:
                if file_filter_collection:
                    pseudo_path = os.path.join(bucket_name, obj.name)
                    if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                        continue
                output.add_deleted(obj.name)

        render(data=output.get_output(ctx.obj['output'], dry_run=True), headers=None, ctx=ctx, nest_data_in_data_attribute=False)
        ctx.exit()

    # Based on the rules for --force:
    #
    # CLI should do a list for 1000 items, and ask for confirmation with a message saying either that more than 1000 items will be deleted,
    # or the exact number of items that will be deleted
    list_objects_responses = retrying_list_objects(
        client=client,
        request_id=ctx.obj['request_id'],
        namespace=namespace,
        bucket_name=bucket_name,
        prefix=prefix,
        start=None,
        end=None,
        limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
        delimiter=delimiter,
        fields='name',
        retrieve_all=False
    )

    objects_to_delete = []
    for response in list_objects_responses:
        objects_to_delete.extend(map(lambda obj: obj.name.encode("utf-8") if is_python2() else obj.name, response.data.objects))

    if not force:
        if include or exclude:
            # If we specify this, the approximate or exact objects to delete is not determinable without paging through the entire list (e.g. in the
            # case that the only matching items are on the last few pages). So in this case just use a generic message
            confirm_prompt = u'WARNING: This command will delete all matching objects in the bucket. Please use --dry-run to list the objects which would be deleted. Are you sure you wish to continue?'
        else:
            if list_objects_responses[-1].data.next_start_with:
                # There are more pages of data
                confirm_prompt = u'WARNING: This command will delete at least {} objects. Are you sure you wish to continue?'.format(len(objects_to_delete))
            else:
                if len(objects_to_delete) == 0:
                    # There are no objects anyway, so just terminate here
                    click.echo(u'There are no objects to delete in {}'.format(bucket_name), file=sys.stderr)
                    ctx.exit()
                else:
                    confirm_prompt = u'WARNING: This command will delete {} objects. Are you sure you wish to continue?'.format(len(objects_to_delete))

        if not click.confirm(confirm_prompt):
            ctx.abort()

    transfer_manager = TransferManager(client, TransferManagerConfig(max_object_storage_requests=parallel_operations_count))
    reusable_progress_bar = ProgressBar(100, '')

    next_start_with = list_objects_responses[-1].data.next_start_with
    while next_start_with or len(objects_to_delete) > 0:
        for obj in objects_to_delete:
            if file_filter_collection:
                pseudo_path = os.path.join(bucket_name, obj)
                if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                    continue

            try:

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': u"Deleted {}".format(obj)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, obj.decode("utf-8") if is_python2() else obj, 'Deleted')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                add_to_deleted_kwargs = {'deleted': obj}
                error_callback_kwargs = {'failed_item': obj}
                add_to_deleted_objects_callback = WorkPoolTaskCallback(output.add_deleted, **add_to_deleted_kwargs)
                add_to_delete_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], success_callbacks=[add_to_deleted_objects_callback], error_callbacks=[add_to_delete_failures_callback])

                delete_kwargs = {
                    'namespace': namespace,
                    'bucket_name': bucket_name,
                    'object_name': obj,
                    'if_match': None,
                    'request_id': ctx.obj['request_id']
                }

                if ctx.obj['debug']:
                    click.echo(u'Deleting {}'.format(obj), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, obj.decode("utf-8") if is_python2() else obj, 'Deleting'))
                transfer_manager.delete_object(callbacks_container, **delete_kwargs)
            except Exception as e:
                # Don't let one get failure fail the entire batch, but store the error for output later
                output.add_failure(obj, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo('Failed to delete {}'.format(obj), file=sys.stderr)

        objects_to_delete = []  # New list (though we could also clear the existing list) in case we need to delete more stuff
        if next_start_with:
            # Because we may not be deleting objects for a while when there are filters, show a dummy message so the caller still knows that there
            # is progress
            if include or exclude:
                reusable_progress_bar.reset_progress(100, 'Searching for matching objects to delete')

            list_objects_response = retrying_list_objects_single_page(
                client=client,
                request_id=ctx.obj['request_id'],
                namespace=namespace,
                bucket_name=bucket_name,
                prefix=prefix,
                start=next_start_with,
                end=None,
                limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
                delimiter=delimiter,
                fields='name'
            )
            objects_to_delete.extend(map(lambda obj: obj.name.encode("utf-8") if is_python2() else obj.name, list_objects_response.data.objects))
            next_start_with = list_objects_response.data.next_start_with

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


@objectstorage_cli.object_group.command(name='bulk-delete-versions')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--prefix', help="Delete all object versions with the given prefix. "
                                  "Only one of prefix or objectName can be given as input. "
                                  "Omit this parameter to delete all objects in the bucket.")
@cli_util.option('--object-name', help="Delete all versions of the given objectName. "
                                       "Only one of prefix or objectName can be given as input. "
                                       "Omit this parameter to delete all objects in the bucket.")
@cli_util.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                                     "delimiter character (after an optionally specified prefix) are deleted. "
                                     "Scanned objects whose names contain the delimiter have part of their name "
                                     "up to the last occurrence of the delimiter (after the optional prefix) "
                                     "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                                     "character at this time.")
@cli_util.option('--dry-run', is_flag=True, help='Displays a list of objects which would be deleted by this command, if it were run without --dry-run. If --dry-run is passed, no objects will actually be deleted.')
@cli_util.option('--force', is_flag=True, help='Do not ask for confirmation prior to performing the bulk delete.')
@cli_util.option('--parallel-operations-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform. Decreasing this value will make bulk deletes less resource intensive but they may take longer. Increasing this value may improve bulk delete times, but the upload process will consume more system resources and network bandwidth.')
@cli_util.option('--include', multiple=True, help="""Only delete objects which match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--exclude', multiple=True, help="""Only delete objects which do not match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_delete_versions(ctx, from_json, namespace, bucket_name, prefix, delimiter, dry_run, force, include, exclude, parallel_operations_count, object_name):
    """
    Deletes all object versions in a bucket which match the provided criteria.


    \b
    Examples
    ========

    \b
    Deleting all object versions in the bucket
    ------------------------------------------
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket

    \b
    Delete all object versions that match a given prefix
    ----------------------------------------------------
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --prefix myprefix

    \b
    You can delete all object versions that match a given prefix by specifying the --prefix flag. In the above example, "--prefix myprefix" would
    match object names such as myprefix_textfile1.txt, myprefix_myImage.png etc.

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, then you
    can delete objects at a given level (and all sub levels) by specifying a prefix:

    \b
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/

    \b
    This will delete all objects of the form level1/level2/<object name>, level1/level2/leve3/<object name>,
    level1/level2/leve3/level4/<object name> etc.

    \b
    Limiting deleted objects using a prefix and delimiter
    -----------------------------------------------------
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter /

    \b
    If you have named your objects so that they exist in Object Storage as a hierarchy, e.g. level1/level2/level3/myobject.txt, and you only
    want to delete objects at a given level of the hierarchy, e.g. example everything of the form level1/level2/<object name> but not
    level1/level2/leve3/<object name> or any other sub-levels, you can specify a prefix and delimiter. Currently the only supported delimiter
    is /

    \b
    Deleting all object versions using object name
    ----------------------------------------------

    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --object-name <object name>

    You can delete all object versions that match a given object name by specifying the --object-name flag. Both -object-name and -prefix cannot be given in the same command

    \b
    Previewing what would be deleted
    --------------------------------
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --dry-run
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --dry-run
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter / --dry-run

    \b
    For any bulk-delete command you can get a list of all objects which would be deleted, but without actually deleting them, by using the --dry-run
    flag

    \b
    Do not prompt for delete
    ------------------------
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --force
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --force
    oci os object bulk-delete-versions -ns mynamespace -bn mybucket --prefix level1/level2/ --delimiter / --force

    \b
    By default, the bulk-delete-versions command will prompt you prior to deleting objects. To suppress this prompt, pass the --force option.
    """
    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    if object_name and (prefix or include or exclude):
        raise click.UsageError('The --object-name parameter cannot be combined with either --prefix or --include or --exclude')

    client = build_client('object_storage', 'object_storage', ctx)

    output = BulkDeleteOperationOutput()

    # When deleting objects, since the items (probably) don't exist on local disk there is no base directory to reference. However, here we
    # use the bucket name as a fake base directory
    file_filter_collection = _get_file_filter_collection(bucket_name, include, exclude, prefix)
    if dry_run:
        list_all_object_versions_responses = retrying_list_object_versions(
            client=client,
            request_id=ctx.obj['request_id'],
            namespace=namespace,
            bucket_name=bucket_name,
            prefix=prefix,
            start=object_name,
            end=None,
            limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
            delimiter=delimiter,
            page=None,
            fields='name',
            retrieve_all=True
        )

        for response in list_all_object_versions_responses:
            for obj in response.data.items:
                if file_filter_collection:
                    pseudo_path = os.path.join(bucket_name, obj.name)
                    if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                        continue
                if object_name and object_name != obj.name:
                    continue
                output.add_deleted(obj.name + "," + obj.version_id)
        render(data=output.get_output(ctx.obj['output'], dry_run=True), headers=None, ctx=ctx, nest_data_in_data_attribute=False)
        ctx.exit()

    reusable_progress_bar = ProgressBar(100, '')

    # Based on the rules for --force:
    #
    # CLI should do a list for 1000 items, and ask for confirmation with a message saying either that more than 1000 items will be deleted,
    # or the exact number of items that will be deleted
    #
    # Moving transfer manager inside while loop since we should wait for pool completion after delete
    # before list is called again
    #
    # Always list first page of versions that match given criteria and delete versions,
    # next_page_exists is not used for anything except to find out if next page exists or not
    #
    while True:

        transfer_manager = TransferManager(client, TransferManagerConfig(max_object_storage_requests=parallel_operations_count))
        list_all_object_versions_responses = retrying_list_object_versions(
            client=client,
            request_id=ctx.obj['request_id'],
            namespace=namespace,
            bucket_name=bucket_name,
            prefix=prefix,
            start=object_name,
            end=None,
            limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
            delimiter=delimiter,
            page=None,
            fields='name',
            retrieve_all=False
        )

        # if --object-name is provided, we should only delete objects that match
        object_versions_to_delete = []
        for response in list_all_object_versions_responses:
            for obj in response.data.items:
                if object_name and object_name != obj.name:
                    continue
                object_versions_to_delete.append(obj)

        if not force:
            if include or exclude:
                # If we specify this, the approximate or exact objects to delete is not determinable without paging through the entire list (e.g. in the
                # case that the only matching items are on the last few pages). So in this case just use a generic message
                confirm_prompt = 'WARNING: This command will delete all matching object versions in the bucket. Please use --dry-run to list the objects which would be deleted. Are you sure you wish to continue?'
            else:
                if list_all_object_versions_responses[-1].headers.get('opc-next-page'):
                    # There are more pages of data
                    confirm_prompt = 'WARNING: This command will delete at least {} object versions. Are you sure you wish to continue?'.format(len(object_versions_to_delete))
                else:
                    if len(object_versions_to_delete) == 0:
                        # There are no objects anyway, so just terminate here
                        click.echo('There are no objects to delete in {}'.format(bucket_name), file=sys.stderr)
                        sys.exit()
                    else:
                        confirm_prompt = 'WARNING: This command will delete {} object versions. Are you sure you wish to continue?'.format(len(object_versions_to_delete))

            if not click.confirm(confirm_prompt):
                ctx.abort()

        for obj in object_versions_to_delete:
            if file_filter_collection:
                pseudo_path = os.path.join(bucket_name, obj.name)
                if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                    continue

            try:
                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': 'Deleted object {} , version_id {}'.format(obj.name, obj.version_id)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, obj.name + "," + obj.version_id, 'Deleted')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                add_to_deleted_kwargs = {'deleted': obj.name + "," + obj.version_id}
                error_callback_kwargs = {'failed_item': obj.name + "," + obj.version_id}
                add_to_deleted_objects_callback = WorkPoolTaskCallback(output.add_deleted, **add_to_deleted_kwargs)
                add_to_delete_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], success_callbacks=[add_to_deleted_objects_callback], error_callbacks=[add_to_delete_failures_callback])
                delete_kwargs = {
                    'namespace': namespace,
                    'bucket_name': bucket_name,
                    'object_name': obj.name,
                    'if_match': None,
                    'request_id': ctx.obj['request_id'],
                    'version_id': obj.version_id
                }
                if ctx.obj['debug']:
                    click.echo('Deleting object name {}, version-id {}'.format(obj.name, obj.version_id), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, obj.name + "," + obj.version_id, 'Deleting'))

                transfer_manager.delete_object(callbacks_container, **delete_kwargs)
            except Exception as e:
                # Don't let one get failure fail the entire batch, but store the error for output later
                output.add_failure(obj.name + "," + obj.version_id, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo('Failed to delete object name {}, version-id {} '.format(obj.name, obj.version_id), file=sys.stderr)

        transfer_manager.wait_for_completion()

        if list_all_object_versions_responses[-1].headers.get('opc-next-page') is None:
            break

        # Because we may not be deleting objects for a while when there are filters, show a dummy message so the caller still knows that there
        # is progress
        if include or exclude:
            reusable_progress_bar.reset_progress(100, 'Searching for matching objects to delete')

    reusable_progress_bar.render_finish()

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


@objectstorage_cli.object_group.command(name='resume-put')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help="The file to load as the content of the object.")
@cli_util.option('--name',
                 help='The name of the object. Default value is the filename excluding the path.')
@cli_util.option('--upload-id', required=True, help='Upload ID to resume.')
@cli_util.option('--part-size', type=click.INT,
                 help='Part size in MiB')
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, 1000), default=None,
                 help='This option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads. Defaults to 3 and the maximum is 1000.')
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_resume_put(ctx, from_json, namespace, bucket_name, name, file, upload_id, part_size, disable_parallel_uploads, parallel_upload_count):
    """
    Resume a previous multipart put.

    Example:
        oci os object resume-put -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt --upload-id my-upload-id
    """
    kwargs = {}

    if parallel_upload_count is not None and disable_parallel_uploads:
        raise click.UsageError('The option --parallel-upload-count is not applicable when using the --disable-parallel-uploads flag.')

    if part_size is not None:
        kwargs['part_size'] = part_size * MEBIBYTE

    # Don't accept stdin with resume-put
    if file.name == '<stdin>':
        raise click.UsageError('Stdin is not supported by resume-put')

    # default object name is filename without path
    if not name:
        if not hasattr(file, 'name'):
            raise click.UsageError('The --file must have a name attribute, or --name must be specified')
        name = os.path.basename(file.name)

    client = build_client('object_storage', 'object_storage', ctx)

    total_size = os.fstat(file.fileno()).st_size
    if total_size > 0:
        upload_manager_kwargs = {}
        if disable_parallel_uploads:
            upload_manager_kwargs['allow_parallel_uploads'] = False

        if parallel_upload_count is not None:
            upload_manager_kwargs['parallel_process_count'] = parallel_upload_count

        upload_manager = UploadManager(client, **upload_manager_kwargs)

        with ProgressBar(total_size, 'Uploading object') as bar:
            kwargs['progress_callback'] = bar.update
            response = upload_manager.resume_upload_file(namespace, bucket_name, name, file.name, upload_id, **kwargs)

        display_headers = filter_object_headers(response.headers, OBJECT_PUT_DISPLAY_HEADERS)
        render(None, display_headers, ctx, display_all_headers=True)


@cli_util.copy_params_from_generated_command(objectstorage_cli.restore_objects, params_to_exclude=['namespace_name', 'bucket_name', 'object_name'])
@objectstorage_cli.object_group.command(name='restore', help=objectstorage_cli.restore_objects.help)
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help="""The top-level namespace used for the request.""")
@cli_util.option('-bn', '--bucket', '--bucket-name', 'bucket_name', required=True, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--name', required=True, help="""A object which was in an archived state and need to be restored.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def restore_objects(ctx, **kwargs):
    details = {}

    namespace = kwargs['namespace']
    bucket = kwargs['bucket_name']
    name = kwargs['name']

    details['objectName'] = name

    if kwargs['hours'] is not None:
        details['hours'] = kwargs['hours']

    client = build_client('object_storage', 'object_storage', ctx)
    kwargs = {'opc_client_request_id': ctx.obj['request_id']}
    result = client.restore_objects(
        namespace_name=namespace,
        bucket_name=bucket,
        restore_objects_details=details,
        **kwargs
    )

    if result.status == 200:
        click.echo("This object will be available for download in about 4 hours. Use 'oci os object restore-status -ns {ns} -bn {bn} --name {name}' command to check the status.".format(ns=namespace, bn=bucket, name=name), file=sys.stderr)
    else:
        render_response(result, ctx)


@objectstorage_cli.object_group.command(name='restore-status')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--name', required=True, help='The name of the object.')
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def restore_status(ctx, from_json, namespace, bucket_name, name):
    """
    Gets the restore status for an object.

    Example:
        oci os object restore-status -ns mynamespace -bn mybucket --name myfile.txt
    """
    client = build_client('object_storage', 'object_storage', ctx)
    response = client.head_object(
        namespace,
        bucket_name,
        name,
        opc_client_request_id=ctx.obj['request_id'])

    archival_state = response.headers.get('archival-state', None)

    if archival_state is None:
        msg = "Available, this object is available for download."
    elif archival_state.lower() == 'archived':
        msg = "Archived, this object is not available for download. Use 'oci os object restore -ns {ns} -bn {bn} --name {name}' command to start restoring the object.".format(ns=namespace, bn=bucket_name, name=name)
    elif archival_state.lower() == 'restoring':
        msg = "Restoring, this object is being restored and will be available for download in about 4 hours from the time you issued the restore command."
    elif archival_state.lower() == 'restored':
        try:
            # expected format: Literal Z at the end for UTC with milliseconds
            time_of_archival = response.headers['time-of-archival']
            time_of_archival_dt = arrow.get(time_of_archival, 'YYYY-MM-DDTHH:mm:ss.SSS[Z]')
            diff = time_of_archival_dt - arrow.utcnow()
            time_left = time_delta(diff.days, diff.seconds)
            msg = "Restored. You have {} to download the restored object before it is once again archived.".format(time_left)
        except arrow.parser.ParserError:
            msg = "Restored. The object will be re-archived at {}.".format(time_of_archival)
    else:
        msg = "Unknown"

    click.echo(msg, file=sys.stderr)


def time_delta(days, remaning_secs_in_day):
    hours, seconds = divmod(remaning_secs_in_day, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days == 0 and hours == 0 and minutes == 0:
        return 'less than 1 minute'

    days_str = "1 day" if days == 1 else "{} days".format(days)
    hours_str = "1 hour" if hours == 1 else "{} hours".format(hours)
    minutes_str = "1 min" if minutes == 1 else "{} mins".format(minutes)

    return ' '.join([days_str, hours_str, minutes_str])


@click.command(name='multipart', cls=CommandGroupWithAlias)
@help_option_group
def multipart():
    pass


@click.command(name='abort')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('-on', '--object-name', required=True, help='The name of the object.')
@cli_util.option('--upload-id', required=True, help='Upload ID to abort.')
@cli_util.option('--force', is_flag=True, help='Abort the existing multipart upload without a confirmation prompt.')
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def multipart_abort(ctx, from_json, namespace, bucket_name, object_name, upload_id, force):
    """
    Aborts an uncommitted multipart upload

    Example:
        oci os multipart abort -ns mynamespace -bn mybucket --object-name myfile.txt --upload-id my-upload-id
    """
    client = build_client('object_storage', 'object_storage', ctx)

    if not force:
        try:
            response = client.list_multipart_upload_parts(namespace, bucket_name, object_name, upload_id, limit=1)
            render_response(response, ctx)
            if response.status == 200:
                if not click.confirm("WARNING: Are you sure you want to permanently remove this incomplete upload?"):
                    ctx.abort()
        except exceptions.ServiceError:
            raise

    render_response(client.abort_multipart_upload(namespace, bucket_name, object_name, upload_id), ctx)


@cli_util.copy_params_from_generated_command(objectstorage_cli.copy_object, params_to_exclude=['destination_object_name', 'destination_region', 'destination_namespace'] + SSE_PARAMS + SOURCE_SSE_PARAMS)
@objectstorage_cli.object_group.command(name='copy', help=objectstorage_cli.copy_object.help)
@cli_util.option('--destination-region', help="""The destination region object will be copied to.""")
@cli_util.option('--destination-namespace', help="""The destination namespace object will be copied to.""")
@cli_util.option('--destination-object-name', help="""The destination name for the copy object.""")
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--source-encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the source object.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({'destination-object-metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def copy_object(ctx, **kwargs):
    if 'source_object_name' in kwargs and ('destination_object_name' not in kwargs or kwargs['destination_object_name'] is None):
        kwargs['destination_object_name'] = kwargs['source_object_name']
    if 'destination_namespace' not in kwargs or kwargs['destination_namespace'] is None:
        client = build_client('object_storage', 'object_storage', ctx)
        kwargs['destination_namespace'] = client.get_namespace().data
    if 'destination_region' not in kwargs or kwargs['destination_region'] is None:
        kwargs['destination_region'] = ctx.obj['config']['region']
    if 'encryption_key_file' in kwargs:
        sse_args = _get_encryption_key_params(kwargs['encryption_key_file'])
        if sse_args:
            kwargs.update(sse_args)
        del kwargs['encryption_key_file']
    if 'source_encryption_key_file' in kwargs:
        sse_args = _get_source_encryption_key_params(kwargs['source_encryption_key_file'])
        if sse_args:
            kwargs.update(sse_args)
        del kwargs['source_encryption_key_file']
    ctx.invoke(objectstorage_cli.copy_object, **kwargs)


objectstorage_cli.replication_group.commands.pop(objectstorage_cli.create_replication_policy.name)


@cli_util.copy_params_from_generated_command(objectstorage_cli.create_replication_policy, params_to_exclude=['destination_region_name', 'destination_bucket_name'])
@objectstorage_cli.replication_group.command(name='create-replication-policy', help=objectstorage_cli.create_replication_policy.help)
@cli_util.option('--destination-region', required=True, help=copy_help_from_generated_code(objectstorage_cli.create_replication_policy, 'destination_region_name', remove_required=True))
@cli_util.option('--destination-bucket', required=True, help=copy_help_from_generated_code(objectstorage_cli.create_replication_policy, 'destination_bucket_name', remove_required=True))
@click.pass_context
def create_replication_policy(ctx, **kwargs):
    if 'destination_bucket' in kwargs:
        kwargs['destination_bucket_name'] = kwargs['destination_bucket']
        kwargs.pop('destination_bucket')
    if 'destination_region' in kwargs:
        kwargs['destination_region_name'] = kwargs['destination_region']
        kwargs.pop('destination_region')
    ctx.invoke(objectstorage_cli.create_replication_policy, **kwargs)


@cli_util.copy_params_from_generated_command(objectstorage_cli.reencrypt_object,
                                             params_to_exclude=SSE_REENCRYPT_OBJECT_PARAMS)
@objectstorage_cli.object_group.command(name='reencrypt', help=objectstorage_cli.reencrypt_object.help)
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--source-encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the source object.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def reencrypt_object(ctx, **kwargs):
    if 'encryption_key_file' in kwargs:
        sse_json = _get_sse_customer_key_details(kwargs['encryption_key_file'])
        if sse_json:
            kwargs.update({'sse_customer_key': sse_json})
        del kwargs['encryption_key_file']
    if 'source_encryption_key_file' in kwargs:
        sse_json = _get_sse_customer_key_details(kwargs['source_encryption_key_file'])
        if sse_json:
            kwargs.update({'source_sse_customer_key': sse_json})
        del kwargs['source_encryption_key_file']
    ctx.invoke(objectstorage_cli.reencrypt_object, **kwargs)


objectstorage_cli.make_bucket_writable.help += " If you are replicating to a destination bucket in a different region, you must specify the --region parameter."
objectstorage_cli.list_replication_sources.help += " If you are replicating to a destination bucket in a different region, you must specify the --region parameter."


objectstorage_cli.os_root_group.add_command(multipart)
objectstorage_cli.list_multipart_uploads.name = 'list'
get_param(objectstorage_cli.list_multipart_uploads, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.list_multipart_uploads, 'namespace_name').opts.extend(['--namespace', '-ns'])
multipart.add_command(objectstorage_cli.list_multipart_uploads)
multipart.add_command(multipart_abort)


# Overriding the generated command to simplify the --duration complex type parameter to it's simple constituent parts
# of --time-amount (int) and --time-unit (string enum)
@cli_util.copy_params_from_generated_command(objectstorage_cli.create_retention_rule, params_to_exclude=['duration'])
@objectstorage_cli.retention_rule_group.command(name=cli_util.override('create_retention_rule.command_name', 'create'), help=objectstorage_cli.create_retention_rule.help)
@cli_util.option('--time-amount', type=click.INT, help="""The amount of time that objects in the bucket should be preserved for and which is calculated in relation to each object's Last-Modified timestamp. If time-amount is not specified, then there is no time limit and the objects in the bucket will be preserved indefinitely.""")
@cli_util.option('--time-unit', type=custom_types.CliCaseInsensitiveChoice(["DAYS", "YEARS"]), help="""The unit that should be used to interpret time-amount""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_retention_rule(ctx, **kwargs):
    if kwargs['time_amount'] is not None:
        kwargs['duration'] = {'timeAmount': kwargs['time_amount']}
        if kwargs['time_unit'] is not None:
            kwargs['duration']['timeUnit'] = str(kwargs['time_unit']).upper()
        else:
            raise click.UsageError('Parameter --time-unit is required when --time-amount is specified')

    del kwargs['time_amount']
    del kwargs['time_unit']

    ctx.invoke(objectstorage_cli.create_retention_rule, **kwargs)


# Overriding the generated command and reimplement it. We can't use the generated command because of the following reason:
#   - We need a way to unset/remove the value of a field (--duration and --time-rule-locked) effectively
#     setting it to null
#     This was not possible with the generated command, it'll never allow a None to be passed to the backend
#   - Overriding the generated command to simplify the --duration complex type parameter to it's simple constituent parts
#     of --time-amount (int) and --time-unit (string enum)
@cli_util.copy_params_from_generated_command(objectstorage_cli.update_retention_rule, params_to_exclude=['duration', 'force', 'time_rule_locked'])
@objectstorage_cli.retention_rule_group.command(name='update', help=objectstorage_cli.update_retention_rule.help)
@cli_util.option('--time-amount', help="""The amount of time that objects in the bucket should be preserved for and which is calculated in relation to each object's Last-Modified timestamp. To unset it, specify an empty string.""")
@cli_util.option('--time-unit', type=custom_types.CliCaseInsensitiveChoice(["DAYS", "YEARS"]), help="""The unit that should be used to interpret time-amount""")
@cli_util.option('--time-rule-locked', help=u"""The date and time as per [RFC 3339] after which this rule is locked and can only be deleted by deleting the bucket. Once a rule is locked, only increases in the duration are allowed and no other properties can be changed. Specifying it when a duration is not specified is considered an error. This property cannot be updated for rules that are in a locked state. Before time-rule-locked has elapsed, it can be unset by specifying an empty string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_retention_rule(ctx, **kwargs):
    namespace_name = kwargs['namespace_name']
    bucket_name = kwargs['bucket_name']
    retention_rule_id = kwargs['retention_rule_id']

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(retention_rule_id, six.string_types) and len(retention_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --retention-rule-id cannot be whitespace or empty string')

    # Gather the values to be sent to the API as the body (UpdateRetentionRuleDetails)
    details = {}

    if kwargs['display_name'] is not None:
        details['displayName'] = kwargs['display_name']

    # Check if --time-amount option is provided
    if kwargs['time_amount'] is not None:
        # If --time-amount is provided and is either --time-amount= or --time-amount='', then the duration must be unset effectively
        # making it infinite duration
        if kwargs['time_amount'] == '':
            details['duration'] = None
        else:
            # convert the --time-amount value to an integer
            try:
                timeAmount = int(kwargs['time_amount'])
            except ValueError:
                raise click.BadParameter(kwargs['time_amount'] + ' is not a valid integer')

            duration = {'timeAmount': timeAmount}
            if kwargs['time_unit'] is not None:
                duration['timeUnit'] = str(kwargs['time_unit']).upper()
            else:
                raise click.UsageError('Parameter --time-unit is required when --time-amount is specified')

            # construct the duration field that will be sent to the backend handlers
            details['duration'] = cli_util.parse_json_parameter("duration", duration)

    # Check if --time-rule-locked option is provided
    if kwargs['time_rule_locked'] is not None:
        # Check if a value is provided for --time-rule-locked
        if kwargs['time_rule_locked'] == '':
            details['timeRuleLocked'] = None
        else:
            # CliDatetime.convert will throw a click.BadParameter exception if the value is not a valid datetime
            details['timeRuleLocked'] = custom_types.cli_datetime.CliDatetime().convert(kwargs['time_rule_locked'], None, ctx)

    # Extra arguments to be passed in to the client for making the API invocation
    args = {}
    if kwargs['if_match'] is not None:
        args['if_match'] = kwargs['if_match']
    args['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # Invoke the API and handle the response
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    result = client.update_retention_rule(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        retention_rule_id=retention_rule_id,
        update_retention_rule_details=details,
        **args
    )
    cli_util.render_response(result, ctx)


# Retrieves a single page of objects, retrying the call if we received a retryable exception. This will return the
# raw response and it is up to the caller to handle pagination etc
def retrying_list_objects_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, fields):
    args = {
        'fields': fields,
        'opc_client_request_id': request_id,
        'limit': limit
    }
    if delimiter is not None:
        args['delimiter'] = delimiter
    if prefix is not None:
        args['prefix'] = prefix
    if start:
        args['start'] = start
    if end is not None:
        args['end'] = end

    return _make_retrying_list_call(client, namespace, bucket_name, **args)


# Retrieves a single page of object versions, retrying the call if we received a retryable exception. This will return the
# raw response and it is up to the caller to handle pagination etc
def retrying_list_object_versions_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, page, fields):
    args = {
        'fields': fields,
        'opc_client_request_id': request_id,
        'limit': limit
    }
    if delimiter is not None:
        args['delimiter'] = delimiter
    if prefix is not None:
        args['prefix'] = prefix
    if start is not None:
        args['start'] = start
    if end is not None:
        args['end'] = end
    if page is not None:
        args['page'] = page

    return _make_retrying_list_versions_call(client, namespace, bucket_name, **args)


# Retrieves multiple pages of objects, retrying each list page call if we received a retryable exception. This will return a list of
# the raw responses we received in the order we received them
#
# This method can retrieve all matching objects or only up to a given limit. The default is only to retrieve up to the given limit
def retrying_list_objects(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, fields, retrieve_all=False):
    all_responses = list()

    if retrieve_all:
        response = retrying_list_objects_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, fields)
        all_responses.append(response)
        next_start = response.data.next_start_with

        while next_start:
            response = retrying_list_objects_single_page(client, request_id, namespace, bucket_name, prefix, next_start, end, limit, delimiter, fields)

            all_responses.append(response)
            next_start = response.data.next_start_with
    else:
        next_start = start
        while limit > 0:
            response = retrying_list_objects_single_page(client, request_id, namespace, bucket_name, prefix, next_start, end, limit, delimiter, fields)

            all_responses.append(response)
            next_start = response.data.next_start_with

            if next_start:
                limit -= len(response.data.objects)
            else:
                limit = 0

    return all_responses


# Retrieves multiple pages of object versions, retrying each list page call if we received a retryable exception. This will return a list of
# the raw responses we received in the order we received them
#
# This method can retrieve all matching object versions or only up to a given limit. The default is only to retrieve up to the given limit
def retrying_list_object_versions(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, page, fields, retrieve_all=False):
    all_responses = list()

    if retrieve_all:
        response = retrying_list_object_versions_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, page, fields)
        all_responses.append(response)
        page = response.headers.get('opc-next-page')

        while page:
            response = retrying_list_object_versions_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, page, fields)

            all_responses.append(response)
            page = response.headers.get('opc-next-page')
    else:
        while limit > 0:
            response = retrying_list_object_versions_single_page(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, page, fields)

            all_responses.append(response)
            page = response.headers.get('opc-next-page')

            if page:
                limit -= len(response.data.items)
            else:
                limit = 0

    return all_responses


# Normalizes the object name path of an object we're going to upload to object storage (e.g. a/b/c/object.txt) so that
# it uses the object storage delimiter character (/)
#
# On Unix filesystems this should be a no-op because the path separator is already the slash but on Windows systems this will replace
# the Windows path separator (\) with /
def normalize_object_name_path_for_object_storage(object_name_path, path_separator=os.sep):
    return object_name_path.replace(path_separator, '/')


# Calls list_object with retries:
#
#    - Max of 3 attempts
#    - Exponential back off of (2 ^ retries) seconds
#    - Random jitter between retries of 0-2 seconds
#    - Retry on timeouts, connection errors, internal server errors and throttles
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
       retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
def _make_retrying_list_call(client, namespace, bucket_name, **kwargs):
    return client.list_objects(
        namespace,
        bucket_name,
        **kwargs
    )


# Calls list_object_versions with retries:
#
#    - Max of 3 attempts
#    - Exponential back off of (2 ^ retries) seconds
#    - Random jitter between retries of 0-2 seconds
#    - Retry on timeouts, connection errors, internal server errors and throttles
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
       retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
def _make_retrying_list_versions_call(client, namespace, bucket_name, **kwargs):
    return client.list_object_versions(
        namespace,
        bucket_name,
        **kwargs
    )


# HEADs an object to retrieve its metadata. This has the following retry conditions:
#
#    - Max of 3 attempts
#    - Exponential back off of (2 ^ retries) seconds
#    - Random jitter between retries of 0-2 seconds
#    - Retry on timeouts, connection errors, internal server errors and throttles
#
# 404s are not retried but they will also not result in the exception bubbling up. Instead, they will result in None
# being returned
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
       retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
def _make_retrying_head_object_call(client, namespace, bucket_name, name, client_request_id):
    kwargs = {'opc_client_request_id': client_request_id}

    try:
        return client.head_object(namespace, bucket_name, name, **kwargs)
    except exceptions.ServiceError as e:
        if e.status == 404:
            return None
        else:
            raise


def _get_progress_bar_label(original_label, object_name, prefix='Processing'):
    if original_label:
        formatted_progress_bar_label = original_label
    else:
        # If the names are too long then we can end up with multiple progress bars since we overflow a single line. To prevent
        # this, make sure that the label won't consume more than half the terminal width
        terminal_width = click.termui.get_terminal_size()[0] / 2
        remaining_width = terminal_width - (len(prefix) + 1)

        if len(object_name) > remaining_width:
            object_name_to_use = object_name[(object_name.rfind('/') + 1):]
            object_name_length = len(object_name_to_use)
            if object_name_length > remaining_width or object_name_length == 0:
                object_name_to_use = 'item'
        else:
            object_name_to_use = object_name

        formatted_progress_bar_label = u'{} {}'.format(prefix, object_name_to_use)

    return formatted_progress_bar_label


def _success_upload_callback_add_item_to_dict(**kwargs):
    kwargs['target_dict'].update({kwargs['target_dict_key']: filter_object_headers(kwargs.get('work_pool_task_result').headers, OBJECT_PUT_DISPLAY_HEADERS)})


def _error_callback_add_item_to_dict(**kwargs):
    kwargs['target_dict'].update({kwargs['target_dict_key']: str(kwargs.get('callback_exception'))})


def _print_to_console(**kwargs):
    click.echo(kwargs['message'], file=sys.stderr)


def _get_file_filter_collection(base_directory, include, exclude, object_prefix):
    file_filter_collection = None
    if include:
        file_filter_collection = SingleTypeFileFilterCollection(base_directory, BaseFileFilterCollection.INCLUDE)
        for i in include:
            # If objects have a prefix with a path separator, we're going to transform that into part of the path
            # so a caller's --include and --exclude filters may not take that into account. Instead, try and do that
            # for them here
            if object_prefix and (object_prefix.find(os.sep) >= 0 or object_prefix.find('/') >= 0):
                file_filter_collection.add_filter(os.path.join(object_prefix, i))

            file_filter_collection.add_filter(i)
    elif exclude:
        file_filter_collection = SingleTypeFileFilterCollection(base_directory, BaseFileFilterCollection.EXCLUDE)
        for e in exclude:
            if object_prefix and (object_prefix.find(os.sep) >= 0 or object_prefix.find('/') >= 0):
                file_filter_collection.add_filter(os.path.join(object_prefix, e))

            file_filter_collection.add_filter(e)

    return file_filter_collection


# Returns a dictionary containing information about the customer-provided encryption key that is to be sent
# along with the request
def _get_encryption_key_params(encryption_key_file):
    return _get_sse_params(encryption_key_file, SSE_PARAMS)


# Returns a dictionary containing information about the customer-provided encryption key for the source object
# (of a copy operation). This information is sent via HTTP headers.
def _get_source_encryption_key_params(source_encryption_key_file):
    return _get_sse_params(source_encryption_key_file, SOURCE_SSE_PARAMS)


# Reads the base64-encoded AES key data from the specified file and computes its SHA256 checksum
# and returns a dictionary of key/value pairs that are sent as HTTP headers
def _get_sse_params(data_file, param_names):
    if data_file:
        key_data_base64_str = data_file.read()
        key_sha256 = hashlib.sha256(base64.b64decode(key_data_base64_str)).digest()
        key_sha256_base64_str = base64.b64encode(key_sha256).decode('utf-8')
        return {
            param_names[0]: SSE_ALGORITHM,
            param_names[1]: key_data_base64_str,
            param_names[2]: key_sha256_base64_str
        }
    return None


# Reads the base64-encoded AES key data from the specified file and computes its SHA256 checksum
# and returns a json representing the SSECustomerKeyDetails of the ReencryptObject API payload
def _get_sse_customer_key_details(data_file):
    if data_file:
        key_data_base64_str = data_file.read()
        key_sha256 = hashlib.sha256(base64.b64decode(key_data_base64_str)).digest()
        key_sha256_base64_str = base64.b64encode(key_sha256).decode('utf-8')
        return {
            'algorithm': SSE_ALGORITHM,
            'key': key_data_base64_str,
            'keySha256': key_sha256_base64_str
        }
    return None


class FileReadCallbackStream:
    def __init__(self, file, progress_callback):
        self.progress_callback = progress_callback
        self.file = file
        self.mode = file.mode

    # this is used by 'requests' to determine the Content-Length header using fstat
    def fileno(self):
        return self.file.fileno()

    def read(self, n):
        self.progress_callback(n)
        return self.file.read(n)


# This is a thin wrapper so that we can support updating the completion of individual parts when doing bulk multipart options (get or put) via the
# TransferManager. The TransferManager supports callbacks at the "task" completion level (and multipart-uploading an entire file
# is considered a part), but the underlying components it uses (MultipartObjectAssembler for multipart put and the GetObjectMultipartTask for gets)
# supports callbacks at the part level. This lets us hook into that
class BulkOperationMultipartUploadProgressBar:
    def __init__(self, progress_bar, total_bytes, label):
        self.label = label
        self.progress_bar = progress_bar  # This should be the below ProgressBar class, not a click.progressbar
        self.bytes_read = 0
        self.total_bytes = total_bytes

    def update(self, bytes_read, **kwargs):
        self.bytes_read += bytes_read
        if 'total_bytes' in kwargs:
            self.total_bytes = kwargs['total_bytes']

        self.progress_bar.reset_progress(self.total_bytes, self.label)
        self.progress_bar.update(self.bytes_read)


class ProgressBar:
    PROGRESS_BAR_GRANULARITY = 10000

    def __init__(self, total_bytes, label, next_part=None):
        self._total_bytes = total_bytes
        self._total_progress_bytes = 0
        self._last_progress = 0
        self._progressbar = click.progressbar(length=ProgressBar.PROGRESS_BAR_GRANULARITY,
                                              label=label, file=sys.stderr)

    def __enter__(self):
        self._progressbar.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self._progressbar.__exit__(exc_type, exc_value, tb)

    def update(self, bytes_read):
        self._total_progress_bytes += bytes_read
        current_progress = ProgressBar.PROGRESS_BAR_GRANULARITY * (float(self._total_progress_bytes) / self._total_bytes)
        if current_progress != self._last_progress:
            self._progressbar.update(current_progress - self._last_progress)
            self._last_progress = current_progress

    def update_indeterminate_size(self, bytes_read):
        self._total_progress_bytes += bytes_read

        # This should make the bar wrap around itself (i.e. it gets to the end and then resets)
        if self._total_progress_bytes >= self._total_bytes:
            self.reset_progress(self._total_bytes, self._progressbar.label)

        self.update(bytes_read)

    def reset_progress(self, total_bytes, new_label):
        self._progressbar.label = new_label
        self._progressbar.pos = 0
        self._progressbar.avg = []
        self._progressbar.finished = False

        self._total_bytes = total_bytes
        self._last_progress = 0
        self._total_progress_bytes = 0

    def update_label_to_end(self, new_label):
        self._progressbar.label = new_label
        self._progressbar.finished = True
        self._progressbar.render_progress()
        print()

    def render_finish(self):
        self._progressbar.render_finish()


class SingleUploadRetry():
    def __init__(self, object_storage_client, namespace_name, bucket_name, object_name, file_path, bar, total_size, **kwargs):
        self.object_storage_client = object_storage_client
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.file_path = file_path
        self.bar = bar
        self.total_size = total_size
        self.kwargs = kwargs.copy()  # Copy because we're going to potentially do some destructive stuff to the dict below

        # These are not valid for single uploads, so remove them if present
        self.kwargs.pop('allow_parallel_uploads', None)
        self.kwargs.pop('parallel_process_count', None)
        self.kwargs.pop('part_size', None)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
           retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def retrying_upload_file_call(self):
        if self.bar:
            self.bar.render_finish()
        click.echo("Retrying upload", file=sys.stderr)
        if self.total_size > 0:
            self.bar = ProgressBar(self.total_size, 'Uploading object')
            self.kwargs['progress_callback'] = self.bar.update
        upload_manager = UploadManager(self.object_storage_client, allow_multipart_uploads=False)
        return upload_manager.upload_file(self.namespace_name, self.bucket_name, self.object_name, self.file_path, **self.kwargs)


# A class to retry resume upload for failed multipart object put
class RetryResumeUpload():
    def __init__(self, ma, upload_id, total_size, bar):
        self.ma = ma
        self.upload_id = upload_id
        self.total_size = total_size
        self.bar = bar

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000, retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def retrying_resume_multipart_upload(self):
        self.bar.render_finish()
        click.echo("Retrying multipart upload", file=sys.stderr)

        try:
            with ProgressBar(self.total_size, 'Uploading object') as self.bar:
                resume_kwargs = {}
                resume_kwargs['progress_callback'] = self.bar.update
                self.ma.resume(upload_id=self.upload_id, **resume_kwargs)
        except RuntimeError as re:
            if 'thread' in str(re) or 'Thread' in str(re):
                raise Exception('Cannot start that many threads, please reduce the parallel-upload-count. The default is 3.')
            else:
                raise re
