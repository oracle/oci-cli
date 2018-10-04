# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import arrow
import click
import os
import os.path
import stat
import sys
from oci import exceptions
from oci.object_storage.transfer import constants
from ..cli_util import render, render_response, parse_json_parameter, help_option, help_option_group, build_client, wrap_exceptions, filter_object_headers, get_param
from oci.object_storage import UploadManager, MultipartObjectAssembler
from oci_cli.file_filters import BaseFileFilterCollection
from oci_cli.file_filters import SingleTypeFileFilterCollection
from retrying import retry
from .. import retry_utils
from ..object_storage_transfer_manager import TransferManager, TransferManagerConfig, WorkPoolTaskCallback, WorkPoolTaskErrorCallback, WorkPoolTaskSuccessCallback, WorkPoolTaskCallbacksContainer
from .. import json_skeleton_utils
from ..aliasing import CommandGroupWithAlias
from .. import custom_types  # noqa: F401
from ..custom_types import BulkPutOperationOutput, BulkGetOperationOutput, BulkDeleteOperationOutput
from ..generated import objectstorage_cli
from .. import cli_util

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

objectstorage_cli.object_group.commands.pop(objectstorage_cli.abort_multipart_upload.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.copy_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.create_multipart_upload.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.commit_multipart_upload.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.get_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.head_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_objects.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_multipart_upload_parts.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.list_multipart_uploads.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.put_object.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.restore_objects.name)
objectstorage_cli.object_group.commands.pop(objectstorage_cli.upload_part.name)
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
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[ObjectSummary]'})
@wrap_exceptions
def object_list(ctx, from_json, namespace, bucket_name, prefix, start, end, limit, delimiter, fields, all_pages, page_size):
    """
    Lists the objects in a bucket.

    Example:
        oci os object list -ns mynamespace -bn mybucket --fields name,size,timeCreated
    """
    if all_pages and limit is not None:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    elif not all_pages and limit is None:
        limit = 100

    client = build_client('object_storage', ctx)

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

        objects = response.data.objects
        next_start = response.data.next_start_with
        all_objects.extend(objects)

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

    render(all_objects, metadata, ctx, display_all_headers=True)


@objectstorage_cli.object_group.command(name='put')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='The top-level namespace used for the request.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--file', type=click.File(mode='rb'), required=True,
                 help="The file to load as the content of the object, or '-' to read from STDIN.")
@cli_util.option('--name',
                 help='The name of the object. Default value is the filename excluding the path. Required if reading object from STDIN.')
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--content-md5', help='The base-64 encoded MD5 hash of the body.')
@cli_util.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@cli_util.option('--content-type', help='The content type of the object.')
@cli_util.option('--content-language', help='The content language of the object.')
@cli_util.option('--content-encoding', help='The content encoding of the object.')
@cli_util.option('--force', is_flag=True, help='If the object already exists, overwrite the existing object without a confirmation prompt.')
@cli_util.option('--no-overwrite', is_flag=True, help='If the object already exists, do not overwrite the existing object.')
@cli_util.option('--no-multipart', is_flag=True,
                 help='Do not use multipart uploads to upload the file in parts. By default files above 128 MiB will be uploaded in multiple parts, then combined server-side.')
@cli_util.option('--part-size', type=click.INT,
                 help='Part size (in MiB) to use if uploading via multipart upload operations')
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='If the object will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel.')
@cli_util.option('--parallel-upload-count', type=click.INT, default=None,
                 help='If the object will be uploaded in multiple parts, this option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads or --no-multipart. Defaults to 3.')
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}}, output_type={'module': 'object_storage', 'class': 'ObjectSummary'})
@wrap_exceptions
def object_put(ctx, from_json, namespace, bucket_name, name, file, if_match, content_md5, metadata, content_type, content_language, content_encoding, force, no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count):
    """
    Creates a new object or overwrites an existing one.

    The object can be uploaded as a single part or as multiple parts. Below are the rules for whether an object will be uploaded via single or multipart upload (listed in order of precedence):

        * If the object is being uploaded from STDIN, it will be uploaded as a multipart upload (if the object content is smaller than --part-size, default for STDIN is 10 MiB, the multipart upload may contain only one part, but it will still use the MultipartUpload API)

        * If the --no-multipart flag is specified, the object will be uploaded as a single part regardless of size (specifying --no-multipart when uploading from STDIN will result in an error)

        * If the object is larger than --part-size, it will be uploaded as multiple parts (the default part size is 128 MiB)

        * If the object is empty it will be uploaded as a single part

    Example:
        oci os object put -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt --metadata '{"key1":"value1","key2":"value2"}'
    """
    # explicitly disallow retries for object put because we may not be able to re-read the input source
    ctx.obj['no_retry'] = True

    client = build_client('object_storage', ctx)

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


