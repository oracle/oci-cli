# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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
from services.operator_access_control.src.oci_cli_operator_access_control.generated import opctl_service_cli


@click.command(cli_util.override('operator_control.operator_control_root_group.command_name', 'operator-control'), cls=CommandGroupWithAlias, help=cli_util.override('operator_control.operator_control_root_group.help', """Operator Access Control enables you to control the time duration and the actions an Oracle operator can perform on your Exadata Cloud@Customer infrastructure.
Using logging service, you can view a near real-time audit report of all actions performed by an Oracle operator.

Use the table of contents and search tool to explore the OperatorAccessControl API."""), short_help=cli_util.override('operator_control.operator_control_root_group.short_help', """OperatorAccessControl API"""))
@cli_util.help_option_group
def operator_control_root_group():
    pass


@click.command(cli_util.override('operator_control.operator_control_group.command_name', 'operator-control'), cls=CommandGroupWithAlias, help="""Operator Access Control enables you to grant, audit, or revoke the access Oracle has to your Exadata Cloud@Customer infrastructure, and obtain audit reports of all actions taken by a human operator, in a near real-time manner.""")
@cli_util.help_option_group
def operator_control_group():
    pass


opctl_service_cli.opctl_service_group.add_command(operator_control_root_group)
operator_control_root_group.add_command(operator_control_group)


