# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import click
import os
import os.path
import stat
import sys
from oci import exceptions
from oci.object_storage.transfer import constants
from oci.object_storage import models
from .cli_root import cli
from .cli_util import render, render_response, parse_json_parameter, help_option, help_option_group, build_client, confirm_delete_option, wrap_exceptions, filter_object_headers, formatted_flat_dict, load_context_obj_values_from_defaults, coalesce_provided_and_default_value, get_click_file_from_default_values_file
from oci.object_storage import UploadManager, MultipartObjectAssembler
from oci_cli.file_filters import BaseFileFilterCollection
from oci_cli.file_filters import SingleTypeFileFilterCollection
from retrying import retry
from . import retry_utils
from .object_storage_transfer_manager import TransferManager, TransferManagerConfig, WorkPoolTaskCallback, WorkPoolTaskErrorCallback, WorkPoolTaskSuccessCallback, WorkPoolTaskCallbacksContainer
from . import json_skeleton_utils
from .custom_types import CliDatetime


OBJECT_LIST_PAGE_SIZE = 100
OBJECT_LIST_PAGE_SIZE_BULK_OPERATIONS = 1000

MEBIBYTE = 1024 * 1024

OBJECT_GET_CHUNK_SIZE = MEBIBYTE

OBJECT_PUT_DISPLAY_HEADERS = {
    "etag",
    "opc-content-md5",
    "last-modified",
    "opc-multipart-md5"
}


INCLUDE_EXCLUDE_PATTERN = """*: Matches everything
?: Matches any single character
[sequence]: Matches any character in sequence
[!sequence]: Matches any character not in sequence
"""


@click.group(name='os', help="""Object Storage Service""")
@help_option_group
def objectstorage():
    pass


cli.add_command(objectstorage)


@click.group(name='ns')
@help_option_group
def ns():
    pass


@click.command(name='get')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'str'})
@wrap_exceptions
def ns_get(ctx, generate_full_command_json_input, generate_param_json_input, from_json):
    """
    Gets the name of the namespace for the user making the request.

    Example:
        oci os ns get
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)

    client = build_client('os', ctx)
    render_response(client.get_namespace(opc_client_request_id=ctx.obj['request_id']), ctx)


objectstorage.add_command(ns)
ns.add_command(ns_get)


@click.group('bucket')
@help_option_group
def bucket():
    pass


@click.command(name='list')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('--compartment-id', help='The compartment ID to return buckets for. [required]')
@click.option('--limit', default=100, show_default=True, help='The maximum number of items to return.')
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[Bucket]'})
@wrap_exceptions
def bucket_list(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, compartment_id, limit, page):
    """
    Lists the `BucketSummary`s in a namespace. A `BucketSummary` contains only summary fields for the bucket
    and not fields such as the user-defined metadata.

    Example:
        oci os bucket list -ns mynamespace --compartment-id ocid1.compartment.oc1..aaaaaaaarhifmvrvuqtye5q65flzp3pp2jojdc6rck6copzqck3ukcypxfga
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    compartment_id = coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    limit = coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = coalesce_provided_and_default_value(ctx, 'page', page, False)

    client = build_client('os', ctx)

    kwargs = {
        'opc_client_request_id': ctx.obj['request_id'],
        'limit': limit
    }

    if page is not None:
        kwargs['page'] = page

    render_response(client.list_buckets(namespace,
                                        compartment_id,
                                        **kwargs), ctx)