@objectstorage_cli.object_group.command(name='bulk-upload')
@cli_util.option('-ns', '--namespace', '--namespace-name', 'namespace', required=True, help='Object Storage namespace.')
@cli_util.option('-bn', '--bucket-name', required=True, help='The name of the bucket.')
@cli_util.option('--src-dir', required=True, help='The directory which contains files to upload. Files in the directory and all subdirectories will be uploaded.')
@cli_util.option('--object-prefix', help='A prefix to apply to the names of all files being uploaded')
@cli_util.option('--metadata', help='Arbitrary string keys and values for user-defined metadata. This will be applied to all files being uploaded. Must be in JSON format. Example: \'{"key1":"value1","key2":"value2"}\'')
@cli_util.option('--content-type', help='The content type to apply to all files being uploaded.')
@cli_util.option('--content-language', help='The content language to apply to all files being uploaded.')
@cli_util.option('--content-encoding', help='The content encoding to apply to all files being uploaded.')
@cli_util.option('--overwrite', is_flag=True, help="""If a file being uploaded already exists in Object Storage, overwrite the existing object in Object Storage without a confirmation prompt. If neither this flag nor --no-overwrite is specified, you will be prompted each time an object would be overwritten.

Specifying this flag will also allow for faster uploads as the CLI will not initially check whether or not the files already exist in Object Storage.""")
@cli_util.option('--no-overwrite', is_flag=True, help='If a file being uploaded already exists in Object Storage, do not overwite it. If neither this flag nor --overwrite is specified, you will be prompted each time an object would be overwritten')
@cli_util.option('--no-multipart', is_flag=True,
                 help='Do not use multipart uploads to upload the file in parts. By default files above 128 MiB will be uploaded in multiple parts, then combined server-side. This applies to all files being uploaded')
@cli_util.option('--part-size', type=click.INT,
                 help='Part size (in MiB) to use if uploading via multipart upload operations. This applies to all files which will be uploaded in multiple parts. Part size must be greater than 10 MiB')
@cli_util.option('--disable-parallel-uploads', is_flag=True,
                 help='[DEPRECATED] This option is no longer used. If a file in the directory will be uploaded in multiple parts, this option disables those parts from being uploaded in parallel. This applies to all files being uploaded in multiple parts')
