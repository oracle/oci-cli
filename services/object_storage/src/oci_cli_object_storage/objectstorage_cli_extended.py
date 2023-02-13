# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import division
from __future__ import print_function

import base64
import datetime
import hashlib
import math
import os
import os.path
import stat
import sys
from mimetypes import guess_type

import arrow
import click
import dateutil.parser
import pytz
import six  # noqa: F401
from oci import exceptions
from oci.object_storage import UploadManager, MultipartObjectAssembler
from oci.object_storage.transfer import constants
from oci.retry import RetryStrategyBuilder

import oci_cli.cli_root as cli_root
import oci_cli.final_command_processor as final_command_processor
import services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager  # noqa: F401,E402
from oci_cli import cli_exceptions
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli.cli_util import render, render_response, parse_json_parameter, help_option, help_option_group, \
    build_client, wrap_exceptions, filter_object_headers, get_param, copy_help_from_generated_code, stream_page_object
from oci_cli.custom_types import BulkPutOperationOutput, BulkGetOperationOutput, BulkDeleteOperationOutput
from oci_cli.file_filters import BaseFileFilterCollection
from oci_cli.file_filters import SingleTypeFileFilterCollection
from services.object_storage.src.oci_cli_object_storage.generated import objectstorage_cli
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager import TransferManager, \
    TransferManagerConfig, WorkPoolTaskCallback, WorkPoolTaskErrorCallback, WorkPoolTaskSuccessCallback, \
    WorkPoolTaskCallbacksContainer
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.delete_tasks import \
    DeleteUploadTask, DeleteReplicationPolicyTask, DeletePreAuthenticatedRequestTask, DeleteObjectTask
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.wrapped_semaphore import \
    WrappedSemaphore


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
DEFAULT_PARALLEL_UPLOAD_COUNT = 10
MAXIMUM_PARALLEL_UPLOAD_COUNT = 1000
DEFAULT_PARALLEL_DOWNLOAD_COUNT = 10
MAXIMUM_PARALLEL_DOWNLOAD_COUNT = 1000
MULTIPART_MAX_RETRIES = 60

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
get_param(objectstorage_cli.update_object_storage_tier, 'namespace_name').opts.extend(['--namespace', '-ns'])
get_param(objectstorage_cli.update_object_storage_tier, 'bucket_name').opts.extend(['--bucket', '-bn'])


cli_util.rename_command(objectstorage_cli, objectstorage_cli.os_root_group, objectstorage_cli.namespace_group, "ns")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.namespace_group, objectstorage_cli.get_namespace_metadata, "get-metadata")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.namespace_group, objectstorage_cli.update_namespace_metadata, "update-metadata")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.os_root_group, objectstorage_cli.preauthenticated_request_group, "preauth-request")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.work_request_log_entry_group, objectstorage_cli.list_work_request_logs, "list")
cli_util.rename_command(objectstorage_cli, objectstorage_cli.object_group, objectstorage_cli.update_object_storage_tier, "update-storage-tier")

objectstorage_cli.os_root_group.help = "Object Storage Service CLI"
objectstorage_cli.os_root_group.short_help = "Object Storage Service"

objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_object_versions.name)

cli_util.override_command_short_help_and_help(objectstorage_cli.get_bucket, u"""Gets the current representation of the given bucket in the given Object Storage namespace. \n[Command Reference](getBucket)

Bucket  summary  includes  the  'namespace',  'name',  'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields.""")
cli_util.update_param_help(objectstorage_cli.get_bucket, 'fields', """This parameter can only include 'approximateCount' (approximate number of objects) and 'approximateSize' (total approximate size in bytes of all objects). For example '--fields approximateCount --fields approximateSize'.""", append=False)

cli_util.update_param_help(objectstorage_cli.update_object_storage_tier, 'bucket_name', """The name of the bucket. Example: `my-bucket1`""", append=False)
cli_util.update_param_help(objectstorage_cli.update_object_storage_tier, 'object_name', """The name of the object for which the storage tier needs to be changed.""", append=False)

# Create and store extended parameters which are used in multiple operations
content_type_option_help_text = 'The optional Content-Type header that defines the standard MIME type format of the object to be returned in GetObject and HeadObject responses. Content type defaults to \'application/octet-stream\' if not specified. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and perform special operations on text only objects.'
content_language_option_help_text = 'The optional Content-Language header that defines the content language of the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.'
content_encoding_option_help_text = 'The optional Content-Encoding header that defines the content encoding of the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.'
content_disposition_option_help_text = 'The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.'
cache_control_option_help_text = 'The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.'
metadata_option_help_text = 'Arbitrary string keys and values for user-defined metadata. This will be applied to all files being uploaded. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\''
storage_tier_option_help_text = 'The storage tier that the objects should be stored in. If not specified, the objects will be stored in the same storage tier as the bucket.'
no_follow_symlinks_option_help_text = 'Symbolic links will be ignored while traversing the local filesystem.'
no_multipart_option_help_text = 'Do not transfer the file in multiple parts. By default, files above 128 MiB will be transferred in multiple parts, then combined.'
parallel_operations_count_option_help_text = 'The number of parallel operations to perform. Decreasing this value will make the process less resource intensive but it may take longer. Increasing this value may decrease the time taken, but the process will consume more system resources and network bandwidth. The maximum is 1000.'
part_size_option_help_text = 'Part size (in MiB) to use when the file is split into multiple parts and then combined. Part size must be greater than 10 MiB and defaults to 128 MiB.'
include_option_help_text = """Only process files which match the specified pattern. Patterns are applied relative to the current directory. This option can be specified multiple times to match on multiple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN)
exclude_option_help_text = """Only process files which do not match the specified pattern. Patterns are applied relative to the current directory. This option can be specified multiple times to match on multiple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN)


@objectstorage_cli.object_group.command(name='list-object-versions', help=u"""Lists the object versions in a bucket.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.option('--namespace-name', '--namespace', '-ns', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', '--bucket', '-bn', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--prefix', help=u"""The string to use for matching against the start of object names in a list query.""")
@cli_util.option('--start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--delimiter', help=u"""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@cli_util.option('--fields', default='name,size,etag,md5,timeCreated,timeModified,storageTier,archivalState', show_default=True, help=u"""Object summary in list of objects includes the 'name' field. This parameter can also include 'size' (object size in bytes), 'etag', 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState'. Value of this parameter should be a comma-separated, case-insensitive list of those field names. For example 'name,size,etag,md5,timeCreated,timeModified,storageTier,archivalState' Allowed values are: name, size, etag, md5, timeCreated, timeModified, storageTier, archivalState.""")
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
@cli_util.option('--fields', default='name,size,etag,md5,timeCreated,timeModified,storageTier,archivalState', show_default=True, help="Object summary in list of objects includes the 'name' field. This parameter may also include "
                 "'size' (object size in bytes), 'md5', 'timeCreated' (object creation date and time), 'timeModified' (object modification date and time), 'storageTier' and 'archivalState' fields. "
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
@cli_util.option('--metadata', help=metadata_option_help_text)
@cli_util.option('--content-type', help=content_type_option_help_text)
@cli_util.option('--content-language', help=content_language_option_help_text)
@cli_util.option('--content-encoding', help=content_encoding_option_help_text)
@cli_util.option('--force', is_flag=True,
                 help='If the object name already exists, overwrite the existing object without a confirmation prompt.')
@cli_util.option('--no-overwrite', is_flag=True,
                 help='If the object name already exists, do not overwrite the existing object.')
@cli_util.option('--no-multipart', is_flag=True, help=no_multipart_option_help_text)
@cli_util.option('--part-size', type=click.INT, help=part_size_option_help_text)
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, MAXIMUM_PARALLEL_UPLOAD_COUNT), default=None,
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--verify-checksum', is_flag=True,
                 help='Verify the checksum of the uploaded object with the local file.')
@cli_util.option('--content-disposition', help=content_disposition_option_help_text)
@cli_util.option('--cache-control', help=cache_control_option_help_text)
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--storage-tier',
                 type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]),
                 help=storage_tier_option_help_text)
