# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('ccc.ccc_root_group.command_name', 'ccc'), cls=CommandGroupWithAlias, help=cli_util.override('ccc.ccc_root_group.help', """Compute Cloud at Customer API"""), short_help=cli_util.override('ccc.ccc_root_group.short_help', """Compute Cloud at Customer Control Plane API"""))
@cli_util.help_option_group
def ccc_root_group():
    pass


@click.command(cli_util.override('ccc.ccc_upgrade_schedule_group.command_name', 'ccc-upgrade-schedule'), cls=CommandGroupWithAlias, help="""Defines a schedule for preferred update times.""")
@cli_util.help_option_group
def ccc_upgrade_schedule_group():
    pass


@click.command(cli_util.override('ccc.ccc_infrastructure_group.command_name', 'ccc-infrastructure'), cls=CommandGroupWithAlias, help="""A CCC Infrastructure.""")
@cli_util.help_option_group
def ccc_infrastructure_group():
    pass


@click.command(cli_util.override('ccc.ccc_upgrade_schedule_collection_group.command_name', 'ccc-upgrade-schedule-collection'), cls=CommandGroupWithAlias, help="""Results of a CCC Upgrade Schedule search. Contains the summary items and other information, such as metadata.""")
@cli_util.help_option_group
def ccc_upgrade_schedule_collection_group():
    pass


@click.command(cli_util.override('ccc.ccc_infrastructure_collection_group.command_name', 'ccc-infrastructure-collection'), cls=CommandGroupWithAlias, help="""Results of a CCC Infrastructure search. Contains the summary items and other information, such as metadata.""")
@cli_util.help_option_group
def ccc_infrastructure_collection_group():
    pass


ccc_root_group.add_command(ccc_upgrade_schedule_group)
ccc_root_group.add_command(ccc_infrastructure_group)
ccc_root_group.add_command(ccc_upgrade_schedule_collection_group)
ccc_root_group.add_command(ccc_infrastructure_collection_group)


