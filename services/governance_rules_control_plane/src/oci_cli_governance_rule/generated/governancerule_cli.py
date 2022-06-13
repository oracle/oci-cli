# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
from services.governance_rules_control_plane.src.oci_cli_governance_rules_control_plane.generated import governance_rules_control_plane_service_cli


@click.command(cli_util.override('governance_rule.governance_rule_root_group.command_name', 'governance-rule'), cls=CommandGroupWithAlias, help=cli_util.override('governance_rule.governance_rule_root_group.help', """A description of the GovernanceRulesControlPlane API"""), short_help=cli_util.override('governance_rule.governance_rule_root_group.short_help', """GovernanceRulesControlPlane API"""))
@cli_util.help_option_group
def governance_rule_root_group():
    pass


@click.command(cli_util.override('governance_rule.enforced_governance_rule_group.command_name', 'enforced-governance-rule'), cls=CommandGroupWithAlias, help="""Represents the governance rule shown to the child which is a subset of governance rule resource in parent tenancy.""")
@cli_util.help_option_group
def enforced_governance_rule_group():
    pass


@click.command(cli_util.override('governance_rule.tenancy_attachment_group.command_name', 'tenancy-attachment'), cls=CommandGroupWithAlias, help="""Tenancy attachment associates a tenancy to a governance rule via an inclusion criterion.""")
@cli_util.help_option_group
def tenancy_attachment_group():
    pass


@click.command(cli_util.override('governance_rule.governance_rule_group.command_name', 'governance-rule'), cls=CommandGroupWithAlias, help="""Represents a rule in parent tenancy which governs resources in child tenancies.""")
@cli_util.help_option_group
def governance_rule_group():
    pass


@click.command(cli_util.override('governance_rule.inclusion_criterion_group.command_name', 'inclusion-criterion'), cls=CommandGroupWithAlias, help="""Represents the criterion for the inclusion of the child tenancies under a governance rule. This can be either TENANCY or TAG.""")
@cli_util.help_option_group
def inclusion_criterion_group():
    pass


governance_rules_control_plane_service_cli.governance_rules_control_plane_service_group.add_command(governance_rule_root_group)
governance_rule_root_group.add_command(enforced_governance_rule_group)
governance_rule_root_group.add_command(tenancy_attachment_group)
governance_rule_root_group.add_command(governance_rule_group)
governance_rule_root_group.add_command(inclusion_criterion_group)