@cli_util.option('--opc-sse-kms-key-id', help=u"""The OCID of a master encryption key used to call the Key Management Service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}},
    output_type={'module': 'object_storage', 'class': 'ObjectSummary'})
@wrap_exceptions
def object_put(ctx, from_json, namespace, bucket_name, name, file, if_match, content_md5, metadata, content_type,
               content_language, content_encoding, force, no_overwrite, no_multipart, part_size,
               disable_parallel_uploads, parallel_upload_count, verify_checksum, content_disposition, cache_control,
               encryption_key_file, storage_tier, opc_sse_kms_key_id):
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
                sys.exit(0)
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

    if storage_tier is not None:
        kwargs['storage_tier'] = storage_tier

    if opc_sse_kms_key_id is not None:
        kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id

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

        # explicitly disallow retries for object put because we may not be able to re-read the input source
        ctx.obj['no_retry'] = True

        client = build_client('object_storage', 'object_storage', ctx)
        upload_manager = UploadManager(client)

        if disable_parallel_uploads:
            upload_manager.allow_parallel_uploads = False

        upload_manager.parallel_process_count = parallel_upload_count if parallel_upload_count else DEFAULT_PARALLEL_UPLOAD_COUNT

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

        kwargs['parallel_process_count'] = parallel_upload_count if parallel_upload_count is not None else DEFAULT_PARALLEL_UPLOAD_COUNT

        UploadManager._add_adapter_to_service_client(client, not disable_parallel_uploads, kwargs['parallel_process_count'])

        ma = MultipartObjectAssembler(client,
                                      namespace,
                                      bucket_name,
                                      name,
                                      **kwargs)

        ma.new_upload()
        click.echo('Upload ID: {}'.format(ma.manifest["uploadId"]), file=sys.stderr)
        ma.add_parts_from_file(file.name)
        click.echo('Split file into {} parts for upload.'.format(len(ma.manifest["parts"])), file=sys.stderr)

        max_attempts = MULTIPART_MAX_RETRIES if not ctx.obj['max_attempts'] else ctx.obj['max_attempts']

        # max_attempts retries - with exponential sleep time and a max wait of 60 secs.
        retry_strategy = RetryStrategyBuilder(retry_max_wait_between_calls_seconds=60).add_max_attempts(max_attempts)\
            .no_total_elapsed_time() \
            .add_service_error_check() \
            .get_retry_strategy()

        with ProgressBar(total_size, 'Uploading object') as bar:
            try:
                ma.upload(retry_strategy=retry_strategy, progress_callback=bar.update)
            except RuntimeError as re:
                if 'thread' in str(re) or 'Thread' in str(re):
                    raise Exception('Cannot start that many threads, please reduce the parallel-upload-count. The default is ' + str(DEFAULT_PARALLEL_UPLOAD_COUNT))
                else:
                    raise re
            except Exception as e:
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
@cli_util.option('--src-dir', required=True,
                 help='The directory which contains files to upload. Files in the directory and all subdirectories will be uploaded.')
@cli_util.option('--prefix', '--object-prefix', 'object_prefix', help='A prefix to apply to the names of all files being uploaded')
@cli_util.option('--metadata', help=metadata_option_help_text)
@cli_util.option('--content-type', help=content_type_option_help_text)
@cli_util.option('--content-language', help=content_language_option_help_text)
@cli_util.option('--content-encoding', help=content_encoding_option_help_text)
@cli_util.option('--cache-control', help=cache_control_option_help_text)
@cli_util.option('--content-disposition', help=content_disposition_option_help_text)
@cli_util.option('--storage-tier',
                 type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]),
                 help=storage_tier_option_help_text)
@cli_util.option('--overwrite', is_flag=True, help="""If a file being uploaded already exists in Object Storage with the same name, overwrite the existing object in Object Storage without a confirmation prompt. If neither this flag nor --no-overwrite is specified, you will be prompted each time an object with the same name would be overwritten.

Specifying this flag will also allow for faster uploads as the CLI will not initially check whether or not the files with the same name already exist in Object Storage.""")
@cli_util.option('--no-overwrite', is_flag=True,
                 help='If a file being uploaded already exists in Object Storage with the same name, do not overwite the object. If neither this flag nor --overwrite is specified, you will be prompted each time an object with the same name would be overwritten.')
@cli_util.option('--no-multipart', is_flag=True, help=no_multipart_option_help_text)
@cli_util.option('--part-size', type=click.INT, default=128, help=part_size_option_help_text)
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='[DEPRECATED] This option is no longer used. If a file in the directory will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel. This applies to all files being uploaded in multiple parts')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, MAXIMUM_PARALLEL_UPLOAD_COUNT),
                 default=DEFAULT_PARALLEL_UPLOAD_COUNT, show_default=True,
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--verify-checksum', is_flag=True,
                 help='Verify the checksum of the uploaded object with the local file.')
@cli_util.option('--include', multiple=True, help=include_option_help_text)
@cli_util.option('--exclude', multiple=True, help=exclude_option_help_text)
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--dry-run', is_flag=True, help="""Prints the list of files to be uploaded.""")
@cli_util.option('--no-follow-symlinks', is_flag=True, help=no_follow_symlinks_option_help_text)
@cli_util.option('--opc-sse-kms-key-id', help=u"""The OCID of a master encryption key used to call the Key Management Service to generate a data encryption key or to encrypt or decrypt a data encryption key.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@wrap_exceptions
def object_bulk_put(ctx, from_json, namespace, bucket_name, src_dir, object_prefix, metadata, content_type,
                    content_language, cache_control, content_disposition, content_encoding, storage_tier, overwrite,
                    no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count,
                    verify_checksum, include, exclude, encryption_key_file, opc_sse_kms_key_id, dry_run, no_follow_symlinks):
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

    client = cli_util.build_client('object_storage', 'object_storage', ctx)

    _, _, output = _bulk_upload(ctx, client, namespace, bucket_name, src_dir, cache_control, content_disposition,
                                content_encoding, content_language, content_type, dry_run, encryption_key_file,
                                exclude, include, metadata, no_multipart, no_overwrite, overwrite, parallel_upload_count,
                                part_size, object_prefix, storage_tier, verify_checksum,
                                no_follow_symlinks=no_follow_symlinks, opc_sse_kms_key_id=opc_sse_kms_key_id)

    if dry_run:
        sys.exit(0)

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


def _bulk_upload(ctx, client, namespace, bucket_name, src_dir, cache_control, content_disposition, content_encoding,
                 content_language, content_type, dry_run, encryption_key_file, exclude, include, metadata,
                 no_multipart, no_overwrite, overwrite, parallel_upload_count, part_size, prefix, storage_tier, verify_checksum,
                 syncing=False, no_follow_symlinks=True, opc_sse_kms_key_id=None):
    auto_content_type = False
    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided.')
    expanded_directory = os.path.expandvars(os.path.expanduser(src_dir))
    if not os.path.exists(expanded_directory):
        raise click.UsageError(
            'The specified --src-dir {} (expanded to: {}) does not exist'.format(src_dir, expanded_directory))
    else:
        if not os.access(expanded_directory, os.R_OK):
            raise click.UsageError(
                'The specified --src-dir {} (expanded to: {}) does not have read permissions'.format(src_dir, expanded_directory))

    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, None)

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together.')
    client_request_id = ctx.obj['request_id']
    base_kwargs = {'opc_client_request_id': client_request_id}

    # check if the bucket exists
    client.get_bucket(namespace, bucket_name, **base_kwargs)

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
    if content_disposition is not None:
        base_kwargs['content_disposition'] = content_disposition
    if cache_control is not None:
        base_kwargs['cache_control'] = cache_control
    if part_size is not None:
        base_kwargs['part_size'] = part_size * MEBIBYTE
    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            base_kwargs.update(sse_args)

    upload_output = BulkPutOperationOutput()
    if opc_sse_kms_key_id is not None:
        base_kwargs['opc_sse_kms_key_id'] = opc_sse_kms_key_id

    # Progress bar which we can reuse over and over again
    reusable_progress_bar = ProgressBar(0, '')
    multipart_max_retries = MULTIPART_MAX_RETRIES if not ctx.obj['max_attempts'] else ctx.obj['max_attempts']
    transfer_manager = TransferManager(
        client,
        TransferManagerConfig(
            max_object_storage_requests=parallel_upload_count,
            max_object_storage_multipart_requests=parallel_upload_count,
            max_multipart_files_to_process=parallel_upload_count,
            use_multipart_uploads=(not no_multipart),
            multipart_max_retries=multipart_max_retries
        )
    )
    head_object_results = {}
    upload_transfers = set()
    upload_skipped = set()
    # If we need to check for overwrites then we'll need to make HEAD object calls. We can queue these up in the
    # transfer_manager to be processed by the worker pool in the background so we potentially have to wait less per loop iteration.
    # This window variable controls how much (how many objects) we should look ahead by so that we make sure that all the HEAD requests
    # don't monopolise the processes in the transfer_manager's underlying pool of work
    parallel_head_object_look_ahead_window = int(parallel_upload_count / 2)
    for dir_name, subdir_list, file_list in os.walk(expanded_directory, followlinks=not no_follow_symlinks):
        empty_folder_flag = False  # Flag to be used for differentiating empty-folder upload
        if syncing and (not subdir_list) and (not file_list) and (dir_name != expanded_directory):  # Identifying empty_folder
            file_list = [os.sep]
            empty_folder_flag = True

        for idx, file in enumerate(file_list):
            if empty_folder_flag:  # As os.path.join does not work with filename as '/'
                full_file_path = dir_name + os.sep
            else:
                full_file_path = os.path.join(dir_name, file)

            # os.walk by default only skips the directories which are symlink. We need to check if any file symlink
            # is present and skip those if no_follow_symlink is specified
            if no_follow_symlinks and os.path.islink(full_file_path):
                continue

            if file_filter_collection:
                if file_filter_collection.get_action(full_file_path) == BaseFileFilterCollection.EXCLUDE:
                    continue

            object_name = normalize_file_path_for_object_storage(full_file_path[len(expanded_directory):])
            if is_python2():
                object_name = object_name.decode("utf-8")

            # If we start with a leading path separator (/), strip that from the object name so we get a hierarchy like:
            #    <subfolder1>/<subfolder2>/<object>
            # Rather than:
            #    /<subfolder1>/<subfolder2>/<object>
            if object_name[0] == '/':
                object_name = object_name[1:]

            if prefix:
                object_name = '{}{}'.format(prefix, object_name)

            # If content type is set to auto, then the CLI will guess the content type of the file
            if auto_content_type:
                base_kwargs['content_type'], _ = guess_type(object_name)
            try:
                if not overwrite:
                    if len(file_list) > (idx + parallel_head_object_look_ahead_window):
                        for i in range(parallel_head_object_look_ahead_window):
                            look_ahead_file_path = os.path.join(dir_name, file_list[idx + i])
                            look_ahead_object_name = normalize_file_path_for_object_storage(look_ahead_file_path[len(expanded_directory):])
                            look_ahead_file_path = normalize_file_path_for_object_storage(look_ahead_file_path)
                            if look_ahead_object_name[0] == '/':
                                look_ahead_object_name = look_ahead_object_name[1:]
                            if prefix:
                                look_ahead_object_name = '{}{}'.format(prefix, look_ahead_object_name)

                            if look_ahead_object_name not in head_object_results:
                                head_object_kwargs = {
                                    'namespace_name': namespace,
                                    'bucket_name': bucket_name,
                                    'object_name': look_ahead_object_name,
                                    'opc_client_request_id': client_request_id
                                }
                                head_object_results[look_ahead_object_name] = transfer_manager.head_object(
                                    WorkPoolTaskCallbacksContainer(), **head_object_kwargs)

                    if is_python2():
                        object_name = object_name.encode("utf-8")

                    # Pull the result from the future (this will block until the result is available) or,
                    # if we don't have a future, just make a request
                    if object_name in head_object_results:
                        head_object = head_object_results.pop(object_name).result()
                    else:
                        head_object = _make_retrying_head_object_call(client, namespace, bucket_name, object_name,
                                                                      client_request_id)
                    if head_object is None:
                        # Object does not exist, so make sure that the put fails if one is created in the meantime.
                        base_kwargs['if_none_match'] = '*'
                    else:
                        if empty_folder_flag:           # Skipping download in case of empty folder, if folder exists in bucket
                            upload_output.add_skipped(object_name)
                            upload_skipped.add(object_name)
                            continue
                        r_file_size = int(head_object.headers['content-length'])
                        r_file_mtime = dateutil.parser.parse(head_object.headers['last-modified'])
                        if no_overwrite or (syncing and not requires_sync(full_file_path, r_file_size, r_file_mtime)):
                            upload_output.add_skipped(object_name)
                            upload_skipped.add(object_name)
                            continue

                        base_kwargs['if_match'] = head_object.headers['etag']

                        if not syncing and not click.confirm(
                                'WARNING: {} already exists. Are you sure you want to overwrite it?'.format(
                                    object_name)):
                            upload_output.add_skipped(object_name)
                            upload_skipped.add(object_name)
                            base_kwargs.pop('if_match')     # clear set if_match header for next object iteration
                            continue

                upload_transfers.add(object_name)
                file_size = os.stat(full_file_path).st_size
                full_file_path = normalize_file_path_for_object_storage(full_file_path)
                if dry_run:
                    if syncing:
                        print("Uploading file:", end=" ")
                    print(full_file_path)
                    continue

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': u'Uploaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Uploaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end,
                                                                    **update_progress_kwargs)

                error_callback_kwargs = {'failed_item': object_name}
                success_callback_kwargs = {'uploaded_object': object_name}

                add_to_uploaded_objects_callback = WorkPoolTaskSuccessCallback(upload_output.add_uploaded,
                                                                               **success_callback_kwargs)
                add_to_upload_failures_callback = WorkPoolTaskErrorCallback(upload_output.add_failure,
                                                                            **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback],
                                                                     success_callbacks=[
                                                                         add_to_uploaded_objects_callback],
                                                                     error_callbacks=[add_to_upload_failures_callback])

                if ctx.obj['debug']:
                    click.echo('Uploading {}'.format(full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Uploading'))

                if not ctx.obj['debug']:
                    base_kwargs['multipart_part_completion_callback'] = BulkOperationMultipartUploadProgressBar(
                        reusable_progress_bar, file_size,
                        _get_progress_bar_label(None, object_name, 'Uploading parts for')).update

                if is_python2():
                    object_name = object_name.encode("utf-8")

                if storage_tier:
                    base_kwargs['storage_tier'] = storage_tier

                if empty_folder_flag:  # Using different method of uploading in case of empty_folder
                    transfer_manager.upload_empty_object(callbacks_container, namespace, bucket_name, object_name, verify_checksum, **base_kwargs)
                else:
                    transfer_manager.upload_object(callbacks_container, namespace, bucket_name, object_name,
                                                   full_file_path,
                                                   file_size, verify_checksum, **base_kwargs)

                # These can vary per request, so remove them if they exist so we have a blank slate for the next iteration
                base_kwargs.pop('if_none_match', None)
                base_kwargs.pop('if_match', None)
                base_kwargs.pop('multipart_part_completion_callback', None)
            except Exception as e:
                # Don't let one failure here (either HEADing to see if the object exists, or actaully uploading the object)
                # fail the entire batch, but store the error for output later
                upload_output.add_failure(object_name, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo('Failed to upload {}'.format(object_name), file=sys.stderr)
    if not dry_run:
        transfer_manager.wait_for_completion()
        reusable_progress_bar.render_finish()

    return upload_transfers, upload_skipped, upload_output


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
@cli_util.option('--multipart-download-threshold', type=click.IntRange(128, None), default=128, help='Objects larger than this size (in MiB) will be downloaded in multiple parts. The minimum allowable threshold is 128 MiB.')
@cli_util.option('--part-size', type=click.IntRange(128, None), help=part_size_option_help_text)
@cli_util.option('--parallel-download-count', type=click.IntRange(1, MAXIMUM_PARALLEL_DOWNLOAD_COUNT), default=DEFAULT_PARALLEL_DOWNLOAD_COUNT, show_default=True,
                 help='The number of parallel operations to perform when downloading an object in multiple parts. Decreasing this value will make multipart downloads less resource intensive but they may take longer. Increasing this value may improve download times, but the download process will consume more system resources and network bandwidth.')
@cli_util.option('--no-multipart', is_flag=True, help=no_multipart_option_help_text)
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
def object_get(ctx, from_json, namespace, bucket_name, name, file, version_id, if_match, if_none_match, range, multipart_download_threshold, part_size, parallel_download_count, no_multipart, encryption_key_file, http_response_content_disposition, http_response_cache_control, http_response_content_type, http_response_content_language, http_response_content_encoding, http_response_expires):
    """
    Gets the metadata and body of an object.

    Example:
        oci os object get -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt
    """

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
    if range or no_multipart or (multipart_download_threshold and part_size >= object_size_bytes):
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
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True,
                 help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--prefix',
                 help='Retrieve all objects with the given prefix. Omit this parameter to get all objects in the bucket')
@cli_util.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                                     "delimiter character (after an optionally specified prefix) are returned. "
                                     "Scanned objects whose names contain the delimiter have part of their name "
                                     "up to the last occurrence of the delimiter (after the optional prefix) "
                                     "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                                     "character at this time.")
@cli_util.option('--dest-dir', '--download-dir', 'download_dir', required=True,
                 help='The directory where retrieved objects will be placed as files. This directory will be created if it does not exist.')
@cli_util.option('--overwrite', is_flag=True,
                 help='If a file with the same name as an object already exists in the download directory, overwrite it. If neither this flag nor --no-overwrite is specified, you will be prompted each time a file would be overwritten.')
@cli_util.option('--no-overwrite', is_flag=True,
                 help='If a file with the same name as an object already exists in the download directory, do not overwite it. If neither this flag nor --overwrite is specified, you will be prompted each time a file would be overwritten')
@cli_util.option('--parallel-operations-count', type=click.IntRange(1, MAXIMUM_PARALLEL_DOWNLOAD_COUNT),
                 default=DEFAULT_PARALLEL_DOWNLOAD_COUNT, show_default=True,
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--multipart-download-threshold', type=click.IntRange(128, None), default=128,
                 help='Objects larger than this size (in MiB) will be downloaded in multiple parts. The minimum allowable threshold is 128 MiB.')
@cli_util.option('--no-multipart', is_flag=True, help=no_multipart_option_help_text)
@cli_util.option('--part-size', type=click.IntRange(128, None), default=128, help=part_size_option_help_text)
@cli_util.option('--include', multiple=True, help=include_option_help_text)
@cli_util.option('--exclude', multiple=True, help=exclude_option_help_text)
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--dry-run', is_flag=True, help="""Prints the list of files to be downloaded.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_get(ctx, from_json, namespace, bucket_name, prefix, delimiter, download_dir, overwrite, no_overwrite, include, exclude, parallel_operations_count, multipart_download_threshold, no_multipart, part_size, encryption_key_file, dry_run):
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

    client = build_client('object_storage', 'object_storage', ctx)

    _, _, output = _bulk_download(ctx, client, namespace, bucket_name, download_dir, dry_run, delimiter,
                                  encryption_key_file, exclude, include, multipart_download_threshold, no_multipart,
                                  no_overwrite, overwrite, parallel_operations_count, part_size, prefix)

    if dry_run:
        sys.exit(0)

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


def _bulk_download(ctx, client, namespace, bucket_name, dest_dir, dry_run, delimiter, encryption_key_file, exclude,
                   include, multipart_download_threshold, no_multipart, no_overwrite, overwrite,
                   parallel_operations_count, part_size, prefix, syncing=False):
    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided.')

    part_size = part_size * MEBIBYTE

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together.')
    expanded_directory = os.path.expandvars(os.path.expanduser(dest_dir))
    if not os.path.exists(expanded_directory):
        os.makedirs(expanded_directory)
    else:
        if not os.access(expanded_directory, os.W_OK):
            raise click.UsageError('The specified --dest-dir {} (expanded to: {}) does not have write permissions'.format(dest_dir, expanded_directory))

    kwargs = {
        'request_id': ctx.obj['request_id'],
        'namespace': namespace,
        'bucket_name': bucket_name,
        'prefix': prefix,
        'start': None,
        'end': None,
        'limit': OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
        'delimiter': delimiter,
        'fields': 'name,size,timeModified,archivalState'
    }
    keep_paginating = True
    ask_overwrite = not (overwrite or no_overwrite or syncing or dry_run)
    encryption_key_params = {}
    if encryption_key_file:
        sse_args = _get_encryption_key_params(encryption_key_file)
        if sse_args:
            encryption_key_params = sse_args
    download_output = BulkGetOperationOutput()
    # Progress bar which we can reuse over and over again
    reusable_progress_bar = ProgressBar(0, '')
    transfer_manager = TransferManager(client,
                                       TransferManagerConfig(max_object_storage_requests=parallel_operations_count))
    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, prefix)
    files_to_process = []
    download_transfers = set()
    download_skipped = set()
    try:
        while keep_paginating:
            list_objects_response = retrying_list_call_single_page(client.list_objects, **kwargs)
            next_start = list_objects_response.data.next_start_with
            to_download = []

            if next_start is not None and ask_overwrite:
                if click.confirm("You are downloading more than {} objects, do you want to overwrite all?".format(
                        OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS)):
                    overwrite = True
                ask_overwrite = False

            # Process the current batch and write to disk
            for obj in list_objects_response.data.objects:
                object_name = obj.name

                # For syncing we want to strip the prefix if provided
                if syncing and prefix is not None:
                    object_name = object_name[len(prefix):]

                # If the object name starts with the path separator (account for Unix and Windows paths) then remove it when we
                # do the joining to create a full file name, otherwise we could get an unexpected result
                object_name = normalize_file_path_for_object_storage(object_name)
                if object_name[0] == '/':
                    object_name = object_name[1:]
                full_file_path = os.path.join(expanded_directory, object_name)
                if file_filter_collection:
                    if file_filter_collection.get_action(full_file_path) == BaseFileFilterCollection.EXCLUDE:
                        continue

                # We skip the objects in the Archived/Restoring state and don't consider them for further evaluations
                normalized_full_file_path = normalize_file_path_for_object_storage(full_file_path)
                if syncing and obj.archival_state and obj.archival_state.lower() != 'restored':
                    download_output.add_skipped(obj.name)
                    download_skipped.add(normalized_full_file_path)
                    continue

                # HEAD operation doesn't have microsecond information which is being used while uploading. To have
                # a balance between upload and download ignoring the microsecond information while listing objects.
                last_modified = obj.time_modified.replace(microsecond=0)
                if os.path.exists(full_file_path):
                    if os.path.isdir(full_file_path):
                        download_output.add_skipped(obj.name)
                        download_skipped.add(normalized_full_file_path)
                        continue

                    # for syncing we add an additional behaviour to check for the size and last modified time between
                    # source and destination
                    not_syncing = syncing and not requires_sync(full_file_path, obj.size, last_modified, to_remote=False)
                    if not overwrite and (no_overwrite or not_syncing):
                        download_output.add_skipped(obj.name)
                        download_skipped.add(normalized_full_file_path)
                        continue

                    if not overwrite and not dry_run and not syncing:
                        confirm = click.prompt(
                            'WARNING: {} already exists. Are you sure you want to overwrite it? [y/N/yes to (a)ll]'.format(
                                object_name), default='N', type=custom_types.CliCaseInsensitiveChoice(["Y", "N", "A"]))
                        if confirm == 'N':
                            download_output.add_skipped(obj.name)
                            download_skipped.add(normalized_full_file_path)
                            continue
                        elif confirm == 'A':
                            overwrite = True

                dl_obj = {
                    "name": obj.name,
                    "size": obj.size,
                    "full_file_path": normalized_full_file_path
                }
                to_download.append(dl_obj)
                download_transfers.add(normalized_full_file_path)
                if syncing:
                    files_to_process.append({"last_modified": last_modified, "full_file_path": normalized_full_file_path})
                list_objects_response = None
            if dry_run:
                for obj in to_download:
                    if syncing:
                        click.echo(click.style("Downloading object: {}").format(obj['name']))
                    else:
                        click.echo(click.style("{}").format(obj['name']))

            else:
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
                            'object_name': object_name,
                            'full_file_path': full_file_path,
                            'request_id': ctx.obj['request_id']
                        }
                        get_object_kwargs.update(encryption_key_params)

                        if ctx.obj['debug']:
                            update_progress_kwargs = {'message': 'Downloaded {}'.format(object_name)}
                            update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                        else:
                            update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Downloaded')}
                            update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end,
                                                                            **update_progress_kwargs)

                        error_callback_kwargs = {'failed_item': object_name}
                        success_callback_kwargs = {'downloaded_object': object_name}
                        add_to_downloaded_objects_callback = WorkPoolTaskSuccessCallback(download_output.add_downloaded,
                                                                                         **success_callback_kwargs)
                        add_to_download_failures_callback = WorkPoolTaskErrorCallback(download_output.add_failure,
                                                                                      **error_callback_kwargs)

                        callbacks_container = WorkPoolTaskCallbacksContainer(
                            success_callbacks=[add_to_downloaded_objects_callback],
                            completion_callbacks=[update_progress_callback],
                            error_callbacks=[add_to_download_failures_callback])

                        if ctx.obj['debug']:
                            click.echo('Downloading {} to {}'.format(object_name, full_file_path), file=sys.stderr)
                        else:
                            reusable_progress_bar.reset_progress(100,
                                                                 _get_progress_bar_label(None, object_name, 'Downloading'))

                        # If it's not multipart, or it is but we would only have a single part then just download it, otherwise do a multipart get
                        # If the part size is somehow not known then use a multipart download by default (the multipart download will
                        # try and figure out the size via a HEAD and then take the appropriate action based on the size and threshold)
                        if no_multipart or (multipart_download_threshold and (object_size is not None and part_size >= object_size)):
                            transfer_manager.get_object(callbacks_container, **get_object_kwargs)
                        else:
                            if object_size:
                                multipart_callback_reference = BulkOperationMultipartUploadProgressBar(
                                    reusable_progress_bar, object_size,
                                    _get_progress_bar_label(None, object_name, 'Downloading part for')).update

                                get_object_kwargs['total_size'] = object_size
                                if not ctx.obj['debug']:
                                    get_object_kwargs['chunk_written_callback'] = multipart_callback_reference
                                    get_object_kwargs['part_completed_callback'] = multipart_callback_reference
                            else:
                                multipart_callback_reference = BulkOperationMultipartUploadProgressBar(
                                    reusable_progress_bar, 5 * part_size,
                                    _get_progress_bar_label(None, object_name, 'Downloading part for')).update

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
                        download_output.add_failure(object_name, callback_exception=e)

                        if ctx.obj['debug']:
                            click.echo('Failed to download {}'.format(object_name), file=sys.stderr)

            # Keep going if we have more pages
            kwargs['start'] = next_start
            keep_paginating = (next_start is not None)

        if not dry_run:
            transfer_manager.wait_for_completion()
            reusable_progress_bar.render_finish()

    # ensure that we always set the last mod time
    finally:
        if not dry_run and syncing:
            update_local_file_mtime(files_to_process)

    return download_transfers, download_skipped, download_output


