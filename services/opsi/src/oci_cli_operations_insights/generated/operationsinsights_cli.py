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


@click.command(cli_util.override('opsi.database_insights_group.command_name', 'database-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights database-targeted operations.""")
@cli_util.help_option_group
def database_insights_group():
    pass


@click.command(cli_util.override('opsi.host_insights_group.command_name', 'host-insights'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights host related operations.""")
@cli_util.help_option_group
def host_insights_group():
    pass


@click.command(cli_util.override('opsi.work_requests_group.command_name', 'work-requests'), cls=CommandGroupWithAlias, help="""Logical grouping used for Operations Insights Work Request operations.""")
@cli_util.help_option_group
def work_requests_group():
    pass


opsi_root_group.add_command(enterprise_manager_bridges_group)
opsi_root_group.add_command(database_insights_group)
opsi_root_group.add_command(host_insights_group)
opsi_root_group.add_command(work_requests_group)


@database_insights_group.command(name=cli_util.override('opsi.change_database_insight_compartment.command_name', 'change'), help=u"""Moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeDatabaseInsightCompartment)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.change_host_insight_compartment.command_name', 'change'), help=u"""Moves a HostInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeHostInsightCompartment)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.create_database_insight.command_name', 'create'), help=u"""Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](createDatabaseInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of database""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsight'})
@cli_util.wrap_exceptions
def create_database_insight_create_em_managed_external_database_insight_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, enterprise_manager_identifier, enterprise_manager_bridge_id, enterprise_manager_entity_identifier, freeform_tags, defined_tags):

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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.create_enterprise_manager_bridge.command_name', 'create'), help=u"""Create a Enterprise Manager bridge in Operations Insights. \n[Command Reference](createEnterpriseManagerBridge)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier of the Enterprise Manager bridge""")
@cli_util.option('--display-name', required=True, help=u"""User-friedly name of Enterprise Manager Bridge that does not have to be unique.""")
@cli_util.option('--object-storage-bucket-name', required=True, help=u"""Object Storage Bucket Name""")
@cli_util.option('--freeform-tags', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description of Enterprise Manager Bridge""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'opsi', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'opsi', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'opsi', 'class': 'EnterpriseManagerBridge'})
@cli_util.wrap_exceptions
def create_enterprise_manager_bridge(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, object_storage_bucket_name, freeform_tags, defined_tags, description):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['objectStorageBucketName'] = object_storage_bucket_name
    _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)
    _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

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


@host_insights_group.command(name=cli_util.override('opsi.create_host_insight.command_name', 'create'), help=u"""Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](createHostInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier of host""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.delete_database_insight.command_name', 'delete'), help=u"""Deletes a database insight. The database insight will be deleted and cannot be enabled again. \n[Command Reference](deleteDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.delete_host_insight.command_name', 'delete'), help=u"""Deletes a host insight. The host insight will be deleted and cannot be enabled again. \n[Command Reference](deleteHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.disable_database_insight.command_name', 'disable'), help=u"""Disables a database in Operations Insights. Database metric collection and analysis will be stopped. \n[Command Reference](disableDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.disable_host_insight.command_name', 'disable'), help=u"""Disables a host in Operations Insights. Host metric collection and analysis will be stopped. \n[Command Reference](disableHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.enable_database_insight.command_name', 'enable'), help=u"""Enables a database in Operations Insights. Database metric collection and analysis will be started. \n[Command Reference](enableDatabaseInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["EM_MANAGED_EXTERNAL_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.enable_host_insight.command_name', 'enable'), help=u"""Enables a host in Operations Insights. Host metric collection and analysis will be started. \n[Command Reference](enableHostInsight)""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.list_database_insights.command_name', 'list'), help=u"""Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. \n[Command Reference](listDatabaseInsights)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--enterprise-manager-bridge-id', help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["DISABLED", "ENABLED", "TERMINATED"]), multiple=True, help=u"""Resource Status""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"]), multiple=True, help=u"""Specifies the fields to return in a database summary response. By default all fields are returned if omitted.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["databaseName", "databaseDisplayName", "databaseType"]), help=u"""Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'DatabaseInsightsCollection'})
@cli_util.wrap_exceptions
def list_database_insights(ctx, from_json, all_pages, page_size, compartment_id, enterprise_manager_bridge_id, id, status, lifecycle_state, database_type, database_id, fields, limit, page, sort_order, sort_by):

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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.list_enterprise_manager_bridges.command_name', 'list'), help=u"""Gets a list of Operations Insights Enterprise Manager bridges. Either compartmentId or id must be specified. \n[Command Reference](listEnterpriseManagerBridges)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name.""")
@cli_util.option('--id', help=u"""Unique Enterprise Manager bridge identifier""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'EnterpriseManagerBridgeCollection'})
@cli_util.wrap_exceptions
def list_enterprise_manager_bridges(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, lifecycle_state, limit, page, sort_order, sort_by):

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


