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


@cli.command(cli_util.override('data_science.data_science_root_group.command_name', 'data-science'), cls=CommandGroupWithAlias, help=cli_util.override('data_science.data_science_root_group.help', """Use the Data Science API to organize your data science work, access data and computing resources, and build, train, deploy and manage models and model deployments. For more information, see [Data Science]."""), short_help=cli_util.override('data_science.data_science_root_group.short_help', """Data Science API"""))
@cli_util.help_option_group
def data_science_root_group():
    pass


@click.command(cli_util.override('data_science.model_deployment_shape_group.command_name', 'model-deployment-shape'), cls=CommandGroupWithAlias, help="""The compute shape used to launch a model deployment compute instance.""")
@cli_util.help_option_group
def model_deployment_shape_group():
    pass


@click.command(cli_util.override('data_science.job_shape_group.command_name', 'job-shape'), cls=CommandGroupWithAlias, help="""The compute shape used to launch a job compute instance.""")
@cli_util.help_option_group
def job_shape_group():
    pass


@click.command(cli_util.override('data_science.model_deployment_group.command_name', 'model-deployment'), cls=CommandGroupWithAlias, help="""Model deployments are used by data scientists to perform predictions from the model hosted on an HTTP server.""")
@cli_util.help_option_group
def model_deployment_group():
    pass


@click.command(cli_util.override('data_science.job_run_group.command_name', 'job-run'), cls=CommandGroupWithAlias, help="""A job run.""")
@cli_util.help_option_group
def job_run_group():
    pass