@ccc_infrastructure_group.command(name=cli_util.override('ccc.change_ccc_infrastructure_compartment.command_name', 'change-compartment'), help=u"""Moves a CccInfrastructure resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeCccInfrastructureCompartment)""")
@cli_util.option('--ccc-infrastructure-id', required=True, help=u"""Identifier for a single CCC Infrastructure""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ccc_infrastructure_compartment(ctx, from_json, ccc_infrastructure_id, compartment_id, if_match):

    if isinstance(ccc_infrastructure_id, six.string_types) and len(ccc_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.change_ccc_infrastructure_compartment(
        ccc_infrastructure_id=ccc_infrastructure_id,
        change_ccc_infrastructure_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ccc_upgrade_schedule_group.command(name=cli_util.override('ccc.change_ccc_upgrade_schedule_compartment.command_name', 'change-compartment'), help=u"""Moves a CCC Upgrade Schedule resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeCccUpgradeScheduleCompartment)""")
@cli_util.option('--ccc-upgrade-schedule-id', required=True, help=u"""Unique CccUpgradeSchedule identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_ccc_upgrade_schedule_compartment(ctx, from_json, ccc_upgrade_schedule_id, compartment_id, if_match):

    if isinstance(ccc_upgrade_schedule_id, six.string_types) and len(ccc_upgrade_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-upgrade-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.change_ccc_upgrade_schedule_compartment(
        ccc_upgrade_schedule_id=ccc_upgrade_schedule_id,
        change_ccc_upgrade_schedule_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ccc_infrastructure_group.command(name=cli_util.override('ccc.create_ccc_infrastructure.command_name', 'create'), help=u"""Creates and provisions a new CccInfrastructure. \n[Command Reference](createCccInfrastructure)""")
@cli_util.option('--display-name', required=True, help=u"""CCC Infrastructure display name""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier where CCC Service resides""")
@cli_util.option('--subnet-id', required=True, help=u"""Identifier for network subnet that will be used to communicate with CCC Infrastructure""")
@cli_util.option('--connection-state', help=u"""The current connection state of the CCC Infrastructure resource.""")
@cli_util.option('--connection-details', help=u"""A message describing the current connection state in more detail.""")
@cli_util.option('--upgrade-schedule-id', help=u"""Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccInfrastructure'})
@cli_util.wrap_exceptions
def create_ccc_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, subnet_id, connection_state, connection_details, upgrade_schedule_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['subnetId'] = subnet_id

    if connection_state is not None:
        _details['connectionState'] = connection_state

    if connection_details is not None:
        _details['connectionDetails'] = connection_details

    if upgrade_schedule_id is not None:
        _details['upgradeScheduleId'] = upgrade_schedule_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.create_ccc_infrastructure(
        create_ccc_infrastructure_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_infrastructure') and callable(getattr(client, 'get_ccc_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ccc_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@ccc_upgrade_schedule_group.command(name=cli_util.override('ccc.create_ccc_upgrade_schedule.command_name', 'create'), help=u"""Creates a new CCC Upgrade Schedule. \n[Command Reference](createCccUpgradeSchedule)""")
@cli_util.option('--display-name', required=True, help=u"""CCC Upgrade Schedule display name""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier where CCC Upgrade Schedule resides""")
@cli_util.option('--events', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of preferred times for a CCC Infrastructure to be upgraded.

This option is a JSON list with items of type CreateCccScheduleEvent.  For documentation on CreateCccScheduleEvent please see our API reference: https://docs.cloud.oracle.com/api/#/en/computecloudatcustomer/20221208/datatypes/CreateCccScheduleEvent.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'events': {'module': 'compute_cloud_at_customer', 'class': 'list[CreateCccScheduleEvent]'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'events': {'module': 'compute_cloud_at_customer', 'class': 'list[CreateCccScheduleEvent]'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccUpgradeSchedule'})
@cli_util.wrap_exceptions
def create_ccc_upgrade_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, events, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if events is not None:
        _details['events'] = cli_util.parse_json_parameter("events", events)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.create_ccc_upgrade_schedule(
        create_ccc_upgrade_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_upgrade_schedule') and callable(getattr(client, 'get_ccc_upgrade_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ccc_upgrade_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@ccc_infrastructure_group.command(name=cli_util.override('ccc.delete_ccc_infrastructure.command_name', 'delete'), help=u"""Deletes a CccInfrastructure resource by identifier \n[Command Reference](deleteCccInfrastructure)""")
@cli_util.option('--ccc-infrastructure-id', required=True, help=u"""Identifier for a single CCC Infrastructure""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ccc_infrastructure(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ccc_infrastructure_id, if_match):

    if isinstance(ccc_infrastructure_id, six.string_types) and len(ccc_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.delete_ccc_infrastructure(
        ccc_infrastructure_id=ccc_infrastructure_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_infrastructure') and callable(getattr(client, 'get_ccc_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_ccc_infrastructure(ccc_infrastructure_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@ccc_upgrade_schedule_group.command(name=cli_util.override('ccc.delete_ccc_upgrade_schedule.command_name', 'delete'), help=u"""Deletes a CCC Upgrade Schedule resource by identifier \n[Command Reference](deleteCccUpgradeSchedule)""")
@cli_util.option('--ccc-upgrade-schedule-id', required=True, help=u"""Unique CccUpgradeSchedule identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_ccc_upgrade_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, ccc_upgrade_schedule_id, if_match):

    if isinstance(ccc_upgrade_schedule_id, six.string_types) and len(ccc_upgrade_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-upgrade-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.delete_ccc_upgrade_schedule(
        ccc_upgrade_schedule_id=ccc_upgrade_schedule_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_upgrade_schedule') and callable(getattr(client, 'get_ccc_upgrade_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_ccc_upgrade_schedule(ccc_upgrade_schedule_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@ccc_infrastructure_group.command(name=cli_util.override('ccc.get_ccc_infrastructure.command_name', 'get'), help=u"""Gets a CccInfrastructure by identifier \n[Command Reference](getCccInfrastructure)""")
@cli_util.option('--ccc-infrastructure-id', required=True, help=u"""Identifier for a single CCC Infrastructure""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccInfrastructure'})
@cli_util.wrap_exceptions
def get_ccc_infrastructure(ctx, from_json, ccc_infrastructure_id):

    if isinstance(ccc_infrastructure_id, six.string_types) and len(ccc_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-infrastructure-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.get_ccc_infrastructure(
        ccc_infrastructure_id=ccc_infrastructure_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ccc_upgrade_schedule_group.command(name=cli_util.override('ccc.get_ccc_upgrade_schedule.command_name', 'get'), help=u"""Gets a CCC Upgrade Schedule by identifier \n[Command Reference](getCccUpgradeSchedule)""")
@cli_util.option('--ccc-upgrade-schedule-id', required=True, help=u"""Unique CccUpgradeSchedule identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccUpgradeSchedule'})
@cli_util.wrap_exceptions
def get_ccc_upgrade_schedule(ctx, from_json, ccc_upgrade_schedule_id):

    if isinstance(ccc_upgrade_schedule_id, six.string_types) and len(ccc_upgrade_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-upgrade-schedule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.get_ccc_upgrade_schedule(
        ccc_upgrade_schedule_id=ccc_upgrade_schedule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ccc_infrastructure_collection_group.command(name=cli_util.override('ccc.list_ccc_infrastructures.command_name', 'list-ccc-infrastructures'), help=u"""Returns a list of CCC Infrastructures. \n[Command Reference](listCccInfrastructures)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Identifier for a single CCC Infrastructure""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccInfrastructureCollection'})
@cli_util.wrap_exceptions
def list_ccc_infrastructures(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ccc_infrastructures,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ccc_infrastructures,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_ccc_infrastructures(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ccc_upgrade_schedule_collection_group.command(name=cli_util.override('ccc.list_ccc_upgrade_schedules.command_name', 'list-ccc-upgrade-schedules'), help=u"""Returns a list of CCC Upgrade Schedules. \n[Command Reference](listCccUpgradeSchedules)""")
@cli_util.option('--id', help=u"""Unique CccUpgradeSchedule identifier""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccUpgradeScheduleCollection'})
@cli_util.wrap_exceptions
def list_ccc_upgrade_schedules(ctx, from_json, all_pages, page_size, id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_ccc_upgrade_schedules,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_ccc_upgrade_schedules,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_ccc_upgrade_schedules(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@ccc_infrastructure_group.command(name=cli_util.override('ccc.update_ccc_infrastructure.command_name', 'update'), help=u"""Updates the CccInfrastructure \n[Command Reference](updateCccInfrastructure)""")
@cli_util.option('--ccc-infrastructure-id', required=True, help=u"""Identifier for a single CCC Infrastructure""")
@cli_util.option('--display-name', help=u"""CCC Infrastructure display name""")
@cli_util.option('--subnet-id', help=u"""Identifier for network subnet that will be used to communicate with CCC Infrastructure""")
@cli_util.option('--connection-state', help=u"""The current connection state of the CCC Infrastructure resource.""")
@cli_util.option('--connection-details', help=u"""A message describing the current connection state in more detail.""")
@cli_util.option('--upgrade-schedule-id', help=u"""Schedule used for upgrades. If no schedule is associated with the infrastructure, it can be updated at any time.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccInfrastructure'})
@cli_util.wrap_exceptions
def update_ccc_infrastructure(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ccc_infrastructure_id, display_name, subnet_id, connection_state, connection_details, upgrade_schedule_id, freeform_tags, defined_tags, if_match):

    if isinstance(ccc_infrastructure_id, six.string_types) and len(ccc_infrastructure_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-infrastructure-id cannot be whitespace or empty string')
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

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if connection_state is not None:
        _details['connectionState'] = connection_state

    if connection_details is not None:
        _details['connectionDetails'] = connection_details

    if upgrade_schedule_id is not None:
        _details['upgradeScheduleId'] = upgrade_schedule_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.update_ccc_infrastructure(
        ccc_infrastructure_id=ccc_infrastructure_id,
        update_ccc_infrastructure_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_infrastructure') and callable(getattr(client, 'get_ccc_infrastructure')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ccc_infrastructure(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@ccc_upgrade_schedule_group.command(name=cli_util.override('ccc.update_ccc_upgrade_schedule.command_name', 'update'), help=u"""Updates the CCC Upgrade Schedule \n[Command Reference](updateCccUpgradeSchedule)""")
@cli_util.option('--ccc-upgrade-schedule-id', required=True, help=u"""Unique CccUpgradeSchedule identifier""")
@cli_util.option('--display-name', help=u"""CCC Upgrade Schedule display name""")
@cli_util.option('--events', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of preferred times for a CCC Infrastructure to be upgraded.

This option is a JSON list with items of type UpdateCccScheduleEvent.  For documentation on UpdateCccScheduleEvent please see our API reference: https://docs.cloud.oracle.com/api/#/en/computecloudatcustomer/20221208/datatypes/UpdateCccScheduleEvent.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "NEEDS_ATTENTION", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'events': {'module': 'compute_cloud_at_customer', 'class': 'list[UpdateCccScheduleEvent]'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'events': {'module': 'compute_cloud_at_customer', 'class': 'list[UpdateCccScheduleEvent]'}, 'freeform-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'compute_cloud_at_customer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'compute_cloud_at_customer', 'class': 'CccUpgradeSchedule'})
@cli_util.wrap_exceptions
def update_ccc_upgrade_schedule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, ccc_upgrade_schedule_id, display_name, events, freeform_tags, defined_tags, if_match):

    if isinstance(ccc_upgrade_schedule_id, six.string_types) and len(ccc_upgrade_schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --ccc-upgrade-schedule-id cannot be whitespace or empty string')
    if not force:
        if events or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to events and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if events is not None:
        _details['events'] = cli_util.parse_json_parameter("events", events)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('compute_cloud_at_customer', 'compute_cloud_at_customer', ctx)
    result = client.update_ccc_upgrade_schedule(
        ccc_upgrade_schedule_id=ccc_upgrade_schedule_id,
        update_ccc_upgrade_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_ccc_upgrade_schedule') and callable(getattr(client, 'get_ccc_upgrade_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_ccc_upgrade_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
