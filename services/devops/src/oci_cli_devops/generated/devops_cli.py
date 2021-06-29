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


@cli.command(cli_util.override('devops.devops_root_group.command_name', 'devops'), cls=CommandGroupWithAlias, help=cli_util.override('devops.devops_root_group.help', """Use the DevOps APIs to create a DevOps project to group the pipelines,  add reference to target deployment environments, add artifacts to deploy,  and create deployment pipelines needed to deploy your software."""), short_help=cli_util.override('devops.devops_root_group.short_help', """DevOps API"""))
@cli_util.help_option_group
def devops_root_group():
    pass


@click.command(cli_util.override('devops.deploy_pipeline_group.command_name', 'deploy-pipeline'), cls=CommandGroupWithAlias, help="""A set of stages whose predecessor relation forms a directed acyclic graph.""")
@cli_util.help_option_group
def deploy_pipeline_group():
    pass


@click.command(cli_util.override('devops.deploy_artifact_summary_group.command_name', 'deploy-artifact-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment artifact.""")
@cli_util.help_option_group
def deploy_artifact_summary_group():
    pass


@click.command(cli_util.override('devops.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""DevOps project groups resources needed to implement the CI/CD workload. DevOps resources include artifacts, pipelines, and environments.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('devops.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('devops.deploy_artifact_group.command_name', 'deploy-artifact'), cls=CommandGroupWithAlias, help="""Artifacts are deployment manifests that are referenced in a pipeline stage for automated deployment to the target environment.  DevOps artifacts can be an OCI Container image repository, Kubernetes manifest, an Artifact Registry artifact, or defined inline.""")
@cli_util.help_option_group
def deploy_artifact_group():
    pass


@click.command(cli_util.override('devops.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Details of the work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('devops.deployment_summary_group.command_name', 'deployment-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment.""")
@cli_util.help_option_group
def deployment_summary_group():
    pass


@click.command(cli_util.override('devops.deploy_environment_group.command_name', 'deploy-environment'), cls=CommandGroupWithAlias, help="""The target OCI resources, such as Compute instances, Container Engine for Kubernetes(OKE) clusters, or Function, where artifacts will be deployed.""")
@cli_util.help_option_group
def deploy_environment_group():
    pass


@click.command(cli_util.override('devops.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('devops.deploy_stage_summary_group.command_name', 'deploy-stage-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment stage.""")
@cli_util.help_option_group
def deploy_stage_summary_group():
    pass


@click.command(cli_util.override('devops.project_summary_group.command_name', 'project-summary'), cls=CommandGroupWithAlias, help="""Summary of the project.""")
@cli_util.help_option_group
def project_summary_group():
    pass


@click.command(cli_util.override('devops.deploy_environment_summary_group.command_name', 'deploy-environment-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment environment.""")
@cli_util.help_option_group
def deploy_environment_summary_group():
    pass


@click.command(cli_util.override('devops.deploy_stage_group.command_name', 'deploy-stage'), cls=CommandGroupWithAlias, help="""A single node in a pipeline. It is usually associated with some action on a specific set of OCI resources such as environments. For example, updating a Function or a Kubernetes cluster.""")
@cli_util.help_option_group
def deploy_stage_group():
    pass


@click.command(cli_util.override('devops.deploy_pipeline_summary_group.command_name', 'deploy-pipeline-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment pipeline.""")
@cli_util.help_option_group
def deploy_pipeline_summary_group():
    pass


@click.command(cli_util.override('devops.deployment_group.command_name', 'deployment'), cls=CommandGroupWithAlias, help="""A single execution or run of a pipeline.""")
@cli_util.help_option_group
def deployment_group():
    pass


devops_root_group.add_command(deploy_pipeline_group)
devops_root_group.add_command(deploy_artifact_summary_group)
devops_root_group.add_command(project_group)
devops_root_group.add_command(work_request_log_entry_group)
devops_root_group.add_command(deploy_artifact_group)
devops_root_group.add_command(work_request_group)
devops_root_group.add_command(deployment_summary_group)
devops_root_group.add_command(deploy_environment_group)
devops_root_group.add_command(work_request_error_group)
devops_root_group.add_command(deploy_stage_summary_group)
devops_root_group.add_command(project_summary_group)
devops_root_group.add_command(deploy_environment_summary_group)
devops_root_group.add_command(deploy_stage_group)
devops_root_group.add_command(deploy_pipeline_summary_group)
devops_root_group.add_command(deployment_group)


@deployment_group.command(name=cli_util.override('devops.approve_deployment.command_name', 'approve'), help=u"""Submit stage approval. \n[Command Reference](approveDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""The [OCID] of the stage which is marked for approval.""")
@cli_util.option('--action', required=True, type=custom_types.CliCaseInsensitiveChoice(["APPROVE", "REJECT"]), help=u"""The action of Approve or Reject.""")
@cli_util.option('--reason', help=u"""The reason for approving or rejecting the deployment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def approve_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, deploy_stage_id, action, reason, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployStageId'] = deploy_stage_id
    _details['action'] = action

    if reason is not None:
        _details['reason'] = reason

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.approve_deployment(
        deployment_id=deployment_id,
        approve_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.cancel_deployment.command_name', 'cancel'), help=u"""Cancels a deployment resource by identifier. \n[Command Reference](cancelDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--reason', required=True, help=u"""The reason for canceling the deployment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def cancel_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, reason, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['reason'] = reason

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.cancel_deployment(
        deployment_id=deployment_id,
        cancel_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@project_group.command(name=cli_util.override('devops.change_project_compartment.command_name', 'change-compartment'), help=u"""Moves a project resource from one compartment OCID to another. \n[Command Reference](changeProjectCompartment)""")
@cli_util.option('--project-id', required=True, help=u"""Unique project identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which the resource must be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_project_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.change_project_compartment(
        project_id=project_id,
        change_project_compartment_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.create_deploy_artifact.command_name', 'create'), help=u"""Creates a new deployment artifact. \n[Command Reference](createDeployArtifact)""")
@cli_util.option('--deploy-artifact-type', required=True, help=u"""Type of the deployment artifact.""")
@cli_util.option('--deploy-artifact-source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--argument-substitution-mode', required=True, help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-artifact-source': {'module': 'devops', 'class': 'DeployArtifactSource'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-artifact-source': {'module': 'devops', 'class': 'DeployArtifactSource'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_type, deploy_artifact_source, argument_substitution_mode, project_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactType'] = deploy_artifact_type
    _details['deployArtifactSource'] = cli_util.parse_json_parameter("deploy_artifact_source", deploy_artifact_source)
    _details['argumentSubstitutionMode'] = argument_substitution_mode
    _details['projectId'] = project_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_artifact(
        create_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.create_deploy_artifact_generic_deploy_artifact_source.command_name', 'create-deploy-artifact-generic-deploy-artifact-source'), help=u"""Creates a new deployment artifact. \n[Command Reference](createDeployArtifact)""")
@cli_util.option('--deploy-artifact-type', required=True, help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', required=True, help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--deploy-artifact-source-repository-id', required=True, help=u"""The OCID of a repository""")
@cli_util.option('--deploy-artifact-source-deploy-artifact-path', required=True, help=u"""Specifies the artifact path in the repository.""")
@cli_util.option('--deploy-artifact-source-deploy-artifact-version', required=True, help=u"""Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_generic_deploy_artifact_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_type, argument_substitution_mode, project_id, deploy_artifact_source_repository_id, deploy_artifact_source_deploy_artifact_path, deploy_artifact_source_deploy_artifact_version, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactType'] = deploy_artifact_type
    _details['argumentSubstitutionMode'] = argument_substitution_mode
    _details['projectId'] = project_id
    _details['deployArtifactSource']['repositoryId'] = deploy_artifact_source_repository_id
    _details['deployArtifactSource']['deployArtifactPath'] = deploy_artifact_source_deploy_artifact_path
    _details['deployArtifactSource']['deployArtifactVersion'] = deploy_artifact_source_deploy_artifact_version

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'GENERIC_ARTIFACT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_artifact(
        create_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.create_deploy_artifact_ocir_deploy_artifact_source.command_name', 'create-deploy-artifact-ocir-deploy-artifact-source'), help=u"""Creates a new deployment artifact. \n[Command Reference](createDeployArtifact)""")
@cli_util.option('--deploy-artifact-type', required=True, help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', required=True, help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--deploy-artifact-source-image-uri', required=True, help=u"""Specifies OCIR Image Path - optionally include tag.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-source-image-digest', help=u"""Specifies image digest for the version of the image.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_ocir_deploy_artifact_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_type, argument_substitution_mode, project_id, deploy_artifact_source_image_uri, description, display_name, freeform_tags, defined_tags, deploy_artifact_source_image_digest):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactType'] = deploy_artifact_type
    _details['argumentSubstitutionMode'] = argument_substitution_mode
    _details['projectId'] = project_id
    _details['deployArtifactSource']['imageUri'] = deploy_artifact_source_image_uri

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_artifact_source_image_digest is not None:
        _details['deployArtifactSource']['imageDigest'] = deploy_artifact_source_image_digest

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'OCIR'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_artifact(
        create_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.create_deploy_artifact_inline_deploy_artifact_source.command_name', 'create-deploy-artifact-inline-deploy-artifact-source'), help=u"""Creates a new deployment artifact. \n[Command Reference](createDeployArtifact)""")
@cli_util.option('--deploy-artifact-type', required=True, help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', required=True, help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--deploy-artifact-source-base64-encoded-content', required=True, help=u"""base64 Encoded String""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def create_deploy_artifact_inline_deploy_artifact_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_type, argument_substitution_mode, project_id, deploy_artifact_source_base64_encoded_content, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactType'] = deploy_artifact_type
    _details['argumentSubstitutionMode'] = argument_substitution_mode
    _details['projectId'] = project_id
    _details['deployArtifactSource']['base64EncodedContent'] = deploy_artifact_source_base64_encoded_content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'INLINE'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_artifact(
        create_deploy_artifact_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.create_deploy_environment.command_name', 'create'), help=u"""Creates a new deployment environment. \n[Command Reference](createDeployEnvironment)""")
@cli_util.option('--deploy-environment-type', required=True, help=u"""Deployment environment type.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def create_deploy_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_type, project_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployEnvironmentType'] = deploy_environment_type
    _details['projectId'] = project_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_environment(
        create_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.create_deploy_environment_create_compute_instance_group_deploy_environment_details.command_name', 'create-deploy-environment-create-compute-instance-group-deploy-environment-details'), help=u"""Creates a new deployment environment. \n[Command Reference](createDeployEnvironment)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--compute-instance-group-selectors', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'compute-instance-group-selectors': {'module': 'devops', 'class': 'ComputeInstanceGroupSelectorCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'compute-instance-group-selectors': {'module': 'devops', 'class': 'ComputeInstanceGroupSelectorCollection'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def create_deploy_environment_create_compute_instance_group_deploy_environment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compute_instance_group_selectors, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['computeInstanceGroupSelectors'] = cli_util.parse_json_parameter("compute_instance_group_selectors", compute_instance_group_selectors)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployEnvironmentType'] = 'COMPUTE_INSTANCE_GROUP'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_environment(
        create_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.create_deploy_environment_create_oke_cluster_deploy_environment_details.command_name', 'create-deploy-environment-create-oke-cluster-deploy-environment-details'), help=u"""Creates a new deployment environment. \n[Command Reference](createDeployEnvironment)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the Kubernetes cluster.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def create_deploy_environment_create_oke_cluster_deploy_environment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, cluster_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['clusterId'] = cluster_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployEnvironmentType'] = 'OKE_CLUSTER'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_environment(
        create_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.create_deploy_environment_create_function_deploy_environment_details.command_name', 'create-deploy-environment-create-function-deploy-environment-details'), help=u"""Creates a new deployment environment. \n[Command Reference](createDeployEnvironment)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--function-id', required=True, help=u"""The OCID of the Function.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def create_deploy_environment_create_function_deploy_environment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, function_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['functionId'] = function_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployEnvironmentType'] = 'FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_environment(
        create_deploy_environment_details=_details,
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


@deploy_pipeline_group.command(name=cli_util.override('devops.create_deploy_pipeline.command_name', 'create'), help=u"""Creates a new deployment pipeline. \n[Command Reference](createDeployPipeline)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--description', help=u"""Optional description about the deployment pipeline.""")
@cli_util.option('--display-name', help=u"""Deployment pipeline display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def create_deploy_pipeline(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, description, display_name, deploy_pipeline_parameters, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_pipeline_parameters is not None:
        _details['deployPipelineParameters'] = cli_util.parse_json_parameter("deploy_pipeline_parameters", deploy_pipeline_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_pipeline(
        create_deploy_pipeline_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage.command_name', 'create'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-stage-type', required=True, help=u"""Deployment stage type.""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_type, deploy_pipeline_id, deploy_stage_predecessor_collection, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployStageType'] = deploy_stage_type
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_manual_approval_deploy_stage_details.command_name', 'create-deploy-stage-create-manual-approval-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--approval-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_manual_approval_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, approval_policy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['approvalPolicy'] = cli_util.parse_json_parameter("approval_policy", approval_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'MANUAL_APPROVAL'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_wait_deploy_stage_details.command_name', 'create-deploy-stage-create-wait-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-criteria', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_wait_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, wait_criteria, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['waitCriteria'] = cli_util.parse_json_parameter("wait_criteria", wait_criteria)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'WAIT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--namespace', help=u"""Default namespace to be used for Kubernetes deployment when not specified in the manifest.""")
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_cluster_deploy_environment_id, kubernetes_manifest_deploy_artifact_ids, description, display_name, freeform_tags, defined_tags, namespace, rollback_policy):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeClusterDeployEnvironmentId'] = oke_cluster_deploy_environment_id
    _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if namespace is not None:
        _details['namespace'] = namespace

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'OKE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details.command_name', 'create-deploy-stage-create-load-balancer-traffic-shift-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--blue-backend-ips', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--green-backend-ips', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--traffic-shift-target', required=True, help=u"""Specifies the target or destination backend set.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_load_balancer_traffic_shift_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, blue_backend_ips, green_backend_ips, traffic_shift_target, rollout_policy, load_balancer_config, description, display_name, freeform_tags, defined_tags, rollback_policy):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['blueBackendIps'] = cli_util.parse_json_parameter("blue_backend_ips", blue_backend_ips)
    _details['greenBackendIps'] = cli_util.parse_json_parameter("green_backend_ips", green_backend_ips)
    _details['trafficShiftTarget'] = traffic_shift_target
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)
    _details['loadBalancerConfig'] = cli_util.parse_json_parameter("load_balancer_config", load_balancer_config)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'LOAD_BALANCER_TRAFFIC_SHIFT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-deploy-environment-id', required=True, help=u"""A compute instance group environment OCID for rolling deployment.""")
@cli_util.option('--deployment-spec-deploy-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--failure-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, compute_instance_group_deploy_environment_id, deployment_spec_deploy_artifact_id, rollout_policy, description, display_name, freeform_tags, defined_tags, deploy_artifact_ids, rollback_policy, failure_policy, load_balancer_config):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['computeInstanceGroupDeployEnvironmentId'] = compute_instance_group_deploy_environment_id
    _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_artifact_ids is not None:
        _details['deployArtifactIds'] = cli_util.parse_json_parameter("deploy_artifact_ids", deploy_artifact_ids)

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    if failure_policy is not None:
        _details['failurePolicy'] = cli_util.parse_json_parameter("failure_policy", failure_policy)

    if load_balancer_config is not None:
        _details['loadBalancerConfig'] = cli_util.parse_json_parameter("load_balancer_config", load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_invoke_function_deploy_stage_details.command_name', 'create-deploy-stage-create-invoke-function-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-deploy-environment-id', required=True, help=u"""Function environment OCID.""")
@cli_util.option('--is-async', required=True, type=click.BOOL, help=u"""A boolean flag specifies whether this stage executes asynchronously.""")
@cli_util.option('--is-validation-enabled', required=True, type=click.BOOL, help=u"""A boolean flag specifies whether the invoked function should be validated.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-id', help=u"""Optional binary artifact OCID user may provide to this stage.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_invoke_function_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, function_deploy_environment_id, is_async, is_validation_enabled, description, display_name, freeform_tags, defined_tags, deploy_artifact_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['functionDeployEnvironmentId'] = function_deploy_environment_id
    _details['isAsync'] = is_async
    _details['isValidationEnabled'] = is_validation_enabled

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_artifact_id is not None:
        _details['deployArtifactId'] = deploy_artifact_id

    _details['deployStageType'] = 'INVOKE_FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_function_deploy_stage_details.command_name', 'create-deploy-stage-create-function-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-deploy-environment-id', required=True, help=u"""Function environment OCID.""")
@cli_util.option('--docker-image-deploy-artifact-id', required=True, help=u"""A Docker image artifact OCID.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""User provided key and value pair configuration, which is assigned through constants or parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-memory-in-mbs', type=click.INT, help=u"""Maximum usable memory for the Function (in MB).""")
@cli_util.option('--function-timeout-in-seconds', type=click.INT, help=u"""Timeout for execution of the Function. Value in seconds.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_function_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, function_deploy_environment_id, docker_image_deploy_artifact_id, description, display_name, freeform_tags, defined_tags, config, max_memory_in_mbs, function_timeout_in_seconds):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['functionDeployEnvironmentId'] = function_deploy_environment_id
    _details['dockerImageDeployArtifactId'] = docker_image_deploy_artifact_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if max_memory_in_mbs is not None:
        _details['maxMemoryInMBs'] = max_memory_in_mbs

    if function_timeout_in_seconds is not None:
        _details['functionTimeoutInSeconds'] = function_timeout_in_seconds

    _details['deployStageType'] = 'DEPLOY_FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deploy_stage(
        create_deploy_stage_details=_details,
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


@deployment_group.command(name=cli_util.override('devops.create_deployment.command_name', 'create'), help=u"""Creates a new deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deployment-type', required=True, help=u"""Specifies type for this deployment.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deployment_type, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deploymentType'] = deployment_type

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deployment(
        create_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.create_deployment_create_deploy_pipeline_redeployment_details.command_name', 'create-deployment-create-deploy-pipeline-redeployment-details'), help=u"""Creates a new deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--previous-deployment-id', help=u"""Specifies the OCID of the previous deployment to be redeployed.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_deploy_pipeline_redeployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, display_name, freeform_tags, defined_tags, previous_deployment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if previous_deployment_id is not None:
        _details['previousDeploymentId'] = previous_deployment_id

    _details['deploymentType'] = 'PIPELINE_REDEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deployment(
        create_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.create_deployment_create_deploy_pipeline_deployment_details.command_name', 'create-deployment-create-deploy-pipeline-deployment-details'), help=u"""Creates a new deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'deploy-artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'deploy-artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_deploy_pipeline_deployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, display_name, freeform_tags, defined_tags, deployment_arguments, deploy_artifact_override_arguments):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deployment_arguments is not None:
        _details['deploymentArguments'] = cli_util.parse_json_parameter("deployment_arguments", deployment_arguments)

    if deploy_artifact_override_arguments is not None:
        _details['deployArtifactOverrideArguments'] = cli_util.parse_json_parameter("deploy_artifact_override_arguments", deploy_artifact_override_arguments)

    _details['deploymentType'] = 'PIPELINE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deployment(
        create_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.create_deployment_create_single_deploy_stage_deployment_details.command_name', 'create-deployment-create-single-deploy-stage-deployment-details'), help=u"""Creates a new deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-stage-id', help=u"""Specifies the OCID of the stage to be redeployed.""")
@cli_util.option('--deployment-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-override-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'deploy-artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deployment-arguments': {'module': 'devops', 'class': 'DeploymentArgumentCollection'}, 'deploy-artifact-override-arguments': {'module': 'devops', 'class': 'DeployArtifactOverrideArgumentCollection'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_single_deploy_stage_deployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, display_name, freeform_tags, defined_tags, deploy_stage_id, deployment_arguments, deploy_artifact_override_arguments):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_stage_id is not None:
        _details['deployStageId'] = deploy_stage_id

    if deployment_arguments is not None:
        _details['deploymentArguments'] = cli_util.parse_json_parameter("deployment_arguments", deployment_arguments)

    if deploy_artifact_override_arguments is not None:
        _details['deployArtifactOverrideArguments'] = cli_util.parse_json_parameter("deploy_artifact_override_arguments", deploy_artifact_override_arguments)

    _details['deploymentType'] = 'SINGLE_STAGE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_deployment(
        create_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@project_group.command(name=cli_util.override('devops.create_project.command_name', 'create'), help=u"""Creates a new project. \n[Command Reference](createProject)""")
@cli_util.option('--name', required=True, help=u"""Project name (case-sensitive).""")
@cli_util.option('--notification-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the project is created.""")
@cli_util.option('--description', help=u"""Project description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'notification-config': {'module': 'devops', 'class': 'NotificationConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'notification-config': {'module': 'devops', 'class': 'NotificationConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Project'})
@cli_util.wrap_exceptions
def create_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, notification_config, compartment_id, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['notificationConfig'] = cli_util.parse_json_parameter("notification_config", notification_config)
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_project(
        create_project_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.delete_deploy_artifact.command_name', 'delete'), help=u"""Deletes a deployment artifact resource by identifier. \n[Command Reference](deleteDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_artifact(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, if_match):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
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


@deploy_environment_group.command(name=cli_util.override('devops.delete_deploy_environment.command_name', 'delete'), help=u"""Deletes a deployment environment resource by identifier. \n[Command Reference](deleteDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_environment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_deploy_environment(
        deploy_environment_id=deploy_environment_id,
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


@deploy_pipeline_group.command(name=cli_util.override('devops.delete_deploy_pipeline.command_name', 'delete'), help=u"""Deletes a deployment pipeline resource by identifier. \n[Command Reference](deleteDeployPipeline)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""Unique pipeline identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_pipeline(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, if_match):

    if isinstance(deploy_pipeline_id, six.string_types) and len(deploy_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-pipeline-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_deploy_pipeline(
        deploy_pipeline_id=deploy_pipeline_id,
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


@deploy_stage_group.command(name=cli_util.override('devops.delete_deploy_stage.command_name', 'delete'), help=u"""Deletes a deployment stage resource by identifier. \n[Command Reference](deleteDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_deploy_stage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_deploy_stage(
        deploy_stage_id=deploy_stage_id,
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


@project_group.command(name=cli_util.override('devops.delete_project.command_name', 'delete'), help=u"""Deletes a project resource by identifier \n[Command Reference](deleteProject)""")
@cli_util.option('--project-id', required=True, help=u"""Unique project identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_project(
        project_id=project_id,
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


@deploy_artifact_group.command(name=cli_util.override('devops.get_deploy_artifact.command_name', 'get'), help=u"""Retrieves a deployment artifact by identifier. \n[Command Reference](getDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def get_deploy_artifact(ctx, from_json, deploy_artifact_id):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deploy_environment_group.command(name=cli_util.override('devops.get_deploy_environment.command_name', 'get'), help=u"""Retrieves a deployment environment by identifier. \n[Command Reference](getDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def get_deploy_environment(ctx, from_json, deploy_environment_id):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_deploy_environment(
        deploy_environment_id=deploy_environment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deploy_pipeline_group.command(name=cli_util.override('devops.get_deploy_pipeline.command_name', 'get'), help=u"""Retrieves a deployment pipeline by identifier. \n[Command Reference](getDeployPipeline)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""Unique pipeline identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def get_deploy_pipeline(ctx, from_json, deploy_pipeline_id):

    if isinstance(deploy_pipeline_id, six.string_types) and len(deploy_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-pipeline-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_deploy_pipeline(
        deploy_pipeline_id=deploy_pipeline_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deploy_stage_group.command(name=cli_util.override('devops.get_deploy_stage.command_name', 'get'), help=u"""Retrieves a deployment stage by identifier. \n[Command Reference](getDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def get_deploy_stage(ctx, from_json, deploy_stage_id):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deployment_group.command(name=cli_util.override('devops.get_deployment.command_name', 'get'), help=u"""Retrieves a deployment by identifier. \n[Command Reference](getDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def get_deployment(ctx, from_json, deployment_id):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_deployment(
        deployment_id=deployment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('devops.get_project.command_name', 'get'), help=u"""Retrieves a project by identifier. \n[Command Reference](getProject)""")
@cli_util.option('--project-id', required=True, help=u"""Unique project identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, project_id):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_project(
        project_id=project_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('devops.get_work_request.command_name', 'get'), help=u"""Retrieves the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@deploy_artifact_summary_group.command(name=cli_util.override('devops.list_deploy_artifacts.command_name', 'list-deploy-artifacts'), help=u"""Returns a list of deployment artifacts. \n[Command Reference](listDeployArtifacts)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only DeployArtifacts that matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployArtifactCollection'})
@cli_util.wrap_exceptions
def list_deploy_artifacts(ctx, from_json, all_pages, page_size, id, project_id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deploy_artifacts,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deploy_artifacts,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_deploy_artifacts(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deploy_environment_summary_group.command(name=cli_util.override('devops.list_deploy_environments.command_name', 'list-deploy-environments'), help=u"""Returns a list of deployment environments. \n[Command Reference](listDeployEnvironments)""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only DeployEnvironments that matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployEnvironmentCollection'})
@cli_util.wrap_exceptions
def list_deploy_environments(ctx, from_json, all_pages, page_size, project_id, compartment_id, id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if project_id is not None:
        kwargs['project_id'] = project_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deploy_environments,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deploy_environments,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_deploy_environments(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deploy_pipeline_summary_group.command(name=cli_util.override('devops.list_deploy_pipelines.command_name', 'list-deploy-pipelines'), help=u"""Returns a list of deployment pipelines. \n[Command Reference](listDeployPipelines)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only DeployPipelines that matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployPipelineCollection'})
@cli_util.wrap_exceptions
def list_deploy_pipelines(ctx, from_json, all_pages, page_size, id, project_id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deploy_pipelines,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deploy_pipelines,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_deploy_pipelines(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deploy_stage_summary_group.command(name=cli_util.override('devops.list_deploy_stages.command_name', 'list-deploy-stages'), help=u"""Retrieves a list of deployment stages. \n[Command Reference](listDeployStages)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--deploy-pipeline-id', help=u"""The ID of the parent pipeline.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only deployment stages that matches the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeployStageCollection'})
@cli_util.wrap_exceptions
def list_deploy_stages(ctx, from_json, all_pages, page_size, id, deploy_pipeline_id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if deploy_pipeline_id is not None:
        kwargs['deploy_pipeline_id'] = deploy_pipeline_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deploy_stages,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deploy_stages,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_deploy_stages(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@deployment_summary_group.command(name=cli_util.override('devops.list_deployments.command_name', 'list-deployments'), help=u"""Returns a list of deployments. \n[Command Reference](listDeployments)""")
@cli_util.option('--deploy-pipeline-id', help=u"""The ID of the parent pipeline.""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only Deployments that matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""Search for DevOps resources that were created before a specific date. Specifying this parameter corresponding to `timeCreatedLessThan` parameter will retrieve all assessments created before the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC3339].""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""Search for DevOps resources that were created after a specific date. Specifying this parameter corresponding to `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all security assessments created after the specified created date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as defined by [RFC3339].""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DeploymentCollection'})
@cli_util.wrap_exceptions
def list_deployments(ctx, from_json, all_pages, page_size, deploy_pipeline_id, id, compartment_id, project_id, lifecycle_state, display_name, limit, page, sort_order, sort_by, time_created_less_than, time_created_greater_than_or_equal_to):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if deploy_pipeline_id is not None:
        kwargs['deploy_pipeline_id'] = deploy_pipeline_id
    if id is not None:
        kwargs['id'] = id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
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
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_deployments,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_deployments,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_deployments(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_summary_group.command(name=cli_util.override('devops.list_projects.command_name', 'list-projects'), help=u"""Returns a list of projects. \n[Command Reference](listProjects)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only Projects that matches the given lifecycleState.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'ProjectCollection'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, compartment_id, id, lifecycle_state, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_projects,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_projects,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_projects(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('devops.list_work_request_errors.command_name', 'list'), help=u"""Returns a list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('devops.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
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


@work_request_group.command(name=cli_util.override('devops.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources where the lifecycle state matches the given operation status.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order can be provided. Default sort order is descending and is based on the timeAccepted field.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
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
    client = cli_util.build_client('devops', 'devops', ctx)
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


@deploy_artifact_group.command(name=cli_util.override('devops.update_deploy_artifact.command_name', 'update'), help=u"""Updates the deployment artifact. \n[Command Reference](updateDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-artifact-type', help=u"""Type of the deployment artifact.""")
@cli_util.option('--deploy-artifact-source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--argument-substitution-mode', help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-artifact-source': {'module': 'devops', 'class': 'DeployArtifactSource'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-artifact-source': {'module': 'devops', 'class': 'DeployArtifactSource'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, description, display_name, deploy_artifact_type, deploy_artifact_source, argument_substitution_mode, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')
    if not force:
        if deploy_artifact_source or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to deploy-artifact-source and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_artifact_type is not None:
        _details['deployArtifactType'] = deploy_artifact_type

    if deploy_artifact_source is not None:
        _details['deployArtifactSource'] = cli_util.parse_json_parameter("deploy_artifact_source", deploy_artifact_source)

    if argument_substitution_mode is not None:
        _details['argumentSubstitutionMode'] = argument_substitution_mode

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
        update_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.update_deploy_artifact_generic_deploy_artifact_source.command_name', 'update-deploy-artifact-generic-deploy-artifact-source'), help=u"""Updates the deployment artifact. \n[Command Reference](updateDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--deploy-artifact-source-repository-id', required=True, help=u"""The OCID of a repository""")
@cli_util.option('--deploy-artifact-source-deploy-artifact-path', required=True, help=u"""Specifies the artifact path in the repository.""")
@cli_util.option('--deploy-artifact-source-deploy-artifact-version', required=True, help=u"""Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-artifact-type', help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_generic_deploy_artifact_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, deploy_artifact_source_repository_id, deploy_artifact_source_deploy_artifact_path, deploy_artifact_source_deploy_artifact_version, description, display_name, deploy_artifact_type, argument_substitution_mode, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactSource']['repositoryId'] = deploy_artifact_source_repository_id
    _details['deployArtifactSource']['deployArtifactPath'] = deploy_artifact_source_deploy_artifact_path
    _details['deployArtifactSource']['deployArtifactVersion'] = deploy_artifact_source_deploy_artifact_version

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_artifact_type is not None:
        _details['deployArtifactType'] = deploy_artifact_type

    if argument_substitution_mode is not None:
        _details['argumentSubstitutionMode'] = argument_substitution_mode

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'GENERIC_ARTIFACT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
        update_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.update_deploy_artifact_ocir_deploy_artifact_source.command_name', 'update-deploy-artifact-ocir-deploy-artifact-source'), help=u"""Updates the deployment artifact. \n[Command Reference](updateDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--deploy-artifact-source-image-uri', required=True, help=u"""Specifies OCIR Image Path - optionally include tag.""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-artifact-type', help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--deploy-artifact-source-image-digest', help=u"""Specifies image digest for the version of the image.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_ocir_deploy_artifact_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, deploy_artifact_source_image_uri, description, display_name, deploy_artifact_type, argument_substitution_mode, freeform_tags, defined_tags, if_match, deploy_artifact_source_image_digest):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactSource']['imageUri'] = deploy_artifact_source_image_uri

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_artifact_type is not None:
        _details['deployArtifactType'] = deploy_artifact_type

    if argument_substitution_mode is not None:
        _details['argumentSubstitutionMode'] = argument_substitution_mode

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_artifact_source_image_digest is not None:
        _details['deployArtifactSource']['imageDigest'] = deploy_artifact_source_image_digest

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'OCIR'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
        update_deploy_artifact_details=_details,
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


@deploy_artifact_group.command(name=cli_util.override('devops.update_deploy_artifact_inline_deploy_artifact_source.command_name', 'update-deploy-artifact-inline-deploy-artifact-source'), help=u"""Updates the deployment artifact. \n[Command Reference](updateDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--deploy-artifact-source-base64-encoded-content', required=True, help=u"""base64 Encoded String""")
@cli_util.option('--description', help=u"""Optional description about the deployment artifact.""")
@cli_util.option('--display-name', help=u"""Deployment artifact display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-artifact-type', help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployArtifact'})
@cli_util.wrap_exceptions
def update_deploy_artifact_inline_deploy_artifact_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, deploy_artifact_source_base64_encoded_content, description, display_name, deploy_artifact_type, argument_substitution_mode, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_artifact_id, six.string_types) and len(deploy_artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-artifact-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactSource']['base64EncodedContent'] = deploy_artifact_source_base64_encoded_content

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_artifact_type is not None:
        _details['deployArtifactType'] = deploy_artifact_type

    if argument_substitution_mode is not None:
        _details['argumentSubstitutionMode'] = argument_substitution_mode

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'INLINE'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_artifact(
        deploy_artifact_id=deploy_artifact_id,
        update_deploy_artifact_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.update_deploy_environment.command_name', 'update'), help=u"""Updates the deployment environment. \n[Command Reference](updateDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--deploy-environment-type', required=True, help=u"""Deployment environment type.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, deploy_environment_type, description, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployEnvironmentType'] = deploy_environment_type

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_environment(
        deploy_environment_id=deploy_environment_id,
        update_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.update_deploy_environment_update_function_deploy_environment_details.command_name', 'update-deploy-environment-update-function-deploy-environment-details'), help=u"""Updates the deployment environment. \n[Command Reference](updateDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-id', help=u"""The OCID of the Function.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_function_deploy_environment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, description, display_name, freeform_tags, defined_tags, function_id, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if function_id is not None:
        _details['functionId'] = function_id

    _details['deployEnvironmentType'] = 'FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_environment(
        deploy_environment_id=deploy_environment_id,
        update_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.update_deploy_environment_update_compute_instance_group_deploy_environment_details.command_name', 'update-deploy-environment-update-compute-instance-group-deploy-environment-details'), help=u"""Updates the deployment environment. \n[Command Reference](updateDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-selectors', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'compute-instance-group-selectors': {'module': 'devops', 'class': 'ComputeInstanceGroupSelectorCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'compute-instance-group-selectors': {'module': 'devops', 'class': 'ComputeInstanceGroupSelectorCollection'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_compute_instance_group_deploy_environment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, description, display_name, freeform_tags, defined_tags, compute_instance_group_selectors, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or compute_instance_group_selectors:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and compute-instance-group-selectors will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if compute_instance_group_selectors is not None:
        _details['computeInstanceGroupSelectors'] = cli_util.parse_json_parameter("compute_instance_group_selectors", compute_instance_group_selectors)

    _details['deployEnvironmentType'] = 'COMPUTE_INSTANCE_GROUP'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_environment(
        deploy_environment_id=deploy_environment_id,
        update_deploy_environment_details=_details,
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


@deploy_environment_group.command(name=cli_util.override('devops.update_deploy_environment_update_oke_cluster_deploy_environment_details.command_name', 'update-deploy-environment-update-oke-cluster-deploy-environment-details'), help=u"""Updates the deployment environment. \n[Command Reference](updateDeployEnvironment)""")
@cli_util.option('--deploy-environment-id', required=True, help=u"""Unique environment identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment environment.""")
@cli_util.option('--display-name', help=u"""Deployment environment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--cluster-id', help=u"""The OCID of the Kubernetes cluster.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_oke_cluster_deploy_environment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, description, display_name, freeform_tags, defined_tags, cluster_id, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if cluster_id is not None:
        _details['clusterId'] = cluster_id

    _details['deployEnvironmentType'] = 'OKE_CLUSTER'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_environment(
        deploy_environment_id=deploy_environment_id,
        update_deploy_environment_details=_details,
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


@deploy_pipeline_group.command(name=cli_util.override('devops.update_deploy_pipeline.command_name', 'update'), help=u"""Updates the deployment pipeline. \n[Command Reference](updateDeployPipeline)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""Unique pipeline identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deloyment pipeline.""")
@cli_util.option('--display-name', help=u"""Deloyment pipeline display name. Avoid entering confidential information.""")
@cli_util.option('--deploy-pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-pipeline-parameters': {'module': 'devops', 'class': 'DeployPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployPipeline'})
@cli_util.wrap_exceptions
def update_deploy_pipeline(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, description, display_name, deploy_pipeline_parameters, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_pipeline_id, six.string_types) and len(deploy_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-pipeline-id cannot be whitespace or empty string')
    if not force:
        if deploy_pipeline_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to deploy-pipeline-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_pipeline_parameters is not None:
        _details['deployPipelineParameters'] = cli_util.parse_json_parameter("deploy_pipeline_parameters", deploy_pipeline_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_pipeline(
        deploy_pipeline_id=deploy_pipeline_id,
        update_deploy_pipeline_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage.command_name', 'update'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--deploy-stage-type', required=True, help=u"""Deployment stage type.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, deploy_stage_type, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployStageType'] = deploy_stage_type

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--namespace', help=u"""Default namespace to be used for Kubernetes deployment when not specified in the manifest.""")
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, oke_cluster_deploy_environment_id, kubernetes_manifest_deploy_artifact_ids, namespace, rollback_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or kubernetes_manifest_deploy_artifact_ids or rollback_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and kubernetes-manifest-deploy-artifact-ids and rollback-policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if oke_cluster_deploy_environment_id is not None:
        _details['okeClusterDeployEnvironmentId'] = oke_cluster_deploy_environment_id

    if kubernetes_manifest_deploy_artifact_ids is not None:
        _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)

    if namespace is not None:
        _details['namespace'] = namespace

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'OKE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details.command_name', 'update-deploy-stage-update-load-balancer-traffic-shift-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--blue-backend-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--green-backend-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--traffic-shift-target', help=u"""Specifies the target or destination backend set.""")
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'blue-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'green-backend-ips': {'module': 'devops', 'class': 'BackendSetIpCollection'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_load_balancer_traffic_shift_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, blue_backend_ips, green_backend_ips, traffic_shift_target, rollout_policy, load_balancer_config, rollback_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or blue_backend_ips or green_backend_ips or rollout_policy or load_balancer_config or rollback_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and blue-backend-ips and green-backend-ips and rollout-policy and load-balancer-config and rollback-policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if blue_backend_ips is not None:
        _details['blueBackendIps'] = cli_util.parse_json_parameter("blue_backend_ips", blue_backend_ips)

    if green_backend_ips is not None:
        _details['greenBackendIps'] = cli_util.parse_json_parameter("green_backend_ips", green_backend_ips)

    if traffic_shift_target is not None:
        _details['trafficShiftTarget'] = traffic_shift_target

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if load_balancer_config is not None:
        _details['loadBalancerConfig'] = cli_util.parse_json_parameter("load_balancer_config", load_balancer_config)

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'LOAD_BALANCER_TRAFFIC_SHIFT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-deploy-environment-id', help=u"""A compute instance group environment OCID for rolling deployment.""")
@cli_util.option('--deployment-spec-deploy-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Additional file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--failure-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, compute_instance_group_deploy_environment_id, deployment_spec_deploy_artifact_id, deploy_artifact_ids, rollout_policy, rollback_policy, failure_policy, load_balancer_config, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or deploy_artifact_ids or rollout_policy or rollback_policy or failure_policy or load_balancer_config:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and deploy-artifact-ids and rollout-policy and rollback-policy and failure-policy and load-balancer-config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if compute_instance_group_deploy_environment_id is not None:
        _details['computeInstanceGroupDeployEnvironmentId'] = compute_instance_group_deploy_environment_id

    if deployment_spec_deploy_artifact_id is not None:
        _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id

    if deploy_artifact_ids is not None:
        _details['deployArtifactIds'] = cli_util.parse_json_parameter("deploy_artifact_ids", deploy_artifact_ids)

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    if failure_policy is not None:
        _details['failurePolicy'] = cli_util.parse_json_parameter("failure_policy", failure_policy)

    if load_balancer_config is not None:
        _details['loadBalancerConfig'] = cli_util.parse_json_parameter("load_balancer_config", load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_wait_deploy_stage_details.command_name', 'update-deploy-stage-update-wait-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-criteria', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'WaitCriteria'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_wait_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, wait_criteria, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or wait_criteria:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and wait-criteria will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if wait_criteria is not None:
        _details['waitCriteria'] = cli_util.parse_json_parameter("wait_criteria", wait_criteria)

    _details['deployStageType'] = 'WAIT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_manual_approval_deploy_stage_details.command_name', 'update-deploy-stage-update-manual-approval-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--approval-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'approval-policy': {'module': 'devops', 'class': 'ApprovalPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_manual_approval_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, approval_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or approval_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and approval-policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if approval_policy is not None:
        _details['approvalPolicy'] = cli_util.parse_json_parameter("approval_policy", approval_policy)

    _details['deployStageType'] = 'MANUAL_APPROVAL'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_function_deploy_stage_details.command_name', 'update-deploy-stage-update-function-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-deploy-environment-id', help=u"""Function environment OCID.""")
@cli_util.option('--docker-image-deploy-artifact-id', help=u"""A Docker image artifact OCID.""")
@cli_util.option('--config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""User provided key and value pair configuration, which is assigned through constants or parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-memory-in-mbs', type=click.INT, help=u"""Maximum usable memory for the Function (in MB).""")
@cli_util.option('--function-timeout-in-seconds', type=click.INT, help=u"""Timeout for execution of the Function. Value in seconds.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'config': {'module': 'devops', 'class': 'dict(str, string)'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_function_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, function_deploy_environment_id, docker_image_deploy_artifact_id, config, max_memory_in_mbs, function_timeout_in_seconds, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or config:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and config will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if function_deploy_environment_id is not None:
        _details['functionDeployEnvironmentId'] = function_deploy_environment_id

    if docker_image_deploy_artifact_id is not None:
        _details['dockerImageDeployArtifactId'] = docker_image_deploy_artifact_id

    if config is not None:
        _details['config'] = cli_util.parse_json_parameter("config", config)

    if max_memory_in_mbs is not None:
        _details['maxMemoryInMBs'] = max_memory_in_mbs

    if function_timeout_in_seconds is not None:
        _details['functionTimeoutInSeconds'] = function_timeout_in_seconds

    _details['deployStageType'] = 'DEPLOY_FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_invoke_function_deploy_stage_details.command_name', 'update-deploy-stage-update-invoke-function-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--function-deploy-environment-id', help=u"""Function environment OCID.""")
@cli_util.option('--deploy-artifact-id', help=u"""Optional binary artifact OCID user may provide to this stage.""")
@cli_util.option('--is-async', type=click.BOOL, help=u"""A boolean flag specifies whether this stage executes asynchronously.""")
@cli_util.option('--is-validation-enabled', type=click.BOOL, help=u"""A boolean flag specifies whether the invoked function must be validated.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_invoke_function_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, function_deploy_environment_id, deploy_artifact_id, is_async, is_validation_enabled, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if deploy_stage_predecessor_collection is not None:
        _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if function_deploy_environment_id is not None:
        _details['functionDeployEnvironmentId'] = function_deploy_environment_id

    if deploy_artifact_id is not None:
        _details['deployArtifactId'] = deploy_artifact_id

    if is_async is not None:
        _details['isAsync'] = is_async

    if is_validation_enabled is not None:
        _details['isValidationEnabled'] = is_validation_enabled

    _details['deployStageType'] = 'INVOKE_FUNCTION'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deploy_stage(
        deploy_stage_id=deploy_stage_id,
        update_deploy_stage_details=_details,
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


@deployment_group.command(name=cli_util.override('devops.update_deployment.command_name', 'update'), help=u"""Updates the deployment. \n[Command Reference](updateDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--deployment-type', required=True, help=u"""Specifies type for this deployment.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def update_deployment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, deployment_type, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deploymentType'] = deployment_type

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deployment(
        deployment_id=deployment_id,
        update_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.update_deployment_update_single_deploy_stage_deployment_details.command_name', 'update-deployment-update-single-deploy-stage-deployment-details'), help=u"""Updates the deployment. \n[Command Reference](updateDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def update_deployment_update_single_deploy_stage_deployment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')
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

    _details['deploymentType'] = 'SINGLE_STAGE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deployment(
        deployment_id=deployment_id,
        update_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.update_deployment_update_deploy_pipeline_redeployment_details.command_name', 'update-deployment-update-deploy-pipeline-redeployment-details'), help=u"""Updates the deployment. \n[Command Reference](updateDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def update_deployment_update_deploy_pipeline_redeployment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')
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

    _details['deploymentType'] = 'PIPELINE_REDEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deployment(
        deployment_id=deployment_id,
        update_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@deployment_group.command(name=cli_util.override('devops.update_deployment_update_deploy_pipeline_deployment_details.command_name', 'update-deployment-update-deploy-pipeline-deployment-details'), help=u"""Updates the deployment. \n[Command Reference](updateDeployment)""")
@cli_util.option('--deployment-id', required=True, help=u"""Unique deployment identifier.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def update_deployment_update_deploy_pipeline_deployment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(deployment_id, six.string_types) and len(deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --deployment-id cannot be whitespace or empty string')
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

    _details['deploymentType'] = 'PIPELINE_DEPLOYMENT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_deployment(
        deployment_id=deployment_id,
        update_deployment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_deployment') and callable(getattr(client, 'get_deployment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_deployment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@project_group.command(name=cli_util.override('devops.update_project.command_name', 'update'), help=u"""Updates the project. \n[Command Reference](updateProject)""")
@cli_util.option('--project-id', required=True, help=u"""Unique project identifier.""")
@cli_util.option('--description', help=u"""Project description.""")
@cli_util.option('--notification-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'notification-config': {'module': 'devops', 'class': 'NotificationConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'notification-config': {'module': 'devops', 'class': 'NotificationConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Project'})
@cli_util.wrap_exceptions
def update_project(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, description, notification_config, freeform_tags, defined_tags, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')
    if not force:
        if notification_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to notification-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if notification_config is not None:
        _details['notificationConfig'] = cli_util.parse_json_parameter("notification_config", notification_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_project(
        project_id=project_id,
        update_project_details=_details,
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
