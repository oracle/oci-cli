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


@cli.command(cli_util.override('usage_api.usage_api_root_group.command_name', 'usage-api'), cls=CommandGroupWithAlias, help=cli_util.override('usage_api.usage_api_root_group.help', """Use the Usage API to view your Oracle Cloud usage and costs. The API allows you to request data that meets the specified filter criteria, and to group that data by the dimension of your choosing. The Usage API is used by the Cost Analysis tool in the Console. Also see [Using the Usage API] for more information."""), short_help=cli_util.override('usage_api.usage_api_root_group.short_help', """Usage API"""))
@cli_util.help_option_group
def usage_api_root_group():
    pass


@click.command(cli_util.override('usage_api.schedule_group.command_name', 'schedule'), cls=CommandGroupWithAlias, help="""The schedule.""")
@cli_util.help_option_group
def schedule_group():
    pass


@click.command(cli_util.override('usage_api.usage_summary_group.command_name', 'usage-summary'), cls=CommandGroupWithAlias, help="""The usage store result.""")
@cli_util.help_option_group
def usage_summary_group():
    pass


@click.command(cli_util.override('usage_api.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""A configuration.""")
@cli_util.help_option_group
def configuration_group():
    pass


@click.command(cli_util.override('usage_api.query_group.command_name', 'query'), cls=CommandGroupWithAlias, help="""The query to filter and aggregate.""")
@cli_util.help_option_group
def query_group():
    pass


@click.command(cli_util.override('usage_api.scheduled_run_group.command_name', 'scheduled-run'), cls=CommandGroupWithAlias, help="""The saved schedule run.""")
@cli_util.help_option_group
def scheduled_run_group():
    pass


@click.command(cli_util.override('usage_api.custom_table_group.command_name', 'custom-table'), cls=CommandGroupWithAlias, help="""The saved custom table.""")
@cli_util.help_option_group
def custom_table_group():
    pass


usage_api_root_group.add_command(schedule_group)
usage_api_root_group.add_command(usage_summary_group)
usage_api_root_group.add_command(configuration_group)
usage_api_root_group.add_command(query_group)
usage_api_root_group.add_command(scheduled_run_group)
usage_api_root_group.add_command(custom_table_group)


@custom_table_group.command(name=cli_util.override('usage_api.create_custom_table.command_name', 'create'), help=u"""Returns the created custom table. \n[Command Reference](createCustomTable)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--saved-report-id', required=True, help=u"""The associated saved report OCID.""")
@cli_util.option('--saved-custom-table', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'saved-custom-table': {'module': 'usage_api', 'class': 'SavedCustomTable'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'saved-custom-table': {'module': 'usage_api', 'class': 'SavedCustomTable'}}, output_type={'module': 'usage_api', 'class': 'CustomTable'})
@cli_util.wrap_exceptions
def create_custom_table(ctx, from_json, compartment_id, saved_report_id, saved_custom_table):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['savedReportId'] = saved_report_id
    _details['savedCustomTable'] = cli_util.parse_json_parameter("saved_custom_table", saved_custom_table)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.create_custom_table(
        create_custom_table_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.create_query.command_name', 'create'), help=u"""Returns the created query. \n[Command Reference](createQuery)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID.""")
@cli_util.option('--query-definition', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def create_query(ctx, from_json, compartment_id, query_definition):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['queryDefinition'] = cli_util.parse_json_parameter("query_definition", query_definition)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.create_query(
        create_query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schedule_group.command(name=cli_util.override('usage_api.create_schedule.command_name', 'create'), help=u"""Returns the created schedule. \n[Command Reference](createSchedule)""")
@cli_util.option('--name', required=True, help=u"""The unique name of the schedule created by the user""")
@cli_util.option('--compartment-id', required=True, help=u"""The tenancy of the customer""")
@cli_util.option('--result-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schedule-recurrences', required=True, help=u"""In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10 Describes the frequency of when the schedule will be run""")
@cli_util.option('--time-scheduled', required=True, type=custom_types.CLI_DATETIME, help=u"""The date and time of the first time job execution""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--query-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'result-location': {'module': 'usage_api', 'class': 'ResultLocation'}, 'query-properties': {'module': 'usage_api', 'class': 'QueryProperties'}, 'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'result-location': {'module': 'usage_api', 'class': 'ResultLocation'}, 'query-properties': {'module': 'usage_api', 'class': 'QueryProperties'}, 'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'usage_api', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, result_location, schedule_recurrences, time_scheduled, query_properties, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['resultLocation'] = cli_util.parse_json_parameter("result_location", result_location)
    _details['scheduleRecurrences'] = schedule_recurrences
    _details['timeScheduled'] = time_scheduled
    _details['queryProperties'] = cli_util.parse_json_parameter("query_properties", query_properties)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.create_schedule(
        create_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_schedule') and callable(getattr(client, 'get_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@schedule_group.command(name=cli_util.override('usage_api.create_schedule_object_storage_location.command_name', 'create-schedule-object-storage-location'), help=u"""Returns the created schedule. \n[Command Reference](createSchedule)""")
@cli_util.option('--name', required=True, help=u"""The unique name of the schedule created by the user""")
@cli_util.option('--compartment-id', required=True, help=u"""The tenancy of the customer""")
@cli_util.option('--schedule-recurrences', required=True, help=u"""In x-obmcs-recurring-time format shown here: https://datatracker.ietf.org/doc/html/rfc5545#section-3.3.10 Describes the frequency of when the schedule will be run""")
@cli_util.option('--time-scheduled', required=True, type=custom_types.CLI_DATETIME, help=u"""The date and time of the first time job execution""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--query-properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--result-location-region', required=True, help=u"""The destination Object Store Region specified by customer""")
@cli_util.option('--result-location-namespace', required=True, help=u"""The namespace needed to determine object storage bucket.""")
@cli_util.option('--result-location-bucket-name', required=True, help=u"""The bucket name where usage/cost CSVs will be uploaded""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'query-properties': {'module': 'usage_api', 'class': 'QueryProperties'}, 'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-properties': {'module': 'usage_api', 'class': 'QueryProperties'}, 'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'usage_api', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def create_schedule_object_storage_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, schedule_recurrences, time_scheduled, query_properties, result_location_region, result_location_namespace, result_location_bucket_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resultLocation'] = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['scheduleRecurrences'] = schedule_recurrences
    _details['timeScheduled'] = time_scheduled
    _details['queryProperties'] = cli_util.parse_json_parameter("query_properties", query_properties)
    _details['resultLocation']['region'] = result_location_region
    _details['resultLocation']['namespace'] = result_location_namespace
    _details['resultLocation']['bucketName'] = result_location_bucket_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['resultLocation']['locationType'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.create_schedule(
        create_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_schedule') and callable(getattr(client, 'get_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@custom_table_group.command(name=cli_util.override('usage_api.delete_custom_table.command_name', 'delete'), help=u"""Delete a saved custom table by the OCID. \n[Command Reference](deleteCustomTable)""")
@cli_util.option('--custom-table-id', required=True, help=u"""The custom table unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_custom_table(ctx, from_json, custom_table_id, if_match):

    if isinstance(custom_table_id, six.string_types) and len(custom_table_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-table-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.delete_custom_table(
        custom_table_id=custom_table_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.delete_query.command_name', 'delete'), help=u"""Delete a saved query by the OCID. \n[Command Reference](deleteQuery)""")
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_query(ctx, from_json, query_id, if_match):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.delete_query(
        query_id=query_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schedule_group.command(name=cli_util.override('usage_api.delete_schedule.command_name', 'delete'), help=u"""Delete a saved scheduled report by the OCID. \n[Command Reference](deleteSchedule)""")
@cli_util.option('--schedule-id', required=True, help=u"""The schedule unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_schedule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, schedule_id, if_match):

    if isinstance(schedule_id, six.string_types) and len(schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --schedule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.delete_schedule(
        schedule_id=schedule_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_schedule') and callable(getattr(client, 'get_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_schedule(schedule_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@custom_table_group.command(name=cli_util.override('usage_api.get_custom_table.command_name', 'get'), help=u"""Returns the saved custom table. \n[Command Reference](getCustomTable)""")
@cli_util.option('--custom-table-id', required=True, help=u"""The custom table unique OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'CustomTable'})
@cli_util.wrap_exceptions
def get_custom_table(ctx, from_json, custom_table_id):

    if isinstance(custom_table_id, six.string_types) and len(custom_table_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-table-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.get_custom_table(
        custom_table_id=custom_table_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.get_query.command_name', 'get'), help=u"""Returns the saved query. \n[Command Reference](getQuery)""")
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def get_query(ctx, from_json, query_id):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.get_query(
        query_id=query_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schedule_group.command(name=cli_util.override('usage_api.get_schedule.command_name', 'get'), help=u"""Returns the saved schedule. \n[Command Reference](getSchedule)""")
@cli_util.option('--schedule-id', required=True, help=u"""The schedule unique OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def get_schedule(ctx, from_json, schedule_id):

    if isinstance(schedule_id, six.string_types) and len(schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --schedule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.get_schedule(
        schedule_id=schedule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_run_group.command(name=cli_util.override('usage_api.get_scheduled_run.command_name', 'get'), help=u"""Returns the saved schedule run. \n[Command Reference](getScheduledRun)""")
@cli_util.option('--scheduled-run-id', required=True, help=u"""The scheduledRun unique OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'ScheduledRun'})
@cli_util.wrap_exceptions
def get_scheduled_run(ctx, from_json, scheduled_run_id):

    if isinstance(scheduled_run_id, six.string_types) and len(scheduled_run_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-run-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.get_scheduled_run(
        scheduled_run_id=scheduled_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_table_group.command(name=cli_util.override('usage_api.list_custom_tables.command_name', 'list'), help=u"""Returns the saved custom table list. \n[Command Reference](listCustomTables)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment ID in which to list resources.""")
@cli_util.option('--saved-report-id', required=True, help=u"""The saved report ID in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName"]), help=u"""The field to sort by. If not specified, the default is displayName.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'CustomTableCollection'})
@cli_util.wrap_exceptions
def list_custom_tables(ctx, from_json, all_pages, page_size, compartment_id, saved_report_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

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
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_custom_tables,
            compartment_id=compartment_id,
            saved_report_id=saved_report_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_custom_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            saved_report_id=saved_report_id,
            **kwargs
        )
    else:
        result = client.list_custom_tables(
            compartment_id=compartment_id,
            saved_report_id=saved_report_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.list_queries.command_name', 'list'), help=u"""Returns the saved query list. \n[Command Reference](listQueries)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment ID in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName"]), help=u"""The field to sort by. If not specified, the default is displayName.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'QueryCollection'})
@cli_util.wrap_exceptions
def list_queries(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

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
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_queries,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_queries,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_queries(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@scheduled_run_group.command(name=cli_util.override('usage_api.list_scheduled_runs.command_name', 'list'), help=u"""Returns schedule history list. \n[Command Reference](listScheduledRuns)""")
@cli_util.option('--schedule-id', required=True, help=u"""The unique ID of a schedule.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. If not specified, the default is timeCreated.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'ScheduledRunCollection'})
@cli_util.wrap_exceptions
def list_scheduled_runs(ctx, from_json, all_pages, page_size, schedule_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

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
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scheduled_runs,
            schedule_id=schedule_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scheduled_runs,
            limit,
            page_size,
            schedule_id=schedule_id,
            **kwargs
        )
    else:
        result = client.list_scheduled_runs(
            schedule_id=schedule_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@schedule_group.command(name=cli_util.override('usage_api.list_schedules.command_name', 'list'), help=u"""Returns the saved schedule list. \n[Command Reference](listSchedules)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment ID in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "timeCreated"]), help=u"""The field to sort by. If not specified, the default is timeCreated.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--name', help=u"""Query parameter for filtering by name""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'ScheduleCollection'})
@cli_util.wrap_exceptions
def list_schedules(ctx, from_json, all_pages, page_size, compartment_id, page, limit, sort_by, sort_order, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_schedules,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_schedules,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_schedules(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('usage_api.request_summarized_configurations.command_name', 'request-summarized'), help=u"""Returns the configurations list for the UI drop-down list. \n[Command Reference](requestSummarizedConfigurations)""")
@cli_util.option('--tenant-id', required=True, help=u"""tenant id""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage_api', 'class': 'ConfigurationAggregation'})
@cli_util.wrap_exceptions
def request_summarized_configurations(ctx, from_json, tenant_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.request_summarized_configurations(
        tenant_id=tenant_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@usage_summary_group.command(name=cli_util.override('usage_api.request_summarized_usages.command_name', 'request-summarized-usages'), help=u"""Returns usage for the given account. \n[Command Reference](requestSummarizedUsages)""")
@cli_util.option('--tenant-id', required=True, help=u"""Tenant ID.""")
@cli_util.option('--time-usage-started', required=True, type=custom_types.CLI_DATETIME, help=u"""The usage start time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-usage-ended', required=True, type=custom_types.CLI_DATETIME, help=u"""The usage end time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--granularity', required=True, type=custom_types.CliCaseInsensitiveChoice(["HOURLY", "DAILY", "MONTHLY", "TOTAL"]), help=u"""The usage granularity. HOURLY - Hourly data aggregation. DAILY - Daily data aggregation. MONTHLY - Monthly data aggregation. TOTAL - Not yet supported.""")
@cli_util.option('--is-aggregate-by-time', type=click.BOOL, help=u"""Whether aggregated by time. If isAggregateByTime is true, all usage/cost over the query time period will be added up.""")
@cli_util.option('--forecast', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-type', type=custom_types.CliCaseInsensitiveChoice(["USAGE", "COST", "CREDIT", "EXPIREDCREDIT", "ALLCREDIT"]), help=u"""The query usage type. COST by default if it is missing. Usage - Query the usage data. Cost - Query the cost/billing data. Credit - Query the credit adjustments data. ExpiredCredit - Query the expired credits data. AllCredit - Query the credit adjustments and expired credit.""")
@cli_util.option('--group-by', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Aggregate the result by. example:   `[\"tagNamespace\", \"tagKey\", \"tagValue\", \"service\", \"skuName\", \"skuPartNumber\", \"unit\",     \"compartmentName\", \"compartmentPath\", \"compartmentId\", \"platform\", \"region\", \"logicalAd\",     \"resourceId\", \"tenantId\", \"tenantName\"]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--group-by-tag', type=custom_types.CLI_COMPLEX_TYPE, help=u"""GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list. For example:   `[{\"namespace\":\"oracle\", \"key\":\"createdBy\"]`

This option is a JSON list with items of type Tag.  For documentation on Tag please see our API reference: https://docs.cloud.oracle.com/api/#/en/usageapi/20200107/datatypes/Tag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-depth', type=click.FLOAT, help=u"""The compartment depth level.""")
@cli_util.option('--filter', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximumimum number of items to return.""")
@json_skeleton_utils.get_cli_json_input_option({'forecast': {'module': 'usage_api', 'class': 'Forecast'}, 'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'group-by-tag': {'module': 'usage_api', 'class': 'list[Tag]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'forecast': {'module': 'usage_api', 'class': 'Forecast'}, 'group-by': {'module': 'usage_api', 'class': 'list[string]'}, 'group-by-tag': {'module': 'usage_api', 'class': 'list[Tag]'}, 'filter': {'module': 'usage_api', 'class': 'Filter'}}, output_type={'module': 'usage_api', 'class': 'UsageAggregation'})
@cli_util.wrap_exceptions
def request_summarized_usages(ctx, from_json, tenant_id, time_usage_started, time_usage_ended, granularity, is_aggregate_by_time, forecast, query_type, group_by, group_by_tag, compartment_depth, filter, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['tenantId'] = tenant_id
    _details['timeUsageStarted'] = time_usage_started
    _details['timeUsageEnded'] = time_usage_ended
    _details['granularity'] = granularity

    if is_aggregate_by_time is not None:
        _details['isAggregateByTime'] = is_aggregate_by_time

    if forecast is not None:
        _details['forecast'] = cli_util.parse_json_parameter("forecast", forecast)

    if query_type is not None:
        _details['queryType'] = query_type

    if group_by is not None:
        _details['groupBy'] = cli_util.parse_json_parameter("group_by", group_by)

    if group_by_tag is not None:
        _details['groupByTag'] = cli_util.parse_json_parameter("group_by_tag", group_by_tag)

    if compartment_depth is not None:
        _details['compartmentDepth'] = compartment_depth

    if filter is not None:
        _details['filter'] = cli_util.parse_json_parameter("filter", filter)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.request_summarized_usages(
        request_summarized_usages_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_table_group.command(name=cli_util.override('usage_api.update_custom_table.command_name', 'update'), help=u"""Update a saved custom table by table id. \n[Command Reference](updateCustomTable)""")
@cli_util.option('--saved-custom-table', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-table-id', required=True, help=u"""The custom table unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'saved-custom-table': {'module': 'usage_api', 'class': 'SavedCustomTable'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'saved-custom-table': {'module': 'usage_api', 'class': 'SavedCustomTable'}}, output_type={'module': 'usage_api', 'class': 'CustomTable'})
@cli_util.wrap_exceptions
def update_custom_table(ctx, from_json, force, saved_custom_table, custom_table_id, if_match):

    if isinstance(custom_table_id, six.string_types) and len(custom_table_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-table-id cannot be whitespace or empty string')
    if not force:
        if saved_custom_table:
            if not click.confirm("WARNING: Updates to saved-custom-table will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['savedCustomTable'] = cli_util.parse_json_parameter("saved_custom_table", saved_custom_table)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.update_custom_table(
        custom_table_id=custom_table_id,
        update_custom_table_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_group.command(name=cli_util.override('usage_api.update_query.command_name', 'update'), help=u"""Update a saved query by the OCID. \n[Command Reference](updateQuery)""")
@cli_util.option('--query-definition', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--query-id', required=True, help=u"""The query unique OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'query-definition': {'module': 'usage_api', 'class': 'QueryDefinition'}}, output_type={'module': 'usage_api', 'class': 'Query'})
@cli_util.wrap_exceptions
def update_query(ctx, from_json, force, query_definition, query_id, if_match):

    if isinstance(query_id, six.string_types) and len(query_id.strip()) == 0:
        raise click.UsageError('Parameter --query-id cannot be whitespace or empty string')
    if not force:
        if query_definition:
            if not click.confirm("WARNING: Updates to query-definition will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['queryDefinition'] = cli_util.parse_json_parameter("query_definition", query_definition)

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.update_query(
        query_id=query_id,
        update_query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schedule_group.command(name=cli_util.override('usage_api.update_schedule.command_name', 'update'), help=u"""Update a saved schedule \n[Command Reference](updateSchedule)""")
@cli_util.option('--schedule-id', required=True, help=u"""The schedule unique OCID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'usage_api', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'usage_api', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'usage_api', 'class': 'Schedule'})
@cli_util.wrap_exceptions
def update_schedule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, schedule_id, freeform_tags, defined_tags, if_match):

    if isinstance(schedule_id, six.string_types) and len(schedule_id.strip()) == 0:
        raise click.UsageError('Parameter --schedule-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('usage_api', 'usageapi', ctx)
    result = client.update_schedule(
        schedule_id=schedule_id,
        update_schedule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_schedule') and callable(getattr(client, 'get_schedule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_schedule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