@governance_rule_group.command(name=cli_util.override('governance_rule.create_governance_rule.command_name', 'create'), help=u"""Create governance rule in the root compartment only. Either relatedResourceId or template must be supplied. \n[Command Reference](createGovernanceRule)""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle ID ([OCID]) of the root compartment containing the governance rule.""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the governance rule.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

Example: `QUOTA`""")
@cli_util.option('--creation-option', required=True, type=custom_types.CliCaseInsensitiveChoice(["TEMPLATE", "CLONE"]), help=u"""The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

Example: `TEMPLATE`""")
@cli_util.option('--template', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'template': {'module': 'governance_rules_control_plane', 'class': 'Template'}, 'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'template': {'module': 'governance_rules_control_plane', 'class': 'Template'}, 'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRule'})
@cli_util.wrap_exceptions
def create_governance_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, type, creation_option, template, description, related_resource_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['type'] = type
    _details['creationOption'] = creation_option
    _details['template'] = cli_util.parse_json_parameter("template", template)

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_governance_rule(
        create_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.create_governance_rule_tag_template.command_name', 'create-governance-rule-tag-template'), help=u"""Create governance rule in the root compartment only. Either relatedResourceId or template must be supplied. \n[Command Reference](createGovernanceRule)""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle ID ([OCID]) of the root compartment containing the governance rule.""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the governance rule.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

Example: `QUOTA`""")
@cli_util.option('--creation-option', required=True, type=custom_types.CliCaseInsensitiveChoice(["TEMPLATE", "CLONE"]), help=u"""The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

Example: `TEMPLATE`""")
@cli_util.option('--template-name', required=True, help=u"""The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.""")
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--template-description', help=u"""Description of the tag namespace.""")
@cli_util.option('--template-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Represents an array of tags for tag namespace.

This option is a JSON list with items of type Tag.  For documentation on Tag please see our API reference: https://docs.cloud.oracle.com/api/#/en/governancerule/20220504/datatypes/Tag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--template-tag-defaults', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type TagDefault.  For documentation on TagDefault please see our API reference: https://docs.cloud.oracle.com/api/#/en/governancerule/20220504/datatypes/TagDefault.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-tags': {'module': 'governance_rules_control_plane', 'class': 'list[Tag]'}, 'template-tag-defaults': {'module': 'governance_rules_control_plane', 'class': 'list[TagDefault]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-tags': {'module': 'governance_rules_control_plane', 'class': 'list[Tag]'}, 'template-tag-defaults': {'module': 'governance_rules_control_plane', 'class': 'list[TagDefault]'}}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRule'})
@cli_util.wrap_exceptions
def create_governance_rule_tag_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, type, creation_option, template_name, description, related_resource_id, freeform_tags, defined_tags, template_description, template_tags, template_tag_defaults):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['type'] = type
    _details['creationOption'] = creation_option
    _details['template']['name'] = template_name

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    if template_tags is not None:
        _details['template']['tags'] = cli_util.parse_json_parameter("template_tags", template_tags)

    if template_tag_defaults is not None:
        _details['template']['tagDefaults'] = cli_util.parse_json_parameter("template_tag_defaults", template_tag_defaults)

    _details['template']['type'] = 'TAG'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_governance_rule(
        create_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.create_governance_rule_quota_template.command_name', 'create-governance-rule-quota-template'), help=u"""Create governance rule in the root compartment only. Either relatedResourceId or template must be supplied. \n[Command Reference](createGovernanceRule)""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle ID ([OCID]) of the root compartment containing the governance rule.""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the governance rule.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

Example: `QUOTA`""")
@cli_util.option('--creation-option', required=True, type=custom_types.CliCaseInsensitiveChoice(["TEMPLATE", "CLONE"]), help=u"""The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

Example: `TEMPLATE`""")
@cli_util.option('--template-display-name', required=True, help=u"""Display name of the quota resource.""")
@cli_util.option('--template-statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of quota statements.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--template-description', help=u"""Description of the quota resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-statements': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-statements': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRule'})
@cli_util.wrap_exceptions
def create_governance_rule_quota_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, type, creation_option, template_display_name, template_statements, description, related_resource_id, freeform_tags, defined_tags, template_description):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['type'] = type
    _details['creationOption'] = creation_option
    _details['template']['displayName'] = template_display_name
    _details['template']['statements'] = cli_util.parse_json_parameter("template_statements", template_statements)

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    _details['template']['type'] = 'QUOTA'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_governance_rule(
        create_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.create_governance_rule_allowed_regions_template.command_name', 'create-governance-rule-allowed-regions-template'), help=u"""Create governance rule in the root compartment only. Either relatedResourceId or template must be supplied. \n[Command Reference](createGovernanceRule)""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle ID ([OCID]) of the root compartment containing the governance rule.""")
@cli_util.option('--display-name', required=True, help=u"""Display name of the governance rule.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

Example: `QUOTA`""")
@cli_util.option('--creation-option', required=True, type=custom_types.CliCaseInsensitiveChoice(["TEMPLATE", "CLONE"]), help=u"""The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

Example: `TEMPLATE`""")
@cli_util.option('--template-display-name', required=True, help=u"""Display name of the allowed region resource.""")
@cli_util.option('--template-regions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of allowed regions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--template-description', help=u"""Description of the allowed region resource.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-regions': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-regions': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRule'})
@cli_util.wrap_exceptions
def create_governance_rule_allowed_regions_template(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, type, creation_option, template_display_name, template_regions, description, related_resource_id, freeform_tags, defined_tags, template_description):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['type'] = type
    _details['creationOption'] = creation_option
    _details['template']['displayName'] = template_display_name
    _details['template']['regions'] = cli_util.parse_json_parameter("template_regions", template_regions)

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    _details['template']['type'] = 'ALLOWED_REGIONS'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_governance_rule(
        create_governance_rule_details=_details,
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


@inclusion_criterion_group.command(name=cli_util.override('governance_rule.create_inclusion_criterion.command_name', 'create'), help=u"""Create inclusion criterion of type tenancy or tag for the governance rule. \n[Command Reference](createInclusionCriterion)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""The Oracle ID ([OCID]) of the governance rule. Every inclusion criterion is associated with a governance rule.""")
@cli_util.option('--type', required=True, help=u"""Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.""")
@cli_util.option('--association', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'association': {'module': 'governance_rules_control_plane', 'class': 'Association'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'association': {'module': 'governance_rules_control_plane', 'class': 'Association'}}, output_type={'module': 'governance_rules_control_plane', 'class': 'InclusionCriterion'})
@cli_util.wrap_exceptions
def create_inclusion_criterion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, type, association):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['governanceRuleId'] = governance_rule_id
    _details['type'] = type

    if association is not None:
        _details['association'] = cli_util.parse_json_parameter("association", association)

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_inclusion_criterion(
        create_inclusion_criterion_details=_details,
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


@inclusion_criterion_group.command(name=cli_util.override('governance_rule.create_inclusion_criterion_tenancy_association.command_name', 'create-inclusion-criterion-tenancy-association'), help=u"""Create inclusion criterion of type tenancy or tag for the governance rule. \n[Command Reference](createInclusionCriterion)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""The Oracle ID ([OCID]) of the governance rule. Every inclusion criterion is associated with a governance rule.""")
@cli_util.option('--type', required=True, help=u"""Type of inclusion criterion - TENANCY, ALL or TAG. We support TENANCY and ALL for now.""")
@cli_util.option('--association-tenancy-id', required=True, help=u"""The Oracle ID ([OCID]) of the tenancy to which the governance rule will be applied as part of this tenancy inclusion criterion.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'InclusionCriterion'})
@cli_util.wrap_exceptions
def create_inclusion_criterion_tenancy_association(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, type, association_tenancy_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['association'] = {}
    _details['governanceRuleId'] = governance_rule_id
    _details['type'] = type
    _details['association']['tenancyId'] = association_tenancy_id

    _details['association']['type'] = 'TENANCY'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.create_inclusion_criterion(
        create_inclusion_criterion_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.delete_governance_rule.command_name', 'delete'), help=u"""Delete the specified governance rule. \n[Command Reference](deleteGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_governance_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, if_match):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.delete_governance_rule(
        governance_rule_id=governance_rule_id,
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


@inclusion_criterion_group.command(name=cli_util.override('governance_rule.delete_inclusion_criterion.command_name', 'delete'), help=u"""Delete the specified inclusion criterion. \n[Command Reference](deleteInclusionCriterion)""")
@cli_util.option('--inclusion-criterion-id', required=True, help=u"""Unique inclusion criterion identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_inclusion_criterion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, inclusion_criterion_id, if_match):

    if isinstance(inclusion_criterion_id, six.string_types) and len(inclusion_criterion_id.strip()) == 0:
        raise click.UsageError('Parameter --inclusion-criterion-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.delete_inclusion_criterion(
        inclusion_criterion_id=inclusion_criterion_id,
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


@enforced_governance_rule_group.command(name=cli_util.override('governance_rule.get_enforced_governance_rule.command_name', 'get'), help=u"""Get the specified enforced governance rule's information. \n[Command Reference](getEnforcedGovernanceRule)""")
@cli_util.option('--enforced-governance-rule-id', required=True, help=u"""Unique enforced governance rule identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'EnforcedGovernanceRule'})
@cli_util.wrap_exceptions
def get_enforced_governance_rule(ctx, from_json, enforced_governance_rule_id):

    if isinstance(enforced_governance_rule_id, six.string_types) and len(enforced_governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --enforced-governance-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.get_enforced_governance_rule(
        enforced_governance_rule_id=enforced_governance_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@governance_rule_group.command(name=cli_util.override('governance_rule.get_governance_rule.command_name', 'get'), help=u"""Get the specified governance rule's information. \n[Command Reference](getGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRule'})
@cli_util.wrap_exceptions
def get_governance_rule(ctx, from_json, governance_rule_id):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.get_governance_rule(
        governance_rule_id=governance_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@inclusion_criterion_group.command(name=cli_util.override('governance_rule.get_inclusion_criterion.command_name', 'get'), help=u"""Get the specified inclusion criterion's information. \n[Command Reference](getInclusionCriterion)""")
@cli_util.option('--inclusion-criterion-id', required=True, help=u"""Unique inclusion criterion identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'InclusionCriterion'})
@cli_util.wrap_exceptions
def get_inclusion_criterion(ctx, from_json, inclusion_criterion_id):

    if isinstance(inclusion_criterion_id, six.string_types) and len(inclusion_criterion_id.strip()) == 0:
        raise click.UsageError('Parameter --inclusion-criterion-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.get_inclusion_criterion(
        inclusion_criterion_id=inclusion_criterion_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tenancy_attachment_group.command(name=cli_util.override('governance_rule.get_tenancy_attachment.command_name', 'get'), help=u"""Get the specified tenancy attachment's information. \n[Command Reference](getTenancyAttachment)""")
@cli_util.option('--tenancy-attachment-id', required=True, help=u"""Unique tenancy attachment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'TenancyAttachment'})
@cli_util.wrap_exceptions
def get_tenancy_attachment(ctx, from_json, tenancy_attachment_id):

    if isinstance(tenancy_attachment_id, six.string_types) and len(tenancy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.get_tenancy_attachment(
        tenancy_attachment_id=tenancy_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@enforced_governance_rule_group.command(name=cli_util.override('governance_rule.list_enforced_governance_rules.command_name', 'list'), help=u"""List enforced governance rules. Either compartment id or enforced governance rule id must be supplied. An optional governance rule type or a display name can also be supplied. \n[Command Reference](listEnforcedGovernanceRules)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--enforced-governance-rule-id', help=u"""Unique enforced governance rule identifier.""")
@cli_util.option('--governance-rule-type', type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""A filter to return only resources that match the type given.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'EnforcedGovernanceRuleCollection'})
@cli_util.wrap_exceptions
def list_enforced_governance_rules(ctx, from_json, all_pages, page_size, compartment_id, enforced_governance_rule_id, governance_rule_type, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if enforced_governance_rule_id is not None:
        kwargs['enforced_governance_rule_id'] = enforced_governance_rule_id
    if governance_rule_type is not None:
        kwargs['governance_rule_type'] = governance_rule_type
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
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_enforced_governance_rules,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_enforced_governance_rules,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_enforced_governance_rules(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@governance_rule_group.command(name=cli_util.override('governance_rule.list_governance_rules.command_name', 'list'), help=u"""List governance rules. Either compartment id or governance rule id must be supplied. An optional lifecycle state, display name or a governance rule type can also be supplied. \n[Command Reference](listGovernanceRules)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--governance-rule-id', help=u"""Unique governance rule identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only resources whose lifecycle state matches the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--governance-rule-type', type=custom_types.CliCaseInsensitiveChoice(["QUOTA", "TAG", "ALLOWED_REGIONS"]), help=u"""A filter to return only resources that match the type given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'GovernanceRuleCollection'})
@cli_util.wrap_exceptions
def list_governance_rules(ctx, from_json, all_pages, page_size, compartment_id, governance_rule_id, lifecycle_state, display_name, governance_rule_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if governance_rule_id is not None:
        kwargs['governance_rule_id'] = governance_rule_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if governance_rule_type is not None:
        kwargs['governance_rule_type'] = governance_rule_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_governance_rules,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_governance_rules,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_governance_rules(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@inclusion_criterion_group.command(name=cli_util.override('governance_rule.list_inclusion_criteria.command_name', 'list-inclusion-criteria'), help=u"""List inclusion criteria associated with a governance rule. Governance rule id must be supplied. An optional inclusion criterion id or a lifecycle state can also be supplied. \n[Command Reference](listInclusionCriteria)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--inclusion-criterion-id', help=u"""Unique inclusion criterion identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""A filter to return only resources when their lifecycle state matches the given lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'InclusionCriterionCollection'})
@cli_util.wrap_exceptions
def list_inclusion_criteria(ctx, from_json, all_pages, page_size, governance_rule_id, inclusion_criterion_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if inclusion_criterion_id is not None:
        kwargs['inclusion_criterion_id'] = inclusion_criterion_id
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
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_inclusion_criteria,
            governance_rule_id=governance_rule_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_inclusion_criteria,
            limit,
            page_size,
            governance_rule_id=governance_rule_id,
            **kwargs
        )
    else:
        result = client.list_inclusion_criteria(
            governance_rule_id=governance_rule_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tenancy_attachment_group.command(name=cli_util.override('governance_rule.list_tenancy_attachments.command_name', 'list'), help=u"""List tenancy attachments. Either compartment id, governance rule id or tenancy attachment id must be supplied. An optional lifecycle state or a child tenancy id can also be supplied. \n[Command Reference](listTenancyAttachments)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--tenancy-attachment-id', help=u"""Unique tenancy attachment identifier.""")
@cli_util.option('--governance-rule-id', help=u"""Unique governance rule identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "DELETING", "DELETED"]), help=u"""A filter to return only resources when their lifecycle state matches the given lifecycle state.""")
@cli_util.option('--child-tenancy-id', help=u"""A filter to return only governance rules that match the given tenancy id.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'governance_rules_control_plane', 'class': 'TenancyAttachmentCollection'})
@cli_util.wrap_exceptions
def list_tenancy_attachments(ctx, from_json, all_pages, page_size, compartment_id, tenancy_attachment_id, governance_rule_id, lifecycle_state, child_tenancy_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if tenancy_attachment_id is not None:
        kwargs['tenancy_attachment_id'] = tenancy_attachment_id
    if governance_rule_id is not None:
        kwargs['governance_rule_id'] = governance_rule_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if child_tenancy_id is not None:
        kwargs['child_tenancy_id'] = child_tenancy_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tenancy_attachments,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tenancy_attachments,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_tenancy_attachments(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@governance_rule_group.command(name=cli_util.override('governance_rule.retry_governance_rule.command_name', 'retry'), help=u"""Retry the creation of the specified governance rule. Used by the tenancy admins when all the workflow retries have exhausted. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](retryGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def retry_governance_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, if_match):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.retry_governance_rule(
        governance_rule_id=governance_rule_id,
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


@tenancy_attachment_group.command(name=cli_util.override('governance_rule.retry_tenancy_attachment.command_name', 'retry'), help=u"""Retry governance rule application for the specified tenancy attachment id. Used by the tenancy admins when all the workflow retries have exhausted. \n[Command Reference](retryTenancyAttachment)""")
@cli_util.option('--tenancy-attachment-id', required=True, help=u"""Unique tenancy attachment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def retry_tenancy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tenancy_attachment_id, if_match):

    if isinstance(tenancy_attachment_id, six.string_types) and len(tenancy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.retry_tenancy_attachment(
        tenancy_attachment_id=tenancy_attachment_id,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.update_governance_rule.command_name', 'update'), help=u"""Update the specified governance rule. \n[Command Reference](updateGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--display-name', help=u"""Display name of the governance rule.""")
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--template', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'template': {'module': 'governance_rules_control_plane', 'class': 'Template'}, 'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'template': {'module': 'governance_rules_control_plane', 'class': 'Template'}, 'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_governance_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, display_name, description, template, related_resource_id, freeform_tags, defined_tags, if_match):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')
    if not force:
        if template or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to template and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if template is not None:
        _details['template'] = cli_util.parse_json_parameter("template", template)

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.update_governance_rule(
        governance_rule_id=governance_rule_id,
        update_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.update_governance_rule_tag_template.command_name', 'update-governance-rule-tag-template'), help=u"""Update the specified governance rule. \n[Command Reference](updateGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--template-name', required=True, help=u"""The name of the tag namespace. It must be unique across all tag namespaces in the tenancy and cannot be changed.""")
@cli_util.option('--display-name', help=u"""Display name of the governance rule.""")
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--template-description', help=u"""Description of the tag namespace.""")
@cli_util.option('--template-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Represents an array of tags for tag namespace.

This option is a JSON list with items of type Tag.  For documentation on Tag please see our API reference: https://docs.cloud.oracle.com/api/#/en/governancerule/20220504/datatypes/Tag.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--template-tag-defaults', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type TagDefault.  For documentation on TagDefault please see our API reference: https://docs.cloud.oracle.com/api/#/en/governancerule/20220504/datatypes/TagDefault.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-tags': {'module': 'governance_rules_control_plane', 'class': 'list[Tag]'}, 'template-tag-defaults': {'module': 'governance_rules_control_plane', 'class': 'list[TagDefault]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-tags': {'module': 'governance_rules_control_plane', 'class': 'list[Tag]'}, 'template-tag-defaults': {'module': 'governance_rules_control_plane', 'class': 'list[TagDefault]'}})
@cli_util.wrap_exceptions
def update_governance_rule_tag_template(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, template_name, display_name, description, related_resource_id, freeform_tags, defined_tags, if_match, template_description, template_tags, template_tag_defaults):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['template']['name'] = template_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    if template_tags is not None:
        _details['template']['tags'] = cli_util.parse_json_parameter("template_tags", template_tags)

    if template_tag_defaults is not None:
        _details['template']['tagDefaults'] = cli_util.parse_json_parameter("template_tag_defaults", template_tag_defaults)

    _details['template']['type'] = 'TAG'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.update_governance_rule(
        governance_rule_id=governance_rule_id,
        update_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.update_governance_rule_quota_template.command_name', 'update-governance-rule-quota-template'), help=u"""Update the specified governance rule. \n[Command Reference](updateGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--template-display-name', required=True, help=u"""Display name of the quota resource.""")
@cli_util.option('--template-statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of quota statements.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the governance rule.""")
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--template-description', help=u"""Description of the quota resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-statements': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-statements': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_governance_rule_quota_template(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, template_display_name, template_statements, display_name, description, related_resource_id, freeform_tags, defined_tags, if_match, template_description):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['template']['displayName'] = template_display_name
    _details['template']['statements'] = cli_util.parse_json_parameter("template_statements", template_statements)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    _details['template']['type'] = 'QUOTA'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.update_governance_rule(
        governance_rule_id=governance_rule_id,
        update_governance_rule_details=_details,
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


@governance_rule_group.command(name=cli_util.override('governance_rule.update_governance_rule_allowed_regions_template.command_name', 'update-governance-rule-allowed-regions-template'), help=u"""Update the specified governance rule. \n[Command Reference](updateGovernanceRule)""")
@cli_util.option('--governance-rule-id', required=True, help=u"""Unique governance rule identifier.""")
@cli_util.option('--template-display-name', required=True, help=u"""Display name of the allowed region resource.""")
@cli_util.option('--template-regions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of allowed regions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the governance rule.""")
@cli_util.option('--description', help=u"""Description of the governance rule.""")
@cli_util.option('--related-resource-id', help=u"""The Oracle ID ([OCID]) of the resource, which was used as a template to create this governance rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--template-description', help=u"""Description of the allowed region resource.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-regions': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'governance_rules_control_plane', 'class': 'dict(str, dict(str, object))'}, 'template-regions': {'module': 'governance_rules_control_plane', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_governance_rule_allowed_regions_template(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, governance_rule_id, template_display_name, template_regions, display_name, description, related_resource_id, freeform_tags, defined_tags, if_match, template_description):

    if isinstance(governance_rule_id, six.string_types) and len(governance_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --governance-rule-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['template'] = {}
    _details['template']['displayName'] = template_display_name
    _details['template']['regions'] = cli_util.parse_json_parameter("template_regions", template_regions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if template_description is not None:
        _details['template']['description'] = template_description

    _details['template']['type'] = 'ALLOWED_REGIONS'

    client = cli_util.build_client('governance_rules_control_plane', 'governance_rule', ctx)
    result = client.update_governance_rule(
        governance_rule_id=governance_rule_id,
        update_governance_rule_details=_details,
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