@host_insights_group.command(name=cli_util.override('opsi.list_host_insights.command_name', 'list'), help=u"""Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified. \n[Command Reference](listHostInsights)""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["DISABLED", "ENABLED", "TERMINATED"]), multiple=True, help=u"""Resource Status""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""Lifecycle states""")
@cli_util.option('--host-type', multiple=True, help=u"""Filter by one or more host types. Possible value is EXTERNAL-HOST.""")
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["hostName", "hostType"]), help=u"""Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-type': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'HostInsightSummaryCollection'})
@cli_util.wrap_exceptions
def list_host_insights(ctx, from_json, all_pages, page_size, compartment_id, id, status, lifecycle_state, host_type, platform_type, limit, page, sort_order, sort_by):

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
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
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
def list_hosted_entities(ctx, from_json, all_pages, page_size, compartment_id, id, analysis_time_interval, time_interval_start, time_interval_end, platform_type, limit, page, sort_order, sort_by):

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


@enterprise_manager_bridges_group.command(name=cli_util.override('opsi.list_importable_enterprise_manager_entities.command_name', 'list-importable-enterprise-manager-entities'), help=u"""Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before. \n[Command Reference](listImportableEnterpriseManagerEntities)""")
@cli_util.option('--enterprise-manager-bridge-id', required=True, help=u"""Unique Enterprise Manager bridge identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'ImportableEnterpriseManagerEntityCollection'})
@cli_util.wrap_exceptions
def list_importable_enterprise_manager_entities(ctx, from_json, all_pages, page_size, enterprise_manager_bridge_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(enterprise_manager_bridge_id, six.string_types) and len(enterprise_manager_bridge_id.strip()) == 0:
        raise click.UsageError('Parameter --enterprise-manager-bridge-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
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


@database_insights_group.command(name=cli_util.override('opsi.list_sql_searches.command_name', 'list-sql-searches'), help=u"""Search SQL by SQL Identifier across databases and get the SQL Text and the details of the databases executing the SQL for a given time period. \n[Command Reference](listSqlSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'SqlSearchCollection'})
@cli_util.wrap_exceptions
def list_sql_searches(ctx, from_json, all_pages, compartment_id, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
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


@database_insights_group.command(name=cli_util.override('opsi.list_sql_texts.command_name', 'list-sql-texts'), help=u"""Query SQL Warehouse to get the full SQL Text for a SQL. \n[Command Reference](listSqlTexts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, multiple=True, help=u"""One or more unique SQL_IDs for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the assosicated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database [OCIDs] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}, 'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlTextCollection'})
@cli_util.wrap_exceptions
def list_sql_texts(ctx, from_json, all_pages, compartment_id, sql_identifier, database_id, id, page):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
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
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestErrorCollection'})
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
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestLogEntryCollection'})
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