@click.command(cli_util.override('data_science.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""Projects enable users to organize their data science work.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('data_science.fast_launch_job_config_group.command_name', 'fast-launch-job-config'), cls=CommandGroupWithAlias, help="""The shape config to launch a fast launch capable job instance""")
@cli_util.help_option_group
def fast_launch_job_config_group():
    pass


@click.command(cli_util.override('data_science.model_group.command_name', 'model'), cls=CommandGroupWithAlias, help="""Models are mathematical representations of the relationships between data. Models are represented by their associated metadata and artifacts.""")
@cli_util.help_option_group
def model_group():
    pass


@click.command(cli_util.override('data_science.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_science.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""A job for training models.""")
@cli_util.help_option_group
def job_group():
    pass


@click.command(cli_util.override('data_science.notebook_session_shape_group.command_name', 'notebook-session-shape'), cls=CommandGroupWithAlias, help="""The compute shape used to launch a notebook session compute instance.""")
@cli_util.help_option_group
def notebook_session_shape_group():
    pass


@click.command(cli_util.override('data_science.notebook_session_group.command_name', 'notebook-session'), cls=CommandGroupWithAlias, help="""Notebook sessions are interactive coding environments for data scientists.""")
@cli_util.help_option_group
def notebook_session_group():
    pass


data_science_root_group.add_command(model_deployment_shape_group)
data_science_root_group.add_command(job_shape_group)
data_science_root_group.add_command(model_deployment_group)
data_science_root_group.add_command(job_run_group)
data_science_root_group.add_command(project_group)
data_science_root_group.add_command(fast_launch_job_config_group)
data_science_root_group.add_command(model_group)
data_science_root_group.add_command(work_request_group)
data_science_root_group.add_command(job_group)
data_science_root_group.add_command(notebook_session_shape_group)
data_science_root_group.add_command(notebook_session_group)


@model_group.command(name=cli_util.override('data_science.activate_model.command_name', 'activate'), help=u"""Activates the model. \n[Command Reference](activateModel)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'Model'})
@cli_util.wrap_exceptions
def activate_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.activate_model(
        model_id=model_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_model') and callable(getattr(client, 'get_model')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_model(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_deployment_group.command(name=cli_util.override('data_science.activate_model_deployment.command_name', 'activate'), help=u"""Activates the model deployment. \n[Command Reference](activateModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_model_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_deployment_id, if_match):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.activate_model_deployment(
        model_deployment_id=model_deployment_id,
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


@notebook_session_group.command(name=cli_util.override('data_science.activate_notebook_session.command_name', 'activate'), help=u"""Activates the notebook session. \n[Command Reference](activateNotebookSession)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_notebook_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, notebook_session_id, if_match):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.activate_notebook_session(
        notebook_session_id=notebook_session_id,
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


@job_run_group.command(name=cli_util.override('data_science.cancel_job_run.command_name', 'cancel'), help=u"""Cancels an IN_PROGRESS job run. \n[Command Reference](cancelJobRun)""")
@cli_util.option('--job-run-id', required=True, help=u"""The [OCID] of the job run.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_job_run(ctx, from_json, job_run_id, if_match):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.cancel_job_run(
        job_run_id=job_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_science.cancel_work_request.command_name', 'cancel'), help=u"""Cancels a work request that has not started. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
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
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_science.change_job_compartment.command_name', 'change-compartment'), help=u"""Changes a job's compartment \n[Command Reference](changeJobCompartment)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_job_compartment(ctx, from_json, job_id, compartment_id, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_job_compartment(
        job_id=job_id,
        change_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_run_group.command(name=cli_util.override('data_science.change_job_run_compartment.command_name', 'change-compartment'), help=u"""Changes a job run's compartment \n[Command Reference](changeJobRunCompartment)""")
@cli_util.option('--job-run-id', required=True, help=u"""The [OCID] of the job run.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_job_run_compartment(ctx, from_json, job_run_id, compartment_id, if_match):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_job_run_compartment(
        job_run_id=job_run_id,
        change_job_run_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.change_model_compartment.command_name', 'change-compartment'), help=u"""Moves a model resource into a different compartment. \n[Command Reference](changeModelCompartment)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_model_compartment(ctx, from_json, model_id, compartment_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_model_compartment(
        model_id=model_id,
        change_model_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_deployment_group.command(name=cli_util.override('data_science.change_model_deployment_compartment.command_name', 'change-compartment'), help=u"""Moves a model deployment into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeModelDeploymentCompartment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_model_deployment_compartment(ctx, from_json, model_deployment_id, compartment_id, if_match):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_model_deployment_compartment(
        model_deployment_id=model_deployment_id,
        change_model_deployment_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notebook_session_group.command(name=cli_util.override('data_science.change_notebook_session_compartment.command_name', 'change-compartment'), help=u"""Moves a notebook session resource into a different compartment. \n[Command Reference](changeNotebookSessionCompartment)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_notebook_session_compartment(ctx, from_json, notebook_session_id, compartment_id, if_match):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_notebook_session_compartment(
        notebook_session_id=notebook_session_id,
        change_notebook_session_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_science.change_project_compartment.command_name', 'change-compartment'), help=u"""Moves a project resource into a different compartment. \n[Command Reference](changeProjectCompartment)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_project_compartment(ctx, from_json, project_id, compartment_id, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.change_project_compartment(
        project_id=project_id,
        change_project_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_science.create_job.command_name', 'create'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-infrastructure-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--job-log-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_configuration_details, job_infrastructure_configuration_details, display_name, description, job_log_configuration_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobConfigurationDetails'] = cli_util.parse_json_parameter("job_configuration_details", job_configuration_details)
    _details['jobInfrastructureConfigurationDetails'] = cli_util.parse_json_parameter("job_infrastructure_configuration_details", job_infrastructure_configuration_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if job_log_configuration_details is not None:
        _details['jobLogConfigurationDetails'] = cli_util.parse_json_parameter("job_log_configuration_details", job_log_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.create_job_default_job_configuration_details.command_name', 'create-job-default-job-configuration-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-infrastructure-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--job-log-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-configuration-details-environment-variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Environment variables to set for the job.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-configuration-details-command-line-arguments', help=u"""The arguments to pass to the job.""")
@cli_util.option('--job-configuration-details-maximum-runtime-in-minutes', type=click.INT, help=u"""A time bound for the execution of the job. Timer starts when the job becomes active.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'job-configuration-details-environment-variables': {'module': 'data_science', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'job-configuration-details-environment-variables': {'module': 'data_science', 'class': 'dict(str, string)'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_default_job_configuration_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_infrastructure_configuration_details, display_name, description, job_log_configuration_details, freeform_tags, defined_tags, job_configuration_details_environment_variables, job_configuration_details_command_line_arguments, job_configuration_details_maximum_runtime_in_minutes):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobConfigurationDetails'] = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobInfrastructureConfigurationDetails'] = cli_util.parse_json_parameter("job_infrastructure_configuration_details", job_infrastructure_configuration_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if job_log_configuration_details is not None:
        _details['jobLogConfigurationDetails'] = cli_util.parse_json_parameter("job_log_configuration_details", job_log_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_configuration_details_environment_variables is not None:
        _details['jobConfigurationDetails']['environmentVariables'] = cli_util.parse_json_parameter("job_configuration_details_environment_variables", job_configuration_details_environment_variables)

    if job_configuration_details_command_line_arguments is not None:
        _details['jobConfigurationDetails']['commandLineArguments'] = job_configuration_details_command_line_arguments

    if job_configuration_details_maximum_runtime_in_minutes is not None:
        _details['jobConfigurationDetails']['maximumRuntimeInMinutes'] = job_configuration_details_maximum_runtime_in_minutes

    _details['jobConfigurationDetails']['jobType'] = 'DEFAULT'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.create_job_managed_egress_standalone_job_infrastructure_configuration_details.command_name', 'create-job-managed-egress-standalone-job-infrastructure-configuration-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-infrastructure-configuration-details-shape-name', required=True, help=u"""The shape used to launch the job run instances.""")
@cli_util.option('--job-infrastructure-configuration-details-block-storage-size-in-gbs', required=True, type=click.INT, help=u"""The size of the block storage volume to attach to the instance running the job""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--job-log-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_managed_egress_standalone_job_infrastructure_configuration_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_configuration_details, job_infrastructure_configuration_details_shape_name, job_infrastructure_configuration_details_block_storage_size_in_gbs, display_name, description, job_log_configuration_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobInfrastructureConfigurationDetails'] = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobConfigurationDetails'] = cli_util.parse_json_parameter("job_configuration_details", job_configuration_details)
    _details['jobInfrastructureConfigurationDetails']['shapeName'] = job_infrastructure_configuration_details_shape_name
    _details['jobInfrastructureConfigurationDetails']['blockStorageSizeInGBs'] = job_infrastructure_configuration_details_block_storage_size_in_gbs

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if job_log_configuration_details is not None:
        _details['jobLogConfigurationDetails'] = cli_util.parse_json_parameter("job_log_configuration_details", job_log_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['jobInfrastructureConfigurationDetails']['jobInfrastructureType'] = 'ME_STANDALONE'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.create_job_standalone_job_infrastructure_configuration_details.command_name', 'create-job-standalone-job-infrastructure-configuration-details'), help=u"""Creates a job. \n[Command Reference](createJob)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-infrastructure-configuration-details-shape-name', required=True, help=u"""The shape used to launch the job run instances.""")
@cli_util.option('--job-infrastructure-configuration-details-subnet-id', required=True, help=u"""The subnet to create a secondary vnic in to attach to the instance running the job""")
@cli_util.option('--job-infrastructure-configuration-details-block-storage-size-in-gbs', required=True, type=click.INT, help=u"""The size of the block storage volume to attach to the instance running the job""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--job-log-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-configuration-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job_standalone_job_infrastructure_configuration_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_configuration_details, job_infrastructure_configuration_details_shape_name, job_infrastructure_configuration_details_subnet_id, job_infrastructure_configuration_details_block_storage_size_in_gbs, display_name, description, job_log_configuration_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobInfrastructureConfigurationDetails'] = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobConfigurationDetails'] = cli_util.parse_json_parameter("job_configuration_details", job_configuration_details)
    _details['jobInfrastructureConfigurationDetails']['shapeName'] = job_infrastructure_configuration_details_shape_name
    _details['jobInfrastructureConfigurationDetails']['subnetId'] = job_infrastructure_configuration_details_subnet_id
    _details['jobInfrastructureConfigurationDetails']['blockStorageSizeInGBs'] = job_infrastructure_configuration_details_block_storage_size_in_gbs

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if job_log_configuration_details is not None:
        _details['jobLogConfigurationDetails'] = cli_util.parse_json_parameter("job_log_configuration_details", job_log_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['jobInfrastructureConfigurationDetails']['jobInfrastructureType'] = 'STANDALONE'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job(
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.create_job_artifact.command_name', 'create-job-artifact'), help=u"""Uploads a job artifact. \n[Command Reference](createJobArtifact)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--job-artifact', required=True, help=u"""The job artifact to upload.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--content-disposition', help=u"""This header is for specifying a filename during upload. It is used to identify the file type and validate if the file type is supported. Example: `--content-disposition \"attachment; filename=hello-world.py\"`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_job_artifact(ctx, from_json, job_id, job_artifact, content_length, content_disposition):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if content_disposition is not None:
        kwargs['content_disposition'] = content_disposition
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job_artifact(
        job_id=job_id,
        job_artifact=job_artifact,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_run_group.command(name=cli_util.override('data_science.create_job_run.command_name', 'create'), help=u"""Creates a job run. \n[Command Reference](createJobRun)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job to create a run for.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--job-configuration-override-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-log-configuration-override-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-configuration-override-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-override-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-configuration-override-details': {'module': 'data_science', 'class': 'JobConfigurationDetails'}, 'job-log-configuration-override-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def create_job_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_id, display_name, job_configuration_override_details, job_log_configuration_override_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobId'] = job_id

    if display_name is not None:
        _details['displayName'] = display_name

    if job_configuration_override_details is not None:
        _details['jobConfigurationOverrideDetails'] = cli_util.parse_json_parameter("job_configuration_override_details", job_configuration_override_details)

    if job_log_configuration_override_details is not None:
        _details['jobLogConfigurationOverrideDetails'] = cli_util.parse_json_parameter("job_log_configuration_override_details", job_log_configuration_override_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job_run(
        create_job_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_run') and callable(getattr(client, 'get_job_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_run_group.command(name=cli_util.override('data_science.create_job_run_default_job_configuration_details.command_name', 'create-job-run-default-job-configuration-details'), help=u"""Creates a job run. \n[Command Reference](createJobRun)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate the job with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job to create a run for.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--job-log-configuration-override-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-configuration-override-details-environment-variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Environment variables to set for the job.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--job-configuration-override-details-command-line-arguments', help=u"""The arguments to pass to the job.""")
@cli_util.option('--job-configuration-override-details-maximum-runtime-in-minutes', type=click.INT, help=u"""A time bound for the execution of the job. Timer starts when the job becomes active.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-log-configuration-override-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'job-configuration-override-details-environment-variables': {'module': 'data_science', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-log-configuration-override-details': {'module': 'data_science', 'class': 'JobLogConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'job-configuration-override-details-environment-variables': {'module': 'data_science', 'class': 'dict(str, string)'}}, output_type={'module': 'data_science', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def create_job_run_default_job_configuration_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, job_id, display_name, job_log_configuration_override_details, freeform_tags, defined_tags, job_configuration_override_details_environment_variables, job_configuration_override_details_command_line_arguments, job_configuration_override_details_maximum_runtime_in_minutes):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobConfigurationOverrideDetails'] = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['jobId'] = job_id

    if display_name is not None:
        _details['displayName'] = display_name

    if job_log_configuration_override_details is not None:
        _details['jobLogConfigurationOverrideDetails'] = cli_util.parse_json_parameter("job_log_configuration_override_details", job_log_configuration_override_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if job_configuration_override_details_environment_variables is not None:
        _details['jobConfigurationOverrideDetails']['environmentVariables'] = cli_util.parse_json_parameter("job_configuration_override_details_environment_variables", job_configuration_override_details_environment_variables)

    if job_configuration_override_details_command_line_arguments is not None:
        _details['jobConfigurationOverrideDetails']['commandLineArguments'] = job_configuration_override_details_command_line_arguments

    if job_configuration_override_details_maximum_runtime_in_minutes is not None:
        _details['jobConfigurationOverrideDetails']['maximumRuntimeInMinutes'] = job_configuration_override_details_maximum_runtime_in_minutes

    _details['jobConfigurationOverrideDetails']['jobType'] = 'DEFAULT'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_job_run(
        create_job_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_run') and callable(getattr(client, 'get_job_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('data_science.create_model.command_name', 'create'), help=u"""Creates a new model. \n[Command Reference](createModel)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to create the model in.""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My Model`""")
@cli_util.option('--description', help=u"""A short description of the model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-metadata-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of custom metadata details for the model.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/datascience/20190101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-metadata-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of defined metadata details for the model.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/datascience/20190101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-schema', help=u"""Input schema file content in String format""")
@cli_util.option('--output-schema', help=u"""Output schema file content in String format""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'custom-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}, 'defined-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'custom-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}, 'defined-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}}, output_type={'module': 'data_science', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, project_id, display_name, description, freeform_tags, defined_tags, custom_metadata_list, defined_metadata_list, input_schema, output_schema):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['projectId'] = project_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if custom_metadata_list is not None:
        _details['customMetadataList'] = cli_util.parse_json_parameter("custom_metadata_list", custom_metadata_list)

    if defined_metadata_list is not None:
        _details['definedMetadataList'] = cli_util.parse_json_parameter("defined_metadata_list", defined_metadata_list)

    if input_schema is not None:
        _details['inputSchema'] = input_schema

    if output_schema is not None:
        _details['outputSchema'] = output_schema

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_model(
        create_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_model') and callable(getattr(client, 'get_model')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_model(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('data_science.create_model_artifact.command_name', 'create-model-artifact'), help=u"""Creates model artifact for specified model. \n[Command Reference](createModelArtifact)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--model-artifact', required=True, help=u"""The model artifact to upload.""")
@cli_util.option('--content-length', type=click.INT, help=u"""The content length of the body.""")
@cli_util.option('--content-disposition', help=u"""This header allows you to specify a filename during upload. This file name is used to dispose of the file contents while downloading the file. If this optional field is not populated in the request, then the OCID of the model is used for the file name when downloading. Example: `{\"Content-Disposition\": \"attachment\"            \"filename\"=\"model.tar.gz\"            \"Content-Length\": \"2347\"            \"Content-Type\": \"application/gzip\"}`""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_model_artifact(ctx, from_json, model_id, model_artifact, content_length, content_disposition):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if content_length is not None:
        kwargs['content_length'] = content_length
    if content_disposition is not None:
        kwargs['content_disposition'] = content_disposition
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_model_artifact(
        model_id=model_id,
        model_artifact=model_artifact,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_deployment_group.command(name=cli_util.override('data_science.create_model_deployment.command_name', 'create'), help=u"""Creates a new model deployment. \n[Command Reference](createModelDeployment)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model deployment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the model deployment.""")
@cli_util.option('--model-deployment-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`""")
@cli_util.option('--description', help=u"""A short description of the model deployment.""")
@cli_util.option('--category-log-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-deployment-configuration-details': {'module': 'data_science', 'class': 'ModelDeploymentConfigurationDetails'}, 'category-log-details': {'module': 'data_science', 'class': 'CategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-deployment-configuration-details': {'module': 'data_science', 'class': 'ModelDeploymentConfigurationDetails'}, 'category-log-details': {'module': 'data_science', 'class': 'CategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'ModelDeployment'})
@cli_util.wrap_exceptions
def create_model_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, model_deployment_configuration_details, display_name, description, category_log_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['modelDeploymentConfigurationDetails'] = cli_util.parse_json_parameter("model_deployment_configuration_details", model_deployment_configuration_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if category_log_details is not None:
        _details['categoryLogDetails'] = cli_util.parse_json_parameter("category_log_details", category_log_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_model_deployment(
        create_model_deployment_details=_details,
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


@model_deployment_group.command(name=cli_util.override('data_science.create_model_deployment_single_model_deployment_configuration_details.command_name', 'create-model-deployment-single-model-deployment-configuration-details'), help=u"""Creates a new model deployment. \n[Command Reference](createModelDeployment)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the model deployment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the model deployment.""")
@cli_util.option('--model-deployment-configuration-details-model-configuration-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`""")
@cli_util.option('--description', help=u"""A short description of the model deployment.""")
@cli_util.option('--category-log-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'category-log-details': {'module': 'data_science', 'class': 'CategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'model-deployment-configuration-details-model-configuration-details': {'module': 'data_science', 'class': 'ModelConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'category-log-details': {'module': 'data_science', 'class': 'CategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'model-deployment-configuration-details-model-configuration-details': {'module': 'data_science', 'class': 'ModelConfigurationDetails'}}, output_type={'module': 'data_science', 'class': 'ModelDeployment'})
@cli_util.wrap_exceptions
def create_model_deployment_single_model_deployment_configuration_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, model_deployment_configuration_details_model_configuration_details, display_name, description, category_log_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelDeploymentConfigurationDetails'] = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id
    _details['modelDeploymentConfigurationDetails']['modelConfigurationDetails'] = cli_util.parse_json_parameter("model_deployment_configuration_details_model_configuration_details", model_deployment_configuration_details_model_configuration_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if category_log_details is not None:
        _details['categoryLogDetails'] = cli_util.parse_json_parameter("category_log_details", category_log_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['modelDeploymentConfigurationDetails']['deploymentType'] = 'SINGLE_MODEL'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_model_deployment(
        create_model_deployment_details=_details,
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


@model_group.command(name=cli_util.override('data_science.create_model_provenance.command_name', 'create-model-provenance'), help=u"""Creates provenance information for the specified model. \n[Command Reference](createModelProvenance)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--repository-url', help=u"""For model reproducibility purposes. URL of the git repository associated with model training.""")
@cli_util.option('--git-branch', help=u"""For model reproducibility purposes. Branch of the git repository associated with model training.""")
@cli_util.option('--git-commit', help=u"""For model reproducibility purposes. Commit ID of the git repository associated with model training.""")
@cli_util.option('--script-dir', help=u"""For model reproducibility purposes. Path to model artifacts.""")
@cli_util.option('--training-script', help=u"""For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"""")
@cli_util.option('--training-id', help=u"""The [OCID] of a training session(Job or NotebookSession) in which the model was trained. It is used for model reproducibility purposes.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'ModelProvenance'})
@cli_util.wrap_exceptions
def create_model_provenance(ctx, from_json, model_id, repository_url, git_branch, git_commit, script_dir, training_script, training_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if repository_url is not None:
        _details['repositoryUrl'] = repository_url

    if git_branch is not None:
        _details['gitBranch'] = git_branch

    if git_commit is not None:
        _details['gitCommit'] = git_commit

    if script_dir is not None:
        _details['scriptDir'] = script_dir

    if training_script is not None:
        _details['trainingScript'] = training_script

    if training_id is not None:
        _details['trainingId'] = training_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_model_provenance(
        model_id=model_id,
        create_model_provenance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notebook_session_group.command(name=cli_util.override('data_science.create_notebook_session.command_name', 'create'), help=u"""Creates a new notebook session. \n[Command Reference](createNotebookSession)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project to associate with the notebook session.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the notebook session.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`""")
@cli_util.option('--notebook-session-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--notebook-session-config-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'notebook-session-configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'notebook-session-config-details': {'module': 'data_science', 'class': 'NotebookSessionConfigDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'notebook-session-configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'notebook-session-config-details': {'module': 'data_science', 'class': 'NotebookSessionConfigDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def create_notebook_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, compartment_id, display_name, notebook_session_configuration_details, notebook_session_config_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['projectId'] = project_id
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if notebook_session_configuration_details is not None:
        _details['notebookSessionConfigurationDetails'] = cli_util.parse_json_parameter("notebook_session_configuration_details", notebook_session_configuration_details)

    if notebook_session_config_details is not None:
        _details['notebookSessionConfigDetails'] = cli_util.parse_json_parameter("notebook_session_config_details", notebook_session_config_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_notebook_session(
        create_notebook_session_details=_details,
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


@project_group.command(name=cli_util.override('data_science.create_project.command_name', 'create'), help=u"""Creates a new project. \n[Command Reference](createProject)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to create the project in.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Project'})
@cli_util.wrap_exceptions
def create_project(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.create_project(
        create_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_project') and callable(getattr(client, 'get_project')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_project(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('data_science.deactivate_model.command_name', 'deactivate'), help=u"""Deactivates the model. \n[Command Reference](deactivateModel)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'Model'})
@cli_util.wrap_exceptions
def deactivate_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.deactivate_model(
        model_id=model_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_model') and callable(getattr(client, 'get_model')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_model(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_deployment_group.command(name=cli_util.override('data_science.deactivate_model_deployment.command_name', 'deactivate'), help=u"""Deactivates the model deployment. \n[Command Reference](deactivateModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def deactivate_model_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_deployment_id, if_match):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.deactivate_model_deployment(
        model_deployment_id=model_deployment_id,
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


@notebook_session_group.command(name=cli_util.override('data_science.deactivate_notebook_session.command_name', 'deactivate'), help=u"""Deactivates the notebook session. \n[Command Reference](deactivateNotebookSession)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def deactivate_notebook_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, notebook_session_id, if_match):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.deactivate_notebook_session(
        notebook_session_id=notebook_session_id,
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


@job_group.command(name=cli_util.override('data_science.delete_job.command_name', 'delete'), help=u"""Deletes a job. \n[Command Reference](deleteJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--delete-related-job-runs', type=click.BOOL, help=u"""Delete all JobRuns associated with this job.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, if_match, delete_related_job_runs):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if delete_related_job_runs is not None:
        kwargs['delete_related_job_runs'] = delete_related_job_runs
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.delete_job(
        job_id=job_id,
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


@job_run_group.command(name=cli_util.override('data_science.delete_job_run.command_name', 'delete'), help=u"""Deletes a job run. \n[Command Reference](deleteJobRun)""")
@cli_util.option('--job-run-id', required=True, help=u"""The [OCID] of the job run.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, job_run_id, if_match):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.delete_job_run(
        job_run_id=job_run_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_run') and callable(getattr(client, 'get_job_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_job_run(job_run_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('data_science.delete_model.command_name', 'delete'), help=u"""Deletes the specified model. \n[Command Reference](deleteModel)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.delete_model(
        model_id=model_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_model') and callable(getattr(client, 'get_model')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_model(model_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@model_deployment_group.command(name=cli_util.override('data_science.delete_model_deployment.command_name', 'delete'), help=u"""Deletes the specified model deployment. Any unsaved work in this model deployment is lost. \n[Command Reference](deleteModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_model_deployment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_deployment_id, if_match):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.delete_model_deployment(
        model_deployment_id=model_deployment_id,
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


@notebook_session_group.command(name=cli_util.override('data_science.delete_notebook_session.command_name', 'delete'), help=u"""Deletes the specified notebook session. Any unsaved work in this notebook session are lost. \n[Command Reference](deleteNotebookSession)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_notebook_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, notebook_session_id, if_match):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.delete_notebook_session(
        notebook_session_id=notebook_session_id,
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


@project_group.command(name=cli_util.override('data_science.delete_project.command_name', 'delete'), help=u"""Deletes the specified project. This operation fails unless all associated resources (notebook sessions or models) are in a DELETED state. You must delete all associated resources before deleting a project. \n[Command Reference](deleteProject)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
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
    client = cli_util.build_client('data_science', 'data_science', ctx)
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


@job_group.command(name=cli_util.override('data_science.get_job.command_name', 'get'), help=u"""Gets a job. \n[Command Reference](getJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def get_job(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_job(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_science.get_job_artifact_content.command_name', 'get-job-artifact-content'), help=u"""Downloads job artifact content for specified job. \n[Command Reference](getJobArtifactContent)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--range', help=u"""Optional byte range to fetch, as described in [RFC 7233], section 2.1. Note that only a single range of bytes is supported.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_job_artifact_content(ctx, from_json, file, job_id, range):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    if range is not None:
        kwargs['range'] = range
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_job_artifact_content(
        job_id=job_id,
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


@job_run_group.command(name=cli_util.override('data_science.get_job_run.command_name', 'get'), help=u"""Gets a job run. \n[Command Reference](getJobRun)""")
@cli_util.option('--job-run-id', required=True, help=u"""The [OCID] of the job run.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def get_job_run(ctx, from_json, job_run_id):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_job_run(
        job_run_id=job_run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.get_model.command_name', 'get'), help=u"""Gets the specified model's information. \n[Command Reference](getModel)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'Model'})
@cli_util.wrap_exceptions
def get_model(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_model(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.get_model_artifact_content.command_name', 'get-model-artifact-content'), help=u"""Downloads model artifact content for specified model. \n[Command Reference](getModelArtifactContent)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--range', help=u"""Optional byte range to fetch, as described in [RFC 7233], section 2.1. Note that only a single range of bytes is supported.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_model_artifact_content(ctx, from_json, file, model_id, range):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if range is not None:
        kwargs['range'] = range
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_model_artifact_content(
        model_id=model_id,
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


@model_deployment_group.command(name=cli_util.override('data_science.get_model_deployment.command_name', 'get'), help=u"""Retrieves the model deployment for the specified `modelDeploymentId`. \n[Command Reference](getModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'ModelDeployment'})
@cli_util.wrap_exceptions
def get_model_deployment(ctx, from_json, model_deployment_id):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_model_deployment(
        model_deployment_id=model_deployment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.get_model_provenance.command_name', 'get-model-provenance'), help=u"""Gets provenance information for specified model. \n[Command Reference](getModelProvenance)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'ModelProvenance'})
@cli_util.wrap_exceptions
def get_model_provenance(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_model_provenance(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notebook_session_group.command(name=cli_util.override('data_science.get_notebook_session.command_name', 'get'), help=u"""Gets the specified notebook session's information. \n[Command Reference](getNotebookSession)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def get_notebook_session(ctx, from_json, notebook_session_id):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_notebook_session(
        notebook_session_id=notebook_session_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_science.get_project.command_name', 'get'), help=u"""Gets the specified project's information. \n[Command Reference](getProject)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, project_id):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_project(
        project_id=project_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_science.get_work_request.command_name', 'get'), help=u"""Gets the specified work request's information. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_science.head_job_artifact.command_name', 'head-job-artifact'), help=u"""Gets job artifact metadata. \n[Command Reference](headJobArtifact)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_job_artifact(ctx, from_json, job_id):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.head_job_artifact(
        job_id=job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.head_model_artifact.command_name', 'head-model-artifact'), help=u"""Gets model artifact metadata for specified model. \n[Command Reference](headModelArtifact)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def head_model_artifact(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.head_model_artifact(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fast_launch_job_config_group.command(name=cli_util.override('data_science.list_fast_launch_job_configs.command_name', 'list'), help=u"""List fast launch capable job configs in the specified compartment. \n[Command Reference](listFastLaunchJobConfigs)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[FastLaunchJobConfigSummary]'})
@cli_util.wrap_exceptions
def list_fast_launch_job_configs(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fast_launch_job_configs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fast_launch_job_configs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_fast_launch_job_configs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_run_group.command(name=cli_util.override('data_science.list_job_runs.command_name', 'list'), help=u"""List out job runs. \n[Command Reference](listJobRuns)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--job-id', help=u"""The [OCID] of the job.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "NEEDS_ATTENTION"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[JobRunSummary]'})
@cli_util.wrap_exceptions
def list_job_runs(ctx, from_json, all_pages, page_size, compartment_id, id, job_id, created_by, display_name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if job_id is not None:
        kwargs['job_id'] = job_id
    if created_by is not None:
        kwargs['created_by'] = created_by
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
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_runs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_runs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_job_runs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_shape_group.command(name=cli_util.override('data_science.list_job_shapes.command_name', 'list'), help=u"""List job shapes available in the specified compartment. \n[Command Reference](listJobShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[JobShapeSummary]'})
@cli_util.wrap_exceptions
def list_job_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_job_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_science.list_jobs.command_name', 'list'), help=u"""List jobs in the specified compartment. \n[Command Reference](listJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--project-id', help=u"""<b>Filter</b> results by the [OCID] of the project.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid   state for the resource type.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[JobSummary]'})
@cli_util.wrap_exceptions
def list_jobs(ctx, from_json, all_pages, page_size, compartment_id, project_id, id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if project_id is not None:
        kwargs['project_id'] = project_id
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_jobs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_jobs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_deployment_shape_group.command(name=cli_util.override('data_science.list_model_deployment_shapes.command_name', 'list'), help=u"""Lists the valid model deployment shapes. \n[Command Reference](listModelDeploymentShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[ModelDeploymentShapeSummary]'})
@cli_util.wrap_exceptions
def list_model_deployment_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_model_deployment_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_model_deployment_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_model_deployment_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_deployment_group.command(name=cli_util.override('data_science.list_model_deployments.command_name', 'list'), help=u"""Lists all model deployments in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must include compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned. \n[Command Reference](listModelDeployments)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--project-id', help=u"""<b>Filter</b> results by the [OCID] of the project.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "INACTIVE", "UPDATING", "DELETED", "NEEDS_ATTENTION"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, results are shown in descending order. When you sort by `displayName`, results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[ModelDeploymentSummary]'})
@cli_util.wrap_exceptions
def list_model_deployments(ctx, from_json, all_pages, page_size, compartment_id, id, project_id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_model_deployments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_model_deployments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_model_deployments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('data_science.list_models.command_name', 'list'), help=u"""Lists models in the specified compartment. \n[Command Reference](listModels)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--project-id', help=u"""<b>Filter</b> results by the [OCID] of the project.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "lifecycleState"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. All other fields default to ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[ModelSummary]'})
@cli_util.wrap_exceptions
def list_models(ctx, from_json, all_pages, page_size, compartment_id, id, project_id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_models,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_models,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_models(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@notebook_session_shape_group.command(name=cli_util.override('data_science.list_notebook_session_shapes.command_name', 'list'), help=u"""Lists the valid notebook session shapes. \n[Command Reference](listNotebookSessionShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[NotebookSessionShapeSummary]'})
@cli_util.wrap_exceptions
def list_notebook_session_shapes(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_notebook_session_shapes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_notebook_session_shapes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_notebook_session_shapes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@notebook_session_group.command(name=cli_util.override('data_science.list_notebook_sessions.command_name', 'list'), help=u"""Lists the notebook sessions in the specified compartment. \n[Command Reference](listNotebookSessions)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--project-id', help=u"""<b>Filter</b> results by the [OCID] of the project.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[NotebookSessionSummary]'})
@cli_util.wrap_exceptions
def list_notebook_sessions(ctx, from_json, all_pages, page_size, compartment_id, id, project_id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if project_id is not None:
        kwargs['project_id'] = project_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_notebook_sessions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_notebook_sessions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_notebook_sessions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_science.list_projects.command_name', 'list'), help=u"""Lists projects in the specified compartment. \n[Command Reference](listProjects)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--display-name', help=u"""<b>Filter</b> results by its user-friendly name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), help=u"""<b>Filter</b> results by the specified lifecycle state. Must be a valid state for the resource type.""")
@cli_util.option('--created-by', help=u"""<b>Filter</b> results by the [OCID] of the user who created the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by `timeCreated`, the results are shown in descending order. When you sort by `displayName`, the results are shown in ascending order. Sort order for the `displayName` field is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[ProjectSummary]'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, compartment_id, id, display_name, lifecycle_state, created_by, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if created_by is not None:
        kwargs['created_by'] = created_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
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


@work_request_group.command(name=cli_util.override('data_science.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Lists work request errors for the specified work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.list_work_request_errors(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_science.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists work request logs for the specified work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.list_work_request_logs(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_science.list_work_requests.command_name', 'list'), help=u"""Lists work requests in the specified compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""<b>Filter</b> results by the [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""<b>Filter</b> results by [OCID]. Must be an OCID of the correct type for the resource type.""")
@cli_util.option('--operation-type', type=custom_types.CliCaseInsensitiveChoice(["NOTEBOOK_SESSION_CREATE", "NOTEBOOK_SESSION_DELETE", "NOTEBOOK_SESSION_ACTIVATE", "NOTEBOOK_SESSION_DEACTIVATE", "MODEL_DEPLOYMENT_CREATE", "MODEL_DEPLOYMENT_DELETE", "MODEL_DEPLOYMENT_ACTIVATE", "MODEL_DEPLOYMENT_DEACTIVATE", "MODEL_DEPLOYMENT_UPDATE", "PROJECT_DELETE", "WORKREQUEST_CANCEL", "JOB_DELETE"]), help=u"""<b>Filter</b> results by the type of the operation associated with the work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""<b>Filter</b> results by work request status.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. See [List Pagination].

Example: `500`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call.

See [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["operationType", "status", "timeAccepted"]), help=u"""Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, the results are shown in descending order. All other fields default to ascending order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, id, operation_type, status, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if operation_type is not None:
        kwargs['operation_type'] = operation_type
    if status is not None:
        kwargs['status'] = status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_science', 'data_science', ctx)
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


@job_group.command(name=cli_util.override('data_science.update_job.command_name', 'update'), help=u"""Updates a job. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--job-infrastructure-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'job-infrastructure-configuration-details': {'module': 'data_science', 'class': 'JobInfrastructureConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, display_name, description, job_infrastructure_configuration_details, freeform_tags, defined_tags, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if job_infrastructure_configuration_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to job-infrastructure-configuration-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if job_infrastructure_configuration_details is not None:
        _details['jobInfrastructureConfigurationDetails'] = cli_util.parse_json_parameter("job_infrastructure_configuration_details", job_infrastructure_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.update_job_managed_egress_standalone_job_infrastructure_configuration_details.command_name', 'update-job-managed-egress-standalone-job-infrastructure-configuration-details'), help=u"""Updates a job. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--job-infrastructure-configuration-details-shape-name', required=True, help=u"""The shape used to launch the job run instances.""")
@cli_util.option('--job-infrastructure-configuration-details-block-storage-size-in-gbs', required=True, type=click.INT, help=u"""The size of the block storage volume to attach to the instance running the job""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_managed_egress_standalone_job_infrastructure_configuration_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, job_infrastructure_configuration_details_shape_name, job_infrastructure_configuration_details_block_storage_size_in_gbs, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobInfrastructureConfigurationDetails'] = {}
    _details['jobInfrastructureConfigurationDetails']['shapeName'] = job_infrastructure_configuration_details_shape_name
    _details['jobInfrastructureConfigurationDetails']['blockStorageSizeInGBs'] = job_infrastructure_configuration_details_block_storage_size_in_gbs

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['jobInfrastructureConfigurationDetails']['jobInfrastructureType'] = 'ME_STANDALONE'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_science.update_job_standalone_job_infrastructure_configuration_details.command_name', 'update-job-standalone-job-infrastructure-configuration-details'), help=u"""Updates a job. \n[Command Reference](updateJob)""")
@cli_util.option('--job-id', required=True, help=u"""The [OCID] of the job.""")
@cli_util.option('--job-infrastructure-configuration-details-shape-name', required=True, help=u"""The shape used to launch the job run instances.""")
@cli_util.option('--job-infrastructure-configuration-details-subnet-id', required=True, help=u"""The subnet to create a secondary vnic in to attach to the instance running the job""")
@cli_util.option('--job-infrastructure-configuration-details-block-storage-size-in-gbs', required=True, type=click.INT, help=u"""The size of the block storage volume to attach to the instance running the job""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "FAILED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job_standalone_job_infrastructure_configuration_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_id, job_infrastructure_configuration_details_shape_name, job_infrastructure_configuration_details_subnet_id, job_infrastructure_configuration_details_block_storage_size_in_gbs, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(job_id, six.string_types) and len(job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['jobInfrastructureConfigurationDetails'] = {}
    _details['jobInfrastructureConfigurationDetails']['shapeName'] = job_infrastructure_configuration_details_shape_name
    _details['jobInfrastructureConfigurationDetails']['subnetId'] = job_infrastructure_configuration_details_subnet_id
    _details['jobInfrastructureConfigurationDetails']['blockStorageSizeInGBs'] = job_infrastructure_configuration_details_block_storage_size_in_gbs

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['jobInfrastructureConfigurationDetails']['jobInfrastructureType'] = 'STANDALONE'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_job(
        job_id=job_id,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_run_group.command(name=cli_util.override('data_science.update_job_run.command_name', 'update'), help=u"""Updates a job run. \n[Command Reference](updateJobRun)""")
@cli_util.option('--job-run-id', required=True, help=u"""The [OCID] of the job run.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "NEEDS_ATTENTION"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'JobRun'})
@cli_util.wrap_exceptions
def update_job_run(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, job_run_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(job_run_id, six.string_types) and len(job_run_id.strip()) == 0:
        raise click.UsageError('Parameter --job-run-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_job_run(
        job_run_id=job_run_id,
        update_job_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_run') and callable(getattr(client, 'get_job_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('data_science.update_model.command_name', 'update'), help=u"""Updates the properties of a model. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties. \n[Command Reference](updateModel)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.  Example: `My Model`""")
@cli_util.option('--description', help=u"""A short description of the model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-metadata-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of custom metadata details for the model.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/datascience/20190101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-metadata-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of defined metadata details for the model.

This option is a JSON list with items of type Metadata.  For documentation on Metadata please see our API reference: https://docs.cloud.oracle.com/api/#/en/datascience/20190101/datatypes/Metadata.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "FAILED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'custom-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}, 'defined-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'custom-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}, 'defined-metadata-list': {'module': 'data_science', 'class': 'list[Metadata]'}}, output_type={'module': 'data_science', 'class': 'Model'})
@cli_util.wrap_exceptions
def update_model(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, display_name, description, freeform_tags, defined_tags, custom_metadata_list, defined_metadata_list, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or custom_metadata_list or defined_metadata_list:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and custom-metadata-list and defined-metadata-list will replace any existing values. Are you sure you want to continue?"):
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if custom_metadata_list is not None:
        _details['customMetadataList'] = cli_util.parse_json_parameter("custom_metadata_list", custom_metadata_list)

    if defined_metadata_list is not None:
        _details['definedMetadataList'] = cli_util.parse_json_parameter("defined_metadata_list", defined_metadata_list)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_model(
        model_id=model_id,
        update_model_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_model') and callable(getattr(client, 'get_model')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_model(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_deployment_group.command(name=cli_util.override('data_science.update_model_deployment.command_name', 'update'), help=u"""Updates the properties of a model deployment. Some of the properties of `modelDeploymentConfigurationDetails` or `CategoryLogDetails` can also be updated with zero down time when the model deployment's lifecycle state is ACTIVE or NEEDS_ATTENTION i.e `instanceShapeName`, `instanceCount` and `modelId`, separately `loadBalancerShape` or `CategoryLogDetails` can also be updated independently. All of the fields can be updated when the deployment is in the INACTIVE lifecycle state. Changes will take effect the next time the model deployment is activated. \n[Command Reference](updateModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`""")
@cli_util.option('--description', help=u"""A short description of the model deployment.""")
@cli_util.option('--model-deployment-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--category-log-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-deployment-configuration-details': {'module': 'data_science', 'class': 'UpdateModelDeploymentConfigurationDetails'}, 'category-log-details': {'module': 'data_science', 'class': 'UpdateCategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-deployment-configuration-details': {'module': 'data_science', 'class': 'UpdateModelDeploymentConfigurationDetails'}, 'category-log-details': {'module': 'data_science', 'class': 'UpdateCategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_model_deployment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_deployment_id, display_name, description, model_deployment_configuration_details, category_log_details, freeform_tags, defined_tags, if_match):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')
    if not force:
        if model_deployment_configuration_details or category_log_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to model-deployment-configuration-details and category-log-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if model_deployment_configuration_details is not None:
        _details['modelDeploymentConfigurationDetails'] = cli_util.parse_json_parameter("model_deployment_configuration_details", model_deployment_configuration_details)

    if category_log_details is not None:
        _details['categoryLogDetails'] = cli_util.parse_json_parameter("category_log_details", category_log_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_model_deployment(
        model_deployment_id=model_deployment_id,
        update_model_deployment_details=_details,
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


@model_deployment_group.command(name=cli_util.override('data_science.update_model_deployment_update_single_model_deployment_configuration_details.command_name', 'update-model-deployment-update-single-model-deployment-configuration-details'), help=u"""Updates the properties of a model deployment. Some of the properties of `modelDeploymentConfigurationDetails` or `CategoryLogDetails` can also be updated with zero down time when the model deployment's lifecycle state is ACTIVE or NEEDS_ATTENTION i.e `instanceShapeName`, `instanceCount` and `modelId`, separately `loadBalancerShape` or `CategoryLogDetails` can also be updated independently. All of the fields can be updated when the deployment is in the INACTIVE lifecycle state. Changes will take effect the next time the model deployment is activated. \n[Command Reference](updateModelDeployment)""")
@cli_util.option('--model-deployment-id', required=True, help=u"""The [OCID] of the model deployment.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. Does not have to be unique, and can be modified. Avoid entering confidential information. Example: `My ModelDeployment`""")
@cli_util.option('--description', help=u"""A short description of the model deployment.""")
@cli_util.option('--category-log-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--model-deployment-configuration-details-model-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'category-log-details': {'module': 'data_science', 'class': 'UpdateCategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'model-deployment-configuration-details-model-configuration-details': {'module': 'data_science', 'class': 'UpdateModelConfigurationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'category-log-details': {'module': 'data_science', 'class': 'UpdateCategoryLogDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}, 'model-deployment-configuration-details-model-configuration-details': {'module': 'data_science', 'class': 'UpdateModelConfigurationDetails'}})
@cli_util.wrap_exceptions
def update_model_deployment_update_single_model_deployment_configuration_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_deployment_id, display_name, description, category_log_details, freeform_tags, defined_tags, if_match, model_deployment_configuration_details_model_configuration_details):

    if isinstance(model_deployment_id, six.string_types) and len(model_deployment_id.strip()) == 0:
        raise click.UsageError('Parameter --model-deployment-id cannot be whitespace or empty string')
    if not force:
        if category_log_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to category-log-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelDeploymentConfigurationDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if category_log_details is not None:
        _details['categoryLogDetails'] = cli_util.parse_json_parameter("category_log_details", category_log_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if model_deployment_configuration_details_model_configuration_details is not None:
        _details['modelDeploymentConfigurationDetails']['modelConfigurationDetails'] = cli_util.parse_json_parameter("model_deployment_configuration_details_model_configuration_details", model_deployment_configuration_details_model_configuration_details)

    _details['modelDeploymentConfigurationDetails']['deploymentType'] = 'SINGLE_MODEL'

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_model_deployment(
        model_deployment_id=model_deployment_id,
        update_model_deployment_details=_details,
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


@model_group.command(name=cli_util.override('data_science.update_model_provenance.command_name', 'update-model-provenance'), help=u"""Updates the provenance information for the specified model. \n[Command Reference](updateModelProvenance)""")
@cli_util.option('--model-id', required=True, help=u"""The [OCID] of the model.""")
@cli_util.option('--repository-url', help=u"""For model reproducibility purposes. URL of the git repository associated with model training.""")
@cli_util.option('--git-branch', help=u"""For model reproducibility purposes. Branch of the git repository associated with model training.""")
@cli_util.option('--git-commit', help=u"""For model reproducibility purposes. Commit ID of the git repository associated with model training.""")
@cli_util.option('--script-dir', help=u"""For model reproducibility purposes. Path to model artifacts.""")
@cli_util.option('--training-script', help=u"""For model reproducibility purposes. Path to the python script or notebook in which the model was trained.\"""")
@cli_util.option('--training-id', help=u"""The [OCID] of a training session(Job or NotebookSession) in which the model was trained. It is used for model reproducibility purposes.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_science', 'class': 'ModelProvenance'})
@cli_util.wrap_exceptions
def update_model_provenance(ctx, from_json, model_id, repository_url, git_branch, git_commit, script_dir, training_script, training_id, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if repository_url is not None:
        _details['repositoryUrl'] = repository_url

    if git_branch is not None:
        _details['gitBranch'] = git_branch

    if git_commit is not None:
        _details['gitCommit'] = git_commit

    if script_dir is not None:
        _details['scriptDir'] = script_dir

    if training_script is not None:
        _details['trainingScript'] = training_script

    if training_id is not None:
        _details['trainingId'] = training_id

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_model_provenance(
        model_id=model_id,
        update_model_provenance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notebook_session_group.command(name=cli_util.override('data_science.update_notebook_session.command_name', 'update'), help=u"""Updates the properties of a notebook session. You can update the `displayName`, `freeformTags`, and `definedTags` properties. When the notebook session is in the INACTIVE lifecycle state, you can update `notebookSessionConfigurationDetails` and change `shape`, `subnetId`, and `blockStorageSizeInGBs`. Changes to the `notebookSessionConfigurationDetails` take effect the next time the `ActivateNotebookSession` action is invoked on the notebook session resource. \n[Command Reference](updateNotebookSession)""")
@cli_util.option('--notebook-session-id', required=True, help=u"""The [OCID] of the notebook session.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information. Example: `My NotebookSession`""")
@cli_util.option('--notebook-session-configuration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "INACTIVE", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'notebook-session-configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'notebook-session-configuration-details': {'module': 'data_science', 'class': 'NotebookSessionConfigurationDetails'}, 'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'NotebookSession'})
@cli_util.wrap_exceptions
def update_notebook_session(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, notebook_session_id, display_name, notebook_session_configuration_details, freeform_tags, defined_tags, if_match):

    if isinstance(notebook_session_id, six.string_types) and len(notebook_session_id.strip()) == 0:
        raise click.UsageError('Parameter --notebook-session-id cannot be whitespace or empty string')
    if not force:
        if notebook_session_configuration_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to notebook-session-configuration-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if notebook_session_configuration_details is not None:
        _details['notebookSessionConfigurationDetails'] = cli_util.parse_json_parameter("notebook_session_configuration_details", notebook_session_configuration_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_notebook_session(
        notebook_session_id=notebook_session_id,
        update_notebook_session_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_notebook_session') and callable(getattr(client, 'get_notebook_session')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_notebook_session(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@project_group.command(name=cli_util.override('data_science.update_project.command_name', 'update'), help=u"""Updates the properties of a project. You can update the `displayName`, `description`, `freeformTags`, and `definedTags` properties. \n[Command Reference](updateProject)""")
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource. It does not have to be unique and can be modified. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A short description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the `etag` you provide matches the resource's current `etag` value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_science', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_science', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_science', 'class': 'Project'})
@cli_util.wrap_exceptions
def update_project(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, project_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')
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

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_science', 'data_science', ctx)
    result = client.update_project(
        project_id=project_id,
        update_project_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_project') and callable(getattr(client, 'get_project')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_project(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