@click.command(name='create')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('--compartment-id', help='The ID of the compartment in which to create the bucket. [required]')
@click.option('--name', help='The name of the bucket.')
@click.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@click.option('--public-access-type', type=click.Choice(['NoPublicAccess', 'ObjectRead']), help='The type of public access available on this bucket. Allows authenticated caller to access the bucket or contents of this bucket. By default a bucket is set to NoPublicAccess. It is treated as NoPublicAccess when this value is not specified. When the type is NoPublicAccess the bucket does not allow any public access. When the type is ObjectRead the bucket allows public access to the GetObject operation only.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@wrap_exceptions
def bucket_create(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, name, compartment_id, metadata, public_access_type):
    """
    Creates a bucket in the given namespace with a bucket name and optional user-defined metadata.

    Example:
        oci os bucket create -ns mynamespace --name mybucket --compartment-id ocid1.compartment.oc1..aaaaaaaarhifmvrvuqtye5q65flzp3pp2jojdc6rck6copzqck3ukcypxfga --metadata '{"key1":"value1","key2":"value2"}'
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    compartment_id = coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    metadata = coalesce_provided_and_default_value(ctx, 'metadata', metadata, False)
    public_access_type = coalesce_provided_and_default_value(ctx, 'public-access-type', public_access_type, False)

    bucket_details = models.CreateBucketDetails()
    bucket_details.compartment_id = compartment_id
    bucket_details.name = name
    bucket_details.metadata = parse_json_parameter("metadata", metadata, default={})
    if public_access_type is not None:
        bucket_details.public_access_type = public_access_type
    client = build_client('os', ctx)
    render_response(client.create_bucket(namespace, bucket_details, opc_client_request_id=ctx.obj['request_id']), ctx)


@click.command(name='update')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('--name', help='The name of the bucket. [required]')
@click.option('--if-match', help='The entity tag to match.')
@click.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. Must be in JSON format. Values will be appended to existing metadata. To remove a key, set it to null. Example: \'{"key1":"value1","key2":null}\'')
@click.option('--public-access-type', type=click.Choice(['NoPublicAccess', 'ObjectRead']), help='The type of public access available on this bucket. Allows authenticated caller to access the bucket or contents of this bucket. By default a bucket is set to NoPublicAccess. It is treated as NoPublicAccess when this value is not specified. When the type is NoPublicAccess the bucket does not allow any public access. When the type is ObjectRead the bucket allows public access to the GetObject operation only.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@wrap_exceptions
def bucket_update(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, name, if_match, metadata, public_access_type):
    """
    Updates a bucket's user-defined metadata.

    Example:
        oci os bucket update -ns mynamespace --name mybucket --metadata '{"key1":"value1","key2":"value2"}'
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    metadata = coalesce_provided_and_default_value(ctx, 'metadata', metadata, False)
    public_access_type = coalesce_provided_and_default_value(ctx, 'public-access-type', public_access_type, False)

    bucket_details = models.UpdateBucketDetails()
    bucket_details.name = name
    bucket_details.metadata = parse_json_parameter("metadata", metadata, default={})
    if public_access_type is not None:
        bucket_details.public_access_type = public_access_type

    client = build_client('os', ctx)
    render_response(client.update_bucket(
        namespace,
        name,
        bucket_details,
        if_match=if_match,
        opc_client_request_id=ctx.obj['request_id']
    ), ctx)


@click.command(name='get')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('--name', help='The name of the bucket. [required]')
@click.option('--if-match', help='The entity tag to match.')
@click.option('--if-none-match', help='The entity tag to avoid matching.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@wrap_exceptions
def bucket_get(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, name, if_match, if_none_match):
    """
    Gets the current representation of the given bucket in the given namespace.

    Example:
        oci os bucket get -ns mynamespace --name mybucket
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    if_none_match = coalesce_provided_and_default_value(ctx, 'if-none-match', if_none_match, False)

    client = build_client('os', ctx)
    render_response(client.get_bucket(
        namespace,
        name,
        if_match=if_match,
        if_none_match=if_none_match,
        opc_client_request_id=ctx.obj['request_id']
    ), ctx)


@click.command(name='delete')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('--name', help='The name of the bucket. [required]')
@click.option('--if-match', help='The entity tag to match.')
@confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def bucket_delete(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, name, if_match):
    """
    Deletes a bucket if it is already empty.

    Example:
        oci os bucket delete -ns mynamespace --name mybucket
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    client = build_client('os', ctx)
    render_response(client.delete_bucket(namespace, name, if_match=if_match, opc_client_request_id=ctx.obj['request_id']), ctx)


objectstorage.add_command(bucket)
bucket.add_command(bucket_create)
bucket.add_command(bucket_list)
bucket.add_command(bucket_get)
bucket.add_command(bucket_delete)
bucket.add_command(bucket_update)


@click.group('object')
@help_option_group
def object_group():
    pass


@click.command(name='list')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--prefix', help='Only object names that begin with this prefix will be returned.')
@click.option('--start', help='Only object names greater or equal to this parameter will be returned.')
@click.option('--end', help='Only object names less than this parameter will be returned.')
@click.option('--limit', default=100, show_default=True, help='The maximum number of items to return.')
@click.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                                  "delimiter character (after an optionally specified prefix) are returned. "
                                  "Scanned objects whose names contain the delimiter have part of their name "
                                  "up to the last occurrence of the delimiter (after the optional prefix) "
                                  "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                                  "character at this time.")
@click.option('--fields', default='name,size,timeCreated,md5', show_default=True,
              help="Object summary in list of objects includes the 'name' field. This parameter may also include "
                   "'size' (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields. "
                   "Value of this parameter should be a comma separated, case-insensitive list of those field names.")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[ObjectSummary]'})
@wrap_exceptions
def object_list(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, prefix, start, end, limit, delimiter, fields):
    """
    Lists the objects in a bucket.

    Example:
        oci os object list -ns mynamespace -bn mybucket --fields name,size,timeCreated
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    prefix = coalesce_provided_and_default_value(ctx, 'prefix', prefix, False)
    start = coalesce_provided_and_default_value(ctx, 'start', start, False)
    end = coalesce_provided_and_default_value(ctx, 'end', end, False)
    limit = coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    delimiter = coalesce_provided_and_default_value(ctx, 'delimiter', delimiter, False)
    fields = coalesce_provided_and_default_value(ctx, 'fields', fields, False)

    client = build_client('os', ctx)

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

    while limit > 0:

        args['limit'] = min(limit, OBJECT_LIST_PAGE_SIZE)

        response = client.list_objects(
            namespace,
            bucket_name,
            **args
        )

        if response.data.prefixes is not None:
            for prefix in response.data.prefixes:
                if prefix not in prefixes:
                    prefixes.append(prefix)

        objects = response.data.objects
        next_start = response.data.next_start_with

        all_objects.extend(objects)

        if next_start:
            limit -= len(objects)
            args['start'] = next_start
        else:
            limit = 0

    metadata = {'prefixes': prefixes}

    if response.data.next_start_with:
        metadata['next-start-with'] = response.data.next_start_with

    render(all_objects, metadata, ctx, display_all_headers=True)


@click.command(name='put')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--file', type=click.File(mode='rb'),
              help="The file to load as the content of the object, or '-' to read from STDIN. [required]")
@click.option('--name',
              help='The name of the object. Default value is the filename excluding the path. Required if reading object from STDIN.')
@click.option('--if-match', help='The entity tag to match.')
@click.option('--content-md5', help='The base-64 encoded MD5 hash of the body.')
@click.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@click.option('--content-type', help='The content type of the object.')
@click.option('--content-language', help='The content language of the object.')
@click.option('--content-encoding', help='The content encoding of the object.')
@click.option('--force', is_flag=True, help='If the object already exists, overwrite the existing object without a confirmation prompt.')
@click.option('--no-multipart', is_flag=True,
              help='Do not use multipart uploads to upload the file in parts. By default files above 128 MiB will be uploaded in multiple parts, then combined server-side.')
@click.option('--part-size', type=click.INT,
              help='Part size (in MiB) to use if uploading via multipart upload operations')
@click.option('--disable-parallel-uploads', is_flag=True,
              help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@click.option('--parallel-upload-count', type=click.INT, default=None,
              help='If the object will be uploaded in multiple parts, this option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads or --no-multipart. Defaults to 3.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}}, output_type={'module': 'object_storage', 'class': 'ObjectSummary'})
@wrap_exceptions
def object_put(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, file, if_match, content_md5, metadata, content_type, content_language, content_encoding, force, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count):
    """
    Creates a new object or overwrites an existing one.

    Example:
        oci os object put -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt --metadata '{"key1":"value1","key2":"value2"}'
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, False)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    content_md5 = coalesce_provided_and_default_value(ctx, 'content-md5', content_md5, False)
    metadata = coalesce_provided_and_default_value(ctx, 'metadata', metadata, False)
    content_type = coalesce_provided_and_default_value(ctx, 'content-type', content_type, False)
    content_language = coalesce_provided_and_default_value(ctx, 'content-language', content_language, False)
    content_encoding = coalesce_provided_and_default_value(ctx, 'content-encoding', content_encoding, False)
    force = coalesce_provided_and_default_value(ctx, 'force', force, False)
    no_multipart = coalesce_provided_and_default_value(ctx, 'no-multipart', no_multipart, False)
    part_size = coalesce_provided_and_default_value(ctx, 'part-size', part_size, False)
    disable_parallel_uploads = coalesce_provided_and_default_value(ctx, 'disable-parallel-uploads', disable_parallel_uploads, False)
    parallel_upload_count = coalesce_provided_and_default_value(ctx, 'parallel-upload-count', parallel_upload_count, False)

    if not file:
        file_from_default_values = get_click_file_from_default_values_file(ctx, 'file', 'rb', True)
        if file_from_default_values:
            file = file_from_default_values

    client = build_client('os', ctx)

    client_request_id = ctx.obj['request_id']
    kwargs = {'opc_client_request_id': client_request_id}

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
            if not click.confirm("WARNING: This object already exists. Are you sure you want to overwrite it?"):
                ctx.abort()

    if if_match is not None:
        kwargs['if_match'] = if_match

    if content_md5 is not None:
        kwargs['content_md5'] = content_md5

    if metadata is not None:
        kwargs['metadata'] = parse_json_parameter("metadata", metadata, default={})

    if content_type is not None:
        kwargs['content_type'] = content_type

    if content_language is not None:
        kwargs['content_language'] = content_language

    if content_encoding is not None:
        kwargs['content_encoding'] = content_encoding

    if part_size is not None:
        kwargs['part_size'] = part_size * MEBIBYTE

    total_size = os.fstat(file.fileno()).st_size
    size_qualifies_for_multipart = UploadManager._use_multipart(total_size, part_size) if part_size else UploadManager._use_multipart(total_size)

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

        upload_manager = UploadManager(client, allow_multipart_uploads=False)
        response = upload_manager.upload_file(namespace, bucket_name, name, file.name, **kwargs)

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

        ma = MultipartObjectAssembler(client,
                                      namespace,
                                      bucket_name,
                                      name,
                                      **kwargs)
        ma.new_upload()
        click.echo('Upload ID: {}'.format(ma.manifest["uploadId"]), file=sys.stderr)
        ma.add_parts_from_file(file.name)
        click.echo('Split file into {} parts for upload.'.format(len(ma.manifest["parts"])), file=sys.stderr)
        with ProgressBar(total_size, 'Uploading object') as bar:
            ma.upload(progress_callback=bar.update)
        response = ma.commit()

    display_headers = filter_object_headers(response.headers, OBJECT_PUT_DISPLAY_HEADERS)
    render(None, display_headers, ctx, display_all_headers=True)


@click.command(name='bulk-upload')
@click.option('-ns', '--namespace', help='Object Storage namespace. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--src-dir', help='The directory which contains files to upload. Files in the directory and all subdirectories will be uploaded. [required]')
@click.option('--object-prefix', help='A prefix to apply to the names of all files being uploaded')
@click.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. This will be applied to all files being uploaded. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@click.option('--content-type', help='The content type to apply to all files being uploaded.')
@click.option('--content-language', help='The content language to apply to all files being uploaded.')
@click.option('--content-encoding', help='The content encoding to apply to all files being uploaded.')
@click.option('--overwrite', is_flag=True, help='If a file being uploaded already exists in Object Storage, overwrite the existing object in Object Storage without a confirmation prompt. If neither this flag nor --no-overwrite is specified, you will be prompted each time an object would be overwritten')
@click.option('--no-overwrite', is_flag=True, help='If a file being uploaded already exists in Object Storage, do not overwite it. If neither this flag nor --overwrite is specified, you will be prompted each time an object would be overwritten')
@click.option('--no-multipart', is_flag=True,
              help='Do not use multipart uploads to upload the file in parts. By default files above 128 MiB will be uploaded in multiple parts, then combined server-side. This applies to all files being uploaded')
@click.option('--part-size', type=click.INT,
              help='Part size (in MiB) to use if uploading via multipart upload operations. This applies to all files which will be uploaded in multiple parts. Part size must be greater than 10 MiB')
@click.option('--disable-parallel-uploads', is_flag=True,
              help='[DEPRECATED] This option is no longer used. If a file in the directory will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel. This applies to all files being uploaded in multiple parts')
@click.option('--parallel-upload-count', type=click.INT, default=10, show_default=True,
              help='The number of parallel operations to perform. Decreasing this value will make bulk uploads less resource intensive but they may take longer. Increasing this value may improve bulk upload times, but the upload process will consume more system resources and network bandwidth.')
@click.option('--include', multiple=True, help="""Only upload files which match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--exclude', multiple=True, help="""Only upload files which do not match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@wrap_exceptions
def object_bulk_put(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, src_dir, object_prefix, metadata, content_type, content_language, content_encoding, overwrite, no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count, include, exclude):
    """
    Uploads all objects in a given directory and all subdirectories.


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
    If a file being uploaded already exists in Object Storage, it can be overwritten without a prompt by
    using the --overwrite flag.

    \b
    Prevent object overwrite to resolve object name collision
    ----------------------------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory --no-overwrite

    \b
    If a file being uploaded already exists in Object Storage, it can be preserved (not overwritten) without a
    prompt by using the --no-overwrite flag.
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    src_dir = coalesce_provided_and_default_value(ctx, 'src-dir', src_dir, True)
    object_prefix = coalesce_provided_and_default_value(ctx, 'object-prefix', object_prefix, False)
    metadata = coalesce_provided_and_default_value(ctx, 'metadata', metadata, False)
    content_type = coalesce_provided_and_default_value(ctx, 'content-type', content_type, False)
    content_language = coalesce_provided_and_default_value(ctx, 'content-language', content_language, False)
    content_encoding = coalesce_provided_and_default_value(ctx, 'content-encoding', content_encoding, False)
    overwrite = coalesce_provided_and_default_value(ctx, 'overwrite', overwrite, False)
    no_overwrite = coalesce_provided_and_default_value(ctx, 'no-overwrite', no_overwrite, False)
    no_multipart = coalesce_provided_and_default_value(ctx, 'no-multipart', no_multipart, False)
    part_size = coalesce_provided_and_default_value(ctx, 'part-size', part_size, False)
    disable_parallel_uploads = coalesce_provided_and_default_value(ctx, 'disable-parallel-uploads', disable_parallel_uploads, False)
    parallel_upload_count = coalesce_provided_and_default_value(ctx, 'parallel-upload-count', parallel_upload_count, False)
    include = coalesce_provided_and_default_value(ctx, 'include', include, False)
    exclude = coalesce_provided_and_default_value(ctx, 'exclude', exclude, False)

    if ctx.obj['output'] == 'table':
        raise click.UsageError('Table output is not supported for this operation')

    expanded_directory = os.path.expandvars(os.path.expanduser(src_dir))
    if not os.path.exists(expanded_directory):
        raise click.UsageError('The specified --src-dir {} (expanded to: {}) does not exist'.format(src_dir, expanded_directory))

    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, None)

    if part_size is not None and no_multipart:
        raise click.UsageError('The option --part-size is not applicable when using the --no-multipart flag.')

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together')

    client = build_client('os', ctx)
    client_request_id = ctx.obj['request_id']

    base_kwargs = {'opc_client_request_id': client_request_id}
    if metadata is not None:
        base_kwargs['metadata'] = parse_json_parameter("metadata", metadata, default={})
    if content_type is not None:
        base_kwargs['content_type'] = content_type
    if content_language is not None:
        base_kwargs['content_language'] = content_language
    if content_encoding is not None:
        base_kwargs['content_encoding'] = content_encoding
    if part_size is not None:
        base_kwargs['part_size'] = part_size * MEBIBYTE

    output = {
        'uploaded-objects': {},
        'upload-failures': {},
        'skipped-objects': []
    }

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

            object_name = normalize_object_name_path_for_object_storage(full_file_path[len(expanded_directory):])

            # If we start with a leading path separator (/), strip that from the object name so we get a hierarchy like:
            #    <subfolder1>/<subfolder2>/<object>
            # Rather than:
            #    /<subfolder1>/<subfolder2>/<object>
            if object_name[0] == '/':
                object_name = object_name[1:]

            if object_prefix:
                object_name = '{}{}'.format(object_prefix, object_name)

            try:
                if not overwrite:
                    if len(file_list) > (idx + parallel_head_object_look_ahead_window):
                        for i in range(parallel_head_object_look_ahead_window):
                            look_ahead_file_path = os.path.join(dir_name, file_list[idx + i])
                            look_ahead_object_name = normalize_object_name_path_for_object_storage(look_ahead_file_path[len(expanded_directory):])
                            if look_ahead_object_name[0] == '/':
                                look_ahead_object_name = look_ahead_object_name[1:]
                            if object_prefix:
                                look_ahead_object_name = '{}{}'.format(object_prefix, look_ahead_object_name)

                            if look_ahead_object_name not in head_object_results:
                                head_object_kwargs = {
                                    'namespace_name': namespace,
                                    'bucket_name': bucket_name,
                                    'object_name': look_ahead_object_name,
                                    'opc_client_request_id': client_request_id
                                }
                                head_object_results[look_ahead_object_name] = transfer_manager.head_object(WorkPoolTaskCallbacksContainer(), **head_object_kwargs)

                    # Pull the result from the future (this will block until the result is available) or, if we don't have a future, just make a request
                    if object_name in head_object_results:
                        head_object = head_object_results.pop(object_name).result()
                    else:
                        head_object = _make_retrying_head_object_call(client, namespace, bucket_name, object_name, client_request_id)

                    if head_object is None:
                        # Object does not exist, so make sure that the put fails if one is created in the meantime.
                        base_kwargs['if_none_match'] = '*'
                    else:
                        if no_overwrite:
                            output['skipped-objects'].append(object_name)
                            continue

                        base_kwargs['if_match'] = head_object.headers['etag']
                        if not click.confirm('WARNING: {} already exists. Are you sure you want to overwrite it?'.format(object_name)):
                            output['skipped-objects'].append(object_name)
                            continue

                with open(full_file_path, 'rb') as file_object:
                    file_size = os.fstat(file_object.fileno()).st_size

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': 'Uploaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Uploaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                error_callback_kwargs = {'target_dict': output['upload-failures'], 'target_dict_key': object_name}
                success_callback_kwargs = {'target_dict': output['uploaded-objects'], 'target_dict_key': object_name}
                add_to_uploaded_objects_callback = WorkPoolTaskSuccessCallback(_success_upload_callback_add_item_to_dict, **success_callback_kwargs)
                add_to_upload_failures_callback = WorkPoolTaskErrorCallback(_error_callback_add_item_to_dict, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], success_callbacks=[add_to_uploaded_objects_callback], error_callbacks=[add_to_upload_failures_callback])

                if ctx.obj['debug']:
                    click.echo('Uploading {}'.format(full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Uploading'))

                if not ctx.obj['debug']:
                    base_kwargs['multipart_part_completion_callback'] = BulkPutMultipartUploadProgressBar(reusable_progress_bar, file_size, _get_progress_bar_label(None, object_name, 'Uploading part for')).update

                transfer_manager.upload_object(callbacks_container, namespace, bucket_name, object_name, full_file_path, file_size, **base_kwargs)

                # These can vary per request, so remove them if they exist so we have a blank slate for the next iteration
                base_kwargs.pop('if_none_match', None)
                base_kwargs.pop('if_match', None)
                base_kwargs.pop('multipart_part_completion_callback', None)
            except Exception as e:
                # Don't let one failure here (either HEADing to see if the object exists, or actaully uploading the object)
                # fail the entire batch, but store the error for output later
                output['upload-failures'][object_name] = str(e)

                if ctx.obj['debug']:
                    click.echo('Failed to upload {}'.format(object_name), file=sys.stderr)

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    click.echo(formatted_flat_dict(output))

    if len(output['upload-failures']) > 0:
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


@click.command(name='get')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--name', help='The name of the object. [required]')
@click.option('--file', type=click.File(mode='wb'),
              help="The name of the file that will receive the object content, or '-' to write to STDOUT. [required]")
@click.option('--if-match', help='The entity tag to match.')
@click.option('--if-none-match', help='The entity tag to avoid matching.')
@click.option('--range',
              help='Byte range to fetch. Follows https://tools.ietf.org/html/rfc7233#section-2.1. Example: bytes=2-10')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_get(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, file, if_match, if_none_match, range):
    """
    Gets the metadata and body of an object.

    Example:
        oci os object get -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    # No defaulting of the file so that we don't inadvertently overwrite the same file or stream each time
    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    if_none_match = coalesce_provided_and_default_value(ctx, 'if-none-match', if_none_match, False)
    range = coalesce_provided_and_default_value(ctx, 'range', range, False)

    if not file:
        file_from_default_values = get_click_file_from_default_values_file(ctx, 'file', 'wb', True)
        if file_from_default_values:
            file = file_from_default_values

    client = build_client('os', ctx)
    response = client.get_object(
        namespace,
        bucket_name,
        name,
        if_match=if_match,
        if_none_match=if_none_match,
        range=range,
        opc_client_request_id=ctx.obj['request_id']
    )

    # if outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>':
        bar = ProgressBar(total_bytes=int(response.headers['Content-Length']), label='Downloading object')

    # Stream using the raw urllib3.HTTPResponse, since using the Requests response
    # will automatically try to decode.
    for chunk in response.data.raw.stream(OBJECT_GET_CHUNK_SIZE, decode_content=False):
        if bar:
            bar.update(len(chunk))
        file.write(chunk)

    if bar:
        bar.render_finish()


@click.command(name='bulk-download')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--prefix', help='Retrieve all objects with the given prefix. Omit this parameter to get all objects in the bucket')
@click.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                                  "delimiter character (after an optionally specified prefix) are returned. "
                                  "Scanned objects whose names contain the delimiter have part of their name "
                                  "up to the last occurrence of the delimiter (after the optional prefix) "
                                  "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                                  "character at this time.")
@click.option('--download-dir', help='The directory where retrieved objects will be placed as files. This directory will be created if it does not exist. [required]')
@click.option('--overwrite', is_flag=True, help='If a file with the same name as an object already exists in the download directory, overwrite it. If neither this flag nor --no-overwrite is specified, you will be prompted each time a file would be overwritten.')
@click.option('--no-overwrite', is_flag=True, help='If a file with the same name as an object already exists in the download directory, do not overwite it. If neither this flag nor --overwrite is specified, you will be prompted each time a file would be overwritten')
@click.option('--parallel-operations-count', type=click.INT, default=10, show_default=True,
              help='The number of parallel operations to perform. Decreasing this value will make bulk downloads less resource intensive but they may take longer. Increasing this value may improve bulk download times, but the upload process will consume more system resources and network bandwidth.')
@click.option('--include', multiple=True, help="""Only download objects which match the provided pattern. Patterns are taken relative to the DOWNLOAD directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--exclude', multiple=True, help="""Only download objects which do not match the provided pattern. Patterns are taken relative to the DOWNLOAD directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_get(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, prefix, delimiter, download_dir, overwrite, no_overwrite, include, exclude, parallel_operations_count):
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
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    prefix = coalesce_provided_and_default_value(ctx, 'prefix', prefix, False)
    delimiter = coalesce_provided_and_default_value(ctx, 'delimiter', delimiter, False)
    download_dir = coalesce_provided_and_default_value(ctx, 'download-dir', download_dir, True)
    overwrite = coalesce_provided_and_default_value(ctx, 'overwrite', overwrite, False)
    no_overwrite = coalesce_provided_and_default_value(ctx, 'no-overwrite', no_overwrite, False)
    include = coalesce_provided_and_default_value(ctx, 'include', include, False)
    exclude = coalesce_provided_and_default_value(ctx, 'exclude', exclude, False)
    parallel_operations_count = coalesce_provided_and_default_value(ctx, 'parallel-operations-count', parallel_operations_count, False)

    if ctx.obj['output'] == 'table':
        raise click.UsageError('Table output is not supported for this operation')

    client = build_client('os', ctx)

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together')

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
        'fields': 'name'
    }
    keep_paginating = True

    output = {
        'skipped-objects': [],
        'download-failures': {}
    }

    # Progress bar which we can reuse over and over again
    reusable_progress_bar = ProgressBar(0, '')

    transfer_manager = TransferManager(client, TransferManagerConfig(max_object_storage_requests=parallel_operations_count))
    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, prefix)

    while keep_paginating:
        list_objects_response = retrying_list_objects_single_page(**kwargs)
        next_start = list_objects_response.data.next_start_with

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
                    output['skipped-objects'].append(object_name)
                    continue

                if not overwrite:
                    if not click.confirm('WARNING: {} already exists. Are you sure you want to overwrite it?'.format(object_name)):
                        output['skipped-objects'].append(object_name)
                        continue

            directory_for_file = os.path.dirname(full_file_path)
            if not os.path.exists(directory_for_file):
                os.makedirs(directory_for_file)

            try:
                get_object_kwargs = {
                    'namespace': namespace,
                    'bucket_name': bucket_name,
                    'object_name': object_name,
                    'full_file_path': full_file_path
                }

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': 'Downloaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Downloaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                error_callback_kwargs = {'target_dict': output['download-failures'], 'target_dict_key': object_name}
                add_to_download_failures_callback = WorkPoolTaskErrorCallback(_error_callback_add_item_to_dict, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], error_callbacks=[add_to_download_failures_callback])

                if ctx.obj['debug']:
                    click.echo('Downloading {} to {}'.format(object_name, full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Downloading'))

                transfer_manager.get_object(callbacks_container, **get_object_kwargs)
            except Exception as e:
                # Don't let one get failure fail the entire batch, but store the error for output later
                output['download-failures'][object_name] = str(e)

                if ctx.obj['debug']:
                    click.echo('Failed to download {}'.format(object_name), file=sys.stderr)

        # Keep going if we have more pages
        kwargs['start'] = next_start
        keep_paginating = (next_start is not None)

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    click.echo(formatted_flat_dict(output))

    if len(output['download-failures']) > 0:
        sys.exit(1)


@click.command(name='head')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--name', help='The name of the object. [required]')
@click.option('--if-match', help='The entity tag to match.')
@click.option('--if-none-match', help='The entity tag to avoid matching.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_head(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, if_match, if_none_match):
    """
    Gets the user-defined metadata and entity tag for an object.

    Example:
        oci os object head -ns mynamespace -bn mybucket --name myfile.txt
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    if_none_match = coalesce_provided_and_default_value(ctx, 'if-none-match', if_none_match, False)

    client = build_client('os', ctx)
    response = client.head_object(
        namespace,
        bucket_name,
        name,
        if_match=if_match,
        if_none_match=if_none_match,
        opc_client_request_id=ctx.obj['request_id'])

    render(None, response.headers, ctx, display_all_headers=True)


@click.command(name='delete')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--name', help='The name of the object to delete. [required]')
@click.option('--if-match', help='The entity tag to match.')
@confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_delete(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, if_match):
    """
    Deletes an object.

    Example:
        oci os object delete -ns mynamespace -bn mybucket --name myfile.txt
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    if_match = coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    client = build_client('os', ctx)
    render_response(client.delete_object(namespace, bucket_name, name, if_match=if_match, opc_client_request_id=ctx.obj['request_id']), ctx)


@click.command(name='bulk-delete')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--prefix', help='Delete all objects with the given prefix. Omit this parameter to delete all objects in the bucket.')
@click.option('--delimiter', help="When this parameter is set, only objects whose names do not contain the "
                                  "delimiter character (after an optionally specified prefix) are deleted. "
                                  "Scanned objects whose names contain the delimiter have part of their name "
                                  "up to the last occurrence of the delimiter (after the optional prefix) "
                                  "returned as a set of prefixes. Note: Only '/' is a supported delimiter "
                                  "character at this time.")
@click.option('--dry-run', is_flag=True, help='Displays a list of objects which would be deleted by this command, if it were run without --dry-run. If --dry-run is passed, no objects will actually be deleted.')
@click.option('--force', is_flag=True, help='Do not ask for confirmation prior to performing the bulk delete.')
@click.option('--parallel-operations-count', type=click.INT, default=10, show_default=True,
              help='The number of parallel operations to perform. Decreasing this value will make bulk deletes less resource intensive but they may take longer. Increasing this value may improve bulk delete times, but the upload process will consume more system resources and network bandwidth.')
@click.option('--include', multiple=True, help="""Only delete objects which match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--exclude', multiple=True, help="""Only download objects which do not match the provided pattern. Patterns are taken relative to the bucket root. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_delete(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, prefix, delimiter, dry_run, force, include, exclude, parallel_operations_count):
    """
    Deletes all objects in a bucket which match the provided criteria


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
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    prefix = coalesce_provided_and_default_value(ctx, 'prefix', prefix, False)
    delimiter = coalesce_provided_and_default_value(ctx, 'delimiter', delimiter, False)
    dry_run = coalesce_provided_and_default_value(ctx, 'dry-run', dry_run, False)
    force = coalesce_provided_and_default_value(ctx, 'force', force, False)
    include = coalesce_provided_and_default_value(ctx, 'include', include, False)
    exclude = coalesce_provided_and_default_value(ctx, 'exclude', exclude, False)
    parallel_operations_count = coalesce_provided_and_default_value(ctx, 'parallel-operations-count', parallel_operations_count, False)

    if ctx.obj['output'] == 'table':
        raise click.UsageError('Table output is not supported for this operation')

    client = build_client('os', ctx)

    output = {
        'deleted-objects': [],
        'delete-failures': {}
    }

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
                output['deleted-objects'].append(obj.name)

        click.echo(formatted_flat_dict(output))
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
        objects_to_delete.extend(map(lambda obj: obj.name, response.data.objects))

    if not force:
        if include or exclude:
            # If we specify this, the approximate or exact objects to delete is not determinable without paging through the entire list (e.g. in the
            # case that the only matching items are on the last few pages). So in this case just use a generic message
            confirm_prompt = 'WARNING: This command will delete all matching objects in the bucket. Please use --dry-run to list the objects which would be deleted. Are you sure you wish to continue?'
        else:
            if list_objects_responses[-1].data.next_start_with:
                # There are more pages of data
                confirm_prompt = 'WARNING: This command will delete at least {} objects. Are you sure you wish to continue?'.format(len(objects_to_delete))
            else:
                if len(objects_to_delete) == 0:
                    # There are no objects anyway, so just terminate here
                    click.echo('There are no objects to delete in {}'.format(bucket_name), file=sys.stderr)
                    ctx.exit()
                else:
                    confirm_prompt = 'WARNING: This command will delete {} objects. Are you sure you wish to continue?'.format(len(objects_to_delete))

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
                    update_progress_kwargs = {'message': 'Deleted {}'.format(obj)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, obj, 'Deleted')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                add_to_list_args = [obj]
                error_callback_kwargs = {'target_dict': output['delete-failures'], 'target_dict_key': obj}
                add_to_deleted_objects_callback = WorkPoolTaskCallback(output['deleted-objects'].append, *add_to_list_args)
                add_to_delete_failures_callback = WorkPoolTaskErrorCallback(_error_callback_add_item_to_dict, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], success_callbacks=[add_to_deleted_objects_callback], error_callbacks=[add_to_delete_failures_callback])

                delete_kwargs = {
                    'namespace': namespace,
                    'bucket_name': bucket_name,
                    'object_name': obj,
                    'if_match': None,
                    'request_id': ctx.obj['request_id']
                }

                if ctx.obj['debug']:
                    click.echo('Deleting {}'.format(obj), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, obj, 'Deleting'))

                transfer_manager.delete_object(callbacks_container, **delete_kwargs)
            except Exception as e:
                # Don't let one get failure fail the entire batch, but store the error for output later
                output['delete-failures'][obj] = str(e)

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
            objects_to_delete.extend(map(lambda obj: obj.name, list_objects_response.data.objects))
            next_start_with = list_objects_response.data.next_start_with

    transfer_manager.wait_for_completion()
    reusable_progress_bar.render_finish()

    click.echo(formatted_flat_dict(output))

    if len(output['delete-failures']) > 0:
        sys.exit(1)


@click.command(name='resume-put')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--file', type=click.File(mode='rb'), help="The file to load as the content of the object. [required]")
@click.option('--name',
              help='The name of the object. Default value is the filename excluding the path.')
@click.option('--upload-id', help='Upload ID to resume. [required]')
@click.option('--part-size', type=click.INT,
              help='Part size in MiB')
@click.option('--disable-parallel-uploads', is_flag=True,
              help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@click.option('--parallel-upload-count', type=click.INT, default=None,
              help='This option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads. Defaults to 3.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def object_resume_put(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, file, upload_id, part_size, disable_parallel_uploads, parallel_upload_count):
    """
    Resume a previous multipart put.

    Example:
        oci os object resume-put -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt --upload-id my-upload-id
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, False)
    upload_id = coalesce_provided_and_default_value(ctx, 'upload-id', upload_id, True)
    part_size = coalesce_provided_and_default_value(ctx, 'part-size', part_size, False)
    disable_parallel_uploads = coalesce_provided_and_default_value(ctx, 'disable-parallel-uploads', disable_parallel_uploads, False)
    parallel_upload_count = coalesce_provided_and_default_value(ctx, 'parallel-upload-count', parallel_upload_count, False)

    if not file:
        file_from_default_values = get_click_file_from_default_values_file(ctx, 'file', 'rb', True)
        if file_from_default_values:
            file = file_from_default_values

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

    client = build_client('os', ctx)

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


objectstorage.add_command(object_group)
object_group.add_command(object_list)
object_group.add_command(object_bulk_put)
object_group.add_command(object_put)
object_group.add_command(object_bulk_get)
object_group.add_command(object_get)
object_group.add_command(object_head)
object_group.add_command(object_bulk_delete)
object_group.add_command(object_delete)
object_group.add_command(object_resume_put)


@click.group(name='multipart')
@help_option_group
def multipart():
    pass


@click.command(name='list')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('--limit', default=100, type=int, show_default=True, help='The maximum number of items to return.')
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[MultipartUploadPartSummary]'})
@wrap_exceptions
def multipart_list(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, limit, page):
    """
    List uncommitted multipart uploads for a namespace and bucket

    Example:
        oci os multipart list -ns mynamespace -bn mybucket
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    limit = coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = coalesce_provided_and_default_value(ctx, 'page', page, False)

    client = build_client('os', ctx)

    args = {
        'opc_client_request_id': ctx.obj['request_id'],
        'limit': limit
    }

    if page:
        args['page'] = page

    render_response(client.list_multipart_uploads(namespace, bucket_name, **args), ctx)


@click.command(name='abort')
@click.option('-ns', '--namespace', help='The top-level namespace used for the request. [required]')
@click.option('-bn', '--bucket-name', help='The name of the bucket. [required]')
@click.option('-on', '--object-name', help='The name of the object. [required]')
@click.option('--upload-id', help='Upload ID to abort. [required]')
@click.option('--force', is_flag=True, help='Abort the existing multipart upload without a confirmation prompt.')
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def multipart_abort(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, object_name, upload_id, force):
    """
    Aborts an uncommitted multipart upload

    Example:
        oci os multipart abort -ns mynamespace -bn mybucket --name myfile.txt --upload-id my-upload-id
    """
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    object_name = coalesce_provided_and_default_value(ctx, 'object-name', object_name, True)
    upload_id = coalesce_provided_and_default_value(ctx, 'upload-id', upload_id, True)
    force = coalesce_provided_and_default_value(ctx, 'force', force, False)

    client = build_client('os', ctx)

    if not force:
        try:
            response = client.list_multipart_upload_parts(namespace, bucket_name, object_name, upload_id, limit=1)
            render_response(response, ctx)
            if response.status == 200:
                if not click.confirm("WARNING: Are you sure you want to permanently remove this incomplete upload?"):
                    ctx.abort()
        except exceptions.ServiceError as e:
            if e.status != 404:
                raise

    render_response(client.abort_multipart_upload(namespace, bucket_name, object_name, upload_id), ctx)


objectstorage.add_command(multipart)
multipart.add_command(multipart_list)
multipart.add_command(multipart_abort)


@click.group('preauth-request', short_help="""Operations on pre-authenticated requests.""", help="""Pre-authenticated requests provide a way to allow access to specified object operations for a fixed amount of time without performing authentication.

The access-uri will only be returned from the create operation for a pre-authenticated request (not get or list).  Note the access-uri value upon creation in order to use the pre-authenticated request later.""")
@help_option_group
def preauthenticated_request_group():
    pass


@preauthenticated_request_group.command(name='create', help="""Creates a pre-authenticated request.

The access-uri will only be returned from the create operation for a pre-authenticated request (not get or list).  Note the access-uri value upon creation in order to use the pre-authenticated request later.""")
@click.option('-ns', '--namespace', help="""The top-level namespace used for the request. [required]""")
@click.option('-bn', '--bucket-name', help="""The name of the bucket.

Example: `my-new-bucket1` [required]""")
@click.option('--name', help="""The user specified name for pre-authenticated request. Helpful for management purposes. [required]""")
@click.option('--access-type', type=click.Choice(['ObjectRead', 'ObjectWrite', 'ObjectReadWrite', 'AnyObjectWrite']), help="""The operation that can be performed on this resource e.g PUT or GET. [required]""")
@click.option('--time-expires', type=CliDatetime(), help="The expiration date after which the pre-authenticated request will no longer be valid. " + CliDatetime.VALID_DATETIME_CLI_HELP_MESSAGE.strip() + """
\b
[required]""")
@click.option('-on', '--object-name', help="""Name of object that is being granted access to by the pre-authenticated request. This option must be specified if --access-type is ObjectRead, ObjectWrite, or ObjectReadWrite. This option cannot be specified if the --access-type is AnyObjectWrite.""")
@click.option('--opc-client-request-id', help="""The client request ID for tracing.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequest'})
@wrap_exceptions
def create_preauthenticated_request(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, name, access_type, time_expires, object_name, opc_client_request_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    name = coalesce_provided_and_default_value(ctx, 'name', name, True)
    access_type = coalesce_provided_and_default_value(ctx, 'access-type', access_type, True)
    time_expires = coalesce_provided_and_default_value(ctx, 'time-expires', time_expires, True)
    object_name = coalesce_provided_and_default_value(ctx, 'object-name', object_name, False)
    opc_client_request_id = coalesce_provided_and_default_value(ctx, 'opc-client-request-id', opc_client_request_id, False)

    kwargs = {}
    if opc_client_request_id is not None:
        kwargs['opc_client_request_id'] = opc_client_request_id

    details = {}
    details['name'] = name
    details['accessType'] = access_type
    details['timeExpires'] = time_expires

    if object_name is not None:
        details['objectName'] = object_name

    client = build_client('os', ctx)
    result = client.create_preauthenticated_request(
        namespace_name=namespace,
        bucket_name=bucket_name,
        create_preauthenticated_request_details=details,
        **kwargs
    )
    render_response(result, ctx)


@preauthenticated_request_group.command(name='delete', help="""Deletes a pre-authenticateted request.""")
@click.option('-ns', '--namespace', help="""The top-level namespace used for the request. [required]""")
@click.option('-bn', '--bucket-name', help="""The name of the bucket.

Example: `my-new-bucket1` [required]""")
@click.option('--par-id', help="""The unique identifier for the pre-authenticated request (PAR). This can be used to manage the PAR such as GET or DELETE the PAR. [required]""")
@click.option('--opc-client-request-id', help="""The client request ID for tracing.""")
@confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@wrap_exceptions
def delete_preauthenticated_request(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, par_id, opc_client_request_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    par_id = coalesce_provided_and_default_value(ctx, 'par-id', par_id, True)
    opc_client_request_id = coalesce_provided_and_default_value(ctx, 'opc-client-request-id', opc_client_request_id, False)

    kwargs = {}
    if opc_client_request_id is not None:
        kwargs['opc_client_request_id'] = opc_client_request_id
    client = build_client('os', ctx)
    result = client.delete_preauthenticated_request(
        namespace_name=namespace,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    render_response(result, ctx)


@preauthenticated_request_group.command(name='get', help="""Gets a pre-authenticated request.""")
@click.option('-ns', '--namespace', help="""The top-level namespace used for the request. [required]""")
@click.option('-bn', '--bucket-name', help="""The name of the bucket.

Example: `my-new-bucket1` [required]""")
@click.option('--par-id', help="""The unique identifier for the pre-authenticated request (PAR). This can be used to manage the PAR such as GET or DELETE the PAR. [required]""")
@click.option('--opc-client-request-id', help="""The client request ID for tracing.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequest'})
@wrap_exceptions
def get_preauthenticated_request(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, par_id, opc_client_request_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    par_id = coalesce_provided_and_default_value(ctx, 'par-id', par_id, True)
    opc_client_request_id = coalesce_provided_and_default_value(ctx, 'opc-client-request-id', opc_client_request_id, False)

    kwargs = {}
    if opc_client_request_id is not None:
        kwargs['opc_client_request_id'] = opc_client_request_id
    client = build_client('os', ctx)
    result = client.get_preauthenticated_request(
        namespace_name=namespace,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    render_response(result, ctx)


@preauthenticated_request_group.command(name='list', help="""Lists pre-authenticated requests for the bucket""")
@click.option('-ns', '--namespace', help="""The top-level namespace used for the request. [required]""")
@click.option('-bn', '--bucket-name', help="""The name of the bucket.

Example: `my-new-bucket1` [required]""")
@click.option('--object-name-prefix', help="""Pre-authenticated requests returned by the list must have object names starting with prefix""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The page at which to start retrieving results.""")
@click.option('--opc-client-request-id', help="""The client request ID for tracing.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[PreauthenticatedRequest]'})
@wrap_exceptions
def list_preauthenticated_requests(ctx, generate_full_command_json_input, generate_param_json_input, from_json, namespace, bucket_name, object_name_prefix, limit, page, opc_client_request_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    load_context_obj_values_from_defaults(ctx)
    namespace = coalesce_provided_and_default_value(ctx, 'namespace', namespace, True)
    bucket_name = coalesce_provided_and_default_value(ctx, 'bucket-name', bucket_name, True)
    object_name_prefix = coalesce_provided_and_default_value(ctx, 'object-name-prefix', object_name_prefix, False)
    limit = coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = coalesce_provided_and_default_value(ctx, 'page', page, False)
    opc_client_request_id = coalesce_provided_and_default_value(ctx, 'opc-client-request-id', opc_client_request_id, False)

    kwargs = {}
    if object_name_prefix is not None:
        kwargs['object_name_prefix'] = object_name_prefix
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if opc_client_request_id is not None:
        kwargs['opc_client_request_id'] = opc_client_request_id
    client = build_client('os', ctx)
    result = client.list_preauthenticated_requests(
        namespace_name=namespace,
        bucket_name=bucket_name,
        **kwargs
    )
    render_response(result, ctx)


objectstorage.add_command(preauthenticated_request_group)


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
            if len(object_name_to_use) > remaining_width:
                object_name_to_use = 'item'
        else:
            object_name_to_use = object_name

        formatted_progress_bar_label = '{} {}'.format(prefix, object_name_to_use)

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


# This is a thin wrapper so that we can support updating the completion of individual parts when doing bulk uploads/puts via the
# TransferManager. The TransferManager supports callbacks at the "task" completion level (and multipart-uploading an entire file
# is considered a part), but the underlying MultipartObjectAssembler it uses supports callbacks at the part level. This lets
# us hook into that
class BulkPutMultipartUploadProgressBar:
    def __init__(self, progress_bar, total_bytes, label):
        self.label = label
        self.progress_bar = progress_bar  # This should be the below ProgressBar class, not a click.progressbar
        self.bytes_read = 0
        self.total_bytes = total_bytes

    def update(self, bytes_read):
        self.bytes_read += bytes_read

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

    def render_finish(self):
        self._progressbar.render_finish()
