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


@cli.command(cli_util.override('budgets.budgets_root_group.command_name', 'budgets'), cls=CommandGroupWithAlias, help=cli_util.override('budgets.budgets_root_group.help', """Use the Budgets API to manage budgets and budget alerts."""), short_help=cli_util.override('budgets.budgets_root_group.short_help', """Budgets API"""))
@cli_util.help_option_group
def budgets_root_group():
    pass


@click.command(cli_util.override('budgets.alert_rule_group.command_name', 'alert-rule'), cls=CommandGroupWithAlias, help="""The alert rule.""")
@cli_util.help_option_group
def alert_rule_group():
    pass


@click.command(cli_util.override('budgets.budget_group.command_name', 'budget'), cls=CommandGroupWithAlias, help="""A budget.""")
@cli_util.help_option_group
def budget_group():
    pass


budgets_root_group.add_command(alert_rule_group)
budgets_root_group.add_command(budget_group)


@alert_rule_group.command(name=cli_util.override('budgets.create_alert_rule.command_name', 'create'), help=u"""Creates a new Alert Rule.""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ACTUAL", "FORECAST"]), help=u"""Type of alert. Valid values are ACTUAL (the alert will trigger based on actual usage) or FORECAST (the alert will trigger based on predicted usage).""")
@cli_util.option('--threshold', required=True, type=click.FLOAT, help=u"""The threshold for triggering the alert expressed as a whole number or decimal value. If thresholdType is ABSOLUTE, threshold can have at most 12 digits before the decimal point and up to 2 digits after the decimal point. If thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to 2 digits after the decimal point.""")
@cli_util.option('--threshold-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PERCENTAGE", "ABSOLUTE"]), help=u"""The type of threshold.""")
@cli_util.option('--display-name', help=u"""The name of the alert rule.""")
@cli_util.option('--description', help=u"""The description of the alert rule.""")
@cli_util.option('--recipients', help=u"""The audience that will receive the alert when it triggers. An empty string is interpreted as null.""")
@cli_util.option('--message', help=u"""The message to be sent to the recipients when alert rule is triggered.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'budget', 'class': 'AlertRule'})
@cli_util.wrap_exceptions
def create_alert_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, budget_id, type, threshold, threshold_type, display_name, description, recipients, message, freeform_tags, defined_tags):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['threshold'] = threshold
    _details['thresholdType'] = threshold_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if recipients is not None:
        _details['recipients'] = recipients

    if message is not None:
        _details['message'] = message

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.create_alert_rule(
        budget_id=budget_id,
        create_alert_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_alert_rule') and callable(getattr(client, 'get_alert_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_alert_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@budget_group.command(name=cli_util.override('budgets.create_budget.command_name', 'create'), help=u"""Creates a new Budget.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment""")
@cli_util.option('--amount', required=True, type=click.FLOAT, help=u"""The amount of the budget expressed as a whole number in the currency of the customer's rate card.""")
@cli_util.option('--reset-period', required=True, type=custom_types.CliCaseInsensitiveChoice(["MONTHLY"]), help=u"""The reset period for the budget.""")
@cli_util.option('--target-compartment-id', help=u"""This is DEPRECTAED. Set the target compartment id in targets instead.""")
@cli_util.option('--display-name', help=u"""The displayName of the budget.""")
@cli_util.option('--description', help=u"""The description of the budget.""")
@cli_util.option('--target-type', type=custom_types.CliCaseInsensitiveChoice(["COMPARTMENT", "TAG"]), help=u"""The type of target on which the budget is applied.""")
@cli_util.option('--targets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of targets on which the budget is applied.   If targetType is \"COMPARTMENT\", targets contains list of compartment OCIDs.   If targetType is \"TAG\", targets contains list of cost tracking tag identifiers in the form of \"{tagNamespace}.{tagKey}.{tagValue}\". Curerntly, the array should contain EXACT ONE item.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'targets': {'module': 'budget', 'class': 'list[string]'}, 'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'targets': {'module': 'budget', 'class': 'list[string]'}, 'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'budget', 'class': 'Budget'})
@cli_util.wrap_exceptions
def create_budget(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, amount, reset_period, target_compartment_id, display_name, description, target_type, targets, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['amount'] = amount
    _details['resetPeriod'] = reset_period

    if target_compartment_id is not None:
        _details['targetCompartmentId'] = target_compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if target_type is not None:
        _details['targetType'] = target_type

    if targets is not None:
        _details['targets'] = cli_util.parse_json_parameter("targets", targets)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.create_budget(
        create_budget_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_budget') and callable(getattr(client, 'get_budget')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_budget(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@alert_rule_group.command(name=cli_util.override('budgets.delete_alert_rule.command_name', 'delete'), help=u"""Deletes a specified Alert Rule resource.""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--alert-rule-id', required=True, help=u"""The unique Alert Rule OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_alert_rule(ctx, from_json, budget_id, alert_rule_id, if_match):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    if isinstance(alert_rule_id, six.string_types) and len(alert_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --alert-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.delete_alert_rule(
        budget_id=budget_id,
        alert_rule_id=alert_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@budget_group.command(name=cli_util.override('budgets.delete_budget.command_name', 'delete'), help=u"""Deletes a specified Budget resource""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_budget(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, budget_id, if_match):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.delete_budget(
        budget_id=budget_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_budget') and callable(getattr(client, 'get_budget')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_budget(budget_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@alert_rule_group.command(name=cli_util.override('budgets.get_alert_rule.command_name', 'get'), help=u"""Gets an Alert Rule for a specified Budget.""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--alert-rule-id', required=True, help=u"""The unique Alert Rule OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'budget', 'class': 'AlertRule'})
@cli_util.wrap_exceptions
def get_alert_rule(ctx, from_json, budget_id, alert_rule_id):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    if isinstance(alert_rule_id, six.string_types) and len(alert_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --alert-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.get_alert_rule(
        budget_id=budget_id,
        alert_rule_id=alert_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@budget_group.command(name=cli_util.override('budgets.get_budget.command_name', 'get'), help=u"""Gets a Budget by identifier""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'budget', 'class': 'Budget'})
@cli_util.wrap_exceptions
def get_budget(ctx, from_json, budget_id):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.get_budget(
        budget_id=budget_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@alert_rule_group.command(name=cli_util.override('budgets.list_alert_rules.command_name', 'list'), help=u"""Returns a list of Alert Rules for a specified Budget.""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. If not specified, the default is timeCreated. The default sort order for timeCreated is DESC. The default sort order for displayName is ASC in alphanumeric order.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The current state of the resource to filter by.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'budget', 'class': 'list[AlertRuleSummary]'})
@cli_util.wrap_exceptions
def list_alert_rules(ctx, from_json, all_pages, page_size, budget_id, limit, page, sort_order, sort_by, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

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
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_alert_rules,
            budget_id=budget_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_alert_rules,
            limit,
            page_size,
            budget_id=budget_id,
            **kwargs
        )
    else:
        result = client.list_alert_rules(
            budget_id=budget_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@budget_group.command(name=cli_util.override('budgets.list_budgets.command_name', 'list'), help=u"""Gets a list of Budgets in a compartment.

By default, ListBudgets returns budgets of 'COMPARTMENT' target type and the budget records with only ONE target compartment OCID.

To list ALL budgets, set the targetType query parameter to ALL. Example:   'targetType=ALL'

Additional targetTypes would be available in future releases. Clients should ignore new targetType or upgrade to latest version of client SDK to handle new targetType.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. If not specified, the default is timeCreated. The default sort order for timeCreated is DESC. The default sort order for displayName is ASC in alphanumeric order.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The current state of the resource to filter by.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--target-type', type=custom_types.CliCaseInsensitiveChoice(["ALL", "COMPARTMENT", "TAG"]), help=u"""The type of target to filter by.   * ALL - List all budgets   * COMPARTMENT - List all budgets with targetType == \"COMPARTMENT\"   * TAG - List all budgets with targetType == \"TAG\"""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'budget', 'class': 'list[BudgetSummary]'})
@cli_util.wrap_exceptions
def list_budgets(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by, lifecycle_state, display_name, target_type):

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
    if display_name is not None:
        kwargs['display_name'] = display_name
    if target_type is not None:
        kwargs['target_type'] = target_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('budget', 'budget', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_budgets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_budgets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_budgets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@alert_rule_group.command(name=cli_util.override('budgets.update_alert_rule.command_name', 'update'), help=u"""Update an Alert Rule for the budget identified by the OCID.""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--alert-rule-id', required=True, help=u"""The unique Alert Rule OCID""")
@cli_util.option('--display-name', help=u"""The name of the alert rule.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["ACTUAL", "FORECAST"]), help=u"""Type of alert. Valid values are ACTUAL (the alert will trigger based on actual usage) or FORECAST (the alert will trigger based on predicted usage).""")
@cli_util.option('--threshold', type=click.FLOAT, help=u"""The threshold for triggering the alert expressed as a whole number or decimal value. If thresholdType is ABSOLUTE, threshold can have at most 12 digits before the decimal point and up to 2 digits after the decimal point. If thresholdType is PERCENTAGE, the maximum value is 10000 and can have up to 2 digits after the decimal point.""")
@cli_util.option('--threshold-type', type=custom_types.CliCaseInsensitiveChoice(["PERCENTAGE", "ABSOLUTE"]), help=u"""The type of threshold.""")
@cli_util.option('--recipients', help=u"""The audience that will receive the alert when it triggers. If you need to clear out this value, please pass in an empty string instead of null.""")
@cli_util.option('--description', help=u"""The description of the alert rule""")
@cli_util.option('--message', help=u"""The message to be delivered to the recipients when alert is triggered""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'budget', 'class': 'AlertRule'})
@cli_util.wrap_exceptions
def update_alert_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, budget_id, alert_rule_id, display_name, type, threshold, threshold_type, recipients, description, message, freeform_tags, defined_tags, if_match):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')

    if isinstance(alert_rule_id, six.string_types) and len(alert_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --alert-rule-id cannot be whitespace or empty string')
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

    if type is not None:
        _details['type'] = type

    if threshold is not None:
        _details['threshold'] = threshold

    if threshold_type is not None:
        _details['thresholdType'] = threshold_type

    if recipients is not None:
        _details['recipients'] = recipients

    if description is not None:
        _details['description'] = description

    if message is not None:
        _details['message'] = message

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.update_alert_rule(
        budget_id=budget_id,
        alert_rule_id=alert_rule_id,
        update_alert_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_alert_rule') and callable(getattr(client, 'get_alert_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_alert_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@budget_group.command(name=cli_util.override('budgets.update_budget.command_name', 'update'), help=u"""Update a Budget identified by the OCID""")
@cli_util.option('--budget-id', required=True, help=u"""The unique Budget OCID""")
@cli_util.option('--display-name', help=u"""The displayName of the budget.""")
@cli_util.option('--description', help=u"""The description of the budget.""")
@cli_util.option('--amount', type=click.FLOAT, help=u"""The amount of the budget expressed as a whole number in the currency of the customer's rate card.""")
@cli_util.option('--reset-period', type=custom_types.CliCaseInsensitiveChoice(["MONTHLY"]), help=u"""The reset period for the budget.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'budget', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'budget', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'budget', 'class': 'Budget'})
@cli_util.wrap_exceptions
def update_budget(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, budget_id, display_name, description, amount, reset_period, freeform_tags, defined_tags, if_match):

    if isinstance(budget_id, six.string_types) and len(budget_id.strip()) == 0:
        raise click.UsageError('Parameter --budget-id cannot be whitespace or empty string')
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

    if amount is not None:
        _details['amount'] = amount

    if reset_period is not None:
        _details['resetPeriod'] = reset_period

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('budget', 'budget', ctx)
    result = client.update_budget(
        budget_id=budget_id,
        update_budget_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_budget') and callable(getattr(client, 'get_budget')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_budget(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