def update_local_file_mtime(files_to_process):
    for file in files_to_process:
        try:
            m_time = file['last_modified'].timestamp()
            os.utime(file['full_file_path'], (m_time, m_time))
        except FileNotFoundError:
            # we might have situations where the file was sent to transfer_manager but not downloaded yet.
            # So it'd be present in the list but not in file system
            continue


@objectstorage_cli.object_group.command(name='sync',
                                        help='Synchronizes a filesystem directory with objects in a bucket. '
                                             'Traverses sub-directories copying new and modified files or objects '
                                             'from the source to the destination and optionally deleting those '
                                             'that are not present in the source.')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True,
                 help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--src-dir',
                 help='Required when not specifying --dest-dir. The directory from which the files will be synced to a bucket as objects. A local file will require uploading if the size of the local file is different than the size of the object, the last modified time of the local file is newer than the last modified time of the object, or the local file does not exist under the specified bucket and prefix.')
@cli_util.option('--dest-dir',
                 help='Required when not specifying --src-dir. The directory into which objects in a bucket will be synced as files. This directory will be created if it does not exist. An object will require downloading if it does not exist in the local directory or if it exists, either the size of the object differs from the size of the local file or the last modified time of the object is newer than the last modified time of the local file. Objects in Archive tier which have not been restored will not be downloaded.')
