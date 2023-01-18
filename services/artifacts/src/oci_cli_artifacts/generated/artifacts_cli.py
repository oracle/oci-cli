# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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


@cli.command(cli_util.override('artifacts.artifacts_root_group.command_name', 'artifacts'), cls=CommandGroupWithAlias, help=cli_util.override('artifacts.artifacts_root_group.help', """API covering the Artifacts and [Registry] services.
Use this API to manage resources such as generic artifacts and container images."""), short_help=cli_util.override('artifacts.artifacts_root_group.short_help', """Artifacts and Container Images API"""))
@cli_util.help_option_group
def artifacts_root_group():
    pass


@click.command(cli_util.override('artifacts.container_image_summary_group.command_name', 'container-image-summary'), cls=CommandGroupWithAlias, help="""Container image summary.""")
@cli_util.help_option_group
def container_image_summary_group():
    pass


@click.command(cli_util.override('artifacts.container_image_signature_summary_group.command_name', 'container-image-signature-summary'), cls=CommandGroupWithAlias, help="""Container image signature summary.""")
@cli_util.help_option_group
def container_image_signature_summary_group():
    pass


@click.command(cli_util.override('artifacts.container_configuration_group.command_name', 'container-configuration'), cls=CommandGroupWithAlias, help="""Container configuration.""")
@cli_util.help_option_group
def container_configuration_group():
    pass


@click.command(cli_util.override('artifacts.container_repository_group.command_name', 'container-repository'), cls=CommandGroupWithAlias, help="""Container repository metadata.""")
@cli_util.help_option_group
def container_repository_group():
    pass


@click.command(cli_util.override('artifacts.generic_artifact_group.command_name', 'generic-artifact'), cls=CommandGroupWithAlias, help="""The metadata of the artifact.""")
@cli_util.help_option_group
def generic_artifact_group():
    pass


@click.command(cli_util.override('artifacts.repository_group.command_name', 'repository'), cls=CommandGroupWithAlias, help="""The metadata for the artifact repository.""")
@cli_util.help_option_group
def repository_group():
    pass


@click.command(cli_util.override('artifacts.container_image_group.command_name', 'container-image'), cls=CommandGroupWithAlias, help="""Container image metadata.""")
@cli_util.help_option_group
def container_image_group():
    pass


@click.command(cli_util.override('artifacts.container_image_signature_group.command_name', 'container-image-signature'), cls=CommandGroupWithAlias, help="""Container image signature metadata.""")
@cli_util.help_option_group
def container_image_signature_group():
    pass


artifacts_root_group.add_command(container_image_summary_group)
artifacts_root_group.add_command(container_image_signature_summary_group)
artifacts_root_group.add_command(container_configuration_group)
artifacts_root_group.add_command(container_repository_group)
artifacts_root_group.add_command(generic_artifact_group)
artifacts_root_group.add_command(repository_group)
artifacts_root_group.add_command(container_image_group)
artifacts_root_group.add_command(container_image_signature_group)