@operator_control_group.command(name=cli_util.override('operator_control.change_operator_control_compartment.command_name', 'change-compartment'), help=u"""Moves the Operator Control resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](changeOperatorControlCompartment)""")
@cli_util.option('--operator-control-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the new compartment to contain the operator contol.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_operator_control_compartment(ctx, from_json, operator_control_id, compartment_id, if_match):

    if isinstance(operator_control_id, six.string_types) and len(operator_control_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    result = client.change_operator_control_compartment(
        operator_control_id=operator_control_id,
        change_operator_control_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_control_group.command(name=cli_util.override('operator_control.create_operator_control.command_name', 'create'), help=u"""Creates an Operator Control. \n[Command Reference](createOperatorControl)""")
@cli_util.option('--operator-control-name', required=True, help=u"""Name of the operator control.""")
@cli_util.option('--approver-groups-list', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of user groups who can approve an access request associated with a resource governed by this operator control.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-fully-pre-approved', required=True, type=click.BOOL, help=u"""Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control will be auto-approved.""")
@cli_util.option('--resource-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER", "CLOUDAUTONOMOUSVMCLUSTER"]), help=u"""resourceType for which the OperatorControl is applicable""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains this operator control.""")
@cli_util.option('--description', help=u"""Description of the operator control.""")
@cli_util.option('--approvers-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of users who can approve an access request associated with a resource governed by this operator control.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pre-approved-op-action-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be auto-approved if the access request only contain operator actions in the pre-approved list.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--email-id-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of emailId.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-message', help=u"""This is the message that will be displayed to the operator users while accessing the system.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'approvers-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'approver-groups-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'pre-approved-op-action-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'email-id-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'approvers-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'approver-groups-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'pre-approved-op-action-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'email-id-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operator_access_control', 'class': 'OperatorControl'})
@cli_util.wrap_exceptions
def create_operator_control(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operator_control_name, approver_groups_list, is_fully_pre_approved, resource_type, compartment_id, description, approvers_list, pre_approved_op_action_list, email_id_list, system_message, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operatorControlName'] = operator_control_name
    _details['approverGroupsList'] = cli_util.parse_json_parameter("approver_groups_list", approver_groups_list)
    _details['isFullyPreApproved'] = is_fully_pre_approved
    _details['resourceType'] = resource_type
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if approvers_list is not None:
        _details['approversList'] = cli_util.parse_json_parameter("approvers_list", approvers_list)

    if pre_approved_op_action_list is not None:
        _details['preApprovedOpActionList'] = cli_util.parse_json_parameter("pre_approved_op_action_list", pre_approved_op_action_list)

    if email_id_list is not None:
        _details['emailIdList'] = cli_util.parse_json_parameter("email_id_list", email_id_list)

    if system_message is not None:
        _details['systemMessage'] = system_message

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    result = client.create_operator_control(
        create_operator_control_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_operator_control') and callable(getattr(client, 'get_operator_control')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_operator_control(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@operator_control_group.command(name=cli_util.override('operator_control.delete_operator_control.command_name', 'delete'), help=u"""Deletes an Operator Control. You cannot delete an Operator Control if it is assigned to govern any target resource currently or in the future. In that case, first, delete all of the current and future assignments before deleting the Operator Control. An Operator Control that was previously assigned to a target resource is marked as DELETED following a successful deletion. However, it is not completely deleted from the system. This is to ensure auditing information for the accesses done under the Operator Control is preserved for future needs. The system purges the deleted Operator Control only when all of the audit data associated with the Operator Control are also deleted. Therefore, you cannot reuse the name of the deleted Operator Control until the system purges the Operator Control. \n[Command Reference](deleteOperatorControl)""")
@cli_util.option('--operator-control-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--description', help=u"""reason for deletion of OperatorControl.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_operator_control(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, operator_control_id, description, if_match):

    if isinstance(operator_control_id, six.string_types) and len(operator_control_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-id cannot be whitespace or empty string')

    kwargs = {}
    if description is not None:
        kwargs['description'] = description
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    result = client.delete_operator_control(
        operator_control_id=operator_control_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_operator_control') and callable(getattr(client, 'get_operator_control')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_operator_control(operator_control_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@operator_control_group.command(name=cli_util.override('operator_control.get_operator_control.command_name', 'get'), help=u"""Gets the Operator Control associated with the specified Operator Control ID. \n[Command Reference](getOperatorControl)""")
@cli_util.option('--operator-control-id', required=True, help=u"""unique OperatorControl identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorControl'})
@cli_util.wrap_exceptions
def get_operator_control(ctx, from_json, operator_control_id):

    if isinstance(operator_control_id, six.string_types) and len(operator_control_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    result = client.get_operator_control(
        operator_control_id=operator_control_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@operator_control_group.command(name=cli_util.override('operator_control.list_operator_controls.command_name', 'list'), help=u"""Lists the operator controls in the compartment. \n[Command Reference](listOperatorControls)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given OperatorControl lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return OperatorControl that match the entire display name given.""")
@cli_util.option('--resource-type', help=u"""A filter to return only lists of resources that match the entire given service type.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'OperatorControlCollection'})
@cli_util.wrap_exceptions
def list_operator_controls(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, resource_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_operator_controls,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_operator_controls,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_operator_controls(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@operator_control_group.command(name=cli_util.override('operator_control.update_operator_control.command_name', 'update'), help=u"""Modifies the existing OperatorControl for a given operator control id except the operator control id. \n[Command Reference](updateOperatorControl)""")
@cli_util.option('--operator-control-id', required=True, help=u"""unique OperatorControl identifier""")
@cli_util.option('--operator-control-name', required=True, help=u"""Name of the operator control.""")
@cli_util.option('--approver-groups-list', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of user groups who can approve an access request associated with a target resource under the governance of this operator control.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-fully-pre-approved', required=True, type=click.BOOL, help=u"""Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control will be auto-approved.""")
@cli_util.option('--description', help=u"""Description of the operator control.""")
@cli_util.option('--approvers-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of users who can approve an access request associated with a target resource under the governance of this operator control.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pre-approved-op-action-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be automatically approved if the access request only contain operator actions in the pre-approved list.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--email-id-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of emailId.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-message', help=u"""System message that would be displayed to the operator users on accessing the target resource under the governance of this operator control.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'approvers-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'approver-groups-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'pre-approved-op-action-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'email-id-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'approvers-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'approver-groups-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'pre-approved-op-action-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'email-id-list': {'module': 'operator_access_control', 'class': 'list[string]'}, 'freeform-tags': {'module': 'operator_access_control', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'operator_access_control', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'operator_access_control', 'class': 'OperatorControl'})
@cli_util.wrap_exceptions
def update_operator_control(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, operator_control_id, operator_control_name, approver_groups_list, is_fully_pre_approved, description, approvers_list, pre_approved_op_action_list, email_id_list, system_message, freeform_tags, defined_tags, if_match):

    if isinstance(operator_control_id, six.string_types) and len(operator_control_id.strip()) == 0:
        raise click.UsageError('Parameter --operator-control-id cannot be whitespace or empty string')
    if not force:
        if approvers_list or approver_groups_list or pre_approved_op_action_list or email_id_list or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to approvers-list and approver-groups-list and pre-approved-op-action-list and email-id-list and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['operatorControlName'] = operator_control_name
    _details['approverGroupsList'] = cli_util.parse_json_parameter("approver_groups_list", approver_groups_list)
    _details['isFullyPreApproved'] = is_fully_pre_approved

    if description is not None:
        _details['description'] = description

    if approvers_list is not None:
        _details['approversList'] = cli_util.parse_json_parameter("approvers_list", approvers_list)

    if pre_approved_op_action_list is not None:
        _details['preApprovedOpActionList'] = cli_util.parse_json_parameter("pre_approved_op_action_list", pre_approved_op_action_list)

    if email_id_list is not None:
        _details['emailIdList'] = cli_util.parse_json_parameter("email_id_list", email_id_list)

    if system_message is not None:
        _details['systemMessage'] = system_message

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('operator_access_control', 'operator_control', ctx)
    result = client.update_operator_control(
        operator_control_id=operator_control_id,
        update_operator_control_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_operator_control') and callable(getattr(client, 'get_operator_control')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_operator_control(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
