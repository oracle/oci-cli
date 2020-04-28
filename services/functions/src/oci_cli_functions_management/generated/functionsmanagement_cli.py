# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.functions.src.oci_cli_functions.generated import fn_service_cli


@click.command(cli_util.override('functions_management.functions_management_root_group.command_name', 'functions-management'), cls=CommandGroupWithAlias, help=cli_util.override('functions_management.functions_management_root_group.help', """API for the Functions service."""), short_help=cli_util.override('functions_management.functions_management_root_group.short_help', """Functions Service API"""))
@cli_util.help_option_group
def functions_management_root_group():
    pass


@click.command(cli_util.override('functions_management.application_group.command_name', 'application'), cls=CommandGroupWithAlias, help="""An application contains functions and defined attributes shared between those functions, such as network configuration and configuration. Avoid entering confidential information.""")
@cli_util.help_option_group
def application_group():
    pass


@click.command(cli_util.override('functions_management.function_group.command_name', 'function'), cls=CommandGroupWithAlias, help="""A function resource defines the code (Docker image) and configuration for a specific function. Functions are defined in applications. Avoid entering confidential information.""")
@cli_util.help_option_group
def function_group():
    pass


fn_service_cli.fn_service_group.add_command(functions_management_root_group)
functions_management_root_group.add_command(application_group)
functions_management_root_group.add_command(function_group)