@work_requests_group.command(name=cli_util.override('opsi.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'opsi', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
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


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_capacity_trend.command_name', 'summarize-database-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeDatabaseInsightResourceCapacityTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity", "baseCapacity"]), help=u"""Sorts using end timestamp , capacity or baseCapacity""")
@cli_util.option('--tablespace-name', help=u"""Tablespace name for a database""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_capacity_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, utilization_level, page, sort_order, sort_by, tablespace_name, host_name):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_capacity_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_forecast_trend.command_name', 'summarize-database-insight-resource-forecast-trend'), help=u"""Get Forecast predictions for CPU and Storage resources since a time in the past. \n[Command Reference](summarizeDatabaseInsightResourceForecastTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@cli_util.option('--tablespace-name', help=u"""Tablespace name for a database""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_forecast_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, statistic, forecast_days, forecast_model, utilization_level, confidence, page, host_name, tablespace_name):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_forecast_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_statistics.command_name', 'summarize-database-insight-resource-statistics'), help=u"""Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled) for each database filtered by utilization level \n[Command Reference](summarizeDatabaseInsightResourceStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--insight-by', help=u"""Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"]), help=u"""The order in which resource statistics records are listed""")
@cli_util.option('--host-name', multiple=True, help=u"""Filter by one or more hostname.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'host-name': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_statistics(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, percentile, insight_by, forecast_days, limit, page, sort_order, sort_by, host_name):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage.command_name', 'summarize-database-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per database within the specified time period. For each database, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. \n[Command Reference](summarizeDatabaseInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, page, percentile):

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
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_usage_trend.command_name', 'summarize-database-insight-resource-usage-trend'), help=u"""Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeDatabaseInsightResourceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "usage", "capacity"]), help=u"""Sorts using end timestamp, usage or capacity""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_usage_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, page, sort_order, sort_by):

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
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_database_insight_resource_usage_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_database_insight_resource_utilization_insight.command_name', 'summarize-database-insight-resource-utilization-insight'), help=u"""Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. \n[Command Reference](summarizeDatabaseInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by resource metric. Supported values are CPU , STORAGE, MEMORY and IO.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeDatabaseInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_database_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, database_type, database_id, id, forecast_days, page):

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
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if page is not None:
        kwargs['page'] = page
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


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_capacity_trend.command_name', 'summarize-host-insight-resource-capacity-trend'), help=u"""Returns response with time series data (endTimestamp, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeHostInsightResourceCapacityTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "capacity"]), help=u"""Sorts using end timestamp or capacity""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceCapacityTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_capacity_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, utilization_level, page, sort_order, sort_by):

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
    if utilization_level is not None:
        kwargs['utilization_level'] = utilization_level
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_capacity_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_forecast_trend.command_name', 'summarize-host-insight-resource-forecast-trend'), help=u"""Get Forecast predictions for CPU or memory resources since a time in the past. \n[Command Reference](summarizeHostInsightResourceForecastTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--statistic', type=custom_types.CliCaseInsensitiveChoice(["AVG", "MAX"]), help=u"""Choose the type of statistic metric data to be used for forecasting.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--forecast-model', type=custom_types.CliCaseInsensitiveChoice(["LINEAR", "ML_AUTO", "ML_NO_AUTO"]), help=u"""Choose algorithm model for the forecasting. Possible values:   - LINEAR: Uses linear regression algorithm for forecasting.   - ML_AUTO: Automatically detects best algorithm to use for forecasting.   - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.""")
@cli_util.option('--utilization-level', type=custom_types.CliCaseInsensitiveChoice(["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]), help=u"""Filter by utilization level by the following buckets:   - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.   - LOW_UTILIZATION: DBs with utilization lower than 25.   - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.   - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.""")
@cli_util.option('--confidence', type=click.INT, help=u"""This parameter is used to change data's confidence level, this data is ingested by the forecast algorithm. Confidence is the probability of an interval to contain the expected population parameter. Manipulation of this value will lead to different results. If not set, default confidence value is 95%.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceForecastTrendAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_forecast_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, statistic, forecast_days, forecast_model, utilization_level, confidence, page):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_forecast_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_statistics.command_name', 'summarize-host-insight-resource-statistics'), help=u"""Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered by utilization level. \n[Command Reference](summarizeHostInsightResourceStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@cli_util.option('--insight-by', help=u"""Return data of a specific insight Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast, Low Utilization Forecast""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination]. Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"]), help=u"""The order in which resource statistics records are listed.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceStatisticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_statistics(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, percentile, insight_by, forecast_days, limit, page, sort_order, sort_by):

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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_statistics(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_usage.command_name', 'summarize-host-insight-resource-usage'), help=u"""A cumulative distribution function is used to rank the usage data points per host within the specified time period. For each host, the minimum data point with a ranking > the percentile value is included in the summation. Linear regression functions are used to calculate the usage change percentage. \n[Command Reference](summarizeHostInsightResourceUsage)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--percentile', type=click.INT, help=u"""Percentile values of daily usage to be used for computing the aggregate resource usage.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUsageAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_usage(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, page, percentile):

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
    if page is not None:
        kwargs['page'] = page
    if percentile is not None:
        kwargs['percentile'] = percentile
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_usage(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_usage_trend.command_name', 'summarize-host-insight-resource-usage-trend'), help=u"""Returns response with time series data (endTimestamp, usage, capacity) for the time period specified. The maximum time range for analysis is 2 years, hence this is intentionally not paginated. \n[Command Reference](summarizeHostInsightResourceUsageTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["endTimestamp", "usage", "capacity"]), help=u"""Sorts using end timestamp, usage or capacity""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUsageTrendAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_usage_trend(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, page, sort_order, sort_by):

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
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_usage_trend(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@host_insights_group.command(name=cli_util.override('opsi.summarize_host_insight_resource_utilization_insight.command_name', 'summarize-host-insight-resource-utilization-insight'), help=u"""Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period. \n[Command Reference](summarizeHostInsightResourceUtilizationInsight)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--resource-metric', required=True, help=u"""Filter by host resource metric. Supported values are CPU, MEMORY, and LOGICAL_MEMORY.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--platform-type', type=custom_types.CliCaseInsensitiveChoice(["LINUX"]), multiple=True, help=u"""Filter by one or more platform types. Possible value is LINUX.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of host insight resource [OCIDs] of the host insight resource.""")
@cli_util.option('--forecast-days', type=click.INT, help=u"""Number of days used for utilization forecast analysis.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SummarizeHostInsightResourceUtilizationInsightAggregation'})
@cli_util.wrap_exceptions
def summarize_host_insight_resource_utilization_insight(ctx, from_json, compartment_id, resource_metric, analysis_time_interval, time_interval_start, time_interval_end, platform_type, id, forecast_days, page):

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
    if forecast_days is not None:
        kwargs['forecast_days'] = forecast_days
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_host_insight_resource_utilization_insight(
        compartment_id=compartment_id,
        resource_metric=resource_metric,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_insights.command_name', 'summarize-sql-insights'), help=u"""Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given time period across the given databases or database types. \n[Command Reference](summarizeSqlInsights)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
@cli_util.option('--database-time-pct-greater-than', help=u"""Filter sqls by percentage of db time.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlInsightAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_insights(ctx, from_json, compartment_id, database_type, database_id, id, database_time_pct_greater_than, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
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


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics.command_name', 'summarize-sql-statistics'), help=u"""Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given time period across the given databases or database types. \n[Command Reference](summarizeSqlStatistics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]), multiple=True, help=u"""Filter by one or more database type. Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database insight resource [OCIDs] of the database insight resource.""")
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
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}, 'sql-identifier': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics(ctx, from_json, compartment_id, database_type, database_id, id, database_time_pct_greater_than, sql_identifier, analysis_time_interval, time_interval_start, time_interval_end, limit, page, sort_order, sort_by, category):

    kwargs = {}
    if database_type is not None and len(database_type) > 0:
        kwargs['database_type'] = database_type
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
        kwargs['id'] = id
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('opsi', 'operations_insights', ctx)
    result = client.summarize_sql_statistics(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_insights_group.command(name=cli_util.override('opsi.summarize_sql_statistics_time_series.command_name', 'summarize-sql-statistics-time-series'), help=u"""Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period. \n[Command Reference](summarizeSqlStatisticsTimeSeries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--sql-identifier', required=True, help=u"""Unique SQL_ID for a SQL Statement. Example: `6rgjh9bjmy2s7`""")
@cli_util.option('--database-id', multiple=True, help=u"""Optional list of database [OCIDs] of the associated DBaaS entity.""")
@cli_util.option('--id', multiple=True, help=u"""Optional list of database [OCIDs] of the database insight resource.""")
@cli_util.option('--analysis-time-interval', help=u"""Specify time period in ISO 8601 format with respect to current time. Default is last 30 days represented by P30D. If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored. Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).""")
@cli_util.option('--time-interval-start', type=custom_types.CLI_DATETIME, help=u"""Analysis start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). The minimum allowed value is 2 years prior to the current day. timeIntervalStart and timeIntervalEnd parameters are used together. If analysisTimeInterval is specified, this parameter is ignored.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-interval-end', type=custom_types.CLI_DATETIME, help=u"""Analysis end time in UTC in ISO 8601 format(exclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd are used together. If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@json_skeleton_utils.get_cli_json_input_option({'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-id': {'module': 'opsi', 'class': 'list[string]'}, 'id': {'module': 'opsi', 'class': 'list[string]'}}, output_type={'module': 'opsi', 'class': 'SqlStatisticsTimeSeriesAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_sql_statistics_time_series(ctx, from_json, compartment_id, sql_identifier, database_id, id, analysis_time_interval, time_interval_start, time_interval_end, page):

    kwargs = {}
    if database_id is not None and len(database_id) > 0:
        kwargs['database_id'] = database_id
    if id is not None and len(id) > 0:
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight.command_name', 'update'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"]), help=u"""Source of the database entity.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@database_insights_group.command(name=cli_util.override('opsi.update_database_insight_update_autonomous_database_insight_details.command_name', 'update-database-insight-update-autonomous-database-insight-details'), help=u"""Updates configuration of a database insight. \n[Command Reference](updateDatabaseInsight)""")
@cli_util.option('--database-insight-id', required=True, help=u"""Unique database insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.update_host_insight.command_name', 'update'), help=u"""Updates configuration of a host insight. \n[Command Reference](updateHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--entity-source', required=True, type=custom_types.CliCaseInsensitiveChoice(["MACS_MANAGED_EXTERNAL_HOST"]), help=u"""Source of the host entity.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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


@host_insights_group.command(name=cli_util.override('opsi.update_host_insight_update_macs_managed_external_host_insight_details.command_name', 'update-host-insight-update-macs-managed-external-host-insight-details'), help=u"""Updates configuration of a host insight. \n[Command Reference](updateHostInsight)""")
@cli_util.option('--host-insight-id', required=True, help=u"""Unique host insight identifier""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match` parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