@cli_util.option('--cache-control', help=cache_control_option_help_text)
@cli_util.option('--content-disposition', help=content_disposition_option_help_text)
@cli_util.option('--content-encoding', help=content_encoding_option_help_text)
@cli_util.option('--content-language', help=content_language_option_help_text)
@cli_util.option('--content-type', help=content_type_option_help_text)
@cli_util.option('--delete', is_flag=True,
                 help='delete files/objects that exist in the destination but not in the source. No files or objects are deleted by default.')
@cli_util.option('--dry-run', is_flag=True,
                 help='Prints the list of files that would be uploaded, downloaded or deleted without actually performing any actions.')
@cli_util.option('--encryption-key-file', type=click.File(mode='r'),
                 help="""A file containing the base64-encoded string of the AES-256 encryption key associated with the object.""")
@cli_util.option('--exclude', multiple=True, help=exclude_option_help_text)
@cli_util.option('--include', multiple=True, help=include_option_help_text)
@cli_util.option('--metadata', help=metadata_option_help_text)
@cli_util.option('--no-follow-symlinks', is_flag=True, help=no_follow_symlinks_option_help_text)
@cli_util.option('--no-multipart', is_flag=True, help=no_multipart_option_help_text)
@cli_util.option('--parallel-operations-count', type=click.IntRange(1, MAXIMUM_PARALLEL_DOWNLOAD_COUNT), default=DEFAULT_PARALLEL_DOWNLOAD_COUNT, show_default=True,
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--part-size', type=click.IntRange(128, None), default=128, help='Part size (in MiB) to use when downloading an object in multiple parts. The minimum allowable size is 128 MiB.')
@cli_util.option('--prefix', help='When specified with --src-dir, the files are uploaded as objects with the specified prefix. When specified with --dest-dir, only objects with the specified prefix are downloaded but the prefix is not added to the file names.')
@cli_util.option('--storage-tier',
                 type=custom_types.CliCaseInsensitiveChoice(["Standard", "InfrequentAccess", "Archive"]),
                 help=storage_tier_option_help_text)
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@wrap_exceptions
def sync(ctx, from_json, namespace, bucket_name, src_dir, dest_dir, cache_control, content_disposition, content_encoding,
         content_language, content_type, delete, dry_run, encryption_key_file, exclude, include, metadata,
         no_follow_symlinks, no_multipart, parallel_operations_count, part_size, prefix, storage_tier):

    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    output_format = ctx.obj['output']

    if src_dir and dest_dir:
        raise click.UsageError('Only one of --src-dir or --dest-dir options can be specified at a time')
    elif src_dir:
        # upload local files to object storage
        upload_transfers, upload_skipped, sync_output = \
            _bulk_upload(ctx,
                         client=client,
                         namespace=namespace,
                         bucket_name=bucket_name,
                         src_dir=src_dir,
                         cache_control=cache_control,
                         content_disposition=content_disposition,
                         content_encoding=content_encoding,
                         content_language=content_language,
                         content_type=content_type,
                         dry_run=dry_run,
                         encryption_key_file=encryption_key_file,
                         exclude=exclude,
                         include=include,
                         metadata=metadata,
                         no_multipart=no_multipart,
                         no_overwrite=False,
                         overwrite=False,
                         parallel_upload_count=parallel_operations_count,
                         part_size=part_size,
                         prefix=prefix,
                         storage_tier=storage_tier,
                         verify_checksum=False,
                         syncing=True,
                         no_follow_symlinks=no_follow_symlinks)

        output_data = sync_output.get_output(output_format)
        expanded_directory = os.path.expandvars(os.path.expanduser(src_dir))
        if dry_run:
            for on in upload_skipped:
                if prefix is not None:
                    on = on[len(prefix):]
                print('Skipping file:', os.path.join(expanded_directory, on))

        if delete:
            # while deleting we want to exclude all the items in scope, which would consist of the items that actually
            # gets transferred + the items which were supposed to get transferred but for skipped for some reason.
            excluded_object_set = upload_transfers.union(upload_skipped)

            _filter = _get_file_filter_collection(bucket_name, include, exclude, prefix)
            # delete the extra files in remote which are not there in source
            stacked_output = _delete_bucket_components(ctx, client, namespace, bucket_name, dry_run, _filter,
                                                       excluded_object_set, parallel_operations_count, prefix,
                                                       del_pars=False, del_rep_pol=False, del_uploads=False)

            # combine upload output with delete data based on output format
            delete_output_data = stacked_output[0].get_output(output_format)
            if output_format == 'json':
                output_data.update(delete_output_data)
            elif output_format == 'table':
                output_data.extend(delete_output_data)

            if dry_run:
                if output_data['deleted-objects']:
                    for o in output_data['deleted-objects']:
                        print('Deleting object:', o)
            else:
                if stacked_output[0].has_failures():
                    sys.exit(1)

        if dry_run:
            sys.exit(0)

        render(data=output_data, headers=None, ctx=ctx, nest_data_in_data_attribute=False)

        if sync_output.has_failures():
            sys.exit(1)

    elif dest_dir:
        raise_usage_error_for_flags('dest-dir',
                                    ('cache-control', cache_control),
                                    ('content-disposition', content_disposition),
                                    ('content-encoding', content_encoding),
                                    ('content-language', content_language),
                                    ('content-type', content_type),
                                    ('metadata', metadata),
                                    ('storage-tier', storage_tier))

        download_transfers, download_skipped, sync_output = \
            _bulk_download(ctx,
                           client=client,
                           namespace=namespace,
                           bucket_name=bucket_name,
                           dest_dir=dest_dir,
                           dry_run=dry_run,
                           delimiter=None,
                           encryption_key_file=encryption_key_file,
                           exclude=exclude,
                           include=include,
                           multipart_download_threshold=128,  # setting multipart_download_threshold as default
                           no_multipart=no_multipart,
                           no_overwrite=False,
                           overwrite=False,
                           parallel_operations_count=parallel_operations_count,
                           part_size=part_size,
                           prefix=prefix,
                           syncing=True)

        output_data = sync_output.get_output(output_format)
        expanded_directory = os.path.expandvars(os.path.expanduser(dest_dir))
        normalize_expanded_dir = normalize_file_path_for_object_storage(expanded_directory)
        if dry_run:
            for on in download_skipped:
                on = on[len(normalize_expanded_dir):].lstrip('/')
                if prefix is not None:
                    on = prefix + on
                print('Skipping object:', on)

        if delete:
            # while deleting we want to exclude all the items in scope, which would consist of the items that actually
            # gets transferred + the items which were supposed to get transferred but for skipped for some reason.
            excluded_local_objects = download_transfers.union(download_skipped)

            _filter = _get_file_filter_collection(expanded_directory, include, exclude, prefix)
            deleted_objects = []
            for dir_name, subdir_list, file_list in os.walk(expanded_directory, topdown=False, followlinks=not no_follow_symlinks):
                file_list_delete = file_list[:]
                for file in file_list:
                    full_file_path = os.path.join(dir_name, file)
                    # ignore symlinks while delete as well when no_follow_symlink is specified
                    if no_follow_symlinks and os.path.islink(full_file_path):
                        continue

                    if _filter and _filter.get_action(full_file_path) == BaseFileFilterCollection.EXCLUDE:
                        continue

                    if normalize_file_path_for_object_storage(full_file_path) in excluded_local_objects:
                        continue

                    full_file_path = normalize_file_path_for_object_storage(full_file_path)
                    print('Deleting :', full_file_path)
                    if not dry_run:
                        os.remove(full_file_path)
                    file_list_delete.remove(file)
                    deleted_objects.append(full_file_path)

                if (not file_list_delete) and (dir_name != expanded_directory):
                    empty_folder_object = normalize_file_path_for_object_storage(dir_name + os.sep)
                    if empty_folder_object not in excluded_local_objects:
                        if not dry_run:
                            try:  # after deleting the files check and delete the empty parent directories
                                os.rmdir(dir_name)
                                print('Deleting :', empty_folder_object)
                                deleted_objects.append(empty_folder_object)
                            except OSError:
                                pass
                        else:
                            print('Deleting :', empty_folder_object)
                            deleted_objects.append(empty_folder_object)

            # combine download output data with delete data based on output format
            if output_format == 'json':
                output_data['deleted-files'] = deleted_objects
            elif output_format == 'table':
                for del_object in deleted_objects:
                    output_data.append({'action': 'Deleted', 'name': del_object, 'type': 'file'})

        if dry_run:
            sys.exit(0)
        render(data=output_data, headers=None, ctx=ctx, nest_data_in_data_attribute=False)

        if sync_output.has_failures():
            sys.exit(1)

    else:
        raise click.UsageError('Either --src-dir or --dest-dir options must be specified')


def raise_usage_error_for_flags(parent_option_name, *un_wanted_options):
    for flag_name, flag_value in un_wanted_options:
        # if flag is of boolean type then check that the value is false
        if flag_value is not None:
            if not flag_value:
                continue
            raise click.UsageError('Option --{} cannot be specified with --{}'.format(flag_name, parent_option_name))


# specifies if the file should be synced between source and destination
def requires_sync(local_file, remote_file_size, remote_file_mtime, to_remote=True):
    expanded_file = os.path.expandvars(os.path.expanduser(local_file))
    f_stat = os.stat(expanded_file)
    local_file_size = f_stat.st_size
    # local file time is in epoch time
    local_file_mtime = datetime.datetime.fromtimestamp(f_stat.st_mtime, tz=pytz.utc)
    if to_remote:
        return local_file_size != remote_file_size or local_file_mtime > remote_file_mtime
    else:
        return local_file_size != remote_file_size or local_file_mtime < remote_file_mtime


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
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--include', multiple=True, help=include_option_help_text)
@cli_util.option('--exclude', multiple=True, help=exclude_option_help_text)
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

        sys.exit(0)

    # Start bulk delete of objects
    _bulk_delete_objects_using_pool(ctx, client, namespace, bucket_name, None, force, delimiter, prefix,
                                    file_filter_collection, None, output, parallel_operations_count,
                                    lambda r: r.data.next_start_with, lambda res: res.data.objects)

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
                 help=parallel_operations_count_option_help_text)
