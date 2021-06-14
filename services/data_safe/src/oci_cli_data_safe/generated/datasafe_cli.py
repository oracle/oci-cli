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


@cli.command(cli_util.override('data_safe.data_safe_root_group.command_name', 'data-safe'), cls=CommandGroupWithAlias, help=cli_util.override('data_safe.data_safe_root_group.help', """APIs for using Oracle Data Safe."""), short_help=cli_util.override('data_safe.data_safe_root_group.short_help', """Data Safe API"""))
@cli_util.help_option_group
def data_safe_root_group():
    pass


@click.command(cli_util.override('data_safe.data_safe_private_endpoint_group.command_name', 'data-safe-private-endpoint'), cls=CommandGroupWithAlias, help="""A Data Safe private endpoint that allows Data Safe to connect to databases in a customer's virtual cloud network (VCN).""")
@cli_util.help_option_group
def data_safe_private_endpoint_group():
    pass


@click.command(cli_util.override('data_safe.target_database_group.command_name', 'target-database'), cls=CommandGroupWithAlias, help="""The details of the Data Safe target database.""")
@cli_util.help_option_group
def target_database_group():
    pass


@click.command(cli_util.override('data_safe.data_safe_configuration_group.command_name', 'data-safe-configuration'), cls=CommandGroupWithAlias, help="""A Data Safe configuration for a tenancy and region.""")
@cli_util.help_option_group
def data_safe_configuration_group():
    pass