@container_repository_group.command(name=cli_util.override('artifacts.change_container_repository_compartment.command_name', 'change-compartment'), help=u"""Moves a container repository into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeContainerRepositoryCompartment)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the container repository.

Example: `ocid1.containerrepo.oc1..exampleuniqueID`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which to move the resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_container_repository_compartment(ctx, from_json, repository_id, compartment_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.change_container_repository_compartment(
        repository_id=repository_id,
        change_container_repository_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.change_repository_compartment.command_name', 'change-compartment'), help=u"""Moves a repository into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeRepositoryCompartment)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the repository should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_repository_compartment(ctx, from_json, repository_id, compartment_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.change_repository_compartment(
        repository_id=repository_id,
        change_repository_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_image_signature_group.command(name=cli_util.override('artifacts.create_container_image_signature.command_name', 'create'), help=u"""Upload a signature to an image. \n[Command Reference](createContainerImageSignature)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which the container repository exists.""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.

Example: `ocid1.containerimage.oc1..exampleuniqueID`""")
@cli_util.option('--kms-key-id', required=True, help=u"""The [OCID] of the kmsKeyId used to sign the container image.

Example: `ocid1.key.oc1..exampleuniqueID`""")
@cli_util.option('--kms-key-version-id', required=True, help=u"""The [OCID] of the kmsKeyVersionId used to sign the container image.

Example: `ocid1.keyversion.oc1..exampleuniqueID`""")
@cli_util.option('--message', required=True, help=u"""The base64 encoded signature payload that was signed.""")
@cli_util.option('--signature', required=True, help=u"""The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.""")
@cli_util.option('--signing-algorithm', required=True, type=custom_types.CliCaseInsensitiveChoice(["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"]), help=u"""The algorithm to be used for signing. These are the only supported signing algorithms for container images.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImageSignature'})
@cli_util.wrap_exceptions
def create_container_image_signature(ctx, from_json, compartment_id, image_id, kms_key_id, kms_key_version_id, message, signature, signing_algorithm, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['imageId'] = image_id
    _details['kmsKeyId'] = kms_key_id
    _details['kmsKeyVersionId'] = kms_key_version_id
    _details['message'] = message
    _details['signature'] = signature
    _details['signingAlgorithm'] = signing_algorithm

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.create_container_image_signature(
        create_container_image_signature_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_repository_group.command(name=cli_util.override('artifacts.create_container_repository.command_name', 'create'), help=u"""Create a new empty container repository. Avoid entering confidential information. \n[Command Reference](createContainerRepository)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the resource.""")
@cli_util.option('--display-name', required=True, help=u"""The container repository name.""")
@cli_util.option('--is-immutable', type=click.BOOL, help=u"""Whether the repository is immutable. Images cannot be overwritten in an immutable repository.""")
@cli_util.option('--is-public', type=click.BOOL, help=u"""Whether the repository is public. A public repository allows unauthenticated access.""")
@cli_util.option('--readme', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}}, output_type={'module': 'artifacts', 'class': 'ContainerRepository'})
@cli_util.wrap_exceptions
def create_container_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, is_immutable, is_public, readme):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name

    if is_immutable is not None:
        _details['isImmutable'] = is_immutable

    if is_public is not None:
        _details['isPublic'] = is_public

    if readme is not None:
        _details['readme'] = cli_util.parse_json_parameter("readme", readme)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.create_container_repository(
        create_container_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_repository') and callable(getattr(client, 'get_container_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_container_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.create_repository.command_name', 'create'), help=u"""Creates a new repository for storing artifacts. \n[Command Reference](createRepository)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the repository's compartment.""")
@cli_util.option('--repository-type', required=True, help=u"""The repository's supported artifact type.""")
@cli_util.option('--is-immutable', required=True, type=click.BOOL, help=u"""Whether to make the repository immutable. The artifacts of an immutable repository cannot be overwritten.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the repository. If not present, will be auto-generated. It can be modified later. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the repository. It can be updated later.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'Repository'})
@cli_util.wrap_exceptions
def create_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, repository_type, is_immutable, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['repositoryType'] = repository_type
    _details['isImmutable'] = is_immutable

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.create_repository(
        create_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_repository') and callable(getattr(client, 'get_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.create_repository_create_generic_repository_details.command_name', 'create-repository-create-generic-repository-details'), help=u"""Creates a new repository for storing artifacts. \n[Command Reference](createRepository)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the repository's compartment.""")
@cli_util.option('--is-immutable', required=True, type=click.BOOL, help=u"""Whether to make the repository immutable. The artifacts of an immutable repository cannot be overwritten.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the repository. If not present, will be auto-generated. It can be modified later. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the repository. It can be updated later.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'Repository'})
@cli_util.wrap_exceptions
def create_repository_create_generic_repository_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, is_immutable, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['isImmutable'] = is_immutable

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['repositoryType'] = 'GENERIC'

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.create_repository(
        create_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_repository') and callable(getattr(client, 'get_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@container_image_group.command(name=cli_util.override('artifacts.delete_container_image.command_name', 'delete'), help=u"""Delete a container image. \n[Command Reference](deleteContainerImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.

Example: `ocid1.containerimage.oc1..exampleuniqueID`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_container_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_container_image(
        image_id=image_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_image') and callable(getattr(client, 'get_container_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_container_image(image_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@container_image_signature_group.command(name=cli_util.override('artifacts.delete_container_image_signature.command_name', 'delete'), help=u"""Delete a container image signature. \n[Command Reference](deleteContainerImageSignature)""")
@cli_util.option('--image-signature-id', required=True, help=u"""The [OCID] of the container image signature.

Example: `ocid1.containersignature.oc1..exampleuniqueID`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_container_image_signature(ctx, from_json, image_signature_id, if_match):

    if isinstance(image_signature_id, six.string_types) and len(image_signature_id.strip()) == 0:
        raise click.UsageError('Parameter --image-signature-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_container_image_signature(
        image_signature_id=image_signature_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_repository_group.command(name=cli_util.override('artifacts.delete_container_repository.command_name', 'delete'), help=u"""Delete container repository. \n[Command Reference](deleteContainerRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the container repository.

Example: `ocid1.containerrepo.oc1..exampleuniqueID`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_container_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_container_repository(
        repository_id=repository_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_repository') and callable(getattr(client, 'get_container_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_container_repository(repository_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.delete_generic_artifact.command_name', 'delete'), help=u"""Deletes an artifact with a specified [OCID]. \n[Command Reference](deleteGenericArtifact)""")
@cli_util.option('--artifact-id', required=True, help=u"""The [OCID] of the artifact.

Example: `ocid1.genericartifact.oc1..exampleuniqueID`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_generic_artifact(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, artifact_id, if_match):

    if isinstance(artifact_id, six.string_types) and len(artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --artifact-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_generic_artifact(
        artifact_id=artifact_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_generic_artifact') and callable(getattr(client, 'get_generic_artifact')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_generic_artifact(artifact_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.delete_generic_artifact_by_path.command_name', 'delete-generic-artifact-by-path'), help=u"""Deletes an artifact with a specified `artifactPath` and `version`. \n[Command Reference](deleteGenericArtifactByPath)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--artifact-path', required=True, help=u"""A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

Example: `project01/my-web-app/artifact-abc`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""A user-defined string to describe the artifact version.

Example: `1.1.2` or `1.2-beta-2`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_generic_artifact_by_path(ctx, from_json, repository_id, artifact_path, version_parameterconflict, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(artifact_path, six.string_types) and len(artifact_path.strip()) == 0:
        raise click.UsageError('Parameter --artifact-path cannot be whitespace or empty string')

    if isinstance(version_parameterconflict, six.string_types) and len(version_parameterconflict.strip()) == 0:
        raise click.UsageError('Parameter --version-parameterconflict cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_generic_artifact_by_path(
        repository_id=repository_id,
        artifact_path=artifact_path,
        version=version_parameterconflict,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.delete_repository.command_name', 'delete'), help=u"""Deletes the specified repository. This operation fails unless all associated artifacts are in a DELETED state. You must delete all associated artifacts before deleting a repository. \n[Command Reference](deleteRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.delete_repository(
        repository_id=repository_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_repository') and callable(getattr(client, 'get_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_repository(repository_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@container_configuration_group.command(name=cli_util.override('artifacts.get_container_configuration.command_name', 'get'), help=u"""Get container configuration. \n[Command Reference](getContainerConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerConfiguration'})
@cli_util.wrap_exceptions
def get_container_configuration(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_container_configuration(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_image_group.command(name=cli_util.override('artifacts.get_container_image.command_name', 'get'), help=u"""Get container image metadata. \n[Command Reference](getContainerImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.

Example: `ocid1.containerimage.oc1..exampleuniqueID`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImage'})
@cli_util.wrap_exceptions
def get_container_image(ctx, from_json, image_id):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_container_image(
        image_id=image_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_image_signature_group.command(name=cli_util.override('artifacts.get_container_image_signature.command_name', 'get'), help=u"""Get container image signature metadata. \n[Command Reference](getContainerImageSignature)""")
@cli_util.option('--image-signature-id', required=True, help=u"""The [OCID] of the container image signature.

Example: `ocid1.containersignature.oc1..exampleuniqueID`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImageSignature'})
@cli_util.wrap_exceptions
def get_container_image_signature(ctx, from_json, image_signature_id):

    if isinstance(image_signature_id, six.string_types) and len(image_signature_id.strip()) == 0:
        raise click.UsageError('Parameter --image-signature-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_container_image_signature(
        image_signature_id=image_signature_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_repository_group.command(name=cli_util.override('artifacts.get_container_repository.command_name', 'get'), help=u"""Get container repository. \n[Command Reference](getContainerRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the container repository.

Example: `ocid1.containerrepo.oc1..exampleuniqueID`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerRepository'})
@cli_util.wrap_exceptions
def get_container_repository(ctx, from_json, repository_id):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_container_repository(
        repository_id=repository_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.get_generic_artifact.command_name', 'get'), help=u"""Gets information about an artifact with a specified [OCID]. \n[Command Reference](getGenericArtifact)""")
@cli_util.option('--artifact-id', required=True, help=u"""The [OCID] of the artifact.

Example: `ocid1.genericartifact.oc1..exampleuniqueID`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def get_generic_artifact(ctx, from_json, artifact_id):

    if isinstance(artifact_id, six.string_types) and len(artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --artifact-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_generic_artifact(
        artifact_id=artifact_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.get_generic_artifact_by_path.command_name', 'get-generic-artifact-by-path'), help=u"""Gets information about an artifact with a specified `artifactPath` and `version`. \n[Command Reference](getGenericArtifactByPath)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--artifact-path', required=True, help=u"""A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

Example: `project01/my-web-app/artifact-abc`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""A user-defined string to describe the artifact version.

Example: `1.1.2` or `1.2-beta-2`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def get_generic_artifact_by_path(ctx, from_json, repository_id, artifact_path, version_parameterconflict):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(artifact_path, six.string_types) and len(artifact_path.strip()) == 0:
        raise click.UsageError('Parameter --artifact-path cannot be whitespace or empty string')

    if isinstance(version_parameterconflict, six.string_types) and len(version_parameterconflict.strip()) == 0:
        raise click.UsageError('Parameter --version-parameterconflict cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_generic_artifact_by_path(
        repository_id=repository_id,
        artifact_path=artifact_path,
        version=version_parameterconflict,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.get_repository.command_name', 'get'), help=u"""Gets the specified repository's information. \n[Command Reference](getRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'Repository'})
@cli_util.wrap_exceptions
def get_repository(ctx, from_json, repository_id):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.get_repository(
        repository_id=repository_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_image_signature_summary_group.command(name=cli_util.override('artifacts.list_container_image_signatures.command_name', 'list-container-image-signatures'), help=u"""List container image signatures in an image. \n[Command Reference](listContainerImageSignatures)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are inspected depending on the the setting of `accessLevel`. Default is false. Can only be set to true when calling the API on the tenancy (root compartment).""")
@cli_util.option('--image-id', help=u"""A filter to return a container image summary only for the specified container image OCID.""")
@cli_util.option('--repository-id', help=u"""A filter to return container images only for the specified container repository OCID.""")
@cli_util.option('--repository-name', help=u"""A filter to return container images or container image signatures that match the repository name.

Example: `foo` or `foo*`""")
@cli_util.option('--image-digest', help=u"""The digest of the container image.

Example: `sha256:e7d38b3517548a1c71e41bffe9c8ae6d6d29546ce46bf62159837aad072c90aa`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--kms-key-id', help=u"""The [OCID] of the kmsKeyVersionId used to sign the container image.

Example: `ocid1.keyversion.oc1..exampleuniqueID`""")
@cli_util.option('--kms-key-version-id', help=u"""The [OCID] of the kmsKeyVersionId used to sign the container image.

Example: `ocid1.keyversion.oc1..exampleuniqueID`""")
@cli_util.option('--signing-algorithm', type=custom_types.CliCaseInsensitiveChoice(["SHA_224_RSA_PKCS_PSS", "SHA_256_RSA_PKCS_PSS", "SHA_384_RSA_PKCS_PSS", "SHA_512_RSA_PKCS_PSS"]), help=u"""The algorithm to be used for signing. These are the only supported signing algorithms for container images.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImageSignatureCollection'})
@cli_util.wrap_exceptions
def list_container_image_signatures(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, image_id, repository_id, repository_name, image_digest, display_name, kms_key_id, kms_key_version_id, signing_algorithm, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if image_id is not None:
        kwargs['image_id'] = image_id
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if repository_name is not None:
        kwargs['repository_name'] = repository_name
    if image_digest is not None:
        kwargs['image_digest'] = image_digest
    if display_name is not None:
        kwargs['display_name'] = display_name
    if kms_key_id is not None:
        kwargs['kms_key_id'] = kms_key_id
    if kms_key_version_id is not None:
        kwargs['kms_key_version_id'] = kms_key_version_id
    if signing_algorithm is not None:
        kwargs['signing_algorithm'] = signing_algorithm
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_container_image_signatures,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_container_image_signatures,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_image_signatures(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@container_image_summary_group.command(name=cli_util.override('artifacts.list_container_images.command_name', 'list-container-images'), help=u"""List container images in a compartment. \n[Command Reference](listContainerImages)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are inspected depending on the the setting of `accessLevel`. Default is false. Can only be set to true when calling the API on the tenancy (root compartment).""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--image-id', help=u"""A filter to return a container image summary only for the specified container image OCID.""")
@cli_util.option('--is-versioned', type=click.BOOL, help=u"""A filter to return container images based on whether there are any associated versions.""")
@cli_util.option('--repository-id', help=u"""A filter to return container images only for the specified container repository OCID.""")
@cli_util.option('--repository-name', help=u"""A filter to return container images or container image signatures that match the repository name.

Example: `foo` or `foo*`""")
@cli_util.option('--version-parameterconflict', help=u"""A filter to return container images that match the version.

Example: `foo` or `foo*`""")
@cli_util.option('--lifecycle-state', help=u"""A filter to return only resources that match the given lifecycle state name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImageCollection'})
@cli_util.wrap_exceptions
def list_container_images(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, display_name, image_id, is_versioned, repository_id, repository_name, version_parameterconflict, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if display_name is not None:
        kwargs['display_name'] = display_name
    if image_id is not None:
        kwargs['image_id'] = image_id
    if is_versioned is not None:
        kwargs['is_versioned'] = is_versioned
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if repository_name is not None:
        kwargs['repository_name'] = repository_name
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_container_images,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_container_images,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_images(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@container_repository_group.command(name=cli_util.override('artifacts.list_container_repositories.command_name', 'list'), help=u"""List container repositories in a compartment. \n[Command Reference](listContainerRepositories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are inspected depending on the the setting of `accessLevel`. Default is false. Can only be set to true when calling the API on the tenancy (root compartment).""")
@cli_util.option('--repository-id', help=u"""A filter to return container images only for the specified container repository OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--is-public', type=click.BOOL, help=u"""A filter to return resources that match the isPublic value.""")
@cli_util.option('--lifecycle-state', help=u"""A filter to return only resources that match the given lifecycle state name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerRepositoryCollection'})
@cli_util.wrap_exceptions
def list_container_repositories(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, repository_id, display_name, is_public, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if is_public is not None:
        kwargs['is_public'] = is_public
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_container_repositories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_container_repositories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_container_repositories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.list_generic_artifacts.command_name', 'list'), help=u"""Lists artifacts in the specified repository. \n[Command Reference](listGenericArtifacts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--repository-id', required=True, help=u"""A filter to return the artifacts only for the specified repository OCID.""")
@cli_util.option('--id', help=u"""A filter to return the resources for the specified OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--artifact-path', help=u"""Filter results by a prefix for the `artifactPath` and and return artifacts that begin with the specified prefix in their path.""")
@cli_util.option('--version-parameterconflict', help=u"""Filter results by a prefix for `version` and return artifacts that that begin with the specified prefix in their version.""")
@cli_util.option('--sha256', help=u"""Filter results by a specified SHA256 digest for the artifact.""")
@cli_util.option('--lifecycle-state', help=u"""A filter to return only resources that match the given lifecycle state name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'GenericArtifactCollection'})
@cli_util.wrap_exceptions
def list_generic_artifacts(ctx, from_json, all_pages, page_size, compartment_id, repository_id, id, display_name, artifact_path, version_parameterconflict, sha256, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if artifact_path is not None:
        kwargs['artifact_path'] = artifact_path
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    if sha256 is not None:
        kwargs['sha256'] = sha256
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_generic_artifacts,
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_generic_artifacts,
            limit,
            page_size,
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_generic_artifacts(
            compartment_id=compartment_id,
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.list_repositories.command_name', 'list'), help=u"""Lists repositories in the specified compartment. \n[Command Reference](listRepositories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""A filter to return the resources for the specified OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--is-immutable', type=click.BOOL, help=u"""A filter to return resources that match the isImmutable value.""")
@cli_util.option('--lifecycle-state', help=u"""A filter to return only resources that match the given lifecycle state name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by availability domain if the scope of the resource type is within a single availability domain. If you call one of these \"List\" operations without specifying an availability domain, the resources are grouped by availability domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'RepositoryCollection'})
@cli_util.wrap_exceptions
def list_repositories(ctx, from_json, all_pages, page_size, compartment_id, id, display_name, is_immutable, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if is_immutable is not None:
        kwargs['is_immutable'] = is_immutable
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_repositories,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_repositories,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_repositories(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@container_image_group.command(name=cli_util.override('artifacts.remove_container_version.command_name', 'remove'), help=u"""Remove version from container image. \n[Command Reference](removeContainerVersion)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.

Example: `ocid1.containerimage.oc1..exampleuniqueID`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""The version to remove.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImage'})
@cli_util.wrap_exceptions
def remove_container_version(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, version_parameterconflict, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['version'] = version_parameterconflict

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.remove_container_version(
        image_id=image_id,
        remove_container_version_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_image') and callable(getattr(client, 'get_container_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_container_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@container_image_group.command(name=cli_util.override('artifacts.restore_container_image.command_name', 'restore'), help=u"""Restore a container image. \n[Command Reference](restoreContainerImage)""")
@cli_util.option('--image-id', required=True, help=u"""The [OCID] of the container image.

Example: `ocid1.containerimage.oc1..exampleuniqueID`""")
@cli_util.option('--version-parameterconflict', help=u"""Optional version to associate with image.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerImage'})
@cli_util.wrap_exceptions
def restore_container_image(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, image_id, version_parameterconflict, if_match):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.restore_container_image(
        image_id=image_id,
        restore_container_image_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_image') and callable(getattr(client, 'get_container_image')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_container_image(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@container_configuration_group.command(name=cli_util.override('artifacts.update_container_configuration.command_name', 'update'), help=u"""Update container configuration. \n[Command Reference](updateContainerConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--is-repository-created-on-first-push', type=click.BOOL, help=u"""Whether to create a new container repository when a container is pushed to a new repository path. Repositories created in this way belong to the root compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'artifacts', 'class': 'ContainerConfiguration'})
@cli_util.wrap_exceptions
def update_container_configuration(ctx, from_json, compartment_id, is_repository_created_on_first_push, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_repository_created_on_first_push is not None:
        _details['isRepositoryCreatedOnFirstPush'] = is_repository_created_on_first_push

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_container_configuration(
        compartment_id=compartment_id,
        update_container_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@container_repository_group.command(name=cli_util.override('artifacts.update_container_repository.command_name', 'update'), help=u"""Modify the properties of a container repository. Avoid entering confidential information. \n[Command Reference](updateContainerRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the container repository.

Example: `ocid1.containerrepo.oc1..exampleuniqueID`""")
@cli_util.option('--is-immutable', type=click.BOOL, help=u"""Whether the repository is immutable. Images cannot be overwritten in an immutable repository.""")
@cli_util.option('--is-public', type=click.BOOL, help=u"""Whether the repository is public. A public repository allows unauthenticated access.""")
@cli_util.option('--readme', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'readme': {'module': 'artifacts', 'class': 'ContainerRepositoryReadme'}}, output_type={'module': 'artifacts', 'class': 'ContainerRepository'})
@cli_util.wrap_exceptions
def update_container_repository(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, is_immutable, is_public, readme, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')
    if not force:
        if readme:
            if not click.confirm("WARNING: Updates to readme will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_immutable is not None:
        _details['isImmutable'] = is_immutable

    if is_public is not None:
        _details['isPublic'] = is_public

    if readme is not None:
        _details['readme'] = cli_util.parse_json_parameter("readme", readme)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_container_repository(
        repository_id=repository_id,
        update_container_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_container_repository') and callable(getattr(client, 'get_container_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_container_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.update_generic_artifact.command_name', 'update'), help=u"""Updates the artifact with the specified [OCID]. You can only update the tags of an artifact. \n[Command Reference](updateGenericArtifact)""")
@cli_util.option('--artifact-id', required=True, help=u"""The [OCID] of the artifact.

Example: `ocid1.genericartifact.oc1..exampleuniqueID`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def update_generic_artifact(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, artifact_id, freeform_tags, defined_tags, if_match):

    if isinstance(artifact_id, six.string_types) and len(artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --artifact-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_generic_artifact(
        artifact_id=artifact_id,
        update_generic_artifact_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_generic_artifact') and callable(getattr(client, 'get_generic_artifact')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_generic_artifact(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@generic_artifact_group.command(name=cli_util.override('artifacts.update_generic_artifact_by_path.command_name', 'update-generic-artifact-by-path'), help=u"""Updates an artifact with a specified `artifactPath` and `version`. You can only update the tags of an artifact. \n[Command Reference](updateGenericArtifactByPath)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--artifact-path', required=True, help=u"""A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

Example: `project01/my-web-app/artifact-abc`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""A user-defined string to describe the artifact version.

Example: `1.1.2` or `1.2-beta-2`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def update_generic_artifact_by_path(ctx, from_json, force, repository_id, artifact_path, version_parameterconflict, freeform_tags, defined_tags, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(artifact_path, six.string_types) and len(artifact_path.strip()) == 0:
        raise click.UsageError('Parameter --artifact-path cannot be whitespace or empty string')

    if isinstance(version_parameterconflict, six.string_types) and len(version_parameterconflict.strip()) == 0:
        raise click.UsageError('Parameter --version-parameterconflict cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_generic_artifact_by_path(
        repository_id=repository_id,
        artifact_path=artifact_path,
        version=version_parameterconflict,
        update_generic_artifact_by_path_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.update_repository.command_name', 'update'), help=u"""Updates the properties of a repository. You can update the `displayName` and  `description` properties. \n[Command Reference](updateRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--repository-type', required=True, help=u"""The repository's supported artifact type.""")
@cli_util.option('--display-name', help=u"""The repository name.""")
@cli_util.option('--description', help=u"""The repository description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'Repository'})
@cli_util.wrap_exceptions
def update_repository(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, repository_type, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['repositoryType'] = repository_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_repository(
        repository_id=repository_id,
        update_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_repository') and callable(getattr(client, 'get_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('artifacts.update_repository_update_generic_repository_details.command_name', 'update-repository-update-generic-repository-details'), help=u"""Updates the properties of a repository. You can update the `displayName` and  `description` properties. \n[Command Reference](updateRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.artifactrepository.oc1..exampleuniqueID`""")
@cli_util.option('--display-name', help=u"""The repository name.""")
@cli_util.option('--description', help=u"""The repository description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["AVAILABLE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'artifacts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'artifacts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'artifacts', 'class': 'Repository'})
@cli_util.wrap_exceptions
def update_repository_update_generic_repository_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['repositoryType'] = 'GENERIC'

    client = cli_util.build_client('artifacts', 'artifacts', ctx)
    result = client.update_repository(
        repository_id=repository_id,
        update_repository_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_repository') and callable(getattr(client, 'get_repository')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_repository(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