@cli_util.option('--include', multiple=True, help=include_option_help_text)
@cli_util.option('--exclude', multiple=True, help=exclude_option_help_text)
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
            fields='name',
            page=None,
            retrieve_all=True)

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

        sys.exit(0)

    # Start bulk delete of object versions
    _bulk_delete_objects_using_pool(ctx, client, namespace, bucket_name, object_name, force, delimiter, prefix,
                                    file_filter_collection, None, output, parallel_operations_count,
                                    lambda r: r.headers.get('opc-next-page'), lambda res: res.data.items,
                                    is_versioned=True)

    render(data=output.get_output(ctx.obj['output']), headers=None, ctx=ctx, nest_data_in_data_attribute=False)

    if output.has_failures():
        sys.exit(1)


# Common helper method to paginate through objects/versions list and delete them using a pool
def _bulk_delete_objects_using_pool(ctx, client, namespace, bucket_name, object_name, force, delimiter, prefix,
                                    file_filter_collection, excluded_object_set, output, parallel_operations_count,
                                    _next_page_fn, _get_obj_fn, is_versioned=False):
    reusable_progress_bar = ProgressBar(100, 'Delete Object')
    curr_page = None
    first_page = True
    while True:
        transfer_manager = TransferManager(client,
                                           TransferManagerConfig(max_object_storage_requests=parallel_operations_count))

        list_objects_responses = retrying_list_call_single_page(
            func_ref=client.list_object_versions if is_versioned else client.list_objects,
            request_id=ctx.obj['request_id'],
            namespace=namespace,
            bucket_name=bucket_name,
            prefix=prefix,
            start=object_name if is_versioned else curr_page,
            end=None,
            limit=OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
            delimiter=delimiter,
            page=curr_page if is_versioned else None,
            fields='name'
        )

        next_page = _next_page_fn(list_objects_responses)
        objects_to_delete = []
        for obj in _get_obj_fn(list_objects_responses):
            if object_name and object_name != obj.name:
                continue

            if file_filter_collection:
                pseudo_path = os.path.join(bucket_name, obj.name)
                if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                    continue

            # check in the excluded object set and if present exclude the object
            if excluded_object_set and obj.name in excluded_object_set:
                continue

            objects_to_delete.append(obj)

        # Based on the rules for --force:
        #
        # CLI should do a list for 1000 items, and ask for confirmation with a message saying either that
        # more than 1000 items will be deleted, or the exact number of items that will be deleted
        #
        # Moving transfer manager inside while loop since we should wait for pool completion after delete
        # before list is called again
        #
        # Always list first page of versions that match given criteria and delete versions,
        # next_page_exists is not used for anything except to find out if next page exists or not
        if not force:
            o_type = 'object versions' if is_versioned else 'objects'
            if file_filter_collection:
                # If we specify this, the approximate or exact objects to delete is not determinable without paging through the entire list (e.g. in the
                # case that the only matching items are on the last few pages). So in this case just use a generic message
                confirm_prompt = 'WARNING: This command will delete all matching {} in the bucket. Please use ' \
                                 '--dry-run to list the objects which would be deleted. Are you sure you wish to ' \
                                 'continue?'.format(o_type)
            else:
                if len(objects_to_delete) == 0:
                    if first_page:
                        click.echo('There are no objects to delete in {}'.format(bucket_name), file=sys.stderr)
                        sys.exit(0)
                    break
                confirm_prompt = 'WARNING: This command will delete at least {} {}. Are you sure you wish to continue?'\
                    .format(len(objects_to_delete), o_type)
            if first_page and (not click.confirm(confirm_prompt)):
                ctx.abort()

        for obj in objects_to_delete:

            qualified_name = obj.name
            delete_kwargs = {
                'namespace': namespace,
                'bucket_name': bucket_name,
                'object_name': obj.name,
                'if_match': None,
                'request_id': ctx.obj['request_id']
            }

            # handle special case for object version
            if is_versioned:
                delete_kwargs['version_id'] = obj.version_id
                qualified_name = obj.name + "," + obj.version_id

            _add_to_delete_pool(ctx, qualified_name, output, reusable_progress_bar, transfer_manager,
                                DeleteObjectTask, delete_kwargs)

        transfer_manager.wait_for_completion()
        if len(objects_to_delete) == 0:
            if file_filter_collection:      # Even if object not in current page check all the pages
                curr_page = next_page
            else:                       # Object not in current page, end the loop
                break

        if next_page is None:           # This is the last page, end the loop
            break

        first_page = False

        # Because we may not be deleting objects for a while when there are filters,
        # show a dummy message so the caller still knows that there is progress
        if file_filter_collection:
            reusable_progress_bar.reset_progress(100, 'Searching for matching objects to delete')

    reusable_progress_bar.render_finish()


