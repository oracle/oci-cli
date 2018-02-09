# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('os_group.command_name', 'os'), cls=CommandGroupWithAlias, help=cli_util.override('os_group.help', """Common set of Object and Archive Storage APIs for managing buckets and objects."""))
@cli_util.help_option_group
def os_group():
    pass


@click.command(cli_util.override('bucket_group.command_name', 'bucket'), cls=CommandGroupWithAlias, help="""A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment.
The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more
information, see [Managing Buckets].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def bucket_group():
    pass


@click.command(cli_util.override('preauthenticated_request_group.command_name', 'preauthenticated-request'), cls=CommandGroupWithAlias, help="""Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials.
When you create a pre-authenticated request, a unique URL is generated. Users in your organization, partners, or third
parties can use this URL to access the targets identified in the pre-authenticated request. See [Managing Access to Buckets and Objects].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def preauthenticated_request_group():
    pass


@click.command(cli_util.override('object_group.command_name', 'object'), cls=CommandGroupWithAlias, help="""To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def object_group():
    pass


@click.command(cli_util.override('namespace_group.command_name', 'namespace'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def namespace_group():
    pass


@object_group.command(name=cli_util.override('abort_multipart_upload.command_name', 'abort-multipart-upload'), help="""Aborts an in-progress multipart upload and deletes all parts that have been uploaded.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--upload-id', callback=cli_util.handle_required_param, help="""The upload ID for a multipart upload. [required]""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def abort_multipart_upload(ctx, from_json, namespace_name, bucket_name, object_name, upload_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.abort_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('commit_multipart_upload.command_name', 'commit-multipart-upload'), help="""Commits a multipart upload, which involves checking part numbers and ETags of the parts, to create an aggregate object.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--upload-id', callback=cli_util.handle_required_param, help="""The upload ID for a multipart upload. [required]""")
@click.option('--parts-to-commit', callback=cli_util.handle_required_param, type=custom_types.CLI_COMPLEX_TYPE, help="""The part numbers and ETags for the parts to be committed. [required]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--parts-to-exclude', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""The part numbers for the parts to be excluded from the completed object. Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({'parts-to-commit': {'module': 'object_storage', 'class': 'list[CommitMultipartUploadPartDetails]'}, 'parts-to-exclude': {'module': 'object_storage', 'class': 'list[integer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parts-to-commit': {'module': 'object_storage', 'class': 'list[CommitMultipartUploadPartDetails]'}, 'parts-to-exclude': {'module': 'object_storage', 'class': 'list[integer]'}})
@cli_util.wrap_exceptions
def commit_multipart_upload(ctx, from_json, namespace_name, bucket_name, object_name, upload_id, parts_to_commit, parts_to_exclude, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['partsToCommit'] = cli_util.parse_json_parameter("parts_to_commit", parts_to_commit)

    if parts_to_exclude is not None:
        details['partsToExclude'] = cli_util.parse_json_parameter("parts_to_exclude", parts_to_exclude)

    client = cli_util.build_client('object_storage', ctx)
    result = client.commit_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        commit_multipart_upload_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('create_bucket.command_name', 'create'), help="""Creates a bucket in the given namespace with a bucket name and optional user-defined metadata.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--name', callback=cli_util.handle_required_param, help="""The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, and dashes. Bucket names must be unique within the namespace. Avoid entering confidential information. example: Example: my-new-bucket1 [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The ID of the compartment in which to create the bucket. [required]""")
@click.option('--metadata', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--public-access-type', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help="""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@click.option('--storage-tier', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["Standard", "Archive"]), help="""The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier' property is immutable after bucket is created.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def create_bucket(ctx, from_json, namespace_name, name, compartment_id, metadata, public_access_type, storage_tier):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['name'] = name
    details['compartmentId'] = compartment_id

    if metadata is not None:
        details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if public_access_type is not None:
        details['publicAccessType'] = public_access_type

    if storage_tier is not None:
        details['storageTier'] = storage_tier

    client = cli_util.build_client('object_storage', ctx)
    result = client.create_bucket(
        namespace_name=namespace_name,
        create_bucket_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('create_multipart_upload.command_name', 'create-multipart-upload'), help="""Starts a new multipart upload to a specific object in the given bucket in the given namespace.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object', callback=cli_util.handle_required_param, help="""The name of the object to which this multi-part upload is targeted. Avoid entering confidential information. Example: test/object1.log [required]""")
@click.option('--content-type', callback=cli_util.handle_optional_param, help="""The content type of the object to upload.""")
@click.option('--content-language', callback=cli_util.handle_optional_param, help="""The content language of the object to upload.""")
@click.option('--content-encoding', callback=cli_util.handle_optional_param, help="""The content encoding of the object to upload.""")
@click.option('--metadata', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}}, output_type={'module': 'object_storage', 'class': 'MultipartUpload'})
@cli_util.wrap_exceptions
def create_multipart_upload(ctx, from_json, namespace_name, bucket_name, object, content_type, content_language, content_encoding, metadata, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['object'] = object

    if content_type is not None:
        details['contentType'] = content_type

    if content_language is not None:
        details['contentLanguage'] = content_language

    if content_encoding is not None:
        details['contentEncoding'] = content_encoding

    if metadata is not None:
        details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    client = cli_util.build_client('object_storage', ctx)
    result = client.create_multipart_upload(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_multipart_upload_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('create_preauthenticated_request.command_name', 'create'), help="""Creates a pre-authenticated request specific to the bucket.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--name', callback=cli_util.handle_required_param, help="""A user-specified name for the pre-authenticated request. Helpful for management purposes. [required]""")
@click.option('--access-type', callback=cli_util.handle_required_param, type=custom_types.CliCaseInsensitiveChoice(["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]), help="""The operation that can be performed on this resource. [required]""")
@click.option('--time-expires', callback=cli_util.handle_required_param, type=custom_types.CLI_DATETIME, help="""The expiration date for the pre-authenticated request as per [RFC 3339]. After this date the pre-authenticated request will no longer be valid. [required]""")
@click.option('--object-name', callback=cli_util.handle_optional_param, help="""The name of object that is being granted access to by the pre-authenticated request. This can be null and if it is, the pre-authenticated request grants access to the entire bucket.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequest'})
@cli_util.wrap_exceptions
def create_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, name, access_type, time_expires, object_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['name'] = name
    details['accessType'] = access_type
    details['timeExpires'] = time_expires

    if object_name is not None:
        details['objectName'] = object_name

    client = cli_util.build_client('object_storage', ctx)
    result = client.create_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        create_preauthenticated_request_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('delete_bucket.command_name', 'delete'), help="""Deletes a bucket if it is already empty. If the bucket is not empty, use [DeleteObject] first.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_bucket(ctx, from_json, namespace_name, bucket_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.delete_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('delete_object.command_name', 'delete'), help="""Deletes an object.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_object(ctx, from_json, namespace_name, bucket_name, object_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.delete_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('delete_preauthenticated_request.command_name', 'delete'), help="""Deletes the pre-authenticated request for the bucket.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--par-id', callback=cli_util.handle_required_param, help="""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE. [required]""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, par_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(par_id, six.string_types) and len(par_id.strip()) == 0:
        raise click.UsageError('Parameter --par-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.delete_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('get_bucket.command_name', 'get'), help="""Gets the current representation of the given bucket in the given namespace.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def get_bucket(ctx, from_json, namespace_name, bucket_name, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('get_namespace.command_name', 'get'), help="""Namespaces are unique. Namespaces are either the tenancy name or a random string automatically generated during account creation. You cannot edit a namespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_namespace(ctx, from_json, ):
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_namespace(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('get_namespace_metadata.command_name', 'get-namespace-metadata'), help="""Get the metadata for the namespace, which contains defaultS3CompartmentId and defaultSwiftCompartmentId. Any user with the NAMESPACE_READ permission will be able to see the current metadata. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'NamespaceMetadata'})
@cli_util.wrap_exceptions
def get_namespace_metadata(ctx, from_json, namespace_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_namespace_metadata(
        namespace_name=namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('get_object.command_name', 'get'), help="""Gets the metadata and body of an object.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--range', callback=cli_util.handle_optional_param, help="""Optional byte range to fetch, as described in [RFC 7233], section 2.1. Note that only a single range of bytes is supported.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_object(ctx, from_json, namespace_name, bucket_name, object_name, if_match, if_none_match, range):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if range is not None:
        kwargs['range'] = range
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('get_preauthenticated_request.command_name', 'get'), help="""Gets the pre-authenticated request for the bucket.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--par-id', callback=cli_util.handle_required_param, help="""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'PreauthenticatedRequestSummary'})
@cli_util.wrap_exceptions
def get_preauthenticated_request(ctx, from_json, namespace_name, bucket_name, par_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(par_id, six.string_types) and len(par_id.strip()) == 0:
        raise click.UsageError('Parameter --par-id cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_preauthenticated_request(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        par_id=par_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('head_bucket.command_name', 'head'), help="""Efficiently checks to see if a bucket exists and gets the current ETag for the bucket.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_bucket(ctx, from_json, namespace_name, bucket_name, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.head_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('head_object.command_name', 'head'), help="""Gets the user-defined metadata and entity tag for an object.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_object(ctx, from_json, namespace_name, bucket_name, object_name, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.head_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('list_buckets.command_name', 'list'), help="""Gets a list of all `BucketSummary`s in a compartment. A `BucketSummary` contains only summary fields for the bucket and does not contain fields like the user-defined metadata.

To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The ID of the compartment in which to list buckets. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The page at which to start retrieving results.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[BucketSummary]'})
@cli_util.wrap_exceptions
def list_buckets(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_buckets,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_buckets,
            limit,
            page_size,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_buckets(
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('list_multipart_upload_parts.command_name', 'list-multipart-upload-parts'), help="""Lists the parts of an in-progress multipart upload.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--upload-id', callback=cli_util.handle_required_param, help="""The upload ID for a multipart upload. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The page at which to start retrieving results.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[MultipartUploadPartSummary]'})
@cli_util.wrap_exceptions
def list_multipart_upload_parts(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, object_name, upload_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_multipart_upload_parts,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_multipart_upload_parts,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    else:
        result = client.list_multipart_upload_parts(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('list_multipart_uploads.command_name', 'list-multipart-uploads'), help="""Lists all in-progress multipart uploads for the given bucket in the given namespace.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The page at which to start retrieving results.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[MultipartUpload]'})
@cli_util.wrap_exceptions
def list_multipart_uploads(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_multipart_uploads,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_multipart_uploads,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_multipart_uploads(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('list_objects.command_name', 'list'), help="""Lists the objects in a bucket.

To use this and other API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--prefix', callback=cli_util.handle_optional_param, help="""The string to use for matching against the start of object names in a list query.""")
@click.option('--start', callback=cli_util.handle_optional_param, help="""Object names returned by a list query must be greater or equal to this parameter.""")
@click.option('--end', callback=cli_util.handle_optional_param, help="""Object names returned by a list query must be strictly less than this parameter.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--delimiter', callback=cli_util.handle_optional_param, help="""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@click.option('--fields', callback=cli_util.handle_optional_param, help="""Object summary in list of objects includes the 'name' field. This parameter can also include 'size' (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields. Value of this parameter should be a comma-separated, case-insensitive list of those field names. For example 'name,timeCreated,md5'. Allowed values are: name, size, timeCreated, md5""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ListObjects'})
@cli_util.wrap_exceptions
def list_objects(ctx, from_json, namespace_name, bucket_name, prefix, start, end, limit, delimiter, fields):

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
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.list_objects(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('list_preauthenticated_requests.command_name', 'list'), help="""Lists pre-authenticated requests for the bucket.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name-prefix', callback=cli_util.handle_optional_param, help="""User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return.""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The page at which to start retrieving results.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[PreauthenticatedRequestSummary]'})
@cli_util.wrap_exceptions
def list_preauthenticated_requests(ctx, from_json, all_pages, page_size, namespace_name, bucket_name, object_name_prefix, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if object_name_prefix is not None:
        kwargs['object_name_prefix'] = object_name_prefix
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_preauthenticated_requests,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_preauthenticated_requests,
            limit,
            page_size,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    else:
        result = client.list_preauthenticated_requests(
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('put_object.command_name', 'put'), help="""Creates a new object or overwrites an existing one.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--put-object-body', callback=cli_util.handle_required_param, help="""The object to upload to the object store. [required]""")
@click.option('--content-length', callback=cli_util.handle_optional_param, type=click.INT, help="""The content length of the body.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--expect', callback=cli_util.handle_optional_param, help="""100-continue""")
@click.option('--content-md5', callback=cli_util.handle_optional_param, help="""The base-64 encoded MD5 hash of the body.""")
@click.option('--content-type', callback=cli_util.handle_optional_param, help="""The content type of the object.  Defaults to 'application/octet-stream' if not overridden during the PutObject call.""")
@click.option('--content-language', callback=cli_util.handle_optional_param, help="""The content language of the object.""")
@click.option('--content-encoding', callback=cli_util.handle_optional_param, help="""The content encoding of the object.""")
@click.option('--opc-meta-', callback=cli_util.handle_optional_param, help="""Optional user-defined metadata key and value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def put_object(ctx, from_json, namespace_name, bucket_name, object_name, put_object_body, content_length, if_match, if_none_match, expect, content_md5, content_type, content_language, content_encoding, opc_meta_):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if expect is not None:
        kwargs['expect'] = expect
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    if content_type is not None:
        kwargs['content_type'] = content_type
    if content_language is not None:
        kwargs['content_language'] = content_language
    if content_encoding is not None:
        kwargs['content_encoding'] = content_encoding
    if opc_meta_ is not None:
        kwargs['opc_meta_'] = opc_meta_
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.put_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        put_object_body=put_object_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('rename_object.command_name', 'rename'), help="""Rename an object from source key to target key in the given namespace.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--source-name', callback=cli_util.handle_required_param, help="""The name of the source object to be renamed. [required]""")
@click.option('--new-name', callback=cli_util.handle_required_param, help="""The new name of the source object. [required]""")
@click.option('--src-obj-if-match-e-tag', callback=cli_util.handle_optional_param, help="""The if-match entity tag of the source object.""")
@click.option('--new-obj-if-match-e-tag', callback=cli_util.handle_optional_param, help="""The if-match entity tag of the new object.""")
@click.option('--new-obj-if-none-match-e-tag', callback=cli_util.handle_optional_param, help="""The if-none-match entity tag of the new object.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def rename_object(ctx, from_json, namespace_name, bucket_name, source_name, new_name, src_obj_if_match_e_tag, new_obj_if_match_e_tag, new_obj_if_none_match_e_tag):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['sourceName'] = source_name
    details['newName'] = new_name

    if src_obj_if_match_e_tag is not None:
        details['srcObjIfMatchETag'] = src_obj_if_match_e_tag

    if new_obj_if_match_e_tag is not None:
        details['newObjIfMatchETag'] = new_obj_if_match_e_tag

    if new_obj_if_none_match_e_tag is not None:
        details['newObjIfNoneMatchETag'] = new_obj_if_none_match_e_tag

    client = cli_util.build_client('object_storage', ctx)
    result = client.rename_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        rename_object_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('restore_objects.command_name', 'restore'), help="""Restore one or more objects specified by objectName parameter.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""A object which was in an archived state and need to be restored. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_objects(ctx, from_json, namespace_name, bucket_name, object_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['objectName'] = object_name

    client = cli_util.build_client('object_storage', ctx)
    result = client.restore_objects(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        restore_objects_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('update_bucket.command_name', 'update'), help="""Performs a partial or full update of a bucket's user-defined metadata.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_optional_param, help="""The compartmentId for the compartment to which the bucket is targeted to move to.""")
@click.option('--metadata', callback=cli_util.handle_optional_param, type=custom_types.CLI_COMPLEX_TYPE, help="""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--public-access-type', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help="""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def update_bucket(ctx, from_json, namespace_name, bucket_name, compartment_id, metadata, public_access_type, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if bucket_name is not None:
        details['name'] = bucket_name

    if metadata is not None:
        details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if public_access_type is not None:
        details['publicAccessType'] = public_access_type

    client = cli_util.build_client('object_storage', ctx)
    result = client.update_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        update_bucket_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('update_namespace_metadata.command_name', 'update-namespace-metadata'), help="""Change the default Swift/S3 compartmentId of user's namespace into the user-defined compartmentId. Upon doing this, all subsequent bucket creations will use the new default compartment, but no previously created buckets will be modified. A user must have the NAMESPACE_UPDATE permission to make changes to the default compartments for S3 and Swift.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--default-s3-compartment-id', callback=cli_util.handle_optional_param, help="""The update compartment id for an S3 client if this field is set.""")
@click.option('--default-swift-compartment-id', callback=cli_util.handle_optional_param, help="""The update compartment id for a Swift client if this field is set.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'NamespaceMetadata'})
@cli_util.wrap_exceptions
def update_namespace_metadata(ctx, from_json, namespace_name, default_s3_compartment_id, default_swift_compartment_id):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')
    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if default_s3_compartment_id is not None:
        details['defaultS3CompartmentId'] = default_s3_compartment_id

    if default_swift_compartment_id is not None:
        details['defaultSwiftCompartmentId'] = default_swift_compartment_id

    client = cli_util.build_client('object_storage', ctx)
    result = client.update_namespace_metadata(
        namespace_name=namespace_name,
        update_namespace_metadata_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('upload_part.command_name', 'upload-part'), help="""Uploads a single part of a multipart upload.""")
@click.option('--namespace-name', callback=cli_util.handle_required_param, help="""The top-level namespace used for the request. [required]""")
@click.option('--bucket-name', callback=cli_util.handle_required_param, help="""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1` [required]""")
@click.option('--object-name', callback=cli_util.handle_required_param, help="""The name of the object. Avoid entering confidential information. Example: `test/object1.log` [required]""")
@click.option('--upload-id', callback=cli_util.handle_required_param, help="""The upload ID for a multipart upload. [required]""")
@click.option('--upload-part-num', callback=cli_util.handle_required_param, type=click.INT, help="""The part number that identifies the object part currently being uploaded. [required]""")
@click.option('--upload-part-body', callback=cli_util.handle_required_param, help="""The part being uploaded to the Object Storage Service. [required]""")
@click.option('--content-length', callback=cli_util.handle_optional_param, type=click.INT, help="""The content length of the body.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""The entity tag to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--if-none-match', callback=cli_util.handle_optional_param, help="""The entity tag to avoid matching. The only valid value is \u2018*\u2019, which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@click.option('--expect', callback=cli_util.handle_optional_param, help="""100-continue""")
@click.option('--content-md5', callback=cli_util.handle_optional_param, help="""The base-64 encoded MD5 hash of the body.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upload_part(ctx, from_json, namespace_name, bucket_name, object_name, upload_id, upload_part_num, upload_part_body, content_length, if_match, if_none_match, expect, content_md5):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    if isinstance(object_name, six.string_types) and len(object_name.strip()) == 0:
        raise click.UsageError('Parameter --object-name cannot be whitespace or empty string')
    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if expect is not None:
        kwargs['expect'] = expect
    if content_md5 is not None:
        kwargs['content_md5'] = content_md5
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.upload_part(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        upload_id=upload_id,
        upload_part_num=upload_part_num,
        upload_part_body=upload_part_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)
