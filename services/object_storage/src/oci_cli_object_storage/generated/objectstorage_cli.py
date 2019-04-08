# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('os_root_group.command_name', 'os'), cls=CommandGroupWithAlias, help=cli_util.override('os_root_group.help', """Common set of Object Storage and Archive Storage APIs for managing buckets, objects, and related resources.
"""), short_help=cli_util.override('os_root_group.short_help', """Object Storage Service API"""))
@cli_util.help_option_group
def os_root_group():
    pass


@click.command(cli_util.override('bucket_group.command_name', 'bucket'), cls=CommandGroupWithAlias, help="""A bucket is a container for storing objects in a compartment within a namespace. A bucket is associated with a single compartment. The compartment has policies that indicate what actions a user can perform on a bucket and all the objects in the bucket. For more information, see [Managing Buckets].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def bucket_group():
    pass


@click.command(cli_util.override('object_lifecycle_policy_group.command_name', 'object-lifecycle-policy'), cls=CommandGroupWithAlias, help="""The collection of lifecycle policy rules that together form the object lifecycle policy of a given bucket.""")
@cli_util.help_option_group
def object_lifecycle_policy_group():
    pass


@click.command(cli_util.override('work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workRequest status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('preauthenticated_request_group.command_name', 'preauthenticated-request'), cls=CommandGroupWithAlias, help="""Pre-authenticated requests provide a way to let users access a bucket or an object without having their own credentials. When you create a pre-authenticated request, a unique URL is generated. Users in your organization, partners, or third parties can use this URL to access the targets identified in the pre-authenticated request. See [Using Pre-Authenticated Requests].

To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def preauthenticated_request_group():
    pass


@click.command(cli_util.override('object_group.command_name', 'object'), cls=CommandGroupWithAlias, help="""To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def object_group():
    pass


@click.command(cli_util.override('namespace_group.command_name', 'namespace'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def namespace_group():
    pass


os_root_group.add_command(bucket_group)
os_root_group.add_command(object_lifecycle_policy_group)
os_root_group.add_command(work_request_error_group)
os_root_group.add_command(work_request_log_entry_group)
os_root_group.add_command(work_request_group)
os_root_group.add_command(preauthenticated_request_group)
os_root_group.add_command(object_group)
os_root_group.add_command(namespace_group)


@object_group.command(name=cli_util.override('abort_multipart_upload.command_name', 'abort-multipart-upload'), help=u"""Aborts an in-progress multipart upload and deletes all parts that have been uploaded.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
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


@work_request_group.command(name=cli_util.override('cancel_work_request.command_name', 'cancel'), help=u"""Cancels a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('commit_multipart_upload.command_name', 'commit-multipart-upload'), help=u"""Commits a multipart upload, which involves checking part numbers and entity tags (ETags) of the parts, to create an aggregate object.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--parts-to-commit', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The part numbers and entity tags (ETags) for the parts to be committed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parts-to-exclude', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The part numbers for the parts to be excluded from the completed object. Each part created for this upload must be in either partsToExclude or partsToCommit, but cannot be in both.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@object_group.command(name=cli_util.override('copy_object.command_name', 'copy'), help=u"""Creates a request to copy an object within a region or to another region.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--source-object-name', required=True, help=u"""The name of the object to be copied.""")
@cli_util.option('--destination-region', required=True, help=u"""The destination region the object will be copied to, for example \"us-ashburn-1\".""")
@cli_util.option('--destination-namespace', required=True, help=u"""The destination Object Storage namespace the object will be copied to.""")
@cli_util.option('--destination-bucket', required=True, help=u"""The destination bucket the object will be copied to.""")
@cli_util.option('--destination-object-name', required=True, help=u"""The name of the destination object resulting from the copy operation.""")
@cli_util.option('--source-object-if-match-e-tag', help=u"""The entity tag (ETag) to match against that of the source object. Used to confirm that the source object with a given name is the version of that object storing a specified ETag.""")
@cli_util.option('--destination-object-if-match-e-tag', help=u"""The entity tag (ETag) to match against that of the destination object (an object intended to be overwritten). Used to confirm that the destination object stored under a given name is the version of that object storing a specified entity tag.""")
@cli_util.option('--destination-object-if-none-match-e-tag', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists in the destination bucket.""")
@cli_util.option('--destination-object-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information. Metadata key-value pairs entered in this field are assigned to the destination object. If you enter no metadata values, the destination object will inherit any existing metadata values associated with the source object.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'destination-object-metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destination-object-metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def copy_object(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, namespace_name, bucket_name, source_object_name, destination_region, destination_namespace, destination_bucket, destination_object_name, source_object_if_match_e_tag, destination_object_if_match_e_tag, destination_object_if_none_match_e_tag, destination_object_metadata):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['sourceObjectName'] = source_object_name
    details['destinationRegion'] = destination_region
    details['destinationNamespace'] = destination_namespace
    details['destinationBucket'] = destination_bucket
    details['destinationObjectName'] = destination_object_name

    if source_object_if_match_e_tag is not None:
        details['sourceObjectIfMatchETag'] = source_object_if_match_e_tag

    if destination_object_if_match_e_tag is not None:
        details['destinationObjectIfMatchETag'] = destination_object_if_match_e_tag

    if destination_object_if_none_match_e_tag is not None:
        details['destinationObjectIfNoneMatchETag'] = destination_object_if_none_match_e_tag

    if destination_object_metadata is not None:
        details['destinationObjectMetadata'] = cli_util.parse_json_parameter("destination_object_metadata", destination_object_metadata)

    client = cli_util.build_client('object_storage', ctx)
    result = client.copy_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        copy_object_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('create_bucket.command_name', 'create'), help=u"""Creates a bucket in the given namespace with a bucket name and optional user-defined metadata. Avoid entering confidential information in bucket names.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--name', required=True, help=u"""The name of the bucket. Valid characters are uppercase or lowercase letters, numbers, and dashes. Bucket names must be unique within an Object Storage namespace. Avoid entering confidential information. example: Example: my-new-bucket1""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to create the bucket.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--public-access-type', type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help=u"""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@cli_util.option('--storage-tier', type=custom_types.CliCaseInsensitiveChoice(["Standard", "Archive"]), help=u"""The type of storage tier of this bucket. A bucket is set to 'Standard' tier by default, which means the bucket will be put in the standard storage tier. When 'Archive' tier type is set explicitly, the bucket is put in the Archive Storage tier. The 'storageTier' property is immutable after bucket is created.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""The OCID of a KMS key id used to call KMS to generate the data key or decrypt the encrypted data key.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def create_bucket(ctx, from_json, namespace_name, name, compartment_id, metadata, public_access_type, storage_tier, freeform_tags, defined_tags, kms_key_id):

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

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('object_storage', ctx)
    result = client.create_bucket(
        namespace_name=namespace_name,
        create_bucket_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('create_multipart_upload.command_name', 'create-multipart-upload'), help=u"""Starts a new multipart upload to a specific object in the given bucket in the given namespace.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object', required=True, help=u"""The name of the object to which this multi-part upload is targeted. Avoid entering confidential information. Example: test/object1.log""")
@cli_util.option('--content-type', help=u"""The content type of the object to upload.""")
@cli_util.option('--content-language', help=u"""The content language of the object to upload.""")
@cli_util.option('--content-encoding', help=u"""The content encoding of the object to upload.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string keys and values for the user-defined metadata for the object. Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@preauthenticated_request_group.command(name=cli_util.override('create_preauthenticated_request.command_name', 'create'), help=u"""Creates a pre-authenticated request specific to the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--name', required=True, help=u"""A user-specified name for the pre-authenticated request. Names can be helpful in managing pre-authenticated requests.""")
@cli_util.option('--access-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ObjectRead", "ObjectWrite", "ObjectReadWrite", "AnyObjectWrite"]), help=u"""The operation that can be performed on this resource.""")
@cli_util.option('--time-expires', required=True, type=custom_types.CLI_DATETIME, help=u"""The expiration date for the pre-authenticated request as per [RFC 3339]. After this date the pre-authenticated request will no longer be valid.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--object-name', help=u"""The name of the object that is being granted access to by the pre-authenticated request. Avoid entering confidential information. The object name can be null and if so, the pre-authenticated request grants access to the entire bucket.""")
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


@bucket_group.command(name=cli_util.override('delete_bucket.command_name', 'delete'), help=u"""Deletes a bucket if the bucket is already empty. If the bucket is not empty, use [DeleteObject] first. You also cannot delete a bucket that has a pre-authenticated request associated with that bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@object_group.command(name=cli_util.override('delete_object.command_name', 'delete'), help=u"""Deletes an object.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@object_lifecycle_policy_group.command(name=cli_util.override('delete_object_lifecycle_policy.command_name', 'delete'), help=u"""Deletes the object lifecycle policy for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_object_lifecycle_policy(ctx, from_json, namespace_name, bucket_name, if_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.delete_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('delete_preauthenticated_request.command_name', 'delete'), help=u"""Deletes the pre-authenticated request for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--par-id', required=True, help=u"""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.""")
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


@bucket_group.command(name=cli_util.override('get_bucket.command_name', 'get'), help=u"""Gets the current representation of the given bucket in the given Object Storage namespace.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["approximateCount", "approximateSize"]), multiple=True, help=u"""Bucket summary includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'approximateCount' (approximate number of objects) and 'approximateSize' (total approximate size in bytes of all objects). For example 'approximateCount,approximateSize'.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def get_bucket(ctx, from_json, namespace_name, bucket_name, if_match, if_none_match, fields):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('get_namespace.command_name', 'get'), help=u"""Each Oracle Cloud Infrastructure tenant is assigned one unique and uneditable Object Storage namespace. The namespace is a system-generated string assigned during account creation. For some older tenancies, the namespace string may be the tenancy name in all lower-case letters. You cannot edit a namespace.

GetNamespace returns the name of the Object Storage namespace for the user making the request.""")
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


@namespace_group.command(name=cli_util.override('get_namespace_metadata.command_name', 'get-namespace-metadata'), help=u"""Gets the metadata for the Object Storage namespace, which contains defaultS3CompartmentId and defaultSwiftCompartmentId.

Any user with the NAMESPACE_READ permission will be able to see the current metadata. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
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


@object_group.command(name=cli_util.override('get_object.command_name', 'get'), help=u"""Gets the metadata and body of an object.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--range', help=u"""Optional byte range to fetch, as described in [RFC 7233], section 2.1. Note that only a single range of bytes is supported.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_object(ctx, from_json, file, namespace_name, bucket_name, object_name, if_match, if_none_match, range):

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

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@object_lifecycle_policy_group.command(name=cli_util.override('get_object_lifecycle_policy.command_name', 'get'), help=u"""Gets the object lifecycle policy for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ObjectLifecyclePolicy'})
@cli_util.wrap_exceptions
def get_object_lifecycle_policy(ctx, from_json, namespace_name, bucket_name):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@preauthenticated_request_group.command(name=cli_util.override('get_preauthenticated_request.command_name', 'get'), help=u"""Gets the pre-authenticated request for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--par-id', required=True, help=u"""The unique identifier for the pre-authenticated request. This can be used to manage operations against the pre-authenticated request, such as GET or DELETE.""")
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


@work_request_group.command(name=cli_util.override('get_work_request.command_name', 'get'), help=u"""Gets the status of the work request for the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('head_bucket.command_name', 'head'), help=u"""Efficiently checks to see if a bucket exists and gets the current entity tag (ETag) for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@object_group.command(name=cli_util.override('head_object.command_name', 'head'), help=u"""Gets the user-defined metadata and entity tag (ETag) for an object.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
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


@bucket_group.command(name=cli_util.override('list_buckets.command_name', 'list'), help=u"""Gets a list of all BucketSummary items in a compartment. A BucketSummary contains only summary fields for the bucket and does not contain fields like the user-defined metadata.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list buckets.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["tags"]), multiple=True, help=u"""Bucket summary in list of buckets includes the 'namespace', 'name', 'compartmentId', 'createdBy', 'timeCreated', and 'etag' fields. This parameter can also include 'tags' (freeformTags and definedTags). The only supported value of this parameter is 'tags' for now. Example 'tags'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[BucketSummary]'})
@cli_util.wrap_exceptions
def list_buckets(ctx, from_json, all_pages, page_size, namespace_name, compartment_id, limit, page, fields):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_buckets,
            namespace_name=namespace_name,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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


@object_group.command(name=cli_util.override('list_multipart_upload_parts.command_name', 'list-multipart-upload-parts'), help=u"""Lists the parts of an in-progress multipart upload.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = cli_util.list_call_get_all_results(
            client.list_multipart_upload_parts,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
            upload_id=upload_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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


@object_group.command(name=cli_util.override('list_multipart_uploads.command_name', 'list-multipart-uploads'), help=u"""Lists all of the in-progress multipart uploads for the given bucket in the given Object Storage namespace.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = cli_util.list_call_get_all_results(
            client.list_multipart_uploads,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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


@object_group.command(name=cli_util.override('list_objects.command_name', 'list'), help=u"""Lists the objects in a bucket.

To use this and other API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--prefix', help=u"""The string to use for matching against the start of object names in a list query.""")
@cli_util.option('--start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--delimiter', help=u"""When this parameter is set, only objects whose names do not contain the delimiter character (after an optionally specified prefix) are returned in the objects key of the response body. Scanned objects whose names contain the delimiter have the part of their name up to the first occurrence of the delimiter (including the optional prefix) returned as a set of prefixes. Note that only '/' is a supported delimiter character at this time.""")
@cli_util.option('--fields', help=u"""Object summary in list of objects includes the 'name' field. This parameter can also include 'size' (object size in bytes), 'md5', and 'timeCreated' (object creation date and time) fields. Value of this parameter should be a comma-separated, case-insensitive list of those field names. For example 'name,timeCreated,md5'. Allowed values are: name, size, timeCreated, md5""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'ListObjects'})
@cli_util.wrap_exceptions
def list_objects(ctx, from_json, all_pages, namespace_name, bucket_name, prefix, start, end, limit, delimiter, fields):

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


@preauthenticated_request_group.command(name=cli_util.override('list_preauthenticated_requests.command_name', 'list'), help=u"""Lists pre-authenticated requests for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name-prefix', help=u"""User-specified object name prefixes can be used to query and return a list of pre-authenticated requests.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
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

        result = cli_util.list_call_get_all_results(
            client.list_preauthenticated_requests,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
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


@work_request_error_group.command(name=cli_util.override('list_work_request_errors.command_name', 'list'), help=u"""Lists the errors of the work request with the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists the logs of the work request with the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list buckets.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'object_storage', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('object_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('put_object.command_name', 'put'), help=u"""Creates a new object or overwrites an existing one. See [Special Instructions for Object Storage PUT] for request signature requirements.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--put-object-body', required=True, help=u"""The object to upload to the object store.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--expect', help=u"""100-continue""")
@cli_util.option('--content-md5', help=u"""The base-64 encoded MD5 hash of the body.""")
@cli_util.option('--content-type', help=u"""The content type of the object.  Defaults to 'application/octet-stream' if not overridden during the PutObject call.""")
@cli_util.option('--content-language', help=u"""The content language of the object.""")
@cli_util.option('--content-encoding', help=u"""The content encoding of the object.""")
@cli_util.option('--opc-meta-', help=u"""Optional user-defined metadata key and value.""")
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

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('object_storage', ctx)
    result = client.put_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name,
        put_object_body=put_object_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_lifecycle_policy_group.command(name=cli_util.override('put_object_lifecycle_policy.command_name', 'put'), help=u"""Creates or replaces the object lifecycle policy for the bucket.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The bucket's set of lifecycle policy rules.

This option is a JSON list with items of type ObjectLifecycleRule.  For documentation on ObjectLifecycleRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/objectstorage/20160918/datatypes/ObjectLifecycleRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'object_storage', 'class': 'list[ObjectLifecycleRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'object_storage', 'class': 'list[ObjectLifecycleRule]'}}, output_type={'module': 'object_storage', 'class': 'ObjectLifecyclePolicy'})
@cli_util.wrap_exceptions
def put_object_lifecycle_policy(ctx, from_json, force, namespace_name, bucket_name, items, if_match, if_none_match):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('object_storage', ctx)
    result = client.put_object_lifecycle_policy(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        put_object_lifecycle_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@object_group.command(name=cli_util.override('rename_object.command_name', 'rename'), help=u"""Rename an object in the given Object Storage namespace.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--source-name', required=True, help=u"""The name of the source object to be renamed.""")
@cli_util.option('--new-name', required=True, help=u"""The new name of the source object.""")
@cli_util.option('--src-obj-if-match-e-tag', help=u"""The if-match entity tag (ETag) of the source object.""")
@cli_util.option('--new-obj-if-match-e-tag', help=u"""The if-match entity tag (ETag) of the new object.""")
@cli_util.option('--new-obj-if-none-match-e-tag', help=u"""The if-none-match entity tag (ETag) of the new object.""")
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


@object_group.command(name=cli_util.override('restore_objects.command_name', 'restore'), help=u"""Restores one or more objects specified by the objectName parameter. By default objects will be restored for 24 hours. Duration can be configured using the hours parameter.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""An object that is in an archive storage tier and needs to be restored.""")
@cli_util.option('--hours', type=click.INT, help=u"""The number of hours for which this object will be restored. By default objects will be restored for 24 hours. You can instead configure the duration using the hours parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restore_objects(ctx, from_json, namespace_name, bucket_name, object_name, hours):

    if isinstance(namespace_name, six.string_types) and len(namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --namespace-name cannot be whitespace or empty string')

    if isinstance(bucket_name, six.string_types) and len(bucket_name.strip()) == 0:
        raise click.UsageError('Parameter --bucket-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_client_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['objectName'] = object_name

    if hours is not None:
        details['hours'] = hours

    client = cli_util.build_client('object_storage', ctx)
    result = client.restore_objects(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        restore_objects_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bucket_group.command(name=cli_util.override('update_bucket.command_name', 'update'), help=u"""Performs a partial or full update of a bucket's user-defined metadata.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--compartment-id', help=u"""The compartmentId for the compartment to which the bucket is targeted to move to.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Arbitrary string, up to 4KB, of keys and values for user-defined metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--public-access-type', type=custom_types.CliCaseInsensitiveChoice(["NoPublicAccess", "ObjectRead", "ObjectReadWithoutList"]), help=u"""The type of public access enabled on this bucket. A bucket is set to `NoPublicAccess` by default, which only allows an authenticated caller to access the bucket and its contents. When `ObjectRead` is enabled on the bucket, public access is allowed for the `GetObject`, `HeadObject`, and `ListObjects` operations. When `ObjectReadWithoutList` is enabled on the bucket, public access is allowed for the `GetObject` and `HeadObject` operations.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help=u"""A KMS key OCID that will be associated with the given bucket. If it is empty the Update operation will actually remove the KMS key, if there is one, from the given bucket. Note that the old kms key should still be enbaled in KMS otherwise all the objects in the bucket encrypted with the old KMS key will no longer be accessible.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@json_skeleton_utils.get_cli_json_input_option({'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metadata': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'object_storage', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'object_storage', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'object_storage', 'class': 'Bucket'})
@cli_util.wrap_exceptions
def update_bucket(ctx, from_json, namespace_name, bucket_name, compartment_id, metadata, public_access_type, freeform_tags, defined_tags, kms_key_id, if_match):

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

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if kms_key_id is not None:
        details['kmsKeyId'] = kms_key_id

    client = cli_util.build_client('object_storage', ctx)
    result = client.update_bucket(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        update_bucket_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('update_namespace_metadata.command_name', 'update-namespace-metadata'), help=u"""By default, buckets created using the Amazon S3 Compatibility API or the Swift API are created in the root compartment of the Oracle Cloud Infrastructure tenancy.

You can change the default Swift/Amazon S3 compartmentId designation to a different compartmentId. All subsequent bucket creations will use the new default compartment, but no previously created buckets will be modified. A user must have NAMESPACE_UPDATE permission to make changes to the default compartments for Amazon S3 and Swift.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--default-s3-compartment-id', help=u"""The updated compartment id for use by an S3 client, if this field is set.""")
@cli_util.option('--default-swift-compartment-id', help=u"""The updated compartment id for use by a Swift client, if this field is set.""")
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


@object_group.command(name=cli_util.override('upload_part.command_name', 'upload-part'), help=u"""Uploads a single part of a multipart upload.""")
@cli_util.option('--namespace-name', required=True, help=u"""The Object Storage namespace used for the request.""")
@cli_util.option('--bucket-name', required=True, help=u"""The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`""")
@cli_util.option('--object-name', required=True, help=u"""The name of the object. Avoid entering confidential information. Example: `test/object1.log`""")
@cli_util.option('--upload-id', required=True, help=u"""The upload ID for a multipart upload.""")
@cli_util.option('--upload-part-num', required=True, type=click.INT, help=u"""The part number that identifies the object part currently being uploaded.""")
@cli_util.option('--upload-part-body', required=True, help=u"""The part being uploaded to the Object Storage service.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--if-match', help=u"""The entity tag (ETag) to match. For creating and committing a multipart upload to an object, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--if-none-match', help=u"""The entity tag (ETag) to avoid matching. The only valid value is '*', which indicates that the request should fail if the object already exists. For creating and committing a multipart upload, this is the entity tag of the target object. For uploading a part, this is the entity tag of the target part.""")
@cli_util.option('--expect', help=u"""100-continue""")
@cli_util.option('--content-md5', help=u"""The base-64 encoded MD5 hash of the body.""")
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

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

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
