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


@cli.command(cli_util.override('opsi.opsi_root_group.command_name', 'opsi'), cls=CommandGroupWithAlias, help=cli_util.override('opsi.opsi_root_group.help', """Use the Operations Insights API to perform data extraction operations to obtain database
resource utilization, performance statistics, and reference information. For more information,
see [About Oracle Cloud Infrastructure Operations Insights]."""), short_help=cli_util.override('opsi.opsi_root_group.short_help', """Operations Insights API"""))
@cli_util.help_option_group
def opsi_root_group():
    pass


@click.command(cli_util.override('opsi.enterprise_manager_bridges_group.command_name', 'enterprise-manager-bridges'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Enterprise Manager Bridge operations.""")
@cli_util.help_option_group
def enterprise_manager_bridges_group():
    pass


@click.command(cli_util.override('opsi.operations_insights_private_endpoint_collection_group.command_name', 'operations-insights-private-endpoint-collection'), cls=CommandGroupWithAlias, help="""A collection of Operation Insights private endpoint objects.""")
@cli_util.help_option_group
def operations_insights_private_endpoint_collection_group():
    pass


@click.command(cli_util.override('opsi.exadata_insights_group.command_name', 'exadata-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Exadata related operations.""")
@cli_util.help_option_group
def exadata_insights_group():
    pass


@click.command(cli_util.override('opsi.operations_insights_warehouses_group.command_name', 'operations-insights-warehouses'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Warehouse operations.""")
@cli_util.help_option_group
def operations_insights_warehouses_group():
    pass


@click.command(cli_util.override('opsi.database_insights_group.command_name', 'database-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights database-targeted operations.""")
@cli_util.help_option_group
def database_insights_group():
    pass


@click.command(cli_util.override('opsi.awr_hubs_group.command_name', 'awr-hubs'), cls=CommandGroupWithAlias, help="""Logical grouping used for Awr Hub operations.""")
@cli_util.help_option_group
def awr_hubs_group():
    pass


@click.command(cli_util.override('opsi.host_insights_group.command_name', 'host-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights host related operations.""")
@cli_util.help_option_group
def host_insights_group():
    pass


@click.command(cli_util.override('opsi.operations_insights_private_endpoint_group.command_name', 'operations-insights-private-endpoint'), cls=CommandGroupWithAlias, help="""A private endpoint that allows Operation Insights services to connect to databases in a customer's virtual cloud network (VCN).""")
@cli_util.help_option_group
def operations_insights_private_endpoint_group():
    pass


@click.command(cli_util.override('opsi.operations_insights_warehouse_users_group.command_name', 'operations-insights-warehouse-users'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Warehouse User operations.""")
@cli_util.help_option_group
def operations_insights_warehouse_users_group():
    pass


@click.command(cli_util.override('opsi.work_requests_group.command_name', 'work-requests'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Work Request operations.""")
@cli_util.help_option_group
def work_requests_group():
    pass


opsi_root_group.add_command(enterprise_manager_bridges_group)
opsi_root_group.add_command(operations_insights_private_endpoint_collection_group)
opsi_root_group.add_command(exadata_insights_group)
opsi_root_group.add_command(operations_insights_warehouses_group)
opsi_root_group.add_command(database_insights_group)
opsi_root_group.add_command(awr_hubs_group)
opsi_root_group.add_command(host_insights_group)
opsi_root_group.add_command(operations_insights_private_endpoint_group)
opsi_root_group.add_command(operations_insights_warehouse_users_group)
opsi_root_group.add_command(work_requests_group)


@exadata_insights_group.command(name=cli_util.override('opsi.add_exadata_insight_members.command_name', 'add'), help=u"""Add new members (e.g. databases and hosts) to an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](addExadataInsightMembers)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_EXADATA"]), help=u"""Source of the Exadata system.""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_exadata_insight_members(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, exadata_insight_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.add_exadata_insight_members(
        exadata_insight_id=exadata_insight_id,
        add_exadata_insight_members_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.add_exadata_insight_members_add_em_managed_external_exadata_insight_members_details.command_name', 'add-exadata-insight-members-add-em-managed-external-exadata-insight-members-details'), help=u"""Add new members (e.g. databases and hosts) to an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](addExadataInsightMembers)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--member-entity-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type CreateEmManagedExternalExadataMemberEntityDetails.  For documentation on CreateEmManagedExternalExadataMemberEntityDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/CreateEmManagedExternalExadataMemberEntityDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'member-entity-details': {'module': 'opsi', 'class': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'member-entity-details': {'module': 'opsi', 'class': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'}})
@cli_util.wrap_exceptions
def add_exadata_insight_members_add_em_managed_external_exadata_insight_members_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, member_entity_details, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if member_entity_details is not None:
        _details['memberEntityDetails'] = cli_util.parse_json_parameter("member_entity_details", member_entity_details)

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_EXADATA'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.add_exadata_insight_members(
        exadata_insight_id=exadata_insight_id,
        add_exadata_insight_members_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.change_database_insight_compartment.command_name', 'change'), help=u"""Moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeDatabaseInsightCompartment)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_insight_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, compartment_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_database_insight_compartment(
        database_insight_id=database_insight_id,
        change_database_insight_compartment_details=_details,
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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.change_enterprise_manager_bridge_compartment.command_name', 'change'), help=u"""Moves a EnterpriseManagerBridge resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeEnterpriseManagerBridgeCompartment)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_enterprise_manager_bridge_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, enterprise_manager_bridge_id, compartment_id, if_match):

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_enterprise_manager_bridge_compartment(
        enterprise_manager_bridge_id=enterprise_manager_bridge_id,
        change_enterprise_manager_bridge_compartment_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.change_exadata_insight_compartment.command_name', 'change'), help=u"""Moves an Exadata insight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeExadataInsightCompartment)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_exadata_insight_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, compartment_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_exadata_insight_compartment(
        exadata_insight_id=exadata_insight_id,
        change_exadata_insight_compartment_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.change_host_insight_compartment.command_name', 'change'), help=u"""Moves a HostInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeHostInsightCompartment)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_host_insight_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, compartment_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_host_insight_compartment(
        host_insight_id=host_insight_id,
        change_host_insight_compartment_details=_details,
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


@operations_insights_private_endpoint_group.command(name=cli_util.override('opsi.change_operations_insights_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a private endpoint from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeOperationsInsightsPrivateEndpointCompartment)""")
@cli_util.option('--operations-insights-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint.""")
@cli_util.option('--compartment-id', help=u"""The new compartment [OCID] of the Private service accessed database.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_operations_insights_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_private_endpoint_id, compartment_id, if_match):

    if isinstance(operations_insights_private_endpoint_id, six.string_types) and len(operations_insights_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_operations_insights_private_endpoint_compartment(
        operations_insights_private_endpoint_id=operations_insights_private_endpoint_id,
        change_operations_insights_private_endpoint_compartment_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.change_pe_comanaged_database_insight.command_name', 'change-pe-comanaged'), help=u"""Change the connection details of a co-managed  database insight. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changePeComanagedDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--service-name', required=True, help=u"""Database service name used for connection requests.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the OPSI private endpoint""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}})
@cli_util.wrap_exceptions
def change_pe_comanaged_database_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, service_name, credential_details, opsi_private_endpoint_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceName'] = service_name
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['opsiPrivateEndpointId'] = opsi_private_endpoint_id

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_pe_comanaged_database_insight(
        database_insight_id=database_insight_id,
        change_pe_comanaged_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.change_pe_comanaged_database_insight_credentials_by_source.command_name', 'change-pe-comanaged-database-insight-credentials-by-source'), help=u"""Change the connection details of a co-managed  database insight. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changePeComanagedDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--service-name', required=True, help=u"""Database service name used for connection requests.""")
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the OPSI private endpoint""")
@cli_util.option('--credential-details-credential-source-name', required=True, help=u"""Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_pe_comanaged_database_insight_credentials_by_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, service_name, opsi_private_endpoint_id, credential_details_credential_source_name, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['serviceName'] = service_name
    _details['opsiPrivateEndpointId'] = opsi_private_endpoint_id
    _details['credentialDetails']['credentialSourceName'] = credential_details_credential_source_name

    _details['credentialDetails']['credentialType'] = 'CREDENTIALS_BY_SOURCE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_pe_comanaged_database_insight(
        database_insight_id=database_insight_id,
        change_pe_comanaged_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.change_pe_comanaged_database_insight_credential_by_vault.command_name', 'change-pe-comanaged-database-insight-credential-by-vault'), help=u"""Change the connection details of a co-managed  database insight. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changePeComanagedDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--service-name', required=True, help=u"""Database service name used for connection requests.""")
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the OPSI private endpoint""")
@cli_util.option('--credential-details-credential-source-name', required=True, help=u"""Credential source name that had been added in Management Agent wallet. This is supplied in the External Database Service.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--credential-details-user-name', help=u"""database user name.""")
@cli_util.option('--credential-details-password-secret-id', help=u"""The secret [OCID] mapping to the database credentials.""")
@cli_util.option('--credential-details-role', type=custom_types.CliCaseInsensitiveChoice(["NORMAL"]), help=u"""database user role.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_pe_comanaged_database_insight_credential_by_vault(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, service_name, opsi_private_endpoint_id, credential_details_credential_source_name, if_match, credential_details_user_name, credential_details_password_secret_id, credential_details_role):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialDetails'] = {}
    _details['serviceName'] = service_name
    _details['opsiPrivateEndpointId'] = opsi_private_endpoint_id
    _details['credentialDetails']['credentialSourceName'] = credential_details_credential_source_name

    if credential_details_user_name is not None:
        _details['credentialDetails']['userName'] = credential_details_user_name

    if credential_details_password_secret_id is not None:
        _details['credentialDetails']['passwordSecretId'] = credential_details_password_secret_id

    if credential_details_role is not None:
        _details['credentialDetails']['role'] = credential_details_role

    _details['credentialDetails']['credentialType'] = 'CREDENTIALS_BY_VAULT'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.change_pe_comanaged_database_insight(
        database_insight_id=database_insight_id,
        change_pe_comanaged_database_insight_details=_details,
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


@awr_hubs_group.command(name=cli_util.override('opsi.create_awr_hub.command_name', 'create'), help=u"""Create a AWR hub resource for the tenant in Operations Insights. This resource will be created in root compartment. \n[Command Reference](createAwrHub)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""OPSI Warehouse OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""User-friedly name of AWR Hub that does not have to be unique.""")
@cli_util.option('--object-storage-bucket-name', required=True, help=u"""Object Storage Bucket Name""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'AwrHub'})
@cli_util.wrap_exceptions
def create_awr_hub(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_id, compartment_id, display_name, object_storage_bucket_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operationsInsightsWarehouseId'] = operations_insights_warehouse_id
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['objectStorageBucketName'] = object_storage_bucket_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_awr_hub(
        create_awr_hub_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.create_database_insight.command_name', 'create'), help=u"""Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](createDatabaseInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of database""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def create_database_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_database_insight(
        create_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.create_database_insight_create_em_managed_external_database_insight_details.command_name', 'create-database-insight-create-em-managed-external-database-insight-details'), help=u"""Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](createDatabaseInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of database""")
@cli_util.option('--enterprise-manager-identifier', required=True, help=u"""Enterprise Manager Unique Identifier""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID""")
@cli_util.option('--enterprise-manager-entity-identifier', required=True, help=u"""Enterprise Manager Entity Unique Identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--exadata-insight-id', help=u"""The [OCID] of the Exadata insight.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def create_database_insight_create_em_managed_external_database_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, enterprise_manager_identifier, enterprise_manager_bridge_id, enterprise_manager_entity_identifier, freeform_tags, defined_tags, exadata_insight_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['enterpriseManagerIdentifier'] = enterprise_manager_identifier
    _details['enterpriseManagerBridgeId'] = enterprise_manager_bridge_id
    _details['enterpriseManagerEntityIdentifier'] = enterprise_manager_entity_identifier

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if exadata_insight_id is not None:
        _details['exadataInsightId'] = exadata_insight_id

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_database_insight(
        create_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.create_database_insight_create_pe_comanaged_database_insight_details.command_name', 'create-database-insight-create-pe-comanaged-database-insight-details'), help=u"""Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](createDatabaseInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of database""")
@cli_util.option('--database-id', required=True, help=u"""The [OCID] of the database.""")
@cli_util.option('--database-resource-type', required=True, help=u"""OCI database resource type""")
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the OPSI private endpoint""")
@cli_util.option('--service-name', required=True, help=u"""Database service name used for connection requests.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["VIRTUAL_MACHINE", "BARE_METAL", "EXACS"]), help=u"""Database Deployment Type""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}, 'system-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}, 'system-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def create_database_insight_create_pe_comanaged_database_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, database_id, database_resource_type, opsi_private_endpoint_id, service_name, credential_details, deployment_type, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['databaseId'] = database_id
    _details['databaseResourceType'] = database_resource_type
    _details['opsiPrivateEndpointId'] = opsi_private_endpoint_id
    _details['serviceName'] = service_name
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)
    _details['deploymentType'] = deployment_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    _details['entitySource'] = 'PE_COMANAGED_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_database_insight(
        create_database_insight_details=_details,
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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.create_enterprise_manager_bridge.command_name', 'create'), help=u"""Create a Enterprise Manager bridge in Operations Insights. \n[Command Reference](createEnterpriseManagerBridge)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier of the Enterprise Manager bridge""")
@cli_util.option('--display-name', required=True, help=u"""User-friedly name of Enterprise Manager Bridge that does not have to be unique.""")
@cli_util.option('--object-storage-bucket-name', required=True, help=u"""Object Storage Bucket Name""")
@cli_util.option('--description', help=u"""Description of Enterprise Manager Bridge""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'EnterpriseManagerBridge'})
@cli_util.wrap_exceptions
def create_enterprise_manager_bridge(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, object_storage_bucket_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['objectStorageBucketName'] = object_storage_bucket_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_enterprise_manager_bridge(
        create_enterprise_manager_bridge_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.create_exadata_insight.command_name', 'create'), help=u"""Create an Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](createExadataInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_EXADATA"]), help=u"""Source of the Exadata system.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of Exadata insight""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'ExadataInsight'})
@cli_util.wrap_exceptions
def create_exadata_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_exadata_insight(
        create_exadata_insight_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.create_exadata_insight_create_em_managed_external_exadata_insight_details.command_name', 'create-exadata-insight-create-em-managed-external-exadata-insight-details'), help=u"""Create an Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](createExadataInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of Exadata insight""")
@cli_util.option('--enterprise-manager-identifier', required=True, help=u"""Enterprise Manager Unique Identifier""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID""")
@cli_util.option('--enterprise-manager-entity-identifier', required=True, help=u"""Enterprise Manager Entity Unique Identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--member-entity-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type CreateEmManagedExternalExadataMemberEntityDetails.  For documentation on CreateEmManagedExternalExadataMemberEntityDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/CreateEmManagedExternalExadataMemberEntityDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-auto-sync-enabled', type=click.BOOL, help=u"""Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'member-entity-details': {'module': 'opsi', 'class': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'member-entity-details': {'module': 'opsi', 'class': 'list[CreateEmManagedExternalExadataMemberEntityDetails]'}}, output_type={'module': 'opsi', 'class': 'ExadataInsight'})
@cli_util.wrap_exceptions
def create_exadata_insight_create_em_managed_external_exadata_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, enterprise_manager_identifier, enterprise_manager_bridge_id, enterprise_manager_entity_identifier, freeform_tags, defined_tags, member_entity_details, is_auto_sync_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['enterpriseManagerIdentifier'] = enterprise_manager_identifier
    _details['enterpriseManagerBridgeId'] = enterprise_manager_bridge_id
    _details['enterpriseManagerEntityIdentifier'] = enterprise_manager_entity_identifier

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if member_entity_details is not None:
        _details['memberEntityDetails'] = cli_util.parse_json_parameter("member_entity_details", member_entity_details)

    if is_auto_sync_enabled is not None:
        _details['isAutoSyncEnabled'] = is_auto_sync_enabled

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_EXADATA'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_exadata_insight(
        create_exadata_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.create_host_insight.command_name', 'create'), help=u"""Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](createHostInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of host""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_host_insight(
        create_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.create_host_insight_create_macs_managed_external_host_insight_details.command_name', 'create-host-insight-create-macs-managed-external-host-insight-details'), help=u"""Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](createHostInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of host""")
@cli_util.option('--management-agent-id', required=True, help=u"""The [OCID] of the Management Agent""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight_create_macs_managed_external_host_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, management_agent_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['managementAgentId'] = management_agent_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['entitySource'] = 'MACS_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_host_insight(
        create_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.create_host_insight_create_em_managed_external_host_insight_details.command_name', 'create-host-insight-create-em-managed-external-host-insight-details'), help=u"""Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](createHostInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of host""")
@cli_util.option('--enterprise-manager-identifier', required=True, help=u"""Enterprise Manager Unique Identifier""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""OPSI Enterprise Manager Bridge OCID""")
@cli_util.option('--enterprise-manager-entity-identifier', required=True, help=u"""Enterprise Manager Entity Unique Identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--exadata-insight-id', help=u"""The [OCID] of the Exadata insight.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def create_host_insight_create_em_managed_external_host_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, enterprise_manager_identifier, enterprise_manager_bridge_id, enterprise_manager_entity_identifier, freeform_tags, defined_tags, exadata_insight_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['enterpriseManagerIdentifier'] = enterprise_manager_identifier
    _details['enterpriseManagerBridgeId'] = enterprise_manager_bridge_id
    _details['enterpriseManagerEntityIdentifier'] = enterprise_manager_entity_identifier

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if exadata_insight_id is not None:
        _details['exadataInsightId'] = exadata_insight_id

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_host_insight(
        create_host_insight_details=_details,
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


@operations_insights_private_endpoint_group.command(name=cli_util.override('opsi.create_operations_insights_private_endpoint.command_name', 'create'), help=u"""Create a private endpoint resource for the tenant in Operations Insights. This resource will be created in customer compartment. \n[Command Reference](createOperationsInsightsPrivateEndpoint)""")
@cli_util.option('--display-name', required=True, help=u"""The display name for the private endpoint. It is changeable.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] of the Private service accessed database.""")
@cli_util.option('--vcn-id', required=True, help=u"""The VCN [OCID] of the Private service accessed database.""")
@cli_util.option('--subnet-id', required=True, help=u"""The Subnet [OCID] of the Private service accessed database.""")
@cli_util.option('--is-used-for-rac-dbs', required=True, type=click.BOOL, help=u"""The flag to identify if private endpoint is used for rac database or not""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCID] of the network security groups that the private endpoint belongs to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'OperationsInsightsPrivateEndpoint'})
@cli_util.wrap_exceptions
def create_operations_insights_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, vcn_id, subnet_id, is_used_for_rac_dbs, description, nsg_ids, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['vcnId'] = vcn_id
    _details['subnetId'] = subnet_id
    _details['isUsedForRacDbs'] = is_used_for_rac_dbs

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_operations_insights_private_endpoint(
        create_operations_insights_private_endpoint_details=_details,
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


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.create_operations_insights_warehouse.command_name', 'create'), help=u"""Create a Operations Insights Warehouse resource for the tenant in Operations Insights. New ADW will be provisioned for this tenant. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. If the 'opsi-warehouse-type' header is passed to the API, a warehouse resource without ADW or Schema provisioning is created. \n[Command Reference](createOperationsInsightsWarehouse)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""User-friedly name of Operations Insights Warehouse that does not have to be unique.""")
@cli_util.option('--cpu-allocated', required=True, help=u"""Number of OCPUs allocated to OPSI Warehouse ADW.""")
@cli_util.option('--storage-allocated-in-gbs', help=u"""Storage allocated to OPSI Warehouse ADW.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouse'})
@cli_util.wrap_exceptions
def create_operations_insights_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, cpu_allocated, storage_allocated_in_gbs, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['cpuAllocated'] = cpu_allocated

    if storage_allocated_in_gbs is not None:
        _details['storageAllocatedInGBs'] = storage_allocated_in_gbs

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_operations_insights_warehouse(
        create_operations_insights_warehouse_details=_details,
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


@operations_insights_warehouse_users_group.command(name=cli_util.override('opsi.create_operations_insights_warehouse_user.command_name', 'create'), help=u"""Create a Operations Insights Warehouse user resource for the tenant in Operations Insights. This resource will be created in root compartment. \n[Command Reference](createOperationsInsightsWarehouseUser)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""OPSI Warehouse OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--name', required=True, help=u"""Username for schema which would have access to AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.""")
@cli_util.option('--connection-password', required=True, help=u"""User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.""")
@cli_util.option('--is-awr-data-access', required=True, type=click.BOOL, help=u"""Indicate whether user has access to AWR data.""")
@cli_util.option('--is-em-data-access', type=click.BOOL, help=u"""Indicate whether user has access to EM data.""")
@cli_util.option('--is-opsi-data-access', type=click.BOOL, help=u"""Indicate whether user has access to OPSI data.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouseUser'})
@cli_util.wrap_exceptions
def create_operations_insights_warehouse_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_id, compartment_id, name, connection_password, is_awr_data_access, is_em_data_access, is_opsi_data_access, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operationsInsightsWarehouseId'] = operations_insights_warehouse_id
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['connectionPassword'] = connection_password
    _details['isAwrDataAccess'] = is_awr_data_access

    if is_em_data_access is not None:
        _details['isEmDataAccess'] = is_em_data_access

    if is_opsi_data_access is not None:
        _details['isOpsiDataAccess'] = is_opsi_data_access

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.create_operations_insights_warehouse_user(
        create_operations_insights_warehouse_user_details=_details,
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


@awr_hubs_group.command(name=cli_util.override('opsi.delete_awr_hub.command_name', 'delete'), help=u"""Deletes an AWR hub. \n[Command Reference](deleteAwrHub)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_awr_hub(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, awr_hub_id, if_match):

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_awr_hub(
        awr_hub_id=awr_hub_id,
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


@database_insights_group.command(name=cli_util.override('opsi.delete_database_insight.command_name', 'delete'), help=u"""Deletes a database insight. The database insight will be deleted and cannot be enabled again. \n[Command Reference](deleteDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_database_insight(
        database_insight_id=database_insight_id,
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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.delete_enterprise_manager_bridge.command_name', 'delete'), help=u"""Deletes an Operations Insights Enterprise Manager bridge. If any database insight is still referencing this bridge, the operation will fail. \n[Command Reference](deleteEnterpriseManagerBridge)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_enterprise_manager_bridge(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, enterprise_manager_bridge_id, if_match):

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_enterprise_manager_bridge(
        enterprise_manager_bridge_id=enterprise_manager_bridge_id,
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


@exadata_insights_group.command(name=cli_util.override('opsi.delete_exadata_insight.command_name', 'delete'), help=u"""Deletes an Exadata insight. The Exadata insight will be deleted and cannot be enabled again. \n[Command Reference](deleteExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_exadata_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_exadata_insight(
        exadata_insight_id=exadata_insight_id,
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


@host_insights_group.command(name=cli_util.override('opsi.delete_host_insight.command_name', 'delete'), help=u"""Deletes a host insight. The host insight will be deleted and cannot be enabled again. \n[Command Reference](deleteHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_host_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_host_insight(
        host_insight_id=host_insight_id,
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


@operations_insights_private_endpoint_group.command(name=cli_util.override('opsi.delete_operations_insights_private_endpoint.command_name', 'delete'), help=u"""Deletes a private endpoint. \n[Command Reference](deleteOperationsInsightsPrivateEndpoint)""")
@cli_util.option('--operations-insights-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operations_insights_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_private_endpoint_id, if_match):

    if isinstance(operations_insights_private_endpoint_id, six.string_types) and len(operations_insights_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_operations_insights_private_endpoint(
        operations_insights_private_endpoint_id=operations_insights_private_endpoint_id,
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


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.delete_operations_insights_warehouse.command_name', 'delete'), help=u"""Deletes an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. User must delete AWR Hub resource for this warehouse before calling this operation. User must delete the warehouse users before calling this operation. \n[Command Reference](deleteOperationsInsightsWarehouse)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operations_insights_warehouse(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_id, if_match):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_operations_insights_warehouse(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
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


@operations_insights_warehouse_users_group.command(name=cli_util.override('opsi.delete_operations_insights_warehouse_user.command_name', 'delete'), help=u"""Deletes an Operations Insights Warehouse User. \n[Command Reference](deleteOperationsInsightsWarehouseUser)""")
@cli_util.option('--operations-insights-warehouse-user-id', required=True, help=u"""Unique Operations Insights Warehouse User identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operations_insights_warehouse_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_user_id, if_match):

    if isinstance(operations_insights_warehouse_user_id, six.string_types) and len(operations_insights_warehouse_user_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.delete_operations_insights_warehouse_user(
        operations_insights_warehouse_user_id=operations_insights_warehouse_user_id,
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


@database_insights_group.command(name=cli_util.override('opsi.disable_database_insight.command_name', 'disable'), help=u"""Disables a database in Operations Insights. Database metric collection and analysis will be stopped. \n[Command Reference](disableDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_database_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.disable_database_insight(
        database_insight_id=database_insight_id,
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


@exadata_insights_group.command(name=cli_util.override('opsi.disable_exadata_insight.command_name', 'disable'), help=u"""Disables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be stopped. \n[Command Reference](disableExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_exadata_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.disable_exadata_insight(
        exadata_insight_id=exadata_insight_id,
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


@host_insights_group.command(name=cli_util.override('opsi.disable_host_insight.command_name', 'disable'), help=u"""Disables a host in Operations Insights. Host metric collection and analysis will be stopped. \n[Command Reference](disableHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disable_host_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.disable_host_insight(
        host_insight_id=host_insight_id,
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


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.download_operations_insights_warehouse_wallet.command_name', 'download'), help=u"""Download the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed. \n[Command Reference](downloadOperationsInsightsWarehouseWallet)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--operations-insights-warehouse-wallet-password', required=True, help=u"""User provided ADW wallet password for the Operations Insights Warehouse.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def download_operations_insights_warehouse_wallet(ctx, from_json, file, operations_insights_warehouse_id, operations_insights_warehouse_wallet_password):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operationsInsightsWarehouseWalletPassword'] = operations_insights_warehouse_wallet_password

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.download_operations_insights_warehouse_wallet(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
        download_operations_insights_warehouse_wallet_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.enable_database_insight.command_name', 'enable'), help=u"""Enables a database in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](enableDatabaseInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_database_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, database_insight_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_database_insight(
        database_insight_id=database_insight_id,
        enable_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.enable_database_insight_enable_em_managed_external_database_insight_details.command_name', 'enable-database-insight-enable-em-managed-external-database-insight-details'), help=u"""Enables a database in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](enableDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_database_insight_enable_em_managed_external_database_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_database_insight(
        database_insight_id=database_insight_id,
        enable_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.enable_database_insight_enable_pe_comanaged_database_insight_details.command_name', 'enable-database-insight-enable-pe-comanaged-database-insight-details'), help=u"""Enables a database in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](enableDatabaseInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] of the Private service accessed database.""")
@cli_util.option('--opsi-private-endpoint-id', required=True, help=u"""The [OCID] of the OPSI private endpoint""")
@cli_util.option('--service-name', required=True, help=u"""Database service name used for connection requests.""")
@cli_util.option('--credential-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""System tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'credential-details': {'module': 'opsi', 'class': 'CredentialDetails'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def enable_database_insight_enable_pe_comanaged_database_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, opsi_private_endpoint_id, service_name, credential_details, database_insight_id, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['opsiPrivateEndpointId'] = opsi_private_endpoint_id
    _details['serviceName'] = service_name
    _details['credentialDetails'] = cli_util.parse_json_parameter("credential_details", credential_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    _details['entitySource'] = 'PE_COMANAGED_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_database_insight(
        database_insight_id=database_insight_id,
        enable_database_insight_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.enable_exadata_insight.command_name', 'enable'), help=u"""Enables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](enableExadataInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_EXADATA"]), help=u"""Source of the Exadata system.""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_exadata_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, exadata_insight_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_exadata_insight(
        exadata_insight_id=exadata_insight_id,
        enable_exadata_insight_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.enable_exadata_insight_enable_em_managed_external_exadata_insight_details.command_name', 'enable-exadata-insight-enable-em-managed-external-exadata-insight-details'), help=u"""Enables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started. \n[Command Reference](enableExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_exadata_insight_enable_em_managed_external_exadata_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_EXADATA'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_exadata_insight(
        exadata_insight_id=exadata_insight_id,
        enable_exadata_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.enable_host_insight.command_name', 'enable'), help=u"""Enables a host in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](enableHostInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, entity_source, host_insight_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_host_insight(
        host_insight_id=host_insight_id,
        enable_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.enable_host_insight_enable_macs_managed_external_host_insight_details.command_name', 'enable-host-insight-enable-macs-managed-external-host-insight-details'), help=u"""Enables a host in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](enableHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight_enable_macs_managed_external_host_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['entitySource'] = 'MACS_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_host_insight(
        host_insight_id=host_insight_id,
        enable_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.enable_host_insight_enable_em_managed_external_host_insight_details.command_name', 'enable-host-insight-enable-em-managed-external-host-insight-details'), help=u"""Enables a host in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](enableHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_host_insight_enable_em_managed_external_host_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.enable_host_insight(
        host_insight_id=host_insight_id,
        enable_host_insight_details=_details,
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


@awr_hubs_group.command(name=cli_util.override('opsi.get_awr_hub.command_name', 'get'), help=u"""Gets details of an AWR hub. \n[Command Reference](getAwrHub)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'AwrHub'})
@cli_util.wrap_exceptions
def get_awr_hub(ctx, from_json, awr_hub_id):

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_awr_hub(
        awr_hub_id=awr_hub_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@awr_hubs_group.command(name=cli_util.override('opsi.get_awr_report.command_name', 'get-awr-report'), help=u"""Gets the AWR report for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not be greater than 7 days. Either beginSnapshotIdentifierGreaterThanOrEqualTo & endSnapshotIdentifierLessThanOrEqualTo params Or timeGreaterThanOrEqualTo & timeLessThanOrEqualTo params are required. \n[Command Reference](getAwrReport)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@cli_util.option('--awr-source-database-identifier', required=True, help=u"""AWR source database identifier.""")
@cli_util.option('--report-format', type=custom_types.CliCaseInsensitiveChoice(["HTML", "TEXT"]), help=u"""The format of the AWR report. Default report format is HTML.""")
@cli_util.option('--instance-number', help=u"""The optional single value query parameter to filter by database instance number.""")
@cli_util.option('--begin-snapshot-identifier-greater-than-or-equal-to', type=click.INT, help=u"""The optional greater than or equal to filter on the snapshot ID.""")
@cli_util.option('--end-snapshot-identifier-less-than-or-equal-to', type=click.INT, help=u"""The optional less than or equal to query parameter to filter the snapshot Identifier.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'AwrReport'})
@cli_util.wrap_exceptions
def get_awr_report(ctx, from_json, awr_hub_id, awr_source_database_identifier, report_format, instance_number, begin_snapshot_identifier_greater_than_or_equal_to, end_snapshot_identifier_less_than_or_equal_to, time_greater_than_or_equal_to, time_less_than_or_equal_to):

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')

    kwargs = {}
    if report_format is not None:
        kwargs['report_format'] = report_format
    if instance_number is not None:
        kwargs['instance_number'] = instance_number
    if begin_snapshot_identifier_greater_than_or_equal_to is not None:
        kwargs['begin_snapshot_identifier_greater_than_or_equal_to'] = begin_snapshot_identifier_greater_than_or_equal_to
    if end_snapshot_identifier_less_than_or_equal_to is not None:
        kwargs['end_snapshot_identifier_less_than_or_equal_to'] = end_snapshot_identifier_less_than_or_equal_to
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_awr_report(
        awr_hub_id=awr_hub_id,
        awr_source_database_identifier=awr_source_database_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.get_database_insight.command_name', 'get'), help=u"""Gets details of a database insight. \n[Command Reference](getDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def get_database_insight(ctx, from_json, database_insight_id):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_database_insight(
        database_insight_id=database_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.get_enterprise_manager_bridge.command_name', 'get'), help=u"""Gets details of an Operations Insights Enterprise Manager bridge. \n[Command Reference](getEnterpriseManagerBridge)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'EnterpriseManagerBridge'})
@cli_util.wrap_exceptions
def get_enterprise_manager_bridge(ctx, from_json, enterprise_manager_bridge_id):

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_enterprise_manager_bridge(
        enterprise_manager_bridge_id=enterprise_manager_bridge_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.get_exadata_insight.command_name', 'get'), help=u"""Gets details of an Exadata insight. \n[Command Reference](getExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'ExadataInsight'})
@cli_util.wrap_exceptions
def get_exadata_insight(ctx, from_json, exadata_insight_id):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_exadata_insight(
        exadata_insight_id=exadata_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.get_host_insight.command_name', 'get'), help=u"""Gets details of a host insight. \n[Command Reference](getHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'HostInsight'})
@cli_util.wrap_exceptions
def get_host_insight(ctx, from_json, host_insight_id):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_host_insight(
        host_insight_id=host_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operations_insights_private_endpoint_group.command(name=cli_util.override('opsi.get_operations_insights_private_endpoint.command_name', 'get'), help=u"""Gets the details of the specified private endpoint. \n[Command Reference](getOperationsInsightsPrivateEndpoint)""")
@cli_util.option('--operations-insights-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_operations_insights_private_endpoint(ctx, from_json, operations_insights_private_endpoint_id):

    if isinstance(operations_insights_private_endpoint_id, six.string_types) and len(operations_insights_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_operations_insights_private_endpoint(
        operations_insights_private_endpoint_id=operations_insights_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.get_operations_insights_warehouse.command_name', 'get'), help=u"""Gets details of an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. \n[Command Reference](getOperationsInsightsWarehouse)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouse'})
@cli_util.wrap_exceptions
def get_operations_insights_warehouse(ctx, from_json, operations_insights_warehouse_id):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_operations_insights_warehouse(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operations_insights_warehouse_users_group.command(name=cli_util.override('opsi.get_operations_insights_warehouse_user.command_name', 'get'), help=u"""Gets details of an Operations Insights Warehouse User. \n[Command Reference](getOperationsInsightsWarehouseUser)""")
@cli_util.option('--operations-insights-warehouse-user-id', required=True, help=u"""Unique Operations Insights Warehouse User identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouseUser'})
@cli_util.wrap_exceptions
def get_operations_insights_warehouse_user(ctx, from_json, operations_insights_warehouse_user_id):

    if isinstance(operations_insights_warehouse_user_id, six.string_types) and len(operations_insights_warehouse_user_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-user-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_operations_insights_warehouse_user(
        operations_insights_warehouse_user_id=operations_insights_warehouse_user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_requests_group.command(name=cli_util.override('opsi.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_database_configuration.command_name', 'ingest-database-configuration'), help=u"""This is a generic ingest endpoint for all database configuration metrics. \n[Command Reference](ingestDatabaseConfiguration)""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of one or more database configuration metrics objects.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[DatabaseConfigurationMetricGroup]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[DatabaseConfigurationMetricGroup]'}}, output_type={'module': 'opsi', 'class': 'IngestDatabaseConfigurationResponseDetails'})
@cli_util.wrap_exceptions
def ingest_database_configuration(ctx, from_json, items, database_id, id, if_match):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_database_configuration(
        ingest_database_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.ingest_host_configuration.command_name', 'ingest-host-configuration'), help=u"""This is a generic ingest endpoint for all the host configuration metrics \n[Command Reference](ingestHostConfiguration)""")
@cli_util.option('--id', required=True, help=u"""Required [OCID] of the host insight resource.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of one or more host configuration metric data points""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[HostConfigurationMetricGroup]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[HostConfigurationMetricGroup]'}}, output_type={'module': 'opsi', 'class': 'IngestHostConfigurationResponseDetails'})
@cli_util.wrap_exceptions
def ingest_host_configuration(ctx, from_json, id, items, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_host_configuration(
        id=id,
        ingest_host_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.ingest_host_metrics.command_name', 'ingest-host-metrics'), help=u"""This is a generic ingest endpoint for all the host performance metrics \n[Command Reference](ingestHostMetrics)""")
@cli_util.option('--id', required=True, help=u"""Required [OCID] of the host insight resource.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of one or more host performance metric data points""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[HostPerformanceMetricGroup]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[HostPerformanceMetricGroup]'}}, output_type={'module': 'opsi', 'class': 'IngestHostMetricsResponseDetails'})
@cli_util.wrap_exceptions
def ingest_host_metrics(ctx, from_json, id, items, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_host_metrics(
        id=id,
        ingest_host_metrics_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_bucket.command_name', 'ingest-sql-bucket'), help=u"""The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified. \n[Command Reference](ingestSqlBucket)""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Bucket Metric Entries.

This option is a JSON list with items of type SqlBucket.  For documentation on SqlBucket please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlBucket.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlBucket]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlBucket]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlBucketResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_bucket(ctx, from_json, items, compartment_id, database_id, id, if_match):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_bucket(
        ingest_sql_bucket_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_plan_lines.command_name', 'ingest-sql-plan-lines'), help=u"""The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified. \n[Command Reference](ingestSqlPlanLines)""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Plan Line Entries.

This option is a JSON list with items of type SqlPlanLine.  For documentation on SqlPlanLine please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlPlanLine.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlPlanLine]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlPlanLine]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlPlanLinesResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_plan_lines(ctx, from_json, items, compartment_id, database_id, id, if_match):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_plan_lines(
        ingest_sql_plan_lines_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_stats.command_name', 'ingest-sql-stats'), help=u"""The SQL Stats endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline. Either databaseId or id must be specified. \n[Command Reference](ingestSqlStats)""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Stats Metric Entries.

This option is a JSON list with items of type SqlStats.  For documentation on SqlStats please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlStats.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlStats]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlStats]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlStatsResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_stats(ctx, from_json, items, database_id, id, if_match):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_stats(
        ingest_sql_stats_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.ingest_sql_text.command_name', 'ingest-sql-text'), help=u"""The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline. Either databaseId or id must be specified. Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion. \n[Command Reference](ingestSqlText)""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of SQL Text Entries.

This option is a JSON list with items of type SqlText.  For documentation on SqlText please see our API reference: https://docs.cloud.oracle.com/api/#/en/operationsinsights/20200630/datatypes/SqlText.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'opsi', 'class': 'list[SqlText]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'opsi', 'class': 'list[SqlText]'}}, output_type={'module': 'opsi', 'class': 'IngestSqlTextResponseDetails'})
@cli_util.wrap_exceptions
def ingest_sql_text(ctx, from_json, items, compartment_id, database_id, id, if_match):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.ingest_sql_text(
        ingest_sql_text_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@awr_hubs_group.command(name=cli_util.override('opsi.list_awr_hubs.command_name', 'list'), help=u"""Gets a list of AWR hubs. Either compartmentId or id must be specified. All these resources are expected to be in root compartment. \n[Command Reference](listAwrHubs)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--id', help=u"""Unique Awr Hub identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'AwrHubSummaryCollection'})
@cli_util.wrap_exceptions
def list_awr_hubs(ctx, from_json, all_pages, page_size, operations_insights_warehouse_id, compartment_id, display_name, id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
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
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_awr_hubs,
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_awr_hubs,
            limit,
            page_size,
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    else:
        result = client.list_awr_hubs(
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@awr_hubs_group.command(name=cli_util.override('opsi.list_awr_snapshots.command_name', 'list-awr-snapshots'), help=u"""Lists AWR snapshots for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not exceed an elapsed range of 1 day. The timeGreaterThanOrEqualTo & timeLessThanOrEqualTo params are optional. If these params are not provided, by default last 1 day snapshots will be returned. \n[Command Reference](listAwrSnapshots)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@cli_util.option('--awr-source-database-identifier', required=True, help=u"""AWR source database identifier.""")
@cli_util.option('--time-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeBegin", "snapshotId"]), help=u"""The option to sort the AWR snapshot summary data. Default sort is by timeBegin.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'AwrSnapshotCollection'})
@cli_util.wrap_exceptions
def list_awr_snapshots(ctx, from_json, all_pages, page_size, awr_hub_id, awr_source_database_identifier, time_greater_than_or_equal_to, time_less_than_or_equal_to, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')

    kwargs = {}
    if time_greater_than_or_equal_to is not None:
        kwargs['time_greater_than_or_equal_to'] = time_greater_than_or_equal_to
    if time_less_than_or_equal_to is not None:
        kwargs['time_less_than_or_equal_to'] = time_less_than_or_equal_to
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_awr_snapshots,
            awr_hub_id=awr_hub_id,
            awr_source_database_identifier=awr_source_database_identifier,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_awr_snapshots,
            limit,
            page_size,
            awr_hub_id=awr_hub_id,
            awr_source_database_identifier=awr_source_database_identifier,
            **kwargs
        )
    else:
        result = client.list_awr_snapshots(
            awr_hub_id=awr_hub_id,
            awr_source_database_identifier=awr_source_database_identifier,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_database_configurations.command_name', 'list-database-configurations'), help=u"""Gets a list of database insight configurations based on the query parameters specified. Either compartmentId or databaseInsightId query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of database insight configurations in that compartment and in all sub-compartments will be returned. \n[Command Reference](listDatabaseConfigurations)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseName", "databaseDisplayName", "databaseType"]), help=u"""Database configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'DatabaseConfigurationCollection'})
@cli_util.wrap_exceptions
def list_database_configurations(ctx, from_json, all_pages, page_size, compartment_id, enterprise_manager_bridge_id, id, database_id, exadata_insight_id, cdb_name, database_type, limit, page, sort_order, sort_by, host_name, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if enterprise_manager_bridge_id is not None:
        kwargs['enterprise_manager_bridge_id'] = enterprise_manager_bridge_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_configurations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_configurations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_database_configurations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_database_insights.command_name', 'list'), help=u"""Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of database insights in that compartment and in all sub-compartments will be returned. \n[Command Reference](listDatabaseInsights)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["DISABLED", "ENABLED", "TERMINATED"]), multiple=True, help=u"""Resource Status""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"]), multiple=True, help=u"""Specifies the fields to return in a database summary response. By default all fields are returned if omitted.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseName", "databaseDisplayName", "databaseType"]), help=u"""Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--exadata-insight-id', help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--opsi-private-endpoint-id', help=u"""Unique Operations Insights PrivateEndpoint identifier""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsightsCollection'})
@cli_util.wrap_exceptions
def list_database_insights(ctx, from_json, all_pages, page_size, compartment_id, enterprise_manager_bridge_id, id, status, lifecycle_state, database_type, database_id, fields, limit, page, sort_order, sort_by, exadata_insight_id, compartment_id_in_subtree, opsi_private_endpoint_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if enterprise_manager_bridge_id is not None:
        kwargs['enterprise_manager_bridge_id'] = enterprise_manager_bridge_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if exadata_insight_id is not None:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if opsi_private_endpoint_id is not None:
        kwargs['opsi_private_endpoint_id'] = opsi_private_endpoint_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_insights,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_insights,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_database_insights(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.list_enterprise_manager_bridges.command_name', 'list'), help=u"""Gets a list of Operations Insights Enterprise Manager bridges. Either compartmentId or id must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of bridges in that compartment and in all sub-compartments will be returned. \n[Command Reference](listEnterpriseManagerBridges)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'EnterpriseManagerBridgeCollection'})
@cli_util.wrap_exceptions
def list_enterprise_manager_bridges(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, lifecycle_state, limit, page, sort_order, sort_by, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_enterprise_manager_bridges,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_enterprise_manager_bridges,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_enterprise_manager_bridges(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.list_exadata_configurations.command_name', 'list-exadata-configurations'), help=u"""Gets a list of exadata insight configurations. Either compartmentId or exadataInsightsId query parameter must be specified. \n[Command Reference](listExadataConfigurations)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["exadataName", "exadataDisplayName", "exadataType"]), help=u"""Exadata configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'ExadataConfigurationCollection'})
@cli_util.wrap_exceptions
def list_exadata_configurations(ctx, from_json, all_pages, page_size, compartment_id, exadata_insight_id, exadata_type, limit, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_exadata_configurations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_exadata_configurations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_exadata_configurations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.list_exadata_insights.command_name', 'list'), help=u"""Gets a list of Exadata insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of Exadata insights in that compartment and in all sub-compartments will be returned. \n[Command Reference](listExadataInsights)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of Exadata insight resource [OCIDs].""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["DISABLED", "ENABLED", "TERMINATED"]), multiple=True, help=u"""Resource Status""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "exadataName"]), help=u"""Exadata insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified. Default order for timeCreated is descending. Default order for exadataName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'ExadataInsightSummaryCollection'})
@cli_util.wrap_exceptions
def list_exadata_insights(ctx, from_json, all_pages, page_size, compartment_id, enterprise_manager_bridge_id, id, status, lifecycle_state, exadata_type, limit, page, sort_order, sort_by, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if enterprise_manager_bridge_id is not None:
        kwargs['enterprise_manager_bridge_id'] = enterprise_manager_bridge_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_exadata_insights,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_exadata_insights,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_exadata_insights(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.list_host_configurations.command_name', 'list-host-configurations'), help=u"""Gets a list of host insight configurations based on the query parameters specified. Either compartmentId or hostInsightId query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of host insight configurations in that compartment and in all sub-compartments will be returned. \n[Command Reference](listHostConfigurations)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["hostName", "platformType"]), help=u"""Host configuration list sort options.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'HostConfigurationCollection'})
@cli_util.wrap_exceptions
def list_host_configurations(ctx, from_json, all_pages, page_size, compartment_id, enterprise_manager_bridge_id, id, exadata_insight_id, platform_type, limit, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if enterprise_manager_bridge_id is not None:
        kwargs['enterprise_manager_bridge_id'] = enterprise_manager_bridge_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_host_configurations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_host_configurations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_host_configurations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.list_host_insights.command_name', 'list'), help=u"""Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. When both compartmentId and compartmentIdInSubtree are specified, a list of host insights in that compartment and in all sub-compartments will be returned. \n[Command Reference](listHostInsights)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["DISABLED", "ENABLED", "TERMINATED"]), multiple=True, help=u"""Resource Status""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--host-type', multiple=True, help=u"""Filter by one or more host types. Possible value is EXTERNAL-HOST.""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["hostName", "hostType"]), help=u"""Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--exadata-insight-id', help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'HostInsightSummaryCollection'})
@cli_util.wrap_exceptions
def list_host_insights(ctx, from_json, all_pages, page_size, compartment_id, id, status, lifecycle_state, host_type, platform_type, limit, page, sort_order, sort_by, enterprise_manager_bridge_id, exadata_insight_id, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if host_type is not None and len(host_type) > 0:
        kwargs['host_type'] = host_type
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if enterprise_manager_bridge_id is not None:
        kwargs['enterprise_manager_bridge_id'] = enterprise_manager_bridge_id
    if exadata_insight_id is not None:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_host_insights,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_host_insights,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_host_insights(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.list_hosted_entities.command_name', 'list-hosted-entities'), help=u"""Get a list of hosted entities details. \n[Command Reference](listHostedEntities)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', required=True, help=u"""Required [OCID] of the host insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--exadata-insight-id', help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["entityName", "entityType"]), help=u"""Hosted entity list sort options.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'HostedEntityCollection'})
@cli_util.wrap_exceptions
def list_hosted_entities(ctx, from_json, all_pages, page_size, compartment_id, id, analysis_time_interval, time_interval_start, time_interval_end, platform_type, exadata_insight_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if exadata_insight_id is not None:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_hosted_entities,
            compartment_id=compartment_id,
            id=id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_hosted_entities,
            limit,
            page_size,
            compartment_id=compartment_id,
            id=id,
            **kwargs
        )
    else:
        result = client.list_hosted_entities(
            compartment_id=compartment_id,
            id=id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.list_importable_agent_entities.command_name', 'list-importable-agent-entities'), help=u"""Gets a list of agent entities available to add a new hostInsight.  An agent entity is \"available\" and will be shown if all the following conditions are true:    1.  The agent OCID is not already being used for an existing hostInsight.    2.  The agent availabilityStatus = 'ACTIVE'    3.  The agent lifecycleState = 'ACTIVE' \n[Command Reference](listImportableAgentEntities)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["entityName", "entityType"]), help=u"""Hosted entity list sort options.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'ImportableAgentEntitySummaryCollection'})
@cli_util.wrap_exceptions
def list_importable_agent_entities(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_importable_agent_entities,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_importable_agent_entities,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_importable_agent_entities(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.list_importable_enterprise_manager_entities.command_name', 'list-importable-enterprise-manager-entities'), help=u"""Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before. \n[Command Reference](listImportableEnterpriseManagerEntities)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--enterprise-manager-entity-type', multiple=True, help=u"""Filter by one or more Enterprise Manager entity types. Currently, the supported types are \"oracle_pdb\", \"oracle_database\", \"host\", \"oracle_dbmachine\", \"oracle_exa_cloud_service\", and \"oracle_oci_exadata_cloud_service\". If this parameter is not specified, targets of all supported entity types are returned by default.""")
@cli_util.option('--enterprise-manager-identifier', help=u"""Used in combination with enterpriseManagerParentEntityIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular Enterprise Manager parent entity.""")
@cli_util.option('--enterprise-manager-parent-entity-identifier', help=u"""Used in combination with enterpriseManagerIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular  Enterprise Manager parent entity.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'enterprise-manager-entity-type': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'enterprise-manager-entity-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'ImportableEnterpriseManagerEntityCollection'})
@cli_util.wrap_exceptions
def list_importable_enterprise_manager_entities(ctx, from_json, all_pages, page_size, enterprise_manager_bridge_id, limit, page, enterprise_manager_entity_type, enterprise_manager_identifier, enterprise_manager_parent_entity_identifier):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if enterprise_manager_entity_type is not None and len(enterprise_manager_entity_type) > 0:
        kwargs['enterprise_manager_entity_type'] = enterprise_manager_entity_type
    if enterprise_manager_identifier is not None:
        kwargs['enterprise_manager_identifier'] = enterprise_manager_identifier
    if enterprise_manager_parent_entity_identifier is not None:
        kwargs['enterprise_manager_parent_entity_identifier'] = enterprise_manager_parent_entity_identifier
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_importable_enterprise_manager_entities,
            enterprise_manager_bridge_id=enterprise_manager_bridge_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_importable_enterprise_manager_entities,
            limit,
            page_size,
            enterprise_manager_bridge_id=enterprise_manager_bridge_id,
            **kwargs
        )
    else:
        result = client.list_importable_enterprise_manager_entities(
            enterprise_manager_bridge_id=enterprise_manager_bridge_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operations_insights_private_endpoint_collection_group.command(name=cli_util.override('opsi.list_operations_insights_private_endpoints.command_name', 'list-operations-insights-private-endpoints'), help=u"""Gets a list of Operation Insights private endpoints. \n[Command Reference](listOperationsInsightsPrivateEndpoints)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--opsi-private-endpoint-id', help=u"""Unique Operations Insights PrivateEndpoint identifier""")
@cli_util.option('--is-used-for-rac-dbs', type=click.BOOL, help=u"""The option to filter OPSI private endpoints that can used for RAC. Should be used along with vcnId query parameter.""")
@cli_util.option('--vcn-id', help=u"""The [OCID] of the VCN.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "id", "displayName"]), help=u"""The field to sort private endpoints.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsPrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_operations_insights_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, display_name, opsi_private_endpoint_id, is_used_for_rac_dbs, vcn_id, lifecycle_state, limit, page, sort_order, sort_by, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if opsi_private_endpoint_id is not None:
        kwargs['opsi_private_endpoint_id'] = opsi_private_endpoint_id
    if is_used_for_rac_dbs is not None:
        kwargs['is_used_for_rac_dbs'] = is_used_for_rac_dbs
    if vcn_id is not None:
        kwargs['vcn_id'] = vcn_id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operations_insights_private_endpoints,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operations_insights_private_endpoints,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_operations_insights_private_endpoints(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operations_insights_warehouse_users_group.command(name=cli_util.override('opsi.list_operations_insights_warehouse_users.command_name', 'list'), help=u"""Gets a list of Operations Insights Warehouse users. Either compartmentId or id must be specified. All these resources are expected to be in root compartment. \n[Command Reference](listOperationsInsightsWarehouseUsers)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--id', help=u"""Unique Operations Insights Warehouse User identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouseUserSummaryCollection'})
@cli_util.wrap_exceptions
def list_operations_insights_warehouse_users(ctx, from_json, all_pages, page_size, operations_insights_warehouse_id, compartment_id, display_name, id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
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
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operations_insights_warehouse_users,
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operations_insights_warehouse_users,
            limit,
            page_size,
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    else:
        result = client.list_operations_insights_warehouse_users(
            operations_insights_warehouse_id=operations_insights_warehouse_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.list_operations_insights_warehouses.command_name', 'list'), help=u"""Gets a list of Operations Insights warehouses. Either compartmentId or id must be specified. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. \n[Command Reference](listOperationsInsightsWarehouses)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--id', help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'OperationsInsightsWarehouseSummaryCollection'})
@cli_util.wrap_exceptions
def list_operations_insights_warehouses(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
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
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operations_insights_warehouses,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operations_insights_warehouses,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_operations_insights_warehouses(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_plans.command_name', 'list-sql-plans'), help=u"""Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan. Either databaseId or id must be specified. \n[Command Reference](listSqlPlans)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--plan-hash', required=True, multiple=True, help=u"""Unique plan hash for a SQL Plan of a particular SQL Statement. Example: `9820154385`""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'plan-hash': {'module': 'opsi', 'class': 'list[integer]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plan-hash': {'module': 'opsi', 'class': 'list[integer]'}}, output_type={'module': 'opsi', 'class': 'SqlPlanCollection'})
@cli_util.wrap_exceptions
def list_sql_plans(ctx, from_json, all_pages, compartment_id, sql_identifier, plan_hash, database_id, id, page):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_plans,
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            plan_hash=plan_hash,
            **kwargs
        )
    else:
        result = client.list_sql_plans(
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            plan_hash=plan_hash,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_searches.command_name', 'list-sql-searches'), help=u"""Search SQL by SQL Identifier across databases in a compartment and in all sub-compartments if specified. And get the SQL Text and the details of the databases executing the SQL for a given time period. \n[Command Reference](listSqlSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlSearchCollection'})
@cli_util.wrap_exceptions
def list_sql_searches(ctx, from_json, all_pages, compartment_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_searches,
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    else:
        result = client.list_sql_searches(
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.list_sql_texts.command_name', 'list-sql-texts'), help=u"""Query SQL Warehouse to get the full SQL Text for a SQL in a compartment and in all sub-compartments if specified. \n[Command Reference](listSqlTexts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, multiple=True, help=u"""One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the assosicated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database [OCIDs] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlTextCollection'})
@cli_util.wrap_exceptions
def list_sql_texts(ctx, from_json, all_pages, compartment_id, sql_identifier, database_id, id, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_sql_texts,
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    else:
        result = client.list_sql_texts(
            compartment_id=compartment_id,
            sql_identifier=sql_identifier,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_requests_group.command(name=cli_util.override('opsi.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
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


@work_requests_group.command(name=cli_util.override('opsi.list_work_request_logs.command_name', 'list'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
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


@work_requests_group.command(name=cli_util.override('opsi.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. Either compartmentId or id must be specified. Only one of id, resourceId or relatedResourceId can be specified optionally. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--related-resource-id', help=u"""The ID of the related resource for the resource affected by the work request, e.g. the related Exadata Insight OCID of the Database Insight work request""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, page, limit, compartment_id, id, status, resource_id, related_resource_id, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if related_resource_id is not None:
        kwargs['related_resource_id'] = related_resource_id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
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


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.rotate_operations_insights_warehouse_wallet.command_name', 'rotate'), help=u"""Rotate the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed. \n[Command Reference](rotateOperationsInsightsWarehouseWallet)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def rotate_operations_insights_warehouse_wallet(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_id, if_match):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.rotate_operations_insights_warehouse_wallet(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
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


@awr_hubs_group.command(name=cli_util.override('opsi.summarize_awr_sources_summaries.command_name', 'summarize-awr-sources-summaries'), help=u"""Gets a list of summary of AWR Sources. \n[Command Reference](summarizeAwrSourcesSummaries)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--name', help=u"""Name for an Awr source database""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["snapshotsUploaded", "name"]), help=u"""The order in which Awr sources summary records are listed""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SummarizeAwrSourcesSummariesCollection'})
@cli_util.wrap_exceptions
def summarize_awr_sources_summaries(ctx, from_json, awr_hub_id, compartment_id, name, limit, page, sort_by, sort_order):

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_awr_sources_summaries(
        awr_hub_id=awr_hub_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_capacity_trend.command_name', 'summarize-database-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeDatabaseInsightResourceCapacityTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity", "baseCapacity"]), help=u"""Sorts using end timestamp , capacity or baseCapacity""")
@cli_util.option('--tablespace-name', help=u"""Tablespace name for a database""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_capacity_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, cdb_name, utilization_level, page, sort_order, sort_by, tablespace_name, host_name, is_database_instance_level_metrics, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if tablespace_name is not None:
        kwargs['tablespace_name'] = tablespace_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_capacity_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_forecast_trend.command_name', 'summarize-database-insight-resource-forecast-trend'), help=u"""Get Forecast predictions for CPU and Storage resources since a time in the past. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeDatabaseInsightResourceForecastTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--tablespace-name', help=u"""Tablespace name for a database""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_forecast_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, cdb_name, statistic, forecast_days, forecast_model, utilization_level, confidence, page, host_name, tablespace_name, is_database_instance_level_metrics, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if statistic is not None:
        kwargs['statistic'] = statistic
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if forecast_model is not None:
        kwargs['forecast_model'] = forecast_model
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if confidence is not None:
        kwargs['confidence'] = confidence
    if page is not None:
        kwargs['page'] = page
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if tablespace_name is not None:
        kwargs['tablespace_name'] = tablespace_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_forecast_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_statistics.command_name', 'summarize-database-insight-resource-statistics'), help=u"""Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled) for each database filtered by utilization level in a compartment and in all sub-compartments if specified. \n[Command Reference](summarizeDatabaseInsightResourceStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--insight-by', help=u"""Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"]), help=u"""The order in which resource statistics records are listed""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_statistics(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, cdb_name, percentile, insight_by, forecast_days, limit, page, sort_order, sort_by, host_name, is_database_instance_level_metrics, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if percentile is not None:
        kwargs['percentile'] = percentile
    if insight_by is not None:
        kwargs['insight_by'] = insight_by
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage.command_name', 'summarize-database-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeDatabaseInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, host_name, is_database_instance_level_metrics, page, percentile, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage_trend.command_name', 'summarize-database-insight-resource-usage-trend'), help=u"""Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeDatabaseInsightResourceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "usage", "capacity"]), help=u"""Sorts using end timestamp, usage or capacity""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, page, sort_order, sort_by, host_name, is_database_instance_level_metrics, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_utilization_insight.command_name', 'summarize-database-insight-resource-utilization-insight'), help=u"""Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeDatabaseInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--is-database-instance-level-metrics', type=click.BOOL, help=u"""Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied. When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the whole database which contains an instance on this host.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, exadata_insight_id, forecast_days, host_name, is_database_instance_level_metrics, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if is_database_instance_level_metrics is not None:
        kwargs['is_database_instance_level_metrics'] = is_database_instance_level_metrics
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_utilization_insight(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_tablespace_usage_trend.command_name', 'summarize-database-insight-tablespace-usage-trend'), help=u"""Returns response with usage time series data (endTimestamp, usage, capacity) with breakdown by tablespaceName for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. Either databaseId or id must be specified. \n[Command Reference](summarizeDatabaseInsightTablespaceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_tablespace_usage_trend(ctx, from_json, compartment_id, analysis_time_interval, time_interval_start, time_interval_end, database_id, id, page, limit):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_tablespace_usage_trend(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_capacity_trend.command_name', 'summarize-exadata-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system for a resource metric. Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters. Top five resources are returned if total exceeds the limit specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId, cdbName and hostName query parameter applies to ResourceType DATABASE. Valid values for ResourceType HOST are CPU and MEMORY. HostName is returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER. Valid values for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field. \n[Command Reference](summarizeExadataInsightResourceCapacityTrend)""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-insight-id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--host-insight-id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--storage-server-name', multiple=True, help=u"""Optional storage server name on an exadata system.""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "name"]), help=u"""The order in which resource capacity trend records are listed""")
@json_skeleton_utils.get_cli_json_input_option({'database-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'storage-server-name': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'storage-server-name': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceCapacityTrendCollection'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_capacity_trend(ctx, from_json, resource_type, resource_metric, exadata_insight_id, compartment_id, analysis_time_interval, time_interval_start, time_interval_end, database_insight_id, host_insight_id, storage_server_name, exadata_type, cdb_name, host_name, page, limit, sort_order, sort_by):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_insight_id is not None and len(database_insight_id) > 0:
        kwargs['database_insight_id'] = database_insight_id
    if host_insight_id is not None and len(host_insight_id) > 0:
        kwargs['host_insight_id'] = host_insight_id
    if storage_server_name is not None and len(storage_server_name) > 0:
        kwargs['storage_server_name'] = storage_server_name
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_capacity_trend(
        resource_type=resource_type,
        resource_metric=resource_metric,
        exadata_insight_id=exadata_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_capacity_trend_aggregated.command_name', 'summarize-exadata-insight-resource-capacity-trend-aggregated'), help=u"""Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system or fleet aggregation for a resource metric. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. \n[Command Reference](summarizeExadataInsightResourceCapacityTrendAggregated)""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity"]), help=u"""Sorts using end timestamp or capacity.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceCapacityTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_capacity_trend_aggregated(ctx, from_json, resource_type, resource_metric, compartment_id, analysis_time_interval, time_interval_start, time_interval_end, exadata_insight_id, exadata_type, cdb_name, host_name, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_capacity_trend_aggregated(
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_forecast_trend.command_name', 'summarize-exadata-insight-resource-forecast-trend'), help=u"""Get historical usage and forecast predictions for an exadata system with breakdown by databases, hosts or storage servers. Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters. Top five resources are returned if total exceeds the limit specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId , cdbName and hostName query parameter applies to ResourceType DATABASE. Valid values for ResourceType HOST are CPU and MEMORY. HostName s returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER. Valid value for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field. \n[Command Reference](summarizeExadataInsightResourceForecastTrend)""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-insight-id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--host-insight-id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--storage-server-name', multiple=True, help=u"""Optional storage server name on an exadata system.""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-start-day', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "name", "daysToReachCapacity"]), help=u"""The order in which resource Forecast trend records are listed""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'storage-server-name': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'host-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'storage-server-name': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceForecastTrendCollection'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_forecast_trend(ctx, from_json, resource_type, resource_metric, exadata_insight_id, analysis_time_interval, time_interval_start, time_interval_end, database_insight_id, host_insight_id, storage_server_name, exadata_type, statistic, forecast_start_day, forecast_days, forecast_model, cdb_name, host_name, limit, confidence, sort_order, sort_by, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if database_insight_id is not None and len(database_insight_id) > 0:
        kwargs['database_insight_id'] = database_insight_id
    if host_insight_id is not None and len(host_insight_id) > 0:
        kwargs['host_insight_id'] = host_insight_id
    if storage_server_name is not None and len(storage_server_name) > 0:
        kwargs['storage_server_name'] = storage_server_name
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if statistic is not None:
        kwargs['statistic'] = statistic
    if forecast_start_day is not None:
        kwargs['forecast_start_day'] = forecast_start_day
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if forecast_model is not None:
        kwargs['forecast_model'] = forecast_model
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if limit is not None:
        kwargs['limit'] = limit
    if confidence is not None:
        kwargs['confidence'] = confidence
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_forecast_trend(
        resource_type=resource_type,
        resource_metric=resource_metric,
        exadata_insight_id=exadata_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_forecast_trend_aggregated.command_name', 'summarize-exadata-insight-resource-forecast-trend-aggregated'), help=u"""Get aggregated historical usage and forecast predictions for resources. Either compartmentId or exadataInsightsId query parameter must be specified. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. \n[Command Reference](summarizeExadataInsightResourceForecastTrendAggregated)""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-start-day', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_forecast_trend_aggregated(ctx, from_json, resource_type, resource_metric, compartment_id, analysis_time_interval, time_interval_start, time_interval_end, exadata_insight_id, exadata_type, statistic, forecast_start_day, forecast_days, forecast_model, cdb_name, host_name, confidence, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if statistic is not None:
        kwargs['statistic'] = statistic
    if forecast_start_day is not None:
        kwargs['forecast_start_day'] = forecast_start_day
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if forecast_model is not None:
        kwargs['forecast_model'] = forecast_model
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if confidence is not None:
        kwargs['confidence'] = confidence
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_forecast_trend_aggregated(
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_statistics.command_name', 'summarize-exadata-insight-resource-statistics'), help=u"""Lists the Resource statistics (usage, capacity, usage change percent, utilization percent) for each resource based on resourceMetric filtered by utilization level. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS, THROUGHPUT. Valid value for ResourceType DISKGROUP is STORAGE. \n[Command Reference](summarizeExadataInsightResourceStatistics)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent"]), help=u"""The order in which resource statistics records are listed""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_statistics(ctx, from_json, exadata_insight_id, resource_type, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, exadata_type, cdb_name, host_name, percentile, sort_order, sort_by, limit, page):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if percentile is not None:
        kwargs['percentile'] = percentile
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_statistics(
        exadata_insight_id=exadata_insight_id,
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_usage.command_name', 'summarize-exadata-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per resource within the specified time period. For each resource, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. \n[Command Reference](summarizeExadataInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "capacity", "usageChangePercent"]), help=u"""The order in which resource usage summary records are listed""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceUsageCollection'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_usage(ctx, from_json, compartment_id, resource_type, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, exadata_insight_id, exadata_type, cdb_name, host_name, sort_order, sort_by, page, limit, percentile, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if percentile is not None:
        kwargs['percentile'] = percentile
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_usage(
        compartment_id=compartment_id,
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_usage_aggregated.command_name', 'summarize-exadata-insight-resource-usage-aggregated'), help=u"""A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. \n[Command Reference](summarizeExadataInsightResourceUsageAggregated)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_usage_aggregated(ctx, from_json, compartment_id, resource_type, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, exadata_insight_id, exadata_type, cdb_name, host_name, page, percentile, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_usage_aggregated(
        compartment_id=compartment_id,
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_insight_resource_utilization_insight.command_name', 'summarize-exadata-insight-resource-utilization-insight'), help=u"""Gets current utilization, projected utilization and days to reach projectedUtilization for an exadata system over specified time period. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. \n[Command Reference](summarizeExadataInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-type', required=True, help=u"""Filter by resource. Supported values are HOST , STORAGE_SERVER and DATABASE""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--forecast-start-day', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by hostname.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-type': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeExadataInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_exadata_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_type, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, exadata_insight_id, exadata_type, forecast_start_day, forecast_days, cdb_name, host_name, limit, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if forecast_start_day is not None:
        kwargs['forecast_start_day'] = forecast_start_day
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_insight_resource_utilization_insight(
        compartment_id=compartment_id,
        resource_type=resource_type,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@exadata_insights_group.command(name=cli_util.override('opsi.summarize_exadata_members.command_name', 'summarize-exadata-members'), help=u"""Lists the software and hardware inventory of the Exadata System. \n[Command Reference](summarizeExadataMembers)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""[OCID] of exadata insight resource.""")
@cli_util.option('--exadata-type', multiple=True, help=u"""Filter by one or more Exadata types. Possible value are DBMACHINE, EXACS, and EXACC.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "displayName", "entityType"]), help=u"""The order in which exadata member records are listed""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'exadata-type': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'exadata-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'ExadataMemberCollection'})
@cli_util.wrap_exceptions
def summarize_exadata_members(ctx, from_json, exadata_insight_id, exadata_type, sort_order, sort_by, limit, page):

    kwargs = {}
    if exadata_type is not None and len(exadata_type) > 0:
        kwargs['exadata_type'] = exadata_type
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_exadata_members(
        exadata_insight_id=exadata_insight_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_capacity_trend.command_name', 'summarize-host-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeHostInsightResourceCapacityTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity"]), help=u"""Sorts using end timestamp or capacity""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceCapacityTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_capacity_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, utilization_level, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_capacity_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_forecast_trend.command_name', 'summarize-host-insight-resource-forecast-trend'), help=u"""Get Forecast predictions for CPU or memory resources since a time in the past. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeHostInsightResourceForecastTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_forecast_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, statistic, forecast_days, forecast_model, utilization_level, confidence, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if statistic is not None:
        kwargs['statistic'] = statistic
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if forecast_model is not None:
        kwargs['forecast_model'] = forecast_model
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if confidence is not None:
        kwargs['confidence'] = confidence
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_forecast_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_statistics.command_name', 'summarize-host-insight-resource-statistics'), help=u"""Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered by utilization level in a compartment and in all sub-compartments if specified. \n[Command Reference](summarizeHostInsightResourceStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--insight-by', help=u"""Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"]), help=u"""The order in which resource statistics records are listed.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_statistics(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, percentile, insight_by, forecast_days, limit, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if percentile is not None:
        kwargs['percentile'] = percentile
    if insight_by is not None:
        kwargs['insight_by'] = insight_by
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_usage.command_name', 'summarize-host-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per host within the specified time period. For each host, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeHostInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_usage(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, page, percentile, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_usage(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_usage_trend.command_name', 'summarize-host-insight-resource-usage-trend'), help=u"""Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeHostInsightResourceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "usage", "capacity"]), help=u"""Sorts using end timestamp, usage or capacity""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_usage_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, page, sort_order, sort_by, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_usage_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_utilization_insight.command_name', 'summarize-host-insight-resource-utilization-insight'), help=u"""Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments. \n[Command Reference](summarizeHostInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]), multiple=True, help=u"""Filter by one or more platform types. Supported platformType(s) for MACS-managed external host insight: [LINUX]. Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, exadata_insight_id, forecast_days, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if platform_type is not None and len(platform_type) > 0:
        kwargs['platform_type'] = platform_type
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_utilization_insight(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_top_processes_usage_trend.command_name', 'summarize-host-insight-top-processes-usage-trend'), help=u"""Returns response with aggregated time series data (timeIntervalstart, timeIntervalEnd, commandArgs, usageData) for top processes. Data is aggregated for the time period specified and proceses are sorted descendent by the proces metric specified (CPU, MEMORY, VIRTUAL_MEMORY). HostInsight Id and Process metric must be specified \n[Command Reference](summarizeHostInsightTopProcessesUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', required=True, help=u"""Required [OCID] of the host insight resource.""")
@cli_util.option('--resource-metric', required=True, help=u"""Host top processes resource metric sort options. Supported values are CPU, MEMORY, VIIRTUAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightsTopProcessesUsageTrendCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_top_processes_usage_trend(ctx, from_json, compartment_id, id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, page, limit):

    kwargs = {}
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_top_processes_usage_trend(
        compartment_id=compartment_id,
        id=id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.summarize_operations_insights_warehouse_resource_usage.command_name', 'summarize-operations-insights-warehouse-resource-usage'), help=u"""Gets the details of resources used by an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. \n[Command Reference](summarizeOperationsInsightsWarehouseResourceUsage)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SummarizeOperationsInsightsWarehouseResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_operations_insights_warehouse_resource_usage(ctx, from_json, operations_insights_warehouse_id):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_operations_insights_warehouse_resource_usage(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_insights.command_name', 'summarize-sql-insights'), help=u"""Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types in a compartment and in all sub-compartments if specified. \n[Command Reference](summarizeSqlInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--database-time-pct-greater-than', help=u"""Filter sqls by percentage of db time.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlInsightAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_insights(ctx, from_json, compartment_id, database_type, database_id, id, exadata_insight_id, cdb_name, host_name, database_time_pct_greater_than, analysis_time_interval, time_interval_start, time_interval_end, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if database_time_pct_greater_than is not None:
        kwargs['database_time_pct_greater_than'] = database_time_pct_greater_than
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_insights(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_plan_insights.command_name', 'summarize-sql-plan-insights'), help=u"""Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period. Either databaseId or id must be specified. \n[Command Reference](summarizeSqlPlanInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlPlanInsightAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_plan_insights(ctx, from_json, compartment_id, sql_identifier, database_id, id, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_plan_insights(
        compartment_id=compartment_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_response_time_distributions.command_name', 'summarize-sql-response-time-distributions'), help=u"""Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period. Either databaseId or id must be specified. \n[Command Reference](summarizeSqlResponseTimeDistributions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlResponseTimeDistributionAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_response_time_distributions(ctx, from_json, compartment_id, sql_identifier, database_id, id, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_response_time_distributions(
        compartment_id=compartment_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics.command_name', 'summarize-sql-statistics'), help=u"""Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given time period across the given databases or database types in a compartment and in all sub-compartments if specified. \n[Command Reference](summarizeSqlStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB", "COMANAGED-VM-CDB", "COMANAGED-VM-PDB", "COMANAGED-VM-NONCDB", "COMANAGED-BM-CDB", "COMANAGED-BM-PDB", "COMANAGED-BM-NONCDB", "COMANAGED-EXACS-CDB", "COMANAGED-EXACS-PDB", "COMANAGED-EXACS-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs].""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--database-time-pct-greater-than', help=u"""Filter sqls by percentage of db time.""")
@cli_util.option('--sql-identifier', multiple=True, help=u"""One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"]), help=u"""The field to use when sorting SQL statistics. Example: databaseTimeInSec""")
@cli_util.option('--category', type=custom_types.CliCaseInsensitiveChoice(["DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "IMPROVING", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"]), multiple=True, help=u"""Filter sqls by one or more performance categories.""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics(ctx, from_json, compartment_id, database_type, database_id, id, exadata_insight_id, cdb_name, host_name, database_time_pct_greater_than, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, limit, page, sort_order, sort_by, category, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if database_time_pct_greater_than is not None:
        kwargs['database_time_pct_greater_than'] = database_time_pct_greater_than
    if sql_identifier is not None and len(sql_identifier) > 0:
        kwargs['sql_identifier'] = sql_identifier
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if category is not None and len(category) > 0:
        kwargs['category'] = category
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics_time_series.command_name', 'summarize-sql-statistics-time-series'), help=u"""Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period in a compartment and in all sub-compartments if specified. \n[Command Reference](summarizeSqlStatisticsTimeSeries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database [OCIDs] of the database insight resource.""")
@cli_util.option('--exadata-insight-id', multiple=True, help=u"""Optional list of exadata insight resource [OCIDs].""")
@cli_util.option('--cdb-name', multiple=True, help=u"""Filter by one or more cdb name.""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--defined-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned. Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-equals', multiple=True, help=u"""A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned. The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive. Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--defined-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned. Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag) or \"{namespace}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\". Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".""")
@cli_util.option('--freeform-tag-exists', multiple=True, help=u"""A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned. The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive. Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported. Multiple values for different tag names are interpreted as \"AND\".""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""A flag to search all resources within a given compartment and all sub-compartments.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'exadata-insight-id': {'module': 'opsi', 'class': 'list[string]'}, 'cdb-name': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-equals': {'module': 'opsi', 'class': 'list[string]'}, 'defined-tag-exists': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tag-exists': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticsTimeSeriesAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics_time_series(ctx, from_json, compartment_id, sql_identifier, database_id, id, exadata_insight_id, cdb_name, host_name, analysis_time_interval, time_interval_start, time_interval_end, page, defined_tag_equals, freeform_tag_equals, defined_tag_exists, freeform_tag_exists, compartment_id_in_subtree):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if exadata_insight_id is not None and len(exadata_insight_id) > 0:
        kwargs['exadata_insight_id'] = exadata_insight_id
    if cdb_name is not None and len(cdb_name) > 0:
        kwargs['cdb_name'] = cdb_name
    if host_name is not None and len(host_name) > 0:
        kwargs['host_name'] = host_name
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    if defined_tag_equals is not None and len(defined_tag_equals) > 0:
        kwargs['defined_tag_equals'] = defined_tag_equals
    if freeform_tag_equals is not None and len(freeform_tag_equals) > 0:
        kwargs['freeform_tag_equals'] = freeform_tag_equals
    if defined_tag_exists is not None and len(defined_tag_exists) > 0:
        kwargs['defined_tag_exists'] = defined_tag_exists
    if freeform_tag_exists is not None and len(freeform_tag_exists) > 0:
        kwargs['freeform_tag_exists'] = freeform_tag_exists
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics_time_series(
        compartment_id=compartment_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics_time_series_by_plan.command_name', 'summarize-sql-statistics-time-series-by-plan'), help=u"""Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period. Either databaseId or id must be specified. \n[Command Reference](summarizeSqlStatisticsTimeSeriesByPlan)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', help=u"""Optional [OCID] of the associated DBaaS entity.""")
@cli_util.option('--id', help=u"""[OCID] of the database insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlStatisticsTimeSeriesByPlanAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics_time_series_by_plan(ctx, from_json, compartment_id, sql_identifier, database_id, id, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_id is not None:
        kwargs['database_id'] = database_id
    if id is not None:
        kwargs['id'] = id
    if analysis_time_interval is not None:
        kwargs['analysis_time_interval'] = analysis_time_interval
    if time_interval_start is not None:
        kwargs['time_interval_start'] = time_interval_start
    if time_interval_end is not None:
        kwargs['time_interval_end'] = time_interval_end
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics_time_series_by_plan(
        compartment_id=compartment_id,
        sql_identifier=sql_identifier,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@awr_hubs_group.command(name=cli_util.override('opsi.update_awr_hub.command_name', 'update'), help=u"""Updates the configuration of a hub . \n[Command Reference](updateAwrHub)""")
@cli_util.option('--awr-hub-id', required=True, help=u"""Unique Awr Hub identifier""")
@cli_util.option('--display-name', help=u"""User-friedly name of AWR Hub that does not have to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_awr_hub(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, awr_hub_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(awr_hub_id, six.string_types) and len(awr_hub_id.strip()) == 0:
        raise click.UsageError('Parameter --awr-hub-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_awr_hub(
        awr_hub_id=awr_hub_id,
        update_awr_hub_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight.command_name', 'update'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", "PE_COMANAGED_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, entity_source, freeform_tags, defined_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_database_insight(
        database_insight_id=database_insight_id,
        update_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight_update_macs_managed_external_database_insight_details.command_name', 'update-database-insight-update-macs-managed-external-database-insight-details'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_macs_managed_external_database_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'MACS_MANAGED_EXTERNAL_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_database_insight(
        database_insight_id=database_insight_id,
        update_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight_update_em_managed_external_database_insight_details.command_name', 'update-database-insight-update-em-managed-external-database-insight-details'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_em_managed_external_database_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_database_insight(
        database_insight_id=database_insight_id,
        update_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight_update_pe_comanaged_database_insight_details.command_name', 'update-database-insight-update-pe-comanaged-database-insight-details'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_pe_comanaged_database_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'PE_COMANAGED_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_database_insight(
        database_insight_id=database_insight_id,
        update_database_insight_details=_details,
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight_update_autonomous_database_insight_details.command_name', 'update-database-insight-update-autonomous-database-insight-details'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_database_insight_update_autonomous_database_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(database_insight_id, six.string_types) and len(database_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --database-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'AUTONOMOUS_DATABASE'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_database_insight(
        database_insight_id=database_insight_id,
        update_database_insight_details=_details,
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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.update_enterprise_manager_bridge.command_name', 'update'), help=u"""Updates configuration of an Operations Insights Enterprise Manager bridge. \n[Command Reference](updateEnterpriseManagerBridge)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--display-name', help=u"""User-friedly name of Enterprise Manager Bridge that does not have to be unique.""")
@cli_util.option('--description', help=u"""Description of Enterprise Manager Bridge""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_enterprise_manager_bridge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, enterprise_manager_bridge_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_enterprise_manager_bridge(
        enterprise_manager_bridge_id=enterprise_manager_bridge_id,
        update_enterprise_manager_bridge_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.update_exadata_insight.command_name', 'update'), help=u"""Updates configuration of an Exadata insight. \n[Command Reference](updateExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_EXADATA"]), help=u"""Source of the Exadata system.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_exadata_insight(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, entity_source, freeform_tags, defined_tags, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_exadata_insight(
        exadata_insight_id=exadata_insight_id,
        update_exadata_insight_details=_details,
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


@exadata_insights_group.command(name=cli_util.override('opsi.update_exadata_insight_update_em_managed_external_exadata_insight_details.command_name', 'update-exadata-insight-update-em-managed-external-exadata-insight-details'), help=u"""Updates configuration of an Exadata insight. \n[Command Reference](updateExadataInsight)""")
@cli_util.option('--exadata-insight-id', required=True, help=u"""Unique Exadata insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-auto-sync-enabled', type=click.BOOL, help=u"""Set to true to enable automatic enablement and disablement of related targets from Enterprise Manager. New resources (e.g. Database Insights) will be placed in the same compartment as the related Exadata Insight.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_exadata_insight_update_em_managed_external_exadata_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, exadata_insight_id, freeform_tags, defined_tags, is_auto_sync_enabled, if_match):

    if isinstance(exadata_insight_id, six.string_types) and len(exadata_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --exadata-insight-id cannot be whitespace or empty string')
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

    if is_auto_sync_enabled is not None:
        _details['isAutoSyncEnabled'] = is_auto_sync_enabled

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_EXADATA'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_exadata_insight(
        exadata_insight_id=exadata_insight_id,
        update_exadata_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.update_host_insight.command_name', 'update'), help=u"""Updates configuration of a host insight. \n[Command Reference](updateHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, entity_source, freeform_tags, defined_tags, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['entitySource'] = entity_source

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_host_insight(
        host_insight_id=host_insight_id,
        update_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.update_host_insight_update_em_managed_external_host_insight_details.command_name', 'update-host-insight-update-em-managed-external-host-insight-details'), help=u"""Updates configuration of a host insight. \n[Command Reference](updateHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight_update_em_managed_external_host_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'EM_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_host_insight(
        host_insight_id=host_insight_id,
        update_host_insight_details=_details,
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


@host_insights_group.command(name=cli_util.override('opsi.update_host_insight_update_macs_managed_external_host_insight_details.command_name', 'update-host-insight-update-macs-managed-external-host-insight-details'), help=u"""Updates configuration of a host insight. \n[Command Reference](updateHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_host_insight_update_macs_managed_external_host_insight_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, host_insight_id, freeform_tags, defined_tags, if_match):

    if isinstance(host_insight_id, six.string_types) and len(host_insight_id.strip()) == 0:
        raise click.UsageError('Parameter --host-insight-id cannot be whitespace or empty string')
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

    _details['entitySource'] = 'MACS_MANAGED_EXTERNAL_HOST'

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_host_insight(
        host_insight_id=host_insight_id,
        update_host_insight_details=_details,
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


@operations_insights_private_endpoint_group.command(name=cli_util.override('opsi.update_operations_insights_private_endpoint.command_name', 'update'), help=u"""Updates one or more attributes of the specified private endpoint. \n[Command Reference](updateOperationsInsightsPrivateEndpoint)""")
@cli_util.option('--operations-insights-private-endpoint-id', required=True, help=u"""The [OCID] of the Operation Insights private endpoint.""")
@cli_util.option('--display-name', help=u"""The display name of the private endpoint.""")
@cli_util.option('--description', help=u"""The description of the private endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCID] of the network security groups that the Private service accessed the database.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'opsi', 'class': 'list[string]'}, 'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_operations_insights_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_private_endpoint_id, display_name, description, nsg_ids, freeform_tags, defined_tags, if_match):

    if isinstance(operations_insights_private_endpoint_id, six.string_types) and len(operations_insights_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if nsg_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to nsg-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_operations_insights_private_endpoint(
        operations_insights_private_endpoint_id=operations_insights_private_endpoint_id,
        update_operations_insights_private_endpoint_details=_details,
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


@operations_insights_warehouses_group.command(name=cli_util.override('opsi.update_operations_insights_warehouse.command_name', 'update'), help=u"""Updates the configuration of an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment. \n[Command Reference](updateOperationsInsightsWarehouse)""")
@cli_util.option('--operations-insights-warehouse-id', required=True, help=u"""Unique Operations Insights Warehouse identifier""")
@cli_util.option('--display-name', help=u"""User-friedly name of Operations Insights Warehouse that does not have to be unique.""")
@cli_util.option('--cpu-allocated', help=u"""Number of OCPUs allocated to OPSI Warehouse ADW.""")
@cli_util.option('--storage-allocated-in-gbs', help=u"""Storage allocated to OPSI Warehouse ADW.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_operations_insights_warehouse(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_id, display_name, cpu_allocated, storage_allocated_in_gbs, freeform_tags, defined_tags, if_match):

    if isinstance(operations_insights_warehouse_id, six.string_types) and len(operations_insights_warehouse_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-id cannot be whitespace or empty string')
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

    if cpu_allocated is not None:
        _details['cpuAllocated'] = cpu_allocated

    if storage_allocated_in_gbs is not None:
        _details['storageAllocatedInGBs'] = storage_allocated_in_gbs

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_operations_insights_warehouse(
        operations_insights_warehouse_id=operations_insights_warehouse_id,
        update_operations_insights_warehouse_details=_details,
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


@operations_insights_warehouse_users_group.command(name=cli_util.override('opsi.update_operations_insights_warehouse_user.command_name', 'update'), help=u"""Updates the configuration of an Operations Insights Warehouse User. \n[Command Reference](updateOperationsInsightsWarehouseUser)""")
@cli_util.option('--operations-insights-warehouse-user-id', required=True, help=u"""Unique Operations Insights Warehouse User identifier""")
@cli_util.option('--connection-password', help=u"""User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.""")
@cli_util.option('--is-awr-data-access', type=click.BOOL, help=u"""Indicate whether user has access to AWR data.""")
@cli_util.option('--is-em-data-access', type=click.BOOL, help=u"""Indicate whether user has access to EM data.""")
@cli_util.option('--is-opsi-data-access', type=click.BOOL, help=u"""Indicate whether user has access to OPSI data.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_operations_insights_warehouse_user(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, operations_insights_warehouse_user_id, connection_password, is_awr_data_access, is_em_data_access, is_opsi_data_access, freeform_tags, defined_tags, if_match):

    if isinstance(operations_insights_warehouse_user_id, six.string_types) and len(operations_insights_warehouse_user_id.strip()) == 0:
        raise click.UsageError('Parameter --operations-insights-warehouse-user-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if connection_password is not None:
        _details['connectionPassword'] = connection_password

    if is_awr_data_access is not None:
        _details['isAwrDataAccess'] = is_awr_data_access

    if is_em_data_access is not None:
        _details['isEmDataAccess'] = is_em_data_access

    if is_opsi_data_access is not None:
        _details['isOpsiDataAccess'] = is_opsi_data_access

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.update_operations_insights_warehouse_user(
        operations_insights_warehouse_user_id=operations_insights_warehouse_user_id,
        update_operations_insights_warehouse_user_details=_details,
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
