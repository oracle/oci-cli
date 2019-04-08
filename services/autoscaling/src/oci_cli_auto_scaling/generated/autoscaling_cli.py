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


@cli.command(cli_util.override('autoscaling_root_group.command_name', 'autoscaling'), cls=CommandGroupWithAlias, help=cli_util.override('autoscaling_root_group.help', """Auto Scaling API spec"""), short_help=cli_util.override('autoscaling_root_group.short_help', """Auto Scaling API"""))
@cli_util.help_option_group
def autoscaling_root_group():
    pass


@click.command(cli_util.override('auto_scaling_configuration_group.command_name', 'auto-scaling-configuration'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def auto_scaling_configuration_group():
    pass


@click.command(cli_util.override('auto_scaling_policy_group.command_name', 'auto-scaling-policy'), cls=CommandGroupWithAlias, help="""A Policy defines the rules and actions of an AutoScalingConfiguration. The only supported type is 'threshold'""")
@cli_util.help_option_group
def auto_scaling_policy_group():
    pass


autoscaling_root_group.add_command(auto_scaling_configuration_group)
autoscaling_root_group.add_command(auto_scaling_policy_group)


@auto_scaling_configuration_group.command(name=cli_util.override('create_auto_scaling_configuration.command_name', 'create'), help=u"""Create an AutoScalingConfiguration""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the AutoScalingConfiguration.""")
@cli_util.option('--policies', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the AutoScalingConfiguration. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cool-down-in-seconds', type=click.INT, help=u"""The minimum period of time between scaling actions. The default is 300 seconds.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""If the AutoScalingConfiguration is enabled""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}, 'resource': {'module': 'autoscaling', 'class': 'Resource'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'autoscaling', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'autoscaling', 'class': 'dict(str, string)'}, 'policies': {'module': 'autoscaling', 'class': 'list[CreateAutoScalingPolicyDetails]'}, 'resource': {'module': 'autoscaling', 'class': 'Resource'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def create_auto_scaling_configuration(ctx, from_json, compartment_id, policies, resource, defined_tags, display_name, freeform_tags, cool_down_in_seconds, is_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['policies'] = cli_util.parse_json_parameter("policies", policies)
    details['resource'] = cli_util.parse_json_parameter("resource", resource)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if cool_down_in_seconds is not None:
        details['coolDownInSeconds'] = cool_down_in_seconds

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.create_auto_scaling_configuration(
        create_auto_scaling_configuration_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('create_auto_scaling_policy.command_name', 'create'), help=u"""Create a Policy for AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the Policy""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-type', required=True, help=u"""Indicates type of Policy""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the Policy. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy(ctx, from_json, auto_scaling_configuration_id, capacity, policy_type, display_name):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)
    details['policyType'] = policy_type

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.create_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        create_auto_scaling_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('create_auto_scaling_policy_create_threshold_policy_details.command_name', 'create-auto-scaling-policy-create-threshold-policy-details'), help=u"""Create a Policy for AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--capacity', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the Policy""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name for the Policy. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[CreateConditionDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[CreateConditionDetails]'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def create_auto_scaling_policy_create_threshold_policy_details(ctx, from_json, auto_scaling_configuration_id, capacity, rules, display_name):

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)
    details['rules'] = cli_util.parse_json_parameter("rules", rules)

    if display_name is not None:
        details['displayName'] = display_name

    details['policyType'] = 'threshold'

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.create_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        create_auto_scaling_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('delete_auto_scaling_configuration.command_name', 'delete'), help=u"""Deletes an AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
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
    client = cli_util.build_client('auto_scaling', ctx)
    result = client.delete_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('delete_auto_scaling_policy.command_name', 'delete'), help=u"""Deletes an AutoScalingConfiguration Policy""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the auto scaling configuration policy.""")
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
    client = cli_util.build_client('auto_scaling', ctx)
    result = client.delete_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('get_auto_scaling_configuration.command_name', 'get'), help=u"""Get AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
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
    client = cli_util.build_client('auto_scaling', ctx)
    result = client.get_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('get_auto_scaling_policy.command_name', 'get'), help=u"""Get Policy from a specific AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the auto scaling configuration policy.""")
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
    client = cli_util.build_client('auto_scaling', ctx)
    result = client.get_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_configuration_group.command(name=cli_util.override('list_auto_scaling_configurations.command_name', 'list'), help=u"""Lists AutoScalingConfigurations in the specific compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the resources monitored by the metric that you are searching for. Use tenancyId to search in the root compartment.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call. For information about pagination, see [List Pagination].""")
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
    client = cli_util.build_client('auto_scaling', ctx)
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


@auto_scaling_policy_group.command(name=cli_util.override('list_auto_scaling_policies.command_name', 'list'), help=u"""Lists Policies in an AutoScalingConfiguration.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call. For information about pagination, see [List Pagination].""")
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
    client = cli_util.build_client('auto_scaling', ctx)
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


@auto_scaling_configuration_group.command(name=cli_util.override('update_auto_scaling_configuration.command_name', 'update'), help=u"""Updates an AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""If the AutoScalingConfiguration is enabled""")
@cli_util.option('--cool-down-in-seconds', type=click.INT, help=u"""The minimum period of time between scaling actions. The default is 300 seconds.""")
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

    details = {}

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if is_enabled is not None:
        details['isEnabled'] = is_enabled

    if cool_down_in_seconds is not None:
        details['coolDownInSeconds'] = cool_down_in_seconds

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.update_auto_scaling_configuration(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('update_auto_scaling_policy.command_name', 'update'), help=u"""Updates a Policy in the specific AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the auto scaling configuration policy.""")
@cli_util.option('--policy-type', required=True, help=u"""Indicates type of Policy""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the Policy""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy(ctx, from_json, force, auto_scaling_configuration_id, auto_scaling_policy_id, policy_type, display_name, capacity, if_match):

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

    details = {}
    details['policyType'] = policy_type

    if display_name is not None:
        details['displayName'] = display_name

    if capacity is not None:
        details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.update_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        update_auto_scaling_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auto_scaling_policy_group.command(name=cli_util.override('update_auto_scaling_policy_update_threshold_policy_details.command_name', 'update-auto-scaling-policy-update-threshold-policy-details'), help=u"""Updates a Policy in the specific AutoScalingConfiguration""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""The OCID of the auto scaling configuration.""")
@cli_util.option('--auto-scaling-policy-id', required=True, help=u"""The ID of the auto scaling configuration policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--capacity', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The capacity requirements of the Policy""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type UpdateConditionDetails.  For documentation on UpdateConditionDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/autoscaling/20181001/datatypes/UpdateConditionDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[UpdateConditionDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'capacity': {'module': 'autoscaling', 'class': 'Capacity'}, 'rules': {'module': 'autoscaling', 'class': 'list[UpdateConditionDetails]'}}, output_type={'module': 'autoscaling', 'class': 'AutoScalingPolicy'})
@cli_util.wrap_exceptions
def update_auto_scaling_policy_update_threshold_policy_details(ctx, from_json, force, auto_scaling_configuration_id, auto_scaling_policy_id, display_name, capacity, rules, if_match):

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

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if capacity is not None:
        details['capacity'] = cli_util.parse_json_parameter("capacity", capacity)

    if rules is not None:
        details['rules'] = cli_util.parse_json_parameter("rules", rules)

    details['policyType'] = 'threshold'

    client = cli_util.build_client('auto_scaling', ctx)
    result = client.update_auto_scaling_policy(
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        auto_scaling_policy_id=auto_scaling_policy_id,
        update_auto_scaling_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
