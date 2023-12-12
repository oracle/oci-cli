# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import oci
import sys
from services.adm.src.oci_cli_application_dependency_management.generated import applicationdependencymanagement_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Remove create-remediation-recipe-external-scm-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_external_scm_configuration.name)


# Remove create-remediation-recipe-github-actions-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_git_hub_actions_configuration.name)


# Remove create-remediation-recipe-gitlab-pipeline-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_git_lab_pipeline_configuration.name)


# Remove create-remediation-recipe-jenkins-pipeline-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_jenkins_pipeline_configuration.name)


# Remove create-remediation-recipe-none-verify-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_none_verify_configuration.name)


# Remove create-remediation-recipe-oci-code-repository-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_oci_code_repository_configuration.name)


# Remove create-remediation-recipe-oci-devops-build-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.create_remediation_recipe_oci_dev_ops_build_configuration.name)


# Remove update-remediation-recipe-external-scm-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_external_scm_configuration.name)


# Remove update-remediation-recipe-github-actions-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_git_hub_actions_configuration.name)


# Remove update-remediation-recipe-gitlab-pipeline-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_git_lab_pipeline_configuration.name)


# Remove update-remediation-recipe-jenkins-pipeline-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_jenkins_pipeline_configuration.name)


# Remove update-remediation-recipe-none-verify-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_none_verify_configuration.name)


# Remove update-remediation-recipe-oci-code-repository-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_oci_code_repository_configuration.name)


# Remove update-remediation-recipe-oci-devops-build-configuration from oci adm remediation-recipe
applicationdependencymanagement_cli.remediation_recipe_group.commands.pop(applicationdependencymanagement_cli.update_remediation_recipe_oci_dev_ops_build_configuration.name)


@cli_util.copy_params_from_generated_command(applicationdependencymanagement_cli.create_vulnerability_audit, params_to_exclude=['wait_for_state'])
@applicationdependencymanagement_cli.vulnerability_audit_group.command(name="create", help=applicationdependencymanagement_cli.create_vulnerability_audit.help)
@click.pass_context
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state ACTIVE --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'source': {'module': 'adm', 'class': 'VulnerabilityAuditSource'}, 'usage-data': {'module': 'adm', 'class': 'UsageDataViaObjectStorageTupleDetails'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, usage_data, display_name, source, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if usage_data is not None:
        _details['usageData'] = cli_util.parse_json_parameter("usage_data", usage_data)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vulnerability_audit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(applicationdependencymanagement_cli.create_vulnerability_audit_unknown_source_vulnerability_audit_source, params_to_exclude=['wait_for_state'])
@applicationdependencymanagement_cli.vulnerability_audit_group.command(name="create-vulnerability-audit-unknown-source-vulnerability-audit-source", help=applicationdependencymanagement_cli.create_vulnerability_audit_unknown_source_vulnerability_audit_source.help)
@click.pass_context
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state ACTIVE --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'usage-data': {'module': 'adm', 'class': 'UsageDataViaObjectStorageTupleDetails'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_unknown_source_vulnerability_audit_source_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, usage_data, display_name, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if usage_data is not None:
        _details['usageData'] = cli_util.parse_json_parameter("usage_data", usage_data)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['type'] = 'UNKNOWN'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vulnerability_audit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(applicationdependencymanagement_cli.create_vulnerability_audit_oci_resource_vulnerability_audit_source, params_to_exclude=['wait_for_state'])
@applicationdependencymanagement_cli.vulnerability_audit_group.command(name="create-vulnerability-audit-oci-resource-vulnerability-audit-source", help=applicationdependencymanagement_cli.create_vulnerability_audit_oci_resource_vulnerability_audit_source.help)
@click.pass_context
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state ACTIVE --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'usage-data': {'module': 'adm', 'class': 'UsageDataViaObjectStorageTupleDetails'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_oci_resource_vulnerability_audit_source_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, source_oci_resource_id, compartment_id, application_dependencies, configuration, usage_data, display_name, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type
    _details['source']['ociResourceId'] = source_oci_resource_id

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if usage_data is not None:
        _details['usageData'] = cli_util.parse_json_parameter("usage_data", usage_data)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['type'] = 'OCI_RESOURCE'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vulnerability_audit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@cli_util.copy_params_from_generated_command(applicationdependencymanagement_cli.create_vulnerability_audit_external_resource_vulnerability_audit_source, params_to_exclude=['wait_for_state'])
@applicationdependencymanagement_cli.vulnerability_audit_group.command(name="create-vulnerability-audit-external-resource-vulnerability-audit-source", help=applicationdependencymanagement_cli.create_vulnerability_audit_external_resource_vulnerability_audit_source.help)
@click.pass_context
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state ACTIVE --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'usage-data': {'module': 'adm', 'class': 'UsageDataViaObjectStorageTupleDetails'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_external_resource_vulnerability_audit_source_extended(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, usage_data, display_name, freeform_tags, defined_tags, if_match, source_description):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if usage_data is not None:
        _details['usageData'] = cli_util.parse_json_parameter("usage_data", usage_data)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if source_description is not None:
        _details['source']['description'] = source_description

    _details['source']['type'] = 'EXTERNAL_RESOURCE'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vulnerability_audit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


# Remove create-vulnerability-audit-usage-data-via-object-storage-tuple-details from oci adm vulnerability-audit
applicationdependencymanagement_cli.vulnerability_audit_group.commands.pop(applicationdependencymanagement_cli.create_vulnerability_audit_usage_data_via_object_storage_tuple_details.name)
