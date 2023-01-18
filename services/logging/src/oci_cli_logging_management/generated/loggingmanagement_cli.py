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


@cli.command(cli_util.override('logging.logging_root_group.command_name', 'logging'), cls=CommandGroupWithAlias, help=cli_util.override('logging.logging_root_group.help', """Use the Logging Management API to create, read, list, update, and delete log groups, log objects, and agent configurations."""), short_help=cli_util.override('logging.logging_root_group.short_help', """Logging Management API"""))
@cli_util.help_option_group
def logging_root_group():
    pass


@click.command(cli_util.override('logging.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('logging.log_group_group.command_name', 'log-group'), cls=CommandGroupWithAlias, help="""Represents a LogGroup object.""")
@cli_util.help_option_group
def log_group_group():
    pass


@click.command(cli_util.override('logging.log_group.command_name', 'log'), cls=CommandGroupWithAlias, help="""Represents a log object.""")
@cli_util.help_option_group
def log_group():
    pass


@click.command(cli_util.override('logging.service_group.command_name', 'service'), cls=CommandGroupWithAlias, help="""Summary of services that are integrated with public logging.""")
@cli_util.help_option_group
def service_group():
    pass


@click.command(cli_util.override('logging.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('logging.unified_agent_configuration_group.command_name', 'unified-agent-configuration'), cls=CommandGroupWithAlias, help="""Top Unified Agent configuration object.""")
@cli_util.help_option_group
def unified_agent_configuration_group():
    pass


@click.command(cli_util.override('logging.log_included_search_group.command_name', 'log-included-search'), cls=CommandGroupWithAlias, help="""A search provided by OCI that serves common customer needs.""")
@cli_util.help_option_group
def log_included_search_group():
    pass


@click.command(cli_util.override('logging.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('logging.log_saved_search_group.command_name', 'log-saved-search'), cls=CommandGroupWithAlias, help="""A log saved search that can be used to save and share a given search result.""")
@cli_util.help_option_group
def log_saved_search_group():
    pass


logging_root_group.add_command(work_request_log_group)
logging_root_group.add_command(log_group_group)
logging_root_group.add_command(log_group)
logging_root_group.add_command(service_group)
logging_root_group.add_command(work_request_error_group)
logging_root_group.add_command(unified_agent_configuration_group)
logging_root_group.add_command(log_included_search_group)
logging_root_group.add_command(work_request_group)
logging_root_group.add_command(log_saved_search_group)


@log_group_group.command(name=cli_util.override('logging.change_log_group_compartment.command_name', 'change-compartment'), help=u"""Moves a log group into a different compartment within the same tenancy.  When provided, the If-Match is checked against the resource ETag values. For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeLogGroupCompartment)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--compartment-id', help=u"""The compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_group_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, compartment_id, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.change_log_group_compartment(
        log_group_id=log_group_id,
        change_log_group_compartment_details=_details,
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


@log_group.command(name=cli_util.override('logging.change_log_log_group.command_name', 'change-log-log-group'), help=u"""Moves a log into a different log group within the same tenancy.  When provided, the If-Match is checked against the ETag values of the resource. \n[Command Reference](changeLogLogGroup)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--log-id', required=True, help=u"""OCID of a log to work with.""")
@cli_util.option('--target-log-group-id', help=u"""Log group OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_log_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, log_id, target_log_group_id, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    if isinstance(log_id, six.string_types) and len(log_id.strip()) == 0:
        raise click.UsageError('Parameter --log-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if target_log_group_id is not None:
        _details['targetLogGroupId'] = target_log_group_id

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.change_log_log_group(
        log_group_id=log_group_id,
        log_id=log_id,
        change_log_log_group_details=_details,
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


@log_saved_search_group.command(name=cli_util.override('logging.change_log_saved_search_compartment.command_name', 'change-compartment'), help=u"""Moves a saved search into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeLogSavedSearchCompartment)""")
@cli_util.option('--log-saved-search-id', required=True, help=u"""OCID of the logSavedSearch""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_log_saved_search_compartment(ctx, from_json, log_saved_search_id, compartment_id, if_match):

    if isinstance(log_saved_search_id, six.string_types) and len(log_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --log-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.change_log_saved_search_compartment(
        log_saved_search_id=log_saved_search_id,
        change_log_saved_search_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@unified_agent_configuration_group.command(name=cli_util.override('logging.change_unified_agent_configuration_compartment.command_name', 'change-compartment'), help=u"""Moves the unified agent configuration into a different compartment within the same tenancy.  When provided, the If-Match is checked against the ETag values of the resource. For information about moving resources between compartments, see [Moving Resources Between Compartments]. \n[Command Reference](changeUnifiedAgentConfigurationCompartment)""")
@cli_util.option('--unified-agent-configuration-id', required=True, help=u"""The OCID of the Unified Agent configuration.""")
@cli_util.option('--compartment-id', help=u"""The OCID the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_unified_agent_configuration_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, unified_agent_configuration_id, compartment_id, if_match):

    if isinstance(unified_agent_configuration_id, six.string_types) and len(unified_agent_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --unified-agent-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.change_unified_agent_configuration_compartment(
        unified_agent_configuration_id=unified_agent_configuration_id,
        change_unified_agent_configuration_compartment_details=_details,
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


@log_group.command(name=cli_util.override('logging.create_log.command_name', 'create'), help=u"""Creates a log within the specified log group. This call fails if a log group has already been created with the same displayName or (service, resource, category) triplet. \n[Command Reference](createLog)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--log-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CUSTOM", "SERVICE"]), help=u"""The logType that the log object is for, whether custom or service.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--retention-duration', type=click.INT, help=u"""Log retention duration in 30-day increments (30, 60, 90 and so on).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'configuration': {'module': 'logging', 'class': 'Configuration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'configuration': {'module': 'logging', 'class': 'Configuration'}})
@cli_util.wrap_exceptions
def create_log(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, display_name, log_type, is_enabled, defined_tags, freeform_tags, configuration, retention_duration):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['logType'] = log_type

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if retention_duration is not None:
        _details['retentionDuration'] = retention_duration

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.create_log(
        log_group_id=log_group_id,
        create_log_details=_details,
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


@log_group_group.command(name=cli_util.override('logging.create_log_group.command_name', 'create'), help=u"""Create a new log group with a unique display name. This call fails if the log group is already created with the same displayName in the compartment. \n[Command Reference](createLogGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the resource belongs to.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def create_log_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.create_log_group(
        create_log_group_details=_details,
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


@log_saved_search_group.command(name=cli_util.override('logging.create_log_saved_search.command_name', 'create'), help=u"""Creates a new LogSavedSearch. \n[Command Reference](createLogSavedSearch)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the resource belongs to.""")
@cli_util.option('--name', required=True, help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--query-parameterconflict', required=True, help=u"""The search query that is saved.""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}}, output_type={'module': 'logging', 'class': 'LogSavedSearch'})
@cli_util.wrap_exceptions
def create_log_saved_search(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, query_parameterconflict, description, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['query'] = query_parameterconflict

    if description is not None:
        _details['description'] = description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.create_log_saved_search(
        create_log_saved_search_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_saved_search') and callable(getattr(client, 'get_log_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_saved_search(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@unified_agent_configuration_group.command(name=cli_util.override('logging.create_unified_agent_configuration.command_name', 'create'), help=u"""Create unified agent configuration registration. \n[Command Reference](createUnifiedAgentConfiguration)""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--service-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the resource belongs to.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--group-association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'service-configuration': {'module': 'logging', 'class': 'UnifiedAgentServiceConfigurationDetails'}, 'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-configuration': {'module': 'logging', 'class': 'UnifiedAgentServiceConfigurationDetails'}, 'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}})
@cli_util.wrap_exceptions
def create_unified_agent_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, is_enabled, service_configuration, compartment_id, display_name, defined_tags, freeform_tags, description, group_association):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled
    _details['serviceConfiguration'] = cli_util.parse_json_parameter("service_configuration", service_configuration)
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if description is not None:
        _details['description'] = description

    if group_association is not None:
        _details['groupAssociation'] = cli_util.parse_json_parameter("group_association", group_association)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.create_unified_agent_configuration(
        create_unified_agent_configuration_details=_details,
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


@unified_agent_configuration_group.command(name=cli_util.override('logging.create_unified_agent_configuration_unified_agent_logging_configuration.command_name', 'create-unified-agent-configuration-unified-agent-logging-configuration'), help=u"""Create unified agent configuration registration. \n[Command Reference](createUnifiedAgentConfiguration)""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that the resource belongs to.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--group-association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-configuration-sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type UnifiedAgentLoggingSource.  For documentation on UnifiedAgentLoggingSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loggingmanagement/20200531/datatypes/UnifiedAgentLoggingSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-configuration-destination', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-configuration-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-configuration-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-configuration-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-configuration-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.wrap_exceptions
def create_unified_agent_configuration_unified_agent_logging_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, is_enabled, compartment_id, display_name, defined_tags, freeform_tags, description, group_association, service_configuration_sources, service_configuration_destination):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceConfiguration'] = {}
    _details['isEnabled'] = is_enabled
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if description is not None:
        _details['description'] = description

    if group_association is not None:
        _details['groupAssociation'] = cli_util.parse_json_parameter("group_association", group_association)

    if service_configuration_sources is not None:
        _details['serviceConfiguration']['sources'] = cli_util.parse_json_parameter("service_configuration_sources", service_configuration_sources)

    if service_configuration_destination is not None:
        _details['serviceConfiguration']['destination'] = cli_util.parse_json_parameter("service_configuration_destination", service_configuration_destination)

    _details['serviceConfiguration']['configurationType'] = 'LOGGING'

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.create_unified_agent_configuration(
        create_unified_agent_configuration_details=_details,
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


@log_group.command(name=cli_util.override('logging.delete_log.command_name', 'delete'), help=u"""Deletes the log object in a log group. \n[Command Reference](deleteLog)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--log-id', required=True, help=u"""OCID of a log to work with.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, log_id, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    if isinstance(log_id, six.string_types) and len(log_id.strip()) == 0:
        raise click.UsageError('Parameter --log-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.delete_log(
        log_group_id=log_group_id,
        log_id=log_id,
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


@log_group_group.command(name=cli_util.override('logging.delete_log_group.command_name', 'delete'), help=u"""Deletes the specified log group. \n[Command Reference](deleteLogGroup)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.delete_log_group(
        log_group_id=log_group_id,
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


@log_saved_search_group.command(name=cli_util.override('logging.delete_log_saved_search.command_name', 'delete'), help=u"""Deletes the specified log saved search. \n[Command Reference](deleteLogSavedSearch)""")
@cli_util.option('--log-saved-search-id', required=True, help=u"""OCID of the logSavedSearch""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_log_saved_search(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, log_saved_search_id, if_match):

    if isinstance(log_saved_search_id, six.string_types) and len(log_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --log-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.delete_log_saved_search(
        log_saved_search_id=log_saved_search_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_saved_search') and callable(getattr(client, 'get_log_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_log_saved_search(log_saved_search_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@unified_agent_configuration_group.command(name=cli_util.override('logging.delete_unified_agent_configuration.command_name', 'delete'), help=u"""Delete unified agent configuration. \n[Command Reference](deleteUnifiedAgentConfiguration)""")
@cli_util.option('--unified-agent-configuration-id', required=True, help=u"""The OCID of the Unified Agent configuration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_unified_agent_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, unified_agent_configuration_id, if_match):

    if isinstance(unified_agent_configuration_id, six.string_types) and len(unified_agent_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --unified-agent-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.delete_unified_agent_configuration(
        unified_agent_configuration_id=unified_agent_configuration_id,
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


@work_request_group.command(name=cli_util.override('logging.delete_work_request.command_name', 'delete'), help=u"""Cancel a work request that has not started yet. \n[Command Reference](deleteWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The asynchronous request ID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_work_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
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


@log_group.command(name=cli_util.override('logging.get_log.command_name', 'get'), help=u"""Gets the log object configuration for the log object OCID. \n[Command Reference](getLog)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--log-id', required=True, help=u"""OCID of a log to work with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'Log'})
@cli_util.wrap_exceptions
def get_log(ctx, from_json, log_group_id, log_id):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    if isinstance(log_id, six.string_types) and len(log_id.strip()) == 0:
        raise click.UsageError('Parameter --log-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_log(
        log_group_id=log_group_id,
        log_id=log_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_group_group.command(name=cli_util.override('logging.get_log_group.command_name', 'get'), help=u"""Get the specified log group's information. \n[Command Reference](getLogGroup)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'LogGroup'})
@cli_util.wrap_exceptions
def get_log_group(ctx, from_json, log_group_id):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_log_group(
        log_group_id=log_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_included_search_group.command(name=cli_util.override('logging.get_log_included_search.command_name', 'get'), help=u"""Retrieves a LogIncludedSearch. \n[Command Reference](getLogIncludedSearch)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--log-included-search-id', required=True, help=u"""OCID of the included search""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'LogIncludedSearch'})
@cli_util.wrap_exceptions
def get_log_included_search(ctx, from_json, compartment_id, log_included_search_id):

    if isinstance(log_included_search_id, six.string_types) and len(log_included_search_id.strip()) == 0:
        raise click.UsageError('Parameter --log-included-search-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_log_included_search(
        compartment_id=compartment_id,
        log_included_search_id=log_included_search_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_saved_search_group.command(name=cli_util.override('logging.get_log_saved_search.command_name', 'get'), help=u"""Retrieves a log saved search. \n[Command Reference](getLogSavedSearch)""")
@cli_util.option('--log-saved-search-id', required=True, help=u"""OCID of the logSavedSearch""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'LogSavedSearch'})
@cli_util.wrap_exceptions
def get_log_saved_search(ctx, from_json, log_saved_search_id):

    if isinstance(log_saved_search_id, six.string_types) and len(log_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --log-saved-search-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_log_saved_search(
        log_saved_search_id=log_saved_search_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@unified_agent_configuration_group.command(name=cli_util.override('logging.get_unified_agent_configuration.command_name', 'get'), help=u"""Get the unified agent configuration for an ID. \n[Command Reference](getUnifiedAgentConfiguration)""")
@cli_util.option('--unified-agent-configuration-id', required=True, help=u"""The OCID of the Unified Agent configuration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'UnifiedAgentConfiguration'})
@cli_util.wrap_exceptions
def get_unified_agent_configuration(ctx, from_json, unified_agent_configuration_id):

    if isinstance(unified_agent_configuration_id, six.string_types) and len(unified_agent_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --unified-agent-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_unified_agent_configuration(
        unified_agent_configuration_id=unified_agent_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('logging.get_work_request.command_name', 'get'), help=u"""Gets the details of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The asynchronous request ID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@log_group_group.command(name=cli_util.override('logging.list_log_groups.command_name', 'list'), help=u"""Lists all log groups for the specified compartment or tenancy. \n[Command Reference](listLogGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Specifies whether or not nested compartments should be traversed. Defaults to false.""")
@cli_util.option('--display-name', help=u"""Resource name""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[LogGroupSummary]'})
@cli_util.wrap_exceptions
def list_log_groups(ctx, from_json, all_pages, page_size, compartment_id, is_compartment_id_in_subtree, display_name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if display_name is not None:
        kwargs['display_name'] = display_name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_included_search_group.command(name=cli_util.override('logging.list_log_included_searches.command_name', 'list'), help=u"""Lists Logging Included Searches for this compartment. \n[Command Reference](listLogIncludedSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--log-included-search-id', help=u"""OCID of the LogIncludedSearch""")
@cli_util.option('--display-name', help=u"""Resource name""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'LogIncludedSearchSummaryCollection'})
@cli_util.wrap_exceptions
def list_log_included_searches(ctx, from_json, all_pages, page_size, compartment_id, log_included_search_id, display_name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if log_included_search_id is not None:
        kwargs['log_included_search_id'] = log_included_search_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_included_searches,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_included_searches,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_included_searches(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_saved_search_group.command(name=cli_util.override('logging.list_log_saved_searches.command_name', 'list'), help=u"""Lists Logging Saved Searches for this compartment. \n[Command Reference](listLogSavedSearches)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--log-saved-search-id', help=u"""OCID of the LogSavedSearch""")
@cli_util.option('--name', help=u"""Resource name""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'LogSavedSearchSummaryCollection'})
@cli_util.wrap_exceptions
def list_log_saved_searches(ctx, from_json, all_pages, page_size, compartment_id, log_saved_search_id, name, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if log_saved_search_id is not None:
        kwargs['log_saved_search_id'] = log_saved_search_id
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_log_saved_searches,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_log_saved_searches,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_log_saved_searches(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@log_group.command(name=cli_util.override('logging.list_logs.command_name', 'list'), help=u"""Lists the specified log group's log objects. \n[Command Reference](listLogs)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--log-type', type=custom_types.CliCaseInsensitiveChoice(["CUSTOM", "SERVICE"]), help=u"""The logType that the log object is for, whether custom or service.""")
@cli_util.option('--source-service', help=u"""Service that created the log object.""")
@cli_util.option('--source-resource', help=u"""Log object resource.""")
@cli_util.option('--display-name', help=u"""Resource name""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]), help=u"""Lifecycle state of the log object""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[LogSummary]'})
@cli_util.wrap_exceptions
def list_logs(ctx, from_json, all_pages, page_size, log_group_id, log_type, source_service, source_resource, display_name, lifecycle_state, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    kwargs = {}
    if log_type is not None:
        kwargs['log_type'] = log_type
    if source_service is not None:
        kwargs['source_service'] = source_service
    if source_resource is not None:
        kwargs['source_resource'] = source_resource
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_logs,
            log_group_id=log_group_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_logs,
            limit,
            page_size,
            log_group_id=log_group_id,
            **kwargs
        )
    else:
        result = client.list_logs(
            log_group_id=log_group_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_group.command(name=cli_util.override('logging.list_services.command_name', 'list'), help=u"""Lists all services that support logging. \n[Command Reference](listServices)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[ServiceSummary]'})
@cli_util.wrap_exceptions
def list_services(ctx, from_json, all_pages, ):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.list_services(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@unified_agent_configuration_group.command(name=cli_util.override('logging.list_unified_agent_configurations.command_name', 'list'), help=u"""Lists all unified agent configurations in the specified compartment. \n[Command Reference](listUnifiedAgentConfigurations)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--log-id', help=u"""Custom log OCID to list resources with the log as destination.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Specifies whether or not nested compartments should be traversed. Defaults to false.""")
@cli_util.option('--group-id', help=u"""The OCID of a group or a dynamic group.""")
@cli_util.option('--display-name', help=u"""Resource name""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]), help=u"""Lifecycle state of the log object""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by (one column only). Default sort order is ascending exception of `timeCreated` and `timeLastModified` columns (descending).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'UnifiedAgentConfigurationCollection'})
@cli_util.wrap_exceptions
def list_unified_agent_configurations(ctx, from_json, all_pages, page_size, compartment_id, log_id, is_compartment_id_in_subtree, group_id, display_name, lifecycle_state, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if log_id is not None:
        kwargs['log_id'] = log_id
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if group_id is not None:
        kwargs['group_id'] = group_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_unified_agent_configurations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_unified_agent_configurations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_unified_agent_configurations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('logging.list_work_request_errors.command_name', 'list'), help=u"""Return a list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The asynchronous request ID.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[WorkRequestError]'})
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
    client = cli_util.build_client('logging', 'logging_management', ctx)
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


@work_request_log_group.command(name=cli_util.override('logging.list_work_request_logs.command_name', 'list'), help=u"""Return a list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The asynchronous request ID.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[WorkRequestLog]'})
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
    client = cli_util.build_client('logging', 'logging_management', ctx)
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


@work_request_group.command(name=cli_util.override('logging.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID to list resources in. See compartmentIdInSubtree      for nested compartments traversal.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), help=u"""Filter results by work request status.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` or `opc-previous-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["operationType", "status", "timeAccepted"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other fields default to ascending order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'logging', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, status, id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if status is not None:
        kwargs['status'] = status
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('logging', 'logging_management', ctx)
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


@log_group.command(name=cli_util.override('logging.update_log.command_name', 'update'), help=u"""Updates the existing log object with the associated configuration. This call       fails if the log object does not exist. \n[Command Reference](updateLog)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--log-id', required=True, help=u"""OCID of a log to work with.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--retention-duration', type=click.INT, help=u"""Log retention duration in 30-day increments (30, 60, 90 and so on).""")
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'configuration': {'module': 'logging', 'class': 'UpdateConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'configuration': {'module': 'logging', 'class': 'UpdateConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_log(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, log_id, display_name, is_enabled, defined_tags, freeform_tags, retention_duration, configuration, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')

    if isinstance(log_id, six.string_types) and len(log_id.strip()) == 0:
        raise click.UsageError('Parameter --log-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or configuration:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and configuration will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if retention_duration is not None:
        _details['retentionDuration'] = retention_duration

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.update_log(
        log_group_id=log_group_id,
        log_id=log_id,
        update_log_details=_details,
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


@log_group_group.command(name=cli_util.override('logging.update_log_group.command_name', 'update'), help=u"""Updates the existing log group with the associated configuration. This call       fails if the log group does not exist. \n[Command Reference](updateLogGroup)""")
@cli_util.option('--log-group-id', required=True, help=u"""OCID of a log group to work with.""")
@cli_util.option('--display-name', help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_log_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, log_group_id, display_name, description, defined_tags, freeform_tags, if_match):

    if isinstance(log_group_id, six.string_types) and len(log_group_id.strip()) == 0:
        raise click.UsageError('Parameter --log-group-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
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

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.update_log_group(
        log_group_id=log_group_id,
        update_log_group_details=_details,
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


@log_saved_search_group.command(name=cli_util.override('logging.update_log_saved_search.command_name', 'update'), help=u"""Updates an  existing log saved search. \n[Command Reference](updateLogSavedSearch)""")
@cli_util.option('--log-saved-search-id', required=True, help=u"""OCID of the logSavedSearch""")
@cli_util.option('--name', help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--query-parameterconflict', help=u"""The search query that is saved.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "INACTIVE", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}}, output_type={'module': 'logging', 'class': 'LogSavedSearch'})
@cli_util.wrap_exceptions
def update_log_saved_search(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, log_saved_search_id, name, description, query_parameterconflict, defined_tags, freeform_tags, if_match):

    if isinstance(log_saved_search_id, six.string_types) and len(log_saved_search_id.strip()) == 0:
        raise click.UsageError('Parameter --log-saved-search-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if query_parameterconflict is not None:
        _details['query'] = query_parameterconflict

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.update_log_saved_search(
        log_saved_search_id=log_saved_search_id,
        update_log_saved_search_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_log_saved_search') and callable(getattr(client, 'get_log_saved_search')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_log_saved_search(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@unified_agent_configuration_group.command(name=cli_util.override('logging.update_unified_agent_configuration.command_name', 'update'), help=u"""Update an existing unified agent configuration. This call       fails if the log group does not exist. \n[Command Reference](updateUnifiedAgentConfiguration)""")
@cli_util.option('--unified-agent-configuration-id', required=True, help=u"""The OCID of the Unified Agent configuration.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--service-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--group-association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'service-configuration': {'module': 'logging', 'class': 'UnifiedAgentServiceConfigurationDetails'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'service-configuration': {'module': 'logging', 'class': 'UnifiedAgentServiceConfigurationDetails'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}})
@cli_util.wrap_exceptions
def update_unified_agent_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, unified_agent_configuration_id, display_name, is_enabled, service_configuration, defined_tags, freeform_tags, description, group_association, if_match):

    if isinstance(unified_agent_configuration_id, six.string_types) and len(unified_agent_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --unified-agent-configuration-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or service_configuration or group_association:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and service-configuration and group-association will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['isEnabled'] = is_enabled
    _details['serviceConfiguration'] = cli_util.parse_json_parameter("service_configuration", service_configuration)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if description is not None:
        _details['description'] = description

    if group_association is not None:
        _details['groupAssociation'] = cli_util.parse_json_parameter("group_association", group_association)

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.update_unified_agent_configuration(
        unified_agent_configuration_id=unified_agent_configuration_id,
        update_unified_agent_configuration_details=_details,
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


@unified_agent_configuration_group.command(name=cli_util.override('logging.update_unified_agent_configuration_unified_agent_logging_configuration.command_name', 'update-unified-agent-configuration-unified-agent-logging-configuration'), help=u"""Update an existing unified agent configuration. This call       fails if the log group does not exist. \n[Command Reference](updateUnifiedAgentConfiguration)""")
@cli_util.option('--unified-agent-configuration-id', required=True, help=u"""The OCID of the Unified Agent configuration.""")
@cli_util.option('--display-name', required=True, help=u"""The user-friendly display name. This must be unique within the enclosing resource, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether or not this resource is currently enabled.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description for this resource.""")
@cli_util.option('--group-association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--service-configuration-sources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type UnifiedAgentLoggingSource.  For documentation on UnifiedAgentLoggingSource please see our API reference: https://docs.cloud.oracle.com/api/#/en/loggingmanagement/20200531/datatypes/UnifiedAgentLoggingSource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-configuration-destination', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-configuration-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-configuration-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'logging', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'logging', 'class': 'dict(str, string)'}, 'group-association': {'module': 'logging', 'class': 'GroupAssociationDetails'}, 'service-configuration-sources': {'module': 'logging', 'class': 'list[UnifiedAgentLoggingSource]'}, 'service-configuration-destination': {'module': 'logging', 'class': 'UnifiedAgentLoggingDestination'}})
@cli_util.wrap_exceptions
def update_unified_agent_configuration_unified_agent_logging_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, unified_agent_configuration_id, display_name, is_enabled, defined_tags, freeform_tags, description, group_association, if_match, service_configuration_sources, service_configuration_destination):

    if isinstance(unified_agent_configuration_id, six.string_types) and len(unified_agent_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --unified-agent-configuration-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or group_association:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and group-association will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceConfiguration'] = {}
    _details['displayName'] = display_name
    _details['isEnabled'] = is_enabled

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if description is not None:
        _details['description'] = description

    if group_association is not None:
        _details['groupAssociation'] = cli_util.parse_json_parameter("group_association", group_association)

    if service_configuration_sources is not None:
        _details['serviceConfiguration']['sources'] = cli_util.parse_json_parameter("service_configuration_sources", service_configuration_sources)

    if service_configuration_destination is not None:
        _details['serviceConfiguration']['destination'] = cli_util.parse_json_parameter("service_configuration_destination", service_configuration_destination)

    _details['serviceConfiguration']['configurationType'] = 'LOGGING'

    client = cli_util.build_client('logging', 'logging_management', ctx)
    result = client.update_unified_agent_configuration(
        unified_agent_configuration_id=unified_agent_configuration_id,
        update_unified_agent_configuration_details=_details,
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