@cli_util.option('--parallel-upload-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform. Decreasing this value will make bulk uploads less resource intensive but they may take longer. Increasing this value may improve bulk upload times, but the upload process will consume more system resources and network bandwidth.')
@cli_util.option('--include', multiple=True, help="""Only upload files which match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@cli_util.option('--exclude', multiple=True, help="""Only upload files which do not match the provided pattern. Patterns are taken relative to the CURRENT directory. This option can be provided mulitple times to match on mulitple patterns. Supported pattern symbols are:
\b
{}
""".format(INCLUDE_EXCLUDE_PATTERN))
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, str)'}})
@wrap_exceptions
def object_bulk_put(ctx, from_json, namespace, bucket_name, src_dir, object_prefix, metadata, content_type, content_language, content_encoding, overwrite, no_overwrite, no_multipart, part_size, disable_parallel_uploads, parallel_upload_count, include, exclude):
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
    If a file being uploaded already exists in Object Storage, it can be overwritten without a prompt by
    using the --overwrite flag. Specifying --overwrite will also allow for faster uploads as the CLI will not
    initially check whether or not the files already exist in Object Storage.

    \b
    Prevent object overwrite to resolve object name collision
    ----------------------------------------------------------
    oci os object bulk-upload -ns mynamespace -bn mybucket --src-dir path/to/upload/directory --no-overwrite

    \b
    If a file being uploaded already exists in Object Storage, it can be preserved (not overwritten) without a
    prompt by using the --no-overwrite flag.
    """
    # there is existing retry logic for bulk_put so we don't want the Python SDK level retries to interfere / overlap with that
    ctx.obj['no_retry'] = True

    if include and exclude:
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    expanded_directory = os.path.expandvars(os.path.expanduser(src_dir))
    if not os.path.exists(expanded_directory):
        raise click.UsageError('The specified --src-dir {} (expanded to: {}) does not exist'.format(src_dir, expanded_directory))

    file_filter_collection = _get_file_filter_collection(expanded_directory, include, exclude, None)

    if part_size is not None and no_multipart:
        raise click.UsageError('The option --part-size is not applicable when using the --no-multipart flag.')

    if overwrite and no_overwrite:
        raise click.UsageError('The options --overwrite and --no-overwrite cannot be used together')

    client = build_client('object_storage', ctx)
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
                            output.add_skipped(object_name)
                            continue

                        base_kwargs['if_match'] = head_object.headers['etag']
                        if not click.confirm('WARNING: {} already exists. Are you sure you want to overwrite it?'.format(object_name)):
                            output.add_skipped(object_name)
                            continue

                with open(full_file_path, 'rb') as file_object:
                    file_size = os.fstat(file_object.fileno()).st_size

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': 'Uploaded {}'.format(object_name)}
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

                transfer_manager.upload_object(callbacks_container, namespace, bucket_name, object_name, full_file_path, file_size, **base_kwargs)

                # These can vary per request, so remove them if they exist so we have a blank slate for the next iteration
                base_kwargs.pop('if_none_match', None)
                base_kwargs.pop('if_match', None)
                base_kwargs.pop('multipart_part_completion_callback', None)
            except Exception as e:
                # Don't let one failure here (either HEADing to see if the object exists, or actaully uploading the object)
                # fail the entire batch, but store the error for output later
                output.add_failure(object_name, callback_exception=e)

                if ctx.obj['debug']:
                    click.echo('Failed to upload {}'.format(object_name), file=sys.stderr)

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
@cli_util.option('--file', type=click.File(mode='wb'), required=True,
                 help="The name of the file that will receive the object content, or '-' to write to STDOUT.")
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--if-none-match', help='The entity tag to avoid matching.')
@cli_util.option('--range',
                 help='Byte range to fetch. Follows https://tools.ietf.org/html/rfc7233#section-2.1. Example: bytes=2-10')
@cli_util.option('--multipart-download-threshold', type=click.IntRange(128, None), help='Objects larger than this size (in MiB) will be downloaded in multiple parts. The minimum allowable threshold is 128 MiB.')
@cli_util.option('--part-size', type=click.IntRange(128, None), help='Part size (in MiB) to use when downloading an object in multiple parts. The minimum allowable size is 128 MiB.')
@cli_util.option('--parallel-download-count', type=click.INT, default=10, show_default=True,
                 help='The number of parallel operations to perform when downloading an object in multiple parts. Decreasing this value will make multipart downloads less resource intensive but they may take longer. Increasing this value may improve download times, but the download process will consume more system resources and network bandwidth.')
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_get(ctx, from_json, namespace, bucket_name, name, file, if_match, if_none_match, range, multipart_download_threshold, part_size, parallel_download_count):
    """
    Gets the metadata and body of an object.

    Example:
        oci os object get -ns mynamespace -bn mybucket --name myfile.txt --file /Users/me/myfile.txt
    """
    # No defaulting of the file so that we don't inadvertently overwrite the same file or stream each time
    if range and multipart_download_threshold:
        raise click.UsageError("Cannot specify both the --range and --multipart-download-threshold parameters")

    client = build_client('object_storage', ctx)

    head_object = client.head_object(namespace, bucket_name, name, opc_client_request_id=ctx.obj['request_id'])
    if not head_object:
        raise click.ClickException('The specified object does not exist')
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
            opc_client_request_id=ctx.obj['request_id']
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
            'total_size': object_size_bytes
        }

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
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_bulk_get(ctx, from_json, namespace, bucket_name, prefix, delimiter, download_dir, overwrite, no_overwrite, include, exclude, parallel_operations_count, multipart_download_threshold, part_size):
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
        raise click.UsageError('The --include and --exclude parameters cannot both be provided')

    if not part_size:
        part_size = 128 * MEBIBYTE
    else:
        part_size = part_size * MEBIBYTE

    client = build_client('object_storage', ctx)

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
        'fields': 'name,size'
    }
    keep_paginating = True

    output = BulkGetOperationOutput()

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
            object_size = obj.size

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

                if not overwrite:
                    if not click.confirm('WARNING: {} already exists. Are you sure you want to overwrite it?'.format(object_name)):
                        output.add_skipped(object_name)
                        continue

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

                if ctx.obj['debug']:
                    update_progress_kwargs = {'message': 'Downloaded {}'.format(object_name)}
                    update_progress_callback = WorkPoolTaskCallback(_print_to_console, **update_progress_kwargs)
                else:
                    update_progress_kwargs = {'new_label': _get_progress_bar_label(None, object_name, 'Downloaded')}
                    update_progress_callback = WorkPoolTaskCallback(reusable_progress_bar.update_label_to_end, **update_progress_kwargs)

                error_callback_kwargs = {'failed_item': object_name}
                add_to_download_failures_callback = WorkPoolTaskErrorCallback(output.add_failure, **error_callback_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(completion_callbacks=[update_progress_callback], error_callbacks=[add_to_download_failures_callback])

                if ctx.obj['debug']:
                    click.echo('Downloading {} to {}'.format(object_name, full_file_path), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, object_name, 'Downloading'))

                # If it's not multipart, or it is but we would only have a single part then just download it, otherwise do a multipart get
                # If the part size is somehow not known then use a multipart download by default (the multipart download will
                # try and figure out the size via a HEAD and then take the appropriate action based on the size and threshold)
                if not multipart_download_threshold or (multipart_download_threshold and (object_size and part_size >= object_size)):
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
                    click.echo('Failed to download {}'.format(object_name), file=sys.stderr)

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
@cli_util.option('--if-match', help='The entity tag to match.')
@cli_util.option('--if-none-match', help='The entity tag to avoid matching.')
@json_skeleton_utils.get_cli_json_input_option({})
@help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@wrap_exceptions
def object_head(ctx, from_json, namespace, bucket_name, name, if_match, if_none_match):
    """
    Gets the user-defined metadata and entity tag for an object.

    Example:
        oci os object head -ns mynamespace -bn mybucket --name myfile.txt
    """
    client = build_client('object_storage', ctx)
    response = client.head_object(
        namespace,
        bucket_name,
        name,
        if_match=if_match,
        if_none_match=if_none_match,
        opc_client_request_id=ctx.obj['request_id'])

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

    client = build_client('object_storage', ctx)

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
                    click.echo('Deleting {}'.format(obj), file=sys.stderr)
                else:
                    reusable_progress_bar.reset_progress(100, _get_progress_bar_label(None, obj, 'Deleting'))

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
            objects_to_delete.extend(map(lambda obj: obj.name, list_objects_response.data.objects))
            next_start_with = list_objects_response.data.next_start_with

    transfer_manager.wait_for_completion()
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
@cli_util.option('--parallel-upload-count', type=click.INT, default=None,
                 help='This option allows you to specify the maximum number of parts that can be uploaded in parallel. This option cannot be used with --disable-parallel-uploads. Defaults to 3.')
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

    client = build_client('object_storage', ctx)

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

    client = build_client('object_storage', ctx)
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
    client = build_client('object_storage', ctx)
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
            time_left = time_delta((time_of_archival_dt - arrow.utcnow()).seconds)
            msg = "Restored. You have {} to download the restored object before it is once again archived.".format(time_left)
        except arrow.parser.ParserError:
            msg = "Restored. The object will be re-archived at {}.".format(time_of_archival)
    else:
        msg = "Unknown"

    click.echo(msg, file=sys.stderr)


