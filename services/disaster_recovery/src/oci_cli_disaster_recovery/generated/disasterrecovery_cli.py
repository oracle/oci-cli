# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('disaster_recovery.disaster_recovery_root_group.command_name', 'disaster-recovery'), cls=CommandGroupWithAlias, help=cli_util.override('disaster_recovery.disaster_recovery_root_group.help', """Use the Full Stack Disaster Recovery (FSDR) API to manage disaster recovery for business applications.
FSDR is an OCI disaster recovery orchestration and management service that provides comprehensive disaster recovery
capabilities for all layers of an application stack, including infrastructure, middleware, database, and application."""), short_help=cli_util.override('disaster_recovery.disaster_recovery_root_group.short_help', """Full Stack Disaster Recovery API"""))
@cli_util.help_option_group
def disaster_recovery_root_group():
    pass


@click.command(cli_util.override('disaster_recovery.dr_protection_group_group.command_name', 'dr-protection-group'), cls=CommandGroupWithAlias, help="""Details about a DR Protection Group.""")
@cli_util.help_option_group
def dr_protection_group_group():
    pass


@click.command(cli_util.override('disaster_recovery.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error associcated with a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('disaster_recovery.dr_plan_execution_group.command_name', 'dr-plan-execution'), cls=CommandGroupWithAlias, help="""The details of a DR Plan Execution.""")
@cli_util.help_option_group
def dr_plan_execution_group():
    pass


@click.command(cli_util.override('disaster_recovery.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message related to the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('disaster_recovery.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Information on a work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('disaster_recovery.dr_plan_group.command_name', 'dr-plan'), cls=CommandGroupWithAlias, help="""The details of a DR Plan.""")
@cli_util.help_option_group
def dr_plan_group():
    pass


disaster_recovery_root_group.add_command(dr_protection_group_group)
disaster_recovery_root_group.add_command(work_request_error_group)
disaster_recovery_root_group.add_command(dr_plan_execution_group)
disaster_recovery_root_group.add_command(work_request_log_entry_group)
disaster_recovery_root_group.add_command(work_request_group)
disaster_recovery_root_group.add_command(dr_plan_group)


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.associate_dr_protection_group.command_name', 'associate'), help=u"""Create an association the DR Protection Group identified by *drProtectionGroupId* and another DR Protection Group in a different region. \n[Command Reference](associateDrProtectionGroup)""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "STANDBY", "UNCONFIGURED"]), help=u"""The role of this DR Protection Group.""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--peer-id', help=u"""The OCID of the peer (remote) DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`""")
@cli_util.option('--peer-region', help=u"""The region of the peer (remote) DR Protection Group.

Example: `us-ashburn-1`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def associate_dr_protection_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, role, dr_protection_group_id, peer_id, peer_region, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['role'] = role

    if peer_id is not None:
        _details['peerId'] = peer_id

    if peer_region is not None:
        _details['peerRegion'] = peer_region

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.associate_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
        associate_dr_protection_group_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.cancel_dr_plan_execution.command_name', 'cancel'), help=u"""Cancel the DR Plan Execution indentified by *drPlanExecutionId*. \n[Command Reference](cancelDrPlanExecution)""")
@cli_util.option('--action-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CANCEL", "PAUSE", "RESUME"]), help=u"""The type of control action.""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, action_type, dr_plan_execution_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['actionType'] = action_type

    _details['actionType'] = 'CANCEL'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.cancel_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        cancel_dr_plan_execution_details=_details,
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


@work_request_group.command(name=cli_util.override('disaster_recovery.cancel_work_request.command_name', 'cancel'), help=u"""Cancel the work request identified by *workRequestId*. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID (OCID) of the asynchronous request.

Example: `ocid1.workrequest.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.change_dr_protection_group_compartment.command_name', 'change-compartment'), help=u"""Move the DR Protection Group identified by *drProtectionGroupId* to a different compartment. \n[Command Reference](changeDrProtectionGroupCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to which the DR Protection Group should be moved.