@application_group.command(name=cli_util.override('functions_management.change_application_compartment.command_name', 'change-compartment'), help=u"""Moves an application into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources Between Compartments].""")
@cli_util.option('--application-id', required=True, help=u"""The [OCID] of this application.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_application_compartment(ctx, from_json, application_id, compartment_id, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.change_application_compartment(
        application_id=application_id,
        change_application_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('functions_management.create_application.command_name', 'create'), help=u"""Creates a new application.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to create the application within.""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the application. The display name must be unique within the compartment containing the application. Avoid entering confidential information.""")
@cli_util.option('--subnet-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCID]s of the subnets in which to run functions in the application.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Application configuration. These values are passed on to the function as environment variables, functions may override application configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'subnet-ids': {'module': 'functions', 'class': 'list[string]'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'subnet-ids': {'module': 'functions', 'class': 'list[string]'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Application'})
@cli_util.wrap_exceptions
def create_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, subnet_ids, config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['subnetIds'] = cli_util.parse_json_parameter("subnet_ids", subnet_ids)

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.create_application(
        create_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_application(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@function_group.command(name=cli_util.override('functions_management.create_function.command_name', 'create'), help=u"""Creates a new function.""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the function. The display name must be unique within the application containing the function. Avoid entering confidential information.""")
@cli_util.option('--application-id', required=True, help=u"""The OCID of the application this function belongs to.""")
@cli_util.option('--image', required=True, help=u"""The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. Example: `phx.ocir.io/ten/functions/function:0.0.1`""")
@cli_util.option('--memory-in-mbs', required=True, type=click.INT, help=u"""Maximum usable memory for the function (MiB).""")
@cli_util.option('--image-digest', help=u"""The image digest for the version of the image that will be pulled when invoking this function. If no value is specified, the digest currently associated with the image in the OCI Registry will be used. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`""")
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout for executions of the function. Value in seconds.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def create_function(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, application_id, image, memory_in_mbs, image_digest, config, timeout_in_seconds, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['applicationId'] = application_id
    _details['image'] = image
    _details['memoryInMBs'] = memory_in_mbs

    if image_digest is not None:
        _details['imageDigest'] = image_digest

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.create_function(
        create_function_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_function') and callable(getattr(client, 'get_function')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_function(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@application_group.command(name=cli_util.override('functions_management.delete_application.command_name', 'delete'), help=u"""Deletes an application.""")
@cli_util.option('--application-id', required=True, help=u"""The [OCID] of this application.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, application_id, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.delete_application(
        application_id=application_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_application(application_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@function_group.command(name=cli_util.override('functions_management.delete_function.command_name', 'delete'), help=u"""Deletes a function.""")
@cli_util.option('--function-id', required=True, help=u"""The [OCID] of this function.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_function(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, function_id, if_match):

    if isinstance(function_id, six.string_types) and len(function_id.strip()) == 0:
        raise click.UsageError('Parameter --function-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.delete_function(
        function_id=function_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_function') and callable(getattr(client, 'get_function')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_function(function_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@application_group.command(name=cli_util.override('functions_management.get_application.command_name', 'get'), help=u"""Retrieves an application.""")
@cli_util.option('--application-id', required=True, help=u"""The [OCID] of this application.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'functions', 'class': 'Application'})
@cli_util.wrap_exceptions
def get_application(ctx, from_json, application_id):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.get_application(
        application_id=application_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@function_group.command(name=cli_util.override('functions_management.get_function.command_name', 'get'), help=u"""Retrieves a function.""")
@cli_util.option('--function-id', required=True, help=u"""The [OCID] of this function.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def get_function(ctx, from_json, function_id):

    if isinstance(function_id, six.string_types) and len(function_id.strip()) == 0:
        raise click.UsageError('Parameter --function-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.get_function(
        function_id=function_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('functions_management.list_applications.command_name', 'list'), help=u"""Lists applications for a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which this resource belongs.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. 1 is the minimum, 50 is the maximum.

Default: 10""")
@cli_util.option('--page', help=u"""The pagination token for a list query returned by a previous operation""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only applications that match the lifecycle state in this parameter. Example: `Creating`""")
@cli_util.option('--display-name', help=u"""A filter to return only applications with display names that match the display name string. Matching is exact.""")
@cli_util.option('--id', help=u"""A filter to return only applications with the specfied OCID.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order.

* **ASC:** Ascending sort order. * **DESC:** Descending sort order.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "id", "displayName"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `displayName`

* **timeCreated:** Sorts by timeCreated. * **displayName:** Sorts by displayName. * **id:** Sorts by id.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'functions', 'class': 'list[ApplicationSummary]'})
@cli_util.wrap_exceptions
def list_applications(ctx, from_json, all_pages, page_size, compartment_id, limit, page, lifecycle_state, display_name, id, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_applications,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_applications,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_applications(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@function_group.command(name=cli_util.override('functions_management.list_functions.command_name', 'list'), help=u"""Lists functions for an application.""")
@cli_util.option('--application-id', required=True, help=u"""The [OCID] of the application to which this function belongs.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. 1 is the minimum, 50 is the maximum.

Default: 10""")
@cli_util.option('--page', help=u"""The pagination token for a list query returned by a previous operation""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only functions that match the lifecycle state in this parameter. Example: `Creating`""")
@cli_util.option('--display-name', help=u"""A filter to return only functions with display names that match the display name string. Matching is exact.""")
@cli_util.option('--id', help=u"""A filter to return only functions with the specified OCID.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order.

* **ASC:** Ascending sort order. * **DESC:** Descending sort order.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "id", "displayName"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `displayName`

* **timeCreated:** Sorts by timeCreated. * **displayName:** Sorts by displayName. * **id:** Sorts by id.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'functions', 'class': 'list[FunctionSummary]'})
@cli_util.wrap_exceptions
def list_functions(ctx, from_json, all_pages, page_size, application_id, limit, page, lifecycle_state, display_name, id, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('functions', 'functions_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_functions,
            application_id=application_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_functions,
            limit,
            page_size,
            application_id=application_id,
            **kwargs
        )
    else:
        result = client.list_functions(
            application_id=application_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('functions_management.update_application.command_name', 'update'), help=u"""Modifies an application""")
@cli_util.option('--application-id', required=True, help=u"""The [OCID] of this application.""")
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Application configuration. These values are passed on to the function as environment variables, functions may override application configuration. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Application'})
@cli_util.wrap_exceptions
def update_application(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, application_id, config, freeform_tags, defined_tags, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')
    if not force:
        if config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.update_application(
        application_id=application_id,
        update_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_application(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@function_group.command(name=cli_util.override('functions_management.update_function.command_name', 'update'), help=u"""Modifies a function""")
@cli_util.option('--function-id', required=True, help=u"""The [OCID] of this function.""")
@cli_util.option('--image', help=u"""The qualified name of the Docker image to use in the function, including the image tag. The image should be in the OCI Registry that is in the same region as the function itself. If an image is specified but no value for imageDigest is provided, the digest currently associated with the image tag in the OCI Registry will be used. Example: `phx.ocir.io/ten/functions/function:0.0.1`""")
@cli_util.option('--image-digest', help=u"""The image digest for the version of the image that will be pulled when invoking this function. Example: `sha256:ca0eeb6fb05351dfc8759c20733c91def84cb8007aa89a5bf606bc8b315b9fc7`""")
@cli_util.option('--memory-in-mbs', type=click.INT, help=u"""Maximum usable memory for the function (MiB).""")
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Function configuration. These values are passed on to the function as environment variables, this overrides application configuration values. Keys must be ASCII strings consisting solely of letters, digits, and the '_' (underscore) character, and must not begin with a digit. Values should be limited to printable unicode characters.

Example: `{\"MY_FUNCTION_CONFIG\": \"ConfVal\"}`

The maximum size for all configuration keys and values is limited to 4KB. This is measured as the sum of octets necessary to represent each key and value in UTF-8.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout for executions of the function. Value in seconds.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config': {'module': 'functions', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'functions', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'functions', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'functions', 'class': 'Function'})
@cli_util.wrap_exceptions
def update_function(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, function_id, image, image_digest, memory_in_mbs, config, timeout_in_seconds, freeform_tags, defined_tags, if_match):

    if isinstance(function_id, six.string_types) and len(function_id.strip()) == 0:
        raise click.UsageError('Parameter --function-id cannot be whitespace or empty string')
    if not force:
        if config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if image is not None:
        _details['image'] = image

    if image_digest is not None:
        _details['imageDigest'] = image_digest

    if memory_in_mbs is not None:
        _details['memoryInMBs'] = memory_in_mbs

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('functions', 'functions_management', ctx)
    result = client.update_function(
        function_id=function_id,
        update_function_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_function') and callable(getattr(client, 'get_function')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_function(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
