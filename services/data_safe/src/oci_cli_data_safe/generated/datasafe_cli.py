# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('data_safe.data_safe_root_group.command_name', 'data-safe'), cls=CommandGroupWithAlias, help=cli_util.override('data_safe.data_safe_root_group.help', """APIs for using Oracle Data Safe."""), short_help=cli_util.override('data_safe.data_safe_root_group.short_help', """Data Safe API"""))
@cli_util.help_option_group
def data_safe_root_group():
    pass


@click.command(cli_util.override('data_safe.data_safe_private_endpoint_group.command_name', 'data-safe-private-endpoint'), cls=CommandGroupWithAlias, help="""A Data Safe private endpoint that allows Data Safe to connect to databases in a customer's virtual cloud network (VCN).""")
@cli_util.help_option_group
def data_safe_private_endpoint_group():
    pass


@click.command(cli_util.override('data_safe.data_safe_configuration_group.command_name', 'data-safe-configuration'), cls=CommandGroupWithAlias, help="""A Data Safe Configuration that allows customer to enable Data Safe in their tenancy.""")
@cli_util.help_option_group
def data_safe_configuration_group():
    pass


@click.command(cli_util.override('data_safe.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('data_safe.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('data_safe.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_safe.enable_data_safe_configuration_details_group.command_name', 'enable-data-safe-configuration-details'), cls=CommandGroupWithAlias, help="""The information needed to enable Data Safe in the tenancy.""")
@cli_util.help_option_group
def enable_data_safe_configuration_details_group():
    pass


data_safe_root_group.add_command(data_safe_private_endpoint_group)
data_safe_root_group.add_command(data_safe_configuration_group)
data_safe_root_group.add_command(work_request_error_group)
data_safe_root_group.add_command(work_request_log_entry_group)
data_safe_root_group.add_command(work_request_group)
data_safe_root_group.add_command(enable_data_safe_configuration_details_group)


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.change_data_safe_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves the Data Safe private endpoint and its dependent resources to the specified compartment. \n[Command Reference](changeDataSafePrivateEndpointCompartment)""")
@cli_util.option('--data-safe-private-endpoint-id', required=True, help=u"""The OCID of the private endpoint.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the new compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_data_safe_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, data_safe_private_endpoint_id, compartment_id, if_match):

    if isinstance(data_safe_private_endpoint_id, six.string_types) and len(data_safe_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --data-safe-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.change_data_safe_private_endpoint_compartment(
        data_safe_private_endpoint_id=data_safe_private_endpoint_id,
        change_data_safe_private_endpoint_compartment_details=_details,
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


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.create_data_safe_private_endpoint.command_name', 'create'), help=u"""Creates a new Data Safe private endpoint. \n[Command Reference](createDataSafePrivateEndpoint)""")
@cli_util.option('--display-name', required=True, help=u"""The display name for the private endpoint. The name does not have to be unique, and it's changeable.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the VCN.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet.""")
@cli_util.option('--private-endpoint-ip', help=u"""The private IP address of the private endpoint.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the network security groups that the private endpoint belongs to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_data_safe_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, vcn_id, subnet_id, private_endpoint_ip, description, nsg_ids, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id
    _details['subnetId'] = subnet_id

    if private_endpoint_ip is not None:
        _details['privateEndpointIp'] = private_endpoint_ip

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_data_safe_private_endpoint(
        create_data_safe_private_endpoint_details=_details,
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


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.delete_data_safe_private_endpoint.command_name', 'delete'), help=u"""Deletes the specified Data Safe private endpoint. \n[Command Reference](deleteDataSafePrivateEndpoint)""")
@cli_util.option('--data-safe-private-endpoint-id', required=True, help=u"""The OCID of the private endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_safe_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, data_safe_private_endpoint_id, if_match):

    if isinstance(data_safe_private_endpoint_id, six.string_types) and len(data_safe_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --data-safe-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.delete_data_safe_private_endpoint(
        data_safe_private_endpoint_id=data_safe_private_endpoint_id,
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
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@enable_data_safe_configuration_details_group.command(name=cli_util.override('data_safe.enable_data_safe_configuration.command_name', 'enable-data-safe-configuration'), help=u"""Enables Data Safe in the tenancy and region. \n[Command Reference](enableDataSafeConfiguration)""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Indicates if Data Safe is enabled.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def enable_data_safe_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, is_enabled, freeform_tags, defined_tags, compartment_id, if_match):
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.enable_data_safe_configuration(
        enable_data_safe_configuration_details=_details,
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


@data_safe_configuration_group.command(name=cli_util.override('data_safe.get_data_safe_configuration.command_name', 'get'), help=u"""Gets the details of the Data Safe configuration. \n[Command Reference](getDataSafeConfiguration)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the specified compartment OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'DataSafeConfiguration'})
@cli_util.wrap_exceptions
def get_data_safe_configuration(ctx, from_json, compartment_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.get_data_safe_configuration(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.get_data_safe_private_endpoint.command_name', 'get'), help=u"""Gets the details of the specified Data Safe private endpoint. \n[Command Reference](getDataSafePrivateEndpoint)""")
@cli_util.option('--data-safe-private-endpoint-id', required=True, help=u"""The OCID of the private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'DataSafePrivateEndpoint'})
@cli_util.wrap_exceptions
def get_data_safe_private_endpoint(ctx, from_json, data_safe_private_endpoint_id):

    if isinstance(data_safe_private_endpoint_id, six.string_types) and len(data_safe_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --data-safe-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.get_data_safe_private_endpoint(
        data_safe_private_endpoint_id=data_safe_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_safe.get_work_request.command_name', 'get'), help=u"""Gets the details of the specified work request. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.list_data_safe_private_endpoints.command_name', 'list'), help=u"""Gets a list of Data Safe private endpoints. \n[Command Reference](listDataSafePrivateEndpoints)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the specified display name.""")
@cli_util.option('--vcn-id', help=u"""A filter to return only the private endpoints that match the specified VCN OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA"]), help=u"""A filter to return only resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""The beginning page from which the results start retrieving.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can specify only one sort order (sortOrder). The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[DataSafePrivateEndpointSummary]'})
@cli_util.wrap_exceptions
def list_data_safe_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, display_name, vcn_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_safe_private_endpoints,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_safe_private_endpoints,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_data_safe_private_endpoints(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('data_safe.list_work_request_errors.command_name', 'list'), help=u"""Gets a list of errors for the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The beginning page from which the results start retrieving.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[WorkRequestError]'})
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('data_safe.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Gets a list of log entries for the specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The beginning page from which the results start retrieving.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[WorkRequestLogEntry]'})
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
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


@work_request_group.command(name=cli_util.override('data_safe.list_work_requests.command_name', 'list'), help=u"""Gets a list of work requests. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--resource-id', help=u"""A filter to return only work requests that match the specified resource OCID.""")
@cli_util.option('--page', help=u"""The beginning page from which the results start retrieving.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.update_data_safe_private_endpoint.command_name', 'update'), help=u"""Updates one or more attributes of the specified Data Safe private endpoint. \n[Command Reference](updateDataSafePrivateEndpoint)""")
@cli_util.option('--data-safe-private-endpoint-id', required=True, help=u"""The OCID of the private endpoint.""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the private endpoint.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the network security groups that the private endpoint belongs to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_data_safe_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_safe_private_endpoint_id, display_name, description, nsg_ids, freeform_tags, defined_tags, if_match):

    if isinstance(data_safe_private_endpoint_id, six.string_types) and len(data_safe_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --data-safe-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if nsg_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to nsg-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_data_safe_private_endpoint(
        data_safe_private_endpoint_id=data_safe_private_endpoint_id,
        update_data_safe_private_endpoint_details=_details,
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