Example: `ocid1.compartment.oc1..exampleocid1`""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_dr_protection_group_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, dr_protection_group_id, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.change_dr_protection_group_compartment(
        dr_protection_group_id=dr_protection_group_id,
        change_dr_protection_group_compartment_details=_details,
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


@dr_plan_group.command(name=cli_util.override('disaster_recovery.create_dr_plan.command_name', 'create'), help=u"""Creates a new DR Plan of the specified DR Plan type. \n[Command Reference](createDrPlan)""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the DR Plan being created.

Example: `EBS Switchover PHX to IAD`""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SWITCHOVER", "FAILOVER"]), help=u"""The type of DR Plan to be created.""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group to which this DR Plan belongs.

Example: `ocid1.drprotectiongroup.oc1.iad.exampleocid2`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlan'})
@cli_util.wrap_exceptions
def create_dr_plan(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, type, dr_protection_group_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['type'] = type
    _details['drProtectionGroupId'] = dr_protection_group_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan(
        create_dr_plan_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.create_dr_plan_execution.command_name', 'create'), help=u"""Execute a DR Plan for a DR Protection Group. \n[Command Reference](createDrPlanExecution)""")
@cli_util.option('--plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid2`""")
@cli_util.option('--execution-options', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the DR Plan Execution.

Example: `Execution - EBS Switchover PHX to IAD`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'execution-options': {'module': 'disaster_recovery', 'class': 'DrPlanExecutionOptionDetails'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'execution-options': {'module': 'disaster_recovery', 'class': 'DrPlanExecutionOptionDetails'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plan_id, execution_options, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['planId'] = plan_id
    _details['executionOptions'] = cli_util.parse_json_parameter("execution_options", execution_options)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan_execution(
        create_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.create_dr_plan_execution_switchover_precheck_execution_option_details.command_name', 'create-dr-plan-execution-switchover-precheck-execution-option-details'), help=u"""Execute a DR Plan for a DR Protection Group. \n[Command Reference](createDrPlanExecution)""")
@cli_util.option('--plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid2`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Plan Execution.

Example: `Execution - EBS Switchover PHX to IAD`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--execution-options-are-warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnigs should be ignored during the switchover.

Example: `true`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_switchover_precheck_execution_option_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plan_id, display_name, freeform_tags, defined_tags, execution_options_are_warnings_ignored):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['executionOptions'] = {}
    _details['planId'] = plan_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if execution_options_are_warnings_ignored is not None:
        _details['executionOptions']['areWarningsIgnored'] = execution_options_are_warnings_ignored

    _details['executionOptions']['planExecutionType'] = 'SWITCHOVER_PRECHECK'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan_execution(
        create_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.create_dr_plan_execution_failover_precheck_execution_option_details.command_name', 'create-dr-plan-execution-failover-precheck-execution-option-details'), help=u"""Execute a DR Plan for a DR Protection Group. \n[Command Reference](createDrPlanExecution)""")
@cli_util.option('--plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid2`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Plan Execution.

Example: `Execution - EBS Switchover PHX to IAD`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--execution-options-are-warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnigs should be ignored during the failover.

Example: `false`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_failover_precheck_execution_option_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plan_id, display_name, freeform_tags, defined_tags, execution_options_are_warnings_ignored):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['executionOptions'] = {}
    _details['planId'] = plan_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if execution_options_are_warnings_ignored is not None:
        _details['executionOptions']['areWarningsIgnored'] = execution_options_are_warnings_ignored

    _details['executionOptions']['planExecutionType'] = 'FAILOVER_PRECHECK'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan_execution(
        create_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.create_dr_plan_execution_switchover_execution_option_details.command_name', 'create-dr-plan-execution-switchover-execution-option-details'), help=u"""Execute a DR Plan for a DR Protection Group. \n[Command Reference](createDrPlanExecution)""")
@cli_util.option('--plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid2`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Plan Execution.

Example: `Execution - EBS Switchover PHX to IAD`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--execution-options-are-prechecks-enabled', type=click.BOOL, help=u"""A flag indicating whether a precheck should be executed before the plan.

Example: `false`""")
@cli_util.option('--execution-options-are-warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnigs should be ignored during the switchover.

Example: `true`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_switchover_execution_option_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plan_id, display_name, freeform_tags, defined_tags, execution_options_are_prechecks_enabled, execution_options_are_warnings_ignored):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['executionOptions'] = {}
    _details['planId'] = plan_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if execution_options_are_prechecks_enabled is not None:
        _details['executionOptions']['arePrechecksEnabled'] = execution_options_are_prechecks_enabled

    if execution_options_are_warnings_ignored is not None:
        _details['executionOptions']['areWarningsIgnored'] = execution_options_are_warnings_ignored

    _details['executionOptions']['planExecutionType'] = 'SWITCHOVER'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan_execution(
        create_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.create_dr_plan_execution_failover_execution_option_details.command_name', 'create-dr-plan-execution-failover-execution-option-details'), help=u"""Execute a DR Plan for a DR Protection Group. \n[Command Reference](createDrPlanExecution)""")
@cli_util.option('--plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid2`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Plan Execution.

Example: `Execution - EBS Switchover PHX to IAD`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--execution-options-are-prechecks-enabled', type=click.BOOL, help=u"""A flag indicating whether a precheck should be executed before the plan.

Example: `true`""")
@cli_util.option('--execution-options-are-warnings-ignored', type=click.BOOL, help=u"""A flag indicating whether warnigs should be ignored during the failover.

Example: `false`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def create_dr_plan_execution_failover_execution_option_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, plan_id, display_name, freeform_tags, defined_tags, execution_options_are_prechecks_enabled, execution_options_are_warnings_ignored):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['executionOptions'] = {}
    _details['planId'] = plan_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if execution_options_are_prechecks_enabled is not None:
        _details['executionOptions']['arePrechecksEnabled'] = execution_options_are_prechecks_enabled

    if execution_options_are_warnings_ignored is not None:
        _details['executionOptions']['areWarningsIgnored'] = execution_options_are_warnings_ignored

    _details['executionOptions']['planExecutionType'] = 'FAILOVER'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_plan_execution(
        create_dr_plan_execution_details=_details,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.create_dr_protection_group.command_name', 'create'), help=u"""Create a new DR Protection Group. \n[Command Reference](createDrProtectionGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the DR Protection Group.

Example: `ocid1.compartment.oc1..exampleocid1`""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the DR Protection Group.

Example: `EBS PHX DRPG`""")
@cli_util.option('--log-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of DR Protection Group members.

This option is a JSON list with items of type CreateDrProtectionGroupMemberDetails.  For documentation on CreateDrProtectionGroupMemberDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/disasterrecovery/20220125/datatypes/CreateDrProtectionGroupMemberDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'log-location': {'module': 'disaster_recovery', 'class': 'CreateObjectStorageLogLocationDetails'}, 'association': {'module': 'disaster_recovery', 'class': 'AssociateDrProtectionGroupDetails'}, 'members': {'module': 'disaster_recovery', 'class': 'list[CreateDrProtectionGroupMemberDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'log-location': {'module': 'disaster_recovery', 'class': 'CreateObjectStorageLogLocationDetails'}, 'association': {'module': 'disaster_recovery', 'class': 'AssociateDrProtectionGroupDetails'}, 'members': {'module': 'disaster_recovery', 'class': 'list[CreateDrProtectionGroupMemberDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'disaster_recovery', 'class': 'DrProtectionGroup'})
@cli_util.wrap_exceptions
def create_dr_protection_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, log_location, association, members, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['logLocation'] = cli_util.parse_json_parameter("log_location", log_location)

    if association is not None:
        _details['association'] = cli_util.parse_json_parameter("association", association)

    if members is not None:
        _details['members'] = cli_util.parse_json_parameter("members", members)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.create_dr_protection_group(
        create_dr_protection_group_details=_details,
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


@dr_plan_group.command(name=cli_util.override('disaster_recovery.delete_dr_plan.command_name', 'delete'), help=u"""Delete the DR Plan identified by *drPlanId*. \n[Command Reference](deleteDrPlan)""")
@cli_util.option('--dr-plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dr_plan(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_plan_id, if_match):

    if isinstance(dr_plan_id, six.string_types) and len(dr_plan_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.delete_dr_plan(
        dr_plan_id=dr_plan_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dr_plan') and callable(getattr(client, 'get_dr_plan')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dr_plan(dr_plan_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.delete_dr_plan_execution.command_name', 'delete'), help=u"""Delete the DR Plan Execution identified by *drPlanExecutionId*. \n[Command Reference](deleteDrPlanExecution)""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_plan_execution_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.delete_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.delete_dr_protection_group.command_name', 'delete'), help=u"""Delete the DR Protection Group identified by *drProtectionGroupId*. \n[Command Reference](deleteDrProtectionGroup)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dr_protection_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_protection_group_id, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.delete_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.disassociate_dr_protection_group.command_name', 'disassociate'), help=u"""Delete the association between the DR Protection Group identified by *drProtectionGroupId*. and its peer DR Protection Group. \n[Command Reference](disassociateDrProtectionGroup)""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The default type (required for forward compatibility).""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disassociate_dr_protection_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, type, dr_protection_group_id, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.disassociate_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
        disassociate_dr_protection_group_details=_details,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.disassociate_dr_protection_group_disassociate_dr_protection_group_default_details.command_name', 'disassociate-dr-protection-group-disassociate-dr-protection-group-default-details'), help=u"""Delete the association between the DR Protection Group identified by *drProtectionGroupId*. and its peer DR Protection Group. \n[Command Reference](disassociateDrProtectionGroup)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def disassociate_dr_protection_group_disassociate_dr_protection_group_default_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_protection_group_id, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'DEFAULT'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.disassociate_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
        disassociate_dr_protection_group_details=_details,
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


@dr_plan_group.command(name=cli_util.override('disaster_recovery.get_dr_plan.command_name', 'get'), help=u"""Get details for the DR Plan identified by *drPlanId*. \n[Command Reference](getDrPlan)""")
@cli_util.option('--dr-plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrPlan'})
@cli_util.wrap_exceptions
def get_dr_plan(ctx, from_json, dr_plan_id):

    if isinstance(dr_plan_id, six.string_types) and len(dr_plan_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.get_dr_plan(
        dr_plan_id=dr_plan_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.get_dr_plan_execution.command_name', 'get'), help=u"""Get details for the DR Plan Execution identified by *drPlanExecutionId*. \n[Command Reference](getDrPlanExecution)""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecution'})
@cli_util.wrap_exceptions
def get_dr_plan_execution(ctx, from_json, dr_plan_execution_id):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.get_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.get_dr_protection_group.command_name', 'get'), help=u"""Get the DR Protection Group identified by *drProtectionGroupId*. \n[Command Reference](getDrProtectionGroup)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrProtectionGroup'})
@cli_util.wrap_exceptions
def get_dr_protection_group(ctx, from_json, dr_protection_group_id):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.get_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('disaster_recovery.get_work_request.command_name', 'get'), help=u"""Get the status of the work request identified by *workRequestId*. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID (OCID) of the asynchronous request.

Example: `ocid1.workrequest.oc1.phx.exampleocid`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.ignore_dr_plan_execution.command_name', 'ignore'), help=u"""Ignore failed group or step in DR Plan Execution identified by *drPlanExecutionId* and resume execution. \n[Command Reference](ignoreDrPlanExecution)""")
@cli_util.option('--group-id', required=True, help=u"""The unique id of the group to ignore as a whole, or the group containing the step to ignore.

Example: `sgid1.group..examplegroupsgid`""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--step-id', help=u"""The unique id of the step to ignore (optional). Only needed when ignoring a step.

Example: `sgid1.step..examplestepsgid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def ignore_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, group_id, dr_plan_execution_id, step_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['groupId'] = group_id

    if step_id is not None:
        _details['stepId'] = step_id

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.ignore_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        ignore_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.list_dr_plan_executions.command_name', 'list'), help=u"""Get a summary list of all DR Plan Executions for a DR Protection Group. \n[Command Reference](listDrPlanExecutions)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group. Mandatory query param.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "DELETING", "DELETED", "PAUSING", "PAUSED", "RESUMING"]), help=u"""A filter to return only DR Plan Executions that match the given lifecycleState.""")
@cli_util.option('--dr-plan-execution-id', help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--dr-plan-execution-type', type=custom_types.CliCaseInsensitiveChoice(["SWITCHOVER", "SWITCHOVER_PRECHECK", "FAILOVER", "FAILOVER_PRECHECK"]), help=u"""The DR Plan Execution type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.

Example: `MY UNIQUE DISPLAY NAME`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Example: `displayName`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanExecutionCollection'})
@cli_util.wrap_exceptions
def list_dr_plan_executions(ctx, from_json, all_pages, page_size, dr_protection_group_id, lifecycle_state, dr_plan_execution_id, dr_plan_execution_type, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if dr_plan_execution_id is not None:
        kwargs['dr_plan_execution_id'] = dr_plan_execution_id
    if dr_plan_execution_type is not None:
        kwargs['dr_plan_execution_type'] = dr_plan_execution_type
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
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dr_plan_executions,
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dr_plan_executions,
            limit,
            page_size,
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    else:
        result = client.list_dr_plan_executions(
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dr_plan_group.command(name=cli_util.override('disaster_recovery.list_dr_plans.command_name', 'list'), help=u"""Gets a summary list of all DR Plans for a DR Protection Group. \n[Command Reference](listDrPlans)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group. Mandatory query param.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), help=u"""A filter to return only DR Plans that match the given lifecycleState.""")
@cli_util.option('--dr-plan-id', help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid`""")
@cli_util.option('--dr-plan-type', type=custom_types.CliCaseInsensitiveChoice(["SWITCHOVER", "FAILOVER"]), help=u"""The DR Plan type.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.

Example: `MY UNIQUE DISPLAY NAME`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Example: `displayName`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrPlanCollection'})
@cli_util.wrap_exceptions
def list_dr_plans(ctx, from_json, all_pages, page_size, dr_protection_group_id, lifecycle_state, dr_plan_id, dr_plan_type, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if dr_plan_id is not None:
        kwargs['dr_plan_id'] = dr_plan_id
    if dr_plan_type is not None:
        kwargs['dr_plan_type'] = dr_plan_type
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
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dr_plans,
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dr_plans,
            limit,
            page_size,
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    else:
        result = client.list_dr_plans(
            dr_protection_group_id=dr_protection_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.list_dr_protection_groups.command_name', 'list'), help=u"""Gets a summary list of all DR Protection Groups in a compartment. \n[Command Reference](listDrProtectionGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID (OCID) of the compartment in which to list resources.

Example: `ocid1.compartment.oc1..exampleocid1`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only DR Protection Groups that match the given lifecycleState.""")
@cli_util.option('--dr-protection-group-id', help=u"""The OCID of the DR Protection Group. Optional query param.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.

Example: `MY UNIQUE DISPLAY NAME`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

Example: `displayName`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'DrProtectionGroupCollection'})
@cli_util.wrap_exceptions
def list_dr_protection_groups(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, dr_protection_group_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if dr_protection_group_id is not None:
        kwargs['dr_protection_group_id'] = dr_protection_group_id
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
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dr_protection_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dr_protection_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dr_protection_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('disaster_recovery.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID (OCID) of the asynchronous request.

Example: `ocid1.workrequest.oc1.phx.exampleocid`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'WorkRequestErrorCollection'})
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
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('disaster_recovery.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for the work request identified by *workRequestId*. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID (OCID) of the asynchronous request.

Example: `ocid1.workrequest.oc1.phx.exampleocid`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'WorkRequestLogEntryCollection'})
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
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
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


@work_request_group.command(name=cli_util.override('disaster_recovery.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""The ID (OCID) of the compartment in which to list resources.

Example: `ocid1.compartment.oc1..exampleocid1`""")
@cli_util.option('--work-request-id', help=u"""The ID (OCID) of the asynchronous work request.

Example: `ocid1.workrequest.oc1.phx.exampleocid1`""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), help=u"""A filter to return only resources whose lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID (OCID) of the resource affected by the work request. Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum.

For important details about how pagination works, see [List Pagination].

Example: `100`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'disaster_recovery', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.pause_dr_plan_execution.command_name', 'pause'), help=u"""Pause the DR Plan Execution identified by *drPlanExecutionId*. \n[Command Reference](pauseDrPlanExecution)""")
@cli_util.option('--action-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CANCEL", "PAUSE", "RESUME"]), help=u"""The type of control action.""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def pause_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, action_type, dr_plan_execution_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['actionType'] = action_type

    _details['actionType'] = 'PAUSE'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.pause_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        pause_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.resume_dr_plan_execution.command_name', 'resume'), help=u"""Resume the DR Plan Execution identified by *drPlanExecutionId*. \n[Command Reference](resumeDrPlanExecution)""")
@cli_util.option('--action-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CANCEL", "PAUSE", "RESUME"]), help=u"""The type of control action.""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def resume_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, action_type, dr_plan_execution_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['actionType'] = action_type

    _details['actionType'] = 'RESUME'

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.resume_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        resume_dr_plan_execution_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.retry_dr_plan_execution.command_name', 'retry'), help=u"""Retry failed group or step in DR Plan Execution identified by *drPlanExecutionId* and resume execution. \n[Command Reference](retryDrPlanExecution)""")
@cli_util.option('--group-id', required=True, help=u"""The unique id of the group to retry as a whole, or the group containing the step being retried.

Example: `sgid1.group..examplegroupsgid`""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--step-id', help=u"""The unique id of the step to retry (optional). Only needed when retrying a step.

Example: `sgid1.step..examplestepsgid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def retry_dr_plan_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, group_id, dr_plan_execution_id, step_id, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['groupId'] = group_id

    if step_id is not None:
        _details['stepId'] = step_id

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.retry_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        retry_dr_plan_execution_details=_details,
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


@dr_plan_group.command(name=cli_util.override('disaster_recovery.update_dr_plan.command_name', 'update'), help=u"""Update the DR Plan identified by *drPlanId*. \n[Command Reference](updateDrPlan)""")
@cli_util.option('--dr-plan-id', required=True, help=u"""The OCID of the DR Plan.

Example: `ocid1.drplan.oc1.iad.exampleocid`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Plan being updated.

Example: `EBS Switchover PHX to IAD`""")
@cli_util.option('--plan-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An ordered list of plan groups in a DR Plan.

This option is a JSON list with items of type UpdateDrPlanGroupDetails.  For documentation on UpdateDrPlanGroupDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/disasterrecovery/20220125/datatypes/UpdateDrPlanGroupDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'plan-groups': {'module': 'disaster_recovery', 'class': 'list[UpdateDrPlanGroupDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'plan-groups': {'module': 'disaster_recovery', 'class': 'list[UpdateDrPlanGroupDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_dr_plan(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_plan_id, display_name, plan_groups, freeform_tags, defined_tags, if_match):

    if isinstance(dr_plan_id, six.string_types) and len(dr_plan_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-id cannot be whitespace or empty string')
    if not force:
        if plan_groups or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to plan-groups and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if plan_groups is not None:
        _details['planGroups'] = cli_util.parse_json_parameter("plan_groups", plan_groups)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.update_dr_plan(
        dr_plan_id=dr_plan_id,
        update_dr_plan_details=_details,
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


@dr_plan_execution_group.command(name=cli_util.override('disaster_recovery.update_dr_plan_execution.command_name', 'update'), help=u"""Update the DR Plan Execution identified by *drPlanExecutionId*. \n[Command Reference](updateDrPlanExecution)""")
@cli_util.option('--dr-plan-execution-id', required=True, help=u"""The OCID of the DR Plan Execution.

Example: `ocid1.drplanexecution.oc1.iad.exampleocid`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Protection Group to update.

Example: `EBS IAD DRPG`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_dr_plan_execution(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_plan_execution_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(dr_plan_execution_id, six.string_types) and len(dr_plan_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-plan-execution-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.update_dr_plan_execution(
        dr_plan_execution_id=dr_plan_execution_id,
        update_dr_plan_execution_details=_details,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.update_dr_protection_group.command_name', 'update'), help=u"""Update the DR Protection Group identified by *drProtectionGroupId*. \n[Command Reference](updateDrProtectionGroup)""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--display-name', help=u"""The display name of the DR Protection Group.

Example: `EBS PHX DRPG`""")
@cli_util.option('--log-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of DR Protection Group members.

This option is a JSON list with items of type UpdateDrProtectionGroupMemberDetails.  For documentation on UpdateDrProtectionGroupMemberDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/disasterrecovery/20220125/datatypes/UpdateDrProtectionGroupMemberDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'log-location': {'module': 'disaster_recovery', 'class': 'UpdateObjectStorageLogLocationDetails'}, 'members': {'module': 'disaster_recovery', 'class': 'list[UpdateDrProtectionGroupMemberDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'log-location': {'module': 'disaster_recovery', 'class': 'UpdateObjectStorageLogLocationDetails'}, 'members': {'module': 'disaster_recovery', 'class': 'list[UpdateDrProtectionGroupMemberDetails]'}, 'freeform-tags': {'module': 'disaster_recovery', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'disaster_recovery', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_dr_protection_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dr_protection_group_id, display_name, log_location, members, freeform_tags, defined_tags, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')
    if not force:
        if log_location or members or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to log-location and members and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if log_location is not None:
        _details['logLocation'] = cli_util.parse_json_parameter("log_location", log_location)

    if members is not None:
        _details['members'] = cli_util.parse_json_parameter("members", members)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.update_dr_protection_group(
        dr_protection_group_id=dr_protection_group_id,
        update_dr_protection_group_details=_details,
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


@dr_protection_group_group.command(name=cli_util.override('disaster_recovery.update_dr_protection_group_role.command_name', 'update-dr-protection-group-role'), help=u"""Update the role of the DR Protection Group identified by *drProtectionGroupId*. \n[Command Reference](updateDrProtectionGroupRole)""")
@cli_util.option('--role', required=True, type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "STANDBY", "UNCONFIGURED"]), help=u"""The role of the DR Protection Group.""")
@cli_util.option('--dr-protection-group-id', required=True, help=u"""The OCID of the DR Protection Group.

Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "CANCELING", "CANCELED", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_dr_protection_group_role(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, role, dr_protection_group_id, if_match):

    if isinstance(dr_protection_group_id, six.string_types) and len(dr_protection_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dr-protection-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['role'] = role

    client = cli_util.build_client('disaster_recovery', 'disaster_recovery', ctx)
    result = client.update_dr_protection_group_role(
        dr_protection_group_id=dr_protection_group_id,
        update_dr_protection_group_role_details=_details,
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
