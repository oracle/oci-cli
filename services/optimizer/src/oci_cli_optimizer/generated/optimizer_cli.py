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


@cli.command(cli_util.override('optimizer.optimizer_root_group.command_name', 'optimizer'), cls=CommandGroupWithAlias, help=cli_util.override('optimizer.optimizer_root_group.help', """Use the Cloud Advisor API to find potential inefficiencies in your tenancy and address them.
Cloud Advisor can help you save money, improve performance, strengthen system resilience, and improve security.
For more information, see [Cloud Advisor]."""), short_help=cli_util.override('optimizer.optimizer_root_group.short_help', """Cloud Advisor API"""))
@cli_util.help_option_group
def optimizer_root_group():
    pass


@click.command(cli_util.override('optimizer.queryable_field_summary_group.command_name', 'queryable-field-summary'), cls=CommandGroupWithAlias, help="""An individual field that can be used as part of a query filter.""")
@cli_util.help_option_group
def queryable_field_summary_group():
    pass


@click.command(cli_util.override('optimizer.category_summary_group.command_name', 'category-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the category summary.""")
@cli_util.help_option_group
def category_summary_group():
    pass


@click.command(cli_util.override('optimizer.profile_group.command_name', 'profile'), cls=CommandGroupWithAlias, help="""The metadata associated with the profile.""")
@cli_util.help_option_group
def profile_group():
    pass


@click.command(cli_util.override('optimizer.profile_summary_group.command_name', 'profile-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the profile summary.""")
@cli_util.help_option_group
def profile_summary_group():
    pass


@click.command(cli_util.override('optimizer.recommendation_group.command_name', 'recommendation'), cls=CommandGroupWithAlias, help="""The metadata associated with the recommendation.""")
@cli_util.help_option_group
def recommendation_group():
    pass


@click.command(cli_util.override('optimizer.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""Details about the log entity.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('optimizer.recommendation_summary_group.command_name', 'recommendation-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the recommendation summary.""")
@cli_util.help_option_group
def recommendation_summary_group():
    pass


@click.command(cli_util.override('optimizer.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('optimizer.profile_level_summary_group.command_name', 'profile-level-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the profile level summary.""")
@cli_util.help_option_group
def profile_level_summary_group():
    pass


@click.command(cli_util.override('optimizer.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""Details about errors encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('optimizer.enrollment_status_summary_group.command_name', 'enrollment-status-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the enrollment status summary.""")
@cli_util.help_option_group
def enrollment_status_summary_group():
    pass


@click.command(cli_util.override('optimizer.resource_action_group.command_name', 'resource-action'), cls=CommandGroupWithAlias, help="""The metadata associated with the resource action.""")
@cli_util.help_option_group
def resource_action_group():
    pass


@click.command(cli_util.override('optimizer.history_summary_group.command_name', 'history-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the recommendation history and its related resources.""")
@cli_util.help_option_group
def history_summary_group():
    pass


@click.command(cli_util.override('optimizer.category_group.command_name', 'category'), cls=CommandGroupWithAlias, help="""The metadata associated with the category.""")
@cli_util.help_option_group
def category_group():
    pass


@click.command(cli_util.override('optimizer.enrollment_status_group.command_name', 'enrollment-status'), cls=CommandGroupWithAlias, help="""The metadata associated with the enrollment status.""")
@cli_util.help_option_group
def enrollment_status_group():
    pass


@click.command(cli_util.override('optimizer.recommendation_strategy_summary_group.command_name', 'recommendation-strategy-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the recommendation strategy.""")
@cli_util.help_option_group
def recommendation_strategy_summary_group():
    pass


@click.command(cli_util.override('optimizer.resource_action_summary_group.command_name', 'resource-action-summary'), cls=CommandGroupWithAlias, help="""The metadata associated with the resource action summary.""")
@cli_util.help_option_group
def resource_action_summary_group():
    pass


optimizer_root_group.add_command(queryable_field_summary_group)
optimizer_root_group.add_command(category_summary_group)
optimizer_root_group.add_command(profile_group)
optimizer_root_group.add_command(profile_summary_group)
optimizer_root_group.add_command(recommendation_group)
optimizer_root_group.add_command(work_request_log_entry_group)
optimizer_root_group.add_command(recommendation_summary_group)
optimizer_root_group.add_command(work_request_group)
optimizer_root_group.add_command(profile_level_summary_group)
optimizer_root_group.add_command(work_request_error_group)
optimizer_root_group.add_command(enrollment_status_summary_group)
optimizer_root_group.add_command(resource_action_group)
optimizer_root_group.add_command(history_summary_group)
optimizer_root_group.add_command(category_group)
optimizer_root_group.add_command(enrollment_status_group)
optimizer_root_group.add_command(recommendation_strategy_summary_group)
optimizer_root_group.add_command(resource_action_summary_group)


@recommendation_group.command(name=cli_util.override('optimizer.bulk_apply_recommendations.command_name', 'bulk-apply'), help=u"""Applies the specified recommendations to the resources. \n[Command Reference](bulkApplyRecommendations)""")
@cli_util.option('--recommendation-id', required=True, help=u"""The unique OCID associated with the recommendation.""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""The current status of the recommendation.""")
@cli_util.option('--resource-action-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The unique OCIDs of the resource actions that recommendations are applied to.

This field is deprecated.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The unique resource actions that recommendations are applied to.

This option is a JSON list with items of type BulkApplyResourceAction.  For documentation on BulkApplyResourceAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/optimizer/20200606/datatypes/BulkApplyResourceAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-status-end', type=custom_types.CLI_DATETIME, help=u"""The date and time the current status will change. The format is defined by RFC3339.

For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resource-action-ids': {'module': 'optimizer', 'class': 'list[string]'}, 'actions': {'module': 'optimizer', 'class': 'list[BulkApplyResourceAction]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resource-action-ids': {'module': 'optimizer', 'class': 'list[string]'}, 'actions': {'module': 'optimizer', 'class': 'list[BulkApplyResourceAction]'}})
@cli_util.wrap_exceptions
def bulk_apply_recommendations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recommendation_id, status, resource_action_ids, actions, time_status_end):

    if isinstance(recommendation_id, six.string_types) and len(recommendation_id.strip()) == 0:
        raise click.UsageError('Parameter --recommendation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status

    if resource_action_ids is not None:
        _details['resourceActionIds'] = cli_util.parse_json_parameter("resource_action_ids", resource_action_ids)

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if time_status_end is not None:
        _details['timeStatusEnd'] = time_status_end

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.bulk_apply_recommendations(
        recommendation_id=recommendation_id,
        bulk_apply_recommendations_details=_details,
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


@profile_group.command(name=cli_util.override('optimizer.create_profile.command_name', 'create'), help=u"""Creates a new profile. \n[Command Reference](createProfile)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy. The tenancy is the root compartment.""")
@cli_util.option('--name', required=True, help=u"""The name assigned to the profile. Avoid entering confidential information.""")
@cli_util.option('--description', required=True, help=u"""Text describing the profile. Avoid entering confidential information.""")
@cli_util.option('--levels-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--aggregation-interval-in-days', type=click.INT, help=u"""The time period over which to collect data for the recommendations, measured in number of days.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type, or namespace. For more information, see [Resource Tags]. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-compartments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'optimizer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'optimizer', 'class': 'dict(str, string)'}, 'levels-configuration': {'module': 'optimizer', 'class': 'LevelsConfiguration'}, 'target-compartments': {'module': 'optimizer', 'class': 'TargetCompartments'}, 'target-tags': {'module': 'optimizer', 'class': 'TargetTags'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'optimizer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'optimizer', 'class': 'dict(str, string)'}, 'levels-configuration': {'module': 'optimizer', 'class': 'LevelsConfiguration'}, 'target-compartments': {'module': 'optimizer', 'class': 'TargetCompartments'}, 'target-tags': {'module': 'optimizer', 'class': 'TargetTags'}}, output_type={'module': 'optimizer', 'class': 'Profile'})
@cli_util.wrap_exceptions
def create_profile(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, levels_configuration, aggregation_interval_in_days, defined_tags, freeform_tags, target_compartments, target_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description
    _details['levelsConfiguration'] = cli_util.parse_json_parameter("levels_configuration", levels_configuration)

    if aggregation_interval_in_days is not None:
        _details['aggregationIntervalInDays'] = aggregation_interval_in_days

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if target_compartments is not None:
        _details['targetCompartments'] = cli_util.parse_json_parameter("target_compartments", target_compartments)

    if target_tags is not None:
        _details['targetTags'] = cli_util.parse_json_parameter("target_tags", target_tags)

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.create_profile(
        create_profile_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_profile') and callable(getattr(client, 'get_profile')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_profile(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@profile_group.command(name=cli_util.override('optimizer.delete_profile.command_name', 'delete'), help=u"""Deletes the specified profile. Uses the profile's OCID to determine which profile to delete. \n[Command Reference](deleteProfile)""")
@cli_util.option('--profile-id', required=True, help=u"""The unique OCID of the profile.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_profile(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, profile_id, if_match):

    if isinstance(profile_id, six.string_types) and len(profile_id.strip()) == 0:
        raise click.UsageError('Parameter --profile-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.delete_profile(
        profile_id=profile_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_profile') and callable(getattr(client, 'get_profile')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_profile(profile_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@resource_action_summary_group.command(name=cli_util.override('optimizer.filter_resource_actions.command_name', 'filter-resource-actions'), help=u"""Queries the Cloud Advisor resource actions that are supported by the specified recommendation. \n[Command Reference](filterResourceActions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--recommendation-id', required=True, help=u"""The unique OCID associated with the recommendation.""")
@cli_util.option('--query-parameterconflict', help=u"""The query describing which resources to search for. For more information, see [Query Language Syntax].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ResourceActionCollection'})
@cli_util.wrap_exceptions
def filter_resource_actions(ctx, from_json, compartment_id, compartment_id_in_subtree, recommendation_id, query_parameterconflict, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if query_parameterconflict is not None:
        _details['query'] = query_parameterconflict

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.filter_resource_actions(
        compartment_id=compartment_id,
        compartment_id_in_subtree=compartment_id_in_subtree,
        recommendation_id=recommendation_id,
        query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@category_group.command(name=cli_util.override('optimizer.get_category.command_name', 'get'), help=u"""Gets the category that corresponds to the specified OCID. \n[Command Reference](getCategory)""")
@cli_util.option('--category-id', required=True, help=u"""The unique OCID associated with the category.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'Category'})
@cli_util.wrap_exceptions
def get_category(ctx, from_json, category_id):

    if isinstance(category_id, six.string_types) and len(category_id.strip()) == 0:
        raise click.UsageError('Parameter --category-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_category(
        category_id=category_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@enrollment_status_group.command(name=cli_util.override('optimizer.get_enrollment_status.command_name', 'get'), help=u"""Gets the Cloud Advisor enrollment status. \n[Command Reference](getEnrollmentStatus)""")
@cli_util.option('--enrollment-status-id', required=True, help=u"""The unique OCID associated with the enrollment status.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'EnrollmentStatus'})
@cli_util.wrap_exceptions
def get_enrollment_status(ctx, from_json, enrollment_status_id):

    if isinstance(enrollment_status_id, six.string_types) and len(enrollment_status_id.strip()) == 0:
        raise click.UsageError('Parameter --enrollment-status-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_enrollment_status(
        enrollment_status_id=enrollment_status_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@profile_group.command(name=cli_util.override('optimizer.get_profile.command_name', 'get'), help=u"""Gets the specified profile's information. Uses the profile's OCID to determine which profile to retrieve. \n[Command Reference](getProfile)""")
@cli_util.option('--profile-id', required=True, help=u"""The unique OCID of the profile.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'Profile'})
@cli_util.wrap_exceptions
def get_profile(ctx, from_json, profile_id):

    if isinstance(profile_id, six.string_types) and len(profile_id.strip()) == 0:
        raise click.UsageError('Parameter --profile-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_profile(
        profile_id=profile_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@recommendation_group.command(name=cli_util.override('optimizer.get_recommendation.command_name', 'get'), help=u"""Gets the recommendation for the specified OCID. \n[Command Reference](getRecommendation)""")
@cli_util.option('--recommendation-id', required=True, help=u"""The unique OCID associated with the recommendation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'Recommendation'})
@cli_util.wrap_exceptions
def get_recommendation(ctx, from_json, recommendation_id):

    if isinstance(recommendation_id, six.string_types) and len(recommendation_id.strip()) == 0:
        raise click.UsageError('Parameter --recommendation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_recommendation(
        recommendation_id=recommendation_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resource_action_group.command(name=cli_util.override('optimizer.get_resource_action.command_name', 'get'), help=u"""Gets the resource action that corresponds to the specified OCID. \n[Command Reference](getResourceAction)""")
@cli_util.option('--resource-action-id', required=True, help=u"""The unique OCID associated with the resource action.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ResourceAction'})
@cli_util.wrap_exceptions
def get_resource_action(ctx, from_json, resource_action_id):

    if isinstance(resource_action_id, six.string_types) and len(resource_action_id.strip()) == 0:
        raise click.UsageError('Parameter --resource-action-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_resource_action(
        resource_action_id=resource_action_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('optimizer.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request associated with the specified ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@category_summary_group.command(name=cli_util.override('optimizer.list_categories.command_name', 'list-categories'), help=u"""Lists the supported Cloud Advisor categories. \n[Command Reference](listCategories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'CategoryCollection'})
@cli_util.wrap_exceptions
def list_categories(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_categories,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_categories,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    else:
        result = client.list_categories(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@enrollment_status_summary_group.command(name=cli_util.override('optimizer.list_enrollment_statuses.command_name', 'list-enrollment-statuses'), help=u"""Lists the Cloud Advisor enrollment statuses. \n[Command Reference](listEnrollmentStatuses)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""A filter that returns results that match the Cloud Advisor enrollment status specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'EnrollmentStatusCollection'})
@cli_util.wrap_exceptions
def list_enrollment_statuses(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by, lifecycle_state, status):

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
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_enrollment_statuses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_enrollment_statuses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_enrollment_statuses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@history_summary_group.command(name=cli_util.override('optimizer.list_histories.command_name', 'list-histories'), help=u"""Lists changes to the recommendations based on user activity. For example, lists when recommendations have been implemented, dismissed, postponed, or reactivated. \n[Command Reference](listHistories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--recommendation-name', help=u"""Optional. A filter that returns results that match the recommendation name specified.""")
@cli_util.option('--recommendation-id', help=u"""The unique OCID associated with the recommendation.""")
@cli_util.option('--resource-type', help=u"""Optional. A filter that returns results that match the resource type specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""A filter that returns recommendations that match the status specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'HistoryCollection'})
@cli_util.wrap_exceptions
def list_histories(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, name, recommendation_name, recommendation_id, resource_type, limit, page, sort_order, sort_by, lifecycle_state, status):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if recommendation_name is not None:
        kwargs['recommendation_name'] = recommendation_name
    if recommendation_id is not None:
        kwargs['recommendation_id'] = recommendation_id
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_histories,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_histories,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    else:
        result = client.list_histories(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@profile_level_summary_group.command(name=cli_util.override('optimizer.list_profile_levels.command_name', 'list-profile-levels'), help=u"""Lists the existing profile levels. \n[Command Reference](listProfileLevels)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--recommendation-name', help=u"""Optional. A filter that returns results that match the recommendation name specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ProfileLevelCollection'})
@cli_util.wrap_exceptions
def list_profile_levels(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, name, recommendation_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if recommendation_name is not None:
        kwargs['recommendation_name'] = recommendation_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_profile_levels,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_profile_levels,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    else:
        result = client.list_profile_levels(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@profile_summary_group.command(name=cli_util.override('optimizer.list_profiles.command_name', 'list-profiles'), help=u"""Lists the existing profiles. \n[Command Reference](listProfiles)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ProfileCollection'})
@cli_util.wrap_exceptions
def list_profiles(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_profiles,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_profiles,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_profiles(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recommendation_strategy_summary_group.command(name=cli_util.override('optimizer.list_recommendation_strategies.command_name', 'list-recommendation-strategies'), help=u"""Lists the existing strategies. \n[Command Reference](listRecommendationStrategies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--recommendation-name', help=u"""Optional. A filter that returns results that match the recommendation name specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'RecommendationStrategyCollection'})
@cli_util.wrap_exceptions
def list_recommendation_strategies(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, name, recommendation_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if recommendation_name is not None:
        kwargs['recommendation_name'] = recommendation_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_recommendation_strategies,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_recommendation_strategies,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    else:
        result = client.list_recommendation_strategies(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recommendation_summary_group.command(name=cli_util.override('optimizer.list_recommendations.command_name', 'list-recommendations'), help=u"""Lists the Cloud Advisor recommendations that are currently supported in the specified category. \n[Command Reference](listRecommendations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--category-id', required=True, help=u"""The unique OCID associated with the category.""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""A filter that returns recommendations that match the status specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'RecommendationCollection'})
@cli_util.wrap_exceptions
def list_recommendations(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, category_id, name, limit, page, sort_order, sort_by, lifecycle_state, status):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_recommendations,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            category_id=category_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_recommendations,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            category_id=category_id,
            **kwargs
        )
    else:
        result = client.list_recommendations(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            category_id=category_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@queryable_field_summary_group.command(name=cli_util.override('optimizer.list_resource_action_queryable_fields.command_name', 'list-resource-action-queryable-fields'), help=u"""Lists the fields that are indexed for querying and their associated value types. \n[Command Reference](listResourceActionQueryableFields)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'QueryableFieldCollection'})
@cli_util.wrap_exceptions
def list_resource_action_queryable_fields(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resource_action_queryable_fields,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resource_action_queryable_fields,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    else:
        result = client.list_resource_action_queryable_fields(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resource_action_summary_group.command(name=cli_util.override('optimizer.list_resource_actions.command_name', 'list-resource-actions'), help=u"""Lists the Cloud Advisor resource actions that are supported by the specified recommendation. \n[Command Reference](listResourceActions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--compartment-id-in-subtree', required=True, type=click.BOOL, help=u"""When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.

Can only be set to true when performing ListCompartments on the tenancy (root compartment).""")
@cli_util.option('--recommendation-id', required=True, help=u"""The unique OCID associated with the recommendation.""")
@cli_util.option('--name', help=u"""Optional. A filter that returns results that match the name specified.""")
@cli_util.option('--resource-type', help=u"""Optional. A filter that returns results that match the resource type specified.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), help=u"""A filter that returns results that match the lifecycle state specified.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""A filter that returns recommendations that match the status specified.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ResourceActionCollection'})
@cli_util.wrap_exceptions
def list_resource_actions(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, recommendation_id, name, resource_type, limit, page, sort_order, sort_by, lifecycle_state, status):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if status is not None:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resource_actions,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            recommendation_id=recommendation_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resource_actions,
            limit,
            page_size,
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            recommendation_id=recommendation_id,
            **kwargs
        )
    else:
        result = client.list_resource_actions(
            compartment_id=compartment_id,
            compartment_id_in_subtree=compartment_id_in_subtree,
            recommendation_id=recommendation_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('optimizer.list_work_request_errors.command_name', 'list'), help=u"""Lists errors associated with the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'WorkRequestErrorCollection'})
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
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('optimizer.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists the logs associated with the specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'WorkRequestLogEntryCollection'})
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
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
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


@work_request_group.command(name=cli_util.override('optimizer.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in the tenancy. The tenancy is the root compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'WorkRequestCollection'})
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
    client = cli_util.build_client('optimizer', 'optimizer', ctx)
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


@enrollment_status_group.command(name=cli_util.override('optimizer.update_enrollment_status.command_name', 'update'), help=u"""Updates the enrollment status of the tenancy. \n[Command Reference](updateEnrollmentStatus)""")
@cli_util.option('--enrollment-status-id', required=True, help=u"""The unique OCID associated with the enrollment status.""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The Cloud Advisor enrollment status.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'EnrollmentStatus'})
@cli_util.wrap_exceptions
def update_enrollment_status(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, enrollment_status_id, status, if_match):

    if isinstance(enrollment_status_id, six.string_types) and len(enrollment_status_id.strip()) == 0:
        raise click.UsageError('Parameter --enrollment-status-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.update_enrollment_status(
        enrollment_status_id=enrollment_status_id,
        update_enrollment_status_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_enrollment_status') and callable(getattr(client, 'get_enrollment_status')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_enrollment_status(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@profile_group.command(name=cli_util.override('optimizer.update_profile.command_name', 'update'), help=u"""Updates the specified profile. Uses the profile's OCID to determine which profile to update. \n[Command Reference](updateProfile)""")
@cli_util.option('--profile-id', required=True, help=u"""The unique OCID of the profile.""")
@cli_util.option('--description', help=u"""Text describing the profile. Avoid entering confidential information.""")
@cli_util.option('--aggregation-interval-in-days', type=click.INT, help=u"""The time period over which to collect data for the recommendations, measured in number of days.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type, or namespace. For more information, see [Resource Tags]. Exists for cross-compatibility only.

Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--levels-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-compartments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""The name assigned to the profile. Avoid entering confidential information.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'optimizer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'optimizer', 'class': 'dict(str, string)'}, 'levels-configuration': {'module': 'optimizer', 'class': 'LevelsConfiguration'}, 'target-compartments': {'module': 'optimizer', 'class': 'TargetCompartments'}, 'target-tags': {'module': 'optimizer', 'class': 'TargetTags'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'optimizer', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'optimizer', 'class': 'dict(str, string)'}, 'levels-configuration': {'module': 'optimizer', 'class': 'LevelsConfiguration'}, 'target-compartments': {'module': 'optimizer', 'class': 'TargetCompartments'}, 'target-tags': {'module': 'optimizer', 'class': 'TargetTags'}}, output_type={'module': 'optimizer', 'class': 'Profile'})
@cli_util.wrap_exceptions
def update_profile(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, profile_id, description, aggregation_interval_in_days, defined_tags, freeform_tags, levels_configuration, target_compartments, target_tags, name, if_match):

    if isinstance(profile_id, six.string_types) and len(profile_id.strip()) == 0:
        raise click.UsageError('Parameter --profile-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or levels_configuration or target_compartments or target_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and levels-configuration and target-compartments and target-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if aggregation_interval_in_days is not None:
        _details['aggregationIntervalInDays'] = aggregation_interval_in_days

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if levels_configuration is not None:
        _details['levelsConfiguration'] = cli_util.parse_json_parameter("levels_configuration", levels_configuration)

    if target_compartments is not None:
        _details['targetCompartments'] = cli_util.parse_json_parameter("target_compartments", target_compartments)

    if target_tags is not None:
        _details['targetTags'] = cli_util.parse_json_parameter("target_tags", target_tags)

    if name is not None:
        _details['name'] = name

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.update_profile(
        profile_id=profile_id,
        update_profile_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_profile') and callable(getattr(client, 'get_profile')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_profile(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@recommendation_group.command(name=cli_util.override('optimizer.update_recommendation.command_name', 'update'), help=u"""Updates the recommendation that corresponds to the specified OCID. Use this operation to implement the following actions:

  * Postpone recommendation   * Dismiss recommendation   * Reactivate recommendation \n[Command Reference](updateRecommendation)""")
@cli_util.option('--recommendation-id', required=True, help=u"""The unique OCID associated with the recommendation.""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""The status of the recommendation.""")
@cli_util.option('--time-status-end', type=custom_types.CLI_DATETIME, help=u"""The date and time the current status will change. The format is defined by RFC3339.

For example, \"The current `postponed` status of the recommendation will end and change to `pending` on this date and time.\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'Recommendation'})
@cli_util.wrap_exceptions
def update_recommendation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, recommendation_id, status, time_status_end, if_match):

    if isinstance(recommendation_id, six.string_types) and len(recommendation_id.strip()) == 0:
        raise click.UsageError('Parameter --recommendation-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status

    if time_status_end is not None:
        _details['timeStatusEnd'] = time_status_end

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.update_recommendation(
        recommendation_id=recommendation_id,
        update_recommendation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_recommendation') and callable(getattr(client, 'get_recommendation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_recommendation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@resource_action_group.command(name=cli_util.override('optimizer.update_resource_action.command_name', 'update'), help=u"""Updates the resource action that corresponds to the specified OCID. Use this operation to implement the following actions:

  * Postpone resource action   * Ignore resource action   * Reactivate resource action \n[Command Reference](updateResourceAction)""")
@cli_util.option('--resource-action-id', required=True, help=u"""The unique OCID associated with the resource action.""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"]), help=u"""The status of the resource action.""")
@cli_util.option('--time-status-end', type=custom_types.CLI_DATETIME, help=u"""The date and time the current status will change. The format is defined by RFC3339.

For example, \"The current `postponed` status of the resource action will end and change to `pending` on this date and time.\"""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "FAILED", "INACTIVE", "ATTACHING", "DETACHING", "DELETING", "DELETED", "UPDATING", "CREATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'optimizer', 'class': 'ResourceAction'})
@cli_util.wrap_exceptions
def update_resource_action(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, resource_action_id, status, time_status_end, if_match):

    if isinstance(resource_action_id, six.string_types) and len(resource_action_id.strip()) == 0:
        raise click.UsageError('Parameter --resource-action-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status

    if time_status_end is not None:
        _details['timeStatusEnd'] = time_status_end

    client = cli_util.build_client('optimizer', 'optimizer', ctx)
    result = client.update_resource_action(
        resource_action_id=resource_action_id,
        update_resource_action_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resource_action') and callable(getattr(client, 'get_resource_action')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resource_action(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
