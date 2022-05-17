# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('devops.devops_root_group.command_name', 'devops'), cls=CommandGroupWithAlias, help=cli_util.override('devops.devops_root_group.help', """Use the DevOps API to create DevOps projects, configure code repositories,  add artifacts to deploy, build and test software applications, configure  target deployment environments, and deploy software applications.  For more information, see [DevOps]."""), short_help=cli_util.override('devops.devops_root_group.short_help', """DevOps API"""))
@cli_util.help_option_group
def devops_root_group():
    pass


@click.command(cli_util.override('devops.build_pipeline_collection_group.command_name', 'build-pipeline-collection'), cls=CommandGroupWithAlias, help="""Results of a pipeline search.""")
@cli_util.help_option_group
def build_pipeline_collection_group():
    pass


@click.command(cli_util.override('devops.deploy_artifact_summary_group.command_name', 'deploy-artifact-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment artifact.""")
@cli_util.help_option_group
def deploy_artifact_summary_group():
    pass


@click.command(cli_util.override('devops.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""DevOps project groups resources needed to implement the CI/CD workload. DevOps resources include artifacts, pipelines, and environments.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('devops.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Details of the work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('devops.repository_group.command_name', 'repository'), cls=CommandGroupWithAlias, help="""Repositories containing the source code to build and deploy.""")
@cli_util.help_option_group
def repository_group():
    pass


@click.command(cli_util.override('devops.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('devops.deploy_stage_summary_group.command_name', 'deploy-stage-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment stage.""")
@cli_util.help_option_group
def deploy_stage_summary_group():
    pass


@click.command(cli_util.override('devops.build_pipeline_group.command_name', 'build-pipeline'), cls=CommandGroupWithAlias, help="""A set of stages forming a directed acyclic graph that defines the build process.""")
@cli_util.help_option_group
def build_pipeline_group():
    pass


@click.command(cli_util.override('devops.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""The properties that define a connection to external repositories.""")
@cli_util.help_option_group
def connection_group():
    pass


@click.command(cli_util.override('devops.project_summary_group.command_name', 'project-summary'), cls=CommandGroupWithAlias, help="""Summary of the project.""")
@cli_util.help_option_group
def project_summary_group():
    pass


@click.command(cli_util.override('devops.repository_path_summary_group.command_name', 'repository-path-summary'), cls=CommandGroupWithAlias, help="""Object containing information about files and directories in a repository.""")
@cli_util.help_option_group
def repository_path_summary_group():
    pass


@click.command(cli_util.override('devops.connection_collection_group.command_name', 'connection-collection'), cls=CommandGroupWithAlias, help="""Collection of connections.""")
@cli_util.help_option_group
def connection_collection_group():
    pass


@click.command(cli_util.override('devops.deploy_stage_group.command_name', 'deploy-stage'), cls=CommandGroupWithAlias, help="""A single node in a pipeline. It is usually associated with some action on a specific set of OCI resources such as environments. For example, updating a Function or a Kubernetes cluster.""")
@cli_util.help_option_group
def deploy_stage_group():
    pass


@click.command(cli_util.override('devops.deployment_group.command_name', 'deployment'), cls=CommandGroupWithAlias, help="""A single execution or run of a pipeline.""")
@cli_util.help_option_group
def deployment_group():
    pass


@click.command(cli_util.override('devops.build_run_summary_group.command_name', 'build-run-summary'), cls=CommandGroupWithAlias, help="""Summary of the build run.""")
@cli_util.help_option_group
def build_run_summary_group():
    pass


@click.command(cli_util.override('devops.deploy_pipeline_group.command_name', 'deploy-pipeline'), cls=CommandGroupWithAlias, help="""A set of stages whose predecessor relation forms a directed acyclic graph.""")
@cli_util.help_option_group
def deploy_pipeline_group():
    pass


@click.command(cli_util.override('devops.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('devops.deploy_artifact_group.command_name', 'deploy-artifact'), cls=CommandGroupWithAlias, help="""Artifacts are deployment manifests that are referenced in a pipeline stage for automated deployment to the target environment.  DevOps artifacts can be an OCI Container image repository, Kubernetes manifest, an Artifact Registry artifact, or defined inline.""")
@cli_util.help_option_group
def deploy_artifact_group():
    pass


@click.command(cli_util.override('devops.trigger_group.command_name', 'trigger'), cls=CommandGroupWithAlias, help="""Trigger the deployment pipeline to deploy the artifact.""")
@cli_util.help_option_group
def trigger_group():
    pass


@click.command(cli_util.override('devops.deployment_summary_group.command_name', 'deployment-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment.""")
@cli_util.help_option_group
def deployment_summary_group():
    pass


@click.command(cli_util.override('devops.repository_commit_group.command_name', 'repository-commit'), cls=CommandGroupWithAlias, help="""Commit object with commit information.""")
@cli_util.help_option_group
def repository_commit_group():
    pass


@click.command(cli_util.override('devops.build_pipeline_stage_group.command_name', 'build-pipeline-stage'), cls=CommandGroupWithAlias, help="""A single node in a build pipeline. A stage takes a specific designated action. There are many types of stages such as 'BUILD' and 'DELIVER_ARTIFACT'.""")
@cli_util.help_option_group
def build_pipeline_stage_group():
    pass


@click.command(cli_util.override('devops.repository_object_group.command_name', 'repository-object'), cls=CommandGroupWithAlias, help="""Object containing information about files and directories in a repository.""")
@cli_util.help_option_group
def repository_object_group():
    pass


@click.command(cli_util.override('devops.deploy_environment_group.command_name', 'deploy-environment'), cls=CommandGroupWithAlias, help="""The target OCI resources, such as Compute instances, Container Engine for Kubernetes(OKE) clusters, or Function, where artifacts are deployed.""")
@cli_util.help_option_group
def deploy_environment_group():
    pass


@click.command(cli_util.override('devops.build_run_group.command_name', 'build-run'), cls=CommandGroupWithAlias, help="""Each time you attempt to run a build pipeline you create one build run. A build can be running currently, or it can be a record of the run that happened in the past. The set of build runs constitutes a build pipeline's history.""")
@cli_util.help_option_group
def build_run_group():
    pass


@click.command(cli_util.override('devops.deploy_environment_summary_group.command_name', 'deploy-environment-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment environment.""")
@cli_util.help_option_group
def deploy_environment_summary_group():
    pass


@click.command(cli_util.override('devops.trigger_collection_group.command_name', 'trigger-collection'), cls=CommandGroupWithAlias, help="""Results of a trigger search. Contains boh trigger summary items and other information such as metadata.""")
@cli_util.help_option_group
def trigger_collection_group():
    pass


@click.command(cli_util.override('devops.deploy_pipeline_summary_group.command_name', 'deploy-pipeline-summary'), cls=CommandGroupWithAlias, help="""Summary of the deployment pipeline.""")
@cli_util.help_option_group
def deploy_pipeline_summary_group():
    pass


@click.command(cli_util.override('devops.build_pipeline_stage_summary_group.command_name', 'build-pipeline-stage-summary'), cls=CommandGroupWithAlias, help="""Summary of the Stage.""")
@cli_util.help_option_group
def build_pipeline_stage_summary_group():
    pass


@click.command(cli_util.override('devops.repository_ref_group.command_name', 'repository-ref'), cls=CommandGroupWithAlias, help="""Reference object with name and commit ID.""")
@cli_util.help_option_group
def repository_ref_group():
    pass


devops_root_group.add_command(build_pipeline_collection_group)
devops_root_group.add_command(deploy_artifact_summary_group)
devops_root_group.add_command(project_group)
devops_root_group.add_command(work_request_group)
devops_root_group.add_command(repository_group)
devops_root_group.add_command(work_request_error_group)
devops_root_group.add_command(deploy_stage_summary_group)
devops_root_group.add_command(build_pipeline_group)
devops_root_group.add_command(connection_group)
devops_root_group.add_command(project_summary_group)
devops_root_group.add_command(repository_path_summary_group)
devops_root_group.add_command(connection_collection_group)
devops_root_group.add_command(deploy_stage_group)
devops_root_group.add_command(deployment_group)
devops_root_group.add_command(build_run_summary_group)
devops_root_group.add_command(deploy_pipeline_group)
devops_root_group.add_command(work_request_log_entry_group)
devops_root_group.add_command(deploy_artifact_group)
devops_root_group.add_command(trigger_group)
devops_root_group.add_command(deployment_summary_group)
devops_root_group.add_command(repository_commit_group)
devops_root_group.add_command(build_pipeline_stage_group)
devops_root_group.add_command(repository_object_group)
devops_root_group.add_command(deploy_environment_group)
devops_root_group.add_command(build_run_group)
devops_root_group.add_command(deploy_environment_summary_group)
devops_root_group.add_command(trigger_collection_group)
devops_root_group.add_command(deploy_pipeline_summary_group)
devops_root_group.add_command(build_pipeline_stage_summary_group)
devops_root_group.add_command(repository_ref_group)


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


@build_run_group.command(name=cli_util.override('devops.cancel_build_run.command_name', 'cancel'), help=u"""Cancels the build run based on the build run ID provided in the request. \n[Command Reference](cancelBuildRun)""")
@cli_util.option('--reason', required=True, help=u"""The reason for canceling the build run.""")
@cli_util.option('--build-run-id', required=True, help=u"""Unique build run identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildRun'})
@cli_util.wrap_exceptions
def cancel_build_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, reason, build_run_id, if_match):

    if isinstance(build_run_id, six.string_types) and len(build_run_id.strip()) == 0:
        raise click.UsageError('Parameter --build-run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['reason'] = reason

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.cancel_build_run(
        build_run_id=build_run_id,
        cancel_build_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_build_run') and callable(getattr(client, 'get_build_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_build_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@build_pipeline_group.command(name=cli_util.override('devops.create_build_pipeline.command_name', 'create'), help=u"""Creates a new build pipeline. \n[Command Reference](createBuildPipeline)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project.""")
@cli_util.option('--description', help=u"""Optional description about the build pipeline.""")
@cli_util.option('--display-name', help=u"""Build pipeline display name. Avoid entering confidential information.""")
@cli_util.option('--build-pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-parameters': {'module': 'devops', 'class': 'BuildPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-parameters': {'module': 'devops', 'class': 'BuildPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipeline'})
@cli_util.wrap_exceptions
def create_build_pipeline(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, description, display_name, build_pipeline_parameters, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if build_pipeline_parameters is not None:
        _details['buildPipelineParameters'] = cli_util.parse_json_parameter("build_pipeline_parameters", build_pipeline_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline(
        create_build_pipeline_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.create_build_pipeline_stage.command_name', 'create'), help=u"""Creates a new stage. \n[Command Reference](createBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-type', required=True, help=u"""Defines the stage type, which is one of the following: BUILD, DELIVER_ARTIFACT, WAIT, and TRIGGER_DEPLOYMENT_PIPELINE.""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the stage.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_type, build_pipeline_id, build_pipeline_stage_predecessor_collection, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineStageType'] = build_pipeline_stage_type
    _details['buildPipelineId'] = build_pipeline_id
    _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline_stage(
        create_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.create_build_pipeline_stage_create_deliver_artifact_stage_details.command_name', 'create-build-pipeline-stage-create-deliver-artifact-stage-details'), help=u"""Creates a new stage. \n[Command Reference](createBuildPipelineStage)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deliver-artifact-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the stage.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_deliver_artifact_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, build_pipeline_stage_predecessor_collection, deliver_artifact_collection, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineId'] = build_pipeline_id
    _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)
    _details['deliverArtifactCollection'] = cli_util.parse_json_parameter("deliver_artifact_collection", deliver_artifact_collection)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['buildPipelineStageType'] = 'DELIVER_ARTIFACT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline_stage(
        create_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.create_build_pipeline_stage_create_trigger_deployment_stage_details.command_name', 'create-build-pipeline-stage-create-trigger-deployment-stage-details'), help=u"""Creates a new stage. \n[Command Reference](createBuildPipelineStage)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""A target deployment pipeline OCID that will run in this stage.""")
@cli_util.option('--is-pass-all-parameters-enabled', required=True, type=click.BOOL, help=u"""A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the stage.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_trigger_deployment_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, build_pipeline_stage_predecessor_collection, deploy_pipeline_id, is_pass_all_parameters_enabled, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineId'] = build_pipeline_id
    _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['isPassAllParametersEnabled'] = is_pass_all_parameters_enabled

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['buildPipelineStageType'] = 'TRIGGER_DEPLOYMENT_PIPELINE'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline_stage(
        create_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.create_build_pipeline_stage_create_wait_stage_details.command_name', 'create-build-pipeline-stage-create-wait-stage-details'), help=u"""Creates a new stage. \n[Command Reference](createBuildPipelineStage)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-criteria', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the stage.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'CreateWaitCriteriaDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'CreateWaitCriteriaDetails'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_wait_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, build_pipeline_stage_predecessor_collection, wait_criteria, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineId'] = build_pipeline_id
    _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)
    _details['waitCriteria'] = cli_util.parse_json_parameter("wait_criteria", wait_criteria)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['buildPipelineStageType'] = 'WAIT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline_stage(
        create_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.create_build_pipeline_stage_create_build_stage_details.command_name', 'create-build-pipeline-stage-create-build-stage-details'), help=u"""Creates a new stage. \n[Command Reference](createBuildPipelineStage)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image', required=True, help=u"""Image name for the build environment""")
@cli_util.option('--build-source-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the stage.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--build-spec-file', help=u"""The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.""")
@cli_util.option('--stage-execution-timeout-in-seconds', type=click.INT, help=u"""Timeout for the build stage execution. Specify value in seconds.""")
@cli_util.option('--primary-build-source', help=u"""Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def create_build_pipeline_stage_create_build_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, build_pipeline_stage_predecessor_collection, image, build_source_collection, display_name, description, freeform_tags, defined_tags, build_spec_file, stage_execution_timeout_in_seconds, primary_build_source):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineId'] = build_pipeline_id
    _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)
    _details['image'] = image
    _details['buildSourceCollection'] = cli_util.parse_json_parameter("build_source_collection", build_source_collection)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if build_spec_file is not None:
        _details['buildSpecFile'] = build_spec_file

    if stage_execution_timeout_in_seconds is not None:
        _details['stageExecutionTimeoutInSeconds'] = stage_execution_timeout_in_seconds

    if primary_build_source is not None:
        _details['primaryBuildSource'] = primary_build_source

    _details['buildPipelineStageType'] = 'BUILD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_pipeline_stage(
        create_build_pipeline_stage_details=_details,
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


@build_run_group.command(name=cli_util.override('devops.create_build_run.command_name', 'create'), help=u"""Starts a build pipeline run for a predefined build pipeline. \n[Command Reference](createBuildRun)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""The OCID of the build pipeline.""")
@cli_util.option('--display-name', help=u"""Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--commit-info', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--build-run-arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'commit-info': {'module': 'devops', 'class': 'CommitInfo'}, 'build-run-arguments': {'module': 'devops', 'class': 'BuildRunArgumentCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'commit-info': {'module': 'devops', 'class': 'CommitInfo'}, 'build-run-arguments': {'module': 'devops', 'class': 'BuildRunArgumentCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildRun'})
@cli_util.wrap_exceptions
def create_build_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, display_name, commit_info, build_run_arguments, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineId'] = build_pipeline_id

    if display_name is not None:
        _details['displayName'] = display_name

    if commit_info is not None:
        _details['commitInfo'] = cli_util.parse_json_parameter("commit_info", commit_info)

    if build_run_arguments is not None:
        _details['buildRunArguments'] = cli_util.parse_json_parameter("build_run_arguments", build_run_arguments)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_build_run(
        create_build_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_build_run') and callable(getattr(client, 'get_build_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_build_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@connection_group.command(name=cli_util.override('devops.create_connection.command_name', 'create'), help=u"""Creates a new connection. \n[Command Reference](createConnection)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project.""")
@cli_util.option('--connection-type', required=True, help=u"""The type of connection.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, connection_type, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['connectionType'] = connection_type

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_connection(
        create_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.create_connection_create_github_access_token_connection_details.command_name', 'create-connection-create-github-access-token-connection-details'), help=u"""Creates a new connection. \n[Command Reference](createConnection)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project.""")
@cli_util.option('--access-token', required=True, help=u"""The OCID of personal access token saved in secret store.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_github_access_token_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, access_token, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['accessToken'] = access_token

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['connectionType'] = 'GITHUB_ACCESS_TOKEN'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_connection(
        create_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.create_connection_create_bitbucket_cloud_app_password_connection_details.command_name', 'create-connection-create-bitbucket-cloud-app-password-connection-details'), help=u"""Creates a new connection. \n[Command Reference](createConnection)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project.""")
@cli_util.option('--username', required=True, help=u"""Public Bitbucket Cloud Username in plain text(not more than 30 characters)""")
@cli_util.option('--app-password', required=True, help=u"""OCID of personal Bitbucket Cloud AppPassword saved in secret store""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_bitbucket_cloud_app_password_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, username, app_password, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['username'] = username
    _details['appPassword'] = app_password

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['connectionType'] = 'BITBUCKET_CLOUD_APP_PASSWORD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_connection(
        create_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.create_connection_create_gitlab_access_token_connection_details.command_name', 'create-connection-create-gitlab-access-token-connection-details'), help=u"""Creates a new connection. \n[Command Reference](createConnection)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project.""")
@cli_util.option('--access-token', required=True, help=u"""The OCID of personal access token saved in secret store.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_gitlab_access_token_connection_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, access_token, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['accessToken'] = access_token

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['connectionType'] = 'GITLAB_ACCESS_TOKEN'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_connection(
        create_connection_details=_details,
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
@cli_util.option('--deploy-artifact-source-repository-id', required=True, help=u"""The OCID of a repository.""")
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


@deploy_artifact_group.command(name=cli_util.override('devops.create_deploy_artifact_helm_repository_deploy_artifact_source.command_name', 'create-deploy-artifact-helm-repository-deploy-artifact-source'), help=u"""Creates a new deployment artifact. \n[Command Reference](createDeployArtifact)""")
@cli_util.option('--deploy-artifact-type', required=True, help=u"""Type of the deployment artifact.""")
@cli_util.option('--argument-substitution-mode', required=True, help=u"""Mode for artifact parameter substitution.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of a project.""")
@cli_util.option('--deploy-artifact-source-chart-url', required=True, help=u"""The URL of an OCIR repository.""")
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
def create_deploy_artifact_helm_repository_deploy_artifact_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_type, argument_substitution_mode, project_id, deploy_artifact_source_chart_url, deploy_artifact_source_deploy_artifact_version, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployArtifactSource'] = {}
    _details['deployArtifactType'] = deploy_artifact_type
    _details['argumentSubstitutionMode'] = argument_substitution_mode
    _details['projectId'] = project_id
    _details['deployArtifactSource']['chartUrl'] = deploy_artifact_source_chart_url
    _details['deployArtifactSource']['deployArtifactVersion'] = deploy_artifact_source_deploy_artifact_version

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'HELM_CHART'

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
@cli_util.option('--deploy-artifact-source-image-uri', required=True, help=u"""Specifies OCIR image path - optionally include tag.""")
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
@cli_util.option('--network-channel', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def create_deploy_environment_create_oke_cluster_deploy_environment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, cluster_id, description, display_name, freeform_tags, defined_tags, network_channel):

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

    if network_channel is not None:
        _details['networkChannel'] = cli_util.parse_json_parameter("network_channel", network_channel)

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-canary-traffic-shift-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-canary-deploy-stage-id', required=True, help=u"""The OCID of an upstream OKE canary deployment stage in this pipeline.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_canary_traffic_shift_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_canary_deploy_stage_id, rollout_policy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeCanaryDeployStageId'] = oke_canary_deploy_stage_id
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'OKE_CANARY_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-blue-green-traffic-shift-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-blue-green-deploy-stage-id', required=True, help=u"""The OCID of the upstream OKE blue-green deployment stage in this pipeline.""")
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
def create_deploy_stage_create_oke_blue_green_traffic_shift_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_blue_green_deploy_stage_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeBlueGreenDeployStageId'] = oke_blue_green_deploy_stage_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'OKE_BLUE_GREEN_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-canary-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-deploy-environment-id', required=True, help=u"""A compute instance group environment OCID for Canary deployment.""")
@cli_util.option('--deployment-spec-deploy-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--production-load-balancer-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_canary_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, compute_instance_group_deploy_environment_id, deployment_spec_deploy_artifact_id, rollout_policy, production_load_balancer_config, description, display_name, freeform_tags, defined_tags, deploy_artifact_ids, test_load_balancer_config):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['computeInstanceGroupDeployEnvironmentId'] = compute_instance_group_deploy_environment_id
    _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)
    _details['productionLoadBalancerConfig'] = cli_util.parse_json_parameter("production_load_balancer_config", production_load_balancer_config)

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

    if test_load_balancer_config is not None:
        _details['testLoadBalancerConfig'] = cli_util.parse_json_parameter("test_load_balancer_config", test_load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-blue-green-traffic-shift-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-blue-green-deployment-deploy-stage-id', required=True, help=u"""The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.""")
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
def create_deploy_stage_create_compute_instance_group_blue_green_traffic_shift_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, compute_instance_group_blue_green_deployment_deploy_stage_id, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['computeInstanceGroupBlueGreenDeploymentDeployStageId'] = compute_instance_group_blue_green_deployment_deploy_stage_id

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_blue_green_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-blue-green-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--blue-green-strategy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'blue-green-strategy': {'module': 'devops', 'class': 'OkeBlueGreenStrategy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'blue-green-strategy': {'module': 'devops', 'class': 'OkeBlueGreenStrategy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_blue_green_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_cluster_deploy_environment_id, kubernetes_manifest_deploy_artifact_ids, blue_green_strategy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeClusterDeployEnvironmentId'] = oke_cluster_deploy_environment_id
    _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)
    _details['blueGreenStrategy'] = cli_util.parse_json_parameter("blue_green_strategy", blue_green_strategy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'OKE_BLUE_GREEN_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_canary_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-canary-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--canary-strategy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'canary-strategy': {'module': 'devops', 'class': 'OkeCanaryStrategy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'canary-strategy': {'module': 'devops', 'class': 'OkeCanaryStrategy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_canary_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_cluster_deploy_environment_id, kubernetes_manifest_deploy_artifact_ids, canary_strategy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeClusterDeployEnvironmentId'] = oke_cluster_deploy_environment_id
    _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)
    _details['canaryStrategy'] = cli_util.parse_json_parameter("canary_strategy", canary_strategy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'OKE_CANARY_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-canary-traffic-shift-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-canary-deploy-stage-id', required=True, help=u"""A compute instance group canary stage OCID for load balancer.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_canary_traffic_shift_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, compute_instance_group_canary_deploy_stage_id, rollout_policy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['computeInstanceGroupCanaryDeployStageId'] = compute_instance_group_canary_deploy_stage_id
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-canary-approval-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compute-instance-group-canary-traffic-shift-deploy-stage-id', required=True, help=u"""A compute instance group canary traffic shift stage OCID for load balancer.""")
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
def create_deploy_stage_create_compute_instance_group_canary_approval_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, compute_instance_group_canary_traffic_shift_deploy_stage_id, approval_policy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['computeInstanceGroupCanaryTrafficShiftDeployStageId'] = compute_instance_group_canary_traffic_shift_deploy_stage_id
    _details['approvalPolicy'] = cli_util.parse_json_parameter("approval_policy", approval_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_helm_chart_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-helm-chart-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--helm-chart-deploy-artifact-id', required=True, help=u"""Helm chart artifact OCID.""")
@cli_util.option('--release-name', required=True, help=u"""Default name of the chart instance. Must be unique within a Kubernetes namespace.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--values-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of values.yaml file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--namespace', help=u"""Default namespace to be used for Kubernetes deployment when not specified in the manifest.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Time to wait for execution of a helm stage. Defaults to 300 seconds.""")
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_oke_helm_chart_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_cluster_deploy_environment_id, helm_chart_deploy_artifact_id, release_name, description, display_name, freeform_tags, defined_tags, values_artifact_ids, namespace, timeout_in_seconds, rollback_policy):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeClusterDeployEnvironmentId'] = oke_cluster_deploy_environment_id
    _details['helmChartDeployArtifactId'] = helm_chart_deploy_artifact_id
    _details['releaseName'] = release_name

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if values_artifact_ids is not None:
        _details['valuesArtifactIds'] = cli_util.parse_json_parameter("values_artifact_ids", values_artifact_ids)

    if namespace is not None:
        _details['namespace'] = namespace

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'OKE_HELM_CHART_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', required=True, help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details.command_name', 'create-deploy-stage-create-compute-instance-group-blue-green-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-environment-id-a', required=True, help=u"""First compute instance group environment OCID for deployment.""")
@cli_util.option('--deploy-environment-id-b', required=True, help=u"""Second compute instance group environment OCID for deployment.""")
@cli_util.option('--deployment-spec-deploy-artifact-id', required=True, help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--rollout-policy', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--production-load-balancer-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--failure-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}, 'production-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def create_deploy_stage_create_compute_instance_group_blue_green_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, deploy_environment_id_a, deploy_environment_id_b, deployment_spec_deploy_artifact_id, rollout_policy, production_load_balancer_config, description, display_name, freeform_tags, defined_tags, deploy_artifact_ids, failure_policy, test_load_balancer_config):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['deployEnvironmentIdA'] = deploy_environment_id_a
    _details['deployEnvironmentIdB'] = deploy_environment_id_b
    _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id
    _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)
    _details['productionLoadBalancerConfig'] = cli_util.parse_json_parameter("production_load_balancer_config", production_load_balancer_config)

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

    if failure_policy is not None:
        _details['failurePolicy'] = cli_util.parse_json_parameter("failure_policy", failure_policy)

    if test_load_balancer_config is not None:
        _details['testLoadBalancerConfig'] = cli_util.parse_json_parameter("test_load_balancer_config", test_load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.create_deploy_stage_create_oke_canary_approval_deploy_stage_details.command_name', 'create-deploy-stage-create-oke-canary-approval-deploy-stage-details'), help=u"""Creates a new deployment stage. \n[Command Reference](createDeployStage)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--deploy-stage-predecessor-collection', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-canary-traffic-shift-deploy-stage-id', required=True, help=u"""The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.""")
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
def create_deploy_stage_create_oke_canary_approval_deploy_stage_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, deploy_stage_predecessor_collection, oke_canary_traffic_shift_deploy_stage_id, approval_policy, description, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['deployPipelineId'] = deploy_pipeline_id
    _details['deployStagePredecessorCollection'] = cli_util.parse_json_parameter("deploy_stage_predecessor_collection", deploy_stage_predecessor_collection)
    _details['okeCanaryTrafficShiftDeployStageId'] = oke_canary_traffic_shift_deploy_stage_id
    _details['approvalPolicy'] = cli_util.parse_json_parameter("approval_policy", approval_policy)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['deployStageType'] = 'OKE_CANARY_APPROVAL'

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


@deployment_group.command(name=cli_util.override('devops.create_deployment_create_single_deploy_stage_redeployment_details.command_name', 'create-deployment-create-single-deploy-stage-redeployment-details'), help=u"""Creates a new deployment. \n[Command Reference](createDeployment)""")
@cli_util.option('--deploy-pipeline-id', required=True, help=u"""The OCID of a pipeline.""")
@cli_util.option('--display-name', help=u"""Deployment display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--previous-deployment-id', help=u"""Specifies the OCID of the previous deployment to be redeployed.""")
@cli_util.option('--deploy-stage-id', help=u"""Specifies the OCID of the stage to be redeployed.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_create_single_deploy_stage_redeployment_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_pipeline_id, display_name, freeform_tags, defined_tags, previous_deployment_id, deploy_stage_id):

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

    if deploy_stage_id is not None:
        _details['deployStageId'] = deploy_stage_id

    _details['deploymentType'] = 'SINGLE_STAGE_REDEPLOYMENT'

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


@repository_group.command(name=cli_util.override('devops.create_repository.command_name', 'create'), help=u"""Creates a new repository. \n[Command Reference](createRepository)""")
@cli_util.option('--name', required=True, help=u"""Unique name of a repository.""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project containing the repository.""")
@cli_util.option('--repository-type', required=True, help=u"""Type of repository.""")
@cli_util.option('--default-branch', help=u"""The default branch of the repository.""")
@cli_util.option('--mirror-repository-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Details of the repository. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'mirror-repository-config': {'module': 'devops', 'class': 'MirrorRepositoryConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mirror-repository-config': {'module': 'devops', 'class': 'MirrorRepositoryConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Repository'})
@cli_util.wrap_exceptions
def create_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, project_id, repository_type, default_branch, mirror_repository_config, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['projectId'] = project_id
    _details['repositoryType'] = repository_type

    if default_branch is not None:
        _details['defaultBranch'] = default_branch

    if mirror_repository_config is not None:
        _details['mirrorRepositoryConfig'] = cli_util.parse_json_parameter("mirror_repository_config", mirror_repository_config)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_repository(
        create_repository_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.create_trigger.command_name', 'create'), help=u"""Creates a new trigger. \n[Command Reference](createTrigger)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project to which the trigger belongs to.""")
@cli_util.option('--trigger-source', required=True, help=u"""Source of the trigger. Allowed values are, GITHUB and GITLAB.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'TriggerCreateResult'})
@cli_util.wrap_exceptions
def create_trigger(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, trigger_source, actions, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['triggerSource'] = trigger_source
    _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_trigger(
        create_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.create_trigger_create_github_trigger_details.command_name', 'create-trigger-create-github-trigger-details'), help=u"""Creates a new trigger. \n[Command Reference](createTrigger)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project to which the trigger belongs to.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'TriggerCreateResult'})
@cli_util.wrap_exceptions
def create_trigger_create_github_trigger_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, actions, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'GITHUB'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_trigger(
        create_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.create_trigger_create_devops_code_repository_trigger_details.command_name', 'create-trigger-create-devops-code-repository-trigger-details'), help=u"""Creates a new trigger. \n[Command Reference](createTrigger)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project to which the trigger belongs to.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repository-id', help=u"""The OCID of the DevOps code repository.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'TriggerCreateResult'})
@cli_util.wrap_exceptions
def create_trigger_create_devops_code_repository_trigger_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, actions, display_name, description, freeform_tags, defined_tags, repository_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if repository_id is not None:
        _details['repositoryId'] = repository_id

    _details['triggerSource'] = 'DEVOPS_CODE_REPOSITORY'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_trigger(
        create_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.create_trigger_create_bitbucket_cloud_trigger_details.command_name', 'create-trigger-create-bitbucket-cloud-trigger-details'), help=u"""Creates a new trigger. \n[Command Reference](createTrigger)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project to which the trigger belongs to.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'TriggerCreateResult'})
@cli_util.wrap_exceptions
def create_trigger_create_bitbucket_cloud_trigger_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, actions, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'BITBUCKET_CLOUD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_trigger(
        create_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.create_trigger_create_gitlab_trigger_details.command_name', 'create-trigger-create-gitlab-trigger-details'), help=u"""Creates a new trigger. \n[Command Reference](createTrigger)""")
@cli_util.option('--project-id', required=True, help=u"""The OCID of the DevOps project to which the trigger belongs to.""")
@cli_util.option('--actions', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'TriggerCreateResult'})
@cli_util.wrap_exceptions
def create_trigger_create_gitlab_trigger_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, actions, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'GITLAB'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.create_trigger(
        create_trigger_details=_details,
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


@build_pipeline_group.command(name=cli_util.override('devops.delete_build_pipeline.command_name', 'delete'), help=u"""Deletes a build pipeline resource by identifier. \n[Command Reference](deleteBuildPipeline)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""Unique build pipeline identifier.""")
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
def delete_build_pipeline(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, if_match):

    if isinstance(build_pipeline_id, six.string_types) and len(build_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_build_pipeline(
        build_pipeline_id=build_pipeline_id,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.delete_build_pipeline_stage.command_name', 'delete'), help=u"""Deletes a stage based on the stage ID provided in the request. \n[Command Reference](deleteBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
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
def delete_build_pipeline_stage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
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


@connection_group.command(name=cli_util.override('devops.delete_connection.command_name', 'delete'), help=u"""Deletes a connection resource by identifier. \n[Command Reference](deleteConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
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
def delete_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_connection(
        connection_id=connection_id,
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


@repository_group.command(name=cli_util.override('devops.delete_ref.command_name', 'delete-ref'), help=u"""Deletes a Repository's Ref by its name. Returns an error if the name is ambiguous. Can be disambiguated by using full names like \"heads/<name>\" or \"tags/<name>\". \n[Command Reference](deleteRef)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', required=True, help=u"""A filter to return only resources that match the given reference name.""")
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
def delete_ref(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, ref_name, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(ref_name, six.string_types) and len(ref_name.strip()) == 0:
        raise click.UsageError('Parameter --ref-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_ref(
        repository_id=repository_id,
        ref_name=ref_name,
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


@repository_group.command(name=cli_util.override('devops.delete_repository.command_name', 'delete'), help=u"""Deletes a repository resource by identifier. \n[Command Reference](deleteRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
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
def delete_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_repository(
        repository_id=repository_id,
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


@trigger_group.command(name=cli_util.override('devops.delete_trigger.command_name', 'delete'), help=u"""Deletes a trigger resource by identifier. \n[Command Reference](deleteTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
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
def delete_trigger(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.delete_trigger(
        trigger_id=trigger_id,
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


@build_pipeline_group.command(name=cli_util.override('devops.get_build_pipeline.command_name', 'get'), help=u"""Retrieves a build pipeline by identifier. \n[Command Reference](getBuildPipeline)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""Unique build pipeline identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildPipeline'})
@cli_util.wrap_exceptions
def get_build_pipeline(ctx, from_json, build_pipeline_id):

    if isinstance(build_pipeline_id, six.string_types) and len(build_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_build_pipeline(
        build_pipeline_id=build_pipeline_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@build_pipeline_stage_group.command(name=cli_util.override('devops.get_build_pipeline_stage.command_name', 'get'), help=u"""Retrieves a stage based on the stage ID provided in the request. \n[Command Reference](getBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def get_build_pipeline_stage(ctx, from_json, build_pipeline_stage_id):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@build_run_group.command(name=cli_util.override('devops.get_build_run.command_name', 'get'), help=u"""Returns the details of a build run for a given build run ID. \n[Command Reference](getBuildRun)""")
@cli_util.option('--build-run-id', required=True, help=u"""Unique build run identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildRun'})
@cli_util.wrap_exceptions
def get_build_run(ctx, from_json, build_run_id):

    if isinstance(build_run_id, six.string_types) and len(build_run_id.strip()) == 0:
        raise click.UsageError('Parameter --build-run-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_build_run(
        build_run_id=build_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_commit.command_name', 'get-commit'), help=u"""Retrieves a repository's commit by commit ID. \n[Command Reference](getCommit)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--commit-id', required=True, help=u"""A filter to return only resources that match the given commit ID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryCommit'})
@cli_util.wrap_exceptions
def get_commit(ctx, from_json, repository_id, commit_id):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(commit_id, six.string_types) and len(commit_id.strip()) == 0:
        raise click.UsageError('Parameter --commit-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_commit(
        repository_id=repository_id,
        commit_id=commit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_commit_diff.command_name', 'get-commit-diff'), help=u"""Compares two revisions for their differences. Supports comparison between two references or commits. \n[Command Reference](getCommitDiff)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--target-version', required=True, help=u"""The commit or reference name where changes are coming from.""")
@cli_util.option('--base-version', help=u"""The commit or reference name to compare changes against. If base version is not provided, the difference goes against an empty tree.""")
@cli_util.option('--is-comparison-from-merge-base', type=click.BOOL, help=u"""Boolean value to indicate whether to use merge base or most recent revision.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DiffResponse'})
@cli_util.wrap_exceptions
def get_commit_diff(ctx, from_json, repository_id, target_version, base_version, is_comparison_from_merge_base):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if base_version is not None:
        kwargs['base_version'] = base_version
    if is_comparison_from_merge_base is not None:
        kwargs['is_comparison_from_merge_base'] = is_comparison_from_merge_base
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_commit_diff(
        repository_id=repository_id,
        target_version=target_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('devops.get_connection.command_name', 'get'), help=u"""Retrieves a connection by identifier. \n[Command Reference](getConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, connection_id):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_connection(
        connection_id=connection_id,
        **kwargs
    )
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


@repository_group.command(name=cli_util.override('devops.get_file_diff.command_name', 'get-file-diff'), help=u"""Gets the line-by-line difference between file on different commits. This API will be deprecated on Wed, 29 Mar 2023 01:00:00 GMT as it does not get recognized when filePath has '/'. This will be replaced by \"/repositories/{repositoryId}/file/diffs\" \n[Command Reference](getFileDiff)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--file-path', required=True, help=u"""Path to a file within a repository.""")
@cli_util.option('--base-version', required=True, help=u"""The branch to compare changes against.""")
@cli_util.option('--target-version', required=True, help=u"""The branch where changes are coming from.""")
@cli_util.option('--is-comparison-from-merge-base', type=click.BOOL, help=u"""Boolean to indicate whether to use merge base or most recent revision.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'FileDiffResponse'})
@cli_util.wrap_exceptions
def get_file_diff(ctx, from_json, repository_id, file_path, base_version, target_version, is_comparison_from_merge_base):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(file_path, six.string_types) and len(file_path.strip()) == 0:
        raise click.UsageError('Parameter --file-path cannot be whitespace or empty string')

    kwargs = {}
    if is_comparison_from_merge_base is not None:
        kwargs['is_comparison_from_merge_base'] = is_comparison_from_merge_base
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_file_diff(
        repository_id=repository_id,
        file_path=file_path,
        base_version=base_version,
        target_version=target_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_mirror_record.command_name', 'get-mirror-record'), help=u"""Returns either current mirror record or last successful mirror record for a specific mirror repository. \n[Command Reference](getMirrorRecord)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--mirror-record-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["current", "lastSuccessful"]), help=u"""The field of mirror record type. Only one mirror record type can be provided: current - The current mirror record. lastSuccessful - The last successful mirror record.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryMirrorRecord'})
@cli_util.wrap_exceptions
def get_mirror_record(ctx, from_json, repository_id, mirror_record_type):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(mirror_record_type, six.string_types) and len(mirror_record_type.strip()) == 0:
        raise click.UsageError('Parameter --mirror-record-type cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_mirror_record(
        repository_id=repository_id,
        mirror_record_type=mirror_record_type,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_object_group.command(name=cli_util.override('devops.get_object.command_name', 'get-object'), help=u"""Retrieves blob of specific branch name/commit ID and file path. \n[Command Reference](getObject)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--file-path', help=u"""A filter to return only commits that affect any of the specified paths.""")
@cli_util.option('--ref-name', help=u"""A filter to return only resources that match the given reference name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryObject'})
@cli_util.wrap_exceptions
def get_object(ctx, from_json, repository_id, file_path, ref_name):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if file_path is not None:
        kwargs['file_path'] = file_path
    if ref_name is not None:
        kwargs['ref_name'] = ref_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_object(
        repository_id=repository_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_object_content.command_name', 'get-object-content'), help=u"""Retrieve contents of a specified object. \n[Command Reference](getObjectContent)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--sha', required=True, help=u"""The SHA of a blob or tree.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--file-path', help=u"""A filter to return only commits that affect any of the specified paths.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_object_content(ctx, from_json, file, repository_id, sha, file_path):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(sha, six.string_types) and len(sha.strip()) == 0:
        raise click.UsageError('Parameter --sha cannot be whitespace or empty string')

    kwargs = {}
    if file_path is not None:
        kwargs['file_path'] = file_path
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_object_content(
        repository_id=repository_id,
        sha=sha,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


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


@repository_group.command(name=cli_util.override('devops.get_ref.command_name', 'get-ref'), help=u"""Retrieves a repository's reference by its name with preference for branches over tags if the name is ambiguous. This can be disambiguated by using full names like \"heads/<name>\" or \"tags/<name>\". \n[Command Reference](getRef)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', required=True, help=u"""A filter to return only resources that match the given reference name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryRef'})
@cli_util.wrap_exceptions
def get_ref(ctx, from_json, repository_id, ref_name):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(ref_name, six.string_types) and len(ref_name.strip()) == 0:
        raise click.UsageError('Parameter --ref-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_ref(
        repository_id=repository_id,
        ref_name=ref_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_repo_file_diff.command_name', 'get-repo-file-diff'), help=u"""Gets the line-by-line difference between file on different commits. \n[Command Reference](getRepoFileDiff)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--base-version', required=True, help=u"""The branch to compare changes against.""")
@cli_util.option('--target-version', required=True, help=u"""The branch where changes are coming from.""")
@cli_util.option('--file-path', help=u"""A filter to return only commits that affect any of the specified paths.""")
@cli_util.option('--is-comparison-from-merge-base', type=click.BOOL, help=u"""Boolean to indicate whether to use merge base or most recent revision.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'FileDiffResponse'})
@cli_util.wrap_exceptions
def get_repo_file_diff(ctx, from_json, repository_id, base_version, target_version, file_path, is_comparison_from_merge_base):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if file_path is not None:
        kwargs['file_path'] = file_path
    if is_comparison_from_merge_base is not None:
        kwargs['is_comparison_from_merge_base'] = is_comparison_from_merge_base
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_repo_file_diff(
        repository_id=repository_id,
        base_version=base_version,
        target_version=target_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_repo_file_lines.command_name', 'get-repo-file-lines'), help=u"""Retrieve lines of a specified file. Supports starting line number and limit. \n[Command Reference](getRepoFileLines)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--revision', required=True, help=u"""Retrieve file lines from specific revision.""")
@cli_util.option('--file-path', help=u"""A filter to return only commits that affect any of the specified paths.""")
@cli_util.option('--start-line-number', type=click.INT, help=u"""Line number from where to start returning file lines.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryFileLines'})
@cli_util.wrap_exceptions
def get_repo_file_lines(ctx, from_json, repository_id, revision, file_path, start_line_number, limit):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if file_path is not None:
        kwargs['file_path'] = file_path
    if start_line_number is not None:
        kwargs['start_line_number'] = start_line_number
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_repo_file_lines(
        repository_id=repository_id,
        revision=revision,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_repository.command_name', 'get'), help=u"""Retrieves a repository by identifier. \n[Command Reference](getRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["branchCount", "commitCount", "sizeInBytes"]), multiple=True, help=u"""Fields parameter can contain multiple flags useful in deciding the API functionality.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Repository'})
@cli_util.wrap_exceptions
def get_repository(ctx, from_json, repository_id, fields):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_repository(
        repository_id=repository_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.get_repository_archive_content.command_name', 'get-repository-archive-content'), help=u"""Returns the archived repository information. \n[Command Reference](getRepositoryArchiveContent)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--ref-name', help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--format', help=u"""The archive format query parameter for downloading repository endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_repository_archive_content(ctx, from_json, file, repository_id, ref_name, format):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if ref_name is not None:
        kwargs['ref_name'] = ref_name
    if format is not None:
        kwargs['format'] = format
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_repository_archive_content(
        repository_id=repository_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@repository_group.command(name=cli_util.override('devops.get_repository_file_lines.command_name', 'get-repository-file-lines'), help=u"""Retrieve lines of a specified file. Supports starting line number and limit. This API will be deprecated on Wed, 29 Mar 2023 01:00:00 GMT as it does not get recognized when filePath has '/'. This will be replaced by \"/repositories/{repositoryId}/file/lines\" \n[Command Reference](getRepositoryFileLines)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--file-path', required=True, help=u"""Path to a file within a repository.""")
@cli_util.option('--revision', required=True, help=u"""Retrieve file lines from specific revision.""")
@cli_util.option('--start-line-number', type=click.INT, help=u"""Line number from where to start returning file lines.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryFileLines'})
@cli_util.wrap_exceptions
def get_repository_file_lines(ctx, from_json, repository_id, file_path, revision, start_line_number, limit):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(file_path, six.string_types) and len(file_path.strip()) == 0:
        raise click.UsageError('Parameter --file-path cannot be whitespace or empty string')

    kwargs = {}
    if start_line_number is not None:
        kwargs['start_line_number'] = start_line_number
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_repository_file_lines(
        repository_id=repository_id,
        file_path=file_path,
        revision=revision,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@trigger_group.command(name=cli_util.override('devops.get_trigger.command_name', 'get'), help=u"""Retrieves a trigger by identifier. \n[Command Reference](getTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def get_trigger(ctx, from_json, trigger_id):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.get_trigger(
        trigger_id=trigger_id,
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


@repository_group.command(name=cli_util.override('devops.list_authors.command_name', 'list-authors'), help=u"""Retrieve a list of all the authors. \n[Command Reference](listAuthors)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryAuthorCollection'})
@cli_util.wrap_exceptions
def list_authors(ctx, from_json, all_pages, page_size, repository_id, ref_name, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if ref_name is not None:
        kwargs['ref_name'] = ref_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_authors,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_authors,
            limit,
            page_size,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_authors(
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@build_pipeline_stage_summary_group.command(name=cli_util.override('devops.list_build_pipeline_stages.command_name', 'list-build-pipeline-stages'), help=u"""Returns a list of all stages in a compartment or build pipeline. \n[Command Reference](listBuildPipelineStages)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--build-pipeline-id', help=u"""The OCID of the parent build pipeline.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return the stages that matches the given lifecycle state.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildPipelineStageCollection'})
@cli_util.wrap_exceptions
def list_build_pipeline_stages(ctx, from_json, all_pages, page_size, id, build_pipeline_id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if build_pipeline_id is not None:
        kwargs['build_pipeline_id'] = build_pipeline_id
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
            client.list_build_pipeline_stages,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_build_pipeline_stages,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_build_pipeline_stages(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@build_pipeline_collection_group.command(name=cli_util.override('devops.list_build_pipelines.command_name', 'list-build-pipelines'), help=u"""Returns a list of build pipelines. \n[Command Reference](listBuildPipelines)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only build pipelines that matches the given lifecycle state.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildPipelineCollection'})
@cli_util.wrap_exceptions
def list_build_pipelines(ctx, from_json, all_pages, page_size, id, project_id, compartment_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

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
            client.list_build_pipelines,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_build_pipelines,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_build_pipelines(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@build_run_summary_group.command(name=cli_util.override('devops.list_build_runs.command_name', 'list-build-runs'), help=u"""Returns a list of build run summary. \n[Command Reference](listBuildRuns)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--build-pipeline-id', help=u"""Unique build pipeline identifier.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only build runs that matches the given lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'BuildRunSummaryCollection'})
@cli_util.wrap_exceptions
def list_build_runs(ctx, from_json, all_pages, page_size, id, build_pipeline_id, project_id, compartment_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if build_pipeline_id is not None:
        kwargs['build_pipeline_id'] = build_pipeline_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
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
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_build_runs,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_build_runs,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_build_runs(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.list_commit_diffs.command_name', 'list-commit-diffs'), help=u"""Compares two revisions and lists the differences. Supports comparison between two references or commits. \n[Command Reference](listCommitDiffs)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--base-version', required=True, help=u"""The commit or reference name to compare changes against.""")
@cli_util.option('--target-version', required=True, help=u"""The commit or reference name where changes are coming from.""")
@cli_util.option('--is-comparison-from-merge-base', type=click.BOOL, help=u"""Boolean value to indicate whether to use merge base or most recent revision.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'DiffCollection'})
@cli_util.wrap_exceptions
def list_commit_diffs(ctx, from_json, all_pages, page_size, repository_id, base_version, target_version, is_comparison_from_merge_base, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if is_comparison_from_merge_base is not None:
        kwargs['is_comparison_from_merge_base'] = is_comparison_from_merge_base
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_commit_diffs,
            repository_id=repository_id,
            base_version=base_version,
            target_version=target_version,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_commit_diffs,
            limit,
            page_size,
            repository_id=repository_id,
            base_version=base_version,
            target_version=target_version,
            **kwargs
        )
    else:
        result = client.list_commit_diffs(
            repository_id=repository_id,
            base_version=base_version,
            target_version=target_version,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@repository_commit_group.command(name=cli_util.override('devops.list_commits.command_name', 'list-commits'), help=u"""Returns a list of commits. \n[Command Reference](listCommits)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--exclude-ref-name', help=u"""A filter to exclude commits that match the given reference name.""")
@cli_util.option('--file-path', help=u"""A filter to return only commits that affect any of the specified paths.""")
@cli_util.option('--timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter to return commits only created after the specified timestamp value.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timestamp-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter to return commits only created before the specified timestamp value.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--commit-message', help=u"""A filter to return any commits that contains the given message.""")
@cli_util.option('--author-name', help=u"""A filter to return any commits that are pushed by the requested author.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryCommitCollection'})
@cli_util.wrap_exceptions
def list_commits(ctx, from_json, all_pages, page_size, repository_id, ref_name, exclude_ref_name, file_path, timestamp_greater_than_or_equal_to, timestamp_less_than_or_equal_to, commit_message, author_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if ref_name is not None:
        kwargs['ref_name'] = ref_name
    if exclude_ref_name is not None:
        kwargs['exclude_ref_name'] = exclude_ref_name
    if file_path is not None:
        kwargs['file_path'] = file_path
    if timestamp_greater_than_or_equal_to is not None:
        kwargs['timestamp_greater_than_or_equal_to'] = timestamp_greater_than_or_equal_to
    if timestamp_less_than_or_equal_to is not None:
        kwargs['timestamp_less_than_or_equal_to'] = timestamp_less_than_or_equal_to
    if commit_message is not None:
        kwargs['commit_message'] = commit_message
    if author_name is not None:
        kwargs['author_name'] = author_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_commits,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_commits,
            limit,
            page_size,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_commits(
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_collection_group.command(name=cli_util.override('devops.list_connections.command_name', 'list-connections'), help=u"""Returns a list of connections. \n[Command Reference](listConnections)""")
@cli_util.option('--id', help=u"""Unique identifier or OCID for listing a single resource by ID.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), help=u"""A filter to return only connections that matches the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--connection-type', type=custom_types.CliCaseInsensitiveChoice(["GITHUB_ACCESS_TOKEN", "GITLAB_ACCESS_TOKEN", "BITBUCKET_CLOUD_APP_PASSWORD"]), help=u"""A filter to return only resources that match the given connection type.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'ConnectionCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, id, project_id, compartment_id, lifecycle_state, display_name, connection_type, limit, page, sort_order, sort_by):

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
    if connection_type is not None:
        kwargs['connection_type'] = connection_type
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
            client.list_connections,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connections,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_connections(
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
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]), help=u"""A filter to return only DeployEnvironments that matches the given lifecycleState.""")
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


@repository_group.command(name=cli_util.override('devops.list_mirror_records.command_name', 'list-mirror-records'), help=u"""Returns a list of mirror entry in history within 30 days. \n[Command Reference](listMirrorRecords)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryMirrorRecordCollection'})
@cli_util.wrap_exceptions
def list_mirror_records(ctx, from_json, all_pages, page_size, repository_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_mirror_records,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_mirror_records,
            limit,
            page_size,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_mirror_records(
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@repository_path_summary_group.command(name=cli_util.override('devops.list_paths.command_name', 'list-paths'), help=u"""Retrieves a list of files and directories in a repository. \n[Command Reference](listPaths)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref', help=u"""The name of branch/tag or commit hash it points to. If names conflict, order of preference is commit > branch > tag. You can disambiguate with \"heads/foobar\" and \"tags/foobar\". If left blank repository's default branch will be used.""")
@cli_util.option('--paths-in-subtree', type=click.BOOL, help=u"""Flag to determine if files must be retrived recursively. Flag is False by default.""")
@cli_util.option('--folder-path', help=u"""The fully qualified path to the folder whose contents are returned, including the folder name. For example, /examples is a fully-qualified path to a folder named examples that was created off of the root directory (/) of a repository.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["type", "sizeInBytes", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order is ascending. If no value is specified name is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryPathCollection'})
@cli_util.wrap_exceptions
def list_paths(ctx, from_json, all_pages, page_size, repository_id, ref, paths_in_subtree, folder_path, limit, page, display_name, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if ref is not None:
        kwargs['ref'] = ref
    if paths_in_subtree is not None:
        kwargs['paths_in_subtree'] = paths_in_subtree
    if folder_path is not None:
        kwargs['folder_path'] = folder_path
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
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
            client.list_paths,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_paths,
            limit,
            page_size,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_paths(
            repository_id=repository_id,
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


@repository_ref_group.command(name=cli_util.override('devops.list_refs.command_name', 'list-refs'), help=u"""Returns a list of references. \n[Command Reference](listRefs)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-type', type=custom_types.CliCaseInsensitiveChoice(["BRANCH", "TAG"]), help=u"""Reference type to distinguish between branch and tag. If it is not specified, all references are returned.""")
@cli_util.option('--commit-id', help=u"""Commit ID in a repository.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--ref-name', help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["refType", "refName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for reference name is ascending. Default order for reference type is ascending. If no value is specified reference name is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryRefCollection'})
@cli_util.wrap_exceptions
def list_refs(ctx, from_json, all_pages, page_size, repository_id, ref_type, commit_id, limit, page, ref_name, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if ref_type is not None:
        kwargs['ref_type'] = ref_type
    if commit_id is not None:
        kwargs['commit_id'] = commit_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if ref_name is not None:
        kwargs['ref_name'] = ref_name
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
            client.list_refs,
            repository_id=repository_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_refs,
            limit,
            page_size,
            repository_id=repository_id,
            **kwargs
        )
    else:
        result = client.list_refs(
            repository_id=repository_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@repository_group.command(name=cli_util.override('devops.list_repositories.command_name', 'list'), help=u"""Returns a list of repositories given a compartment ID or a project ID. \n[Command Reference](listRepositories)""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--repository-id', help=u"""Unique repository identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED"]), help=u"""A filter to return only resources whose lifecycle state matches the given lifecycle state.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for name is ascending. If no value is specified time created is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryCollection'})
@cli_util.wrap_exceptions
def list_repositories(ctx, from_json, all_pages, page_size, compartment_id, project_id, repository_id, lifecycle_state, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if repository_id is not None:
        kwargs['repository_id'] = repository_id
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
            client.list_repositories,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_repositories,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_repositories(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@trigger_collection_group.command(name=cli_util.override('devops.list_triggers.command_name', 'list-triggers'), help=u"""Returns a list of triggers. \n[Command Reference](listTriggers)""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""unique project identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), help=u"""A filter to return only triggers that matches the given lifecycle state.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Unique trigger identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use. Use either ascending or descending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is ascending. If no value is specified, then the default time created value is considered.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'TriggerCollection'})
@cli_util.wrap_exceptions
def list_triggers(ctx, from_json, all_pages, page_size, compartment_id, project_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
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
            client.list_triggers,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_triggers,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_triggers(
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


@repository_group.command(name=cli_util.override('devops.mirror_repository.command_name', 'mirror'), help=u"""Synchronize a mirrored repository to the latest version from external providers. \n[Command Reference](mirrorRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def mirror_repository(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.mirror_repository(
        repository_id=repository_id,
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


@repository_group.command(name=cli_util.override('devops.put_repository_ref.command_name', 'put-repository-ref'), help=u"""Creates a new reference or updates an existing one. \n[Command Reference](putRepositoryRef)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', required=True, help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--ref-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BRANCH", "TAG"]), help=u"""The type of reference (BRANCH or TAG).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryRef'})
@cli_util.wrap_exceptions
def put_repository_ref(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, ref_name, ref_type, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(ref_name, six.string_types) and len(ref_name.strip()) == 0:
        raise click.UsageError('Parameter --ref-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['refType'] = ref_type

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.put_repository_ref(
        repository_id=repository_id,
        ref_name=ref_name,
        put_repository_ref_details=_details,
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


@repository_group.command(name=cli_util.override('devops.put_repository_ref_put_repository_tag_details.command_name', 'put-repository-ref-put-repository-tag-details'), help=u"""Creates a new reference or updates an existing one. \n[Command Reference](putRepositoryRef)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', required=True, help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--object-id', required=True, help=u"""SHA-1 hash value of the object pointed to by the tag.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryRef'})
@cli_util.wrap_exceptions
def put_repository_ref_put_repository_tag_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, ref_name, object_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(ref_name, six.string_types) and len(ref_name.strip()) == 0:
        raise click.UsageError('Parameter --ref-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['objectId'] = object_id

    _details['refType'] = 'TAG'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.put_repository_ref(
        repository_id=repository_id,
        ref_name=ref_name,
        put_repository_ref_details=_details,
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


@repository_group.command(name=cli_util.override('devops.put_repository_ref_put_repository_branch_details.command_name', 'put-repository-ref-put-repository-branch-details'), help=u"""Creates a new reference or updates an existing one. \n[Command Reference](putRepositoryRef)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--ref-name', required=True, help=u"""A filter to return only resources that match the given reference name.""")
@cli_util.option('--commit-id', required=True, help=u"""Commit ID pointed to by the new branch.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'devops', 'class': 'RepositoryRef'})
@cli_util.wrap_exceptions
def put_repository_ref_put_repository_branch_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, ref_name, commit_id, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(ref_name, six.string_types) and len(ref_name.strip()) == 0:
        raise click.UsageError('Parameter --ref-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['commitId'] = commit_id

    _details['refType'] = 'BRANCH'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.put_repository_ref(
        repository_id=repository_id,
        ref_name=ref_name,
        put_repository_ref_details=_details,
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


@build_pipeline_group.command(name=cli_util.override('devops.update_build_pipeline.command_name', 'update'), help=u"""Updates the build pipeline. \n[Command Reference](updateBuildPipeline)""")
@cli_util.option('--build-pipeline-id', required=True, help=u"""Unique build pipeline identifier.""")
@cli_util.option('--description', help=u"""Optional description about the build pipeline.""")
@cli_util.option('--display-name', help=u"""Build pipeline display name. Avoid entering confidential information.""")
@cli_util.option('--build-pipeline-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-parameters': {'module': 'devops', 'class': 'BuildPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-parameters': {'module': 'devops', 'class': 'BuildPipelineParameterCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipeline'})
@cli_util.wrap_exceptions
def update_build_pipeline(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_id, description, display_name, build_pipeline_parameters, freeform_tags, defined_tags, if_match):

    if isinstance(build_pipeline_id, six.string_types) and len(build_pipeline_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to build-pipeline-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if build_pipeline_parameters is not None:
        _details['buildPipelineParameters'] = cli_util.parse_json_parameter("build_pipeline_parameters", build_pipeline_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline(
        build_pipeline_id=build_pipeline_id,
        update_build_pipeline_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.update_build_pipeline_stage.command_name', 'update'), help=u"""Updates the stage based on the stage ID provided in the request. \n[Command Reference](updateBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--build-pipeline-stage-type', required=True, help=u"""Stage types.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the build stage.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, build_pipeline_stage_type, display_name, description, build_pipeline_stage_predecessor_collection, freeform_tags, defined_tags, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_stage_predecessor_collection or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to build-pipeline-stage-predecessor-collection and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['buildPipelineStageType'] = build_pipeline_stage_type

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if build_pipeline_stage_predecessor_collection is not None:
        _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        update_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.update_build_pipeline_stage_update_wait_stage_details.command_name', 'update-build-pipeline-stage-update-wait-stage-details'), help=u"""Updates the stage based on the stage ID provided in the request. \n[Command Reference](updateBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the build stage.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-criteria', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'UpdateWaitCriteriaDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'wait-criteria': {'module': 'devops', 'class': 'UpdateWaitCriteriaDetails'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_wait_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, display_name, description, build_pipeline_stage_predecessor_collection, freeform_tags, defined_tags, wait_criteria, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_stage_predecessor_collection or freeform_tags or defined_tags or wait_criteria:
            if not click.confirm("WARNING: Updates to build-pipeline-stage-predecessor-collection and freeform-tags and defined-tags and wait-criteria will replace any existing values. Are you sure you want to continue?"):
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

    if build_pipeline_stage_predecessor_collection is not None:
        _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if wait_criteria is not None:
        _details['waitCriteria'] = cli_util.parse_json_parameter("wait_criteria", wait_criteria)

    _details['buildPipelineStageType'] = 'WAIT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        update_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.update_build_pipeline_stage_update_build_stage_details.command_name', 'update-build-pipeline-stage-update-build-stage-details'), help=u"""Updates the stage based on the stage ID provided in the request. \n[Command Reference](updateBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the build stage.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image', help=u"""Image name for the build environment.""")
@cli_util.option('--build-spec-file', help=u"""The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.""")
@cli_util.option('--stage-execution-timeout-in-seconds', type=click.INT, help=u"""Timeout for the build stage execution. Specify value in seconds.""")
@cli_util.option('--build-source-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--primary-build-source', help=u"""Name of the build source where the build_spec.yml file is located. If not specified, the first entry in the build source collection is chosen as primary build source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'build-source-collection': {'module': 'devops', 'class': 'BuildSourceCollection'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_build_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, display_name, description, build_pipeline_stage_predecessor_collection, freeform_tags, defined_tags, image, build_spec_file, stage_execution_timeout_in_seconds, build_source_collection, primary_build_source, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_stage_predecessor_collection or freeform_tags or defined_tags or build_source_collection:
            if not click.confirm("WARNING: Updates to build-pipeline-stage-predecessor-collection and freeform-tags and defined-tags and build-source-collection will replace any existing values. Are you sure you want to continue?"):
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

    if build_pipeline_stage_predecessor_collection is not None:
        _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if image is not None:
        _details['image'] = image

    if build_spec_file is not None:
        _details['buildSpecFile'] = build_spec_file

    if stage_execution_timeout_in_seconds is not None:
        _details['stageExecutionTimeoutInSeconds'] = stage_execution_timeout_in_seconds

    if build_source_collection is not None:
        _details['buildSourceCollection'] = cli_util.parse_json_parameter("build_source_collection", build_source_collection)

    if primary_build_source is not None:
        _details['primaryBuildSource'] = primary_build_source

    _details['buildPipelineStageType'] = 'BUILD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        update_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.update_build_pipeline_stage_update_trigger_deployment_stage_details.command_name', 'update-build-pipeline-stage-update-trigger-deployment-stage-details'), help=u"""Updates the stage based on the stage ID provided in the request. \n[Command Reference](updateBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the build stage.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deploy-pipeline-id', help=u"""A target deployment pipeline OCID that will run in this stage.""")
@cli_util.option('--is-pass-all-parameters-enabled', type=click.BOOL, help=u"""A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_trigger_deployment_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, display_name, description, build_pipeline_stage_predecessor_collection, freeform_tags, defined_tags, deploy_pipeline_id, is_pass_all_parameters_enabled, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_stage_predecessor_collection or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to build-pipeline-stage-predecessor-collection and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if build_pipeline_stage_predecessor_collection is not None:
        _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deploy_pipeline_id is not None:
        _details['deployPipelineId'] = deploy_pipeline_id

    if is_pass_all_parameters_enabled is not None:
        _details['isPassAllParametersEnabled'] = is_pass_all_parameters_enabled

    _details['buildPipelineStageType'] = 'TRIGGER_DEPLOYMENT_PIPELINE'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        update_build_pipeline_stage_details=_details,
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


@build_pipeline_stage_group.command(name=cli_util.override('devops.update_build_pipeline_stage_update_deliver_artifact_stage_details.command_name', 'update-build-pipeline-stage-update-deliver-artifact-stage-details'), help=u"""Updates the stage based on the stage ID provided in the request. \n[Command Reference](updateBuildPipelineStage)""")
@cli_util.option('--build-pipeline-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--display-name', help=u"""Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the build stage.""")
@cli_util.option('--build-pipeline-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deliver-artifact-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'build-pipeline-stage-predecessor-collection': {'module': 'devops', 'class': 'BuildPipelineStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deliver-artifact-collection': {'module': 'devops', 'class': 'DeliverArtifactCollection'}}, output_type={'module': 'devops', 'class': 'BuildPipelineStage'})
@cli_util.wrap_exceptions
def update_build_pipeline_stage_update_deliver_artifact_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_pipeline_stage_id, display_name, description, build_pipeline_stage_predecessor_collection, freeform_tags, defined_tags, deliver_artifact_collection, if_match):

    if isinstance(build_pipeline_stage_id, six.string_types) and len(build_pipeline_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --build-pipeline-stage-id cannot be whitespace or empty string')
    if not force:
        if build_pipeline_stage_predecessor_collection or freeform_tags or defined_tags or deliver_artifact_collection:
            if not click.confirm("WARNING: Updates to build-pipeline-stage-predecessor-collection and freeform-tags and defined-tags and deliver-artifact-collection will replace any existing values. Are you sure you want to continue?"):
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

    if build_pipeline_stage_predecessor_collection is not None:
        _details['buildPipelineStagePredecessorCollection'] = cli_util.parse_json_parameter("build_pipeline_stage_predecessor_collection", build_pipeline_stage_predecessor_collection)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if deliver_artifact_collection is not None:
        _details['deliverArtifactCollection'] = cli_util.parse_json_parameter("deliver_artifact_collection", deliver_artifact_collection)

    _details['buildPipelineStageType'] = 'DELIVER_ARTIFACT'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_pipeline_stage(
        build_pipeline_stage_id=build_pipeline_stage_id,
        update_build_pipeline_stage_details=_details,
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


@build_run_group.command(name=cli_util.override('devops.update_build_run.command_name', 'update'), help=u"""Updates the build run. \n[Command Reference](updateBuildRun)""")
@cli_util.option('--build-run-id', required=True, help=u"""Unique build run identifier.""")
@cli_util.option('--display-name', help=u"""Build run display name. Avoid entering confidential information.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'BuildRun'})
@cli_util.wrap_exceptions
def update_build_run(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, build_run_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(build_run_id, six.string_types) and len(build_run_id.strip()) == 0:
        raise click.UsageError('Parameter --build-run-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_build_run(
        build_run_id=build_run_id,
        update_build_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_build_run') and callable(getattr(client, 'get_build_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_build_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@connection_group.command(name=cli_util.override('devops.update_connection.command_name', 'update'), help=u"""Updates the connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
@cli_util.option('--connection-type', required=True, help=u"""The type of connection.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, connection_type, description, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionType'] = connection_type

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_connection(
        connection_id=connection_id,
        update_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.update_connection_update_github_access_token_connection_details.command_name', 'update-connection-update-github-access-token-connection-details'), help=u"""Updates the connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-token', help=u"""OCID of personal access token saved in secret store""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_github_access_token_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, description, display_name, freeform_tags, defined_tags, access_token, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
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

    if access_token is not None:
        _details['accessToken'] = access_token

    _details['connectionType'] = 'GITHUB_ACCESS_TOKEN'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_connection(
        connection_id=connection_id,
        update_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.update_connection_update_gitlab_access_token_connection_details.command_name', 'update-connection-update-gitlab-access-token-connection-details'), help=u"""Updates the connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--access-token', help=u"""The OCID of personal access token saved in secret store.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_gitlab_access_token_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, description, display_name, freeform_tags, defined_tags, access_token, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
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

    if access_token is not None:
        _details['accessToken'] = access_token

    _details['connectionType'] = 'GITLAB_ACCESS_TOKEN'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_connection(
        connection_id=connection_id,
        update_connection_details=_details,
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


@connection_group.command(name=cli_util.override('devops.update_connection_update_bitbucket_cloud_app_password_connection_details.command_name', 'update-connection-update-bitbucket-cloud-app-password-connection-details'), help=u"""Updates the connection. \n[Command Reference](updateConnection)""")
@cli_util.option('--connection-id', required=True, help=u"""Unique connection identifier.""")
@cli_util.option('--description', help=u"""Optional description about the connection.""")
@cli_util.option('--display-name', help=u"""Optional connection display name. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""Public Bitbucket Cloud Username in plain text(not more than 30 characters)""")
@cli_util.option('--app-password', help=u"""OCID of personal Bitbucket Cloud AppPassword saved in secret store""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_bitbucket_cloud_app_password_connection_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connection_id, description, display_name, freeform_tags, defined_tags, username, app_password, if_match):

    if isinstance(connection_id, six.string_types) and len(connection_id.strip()) == 0:
        raise click.UsageError('Parameter --connection-id cannot be whitespace or empty string')
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

    if username is not None:
        _details['username'] = username

    if app_password is not None:
        _details['appPassword'] = app_password

    _details['connectionType'] = 'BITBUCKET_CLOUD_APP_PASSWORD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_connection(
        connection_id=connection_id,
        update_connection_details=_details,
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
@cli_util.option('--deploy-artifact-source-repository-id', required=True, help=u"""The OCID of a repository.""")
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


@deploy_artifact_group.command(name=cli_util.override('devops.update_deploy_artifact_helm_repository_deploy_artifact_source.command_name', 'update-deploy-artifact-helm-repository-deploy-artifact-source'), help=u"""Updates the deployment artifact. \n[Command Reference](updateDeployArtifact)""")
@cli_util.option('--deploy-artifact-id', required=True, help=u"""Unique artifact identifier.""")
@cli_util.option('--deploy-artifact-source-chart-url', required=True, help=u"""The URL of an OCIR repository.""")
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
def update_deploy_artifact_helm_repository_deploy_artifact_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_artifact_id, deploy_artifact_source_chart_url, deploy_artifact_source_deploy_artifact_version, description, display_name, deploy_artifact_type, argument_substitution_mode, freeform_tags, defined_tags, if_match):

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
    _details['deployArtifactSource']['chartUrl'] = deploy_artifact_source_chart_url
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

    _details['deployArtifactSource']['deployArtifactSourceType'] = 'HELM_CHART'

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
@cli_util.option('--deploy-artifact-source-image-uri', required=True, help=u"""Specifies OCIR image path - optionally include tag.""")
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
@cli_util.option('--network-channel', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'network-channel': {'module': 'devops', 'class': 'NetworkChannel'}}, output_type={'module': 'devops', 'class': 'DeployEnvironment'})
@cli_util.wrap_exceptions
def update_deploy_environment_update_oke_cluster_deploy_environment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_environment_id, description, display_name, freeform_tags, defined_tags, cluster_id, network_channel, if_match):

    if isinstance(deploy_environment_id, six.string_types) and len(deploy_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-environment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or network_channel:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and network-channel will replace any existing values. Are you sure you want to continue?"):
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

    if network_channel is not None:
        _details['networkChannel'] = cli_util.parse_json_parameter("network_channel", network_channel)

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-canary-traffic-shift-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_canary_traffic_shift_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, rollout_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or rollout_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and rollout-policy will replace any existing values. Are you sure you want to continue?"):
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

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    _details['deployStageType'] = 'OKE_CANARY_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_canary_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-canary-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_canary_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, kubernetes_manifest_deploy_artifact_ids, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or kubernetes_manifest_deploy_artifact_ids:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and kubernetes-manifest-deploy-artifact-ids will replace any existing values. Are you sure you want to continue?"):
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

    if kubernetes_manifest_deploy_artifact_ids is not None:
        _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)

    _details['deployStageType'] = 'OKE_CANARY_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_helm_chart_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-helm-chart-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oke-cluster-deploy-environment-id', help=u"""Kubernetes cluster environment OCID for deployment.""")
@cli_util.option('--helm-chart-deploy-artifact-id', help=u"""Helm chart artifact OCID.""")
@cli_util.option('--values-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of values.yaml file artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--release-name', help=u"""Name of the Helm chart release.""")
@cli_util.option('--namespace', help=u"""Default namespace to be used for Kubernetes deployment when not specified in the manifest.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Time to wait for execution of a helm stage. Defaults to 300 seconds.""")
@cli_util.option('--rollback-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'values-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollback-policy': {'module': 'devops', 'class': 'DeployStageRollbackPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_helm_chart_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, oke_cluster_deploy_environment_id, helm_chart_deploy_artifact_id, values_artifact_ids, release_name, namespace, timeout_in_seconds, rollback_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or values_artifact_ids or rollback_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and values-artifact-ids and rollback-policy will replace any existing values. Are you sure you want to continue?"):
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

    if helm_chart_deploy_artifact_id is not None:
        _details['helmChartDeployArtifactId'] = helm_chart_deploy_artifact_id

    if values_artifact_ids is not None:
        _details['valuesArtifactIds'] = cli_util.parse_json_parameter("values_artifact_ids", values_artifact_ids)

    if release_name is not None:
        _details['releaseName'] = release_name

    if namespace is not None:
        _details['namespace'] = namespace

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if rollback_policy is not None:
        _details['rollbackPolicy'] = cli_util.parse_json_parameter("rollback_policy", rollback_policy)

    _details['deployStageType'] = 'OKE_HELM_CHART_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_canary_approval_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-canary-approval-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
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
def update_deploy_stage_update_oke_canary_approval_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, approval_policy, if_match):

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

    _details['deployStageType'] = 'OKE_CANARY_APPROVAL'

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
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-canary-approval-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
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
def update_deploy_stage_update_compute_instance_group_canary_approval_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, approval_policy, if_match):

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

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_blue_green_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-blue-green-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kubernetes-manifest-deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'kubernetes-manifest-deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_oke_blue_green_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, kubernetes_manifest_deploy_artifact_ids, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or kubernetes_manifest_deploy_artifact_ids:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and kubernetes-manifest-deploy-artifact-ids will replace any existing values. Are you sure you want to continue?"):
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

    if kubernetes_manifest_deploy_artifact_ids is not None:
        _details['kubernetesManifestDeployArtifactIds'] = cli_util.parse_json_parameter("kubernetes_manifest_deploy_artifact_ids", kubernetes_manifest_deploy_artifact_ids)

    _details['deployStageType'] = 'OKE_BLUE_GREEN_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details.command_name', 'update-deploy-stage-update-oke-blue-green-traffic-shift-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
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
def update_deploy_stage_update_oke_blue_green_traffic_shift_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, if_match):

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

    _details['deployStageType'] = 'OKE_BLUE_GREEN_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-blue-green-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-spec-deploy-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--failure-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'failure-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupFailurePolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_blue_green_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, deployment_spec_deploy_artifact_id, deploy_artifact_ids, rollout_policy, failure_policy, test_load_balancer_config, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or deploy_artifact_ids or rollout_policy or failure_policy or test_load_balancer_config:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and deploy-artifact-ids and rollout-policy and failure-policy and test-load-balancer-config will replace any existing values. Are you sure you want to continue?"):
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

    if deployment_spec_deploy_artifact_id is not None:
        _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id

    if deploy_artifact_ids is not None:
        _details['deployArtifactIds'] = cli_util.parse_json_parameter("deploy_artifact_ids", deploy_artifact_ids)

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if failure_policy is not None:
        _details['failurePolicy'] = cli_util.parse_json_parameter("failure_policy", failure_policy)

    if test_load_balancer_config is not None:
        _details['testLoadBalancerConfig'] = cli_util.parse_json_parameter("test_load_balancer_config", test_load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-canary-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--deployment-spec-deploy-artifact-id', help=u"""The OCID of the artifact that contains the deployment specification.""")
@cli_util.option('--deploy-artifact-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of file artifact OCIDs to deploy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--test-load-balancer-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'deploy-artifact-ids': {'module': 'devops', 'class': 'list[string]'}, 'rollout-policy': {'module': 'devops', 'class': 'ComputeInstanceGroupRolloutPolicy'}, 'test-load-balancer-config': {'module': 'devops', 'class': 'LoadBalancerConfig'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_canary_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, deployment_spec_deploy_artifact_id, deploy_artifact_ids, rollout_policy, test_load_balancer_config, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or deploy_artifact_ids or rollout_policy or test_load_balancer_config:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and deploy-artifact-ids and rollout-policy and test-load-balancer-config will replace any existing values. Are you sure you want to continue?"):
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

    if deployment_spec_deploy_artifact_id is not None:
        _details['deploymentSpecDeployArtifactId'] = deployment_spec_deploy_artifact_id

    if deploy_artifact_ids is not None:
        _details['deployArtifactIds'] = cli_util.parse_json_parameter("deploy_artifact_ids", deploy_artifact_ids)

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    if test_load_balancer_config is not None:
        _details['testLoadBalancerConfig'] = cli_util.parse_json_parameter("test_load_balancer_config", test_load_balancer_config)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-blue-green-traffic-shift-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
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
def update_deploy_stage_update_compute_instance_group_blue_green_traffic_shift_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, if_match):

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

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT'

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


@deploy_stage_group.command(name=cli_util.override('devops.update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details.command_name', 'update-deploy-stage-update-compute-instance-group-canary-traffic-shift-deploy-stage-details'), help=u"""Updates the deployment stage. \n[Command Reference](updateDeployStage)""")
@cli_util.option('--deploy-stage-id', required=True, help=u"""Unique stage identifier.""")
@cli_util.option('--description', help=u"""Optional description about the deployment stage.""")
@cli_util.option('--display-name', help=u"""Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.""")
@cli_util.option('--deploy-stage-predecessor-collection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rollout-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'deploy-stage-predecessor-collection': {'module': 'devops', 'class': 'DeployStagePredecessorCollection'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}, 'rollout-policy': {'module': 'devops', 'class': 'LoadBalancerTrafficShiftRolloutPolicy'}}, output_type={'module': 'devops', 'class': 'DeployStage'})
@cli_util.wrap_exceptions
def update_deploy_stage_update_compute_instance_group_canary_traffic_shift_deploy_stage_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deploy_stage_id, description, display_name, deploy_stage_predecessor_collection, freeform_tags, defined_tags, rollout_policy, if_match):

    if isinstance(deploy_stage_id, six.string_types) and len(deploy_stage_id.strip()) == 0:
        raise click.UsageError('Parameter --deploy-stage-id cannot be whitespace or empty string')
    if not force:
        if deploy_stage_predecessor_collection or freeform_tags or defined_tags or rollout_policy:
            if not click.confirm("WARNING: Updates to deploy-stage-predecessor-collection and freeform-tags and defined-tags and rollout-policy will replace any existing values. Are you sure you want to continue?"):
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

    if rollout_policy is not None:
        _details['rolloutPolicy'] = cli_util.parse_json_parameter("rollout_policy", rollout_policy)

    _details['deployStageType'] = 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT'

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


@deployment_group.command(name=cli_util.override('devops.update_deployment_update_single_deploy_stage_redeployment_details.command_name', 'update-deployment-update-single-deploy-stage-redeployment-details'), help=u"""Updates the deployment. \n[Command Reference](updateDeployment)""")
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
def update_deployment_update_single_deploy_stage_redeployment_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, deployment_id, display_name, freeform_tags, defined_tags, if_match):

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

    _details['deploymentType'] = 'SINGLE_STAGE_REDEPLOYMENT'

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


@repository_group.command(name=cli_util.override('devops.update_repository.command_name', 'update'), help=u"""Updates the repository. \n[Command Reference](updateRepository)""")
@cli_util.option('--repository-id', required=True, help=u"""Unique repository identifier.""")
@cli_util.option('--name', help=u"""Unique name of a repository.""")
@cli_util.option('--description', help=u"""Details of the repository. Avoid entering confidential information.""")
@cli_util.option('--default-branch', help=u"""The default branch of the repository.""")
@cli_util.option('--repository-type', help=u"""Type of repository.""")
@cli_util.option('--mirror-repository-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'mirror-repository-config': {'module': 'devops', 'class': 'MirrorRepositoryConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mirror-repository-config': {'module': 'devops', 'class': 'MirrorRepositoryConfig'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Repository'})
@cli_util.wrap_exceptions
def update_repository(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, repository_id, name, description, default_branch, repository_type, mirror_repository_config, freeform_tags, defined_tags, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')
    if not force:
        if mirror_repository_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to mirror-repository-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if default_branch is not None:
        _details['defaultBranch'] = default_branch

    if repository_type is not None:
        _details['repositoryType'] = repository_type

    if mirror_repository_config is not None:
        _details['mirrorRepositoryConfig'] = cli_util.parse_json_parameter("mirror_repository_config", mirror_repository_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_repository(
        repository_id=repository_id,
        update_repository_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.update_trigger.command_name', 'update'), help=u"""Updates the trigger. \n[Command Reference](updateTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@cli_util.option('--trigger-source', required=True, help=u"""Source of the trigger. Allowed values are, GITHUB and GITLAB.""")
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.

This option is a JSON list with items of type TriggerAction.  For documentation on TriggerAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/devops/20210630/datatypes/TriggerAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def update_trigger(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, trigger_source, display_name, description, actions, freeform_tags, defined_tags, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['triggerSource'] = trigger_source

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_trigger(
        trigger_id=trigger_id,
        update_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.update_trigger_update_devops_code_repository_trigger_details.command_name', 'update-trigger-update-devops-code-repository-trigger-details'), help=u"""Updates the trigger. \n[Command Reference](updateTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.

This option is a JSON list with items of type TriggerAction.  For documentation on TriggerAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/devops/20210630/datatypes/TriggerAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repository-id', help=u"""The OCID of the DevOps code repository.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def update_trigger_update_devops_code_repository_trigger_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, display_name, description, actions, freeform_tags, defined_tags, repository_id, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if repository_id is not None:
        _details['repositoryId'] = repository_id

    _details['triggerSource'] = 'DEVOPS_CODE_REPOSITORY'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_trigger(
        trigger_id=trigger_id,
        update_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.update_trigger_update_github_trigger_details.command_name', 'update-trigger-update-github-trigger-details'), help=u"""Updates the trigger. \n[Command Reference](updateTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.

This option is a JSON list with items of type TriggerAction.  For documentation on TriggerAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/devops/20210630/datatypes/TriggerAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def update_trigger_update_github_trigger_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, display_name, description, actions, freeform_tags, defined_tags, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'GITHUB'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_trigger(
        trigger_id=trigger_id,
        update_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.update_trigger_update_gitlab_trigger_details.command_name', 'update-trigger-update-gitlab-trigger-details'), help=u"""Updates the trigger. \n[Command Reference](updateTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.

This option is a JSON list with items of type TriggerAction.  For documentation on TriggerAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/devops/20210630/datatypes/TriggerAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def update_trigger_update_gitlab_trigger_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, display_name, description, actions, freeform_tags, defined_tags, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'GITLAB'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_trigger(
        trigger_id=trigger_id,
        update_trigger_details=_details,
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


@trigger_group.command(name=cli_util.override('devops.update_trigger_update_bitbucket_cloud_trigger_details.command_name', 'update-trigger-update-bitbucket-cloud-trigger-details'), help=u"""Updates the trigger. \n[Command Reference](updateTrigger)""")
@cli_util.option('--trigger-id', required=True, help=u"""Unique trigger identifier.""")
@cli_util.option('--display-name', help=u"""Trigger display name. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Optional description about the trigger.""")
@cli_util.option('--actions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of actions that are to be performed for this trigger.

This option is a JSON list with items of type TriggerAction.  For documentation on TriggerAction please see our API reference: https://docs.cloud.oracle.com/api/#/en/devops/20210630/datatypes/TriggerAction.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See [Resource Tags]. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'actions': {'module': 'devops', 'class': 'list[TriggerAction]'}, 'freeform-tags': {'module': 'devops', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'devops', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'devops', 'class': 'Trigger'})
@cli_util.wrap_exceptions
def update_trigger_update_bitbucket_cloud_trigger_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, trigger_id, display_name, description, actions, freeform_tags, defined_tags, if_match):

    if isinstance(trigger_id, six.string_types) and len(trigger_id.strip()) == 0:
        raise click.UsageError('Parameter --trigger-id cannot be whitespace or empty string')
    if not force:
        if actions or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to actions and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if actions is not None:
        _details['actions'] = cli_util.parse_json_parameter("actions", actions)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['triggerSource'] = 'BITBUCKET_CLOUD'

    client = cli_util.build_client('devops', 'devops', ctx)
    result = client.update_trigger(
        trigger_id=trigger_id,
        update_trigger_details=_details,
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