@click.command(cli_util.override('data_safe.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error related to a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('data_safe.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log entry related to a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('data_safe.on_prem_connector_group.command_name', 'on-prem-connector'), cls=CommandGroupWithAlias, help="""A Data Safe on-premises connector that enables Data Safe to connect to on-premises databases.""")
@cli_util.help_option_group
def on_prem_connector_group():
    pass


@click.command(cli_util.override('data_safe.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


data_safe_root_group.add_command(data_safe_private_endpoint_group)
data_safe_root_group.add_command(target_database_group)
data_safe_root_group.add_command(data_safe_configuration_group)
data_safe_root_group.add_command(work_request_error_group)
data_safe_root_group.add_command(work_request_log_entry_group)
data_safe_root_group.add_command(on_prem_connector_group)
data_safe_root_group.add_command(work_request_group)


@target_database_group.command(name=cli_util.override('data_safe.activate_target_database.command_name', 'activate'), help=u"""Reactivates a previously deactivated Data Safe target database. \n[Command Reference](activateTargetDatabase)""")
@cli_util.option('--credentials', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}})
@cli_util.wrap_exceptions
def activate_target_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, credentials, target_database_id, if_match):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.activate_target_database(
        target_database_id=target_database_id,
        activate_target_database_details=_details,
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.change_on_prem_connector_compartment.command_name', 'change-compartment'), help=u"""Moves the specified on-premises connector into a different compartment. \n[Command Reference](changeOnPremConnectorCompartment)""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the new compartment where you want to move the on-premises connector.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_on_prem_connector_compartment(ctx, from_json, on_prem_connector_id, compartment_id, if_match):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.change_on_prem_connector_compartment(
        on_prem_connector_id=on_prem_connector_id,
        change_on_prem_connector_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_database_group.command(name=cli_util.override('data_safe.change_target_database_compartment.command_name', 'change-compartment'), help=u"""Moves the Data Safe target database to the specified compartment. \n[Command Reference](changeTargetDatabaseCompartment)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the new compartment to where you want to move the Data Safe target database.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_target_database_compartment(ctx, from_json, target_database_id, compartment_id, if_match):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.change_target_database_compartment(
        target_database_id=target_database_id,
        change_target_database_compartment_details=_details,
        **kwargs
    )
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

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'data_safe', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'DataSafePrivateEndpoint'})
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.create_on_prem_connector.command_name', 'create'), help=u"""Creates a new on-premises connector. \n[Command Reference](createOnPremConnector)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to create the on-premises connector.""")
@cli_util.option('--display-name', help=u"""The display name of the on-premises connector. The name does not have to be unique, and it's changeable.""")
@cli_util.option('--description', help=u"""The description of the on-premises connector.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'OnPremConnector'})
@cli_util.wrap_exceptions
def create_on_prem_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_on_prem_connector(
        create_on_prem_connector_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database.command_name', 'create'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database_installed_database_details.command_name', 'create-target-database-installed-database-details'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-details-instance-id', help=u"""The OCID of the compute instance on which the database is running.""")
@cli_util.option('--database-details-ip-addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A List of either the IP Addresses or FQDN names of the database hosts.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-details-listener-port', type=click.INT, help=u"""The port number of the database listener.""")
@cli_util.option('--database-details-service-name', help=u"""The service name of the database registered as target database.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}, 'database-details-ip-addresses': {'module': 'data_safe', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}, 'database-details-ip-addresses': {'module': 'data_safe', 'class': 'list[string]'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database_installed_database_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, database_details_instance_id, database_details_ip_addresses, database_details_listener_port, database_details_service_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_instance_id is not None:
        _details['databaseDetails']['instanceId'] = database_details_instance_id

    if database_details_ip_addresses is not None:
        _details['databaseDetails']['ipAddresses'] = cli_util.parse_json_parameter("database_details_ip_addresses", database_details_ip_addresses)

    if database_details_listener_port is not None:
        _details['databaseDetails']['listenerPort'] = database_details_listener_port

    if database_details_service_name is not None:
        _details['databaseDetails']['serviceName'] = database_details_service_name

    _details['databaseDetails']['databaseType'] = 'INSTALLED_DATABASE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database_autonomous_database_details.command_name', 'create-target-database-autonomous-database-details'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-details-autonomous-database-id', help=u"""The OCID of the autonomous database registered as a target database in Data Safe.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database_autonomous_database_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, database_details_autonomous_database_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_autonomous_database_id is not None:
        _details['databaseDetails']['autonomousDatabaseId'] = database_details_autonomous_database_id

    _details['databaseDetails']['databaseType'] = 'AUTONOMOUS_DATABASE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database_database_cloud_service_details.command_name', 'create-target-database-database-cloud-service-details'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-details-vm-cluster-id', help=u"""The OCID of the VM cluster in which the database is running.""")
@cli_util.option('--database-details-db-system-id', help=u"""The OCID of the cloud database system registered as a target database in Data Safe.""")
@cli_util.option('--database-details-service-name', help=u"""The database service name.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database_database_cloud_service_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, database_details_vm_cluster_id, database_details_db_system_id, database_details_service_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_vm_cluster_id is not None:
        _details['databaseDetails']['vmClusterId'] = database_details_vm_cluster_id

    if database_details_db_system_id is not None:
        _details['databaseDetails']['dbSystemId'] = database_details_db_system_id

    if database_details_service_name is not None:
        _details['databaseDetails']['serviceName'] = database_details_service_name

    _details['databaseDetails']['databaseType'] = 'DATABASE_CLOUD_SERVICE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database_private_endpoint.command_name', 'create-target-database-private-endpoint'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option-datasafe-private-endpoint-id', help=u"""The OCID of the Data Safe private endpoint.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details, display_name, description, credentials, tls_config, freeform_tags, defined_tags, connection_option_datasafe_private_endpoint_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionOption'] = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if connection_option_datasafe_private_endpoint_id is not None:
        _details['connectionOption']['datasafePrivateEndpointId'] = connection_option_datasafe_private_endpoint_id

    _details['connectionOption']['connectionType'] = 'PRIVATE_ENDPOINT'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.create_target_database_on_premise_connector.command_name', 'create-target-database-on-premise-connector'), help=u"""Registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console. \n[Command Reference](createTargetDatabase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the Data Safe target database.""")
@cli_util.option('--database-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option-on-prem-connector-id', help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def create_target_database_on_premise_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_details, display_name, description, credentials, tls_config, freeform_tags, defined_tags, connection_option_on_prem_connector_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionOption'] = {}
    _details['compartmentId'] = compartment_id
    _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if connection_option_on_prem_connector_id is not None:
        _details['connectionOption']['onPremConnectorId'] = connection_option_on_prem_connector_id

    _details['connectionOption']['connectionType'] = 'ONPREM_CONNECTOR'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.create_target_database(
        create_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.deactivate_target_database.command_name', 'deactivate'), help=u"""Deactivates a target database in Data Safe. \n[Command Reference](deactivateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def deactivate_target_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, if_match):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.deactivate_target_database(
        target_database_id=target_database_id,
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.delete_on_prem_connector.command_name', 'delete'), help=u"""Deletes the specified on-premises connector. \n[Command Reference](deleteOnPremConnector)""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
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
def delete_on_prem_connector(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, on_prem_connector_id, if_match):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.delete_on_prem_connector(
        on_prem_connector_id=on_prem_connector_id,
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


@target_database_group.command(name=cli_util.override('data_safe.delete_target_database.command_name', 'delete'), help=u"""Deregisters the specified database from Data Safe and removes the target database from the Data Safe Console. \n[Command Reference](deleteTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
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
def delete_target_database(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, if_match):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.delete_target_database(
        target_database_id=target_database_id,
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


@target_database_group.command(name=cli_util.override('data_safe.download_privilege_script.command_name', 'download-privilege-script'), help=u"""Downloads the privilege script to grant/revoke required roles from the Data Safe account on the target database. \n[Command Reference](downloadPrivilegeScript)""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def download_privilege_script(ctx, from_json, file, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.download_privilege_script(
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


@data_safe_configuration_group.command(name=cli_util.override('data_safe.enable_data_safe_configuration.command_name', 'enable'), help=u"""Enables Data Safe in the tenancy and region. \n[Command Reference](enableDataSafeConfiguration)""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Indicates if Data Safe is enabled.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_data_safe_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, is_enabled, compartment_id, if_match):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled

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


@on_prem_connector_group.command(name=cli_util.override('data_safe.generate_on_prem_connector_configuration.command_name', 'generate-on-prem-connector-configuration'), help=u"""Creates and downloads the configuration of the specified on-premises connector. \n[Command Reference](generateOnPremConnectorConfiguration)""")
@cli_util.option('--password', required=True, help=u"""The password to encrypt the keys inside the wallet included as part of the configuration. The password must be between 12 and 30 characters long and must contain atleast 1 uppercase, 1 lowercase, 1 numeric, and 1 special character.""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_on_prem_connector_configuration(ctx, from_json, file, password, on_prem_connector_id, if_match):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['password'] = password

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.generate_on_prem_connector_configuration(
        on_prem_connector_id=on_prem_connector_id,
        generate_on_prem_connector_configuration_details=_details,
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.get_on_prem_connector.command_name', 'get'), help=u"""Gets the details of the specified on-premises connector. \n[Command Reference](getOnPremConnector)""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'OnPremConnector'})
@cli_util.wrap_exceptions
def get_on_prem_connector(ctx, from_json, on_prem_connector_id):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.get_on_prem_connector(
        on_prem_connector_id=on_prem_connector_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_database_group.command(name=cli_util.override('data_safe.get_target_database.command_name', 'get'), help=u"""Returns the details of the specified Data Safe target database. \n[Command Reference](getTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'TargetDatabase'})
@cli_util.wrap_exceptions
def get_target_database(ctx, from_json, target_database_id):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.get_target_database(
        target_database_id=target_database_id,
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
@cli_util.option('--compartment-id', required=True, help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the specified display name.""")
@cli_util.option('--vcn-id', help=u"""A filter to return only resources that match the specified VCN OCID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NA"]), help=u"""A filter to return only resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[DataSafePrivateEndpointSummary]'})
@cli_util.wrap_exceptions
def list_data_safe_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, display_name, vcn_id, lifecycle_state, limit, page, sort_order, sort_by, compartment_id_in_subtree, access_level):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
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
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_safe_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_safe_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_data_safe_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@on_prem_connector_group.command(name=cli_util.override('data_safe.list_on_prem_connectors.command_name', 'list'), help=u"""Gets a list of on-premises connectors. \n[Command Reference](listOnPremConnectors)""")
@cli_util.option('--compartment-id', required=True, help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--on-prem-connector-id', help=u"""A filter to return only the on-premises connector that matches the specified id.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the specified display name.""")
@cli_util.option('--on-prem-connector-lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only on-premises connector resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[OnPremConnectorSummary]'})
@cli_util.wrap_exceptions
def list_on_prem_connectors(ctx, from_json, all_pages, page_size, compartment_id, on_prem_connector_id, display_name, on_prem_connector_lifecycle_state, limit, page, sort_order, sort_by, compartment_id_in_subtree, access_level):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if on_prem_connector_id is not None:
        kwargs['on_prem_connector_id'] = on_prem_connector_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if on_prem_connector_lifecycle_state is not None:
        kwargs['on_prem_connector_lifecycle_state'] = on_prem_connector_lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_on_prem_connectors,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_on_prem_connectors,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_on_prem_connectors(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_database_group.command(name=cli_util.override('data_safe.list_target_databases.command_name', 'list'), help=u"""Returns the list of registered target databases in Data Safe. \n[Command Reference](listTargetDatabases)""")
@cli_util.option('--compartment-id', required=True, help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--target-database-id', help=u"""A filter to return the target database that matches the specified OCID.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the specified display name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]), help=u"""A filter to return the target databases that matches the current state of the target database.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"]), help=u"""A filter to return target databases that match the database type of the target database.""")
@cli_util.option('--infrastructure-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""A filter to return target databases that match the infrastructure type of the target database.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the 'accessLevel' setting.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED. Setting this to ACCESSIBLE returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field used for sorting. Only one sorting order (sortOrder) can be specified. The default order for TIMECREATED is descending. The default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[TargetDatabaseSummary]'})
@cli_util.wrap_exceptions
def list_target_databases(ctx, from_json, all_pages, page_size, compartment_id, target_database_id, display_name, lifecycle_state, database_type, infrastructure_type, limit, page, compartment_id_in_subtree, access_level, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if target_database_id is not None:
        kwargs['target_database_id'] = target_database_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if database_type is not None:
        kwargs['database_type'] = database_type
    if infrastructure_type is not None:
        kwargs['infrastructure_type'] = infrastructure_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
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
            client.list_target_databases,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_target_databases,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_target_databases(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('data_safe.list_work_request_errors.command_name', 'list'), help=u"""Gets a list of errors for the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
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
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
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
@cli_util.option('--compartment-id', required=True, help=u"""A filter to return only resources that match the specified compartment OCID.""")
@cli_util.option('--operation-type', help=u"""A filter to return only work requests that match the specific operation type.""")
@cli_util.option('--resource-id', help=u"""A filter to return only work requests that match the specified resource OCID.""")
@cli_util.option('--page', help=u"""For list pagination. The page token representing the page at which to start retrieving results. It is usually retrieved from a previous \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return per page in a paginated \"List\" call. For details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_safe', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, operation_type, resource_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if operation_type is not None:
        kwargs['operation_type'] = operation_type
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


@data_safe_private_endpoint_group.command(name=cli_util.override('data_safe.update_data_safe_private_endpoint.command_name', 'update'), help=u"""Updates one or more attributes of the specified Data Safe private endpoint. \n[Command Reference](updateDataSafePrivateEndpoint)""")
@cli_util.option('--data-safe-private-endpoint-id', required=True, help=u"""The OCID of the private endpoint.""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the private endpoint.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the network security groups that the private endpoint belongs to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.update_on_prem_connector.command_name', 'update'), help=u"""Updates one or more attributes of the specified on-premises connector. \n[Command Reference](updateOnPremConnector)""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--display-name', help=u"""The display name of the on-premises connector. The name does not have to be unique, and it's changeable.""")
@cli_util.option('--description', help=u"""The description of the on-premises connector.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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
def update_on_prem_connector(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, on_prem_connector_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_on_prem_connector(
        on_prem_connector_id=on_prem_connector_id,
        update_on_prem_connector_details=_details,
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


@on_prem_connector_group.command(name=cli_util.override('data_safe.update_on_prem_connector_wallet.command_name', 'update-on-prem-connector-wallet'), help=u"""Updates the wallet for the specified on-premises connector to a new version. \n[Command Reference](updateOnPremConnectorWallet)""")
@cli_util.option('--on-prem-connector-id', required=True, help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--is-update', type=click.BOOL, help=u"""Indicates whether to update or not. If false, the wallet will not be updated. Default is false.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_on_prem_connector_wallet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, on_prem_connector_id, is_update, if_match):

    if isinstance(on_prem_connector_id, six.string_types) and len(on_prem_connector_id.strip()) == 0:
        raise click.UsageError('Parameter --on-prem-connector-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_update is not None:
        _details['isUpdate'] = is_update

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_on_prem_connector_wallet(
        on_prem_connector_id=on_prem_connector_id,
        update_on_prem_connector_wallet_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database.command_name', 'update'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--database-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_target_database(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, display_name, description, database_details, credentials, tls_config, connection_option, freeform_tags, defined_tags, if_match):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if database_details or credentials or tls_config or connection_option or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to database-details and credentials and tls-config and connection-option and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if database_details is not None:
        _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database_installed_database_details.command_name', 'update-target-database-installed-database-details'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--database-details-instance-id', help=u"""The OCID of the compute instance on which the database is running.""")
@cli_util.option('--database-details-ip-addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A List of either the IP Addresses or FQDN names of the database hosts.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-details-listener-port', type=click.INT, help=u"""The port number of the database listener.""")
@cli_util.option('--database-details-service-name', help=u"""The service name of the database registered as target database.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}, 'database-details-ip-addresses': {'module': 'data_safe', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}, 'database-details-ip-addresses': {'module': 'data_safe', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_target_database_installed_database_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, if_match, database_details_instance_id, database_details_ip_addresses, database_details_listener_port, database_details_service_name):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if credentials or tls_config or connection_option or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to credentials and tls-config and connection-option and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_instance_id is not None:
        _details['databaseDetails']['instanceId'] = database_details_instance_id

    if database_details_ip_addresses is not None:
        _details['databaseDetails']['ipAddresses'] = cli_util.parse_json_parameter("database_details_ip_addresses", database_details_ip_addresses)

    if database_details_listener_port is not None:
        _details['databaseDetails']['listenerPort'] = database_details_listener_port

    if database_details_service_name is not None:
        _details['databaseDetails']['serviceName'] = database_details_service_name

    _details['databaseDetails']['databaseType'] = 'INSTALLED_DATABASE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database_autonomous_database_details.command_name', 'update-target-database-autonomous-database-details'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--database-details-autonomous-database-id', help=u"""The OCID of the autonomous database registered as a target database in Data Safe.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_target_database_autonomous_database_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, if_match, database_details_autonomous_database_id):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if credentials or tls_config or connection_option or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to credentials and tls-config and connection-option and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_autonomous_database_id is not None:
        _details['databaseDetails']['autonomousDatabaseId'] = database_details_autonomous_database_id

    _details['databaseDetails']['databaseType'] = 'AUTONOMOUS_DATABASE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database_database_cloud_service_details.command_name', 'update-target-database-database-cloud-service-details'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--database-details-infrastructure-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"]), help=u"""The infrastructure type the database is running on.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-option', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--database-details-vm-cluster-id', help=u"""The OCID of the VM cluster in which the database is running.""")
@cli_util.option('--database-details-db-system-id', help=u"""The OCID of the cloud database system registered as a target database in Data Safe.""")
@cli_util.option('--database-details-service-name', help=u"""The database service name.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'connection-option': {'module': 'data_safe', 'class': 'ConnectionOption'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_target_database_database_cloud_service_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, database_details_infrastructure_type, display_name, description, credentials, tls_config, connection_option, freeform_tags, defined_tags, if_match, database_details_vm_cluster_id, database_details_db_system_id, database_details_service_name):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if credentials or tls_config or connection_option or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to credentials and tls-config and connection-option and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['databaseDetails'] = {}
    _details['databaseDetails']['infrastructureType'] = database_details_infrastructure_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if connection_option is not None:
        _details['connectionOption'] = cli_util.parse_json_parameter("connection_option", connection_option)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if database_details_vm_cluster_id is not None:
        _details['databaseDetails']['vmClusterId'] = database_details_vm_cluster_id

    if database_details_db_system_id is not None:
        _details['databaseDetails']['dbSystemId'] = database_details_db_system_id

    if database_details_service_name is not None:
        _details['databaseDetails']['serviceName'] = database_details_service_name

    _details['databaseDetails']['databaseType'] = 'DATABASE_CLOUD_SERVICE'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database_private_endpoint.command_name', 'update-target-database-private-endpoint'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--database-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--connection-option-datasafe-private-endpoint-id', help=u"""The OCID of the Data Safe private endpoint.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_target_database_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, display_name, description, database_details, credentials, tls_config, freeform_tags, defined_tags, if_match, connection_option_datasafe_private_endpoint_id):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if database_details or credentials or tls_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to database-details and credentials and tls-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionOption'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if database_details is not None:
        _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if connection_option_datasafe_private_endpoint_id is not None:
        _details['connectionOption']['datasafePrivateEndpointId'] = connection_option_datasafe_private_endpoint_id

    _details['connectionOption']['connectionType'] = 'PRIVATE_ENDPOINT'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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


@target_database_group.command(name=cli_util.override('data_safe.update_target_database_on_premise_connector.command_name', 'update-target-database-on-premise-connector'), help=u"""Updates one or more attributes of the specified Data Safe target database. \n[Command Reference](updateTargetDatabase)""")
@cli_util.option('--target-database-id', required=True, help=u"""The OCID of the Data Safe target database.""")
@cli_util.option('--display-name', help=u"""The display name of the target database in Data Safe.""")
@cli_util.option('--description', help=u"""The description of the target database in Data Safe.""")
@cli_util.option('--database-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credentials', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--tls-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--connection-option-on-prem-connector-id', help=u"""The OCID of the on-premises connector.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-details': {'module': 'data_safe', 'class': 'DatabaseDetails'}, 'credentials': {'module': 'data_safe', 'class': 'Credentials'}, 'tls-config': {'module': 'data_safe', 'class': 'TlsConfig'}, 'freeform-tags': {'module': 'data_safe', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_safe', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_target_database_on_premise_connector(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_database_id, display_name, description, database_details, credentials, tls_config, freeform_tags, defined_tags, if_match, connection_option_on_prem_connector_id):

    if isinstance(target_database_id, six.string_types) and len(target_database_id.strip()) == 0:
        raise click.UsageError('Parameter --target-database-id cannot be whitespace or empty string')
    if not force:
        if database_details or credentials or tls_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to database-details and credentials and tls-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionOption'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if database_details is not None:
        _details['databaseDetails'] = cli_util.parse_json_parameter("database_details", database_details)

    if credentials is not None:
        _details['credentials'] = cli_util.parse_json_parameter("credentials", credentials)

    if tls_config is not None:
        _details['tlsConfig'] = cli_util.parse_json_parameter("tls_config", tls_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if connection_option_on_prem_connector_id is not None:
        _details['connectionOption']['onPremConnectorId'] = connection_option_on_prem_connector_id

    _details['connectionOption']['connectionType'] = 'ONPREM_CONNECTOR'

    client = cli_util.build_client('data_safe', 'data_safe', ctx)
    result = client.update_target_database(
        target_database_id=target_database_id,
        update_target_database_details=_details,
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
