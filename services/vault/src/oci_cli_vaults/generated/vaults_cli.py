# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('vault.vault_root_group.command_name', 'vault'), cls=CommandGroupWithAlias, help=cli_util.override('vault.vault_root_group.help', """API for managing secrets."""), short_help=cli_util.override('vault.vault_root_group.short_help', """Secrets Management API"""))
@cli_util.help_option_group
def vault_root_group():
    pass


@click.command(cli_util.override('vault.secret_version_group.command_name', 'secret-version'), cls=CommandGroupWithAlias, help="""The details of the secret version, excluding the contents of the secret.""")
@cli_util.help_option_group
def secret_version_group():
    pass


@click.command(cli_util.override('vault.secret_group.command_name', 'secret'), cls=CommandGroupWithAlias, help="""The details of the secret. Secret details do not contain the contents of the secret itself.""")
@cli_util.help_option_group
def secret_group():
    pass


vault_root_group.add_command(secret_version_group)
vault_root_group.add_command(secret_group)


@secret_group.command(name=cli_util.override('vault.cancel_secret_deletion.command_name', 'cancel-secret-deletion'), help=u"""Cancels the pending deletion of the specified secret. Canceling a scheduled deletion restores the secret's lifecycle state to what it was before you scheduled the secret for deletion. \n[Command Reference](cancelSecretDeletion)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_secret_deletion(ctx, from_json, secret_id, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.cancel_secret_deletion(
        secret_id=secret_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_version_group.command(name=cli_util.override('vault.cancel_secret_version_deletion.command_name', 'cancel-secret-version-deletion'), help=u"""Cancels the scheduled deletion of a secret version. \n[Command Reference](cancelSecretVersionDeletion)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--secret-version-number', required=True, type=click.INT, help=u"""The version number of the secret.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_secret_version_deletion(ctx, from_json, secret_id, secret_version_number, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    if isinstance(secret_version_number, six.string_types) and len(secret_version_number.strip()) == 0:
        raise click.UsageError('Parameter --secret-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.cancel_secret_version_deletion(
        secret_id=secret_id,
        secret_version_number=secret_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_group.command(name=cli_util.override('vault.change_secret_compartment.command_name', 'change-compartment'), help=u"""Moves a secret into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When provided, if-match is checked against the ETag values of the secret. \n[Command Reference](changeSecretCompartment)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_secret_compartment(ctx, from_json, secret_id, compartment_id, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.change_secret_compartment(
        secret_id=secret_id,
        change_secret_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_group.command(name=cli_util.override('vault.create_secret.command_name', 'create'), help=u"""Creates a new secret according to the details of the request.

This operation is not supported by the Oracle Cloud Infrastructure Terraform Provider. \n[Command Reference](createSecret)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the secret.""")
@cli_util.option('--secret-content', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-name', required=True, help=u"""A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault where you want to create the secret.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the secret. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-id', help=u"""The OCID of the master encryption key that is used to encrypt the secret.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata that you can use to provide context about how to use the secret during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules to control how the secret is used and managed.

This option is a JSON list with items of type SecretRule.  For documentation on SecretRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/vaults/20180608/datatypes/SecretRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-content': {'module': 'vault', 'class': 'SecretContentDetails'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-content': {'module': 'vault', 'class': 'SecretContentDetails'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def create_secret(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, secret_content, secret_name, vault_id, defined_tags, description, freeform_tags, key_id, metadata, secret_rules):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['secretContent'] = cli_util.parse_json_parameter("secret_content", secret_content)
    _details['secretName'] = secret_name
    _details['vaultId'] = vault_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if key_id is not None:
        _details['keyId'] = key_id

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if secret_rules is not None:
        _details['secretRules'] = cli_util.parse_json_parameter("secret_rules", secret_rules)

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.create_secret(
        create_secret_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_secret') and callable(getattr(client, 'get_secret')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_secret(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@secret_group.command(name=cli_util.override('vault.create_secret_base64_secret_content_details.command_name', 'create-secret-base64-secret-content-details'), help=u"""Creates a new secret according to the details of the request.

This operation is not supported by the Oracle Cloud Infrastructure Terraform Provider. \n[Command Reference](createSecret)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the secret.""")
@cli_util.option('--secret-name', required=True, help=u"""A user-friendly name for the secret. Secret names should be unique within a vault. Avoid entering confidential information. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--vault-id', required=True, help=u"""The OCID of the vault where you want to create the secret.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the secret. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-id', help=u"""The OCID of the master encryption key that is used to encrypt the secret.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata that you can use to provide context about how to use the secret during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules to control how the secret is used and managed.

This option is a JSON list with items of type SecretRule.  For documentation on SecretRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/vaults/20180608/datatypes/SecretRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-content-name', help=u"""Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--secret-content-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system. When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.""")
@cli_util.option('--secret-content-content', help=u"""The base64-encoded content of the secret.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def create_secret_base64_secret_content_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, secret_name, vault_id, defined_tags, description, freeform_tags, key_id, metadata, secret_rules, secret_content_name, secret_content_stage, secret_content_content):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['secretContent'] = {}
    _details['compartmentId'] = compartment_id
    _details['secretName'] = secret_name
    _details['vaultId'] = vault_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if key_id is not None:
        _details['keyId'] = key_id

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if secret_rules is not None:
        _details['secretRules'] = cli_util.parse_json_parameter("secret_rules", secret_rules)

    if secret_content_name is not None:
        _details['secretContent']['name'] = secret_content_name

    if secret_content_stage is not None:
        _details['secretContent']['stage'] = secret_content_stage

    if secret_content_content is not None:
        _details['secretContent']['content'] = secret_content_content

    _details['secretContent']['contentType'] = 'BASE64'

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.create_secret(
        create_secret_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_secret') and callable(getattr(client, 'get_secret')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_secret(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@secret_group.command(name=cli_util.override('vault.get_secret.command_name', 'get'), help=u"""Gets information about the specified secret. \n[Command Reference](getSecret)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def get_secret(ctx, from_json, secret_id):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.get_secret(
        secret_id=secret_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_version_group.command(name=cli_util.override('vault.get_secret_version.command_name', 'get'), help=u"""Gets information about the specified version of a secret. \n[Command Reference](getSecretVersion)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--secret-version-number', required=True, type=click.INT, help=u"""The version number of the secret.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vault', 'class': 'SecretVersion'})
@cli_util.wrap_exceptions
def get_secret_version(ctx, from_json, secret_id, secret_version_number):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    if isinstance(secret_version_number, six.string_types) and len(secret_version_number.strip()) == 0:
        raise click.UsageError('Parameter --secret-version-number cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.get_secret_version(
        secret_id=secret_id,
        secret_version_number=secret_version_number,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_version_group.command(name=cli_util.override('vault.list_secret_versions.command_name', 'list'), help=u"""Lists all secret versions for the specified secret. \n[Command Reference](listSecretVersions)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. Only one sort order may be provided. Time created is default ordered as descending. Display name is default ordered as ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vault', 'class': 'list[SecretVersionSummary]'})
@cli_util.wrap_exceptions
def list_secret_versions(ctx, from_json, all_pages, page_size, secret_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_secret_versions,
            secret_id=secret_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_secret_versions,
            limit,
            page_size,
            secret_id=secret_id,
            **kwargs
        )
    else:
        result = client.list_secret_versions(
            secret_id=secret_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@secret_group.command(name=cli_util.override('vault.list_secrets.command_name', 'list'), help=u"""Lists all secrets in the specified vault and compartment. \n[Command Reference](listSecrets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--name', help=u"""The secret name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `TIMECREATED` is descending. The default order for `NAME` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--vault-id', help=u"""The OCID of the vault.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), help=u"""A filter that returns only resources that match the specified lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vault', 'class': 'list[SecretSummary]'})
@cli_util.wrap_exceptions
def list_secrets(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_by, sort_order, vault_id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if vault_id is not None:
        kwargs['vault_id'] = vault_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('vault', 'vaults', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_secrets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_secrets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_secrets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@secret_group.command(name=cli_util.override('vault.schedule_secret_deletion.command_name', 'schedule-secret-deletion'), help=u"""Schedules the deletion of the specified secret. This sets the lifecycle state of the secret to `PENDING_DELETION` and then deletes it after the specified retention period ends. \n[Command Reference](scheduleSecretDeletion)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the secret version, expressed in [RFC 3339] timestamp format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_secret_deletion(ctx, from_json, secret_id, time_of_deletion, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.schedule_secret_deletion(
        secret_id=secret_id,
        schedule_secret_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_version_group.command(name=cli_util.override('vault.schedule_secret_version_deletion.command_name', 'schedule-secret-version-deletion'), help=u"""Schedules the deletion of the specified secret version. This deletes it after the specified retention period ends. You can only delete a secret version if the secret version rotation state is marked as `DEPRECATED`. \n[Command Reference](scheduleSecretVersionDeletion)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--secret-version-number', required=True, type=click.INT, help=u"""The version number of the secret.""")
@cli_util.option('--time-of-deletion', type=custom_types.CLI_DATETIME, help=u"""An optional property indicating when to delete the secret version, expressed in [RFC 3339] timestamp format. Example: `2019-04-03T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def schedule_secret_version_deletion(ctx, from_json, secret_id, secret_version_number, time_of_deletion, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    if isinstance(secret_version_number, six.string_types) and len(secret_version_number.strip()) == 0:
        raise click.UsageError('Parameter --secret-version-number cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if time_of_deletion is not None:
        _details['timeOfDeletion'] = time_of_deletion

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.schedule_secret_version_deletion(
        secret_id=secret_id,
        secret_version_number=secret_version_number,
        schedule_secret_version_deletion_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_group.command(name=cli_util.override('vault.update_secret.command_name', 'update'), help=u"""Updates the properties of a secret. Specifically, you can update the version number of the secret to make that version number the current version. You can also update a secret's description, its free-form or defined tags, rules and the secret contents. Updating the secret content automatically creates a new secret version. You cannot, however, update the current secret version number and the secret contents and the rules at the same time. Furthermore, the secret must in an `ACTIVE` lifecycle state to be updated.

This operation is not supported by the Oracle Cloud Infrastructure Terraform Provider. \n[Command Reference](updateSecret)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Details to update the secret version of the specified secret. The secret contents, version number, and rules can't be specified at the same time. Updating the secret contents automatically creates a new secret version.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the secret. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata that you can use to provide context about how to use the secret or during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-content', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules to control how the secret is used and managed.

This option is a JSON list with items of type SecretRule.  For documentation on SecretRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/vaults/20180608/datatypes/SecretRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-content': {'module': 'vault', 'class': 'SecretContentDetails'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-content': {'module': 'vault', 'class': 'SecretContentDetails'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def update_secret(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, secret_id, current_version_number, defined_tags, description, freeform_tags, metadata, secret_content, secret_rules, if_match):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or metadata or secret_content or secret_rules:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and metadata and secret-content and secret-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if secret_content is not None:
        _details['secretContent'] = cli_util.parse_json_parameter("secret_content", secret_content)

    if secret_rules is not None:
        _details['secretRules'] = cli_util.parse_json_parameter("secret_rules", secret_rules)

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.update_secret(
        secret_id=secret_id,
        update_secret_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_secret') and callable(getattr(client, 'get_secret')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_secret(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@secret_group.command(name=cli_util.override('vault.update_secret_base64_secret_content_details.command_name', 'update-secret-base64-secret-content-details'), help=u"""Updates the properties of a secret. Specifically, you can update the version number of the secret to make that version number the current version. You can also update a secret's description, its free-form or defined tags, rules and the secret contents. Updating the secret content automatically creates a new secret version. You cannot, however, update the current secret version number and the secret contents and the rules at the same time. Furthermore, the secret must in an `ACTIVE` lifecycle state to be updated.

This operation is not supported by the Oracle Cloud Infrastructure Terraform Provider. \n[Command Reference](updateSecret)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--current-version-number', type=click.INT, help=u"""Details to update the secret version of the specified secret. The secret contents, version number, and rules can't be specified at the same time. Updating the secret contents automatically creates a new secret version.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A brief description of the secret. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional metadata that you can use to provide context about how to use the secret or during rotation or other administrative tasks. For example, for a secret that you use to connect to a database, the additional metadata might specify the connection endpoint and the connection string. Provide additional metadata as key-value pairs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--secret-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of rules to control how the secret is used and managed.

This option is a JSON list with items of type SecretRule.  For documentation on SecretRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/vaults/20180608/datatypes/SecretRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--secret-content-name', help=u"""Names should be unique within a secret. Valid characters are uppercase or lowercase letters, numbers, hyphens, underscores, and periods.""")
@cli_util.option('--secret-content-stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING"]), help=u"""The rotation state of the secret content. The default is `CURRENT`, meaning that the secret is currently in use. A secret version that you mark as `PENDING` is staged and available for use, but you don't yet want to rotate it into current, active use. For example, you might create or update a secret and mark its rotation state as `PENDING` if you haven't yet updated the secret on the target system. When creating a secret, only the value `CURRENT` is applicable, although the value `LATEST` is also automatically applied. When updating a secret, you can specify a version's rotation state as either `CURRENT` or `PENDING`.""")
@cli_util.option('--secret-content-content', help=u"""The base64-encoded content of the secret.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "SCHEDULING_DELETION", "PENDING_DELETION", "CANCELLING_DELETION", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'vault', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'vault', 'class': 'dict(str, string)'}, 'metadata': {'module': 'vault', 'class': 'dict(str, object)'}, 'secret-rules': {'module': 'vault', 'class': 'list[SecretRule]'}}, output_type={'module': 'vault', 'class': 'Secret'})
@cli_util.wrap_exceptions
def update_secret_base64_secret_content_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, secret_id, current_version_number, defined_tags, description, freeform_tags, metadata, secret_rules, if_match, secret_content_name, secret_content_stage, secret_content_content):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or metadata or secret_rules:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and metadata and secret-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['secretContent'] = {}

    if current_version_number is not None:
        _details['currentVersionNumber'] = current_version_number

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if secret_rules is not None:
        _details['secretRules'] = cli_util.parse_json_parameter("secret_rules", secret_rules)

    if secret_content_name is not None:
        _details['secretContent']['name'] = secret_content_name

    if secret_content_stage is not None:
        _details['secretContent']['stage'] = secret_content_stage

    if secret_content_content is not None:
        _details['secretContent']['content'] = secret_content_content

    _details['secretContent']['contentType'] = 'BASE64'

    client = cli_util.build_client('vault', 'vaults', ctx)
    result = client.update_secret(
        secret_id=secret_id,
        update_secret_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_secret') and callable(getattr(client, 'get_secret')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_secret(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
