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


@cli.command(cli_util.override('autoscaling.autoscaling_root_group.command_name', 'autoscaling'), cls=CommandGroupWithAlias, help=cli_util.override('autoscaling.autoscaling_root_group.help', """APIs for dynamically scaling Compute resources to meet application requirements. For more information about
autoscaling, see [Autoscaling]. For information about the
Compute service, see [Overview of the Compute Service].

**Note:** Autoscaling is not available in US Government Cloud tenancies. For more information, see
[Oracle Cloud Infrastructure US Government Cloud]."""), short_help=cli_util.override('autoscaling.autoscaling_root_group.short_help', """Autoscaling API"""))
@cli_util.help_option_group
def autoscaling_root_group():
    pass


@click.command(cli_util.override('autoscaling.auto_scaling_configuration_group.command_name', 'auto-scaling-configuration'), cls=CommandGroupWithAlias, help="""An autoscaling configuration lets you dynamically scale the resources in a Compute instance pool. For more information, see [Autoscaling].""")
@cli_util.help_option_group
def auto_scaling_configuration_group():
    pass


@click.command(cli_util.override('autoscaling.auto_scaling_policy_summary_group.command_name', 'auto-scaling-policy-summary'), cls=CommandGroupWithAlias, help="""Summary information for an autoscaling policy.""")
@cli_util.help_option_group
def auto_scaling_policy_summary_group():
    pass


@click.command(cli_util.override('autoscaling.auto_scaling_policy_group.command_name', 'auto-scaling-policy'), cls=CommandGroupWithAlias, help="""Autoscaling policies define the criteria that trigger autoscaling actions and the actions to take.

An autoscaling policy is part of an autoscaling configuration. For more information, see [Autoscaling].

You can create the following types of autoscaling policies:

  - **Schedule-based:** Autoscaling events take place at the specific times that you schedule.   - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.""")
@cli_util.help_option_group
def auto_scaling_policy_group():
    pass


autoscaling_root_group.add_command(auto_scaling_configuration_group)
autoscaling_root_group.add_command(auto_scaling_policy_summary_group)
autoscaling_root_group.add_command(auto_scaling_policy_group)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.change_auto_scaling_configuration_compartment.command_name', 'change-compartment'), help=u"""Moves an autoscaling configuration into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