def time_delta(seconds):
    seconds = abs(int(seconds))
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if hours > 0:
        if minutes == 0:
            return '{} hrs'.format(hours)
        else:
            return '{} hrs {} mins'.format(hours, minutes)
    elif minutes > 0:
        return '{} mins'.format(minutes)
    else:
        return 'less than 1 minute'


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
        oci os multipart abort -ns mynamespace -bn mybucket --name myfile.txt --upload-id my-upload-id
    """
    client = build_client('object_storage', ctx)

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


@cli_util.copy_params_from_generated_command(objectstorage_cli.copy_object, params_to_exclude=['destination_object_name', 'destination_region', 'destination_namespace'])
@objectstorage_cli.object_group.command(name='copy', help=objectstorage_cli.copy_object.help)
@cli_util.option('--destination-region', help="""The destination region object will be copied to.""")
@cli_util.option('--destination-namespace', help="""The destination namespace object will be copied to.""")
@cli_util.option('--destination-object-name', help="""The destination name for the copy object.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def copy_object(ctx, **kwargs):
    if 'source_object_name' in kwargs and ('destination_object_name' not in kwargs or kwargs['destination_object_name'] is None):
        kwargs['destination_object_name'] = kwargs['source_object_name']
    if 'destination_namespace' not in kwargs or kwargs['destination_namespace'] is None:
        client = build_client('object_storage', ctx)
        kwargs['destination_namespace'] = client.get_namespace().data
    if 'destination_region' not in kwargs or kwargs['destination_region'] is None:
        kwargs['destination_region'] = ctx.obj['config']['region']
    ctx.invoke(objectstorage_cli.copy_object, **kwargs)


objectstorage_cli.os_root_group.add_command(multipart)
objectstorage_cli.list_multipart_uploads.name = 'list'
get_param(objectstorage_cli.list_multipart_uploads, 'bucket_name').opts.extend(['-bn'])
get_param(objectstorage_cli.list_multipart_uploads, 'namespace_name').opts.extend(['--namespace', '-ns'])
multipart.add_command(objectstorage_cli.list_multipart_uploads)
multipart.add_command(multipart_abort)


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

    def render_finish(self):
        self._progressbar.render_finish()