@objectstorage_cli.object_group.command(name='resume-put')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help="The file to load as the content of the object.")
@cli_util.option('--name',
                 help='The name of the object. Default value is the filename excluding the path.')
@cli_util.option('--upload-id', required=True, help='Upload ID to resume.')
@cli_util.option('--part-size', type=click.INT, help=part_size_option_help_text)
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@cli_util.option('--parallel-upload-count', type=click.IntRange(1, 1000), default=None,
                 help=parallel_operations_count_option_help_text)
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

    if kwargs['version_id'] is not None:
        details['versionId'] = kwargs['version_id']
        kwargs.pop("version_id")

    client = build_client('object_storage', 'object_storage', ctx)
    kwargs = {'opc_client_request_id': ctx.obj['request_id']}
    result = client.restore_objects(
        namespace_name=namespace,
        bucket_name=bucket,
        restore_objects_details=details,
        **kwargs
    )

    if result.status == 200:
        click.echo("This object will be available for download in about 1 hour. Use 'oci os object restore-status -ns {ns} -bn {bn} --name {name}' command to check the status.".format(ns=namespace, bn=bucket, name=name), file=sys.stderr)
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
        msg = "Restoring, this object is being restored and will be available for download in about 1 hour from the time you issued the restore command."
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


@cli_util.copy_params_from_generated_command(objectstorage_cli.delete_bucket, params_to_exclude=['force'])
@objectstorage_cli.bucket_group.command(name='delete', help="Deletes a bucket if the bucket is already empty. If not empty and the --empty option is specified, all objects, pre-authenticated requests, uncommitted multipart uploads and replication policies associated with the bucket are also deleted. \n[Command Reference](deleteBucket)")
@cli_util.option('--force', is_flag=True, help="Perform deletion without prompting for confirmation.")
@cli_util.option('--empty', is_flag=True, help="Delete all objects, pre-authenticated requests, uncommitted multipart uploads and replication policies associated with the bucket.")
@cli_util.option('--dry-run', is_flag=True, help="When specified with the --empty option, displays a list of objects which would be deleted by this command if it were run without --dry-run. No objects will actually be deleted.")
@cli_util.option('--parallel-operations-count', type=click.INT, default=10, show_default=True, help="When specified with the --empty option, specifies the number of parallel delete operations to perform. Decreasing this value will make empty less resource intensive but it may take longer. Increasing this value may improve empty times, but it will consume more system resources and network bandwidth.")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def bucket_delete(ctx, from_json, namespace_name, bucket_name, empty, force, dry_run, parallel_operations_count, if_match):

    if dry_run and not empty:
        raise click.UsageError('The option --dry-run is applicable only when the --empty option is specified')

    if not force and not dry_run:
        if empty:
            confirm_prompt = 'This command will delete the bucket as well as all replication policies, ' \
                             'pre-authenticated requests, objects and uncommitted multipart uploads ' \
                             'associated with it. Are you sure you wish to continue?'
        else:
            confirm_prompt = "Are you sure you want to delete this bucket?"

        if not click.confirm(confirm_prompt):
            ctx.abort()

    if empty:
        kwargs = {'opc_client_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
        client = cli_util.build_client('object_storage', 'object_storage', ctx)
        # Get bucket status for versioning
        result = client.get_bucket(namespace_name=namespace_name, bucket_name=bucket_name, **kwargs)
        response = cli_util.to_dict(result.data)
        versioning = response.get("versioning")
        delete_versions = versioning.lower() != "disabled"

        stacked_output = _delete_bucket_components(ctx, client, namespace_name, bucket_name, dry_run, None, None,
                                                   parallel_operations_count, None, versioned=delete_versions)

        # render the combined output
        combined_out = _combine_output(ctx.obj['output'], dry_run, *stacked_output)
        render(data=combined_out, headers=None, ctx=ctx, nest_data_in_data_attribute=False)

        if dry_run:
            sys.exit()

        for output in stacked_output:
            if output.has_failures():
                sys.exit(1)

    # Try to delete the bucket
    ctx.invoke(objectstorage_cli.delete_bucket,
               from_json=from_json,
               namespace_name=namespace_name,
               bucket_name=bucket_name,
               if_match=if_match)


def _delete_bucket_components(ctx, client, namespace_name, bucket_name, dry_run, file_filter_collection,
                              excluded_object_set, parallel_operations_count, prefix, del_objects=True, versioned=False,
                              del_pars=True, del_rep_pol=True, del_uploads=True):

    stacked_output = []  # this will store the output from deletion of different bucket components (e.g object, par etc)
    output_rep_policy = BulkDeleteOperationOutput('replication-policy')
    output_par = BulkDeleteOperationOutput('preauth-request')
    output_object = BulkDeleteOperationOutput()
    output_upload = BulkDeleteOperationOutput('multipart-upload')

    if dry_run:

        list_params = {
            'request_id': ctx.obj['request_id'],
            'namespace': namespace_name,
            'bucket_name': bucket_name,
            'limit': OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
            'retrieve_all': True
        }

        if del_rep_pol:
            # list replication policies
            rep_policy_list_response = retrying_list_call(client.list_replication_policies, **list_params)
            for response in rep_policy_list_response:
                for rep_policy_obj in response.data:
                    output_rep_policy.add_deleted(rep_policy_obj.name)
            stacked_output.append(output_rep_policy)

        if del_pars:
            # list pre-authenticated requests
            par_list_response = retrying_list_call(client.list_preauthenticated_requests, **list_params)
            for response in par_list_response:
                for par_object in response.data:
                    output_par.add_deleted(par_object.name)
            stacked_output.append(output_par)

        if del_objects:
            # list object/ object versions
            list_obj_params = {
                'client': client,
                'request_id': ctx.obj['request_id'],
                'namespace': namespace_name,
                'bucket_name': bucket_name,
                'prefix': prefix,
                'start': None,
                'end': None,
                'limit': OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
                'delimiter': None,
                'fields': 'name',
                'retrieve_all': True
            }
            if not versioned:
                list_all_objects_responses = retrying_list_objects(**list_obj_params)
                for response in list_all_objects_responses:
                    for obj in response.data.objects:
                        if file_filter_collection:
                            pseudo_path = os.path.join(bucket_name, obj.name)
                            if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                                continue
                        if excluded_object_set and obj.name in excluded_object_set:
                            continue
                        output_object.add_deleted(obj.name)
            else:
                list_all_objects_responses = retrying_list_object_versions(**list_obj_params)
                for response in list_all_objects_responses:
                    for obj in response.data.items:
                        if file_filter_collection:
                            pseudo_path = os.path.join(bucket_name, obj.name)
                            if file_filter_collection.get_action(pseudo_path) == BaseFileFilterCollection.EXCLUDE:
                                continue
                        if excluded_object_set and obj.name in excluded_object_set:
                            continue
                        output_object.add_deleted(obj.name + "," + obj.version_id)
            stacked_output.append(output_object)

        if del_uploads:
            # list un-committed uploads
            list_uploads_response = retrying_list_call(client.list_multipart_uploads, **list_params)
            for response in list_uploads_response:
                for upload_obj in response.data:
                    output_upload.add_deleted(upload_obj.object)
            stacked_output.append(output_upload)

        return stacked_output

    # Actual deletion starts here
    common_delete_kwargs = {
        'namespace': namespace_name,
        'bucket_name': bucket_name,
        'request_id': ctx.obj['request_id']
    }

    list_params = {
        'request_id': ctx.obj['request_id'],
        'namespace': namespace_name,
        'bucket_name': bucket_name,
        'limit': OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS,
        'retrieve_all': False
    }

    if del_rep_pol:
        # Deleting Replication Policies
        rep_policy_delete_kwargs = common_delete_kwargs.copy()
        reusable_progress_bar = ProgressBar(100, 'Deleting Replication Policies')
        while True:
            transfer_manager = TransferManager(client,
                                               TransferManagerConfig(
                                                   max_object_storage_requests=parallel_operations_count))
            rep_policy_list_response = retrying_list_call(client.list_replication_policies, **list_params)

            for response in rep_policy_list_response:
                for r_obj in response.data:
                    rep_policy_delete_kwargs['replication_id'] = r_obj.id
                    _add_to_delete_pool(ctx, r_obj.name, output_rep_policy, reusable_progress_bar, transfer_manager,
                                        DeleteReplicationPolicyTask, rep_policy_delete_kwargs)

            transfer_manager.wait_for_completion()
            if rep_policy_list_response[-1].headers.get('opc-next-page') is None:
                break
        reusable_progress_bar.render_finish()
        stacked_output.append(output_rep_policy)

    if del_pars:
        # Deleting PreAuthenticated Requests
        par_delete_kwargs = common_delete_kwargs.copy()
        reusable_progress_bar = ProgressBar(100, 'Deleting Preauthenticated Requests')
        while True:
            transfer_manager = TransferManager(client,
                                               TransferManagerConfig(
                                                   max_object_storage_requests=parallel_operations_count))
            par_list_response = retrying_list_call(client.list_preauthenticated_requests, **list_params)

            for response in par_list_response:
                for p_obj in response.data:
                    par_delete_kwargs['par_id'] = p_obj.id
                    _add_to_delete_pool(ctx, p_obj.name, output_par, reusable_progress_bar, transfer_manager,
                                        DeletePreAuthenticatedRequestTask, par_delete_kwargs)

            transfer_manager.wait_for_completion()
            if par_list_response[-1].headers.get('opc-next-page') is None:
                break
        reusable_progress_bar.render_finish()
        stacked_output.append(output_par)

    if del_objects:
        if not versioned:
            _bulk_delete_objects_using_pool(ctx, client, namespace_name, bucket_name, None, True, None, prefix,
                                            file_filter_collection, excluded_object_set, output_object,
                                            parallel_operations_count, lambda r: r.data.next_start_with,
                                            lambda res: res.data.objects)
        else:
            # bulk-delete object versions
            _bulk_delete_objects_using_pool(ctx, client, namespace_name, bucket_name, None, True, None, prefix,
                                            file_filter_collection, excluded_object_set, output_object,
                                            parallel_operations_count, lambda r: r.headers.get('opc-next-page'),
                                            lambda res: res.data.items, is_versioned=True)
        stacked_output.append(output_object)

    if del_uploads:
        # Deleting uncommitted uploads
        upload_delete_kwargs = common_delete_kwargs.copy()
        reusable_progress_bar = ProgressBar(100, 'Deleting uncommitted uploads')
        while True:
            transfer_manager = TransferManager(client,
                                               TransferManagerConfig(
                                                   max_object_storage_requests=parallel_operations_count))
            uploads_list_response = retrying_list_call(client.list_multipart_uploads, **list_params)

            for response in uploads_list_response:
                for u_obj in response.data:
                    upload_delete_kwargs['object_name'] = u_obj.object
                    upload_delete_kwargs['upload_id'] = u_obj.upload_id
                    _add_to_delete_pool(ctx, u_obj.object, output_upload, reusable_progress_bar, transfer_manager,
                                        DeleteUploadTask, upload_delete_kwargs)

            transfer_manager.wait_for_completion()
            if uploads_list_response[-1].headers.get('opc-next-page') is None:
                break
        reusable_progress_bar.render_finish()
        stacked_output.append(output_upload)

    return stacked_output


def _combine_output(output_format, dry_run, *args):
    if output_format == 'json':
        return {o.get_type(): o.get_output(output_format, dry_run=dry_run) for o in args}
    else:
        final_table_output = []
        for output in args:
            final_table_output.extend(output.get_output(output_format, dry_run=dry_run))
        return final_table_output


# Adds an object to a delete pool for parallel processing
def _add_to_delete_pool(ctx, qualified_name, output, reusable_progress_bar, transfer_manager, task_handler, delete_kwargs):
    try:
        if ctx.obj['debug']:
            update_progress_kwargs = {'message': 'Deleted {} {}'.format(output.get_type, qualified_name)}
            update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
        else:
            update_progress_kwargs = {
                'new_label': _get_progress_bar_label(None, qualified_name, 'Deleted {}'.format(output.get_type()))}
            update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end,
                                                            **update_progress_kwargs)

        add_to_deleted_kwargs = {'deleted': qualified_name}
        error_callback_kwargs = {'failed_item': qualified_name}
        add_to_deleted_objects_callback = WorkPoolTaskCallback(output.add_deleted, **add_to_deleted_kwargs)
        add_to_delete_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

        callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback],
                                                             success_callbacks=[add_to_deleted_objects_callback],
                                                             error_callbacks=[add_to_delete_failures_callback])
        if ctx.obj['debug']:
            confirmation_msg = 'Deleting object name {}'.format(qualified_name)
            click.echo(confirmation_msg, file=sys.stderr)
        else:
            reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, qualified_name, 'Deleting'))

        transfer_manager.delete_object(callbacks_container, task_handler, **delete_kwargs)
    except Exception as e:
        # Don't let one get failure fail the entire batch, but store the error for output later
        output.add_failure(qualified_name, callback_exception=e)
        if ctx.obj['debug']:
            failure_msg = 'Failed to delete object name {} '.format(qualified_name)
            click.echo(failure_msg, file=sys.stderr)