When you move an autoscaling configuration to a different compartment, associated resources such as instance pools are not moved. \n[Command Reference](changeAutoScalingConfigurationCompartment)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the autoscaling configuration to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_auto_scaling_configuration_compartment(ctx, from_json, auto_scaling_configuration_id, compartment_id, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.change_auto_scaling_configuration_compartment(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        change_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.create_auto_scaling_configuration.command_name', 'create'), help=u"""Creates an autoscaling configuration. \n[Command Reference](createAutoScalingConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the autoscaling configuration.""")
@cli_util.option('--policies', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cool-down-in-seconds', type=click.INT, help=u"""For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state.

For schedule-based autoscaling policies, this value is not used.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling configuration is enabled.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}, 'resource': {'module': 'autoscaling', 'class': 'Resource'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}, 'resource': {'module': 'autoscaling', 'class': 'Resource'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def create_auto_scaling_configuration(ctx, from_json, compartment_id, policies, resource, defined_tags, display_name, freeform_tags, cool_down_in_seconds, is_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['policies'] = cli_util.parse_json_parameter("policies", policies)
    _details['resource'] = cli_util.parse_json_parameter("resource", resource)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cool_down_in_seconds is not None:
        _details['coolDownInSeconds'] = cool_down_in_seconds

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.create_auto_scaling_configuration(
        create_auto_scaling_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.create_auto_scaling_configuration_instance_pool_resource.command_name', 'create-auto-scaling-configuration-instance-pool-resource'), help=u"""Creates an autoscaling configuration. \n[Command Reference](createAutoScalingConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the autoscaling configuration.""")
@cli_util.option('--policies', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-id', required=True, help=u"""The [OCID] of the resource that is managed by the autoscaling configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cool-down-in-seconds', type=click.INT, help=u"""For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which is also the default. The cooldown period starts when the instance pool reaches the running state.

For schedule-based autoscaling policies, this value is not used.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling configuration is enabled.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def create_auto_scaling_configuration_instance_pool_resource(ctx, from_json, compartment_id, policies, resource_id, defined_tags, display_name, freeform_tags, cool_down_in_seconds, is_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resource'] = {}
    _details['compartmentId'] = compartment_id
    _details['policies'] = cli_util.parse_json_parameter("policies", policies)
    _details['resource']['id'] = resource_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cool_down_in_seconds is not None:
        _details['coolDownInSeconds'] = cool_down_in_seconds

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    _details['resource']['type'] = 'instancePool'

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.create_auto_scaling_configuration(
        create_auto_scaling_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.create_auto_scaling_policy.command_name', 'create'), help=u"""Creates an autoscaling policy for the specified autoscaling configuration.

You can create the following types of autoscaling policies:

- **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.

An autoscaling configuration can either have multiple schedule-based autoscaling policies, or one threshold-based autoscaling policy. \n[Command Reference](createAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--policy-type', required=True, help=u"""The type of autoscaling policy.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy(ctx, from_json, auto_scaling_configuration_id, policy_type, capacity, display_name, is_enabled):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyType'] = policy_type

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.create_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        create_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.create_auto_scaling_policy_create_scheduled_policy_details.command_name', 'create-auto-scaling-policy-create-scheduled-policy-details'), help=u"""Creates an autoscaling policy for the specified autoscaling configuration.

You can create the following types of autoscaling policies:

- **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.

An autoscaling configuration can either have multiple schedule-based autoscaling policies, or one threshold-based autoscaling policy. \n[Command Reference](createAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--execution-schedule', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@cli_util.option('--resource-action', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}, 'resource-action': {'module': 'autoscaling', 'class': 'ResourceAction'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}, 'resource-action': {'module': 'autoscaling', 'class': 'ResourceAction'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy_create_scheduled_policy_details(ctx, from_json, auto_scaling_configuration_id, execution_schedule, capacity, display_name, is_enabled, resource_action):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['executionSchedule'] = cli_util.parse_json_parameter("execution_schedule", execution_schedule)

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if resource_action is not None:
        _details['resourceAction'] = cli_util.parse_json_parameter("resource_action", resource_action)

    _details['policyType'] = 'scheduled'

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.create_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        create_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.create_auto_scaling_policy_create_threshold_policy_details.command_name', 'create-auto-scaling-policy-create-threshold-policy-details'), help=u"""Creates an autoscaling policy for the specified autoscaling configuration.

You can create the following types of autoscaling policies:

- **Schedule-based:** Autoscaling events take place at the specific times that you schedule. - **Threshold-based:** An autoscaling action is triggered when a performance metric meets or exceeds a threshold.

An autoscaling configuration can either have multiple schedule-based autoscaling policies, or one threshold-based autoscaling policy. \n[Command Reference](createAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[CreateConditionDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[CreateConditionDetails]'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy_create_threshold_policy_details(ctx, from_json, auto_scaling_configuration_id, rules, capacity, display_name, is_enabled):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    _details['policyType'] = 'threshold'

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.create_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        create_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.delete_auto_scaling_configuration.command_name', 'delete'), help=u"""Deletes an autoscaling configuration. \n[Command Reference](deleteAutoScalingConfiguration)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_auto_scaling_configuration(ctx, from_json, auto_scaling_configuration_id, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.delete_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.delete_auto_scaling_policy.command_name', 'delete'), help=u"""Deletes an autoscaling policy for the specified autoscaling configuration. \n[Command Reference](deleteAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the autoscaling policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_auto_scaling_policy(ctx, from_json, auto_scaling_configuration_id, auto_scaling_policy_id, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_policy_id, six.string_types) and len(auto_scaling_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.delete_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.get_auto_scaling_configuration.command_name', 'get'), help=u"""Gets information about the specified autoscaling configuration. \n[Command Reference](getAutoScalingConfiguration)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'autoscaling', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def get_auto_scaling_configuration(ctx, from_json, auto_scaling_configuration_id):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.get_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.get_auto_scaling_policy.command_name', 'get'), help=u"""Gets information about the specified autoscaling policy in the specified autoscaling configuration. \n[Command Reference](getAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the autoscaling policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def get_auto_scaling_policy(ctx, from_json, auto_scaling_configuration_id, auto_scaling_policy_id):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_policy_id, six.string_types) and len(auto_scaling_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.get_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.list_auto_scaling_configurations.command_name', 'list'), help=u"""Lists autoscaling configurations in the specifed compartment. \n[Command Reference](listAutoScalingConfigurations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resource. Use tenancyId to search in the root compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'autoscaling', 'class': 'list[AutoScalingConfigurationSummary]'})
@cli_util.wrap_exceptions
def list_auto_scaling_configurations(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_auto_scaling_configurations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_auto_scaling_configurations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_auto_scaling_configurations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_summary_group.command(name=cli_util.override('autoscaling.list_auto_scaling_policies.command_name', 'list-auto-scaling-policies'), help=u"""Lists the autoscaling policies in the specified autoscaling configuration. \n[Command Reference](listAutoScalingPolicies)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'autoscaling', 'class': 'list[AutoScalingPolicySummary]'})
@cli_util.wrap_exceptions
def list_auto_scaling_policies(ctx, from_json, all_pages, page_size, auto_scaling_configuration_id, display_name, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_auto_scaling_policies,
            auto_scaling_configuration_id=auto_scaling_configuration_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_auto_scaling_policies,
            limit,
            page_size,
            auto_scaling_configuration_id=auto_scaling_configuration_id,
            **kwargs
        )
    else:
        result = client.list_auto_scaling_policies(
            auto_scaling_configuration_id=auto_scaling_configuration_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('autoscaling.update_auto_scaling_configuration.command_name', 'update'), help=u"""Updates certain fields on the specified autoscaling configuration, such as the name, the cooldown period, and whether the autoscaling configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling configuration is enabled.""")
@cli_util.option('--cool-down-in-seconds', type=click.INT, help=u"""""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration(ctx, from_json, force, auto_scaling_configuration_id, defined_tags, display_name, freeform_tags, is_enabled, cool_down_in_seconds, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cool_down_in_seconds is not None:
        _details['coolDownInSeconds'] = cool_down_in_seconds

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.update_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.update_auto_scaling_policy.command_name', 'update'), help=u"""Updates an autoscaling policy in the specified autoscaling configuration. \n[Command Reference](updateAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the autoscaling policy.""")
@cli_util.option('--policy-type', required=True, help=u"""Indicates the type of autoscaling policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy(ctx, from_json, force, auto_scaling_configuration_id, auto_scaling_policy_id, policy_type, display_name, capacity, is_enabled, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_policy_id, six.string_types) and len(auto_scaling_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-policy-id cannot be whitespace or empty string')
    if not force:
        if capacity:
            if not click.confirm("WARNING: Updates to capacity will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyType'] = policy_type

    if display_name is not None:
        _details['displayName'] = display_name

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.update_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        update_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.update_auto_scaling_policy_update_threshold_policy_details.command_name', 'update-auto-scaling-policy-update-threshold-policy-details'), help=u"""Updates an autoscaling policy in the specified autoscaling configuration. \n[Command Reference](updateAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the autoscaling policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type UpdateConditionDetails.  For documentation on UpdateConditionDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/autoscaling/20181001/datatypes/UpdateConditionDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[UpdateConditionDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[UpdateConditionDetails]'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy_update_threshold_policy_details(ctx, from_json, force, auto_scaling_configuration_id, auto_scaling_policy_id, display_name, capacity, is_enabled, rules, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_policy_id, six.string_types) and len(auto_scaling_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-policy-id cannot be whitespace or empty string')
    if not force:
        if capacity or rules:
            if not click.confirm("WARNING: Updates to capacity and rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    _details['policyType'] = 'threshold'

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.update_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        update_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('autoscaling.update_auto_scaling_policy_update_scheduled_policy_details.command_name', 'update-auto-scaling-policy-update-scheduled-policy-details'), help=u"""Updates an autoscaling policy in the specified autoscaling configuration. \n[Command Reference](updateAutoScalingPolicy)""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The [OCID] of the autoscaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the autoscaling policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscaling policy is enabled.""")
@cli_util.option('--execution-schedule', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The schedule for executing the autoscaling policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-action', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}, 'resource-action': {'module': 'autoscaling', 'class': 'ResourceAction'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'execution-schedule': {'module': 'autoscaling', 'class': 'ExecutionSchedule'}, 'resource-action': {'module': 'autoscaling', 'class': 'ResourceAction'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy_update_scheduled_policy_details(ctx, from_json, force, auto_scaling_configuration_id, auto_scaling_policy_id, display_name, capacity, is_enabled, execution_schedule, resource_action, if_match):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_policy_id, six.string_types) and len(auto_scaling_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-policy-id cannot be whitespace or empty string')
    if not force:
        if capacity or execution_schedule or resource_action:
            if not click.confirm("WARNING: Updates to capacity and execution-schedule and resource-action will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if capacity is not None:
        _details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if execution_schedule is not None:
        _details['executionSchedule'] = cli_util.parse_json_parameter("execution_schedule", execution_schedule)

    if resource_action is not None:
        _details['resourceAction'] = cli_util.parse_json_parameter("resource_action", resource_action)

    _details['policyType'] = 'scheduled'

    client = cli_util.build_client('autoscaling', 'auto_scaling', ctx)
    result = client.update_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        update_auto_scaling_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
