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


@cli.command(cli_util.override('cloud_guard.cloud_guard_root_group.command_name', 'cloud-guard'), cls=CommandGroupWithAlias, help=cli_util.override('cloud_guard.cloud_guard_root_group.help', """A description of the Cloud Guard APIs"""), short_help=cli_util.override('cloud_guard.cloud_guard_root_group.short_help', """Cloud Guard APIs"""))
@cli_util.help_option_group
def cloud_guard_root_group():
    pass


@click.command(cli_util.override('cloud_guard.impacted_resource_summary_group.command_name', 'impacted-resource-summary'), cls=CommandGroupWithAlias, help="""Impacted Resource summary Definition.""")
@cli_util.help_option_group
def impacted_resource_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.target_responder_recipe_responder_rule_group.command_name', 'target-responder-recipe-responder-rule'), cls=CommandGroupWithAlias, help="""Details of ResponderRule.""")
@cli_util.help_option_group
def target_responder_recipe_responder_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.problem_trend_aggregation_group.command_name', 'problem-trend-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding time and count.""")
@cli_util.help_option_group
def problem_trend_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""Cloud Guard configuration details of a tenancy.""")
@cli_util.help_option_group
def configuration_group():
    pass


@click.command(cli_util.override('cloud_guard.security_score_trend_aggregation_group.command_name', 'security-score-trend-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding time and security score.""")
@cli_util.help_option_group
def security_score_trend_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_recipe_responder_rule_group.command_name', 'responder-recipe-responder-rule'), cls=CommandGroupWithAlias, help="""Details of ResponderRule.""")
@cli_util.help_option_group
def responder_recipe_responder_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_execution_summary_group.command_name', 'responder-execution-summary'), cls=CommandGroupWithAlias, help="""Summary of the Responder Execution.""")
@cli_util.help_option_group
def responder_execution_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_execution_group.command_name', 'responder-execution'), cls=CommandGroupWithAlias, help="""Responder Execution Object.""")
@cli_util.help_option_group
def responder_execution_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_execution_aggregation_group.command_name', 'responder-execution-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding count value.""")
@cli_util.help_option_group
def responder_execution_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_rule_group.command_name', 'responder-rule'), cls=CommandGroupWithAlias, help="""Definition of ResponderRule.""")
@cli_util.help_option_group
def responder_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.resource_type_summary_group.command_name', 'resource-type-summary'), cls=CommandGroupWithAlias, help="""Summary of ResourceType""")
@cli_util.help_option_group
def resource_type_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.problem_group.command_name', 'problem'), cls=CommandGroupWithAlias, help="""Problem Definition.""")
@cli_util.help_option_group
def problem_group():
    pass


@click.command(cli_util.override('cloud_guard.security_score_aggregation_group.command_name', 'security-score-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding count value.""")
@cli_util.help_option_group
def security_score_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.target_detector_recipe_group.command_name', 'target-detector-recipe'), cls=CommandGroupWithAlias, help="""Target Detector recipe""")
@cli_util.help_option_group
def target_detector_recipe_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_recipe_group.command_name', 'responder-recipe'), cls=CommandGroupWithAlias, help="""Details of ResponderRecipe.""")
@cli_util.help_option_group
def responder_recipe_group():
    pass


@click.command(cli_util.override('cloud_guard.activity_problem_aggregation_group.command_name', 'activity-problem-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding count.""")
@cli_util.help_option_group
def activity_problem_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_execution_trend_aggregation_group.command_name', 'responder-execution-trend-aggregation'), cls=CommandGroupWithAlias, help="""Provides the timestamps and their corresponding number of remediations.""")
@cli_util.help_option_group
def responder_execution_trend_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.condition_metadata_type_group.command_name', 'condition-metadata-type'), cls=CommandGroupWithAlias, help="""condition type provided by cloud guard""")
@cli_util.help_option_group
def condition_metadata_type_group():
    pass


@click.command(cli_util.override('cloud_guard.target_detector_recipe_detector_rule_group.command_name', 'target-detector-recipe-detector-rule'), cls=CommandGroupWithAlias, help="""Detector Recipe Rule""")
@cli_util.help_option_group
def target_detector_recipe_detector_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.detector_recipe_group.command_name', 'detector-recipe'), cls=CommandGroupWithAlias, help="""Details of Detector recipe""")
@cli_util.help_option_group
def detector_recipe_group():
    pass


@click.command(cli_util.override('cloud_guard.detector_recipe_detector_rule_group.command_name', 'detector-recipe-detector-rule'), cls=CommandGroupWithAlias, help="""Detector Recipe Rule""")
@cli_util.help_option_group
def detector_recipe_detector_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.recommendation_summary_group.command_name', 'recommendation-summary'), cls=CommandGroupWithAlias, help="""Recommendation Definition.""")
@cli_util.help_option_group
def recommendation_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.problem_aggregation_group.command_name', 'problem-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding count value.""")
@cli_util.help_option_group
def problem_aggregation_group():
    pass


@click.command(cli_util.override('cloud_guard.target_group.command_name', 'target'), cls=CommandGroupWithAlias, help="""Description of Target.""")
@cli_util.help_option_group
def target_group():
    pass


@click.command(cli_util.override('cloud_guard.responder_activity_summary_group.command_name', 'responder-activity-summary'), cls=CommandGroupWithAlias, help="""Responder Activity summary Definition.""")
@cli_util.help_option_group
def responder_activity_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.managed_list_group.command_name', 'managed-list'), cls=CommandGroupWithAlias, help="""A cloud guard list containing one or more items of a list type""")
@cli_util.help_option_group
def managed_list_group():
    pass


@click.command(cli_util.override('cloud_guard.managed_list_type_summary_group.command_name', 'managed-list-type-summary'), cls=CommandGroupWithAlias, help="""Summary of the ManagedListType.""")
@cli_util.help_option_group
def managed_list_type_summary_group():
    pass


@click.command(cli_util.override('cloud_guard.target_responder_recipe_group.command_name', 'target-responder-recipe'), cls=CommandGroupWithAlias, help="""Details of Target ResponderRecipe""")
@cli_util.help_option_group
def target_responder_recipe_group():
    pass


@click.command(cli_util.override('cloud_guard.detector_group.command_name', 'detector'), cls=CommandGroupWithAlias, help="""A single Detector""")
@cli_util.help_option_group
def detector_group():
    pass


@click.command(cli_util.override('cloud_guard.detector_rule_group.command_name', 'detector-rule'), cls=CommandGroupWithAlias, help="""Detector""")
@cli_util.help_option_group
def detector_rule_group():
    pass


@click.command(cli_util.override('cloud_guard.risk_score_aggregation_group.command_name', 'risk-score-aggregation'), cls=CommandGroupWithAlias, help="""Provides the dimensions and their corresponding risk score.""")
@cli_util.help_option_group
def risk_score_aggregation_group():
    pass


cloud_guard_root_group.add_command(impacted_resource_summary_group)
cloud_guard_root_group.add_command(target_responder_recipe_responder_rule_group)
cloud_guard_root_group.add_command(problem_trend_aggregation_group)
cloud_guard_root_group.add_command(configuration_group)
cloud_guard_root_group.add_command(security_score_trend_aggregation_group)
cloud_guard_root_group.add_command(responder_recipe_responder_rule_group)
cloud_guard_root_group.add_command(responder_execution_summary_group)
cloud_guard_root_group.add_command(responder_execution_group)
cloud_guard_root_group.add_command(responder_execution_aggregation_group)
cloud_guard_root_group.add_command(responder_rule_group)
cloud_guard_root_group.add_command(resource_type_summary_group)
cloud_guard_root_group.add_command(problem_group)
cloud_guard_root_group.add_command(security_score_aggregation_group)
cloud_guard_root_group.add_command(target_detector_recipe_group)
cloud_guard_root_group.add_command(responder_recipe_group)
cloud_guard_root_group.add_command(activity_problem_aggregation_group)
cloud_guard_root_group.add_command(responder_execution_trend_aggregation_group)
cloud_guard_root_group.add_command(condition_metadata_type_group)
cloud_guard_root_group.add_command(target_detector_recipe_detector_rule_group)
cloud_guard_root_group.add_command(detector_recipe_group)
cloud_guard_root_group.add_command(detector_recipe_detector_rule_group)
cloud_guard_root_group.add_command(recommendation_summary_group)
cloud_guard_root_group.add_command(problem_aggregation_group)
cloud_guard_root_group.add_command(target_group)
cloud_guard_root_group.add_command(responder_activity_summary_group)
cloud_guard_root_group.add_command(managed_list_group)
cloud_guard_root_group.add_command(managed_list_type_summary_group)
cloud_guard_root_group.add_command(target_responder_recipe_group)
cloud_guard_root_group.add_command(detector_group)
cloud_guard_root_group.add_command(detector_rule_group)
cloud_guard_root_group.add_command(risk_score_aggregation_group)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.change_detector_recipe_compartment.command_name', 'change-compartment'), help=u"""Moves the DetectorRecipe from current compartment to another. \n[Command Reference](changeDetectorRecipeCompartment)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the DetectorRecipe should be moved""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_detector_recipe_compartment(ctx, from_json, detector_recipe_id, compartment_id, if_match):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.change_detector_recipe_compartment(
        detector_recipe_id=detector_recipe_id,
        change_detector_recipe_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_list_group.command(name=cli_util.override('cloud_guard.change_managed_list_compartment.command_name', 'change-compartment'), help=u"""Moves the ManagedList from current compartment to another. \n[Command Reference](changeManagedListCompartment)""")
@cli_util.option('--managed-list-id', required=True, help=u"""The cloudguard list OCID to be passed in the request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the ManagedList should be moved""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_managed_list_compartment(ctx, from_json, managed_list_id, compartment_id, if_match):

    if isinstance(managed_list_id, six.string_types) and len(managed_list_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-list-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.change_managed_list_compartment(
        managed_list_id=managed_list_id,
        change_managed_list_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_recipe_group.command(name=cli_util.override('cloud_guard.change_responder_recipe_compartment.command_name', 'change-compartment'), help=u"""Moves the ResponderRecipe from current compartment to another. \n[Command Reference](changeResponderRecipeCompartment)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment into which the ResponderRecipe should be moved""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_responder_recipe_compartment(ctx, from_json, responder_recipe_id, compartment_id, if_match):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.change_responder_recipe_compartment(
        responder_recipe_id=responder_recipe_id,
        change_responder_recipe_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.create_detector_recipe.command_name', 'create'), help=u"""Creates a DetectorRecipe \n[Command Reference](createDetectorRecipe)""")
@cli_util.option('--display-name', required=True, help=u"""DetectorRecipe Display Name""")
@cli_util.option('--source-detector-recipe-id', required=True, help=u"""The id of the source detector recipe.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--description', help=u"""DetectorRecipe Description""")
@cli_util.option('--detector-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Detector Rules to override from source detector recipe

This option is a JSON list with items of type UpdateDetectorRecipeDetectorRule.  For documentation on UpdateDetectorRecipeDetectorRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateDetectorRecipeDetectorRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateDetectorRecipeDetectorRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateDetectorRecipeDetectorRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipe'})
@cli_util.wrap_exceptions
def create_detector_recipe(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, source_detector_recipe_id, compartment_id, description, detector_rules, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['sourceDetectorRecipeId'] = source_detector_recipe_id
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if detector_rules is not None:
        _details['detectorRules'] = cli_util.parse_json_parameter("detector_rules", detector_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_detector_recipe(
        create_detector_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_detector_recipe') and callable(getattr(client, 'get_detector_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_detector_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@managed_list_group.command(name=cli_util.override('cloud_guard.create_managed_list.command_name', 'create'), help=u"""Creates a new ManagedList. \n[Command Reference](createManagedList)""")
@cli_util.option('--display-name', required=True, help=u"""ManagedList display name""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--source-managed-list-id', help=u"""OCID of the Source ManagedList""")
@cli_util.option('--description', help=u"""ManagedList description""")
@cli_util.option('--list-type', type=custom_types.CliCaseInsensitiveChoice(["CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS"]), help=u"""type of the list""")
@cli_util.option('--list-items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of ManagedListItem""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'list-items': {'module': 'cloud_guard', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'list-items': {'module': 'cloud_guard', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'ManagedList'})
@cli_util.wrap_exceptions
def create_managed_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, source_managed_list_id, description, list_type, list_items, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if source_managed_list_id is not None:
        _details['sourceManagedListId'] = source_managed_list_id

    if description is not None:
        _details['description'] = description

    if list_type is not None:
        _details['listType'] = list_type

    if list_items is not None:
        _details['listItems'] = cli_util.parse_json_parameter("list_items", list_items)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_managed_list(
        create_managed_list_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_list') and callable(getattr(client, 'get_managed_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@responder_recipe_group.command(name=cli_util.override('cloud_guard.create_responder_recipe.command_name', 'create'), help=u"""Create a ResponderRecipe. \n[Command Reference](createResponderRecipe)""")
@cli_util.option('--display-name', required=True, help=u"""ResponderRecipe Display Name""")
@cli_util.option('--source-responder-recipe-id', required=True, help=u"""The id of the source responder recipe.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier""")
@cli_util.option('--description', help=u"""ResponderRecipe Description""")
@cli_util.option('--responder-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Responder Rules to override from source responder recipe

This option is a JSON list with items of type UpdateResponderRecipeResponderRule.  For documentation on UpdateResponderRecipeResponderRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateResponderRecipeResponderRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateResponderRecipeResponderRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateResponderRecipeResponderRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipe'})
@cli_util.wrap_exceptions
def create_responder_recipe(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, source_responder_recipe_id, compartment_id, description, responder_rules, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['sourceResponderRecipeId'] = source_responder_recipe_id
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if responder_rules is not None:
        _details['responderRules'] = cli_util.parse_json_parameter("responder_rules", responder_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_responder_recipe(
        create_responder_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_responder_recipe') and callable(getattr(client, 'get_responder_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_responder_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_group.command(name=cli_util.override('cloud_guard.create_target.command_name', 'create'), help=u"""Creates a new Target \n[Command Reference](createTarget)""")
@cli_util.option('--display-name', required=True, help=u"""DetectorTemplate Identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier where the resource is created""")
@cli_util.option('--target-resource-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMPARTMENT", "ERPCLOUD", "HCMCLOUD"]), help=u"""possible type of targets(compartment/HCMCloud/ERPCloud)""")
@cli_util.option('--target-resource-id', required=True, help=u"""Resource ID which the target uses to monitor""")
@cli_util.option('--description', help=u"""The target description.""")
@cli_util.option('--target-detector-recipes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of detector recipes to associate with target

This option is a JSON list with items of type CreateTargetDetectorRecipeDetails.  For documentation on CreateTargetDetectorRecipeDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/CreateTargetDetectorRecipeDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-responder-recipes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of responder recipes to associate with target

This option is a JSON list with items of type CreateTargetResponderRecipeDetails.  For documentation on CreateTargetResponderRecipeDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/CreateTargetResponderRecipeDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the DetectorRule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target-detector-recipes': {'module': 'cloud_guard', 'class': 'list[CreateTargetDetectorRecipeDetails]'}, 'target-responder-recipes': {'module': 'cloud_guard', 'class': 'list[CreateTargetResponderRecipeDetails]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-detector-recipes': {'module': 'cloud_guard', 'class': 'list[CreateTargetDetectorRecipeDetails]'}, 'target-responder-recipes': {'module': 'cloud_guard', 'class': 'list[CreateTargetResponderRecipeDetails]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'Target'})
@cli_util.wrap_exceptions
def create_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, target_resource_type, target_resource_id, description, target_detector_recipes, target_responder_recipes, lifecycle_state, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['targetResourceType'] = target_resource_type
    _details['targetResourceId'] = target_resource_id

    if description is not None:
        _details['description'] = description

    if target_detector_recipes is not None:
        _details['targetDetectorRecipes'] = cli_util.parse_json_parameter("target_detector_recipes", target_detector_recipes)

    if target_responder_recipes is not None:
        _details['targetResponderRecipes'] = cli_util.parse_json_parameter("target_responder_recipes", target_responder_recipes)

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_target(
        create_target_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target') and callable(getattr(client, 'get_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_detector_recipe_group.command(name=cli_util.override('cloud_guard.create_target_detector_recipe.command_name', 'create'), help=u"""Attach a DetectorRecipe with the Target \n[Command Reference](createTargetDetectorRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe Identifier""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipe'})
@cli_util.wrap_exceptions
def create_target_detector_recipe(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, detector_recipe_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['detectorRecipeId'] = detector_recipe_id

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_target_detector_recipe(
        target_id=target_id,
        attach_target_detector_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target_detector_recipe') and callable(getattr(client, 'get_target_detector_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target_detector_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_responder_recipe_group.command(name=cli_util.override('cloud_guard.create_target_responder_recipe.command_name', 'create'), help=u"""Attach a ResponderRecipe with the Target \n[Command Reference](createTargetResponderRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""ResponderRecipe Identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipe'})
@cli_util.wrap_exceptions
def create_target_responder_recipe(ctx, from_json, target_id, responder_recipe_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['responderRecipeId'] = responder_recipe_id

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.create_target_responder_recipe(
        target_id=target_id,
        attach_target_responder_recipe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.delete_detector_recipe.command_name', 'delete'), help=u"""Deletes a DetectorRecipe identified by detectorRecipeId \n[Command Reference](deleteDetectorRecipe)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_detector_recipe(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, detector_recipe_id, if_match):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_detector_recipe(
        detector_recipe_id=detector_recipe_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_detector_recipe') and callable(getattr(client, 'get_detector_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_detector_recipe(detector_recipe_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@managed_list_group.command(name=cli_util.override('cloud_guard.delete_managed_list.command_name', 'delete'), help=u"""Deletes a managed list identified by managedListId \n[Command Reference](deleteManagedList)""")
@cli_util.option('--managed-list-id', required=True, help=u"""The cloudguard list OCID to be passed in the request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_managed_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_list_id, if_match):

    if isinstance(managed_list_id, six.string_types) and len(managed_list_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-list-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_managed_list(
        managed_list_id=managed_list_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_list') and callable(getattr(client, 'get_managed_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_managed_list(managed_list_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@responder_recipe_group.command(name=cli_util.override('cloud_guard.delete_responder_recipe.command_name', 'delete'), help=u"""Delete the ResponderRecipe resource by identifier \n[Command Reference](deleteResponderRecipe)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_responder_recipe(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, responder_recipe_id, if_match):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_responder_recipe(
        responder_recipe_id=responder_recipe_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_responder_recipe') and callable(getattr(client, 'get_responder_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_responder_recipe(responder_recipe_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@target_group.command(name=cli_util.override('cloud_guard.delete_target.command_name', 'delete'), help=u"""Deletes a Target identified by targetId \n[Command Reference](deleteTarget)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_target(
        target_id=target_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target') and callable(getattr(client, 'get_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_target(target_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@target_detector_recipe_group.command(name=cli_util.override('cloud_guard.delete_target_detector_recipe.command_name', 'delete'), help=u"""Delete the TargetDetectorRecipe resource by identifier \n[Command Reference](deleteTargetDetectorRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_target_detector_recipe(ctx, from_json, target_id, target_detector_recipe_id, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_target_detector_recipe(
        target_id=target_id,
        target_detector_recipe_id=target_detector_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_responder_recipe_group.command(name=cli_util.override('cloud_guard.delete_target_responder_recipe.command_name', 'delete'), help=u"""Delete the TargetResponderRecipe resource by identifier \n[Command Reference](deleteTargetResponderRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_target_responder_recipe(ctx, from_json, target_id, target_responder_recipe_id, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.delete_target_responder_recipe(
        target_id=target_id,
        target_responder_recipe_id=target_responder_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_group.command(name=cli_util.override('cloud_guard.execute_responder_execution.command_name', 'execute'), help=u"""Executes the responder execution. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](executeResponderExecution)""")
@cli_util.option('--responder-execution-id', required=True, help=u"""The identifier of the responder execution.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--configurations', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ResponderRule configurations

This option is a JSON list with items of type ResponderConfiguration.  For documentation on ResponderConfiguration please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/ResponderConfiguration.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'configurations': {'module': 'cloud_guard', 'class': 'list[ResponderConfiguration]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configurations': {'module': 'cloud_guard', 'class': 'list[ResponderConfiguration]'}})
@cli_util.wrap_exceptions
def execute_responder_execution(ctx, from_json, responder_execution_id, compartment_id, if_match, configurations):

    if isinstance(responder_execution_id, six.string_types) and len(responder_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if configurations is not None:
        _details['configurations'] = cli_util.parse_json_parameter("configurations", configurations)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.execute_responder_execution(
        responder_execution_id=responder_execution_id,
        compartment_id=compartment_id,
        execute_responder_execution_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@condition_metadata_type_group.command(name=cli_util.override('cloud_guard.get_condition_metadata_type.command_name', 'get'), help=u"""Returns ConditionType with its details. \n[Command Reference](getConditionMetadataType)""")
@cli_util.option('--condition-metadata-type-id', required=True, type=custom_types.CliCaseInsensitiveChoice(["ActivityCondition", "SecurityCondition", "CloudGuardCondition"]), help=u"""The type of the condition meta data.""")
@cli_util.option('--service-type', help=u"""ServiceType filter for the condition meta data.""")
@cli_util.option('--resource-type', help=u"""Resource filter for the condition meta data.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ConditionMetadataType'})
@cli_util.wrap_exceptions
def get_condition_metadata_type(ctx, from_json, condition_metadata_type_id, service_type, resource_type):

    if isinstance(condition_metadata_type_id, six.string_types) and len(condition_metadata_type_id.strip()) == 0:
        raise click.UsageError('Parameter --condition-metadata-type-id cannot be whitespace or empty string')

    kwargs = {}
    if service_type is not None:
        kwargs['service_type'] = service_type
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_condition_metadata_type(
        condition_metadata_type_id=condition_metadata_type_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('cloud_guard.get_configuration.command_name', 'get'), help=u"""GET Cloud Guard Configuration Details for a Tenancy. \n[Command Reference](getConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def get_configuration(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_configuration(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_group.command(name=cli_util.override('cloud_guard.get_detector.command_name', 'get'), help=u"""Returns a Detector identified by detectorId. \n[Command Reference](getDetector)""")
@cli_util.option('--detector-id', required=True, help=u"""The Name of Detector.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Detector'})
@cli_util.wrap_exceptions
def get_detector(ctx, from_json, detector_id):

    if isinstance(detector_id, six.string_types) and len(detector_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_detector(
        detector_id=detector_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.get_detector_recipe.command_name', 'get'), help=u"""Returns a DetectorRecipe identified by detectorRecipeId \n[Command Reference](getDetectorRecipe)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipe'})
@cli_util.wrap_exceptions
def get_detector_recipe(ctx, from_json, detector_recipe_id):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_detector_recipe(
        detector_recipe_id=detector_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.get_detector_recipe_detector_rule.command_name', 'get'), help=u"""Get DetectorRule by identifier \n[Command Reference](getDetectorRecipeDetectorRule)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--detector-rule-id', required=True, help=u"""The key of Detector Rule.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipeDetectorRule'})
@cli_util.wrap_exceptions
def get_detector_recipe_detector_rule(ctx, from_json, detector_recipe_id, detector_rule_id):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    if isinstance(detector_rule_id, six.string_types) and len(detector_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_detector_recipe_detector_rule(
        detector_recipe_id=detector_recipe_id,
        detector_rule_id=detector_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_rule_group.command(name=cli_util.override('cloud_guard.get_detector_rule.command_name', 'get'), help=u"""Returns a Detector Rule identified by detectorRuleId \n[Command Reference](getDetectorRule)""")
@cli_util.option('--detector-id', required=True, help=u"""The Name of Detector.""")
@cli_util.option('--detector-rule-id', required=True, help=u"""The key of Detector Rule.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRule'})
@cli_util.wrap_exceptions
def get_detector_rule(ctx, from_json, detector_id, detector_rule_id):

    if isinstance(detector_id, six.string_types) and len(detector_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-id cannot be whitespace or empty string')

    if isinstance(detector_rule_id, six.string_types) and len(detector_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_detector_rule(
        detector_id=detector_id,
        detector_rule_id=detector_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_list_group.command(name=cli_util.override('cloud_guard.get_managed_list.command_name', 'get'), help=u"""Returns a managed list identified by managedListId \n[Command Reference](getManagedList)""")
@cli_util.option('--managed-list-id', required=True, help=u"""The cloudguard list OCID to be passed in the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ManagedList'})
@cli_util.wrap_exceptions
def get_managed_list(ctx, from_json, managed_list_id):

    if isinstance(managed_list_id, six.string_types) and len(managed_list_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-list-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_managed_list(
        managed_list_id=managed_list_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@problem_group.command(name=cli_util.override('cloud_guard.get_problem.command_name', 'get'), help=u"""Returns a Problems response \n[Command Reference](getProblem)""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Problem'})
@cli_util.wrap_exceptions
def get_problem(ctx, from_json, problem_id):

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_problem(
        problem_id=problem_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_group.command(name=cli_util.override('cloud_guard.get_responder_execution.command_name', 'get'), help=u"""Returns a Responder Execution identified by responderExecutionId \n[Command Reference](getResponderExecution)""")
@cli_util.option('--responder-execution-id', required=True, help=u"""The identifier of the responder execution.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderExecution'})
@cli_util.wrap_exceptions
def get_responder_execution(ctx, from_json, responder_execution_id):

    if isinstance(responder_execution_id, six.string_types) and len(responder_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-execution-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_responder_execution(
        responder_execution_id=responder_execution_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_recipe_group.command(name=cli_util.override('cloud_guard.get_responder_recipe.command_name', 'get'), help=u"""Get a ResponderRecipe by identifier \n[Command Reference](getResponderRecipe)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipe'})
@cli_util.wrap_exceptions
def get_responder_recipe(ctx, from_json, responder_recipe_id):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_responder_recipe(
        responder_recipe_id=responder_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.get_responder_recipe_responder_rule.command_name', 'get'), help=u"""Get ResponderRule by identifier \n[Command Reference](getResponderRecipeResponderRule)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--responder-rule-id', required=True, help=u"""The id of ResponderRule""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipeResponderRule'})
@cli_util.wrap_exceptions
def get_responder_recipe_responder_rule(ctx, from_json, responder_recipe_id, responder_rule_id):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    if isinstance(responder_rule_id, six.string_types) and len(responder_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_responder_recipe_responder_rule(
        responder_recipe_id=responder_recipe_id,
        responder_rule_id=responder_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_rule_group.command(name=cli_util.override('cloud_guard.get_responder_rule.command_name', 'get'), help=u"""Get a ResponderRule by identifier \n[Command Reference](getResponderRule)""")
@cli_util.option('--responder-rule-id', required=True, help=u"""The id of ResponderRule""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRule'})
@cli_util.wrap_exceptions
def get_responder_rule(ctx, from_json, responder_rule_id):

    if isinstance(responder_rule_id, six.string_types) and len(responder_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_responder_rule(
        responder_rule_id=responder_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_group.command(name=cli_util.override('cloud_guard.get_target.command_name', 'get'), help=u"""Returns a Target identified by targetId \n[Command Reference](getTarget)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Target'})
@cli_util.wrap_exceptions
def get_target(ctx, from_json, target_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_target(
        target_id=target_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_detector_recipe_group.command(name=cli_util.override('cloud_guard.get_target_detector_recipe.command_name', 'get'), help=u"""Get a TargetDetectorRecipe by identifier \n[Command Reference](getTargetDetectorRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipe'})
@cli_util.wrap_exceptions
def get_target_detector_recipe(ctx, from_json, target_id, target_detector_recipe_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_target_detector_recipe(
        target_id=target_id,
        target_detector_recipe_id=target_detector_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.get_target_detector_recipe_detector_rule.command_name', 'get'), help=u"""Get DetectorRule by identifier \n[Command Reference](getTargetDetectorRecipeDetectorRule)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@cli_util.option('--detector-rule-id', required=True, help=u"""The id of DetectorRule""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipeDetectorRule'})
@cli_util.wrap_exceptions
def get_target_detector_recipe_detector_rule(ctx, from_json, target_id, target_detector_recipe_id, detector_rule_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')

    if isinstance(detector_rule_id, six.string_types) and len(detector_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_target_detector_recipe_detector_rule(
        target_id=target_id,
        target_detector_recipe_id=target_detector_recipe_id,
        detector_rule_id=detector_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_responder_recipe_group.command(name=cli_util.override('cloud_guard.get_target_responder_recipe.command_name', 'get'), help=u"""Get a TargetResponderRecipe by identifier \n[Command Reference](getTargetResponderRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipe'})
@cli_util.wrap_exceptions
def get_target_responder_recipe(ctx, from_json, target_id, target_responder_recipe_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_target_responder_recipe(
        target_id=target_id,
        target_responder_recipe_id=target_responder_recipe_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.get_target_responder_recipe_responder_rule.command_name', 'get'), help=u"""Get ResponderRule by identifier \n[Command Reference](getTargetResponderRecipeResponderRule)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@cli_util.option('--responder-rule-id', required=True, help=u"""The id of ResponderRule""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipeResponderRule'})
@cli_util.wrap_exceptions
def get_target_responder_recipe_responder_rule(ctx, from_json, target_id, target_responder_recipe_id, responder_rule_id):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')

    if isinstance(responder_rule_id, six.string_types) and len(responder_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.get_target_responder_recipe_responder_rule(
        target_id=target_id,
        target_responder_recipe_id=target_responder_recipe_id,
        responder_rule_id=responder_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@condition_metadata_type_group.command(name=cli_util.override('cloud_guard.list_condition_metadata_types.command_name', 'list'), help=u"""Returns a list of condition types. \n[Command Reference](listConditionMetadataTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ConditionMetadataTypeCollection'})
@cli_util.wrap_exceptions
def list_condition_metadata_types(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_condition_metadata_types,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_condition_metadata_types,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_condition_metadata_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.list_detector_recipe_detector_rules.command_name', 'list'), help=u"""Returns a list of DetectorRule associated with DetectorRecipe. \n[Command Reference](listDetectorRecipeDetectorRules)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipeDetectorRuleCollection'})
@cli_util.wrap_exceptions
def list_detector_recipe_detector_rules(ctx, from_json, all_pages, page_size, detector_recipe_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_detector_recipe_detector_rules,
            detector_recipe_id=detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_detector_recipe_detector_rules,
            limit,
            page_size,
            detector_recipe_id=detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_detector_recipe_detector_rules(
            detector_recipe_id=detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.list_detector_recipes.command_name', 'list'), help=u"""Returns a list of all Detector Recipes in a compartment

The ListDetectorRecipes operation returns only the detector recipes in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform ListDetectorRecipes on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](listDetectorRecipes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--resource-metadata-only', type=click.BOOL, help=u"""Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard is returned.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipeCollection'})
@cli_util.wrap_exceptions
def list_detector_recipes(ctx, from_json, all_pages, page_size, compartment_id, display_name, resource_metadata_only, lifecycle_state, limit, page, compartment_id_in_subtree, access_level, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if resource_metadata_only is not None:
        kwargs['resource_metadata_only'] = resource_metadata_only
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_detector_recipes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_detector_recipes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_detector_recipes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@detector_rule_group.command(name=cli_util.override('cloud_guard.list_detector_rules.command_name', 'list'), help=u"""Returns a list of detector rules for the detectorId passed. \n[Command Reference](listDetectorRules)""")
@cli_util.option('--detector-id', required=True, help=u"""The Name of Detector.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorRuleCollection'})
@cli_util.wrap_exceptions
def list_detector_rules(ctx, from_json, all_pages, page_size, detector_id, compartment_id, display_name, limit, lifecycle_state, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(detector_id, six.string_types) and len(detector_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_detector_rules,
            detector_id=detector_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_detector_rules,
            limit,
            page_size,
            detector_id=detector_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_detector_rules(
            detector_id=detector_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@detector_group.command(name=cli_util.override('cloud_guard.list_detectors.command_name', 'list'), help=u"""Returns detector catalog - list of detectors supported by Cloud Guard \n[Command Reference](listDetectors)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'DetectorCollection'})
@cli_util.wrap_exceptions
def list_detectors(ctx, from_json, all_pages, page_size, compartment_id, limit, lifecycle_state, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_detectors,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_detectors,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_detectors(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@impacted_resource_summary_group.command(name=cli_util.override('cloud_guard.list_impacted_resources.command_name', 'list-impacted-resources'), help=u"""Returns a list of Impacted Resources for a CloudGuard Problem \n[Command Reference](listImpactedResources)""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ImpactedResourceCollection'})
@cli_util.wrap_exceptions
def list_impacted_resources(ctx, from_json, all_pages, page_size, problem_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_impacted_resources,
            problem_id=problem_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_impacted_resources,
            limit,
            page_size,
            problem_id=problem_id,
            **kwargs
        )
    else:
        result = client.list_impacted_resources(
            problem_id=problem_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_list_type_summary_group.command(name=cli_util.override('cloud_guard.list_managed_list_types.command_name', 'list-managed-list-types'), help=u"""Returns all ManagedList types supported by Cloud Guard \n[Command Reference](listManagedListTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ManagedListTypeCollection'})
@cli_util.wrap_exceptions
def list_managed_list_types(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_list_types,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_list_types,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_list_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_list_group.command(name=cli_util.override('cloud_guard.list_managed_lists.command_name', 'list'), help=u"""Returns a list of ListManagedLists. The ListManagedLists operation returns only the managed lists in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed.

The parameter `accessLevel` specifies whether to return ManagedLists in only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform ListManagedLists on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](listManagedLists)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--resource-metadata-only', type=click.BOOL, help=u"""Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard is returned.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--list-type', type=custom_types.CliCaseInsensitiveChoice(["CIDR_BLOCK", "USERS", "GROUPS", "IPV4ADDRESS", "IPV6ADDRESS", "RESOURCE_OCID", "REGION", "COUNTRY", "STATE", "CITY", "TAGS"]), help=u"""The type of the ManagedList.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ManagedListCollection'})
@cli_util.wrap_exceptions
def list_managed_lists(ctx, from_json, all_pages, page_size, compartment_id, display_name, resource_metadata_only, lifecycle_state, list_type, limit, page, compartment_id_in_subtree, access_level, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if resource_metadata_only is not None:
        kwargs['resource_metadata_only'] = resource_metadata_only
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if list_type is not None:
        kwargs['list_type'] = list_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_lists,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_lists,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_lists(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@problem_group.command(name=cli_util.override('cloud_guard.list_problem_histories.command_name', 'list-problem-histories'), help=u"""Returns a list of Actions done on CloudGuard Problem \n[Command Reference](listProblemHistories)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ProblemHistoryCollection'})
@cli_util.wrap_exceptions
def list_problem_histories(ctx, from_json, all_pages, page_size, compartment_id, problem_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_problem_histories,
            compartment_id=compartment_id,
            problem_id=problem_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_problem_histories,
            limit,
            page_size,
            compartment_id=compartment_id,
            problem_id=problem_id,
            **kwargs
        )
    else:
        result = client.list_problem_histories(
            compartment_id=compartment_id,
            problem_id=problem_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@problem_group.command(name=cli_util.override('cloud_guard.list_problems.command_name', 'list'), help=u"""Returns a list of all Problems identified by the Cloud Guard

The ListProblems operation returns only the problems in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform ListProblems on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](listProblems)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-last-detected-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-last-detected-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""End time for a filter. If end time is not specified, end time will be set to today's current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-first-detected-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-first-detected-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""End time for a filter. If end time is not specified, end time will be set to today's current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-detail', type=custom_types.CliCaseInsensitiveChoice(["OPEN", "RESOLVED", "DISMISSED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--region-parameterconflict', help=u"""OCI Monitoring region.""")
@cli_util.option('--risk-level', help=u"""Risk level of the Problem.""")
@cli_util.option('--resource-type', help=u"""Resource Type associated with the resource.""")
@cli_util.option('--city', help=u"""City of the problem.""")
@cli_util.option('--state', help=u"""State of the problem.""")
@cli_util.option('--country', help=u"""Country of the problem.""")
@cli_util.option('--label', help=u"""Label associated with the Problem.""")
@cli_util.option('--detector-rule-id-list', multiple=True, help=u"""Comma seperated list of detector rule ids to be passed in to match against Problems.""")
@cli_util.option('--detector-type', type=custom_types.CliCaseInsensitiveChoice(["IAAS_ACTIVITY_DETECTOR", "IAAS_CONFIGURATION_DETECTOR"]), help=u"""The field to list the Problems by Detector Type. Valid values are IAAS_ACTIVITY_DETECTOR and IAAS_CONFIGURATION_DETECTOR""")
@cli_util.option('--target-id', help=u"""The ID of the target in which to list resources.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource associated with the problem.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["riskLevel", "timeLastDetected", "resourceName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for riskLevel, timeLastDetected and resourceName is descending. Default order for riskLevel and resourceName is ascending. If no value is specified timeLastDetected is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'detector-rule-id-list': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rule-id-list': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'ProblemCollection'})
@cli_util.wrap_exceptions
def list_problems(ctx, from_json, all_pages, page_size, compartment_id, time_last_detected_greater_than_or_equal_to, time_last_detected_less_than_or_equal_to, time_first_detected_greater_than_or_equal_to, time_first_detected_less_than_or_equal_to, lifecycle_detail, lifecycle_state, region_parameterconflict, risk_level, resource_type, city, state, country, label, detector_rule_id_list, detector_type, target_id, compartment_id_in_subtree, access_level, resource_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if time_last_detected_greater_than_or_equal_to is not None:
        kwargs['time_last_detected_greater_than_or_equal_to'] = time_last_detected_greater_than_or_equal_to
    if time_last_detected_less_than_or_equal_to is not None:
        kwargs['time_last_detected_less_than_or_equal_to'] = time_last_detected_less_than_or_equal_to
    if time_first_detected_greater_than_or_equal_to is not None:
        kwargs['time_first_detected_greater_than_or_equal_to'] = time_first_detected_greater_than_or_equal_to
    if time_first_detected_less_than_or_equal_to is not None:
        kwargs['time_first_detected_less_than_or_equal_to'] = time_first_detected_less_than_or_equal_to
    if lifecycle_detail is not None:
        kwargs['lifecycle_detail'] = lifecycle_detail
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if region_parameterconflict is not None:
        kwargs['region'] = region_parameterconflict
    if risk_level is not None:
        kwargs['risk_level'] = risk_level
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if city is not None:
        kwargs['city'] = city
    if state is not None:
        kwargs['state'] = state
    if country is not None:
        kwargs['country'] = country
    if label is not None:
        kwargs['label'] = label
    if detector_rule_id_list is not None and len(detector_rule_id_list) > 0:
        kwargs['detector_rule_id_list'] = detector_rule_id_list
    if detector_type is not None:
        kwargs['detector_type'] = detector_type
    if target_id is not None:
        kwargs['target_id'] = target_id
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_problems,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_problems,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_problems(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recommendation_summary_group.command(name=cli_util.override('cloud_guard.list_recommendations.command_name', 'list-recommendations'), help=u"""Returns a list of all Recommendations. \n[Command Reference](listRecommendations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["riskLevel", "timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for riskLevel and timeCreated is descending. If no value is specified riskLevel is default.""")
@cli_util.option('--target-id', help=u"""The ID of the target in which to list resources.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--lifecycle-detail', type=custom_types.CliCaseInsensitiveChoice(["OPEN", "RESOLVED", "DISMISSED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'RecommendationSummaryCollection'})
@cli_util.wrap_exceptions
def list_recommendations(ctx, from_json, all_pages, page_size, compartment_id, sort_order, sort_by, target_id, compartment_id_in_subtree, access_level, lifecycle_state, lifecycle_detail, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if target_id is not None:
        kwargs['target_id'] = target_id
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lifecycle_detail is not None:
        kwargs['lifecycle_detail'] = lifecycle_detail
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_recommendations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_recommendations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_recommendations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resource_type_summary_group.command(name=cli_util.override('cloud_guard.list_resource_types.command_name', 'list-resource-types'), help=u"""Returns a list of resource types. \n[Command Reference](listResourceTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResourceTypeCollection'})
@cli_util.wrap_exceptions
def list_resource_types(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resource_types,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resource_types,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_resource_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@responder_activity_summary_group.command(name=cli_util.override('cloud_guard.list_responder_activities.command_name', 'list-responder-activities'), help=u"""Returns a list of Responder activities done on CloudGuard Problem \n[Command Reference](listResponderActivities)""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "responderRuleName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for responderRuleName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderActivityCollection'})
@cli_util.wrap_exceptions
def list_responder_activities(ctx, from_json, all_pages, page_size, problem_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_responder_activities,
            problem_id=problem_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_responder_activities,
            limit,
            page_size,
            problem_id=problem_id,
            **kwargs
        )
    else:
        result = client.list_responder_activities(
            problem_id=problem_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@responder_execution_summary_group.command(name=cli_util.override('cloud_guard.list_responder_executions.command_name', 'list-responder-executions'), help=u"""Returns a list of Responder Executions. A Responder Execution is an entity that tracks the collective execution of multiple Responder Rule Executions for a given Problem. \n[Command Reference](listResponderExecutions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--responder-rule-ids', multiple=True, help=u"""Responder Rule Ids filter for the Responder Executions.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Creation Start time for filtering""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Creation End time for filtering""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-completed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Completion End Time""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-completed-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Completion Start Time""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--target-id', help=u"""The ID of the target in which to list resources.""")
@cli_util.option('--resource-type', help=u"""Resource Type associated with the resource.""")
@cli_util.option('--responder-type', type=custom_types.CliCaseInsensitiveChoice(["REMEDIATION", "NOTIFICATION"]), help=u"""The field to list the Responder Executions by Responder Type. Valid values are REMEDIATION and NOTIFICATION""")
@cli_util.option('--responder-execution-status', type=custom_types.CliCaseInsensitiveChoice(["STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL"]), help=u"""The status of the responder execution in which to list responders.""")
@cli_util.option('--responder-execution-mode', type=custom_types.CliCaseInsensitiveChoice(["MANUAL", "AUTOMATED", "ALL"]), help=u"""The mode of the responder execution in which to list responders.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "responderRuleName", "resourceName", "timeCompleted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for responderRuleName and resourceName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'responder-rule-ids': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'responder-rule-ids': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'ResponderExecutionCollection'})
@cli_util.wrap_exceptions
def list_responder_executions(ctx, from_json, all_pages, page_size, compartment_id, compartment_id_in_subtree, access_level, responder_rule_ids, time_created_greater_than_or_equal_to, time_created_less_than_or_equal_to, time_completed_greater_than_or_equal_to, time_completed_less_than_or_equal_to, target_id, resource_type, responder_type, responder_execution_status, responder_execution_mode, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if responder_rule_ids is not None and len(responder_rule_ids) > 0:
        kwargs['responder_rule_ids'] = responder_rule_ids
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than_or_equal_to is not None:
        kwargs['time_created_less_than_or_equal_to'] = time_created_less_than_or_equal_to
    if time_completed_greater_than_or_equal_to is not None:
        kwargs['time_completed_greater_than_or_equal_to'] = time_completed_greater_than_or_equal_to
    if time_completed_less_than_or_equal_to is not None:
        kwargs['time_completed_less_than_or_equal_to'] = time_completed_less_than_or_equal_to
    if target_id is not None:
        kwargs['target_id'] = target_id
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if responder_type is not None:
        kwargs['responder_type'] = responder_type
    if responder_execution_status is not None:
        kwargs['responder_execution_status'] = responder_execution_status
    if responder_execution_mode is not None:
        kwargs['responder_execution_mode'] = responder_execution_mode
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_responder_executions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_responder_executions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_responder_executions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.list_responder_recipe_responder_rules.command_name', 'list'), help=u"""Returns a list of ResponderRule associated with ResponderRecipe. \n[Command Reference](listResponderRecipeResponderRules)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipeResponderRuleCollection'})
@cli_util.wrap_exceptions
def list_responder_recipe_responder_rules(ctx, from_json, all_pages, page_size, responder_recipe_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_responder_recipe_responder_rules,
            responder_recipe_id=responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_responder_recipe_responder_rules,
            limit,
            page_size,
            responder_recipe_id=responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_responder_recipe_responder_rules(
            responder_recipe_id=responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@responder_recipe_group.command(name=cli_util.override('cloud_guard.list_responder_recipes.command_name', 'list'), help=u"""Returns a list of all ResponderRecipes in a compartment The ListResponderRecipe operation returns only the targets in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform ListResponderRecipe on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](listResponderRecipes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--resource-metadata-only', type=click.BOOL, help=u"""Default is false. When set to true, the list of all Oracle Managed Resources Metadata supported by Cloud Guard is returned.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipeCollection'})
@cli_util.wrap_exceptions
def list_responder_recipes(ctx, from_json, all_pages, page_size, compartment_id, resource_metadata_only, display_name, lifecycle_state, limit, page, compartment_id_in_subtree, access_level, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_metadata_only is not None:
        kwargs['resource_metadata_only'] = resource_metadata_only
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_responder_recipes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_responder_recipes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_responder_recipes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@responder_rule_group.command(name=cli_util.override('cloud_guard.list_responder_rules.command_name', 'list'), help=u"""Returns a list of ResponderRule. \n[Command Reference](listResponderRules)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderRuleCollection'})
@cli_util.wrap_exceptions
def list_responder_rules(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_responder_rules,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_responder_rules,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_responder_rules(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.list_target_detector_recipe_detector_rules.command_name', 'list'), help=u"""Returns a list of DetectorRule associated with DetectorRecipe within a Target. \n[Command Reference](listTargetDetectorRecipeDetectorRules)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipeDetectorRuleCollection'})
@cli_util.wrap_exceptions
def list_target_detector_recipe_detector_rules(ctx, from_json, all_pages, page_size, target_id, target_detector_recipe_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_target_detector_recipe_detector_rules,
            target_id=target_id,
            target_detector_recipe_id=target_detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_target_detector_recipe_detector_rules,
            limit,
            page_size,
            target_id=target_id,
            target_detector_recipe_id=target_detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_target_detector_recipe_detector_rules(
            target_id=target_id,
            target_detector_recipe_id=target_detector_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_detector_recipe_group.command(name=cli_util.override('cloud_guard.list_target_detector_recipes.command_name', 'list'), help=u"""Returns a list of all detector recipes associated with the target identified by targetId \n[Command Reference](listTargetDetectorRecipes)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipeCollection'})
@cli_util.wrap_exceptions
def list_target_detector_recipes(ctx, from_json, all_pages, page_size, target_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_target_detector_recipes,
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_target_detector_recipes,
            limit,
            page_size,
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_target_detector_recipes(
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.list_target_responder_recipe_responder_rules.command_name', 'list'), help=u"""Returns a list of ResponderRule associated with ResponderRecipe within a Target. \n[Command Reference](listTargetResponderRecipeResponderRules)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "riskLevel"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for displayName is ascending. If no value is specified displayName is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipeResponderRuleCollection'})
@cli_util.wrap_exceptions
def list_target_responder_recipe_responder_rules(ctx, from_json, all_pages, page_size, target_id, target_responder_recipe_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_target_responder_recipe_responder_rules,
            target_id=target_id,
            target_responder_recipe_id=target_responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_target_responder_recipe_responder_rules,
            limit,
            page_size,
            target_id=target_id,
            target_responder_recipe_id=target_responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_target_responder_recipe_responder_rules(
            target_id=target_id,
            target_responder_recipe_id=target_responder_recipe_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_responder_recipe_group.command(name=cli_util.override('cloud_guard.list_target_responder_recipes.command_name', 'list'), help=u"""Returns a list of all responder recipes associated with the target identified by targetId \n[Command Reference](listTargetResponderRecipes)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipeCollection'})
@cli_util.wrap_exceptions
def list_target_responder_recipes(ctx, from_json, all_pages, page_size, target_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_target_responder_recipes,
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_target_responder_recipes,
            limit,
            page_size,
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_target_responder_recipes(
            target_id=target_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@target_group.command(name=cli_util.override('cloud_guard.list_targets.command_name', 'list'), help=u"""Returns a list of all Targets in a compartment The ListTargets operation returns only the targets in `compartmentId` passed. The list does not include any subcompartments of the compartmentId passed.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform ListTargets on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](listTargets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'TargetCollection'})
@cli_util.wrap_exceptions
def list_targets(ctx, from_json, all_pages, page_size, compartment_id, display_name, lifecycle_state, compartment_id_in_subtree, access_level, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_targets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_targets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_targets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@risk_score_aggregation_group.command(name=cli_util.override('cloud_guard.request_risk_scores.command_name', 'request-risk-scores'), help=u"""Examines the number of problems related to the resource and the relative severity of those problems. \n[Command Reference](requestRiskScores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'RiskScoreAggregationCollection'})
@cli_util.wrap_exceptions
def request_risk_scores(ctx, from_json, compartment_id, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_risk_scores(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_score_trend_aggregation_group.command(name=cli_util.override('cloud_guard.request_security_score_summarized_trend.command_name', 'request-security-score-summarized-trend'), help=u"""Measures the number of resources examined across all regions and compares it with the number of problems detected, for a given time period. \n[Command Reference](requestSecurityScoreSummarizedTrend)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-score-computed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-score-computed-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""End time for a filter. If end time is not specified, end time will be set to today's current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'SecurityScoreTrendAggregationCollection'})
@cli_util.wrap_exceptions
def request_security_score_summarized_trend(ctx, from_json, compartment_id, time_score_computed_greater_than_or_equal_to, time_score_computed_less_than_or_equal_to, limit, page):

    kwargs = {}
    if time_score_computed_greater_than_or_equal_to is not None:
        kwargs['time_score_computed_greater_than_or_equal_to'] = time_score_computed_greater_than_or_equal_to
    if time_score_computed_less_than_or_equal_to is not None:
        kwargs['time_score_computed_less_than_or_equal_to'] = time_score_computed_less_than_or_equal_to
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_security_score_summarized_trend(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_score_aggregation_group.command(name=cli_util.override('cloud_guard.request_security_scores.command_name', 'request-security-scores'), help=u"""Measures the number of resources examined across all regions and compares it with the number of problems detected. \n[Command Reference](requestSecurityScores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'SecurityScoreAggregationCollection'})
@cli_util.wrap_exceptions
def request_security_scores(ctx, from_json, compartment_id, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_security_scores(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@activity_problem_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_activity_problems.command_name', 'request-summarized-activity-problems'), help=u"""Returns the summary of Activity type problems identified by cloud guard, for a given set of dimensions.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.

The compartmentId to be passed with `accessLevel` and `compartmentIdInSubtree` params has to be the root compartment id (tenant-id) only. \n[Command Reference](requestSummarizedActivityProblems)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--include-unknown-locations', type=click.BOOL, help=u"""Default is false. When set to true, the summary of activity problems that has unknown values for city, state or country will be included.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ActivityProblemAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_activity_problems(ctx, from_json, compartment_id, compartment_id_in_subtree, access_level, limit, include_unknown_locations, page):

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if include_unknown_locations is not None:
        kwargs['include_unknown_locations'] = include_unknown_locations
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_activity_problems(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@problem_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_problems.command_name', 'request-summarized-problems'), help=u"""Returns the number of problems identified by cloud guard, for a given set of dimensions.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](requestSummarizedProblems)""")
@cli_util.option('--list-dimensions', required=True, type=custom_types.CliCaseInsensitiveChoice(["RESOURCE_TYPE", "REGION", "COMPARTMENT_ID", "RISK_LEVEL"]), multiple=True, help=u"""The possible attributes based on which the problems can be distinguished.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ProblemAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_problems(ctx, from_json, list_dimensions, compartment_id, compartment_id_in_subtree, access_level, limit, page):

    kwargs = {}
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_problems(
        list_dimensions=list_dimensions,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_responder_executions.command_name', 'request-summarized-responder-executions'), help=u"""Returns the number of Responder Executions, for a given set of dimensions.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](requestSummarizedResponderExecutions)""")
@cli_util.option('--responder-executions-dimensions', required=True, type=custom_types.CliCaseInsensitiveChoice(["RESPONDER_RULE_TYPE", "RESPONDER_EXECUTION_STATUS"]), multiple=True, help=u"""The possible attributes based on which the responder executions can be distinguished""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--responder-type-filter', type=custom_types.CliCaseInsensitiveChoice(["REMEDIATION", "NOTIFICATION"]), multiple=True, help=u"""The possible filters for Responder Type Dimension to distinguish Responder Executions. If no values are passed, the metric for responder executions of all reponder types are returned""")
@cli_util.option('--responder-execution-status-filter', type=custom_types.CliCaseInsensitiveChoice(["STARTED", "AWAITING_CONFIRMATION", "SUCCEEDED", "FAILED", "SKIPPED"]), multiple=True, help=u"""The possible filters for Responder Type Dimension to distinguish Responder Executions. If no values are passed, the metric for responder executions of all status are returned""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderExecutionAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_responder_executions(ctx, from_json, responder_executions_dimensions, compartment_id, responder_type_filter, responder_execution_status_filter, compartment_id_in_subtree, access_level, limit, page):

    kwargs = {}
    if responder_type_filter is not None and len(responder_type_filter) > 0:
        kwargs['responder_type_filter'] = responder_type_filter
    if responder_execution_status_filter is not None and len(responder_execution_status_filter) > 0:
        kwargs['responder_execution_status_filter'] = responder_execution_status_filter
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_responder_executions(
        responder_executions_dimensions=responder_executions_dimensions,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@risk_score_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_risk_scores.command_name', 'request-summarized-risk-scores'), help=u"""DEPRECATED \n[Command Reference](requestSummarizedRiskScores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'RiskScoreAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_risk_scores(ctx, from_json, compartment_id, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_risk_scores(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_score_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_security_scores.command_name', 'request-summarized-security-scores'), help=u"""DEPRECATED \n[Command Reference](requestSummarizedSecurityScores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'SecurityScoreAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_security_scores(ctx, from_json, compartment_id, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_security_scores(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@problem_trend_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_trend_problems.command_name', 'request-summarized-trend-problems'), help=u"""Returns the number of problems identified by cloud guard, for a given time period.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](requestSummarizedTrendProblems)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-first-detected-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-first-detected-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""End time for a filter. If end time is not specified, end time will be set to today's current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ProblemTrendAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_trend_problems(ctx, from_json, compartment_id, time_first_detected_greater_than_or_equal_to, time_first_detected_less_than_or_equal_to, compartment_id_in_subtree, access_level, limit, page):

    kwargs = {}
    if time_first_detected_greater_than_or_equal_to is not None:
        kwargs['time_first_detected_greater_than_or_equal_to'] = time_first_detected_greater_than_or_equal_to
    if time_first_detected_less_than_or_equal_to is not None:
        kwargs['time_first_detected_less_than_or_equal_to'] = time_first_detected_less_than_or_equal_to
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_trend_problems(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_trend_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_trend_responder_executions.command_name', 'request-summarized-trend-responder-executions'), help=u"""Returns the number of remediations performed by Responders, for a given time period.

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if Principal doesn't have access to even one of the child compartments. This is valid only when `compartmentIdInSubtree` is set to `true`.

The parameter `compartmentIdInSubtree` applies when you perform summarize API on the `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE. \n[Command Reference](requestSummarizedTrendResponderExecutions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-completed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Completion End Time""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-completed-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Completion Start Time""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["RESTRICTED", "ACCESSIBLE"]), help=u"""Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). When set to `RESTRICTED` permissions are checked and no partial results are displayed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'ResponderExecutionTrendAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_trend_responder_executions(ctx, from_json, compartment_id, time_completed_greater_than_or_equal_to, time_completed_less_than_or_equal_to, compartment_id_in_subtree, access_level, limit, page):

    kwargs = {}
    if time_completed_greater_than_or_equal_to is not None:
        kwargs['time_completed_greater_than_or_equal_to'] = time_completed_greater_than_or_equal_to
    if time_completed_less_than_or_equal_to is not None:
        kwargs['time_completed_less_than_or_equal_to'] = time_completed_less_than_or_equal_to
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if access_level is not None:
        kwargs['access_level'] = access_level
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_trend_responder_executions(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@security_score_trend_aggregation_group.command(name=cli_util.override('cloud_guard.request_summarized_trend_security_scores.command_name', 'request-summarized-trend-security-scores'), help=u"""DEPRECATED \n[Command Reference](requestSummarizedTrendSecurityScores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-score-computed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Start time for a filter. If start time is not specified, start time will be set to today's current time - 30 days.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-score-computed-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""End time for a filter. If end time is not specified, end time will be set to today's current time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'SecurityScoreTrendAggregationCollection'})
@cli_util.wrap_exceptions
def request_summarized_trend_security_scores(ctx, from_json, compartment_id, time_score_computed_greater_than_or_equal_to, time_score_computed_less_than_or_equal_to, limit, page):

    kwargs = {}
    if time_score_computed_greater_than_or_equal_to is not None:
        kwargs['time_score_computed_greater_than_or_equal_to'] = time_score_computed_greater_than_or_equal_to
    if time_score_computed_less_than_or_equal_to is not None:
        kwargs['time_score_computed_less_than_or_equal_to'] = time_score_computed_less_than_or_equal_to
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.request_summarized_trend_security_scores(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_group.command(name=cli_util.override('cloud_guard.skip_bulk_responder_execution.command_name', 'skip-bulk'), help=u"""Skips the execution for a bulk of responder executions The operation is atomic in nature \n[Command Reference](skipBulkResponderExecution)""")
@cli_util.option('--responder-execution-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of responder execution ids to skip the execution""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'responder-execution-ids': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'responder-execution-ids': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def skip_bulk_responder_execution(ctx, from_json, responder_execution_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['responderExecutionIds'] = cli_util.parse_json_parameter("responder_execution_ids", responder_execution_ids)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.skip_bulk_responder_execution(
        skip_bulk_responder_execution_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@responder_execution_group.command(name=cli_util.override('cloud_guard.skip_responder_execution.command_name', 'skip'), help=u"""Skips the execution of the responder execution. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](skipResponderExecution)""")
@cli_util.option('--responder-execution-id', required=True, help=u"""The identifier of the responder execution.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def skip_responder_execution(ctx, from_json, responder_execution_id, compartment_id, if_match):

    if isinstance(responder_execution_id, six.string_types) and len(responder_execution_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-execution-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.skip_responder_execution(
        responder_execution_id=responder_execution_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@problem_group.command(name=cli_util.override('cloud_guard.trigger_responder.command_name', 'trigger-responder'), help=u"""push the problem to responder \n[Command Reference](triggerResponder)""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@cli_util.option('--responder-rule-id', required=True, help=u"""ResponderRule ID""")
@cli_util.option('--configurations', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ResponderRule configurations

This option is a JSON list with items of type ResponderConfiguration.  For documentation on ResponderConfiguration please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/ResponderConfiguration.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'configurations': {'module': 'cloud_guard', 'class': 'list[ResponderConfiguration]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configurations': {'module': 'cloud_guard', 'class': 'list[ResponderConfiguration]'}})
@cli_util.wrap_exceptions
def trigger_responder(ctx, from_json, problem_id, responder_rule_id, configurations, if_match):

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['responderRuleId'] = responder_rule_id

    if configurations is not None:
        _details['configurations'] = cli_util.parse_json_parameter("configurations", configurations)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.trigger_responder(
        problem_id=problem_id,
        trigger_responder_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@problem_group.command(name=cli_util.override('cloud_guard.update_bulk_problem_status.command_name', 'update-bulk-problem-status'), help=u"""Updates the statuses in bulk for a list of problems The operation is atomic in nature \n[Command Reference](updateBulkProblemStatus)""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["OPEN", "RESOLVED", "DISMISSED"]), help=u"""Action taken by user""")
@cli_util.option('--problem-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of ProblemIds to be passed in to update the Problem status.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'problem-ids': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'problem-ids': {'module': 'cloud_guard', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_bulk_problem_status(ctx, from_json, status, problem_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status
    _details['problemIds'] = cli_util.parse_json_parameter("problem_ids", problem_ids)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_bulk_problem_status(
        update_bulk_problem_status_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('cloud_guard.update_configuration.command_name', 'update'), help=u"""Enable/Disable Cloud Guard. The reporting region cannot be updated once created. \n[Command Reference](updateConfiguration)""")
@cli_util.option('--reporting-region', required=True, help=u"""The reporting region value""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""Status of Cloud Guard Tenant""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--self-manage-resources', type=click.BOOL, help=u"""Identifies if Oracle managed resources will be created by customers. If no value is specified false is the default.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def update_configuration(ctx, from_json, reporting_region, status, compartment_id, self_manage_resources, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['reportingRegion'] = reporting_region
    _details['status'] = status

    if self_manage_resources is not None:
        _details['selfManageResources'] = self_manage_resources

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_configuration(
        compartment_id=compartment_id,
        update_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detector_recipe_group.command(name=cli_util.override('cloud_guard.update_detector_recipe.command_name', 'update'), help=u"""Updates a detector recipe identified by detectorRecipeId \n[Command Reference](updateDetectorRecipe)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--display-name', help=u"""DisplayName of detector recipe""")
@cli_util.option('--description', help=u"""Detector recipe description""")
@cli_util.option('--detector-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Detector Rules to update

This option is a JSON list with items of type UpdateDetectorRecipeDetectorRule.  For documentation on UpdateDetectorRecipeDetectorRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateDetectorRecipeDetectorRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateDetectorRecipeDetectorRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateDetectorRecipeDetectorRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipe'})
@cli_util.wrap_exceptions
def update_detector_recipe(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, detector_recipe_id, display_name, description, detector_rules, freeform_tags, defined_tags, if_match):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')
    if not force:
        if detector_rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to detector-rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if detector_rules is not None:
        _details['detectorRules'] = cli_util.parse_json_parameter("detector_rules", detector_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_detector_recipe(
        detector_recipe_id=detector_recipe_id,
        update_detector_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_detector_recipe') and callable(getattr(client, 'get_detector_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_detector_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.update_detector_recipe_detector_rule.command_name', 'update'), help=u"""Update the DetectorRule by identifier \n[Command Reference](updateDetectorRecipeDetectorRule)""")
@cli_util.option('--detector-recipe-id', required=True, help=u"""DetectorRecipe OCID""")
@cli_util.option('--detector-rule-id', required=True, help=u"""The key of Detector Rule.""")
@cli_util.option('--details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'details': {'module': 'cloud_guard', 'class': 'UpdateDetectorRuleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'details': {'module': 'cloud_guard', 'class': 'UpdateDetectorRuleDetails'}}, output_type={'module': 'cloud_guard', 'class': 'DetectorRecipeDetectorRule'})
@cli_util.wrap_exceptions
def update_detector_recipe_detector_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, detector_recipe_id, detector_rule_id, details, if_match):

    if isinstance(detector_recipe_id, six.string_types) and len(detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-recipe-id cannot be whitespace or empty string')

    if isinstance(detector_rule_id, six.string_types) and len(detector_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-rule-id cannot be whitespace or empty string')
    if not force:
        if details:
            if not click.confirm("WARNING: Updates to details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if details is not None:
        _details['details'] = cli_util.parse_json_parameter("details", details)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_detector_recipe_detector_rule(
        detector_recipe_id=detector_recipe_id,
        detector_rule_id=detector_rule_id,
        update_detector_recipe_detector_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_detector_recipe_detector_rule') and callable(getattr(client, 'get_detector_recipe_detector_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_detector_recipe_detector_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@managed_list_group.command(name=cli_util.override('cloud_guard.update_managed_list.command_name', 'update'), help=u"""Updates a managed list identified by managedListId \n[Command Reference](updateManagedList)""")
@cli_util.option('--managed-list-id', required=True, help=u"""The cloudguard list OCID to be passed in the request.""")
@cli_util.option('--display-name', help=u"""ManagedList display name""")
@cli_util.option('--description', help=u"""ManagedList description""")
@cli_util.option('--list-items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of ManagedListItem""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'list-items': {'module': 'cloud_guard', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'list-items': {'module': 'cloud_guard', 'class': 'list[string]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'ManagedList'})
@cli_util.wrap_exceptions
def update_managed_list(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_list_id, display_name, description, list_items, freeform_tags, defined_tags, if_match):

    if isinstance(managed_list_id, six.string_types) and len(managed_list_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-list-id cannot be whitespace or empty string')
    if not force:
        if list_items or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to list-items and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if list_items is not None:
        _details['listItems'] = cli_util.parse_json_parameter("list_items", list_items)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_managed_list(
        managed_list_id=managed_list_id,
        update_managed_list_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_list') and callable(getattr(client, 'get_managed_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@problem_group.command(name=cli_util.override('cloud_guard.update_problem_status.command_name', 'update-problem-status'), help=u"""updates the problem details \n[Command Reference](updateProblemStatus)""")
@cli_util.option('--problem-id', required=True, help=u"""OCId of the problem.""")
@cli_util.option('--status', required=True, type=custom_types.CliCaseInsensitiveChoice(["OPEN", "RESOLVED", "DISMISSED"]), help=u"""Action taken by user""")
@cli_util.option('--comment', help=u"""User Comments""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cloud_guard', 'class': 'Problem'})
@cli_util.wrap_exceptions
def update_problem_status(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, problem_id, status, comment, if_match):

    if isinstance(problem_id, six.string_types) and len(problem_id.strip()) == 0:
        raise click.UsageError('Parameter --problem-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['status'] = status

    if comment is not None:
        _details['comment'] = comment

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_problem_status(
        problem_id=problem_id,
        update_problem_status_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_problem') and callable(getattr(client, 'get_problem')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_problem(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@responder_recipe_group.command(name=cli_util.override('cloud_guard.update_responder_recipe.command_name', 'update'), help=u"""Update the ResponderRecipe resource by identifier \n[Command Reference](updateResponderRecipe)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--display-name', required=True, help=u"""ResponderRecipe Identifier""")
@cli_util.option('--description', help=u"""ResponderRecipe Description""")
@cli_util.option('--responder-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Responder Rules to Update

This option is a JSON list with items of type UpdateResponderRecipeResponderRule.  For documentation on UpdateResponderRecipeResponderRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateResponderRecipeResponderRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateResponderRecipeResponderRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateResponderRecipeResponderRule]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipe'})
@cli_util.wrap_exceptions
def update_responder_recipe(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, responder_recipe_id, display_name, description, responder_rules, freeform_tags, defined_tags, if_match):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')
    if not force:
        if responder_rules or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to responder-rules and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if responder_rules is not None:
        _details['responderRules'] = cli_util.parse_json_parameter("responder_rules", responder_rules)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_responder_recipe(
        responder_recipe_id=responder_recipe_id,
        update_responder_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_responder_recipe') and callable(getattr(client, 'get_responder_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_responder_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.update_responder_recipe_responder_rule.command_name', 'update'), help=u"""Update the ResponderRule by identifier \n[Command Reference](updateResponderRecipeResponderRule)""")
@cli_util.option('--responder-recipe-id', required=True, help=u"""OCID of ResponderRecipe""")
@cli_util.option('--responder-rule-id', required=True, help=u"""The id of ResponderRule""")
@cli_util.option('--details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'details': {'module': 'cloud_guard', 'class': 'UpdateResponderRuleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'details': {'module': 'cloud_guard', 'class': 'UpdateResponderRuleDetails'}}, output_type={'module': 'cloud_guard', 'class': 'ResponderRecipeResponderRule'})
@cli_util.wrap_exceptions
def update_responder_recipe_responder_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, responder_recipe_id, responder_rule_id, details, if_match):

    if isinstance(responder_recipe_id, six.string_types) and len(responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-recipe-id cannot be whitespace or empty string')

    if isinstance(responder_rule_id, six.string_types) and len(responder_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-rule-id cannot be whitespace or empty string')
    if not force:
        if details:
            if not click.confirm("WARNING: Updates to details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['details'] = cli_util.parse_json_parameter("details", details)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_responder_recipe_responder_rule(
        responder_recipe_id=responder_recipe_id,
        responder_rule_id=responder_rule_id,
        update_responder_recipe_responder_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_responder_recipe_responder_rule') and callable(getattr(client, 'get_responder_recipe_responder_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_responder_recipe_responder_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_group.command(name=cli_util.override('cloud_guard.update_target.command_name', 'update'), help=u"""Updates a Target identified by targetId \n[Command Reference](updateTarget)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--display-name', help=u"""DetectorTemplate Identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current state of the Target.""")
@cli_util.option('--target-detector-recipes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The details of target detector recipes to be updated.

This option is a JSON list with items of type UpdateTargetDetectorRecipe.  For documentation on UpdateTargetDetectorRecipe please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateTargetDetectorRecipe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-responder-recipes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The details of target responder recipes to be updated.

This option is a JSON list with items of type UpdateTargetResponderRecipe.  For documentation on UpdateTargetResponderRecipe please see our API reference: https://docs.cloud.oracle.com/api/#/en/cloudguard/20200131/datatypes/UpdateTargetResponderRecipe.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target-detector-recipes': {'module': 'cloud_guard', 'class': 'list[UpdateTargetDetectorRecipe]'}, 'target-responder-recipes': {'module': 'cloud_guard', 'class': 'list[UpdateTargetResponderRecipe]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-detector-recipes': {'module': 'cloud_guard', 'class': 'list[UpdateTargetDetectorRecipe]'}, 'target-responder-recipes': {'module': 'cloud_guard', 'class': 'list[UpdateTargetResponderRecipe]'}, 'freeform-tags': {'module': 'cloud_guard', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'cloud_guard', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'cloud_guard', 'class': 'Target'})
@cli_util.wrap_exceptions
def update_target(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, display_name, lifecycle_state, target_detector_recipes, target_responder_recipes, freeform_tags, defined_tags, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')
    if not force:
        if target_detector_recipes or target_responder_recipes or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to target-detector-recipes and target-responder-recipes and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if target_detector_recipes is not None:
        _details['targetDetectorRecipes'] = cli_util.parse_json_parameter("target_detector_recipes", target_detector_recipes)

    if target_responder_recipes is not None:
        _details['targetResponderRecipes'] = cli_util.parse_json_parameter("target_responder_recipes", target_responder_recipes)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_target(
        target_id=target_id,
        update_target_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target') and callable(getattr(client, 'get_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_detector_recipe_group.command(name=cli_util.override('cloud_guard.update_target_detector_recipe.command_name', 'update'), help=u"""Update the TargetDetectorRecipe resource by identifier \n[Command Reference](updateTargetDetectorRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@cli_util.option('--detector-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Update detector rules associated with detector recipe in a target.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateTargetRecipeDetectorRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rules': {'module': 'cloud_guard', 'class': 'list[UpdateTargetRecipeDetectorRuleDetails]'}}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipe'})
@cli_util.wrap_exceptions
def update_target_detector_recipe(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, target_detector_recipe_id, detector_rules, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')
    if not force:
        if detector_rules:
            if not click.confirm("WARNING: Updates to detector-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['detectorRules'] = cli_util.parse_json_parameter("detector_rules", detector_rules)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_target_detector_recipe(
        target_id=target_id,
        target_detector_recipe_id=target_detector_recipe_id,
        update_target_detector_recipe_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target_detector_recipe') and callable(getattr(client, 'get_target_detector_recipe')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target_detector_recipe(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_detector_recipe_detector_rule_group.command(name=cli_util.override('cloud_guard.update_target_detector_recipe_detector_rule.command_name', 'update'), help=u"""Update the DetectorRule by identifier \n[Command Reference](updateTargetDetectorRecipeDetectorRule)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-detector-recipe-id', required=True, help=u"""OCID of TargetDetectorRecipe""")
@cli_util.option('--detector-rule-id', required=True, help=u"""The id of DetectorRule""")
@cli_util.option('--details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'details': {'module': 'cloud_guard', 'class': 'UpdateTargetDetectorRuleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'details': {'module': 'cloud_guard', 'class': 'UpdateTargetDetectorRuleDetails'}}, output_type={'module': 'cloud_guard', 'class': 'TargetDetectorRecipeDetectorRule'})
@cli_util.wrap_exceptions
def update_target_detector_recipe_detector_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, target_detector_recipe_id, detector_rule_id, details, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_detector_recipe_id, six.string_types) and len(target_detector_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-detector-recipe-id cannot be whitespace or empty string')

    if isinstance(detector_rule_id, six.string_types) and len(detector_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --detector-rule-id cannot be whitespace or empty string')
    if not force:
        if details:
            if not click.confirm("WARNING: Updates to details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['details'] = cli_util.parse_json_parameter("details", details)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_target_detector_recipe_detector_rule(
        target_id=target_id,
        target_detector_recipe_id=target_detector_recipe_id,
        detector_rule_id=detector_rule_id,
        update_target_detector_recipe_detector_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target_detector_recipe_detector_rule') and callable(getattr(client, 'get_target_detector_recipe_detector_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target_detector_recipe_detector_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@target_responder_recipe_group.command(name=cli_util.override('cloud_guard.update_target_responder_recipe.command_name', 'update'), help=u"""Update the TargetResponderRecipe resource by identifier \n[Command Reference](updateTargetResponderRecipe)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@cli_util.option('--responder-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Update responder rules associated with responder recipe in a target.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateTargetRecipeResponderRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'responder-rules': {'module': 'cloud_guard', 'class': 'list[UpdateTargetRecipeResponderRuleDetails]'}}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipe'})
@cli_util.wrap_exceptions
def update_target_responder_recipe(ctx, from_json, force, target_id, target_responder_recipe_id, responder_rules, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')
    if not force:
        if responder_rules:
            if not click.confirm("WARNING: Updates to responder-rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['responderRules'] = cli_util.parse_json_parameter("responder_rules", responder_rules)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_target_responder_recipe(
        target_id=target_id,
        target_responder_recipe_id=target_responder_recipe_id,
        update_target_responder_recipe_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@target_responder_recipe_responder_rule_group.command(name=cli_util.override('cloud_guard.update_target_responder_recipe_responder_rule.command_name', 'update'), help=u"""Update the ResponderRule by identifier \n[Command Reference](updateTargetResponderRecipeResponderRule)""")
@cli_util.option('--target-id', required=True, help=u"""OCID of target""")
@cli_util.option('--target-responder-recipe-id', required=True, help=u"""OCID of TargetResponderRecipe""")
@cli_util.option('--responder-rule-id', required=True, help=u"""The id of ResponderRule""")
@cli_util.option('--details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'details': {'module': 'cloud_guard', 'class': 'UpdateTargetResponderRuleDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'details': {'module': 'cloud_guard', 'class': 'UpdateTargetResponderRuleDetails'}}, output_type={'module': 'cloud_guard', 'class': 'TargetResponderRecipeResponderRule'})
@cli_util.wrap_exceptions
def update_target_responder_recipe_responder_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, target_id, target_responder_recipe_id, responder_rule_id, details, if_match):

    if isinstance(target_id, six.string_types) and len(target_id.strip()) == 0:
        raise click.UsageError('Parameter --target-id cannot be whitespace or empty string')

    if isinstance(target_responder_recipe_id, six.string_types) and len(target_responder_recipe_id.strip()) == 0:
        raise click.UsageError('Parameter --target-responder-recipe-id cannot be whitespace or empty string')

    if isinstance(responder_rule_id, six.string_types) and len(responder_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --responder-rule-id cannot be whitespace or empty string')
    if not force:
        if details:
            if not click.confirm("WARNING: Updates to details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['details'] = cli_util.parse_json_parameter("details", details)

    client = cli_util.build_client('cloud_guard', 'cloud_guard', ctx)
    result = client.update_target_responder_recipe_responder_rule(
        target_id=target_id,
        target_responder_recipe_id=target_responder_recipe_id,
        responder_rule_id=responder_rule_id,
        update_target_responder_recipe_responder_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_target_responder_recipe_responder_rule') and callable(getattr(client, 'get_target_responder_recipe_responder_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_target_responder_recipe_responder_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