def retrying_list_call(func_ref, request_id, namespace, bucket_name, limit, prefix=None, start=None, end=None,
                       delimiter=None, page=None, fields=None, retrieve_all=False):
    all_responses = list()
    if retrieve_all:
        response = retrying_list_call_single_page(func_ref, request_id, namespace, bucket_name, prefix, start, end,
                                                  limit, delimiter, page, fields)
        all_responses.append(response)
        page = response.headers.get('opc-next-page')
        while page:
            response = retrying_list_call_single_page(func_ref, request_id, namespace, bucket_name, prefix, start, end,
                                                      limit, delimiter, page, fields)
            all_responses.append(response)
            page = response.headers.get('opc-next-page')
    else:
        while limit > 0:
            response = retrying_list_call_single_page(func_ref, request_id, namespace, bucket_name, prefix, start, end,
                                                      limit, delimiter, page, fields)
            all_responses.append(response)
            page = response.headers.get('opc-next-page')
            if page:
                limit -= len(response.data.items)
            else:
                limit = 0
    return all_responses


def retrying_list_call_single_page(func_ref, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter,
                                   page=None, fields=None):
    kwargs = {
        'opc_client_request_id': request_id,
        'limit': limit
    }
    if delimiter is not None:
        kwargs['delimiter'] = delimiter
    if prefix is not None:
        kwargs['prefix'] = prefix
    if start is not None:
        kwargs['start'] = start
    if end is not None:
        kwargs['end'] = end
    if page is not None:
        kwargs['page'] = page
    if fields is not None:
        kwargs['fields'] = fields

    return func_ref(namespace_name=namespace, bucket_name=bucket_name, **kwargs)


