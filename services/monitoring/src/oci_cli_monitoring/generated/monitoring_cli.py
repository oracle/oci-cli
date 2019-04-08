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


@cli.command(cli_util.override('monitoring_root_group.command_name', 'monitoring'), cls=CommandGroupWithAlias, help=cli_util.override('monitoring_root_group.help', """Use the Monitoring API to manage metric queries and alarms for assessing the health, capacity, and performance of your cloud resources.
For information about monitoring, see [Monitoring Overview](/iaas/Content/Monitoring/Concepts/monitoringoverview.htm).
"""), short_help=cli_util.override('monitoring_root_group.short_help', """Monitoring API"""))
@cli_util.help_option_group
def monitoring_root_group():
    pass


@click.command(cli_util.override('metric_data_group.command_name', 'metric-data'), cls=CommandGroupWithAlias, help="""The set of aggregated data returned for a metric. For information about metrics, see [Metrics Overview].""")
@cli_util.help_option_group
def metric_data_group():
    pass


@click.command(cli_util.override('metric_group.command_name', 'metric'), cls=CommandGroupWithAlias, help="""The properties that define a metric. For information about metrics, see [Metrics Overview].""")
@cli_util.help_option_group
def metric_group():
    pass


@click.command(cli_util.override('alarm_status_group.command_name', 'alarm-status'), cls=CommandGroupWithAlias, help="""A summary of properties for the specified alarm and its current evaluation status. For information about alarms, see [Alarms Overview].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def alarm_status_group():
    pass


@click.command(cli_util.override('alarm_history_collection_group.command_name', 'alarm-history-collection'), cls=CommandGroupWithAlias, help="""The configuration details for retrieving alarm history.""")
@cli_util.help_option_group
def alarm_history_collection_group():
    pass


@click.command(cli_util.override('alarm_group.command_name', 'alarm'), cls=CommandGroupWithAlias, help="""The properties that define an alarm. For information about alarms, see [Alarms Overview].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about endpoints and signing API requests, see [About the API]. For information about available SDKs and tools, see [SDKS and Other Tools].""")
@cli_util.help_option_group
def alarm_group():
    pass


@click.command(cli_util.override('suppression_group.command_name', 'suppression'), cls=CommandGroupWithAlias, help="""The configuration details for suppressing an alarm. For information about alarms, see [Alarms Overview].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def suppression_group():
    pass


monitoring_root_group.add_command(metric_data_group)
monitoring_root_group.add_command(metric_group)
monitoring_root_group.add_command(alarm_status_group)
monitoring_root_group.add_command(alarm_history_collection_group)
monitoring_root_group.add_command(alarm_group)
monitoring_root_group.add_command(suppression_group)


@alarm_group.command(name=cli_util.override('create_alarm.command_name', 'create'), help=u"""Creates a new alarm in the specified compartment.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the alarm. It does not have to be unique, and it's changeable. Avoid entering confidential information.

This name is sent as the title for notifications related to this alarm.

Example: `High CPU Utilization`""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the alarm.""")
@cli_util.option('--metric-compartment-id', required=True, help=u"""The [OCID] of the compartment containing the metric being evaluated by the alarm.""")
@cli_util.option('--namespace', required=True, help=u"""The source service or application emitting the metric that is evaluated by the alarm.

Example: `oci_computeagent`""")
@cli_util.option('--query', required=True, help=u"""The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example of threshold alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

  -----

Example of absence alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

  -----""")
@cli_util.option('--severity', required=True, help=u"""The perceived type of response required when the alarm is in the \"FIRING\" state.

Example: `CRITICAL`""")
@cli_util.option('--destinations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [OCIDs] to which the notifications for this alarm will be delivered. An example destination is an OCID for a topic managed by the Oracle Cloud Infrastructure Notification service.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the alarm is enabled.

Example: `true`""")
@cli_util.option('--metric-compartment-id-in-subtree', type=click.BOOL, help=u"""When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false.

Example: `true`""")
@cli_util.option('--resolution', help=u"""The time between calculated aggregation windows for the alarm. Supported value: `1m`""")
@cli_util.option('--pending-duration', help=u"""The period of time that the condition defined in the alarm must persist before the alarm state changes from \"OK\" to \"FIRING\" or vice versa. For example, a value of 5 minutes means that the alarm must persist in breaching the condition for five minutes before the alarm updates its state to \"FIRING\"; likewise, the alarm must persist in not breaching the condition for five minutes before the alarm updates its state to \"OK.\"

The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H` for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

Under the default value of PT1M, the first evaluation that breaches the alarm updates the state to \"FIRING\" and the first evaluation that does not breach the alarm updates the state to \"OK\".

Example: `PT5M`""")
@cli_util.option('--body', help=u"""The human-readable content of the notification delivered. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Avoid entering confidential information.

Example: `High CPU usage alert. Follow runbook instructions for resolution.`""")
@cli_util.option('--repeat-notification-duration', help=u"""The frequency at which notifications are re-submitted, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D.

Default value: null (notifications are not re-submitted).

Example: `PT2H`""")
@cli_util.option('--suppression', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The configuration details for suppressing an alarm.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'monitoring', 'class': 'Alarm'})
@cli_util.wrap_exceptions
def create_alarm(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, metric_compartment_id, namespace, query, severity, destinations, is_enabled, metric_compartment_id_in_subtree, resolution, pending_duration, body, repeat_notification_duration, suppression, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['displayName'] = display_name
    details['compartmentId'] = compartment_id
    details['metricCompartmentId'] = metric_compartment_id
    details['namespace'] = namespace
    details['query'] = query
    details['severity'] = severity
    details['destinations'] = cli_util.parse_json_parameter("destinations", destinations)
    details['isEnabled'] = is_enabled

    if metric_compartment_id_in_subtree is not None:
        details['metricCompartmentIdInSubtree'] = metric_compartment_id_in_subtree

    if resolution is not None:
        details['resolution'] = resolution

    if pending_duration is not None:
        details['pendingDuration'] = pending_duration

    if body is not None:
        details['body'] = body

    if repeat_notification_duration is not None:
        details['repeatNotificationDuration'] = repeat_notification_duration

    if suppression is not None:
        details['suppression'] = cli_util.parse_json_parameter("suppression", suppression)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('monitoring', ctx)
    result = client.create_alarm(
        create_alarm_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_alarm') and callable(getattr(client, 'get_alarm')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_alarm(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@alarm_group.command(name=cli_util.override('delete_alarm.command_name', 'delete'), help=u"""Deletes the specified alarm.""")
@cli_util.option('--alarm-id', required=True, help=u"""The [OCID] of an alarm.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_alarm(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, alarm_id):

    if isinstance(alarm_id, six.string_types) and len(alarm_id.strip()) == 0:
        raise click.UsageError('Parameter --alarm-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    result = client.delete_alarm(
        alarm_id=alarm_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_alarm') and callable(getattr(client, 'get_alarm')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_alarm(alarm_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@alarm_group.command(name=cli_util.override('get_alarm.command_name', 'get'), help=u"""Gets the specified alarm.""")
@cli_util.option('--alarm-id', required=True, help=u"""The [OCID] of an alarm.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'Alarm'})
@cli_util.wrap_exceptions
def get_alarm(ctx, from_json, alarm_id):

    if isinstance(alarm_id, six.string_types) and len(alarm_id.strip()) == 0:
        raise click.UsageError('Parameter --alarm-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    result = client.get_alarm(
        alarm_id=alarm_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@alarm_history_collection_group.command(name=cli_util.override('get_alarm_history.command_name', 'get-alarm-history'), help=u"""Get the history of the specified alarm.""")
@cli_util.option('--alarm-id', required=True, help=u"""The [OCID] of an alarm.""")
@cli_util.option('--alarm-historytype', type=custom_types.CliCaseInsensitiveChoice(["STATE_HISTORY", "STATE_TRANSITION_HISTORY"]), help=u"""The type of history entries to retrieve. State history (STATE_HISTORY) or state transition history (STATE_TRANSITION_HISTORY). If not specified, entries of both types are retrieved.

Example: `STATE_HISTORY`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].

Default: 1000

Example: 500""")
@cli_util.option('--timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter to return only alarm history entries with timestamps occurring on or after the specified date and time. Format defined by RFC3339.

Example: `2019-01-01T01:00:00.789Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timestamp-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter to return only alarm history entries with timestamps occurring before the specified date and time. Format defined by RFC3339.

Example: `2019-01-02T01:00:00.789Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'AlarmHistoryCollection'})
@cli_util.wrap_exceptions
def get_alarm_history(ctx, from_json, alarm_id, alarm_historytype, page, limit, timestamp_greater_than_or_equal_to, timestamp_less_than):

    if isinstance(alarm_id, six.string_types) and len(alarm_id.strip()) == 0:
        raise click.UsageError('Parameter --alarm-id cannot be whitespace or empty string')

    kwargs = {}
    if alarm_historytype is not None:
        kwargs['alarm_historytype'] = alarm_historytype
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if timestamp_greater_than_or_equal_to is not None:
        kwargs['timestamp_greater_than_or_equal_to'] = timestamp_greater_than_or_equal_to
    if timestamp_less_than is not None:
        kwargs['timestamp_less_than'] = timestamp_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    result = client.get_alarm_history(
        alarm_id=alarm_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@alarm_group.command(name=cli_util.override('list_alarms.command_name', 'list'), help=u"""Lists the alarms for the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].

Default: 1000

Example: 500""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), help=u"""A filter to return only alarms that match the given lifecycle state exactly. When not specified, only alarms in the ACTIVE lifecycle state are listed.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "severity"]), help=u"""The field to use when sorting returned alarm definitions. Only one sorting level is provided.

Example: `severity`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC).

Example: `ASC`""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'list[AlarmSummary]'})
@cli_util.wrap_exceptions
def list_alarms(ctx, from_json, all_pages, page_size, compartment_id, page, limit, display_name, lifecycle_state, sort_by, sort_order, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_alarms,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_alarms,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_alarms(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@alarm_status_group.command(name=cli_util.override('list_alarms_status.command_name', 'list-alarms-status'), help=u"""List the status of each alarm in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].

Default: 1000

Example: 500""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly. Use this filter to list an alarm by name. Alternatively, when you know the alarm OCID, use the GetAlarm operation.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "severity"]), help=u"""The field to use when sorting returned alarm definitions. Only one sorting level is provided.

Example: `severity`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned alarm definitions. Ascending (ASC) or descending (DESC).

Example: `ASC`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'list[AlarmStatusSummary]'})
@cli_util.wrap_exceptions
def list_alarms_status(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, page, limit, display_name, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_alarms_status,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_alarms_status,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_alarms_status(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@metric_group.command(name=cli_util.override('list_metrics.command_name', 'list'), help=u"""Returns metric definitions that match the criteria specified in the request. Compartment OCID required. For information about metrics, see [Metrics Overview].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.""")
@cli_util.option('--name', help=u"""The metric name to use when searching for metric definitions.

Example: `CpuUtilization`""")
@cli_util.option('--namespace', help=u"""The source service or application to use when searching for metric definitions.

Example: `oci_computeagent`""")
@cli_util.option('--dimension-filters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Qualifiers that you want to use when searching for metric definitions. Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.

Example: { \"resourceId\": \"<var>&lt;instance_OCID&gt;</var>\" }""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--group-by', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Group metrics by these fields in the response. For example, to list all metric namespaces available in a compartment, groupBy the \"namespace\" field.

Example - group by namespace and resource: `[ \"namespace\", \"resourceId\" ]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAMESPACE", "NAME"]), help=u"""The field to use when sorting returned metric definitions. Only one sorting level is provided.

Example: `NAMESPACE`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use when sorting returned metric definitions. Ascending (ASC) or descending (DESC).

Example: `ASC`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].

Default: 1000

Example: 500""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'dimension-filters': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'group-by': {'module': 'monitoring', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dimension-filters': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'group-by': {'module': 'monitoring', 'class': 'list[string]'}}, output_type={'module': 'monitoring', 'class': 'list[Metric]'})
@cli_util.wrap_exceptions
def list_metrics(ctx, from_json, all_pages, page_size, compartment_id, name, namespace, dimension_filters, group_by, sort_by, sort_order, page, limit, compartment_id_in_subtree):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if name is not None:
        details['name'] = name

    if namespace is not None:
        details['namespace'] = namespace

    if dimension_filters is not None:
        details['dimensionFilters'] = cli_util.parse_json_parameter("dimension_filters", dimension_filters)

    if group_by is not None:
        details['groupBy'] = cli_util.parse_json_parameter("group_by", group_by)

    if sort_by is not None:
        details['sortBy'] = sort_by

    if sort_order is not None:
        details['sortOrder'] = sort_order

    client = cli_util.build_client('monitoring', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_metrics,
            compartment_id=compartment_id,
            list_metrics_details=details,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_metrics,
            limit,
            page_size,
            compartment_id=compartment_id,
            list_metrics_details=details,
            **kwargs
        )
    else:
        result = client.list_metrics(
            compartment_id=compartment_id,
            list_metrics_details=details,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@metric_data_group.command(name=cli_util.override('post_metric_data.command_name', 'post'), help=u"""Publishes raw metric data points to the Monitoring service. For more information about publishing metrics, see [Publishing Custom Metrics].

The endpoints for this operation differ from other Monitoring operations. Replace the string `telemetry` with `telemetry-ingestion` in the endpoint, as in the following example:

https://telemetry-ingestion.eu-frankfurt-1.oraclecloud.com""")
@cli_util.option('--metric-data', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A metric object containing raw metric data points to be posted to the Monitoring service.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--batch-atomicity', type=custom_types.CliCaseInsensitiveChoice(["ATOMIC", "NON_ATOMIC"]), help=u"""Batch atomicity behavior. Requires either partial or full pass of input validation for metric objects in PostMetricData requests. The default value of NON_ATOMIC requires a partial pass: at least one metric object in the request must pass input validation, and any objects that failed validation are identified in the returned summary, along with their error messages. A value of ATOMIC requires a full pass: all metric objects in the request must pass input validation.

Example: `NON_ATOMIC`""")
@json_skeleton_utils.get_cli_json_input_option({'metric-data': {'module': 'monitoring', 'class': 'list[MetricDataDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'metric-data': {'module': 'monitoring', 'class': 'list[MetricDataDetails]'}}, output_type={'module': 'monitoring', 'class': 'PostMetricDataResponseDetails'})
@cli_util.wrap_exceptions
def post_metric_data(ctx, from_json, metric_data, batch_atomicity):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['metricData'] = cli_util.parse_json_parameter("metric_data", metric_data)

    if batch_atomicity is not None:
        details['batchAtomicity'] = batch_atomicity

    client = cli_util.build_client('monitoring', ctx)
    result = client.post_metric_data(
        post_metric_data_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@suppression_group.command(name=cli_util.override('remove_alarm_suppression.command_name', 'remove'), help=u"""Removes any existing suppression for the specified alarm.""")
@cli_util.option('--alarm-id', required=True, help=u"""The [OCID] of an alarm.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_alarm_suppression(ctx, from_json, alarm_id):

    if isinstance(alarm_id, six.string_types) and len(alarm_id.strip()) == 0:
        raise click.UsageError('Parameter --alarm-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('monitoring', ctx)
    result = client.remove_alarm_suppression(
        alarm_id=alarm_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@metric_data_group.command(name=cli_util.override('summarize_metrics_data.command_name', 'summarize-metrics-data'), help=u"""Returns aggregated data that match the criteria specified in the request. Compartment OCID required. For information on metric queries, see [Building Metric Queries].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.""")
@cli_util.option('--namespace', required=True, help=u"""The source service or application to use when searching for metric data points to aggregate.

Example: `oci_computeagent`""")
@cli_util.option('--query', required=True, help=u"""The Monitoring Query Language (MQL) expression to use when searching for metric data points to aggregate. The query must specify a metric, statistic, and interval. Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example: `CpuUtilization[1m].sum()`""")
@cli_util.option('--start-time', type=custom_types.CLI_DATETIME, help=u"""The beginning of the time range to use when searching for metric data points. Format is defined by RFC3339. The response includes metric data points for the startTime. Default value: the timestamp 3 hours before the call was sent.

Example: `2019-02-01T01:02:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--end-time', type=custom_types.CLI_DATETIME, help=u"""The end of the time range to use when searching for metric data points. Format is defined by RFC3339. The response excludes metric data points for the endTime. Default value: the timestamp representing when the call was sent.

Example: `2019-02-01T02:02:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--resolution', help=u"""The time between calculated aggregation windows. Use with the query interval to vary the frequency at which aggregated data points are returned. For example, use a query interval of 5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute frequency. The resolution must be equal or less than the interval in the query. The default resolution is 1m (one minute). Supported values: `1m`-`60m` (also `1h`).

Example: `5m`""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""When true, returns resources from all compartments and subcompartments. The parameter can only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, returns resources from only the compartment specified in compartmentId. Default is false.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'monitoring', 'class': 'list[MetricData]'})
@cli_util.wrap_exceptions
def summarize_metrics_data(ctx, from_json, compartment_id, namespace, query, start_time, end_time, resolution, compartment_id_in_subtree):

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['namespace'] = namespace
    details['query'] = query

    if start_time is not None:
        details['startTime'] = start_time

    if end_time is not None:
        details['endTime'] = end_time

    if resolution is not None:
        details['resolution'] = resolution

    client = cli_util.build_client('monitoring', ctx)
    result = client.summarize_metrics_data(
        compartment_id=compartment_id,
        summarize_metrics_data_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@alarm_group.command(name=cli_util.override('update_alarm.command_name', 'update'), help=u"""Updates the specified alarm.""")
@cli_util.option('--alarm-id', required=True, help=u"""The [OCID] of an alarm.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the alarm. It does not have to be unique, and it's changeable. Avoid entering confidential information.

This name is sent as the title for notifications related to this alarm.

Example: `High CPU Utilization`""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment containing the alarm.""")
@cli_util.option('--metric-compartment-id', help=u"""The [OCID] of the compartment containing the metric being evaluated by the alarm.""")
@cli_util.option('--metric-compartment-id-in-subtree', type=click.BOOL, help=u"""When true, the alarm evaluates metrics from all compartments and subcompartments. The parameter can only be set to true when metricCompartmentId is the tenancy OCID (the tenancy is the root compartment). A true value requires the user to have tenancy-level permissions. If this requirement is not met, then the call is rejected. When false, the alarm evaluates metrics from only the compartment specified in metricCompartmentId. Default is false.

Example: `true`""")
@cli_util.option('--namespace', help=u"""The source service or application emitting the metric that is evaluated by the alarm.

Example: `oci_computeagent`""")
@cli_util.option('--query', help=u"""The Monitoring Query Language (MQL) expression to evaluate for the alarm. The Alarms feature of the Monitoring service interprets results for each returned time series as Boolean values, where zero represents false and a non-zero value represents true. A true value means that the trigger rule condition has been met. The query must specify a metric, statistic, interval, and trigger rule (threshold or absence). Supported values for interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions. Supported grouping functions: `grouping()`, `groupBy()`. For details about Monitoring Query Language (MQL), see [Monitoring Query Language (MQL) Reference]. For available dimensions, review the metric definition for the supported service. See [Supported Services].

Example of threshold alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.groupBy(availabilityDomain).percentile(0.9) > 85

  -----

Example of absence alarm:

  -----

    CpuUtilization[1m]{availabilityDomain=\"cumS:PHX-AD-1\"}.absent()

  -----""")
@cli_util.option('--resolution', help=u"""The time between calculated aggregation windows for the alarm. Supported value: `1m`""")
@cli_util.option('--pending-duration', help=u"""The period of time that the condition defined in the alarm must persist before the alarm state changes from \"OK\" to \"FIRING\" or vice versa. For example, a value of 5 minutes means that the alarm must persist in breaching the condition for five minutes before the alarm updates its state to \"FIRING\"; likewise, the alarm must persist in not breaching the condition for five minutes before the alarm updates its state to \"OK.\"

The duration is specified as a string in ISO 8601 format (`PT10M` for ten minutes or `PT1H` for one hour). Minimum: PT1M. Maximum: PT1H. Default: PT1M.

Under the default value of PT1M, the first evaluation that breaches the alarm updates the state to \"FIRING\" and the first evaluation that does not breach the alarm updates the state to \"OK\".

Example: `PT5M`""")
@cli_util.option('--severity', help=u"""The perceived severity of the alarm with regard to the affected system.

Example: `CRITICAL`""")
@cli_util.option('--body', help=u"""The human-readable content of the notification delivered. Oracle recommends providing guidance to operators for resolving the alarm condition. Consider adding links to standard runbook practices. Avoid entering confidential information.

Example: `High CPU usage alert. Follow runbook instructions for resolution.`""")
@cli_util.option('--destinations', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of [OCIDs] to which the notifications for this alarm will be delivered. An example destination is an OCID for a topic managed by the Oracle Cloud Infrastructure Notification service.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-notification-duration', help=u"""The frequency at which notifications are re-submitted, if the alarm keeps firing without interruption. Format defined by ISO 8601. For example, `PT4H` indicates four hours. Minimum: PT1M. Maximum: P30D.

Default value: null (notifications are not re-submitted).

Example: `PT2H`""")
@cli_util.option('--suppression', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The configuration details for suppressing an alarm.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the alarm is enabled.

Example: `true`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'destinations': {'module': 'monitoring', 'class': 'list[string]'}, 'suppression': {'module': 'monitoring', 'class': 'Suppression'}, 'freeform-tags': {'module': 'monitoring', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'monitoring', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'monitoring', 'class': 'Alarm'})
@cli_util.wrap_exceptions
def update_alarm(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, alarm_id, display_name, compartment_id, metric_compartment_id, metric_compartment_id_in_subtree, namespace, query, resolution, pending_duration, severity, body, destinations, repeat_notification_duration, suppression, is_enabled, freeform_tags, defined_tags):

    if isinstance(alarm_id, six.string_types) and len(alarm_id.strip()) == 0:
        raise click.UsageError('Parameter --alarm-id cannot be whitespace or empty string')
    if not force:
        if destinations or suppression or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to destinations and suppression and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if compartment_id is not None:
        details['compartmentId'] = compartment_id

    if metric_compartment_id is not None:
        details['metricCompartmentId'] = metric_compartment_id

    if metric_compartment_id_in_subtree is not None:
        details['metricCompartmentIdInSubtree'] = metric_compartment_id_in_subtree

    if namespace is not None:
        details['namespace'] = namespace

    if query is not None:
        details['query'] = query

    if resolution is not None:
        details['resolution'] = resolution

    if pending_duration is not None:
        details['pendingDuration'] = pending_duration

    if severity is not None:
        details['severity'] = severity

    if body is not None:
        details['body'] = body

    if destinations is not None:
        details['destinations'] = cli_util.parse_json_parameter("destinations", destinations)

    if repeat_notification_duration is not None:
        details['repeatNotificationDuration'] = repeat_notification_duration

    if suppression is not None:
        details['suppression'] = cli_util.parse_json_parameter("suppression", suppression)

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('monitoring', ctx)
    result = client.update_alarm(
        alarm_id=alarm_id,
        update_alarm_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_alarm') and callable(getattr(client, 'get_alarm')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_alarm(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
