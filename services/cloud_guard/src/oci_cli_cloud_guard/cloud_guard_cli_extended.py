# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import sys
import six
import oci
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.cloud_guard.src.oci_cli_cloud_guard.generated import cloudguard_cli


@cli_util.copy_params_from_generated_command(cloudguard_cli.list_problems, params_to_exclude=['region_parameterconflict'])
@cloudguard_cli.problem_group.command(name=cli_util.override('cloud_guard.list_problems.command_name', 'list'), help=cloudguard_cli.list_problems.help)
@cli_util.option('--problem-region', help=u"""OCI Monitoring region.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rule-id-list': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'list[ProblemSummary]'})
@cli_util.wrap_exceptions
def list_problems_extended(ctx, **kwargs):
    if 'problem_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['problem_region']
        kwargs.pop('problem_region')
    ctx.invoke(cloudguard_cli.list_problems, **kwargs)


cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.create_data_mask_rule.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.create_data_mask_rule_all_targets_selected.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.create_data_mask_rule_target_resource_types_selected.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.create_data_mask_rule_target_ids_selected.name)

cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.update_data_mask_rule.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.update_data_mask_rule_all_targets_selected.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.update_data_mask_rule_target_resource_types_selected.name)
cloudguard_cli.data_mask_rule_group.commands.pop(cloudguard_cli.update_data_mask_rule_target_ids_selected.name)


@cli_util.copy_params_from_generated_command(cloudguard_cli.create_data_mask_rule, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="create", help=cloudguard_cli.create_data_mask_rule.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-selected': {'module': 'cloud_guard', 'class': 'TargetSelected'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def create_data_mask_rule_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, iam_group_id, target_selected, data_mask_categories, description, data_mask_rule_status, lifecycle_state, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['iamGroupId'] = iam_group_id
    _details['targetSelected'] = cli_util.parse_json_parameter("target_selected", target_selected)
    _details['dataMaskCategories'] = data_mask_categories

    if description is not None:
        _details['description'] = description

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_data_mask_rule(
        create_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.create_data_mask_rule_all_targets_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="create-for-all-targets", help=cloudguard_cli.create_data_mask_rule_all_targets_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def create_data_mask_rule_all_targets_selected_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, iam_group_id, data_mask_categories, description, data_mask_rule_status, lifecycle_state, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['iamGroupId'] = iam_group_id
    _details['dataMaskCategories'] = data_mask_categories

    if description is not None:
        _details['description'] = description

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['targetSelected']['kind'] = 'ALL'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_data_mask_rule(
        create_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.create_data_mask_rule_target_resource_types_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="create-for-services", help=cloudguard_cli.create_data_mask_rule_target_resource_types_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def create_data_mask_rule_target_resource_types_selected_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, iam_group_id, data_mask_categories, description, data_mask_rule_status, lifecycle_state, freeform_tags, defined_tags, target_selected_values):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['iamGroupId'] = iam_group_id
    _details['dataMaskCategories'] = data_mask_categories

    if description is not None:
        _details['description'] = description

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_selected_values is not None:
        _details['targetSelected']['values'] = target_selected_values

    _details['targetSelected']['kind'] = 'TARGETTYPES'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_data_mask_rule(
        create_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.create_data_mask_rule_target_ids_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="create-for-targets", help=cloudguard_cli.create_data_mask_rule_target_ids_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}, 'target-selected-values': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def create_data_mask_rule_target_ids_selected_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, iam_group_id, data_mask_categories, description, data_mask_rule_status, lifecycle_state, freeform_tags, defined_tags, target_selected_values):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['iamGroupId'] = iam_group_id
    _details['dataMaskCategories'] = data_mask_categories

    if description is not None:
        _details['description'] = description

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_selected_values is not None:
        _details['targetSelected']['values'] = cli_util.parse_json_parameter("target_selected_values", target_selected_values)

    _details['targetSelected']['kind'] = 'TARGETIDS'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_data_mask_rule(
        create_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.update_data_mask_rule, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="update", help=cloudguard_cli.update_data_mask_rule.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-selected': {'module': 'cloud_guard', 'class': 'TargetSelected'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def update_data_mask_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_mask_rule_id, display_name, compartment_id, iam_group_id, target_selected, data_mask_categories, data_mask_rule_status, freeform_tags, defined_tags, if_match):

    if isinstance(data_mask_rule_id, six.string_types) and len(data_mask_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --data-mask-rule-id cannot be whitespace or empty string')
    if not force:
        if target_selected or data_mask_categories or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to target-selected and data-mask-categories and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if iam_group_id is not None:
        _details['iamGroupId'] = iam_group_id

    if target_selected is not None:
        _details['targetSelected'] = cli_util.parse_json_parameter("target_selected", target_selected)

    if data_mask_categories is not None:
        _details['dataMaskCategories'] = data_mask_categories

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_data_mask_rule(
        data_mask_rule_id=data_mask_rule_id,
        update_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.update_data_mask_rule_all_targets_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="update-for-all-targets", help=cloudguard_cli.update_data_mask_rule_all_targets_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def update_data_mask_rule_all_targets_selected_extended(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_mask_rule_id, display_name, compartment_id, iam_group_id, data_mask_categories, data_mask_rule_status, freeform_tags, defined_tags, if_match):

    if isinstance(data_mask_rule_id, six.string_types) and len(data_mask_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --data-mask-rule-id cannot be whitespace or empty string')
    if not force:
        if data_mask_categories or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to data-mask-categories and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if iam_group_id is not None:
        _details['iamGroupId'] = iam_group_id

    if data_mask_categories is not None:
        _details['dataMaskCategories'] = data_mask_categories

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['targetSelected']['kind'] = 'ALL'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_data_mask_rule(
        data_mask_rule_id=data_mask_rule_id,
        update_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.update_data_mask_rule_target_resource_types_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="update-for-services", help=cloudguard_cli.update_data_mask_rule_target_resource_types_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def update_data_mask_rule_target_resource_types_selected_extended(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_mask_rule_id, display_name, compartment_id, iam_group_id, data_mask_categories, data_mask_rule_status, freeform_tags, defined_tags, if_match, target_selected_values):

    if isinstance(data_mask_rule_id, six.string_types) and len(data_mask_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --data-mask-rule-id cannot be whitespace or empty string')
    if not force:
        if data_mask_categories or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to data-mask-categories and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if iam_group_id is not None:
        _details['iamGroupId'] = iam_group_id

    if data_mask_categories is not None:
        _details['dataMaskCategories'] = data_mask_categories

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_selected_values is not None:
        _details['targetSelected']['values'] = target_selected_values

    _details['targetSelected']['kind'] = 'TARGETTYPES'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_data_mask_rule(
        data_mask_rule_id=data_mask_rule_id,
        update_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(cloudguard_cli.update_data_mask_rule_target_ids_selected, params_to_exclude=[])
@cloudguard_cli.data_mask_rule_group.command(name="update-for-targets", help=cloudguard_cli.update_data_mask_rule_target_ids_selected.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}, 'target-selected-values': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'DataMaskRule'})
@cli_util.wrap_exceptions
def update_data_mask_rule_target_ids_selected_extended(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, data_mask_rule_id, display_name, compartment_id, iam_group_id, data_mask_categories, data_mask_rule_status, freeform_tags, defined_tags, if_match, target_selected_values):

    if isinstance(data_mask_rule_id, six.string_types) and len(data_mask_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --data-mask-rule-id cannot be whitespace or empty string')
    if not force:
        if data_mask_categories or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to data-mask-categories and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetSelected'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if iam_group_id is not None:
        _details['iamGroupId'] = iam_group_id

    if data_mask_categories is not None:
        _details['dataMaskCategories'] = data_mask_categories

    if data_mask_rule_status is not None:
        _details['dataMaskRuleStatus'] = data_mask_rule_status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if target_selected_values is not None:
        _details['targetSelected']['values'] = cli_util.parse_json_parameter("target_selected_values", target_selected_values)

    _details['targetSelected']['kind'] = 'TARGETIDS'

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_data_mask_rule(
        data_mask_rule_id=data_mask_rule_id,
        update_data_mask_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_mask_rule') and callable(getattr(client, 'get_data_mask_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_mask_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