# Retrieves multiple pages of objects, retrying each list page call if we received a retryable exception. This will return a list of
# the raw responses we received in the order we received them
#
# This method can retrieve all matching objects or only up to a given limit. The default is only to retrieve up to the given limit
def retrying_list_objects(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, fields, retrieve_all=False):
    all_responses = list()

    if retrieve_all:
        response = retrying_list_call_single_page(client.list_objects, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter, fields=fields)
        all_responses.append(response)
        next_start = response.data.next_start_with

        while next_start:
            response = retrying_list_call_single_page(client.list_objects, request_id, namespace, bucket_name, prefix, next_start, end, limit, delimiter, fields=fields)

            all_responses.append(response)
            next_start = response.data.next_start_with
    else:
        next_start = start
        while limit > 0:
            response = retrying_list_call_single_page(client.list_objects, request_id, namespace, bucket_name, prefix, next_start, end, limit, delimiter, fields=fields)

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
def retrying_list_object_versions(client, request_id, namespace, bucket_name, prefix, start, end, limit, delimiter,
                                  fields, page=None, retrieve_all=False):
    return retrying_list_call(client.list_object_versions, request_id, namespace, bucket_name, limit, prefix, start, end,
                              delimiter, page, fields, retrieve_all)


# Normalizes the object name path of an object we're going to upload to object storage (e.g. a/b/c/object.txt) so that
# it uses the object storage delimiter character (/)
#
# On Unix filesystems this should be a no-op because the path separator is already the slash but on Windows systems this will replace
# the Windows path separator (\) with /
def normalize_file_path_for_object_storage(object_name_path, path_separator=os.sep):
    return object_name_path.replace(path_separator, '/')


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
    if object_prefix:
        object_prefix = object_prefix.replace('/', os.sep)
    if include:
        file_filter_collection = SingleTypeFileFilterCollection(base_directory, BaseFileFilterCollection.INCLUDE)
        for i in include:
            # If objects have a prefix with a path separator, we're going to transform that into part of the path
            # so a caller's --include and --exclude filters may not take that into account. Instead, try and do that
            # for them here
            if object_prefix and (object_prefix.find(os.sep) >= 0):
                file_filter_collection.add_filter(os.path.join(object_prefix, i))

            file_filter_collection.add_filter(i)
    elif exclude:
        file_filter_collection = SingleTypeFileFilterCollection(base_directory, BaseFileFilterCollection.EXCLUDE)
        for e in exclude:
            if object_prefix and (object_prefix.find(os.sep) >= 0):
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
        key_data_base64_str = data_file.read().strip()
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
        key_data_base64_str = data_file.read().strip()
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
        self._total_bytes = 1 if total_bytes == 0 else total_bytes
        self._total_progress_bytes = 0
        self._last_progress = 0
        self._progressbar = click.progressbar(length=ProgressBar.PROGRESS_BAR_GRANULARITY,
                                              label=label, file=sys.stderr)
        # To synchronize as same progressbar is being shared between the threads
        self._semaphore = WrappedSemaphore(1)

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
        self._semaphore.acquire()
        self._progressbar.label = new_label
        self._progressbar.pos = 0
        self._progressbar.avg = []
        self._progressbar.finished = False

        self._total_bytes = total_bytes
        self._last_progress = 0
        self._total_progress_bytes = 0
        self._semaphore.release()

    def update_label_to_end(self, new_label):
        self._semaphore.acquire()
        self._progressbar.label = new_label
        self._progressbar.finished = True
        self._progressbar.render_progress()
        print()
        self._semaphore.release()

    def render_finish(self):
        self._progressbar.render_finish()
