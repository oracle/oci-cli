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


@cli.command(cli_util.override('speech.speech_root_group.command_name', 'speech'), cls=CommandGroupWithAlias, help=cli_util.override('speech.speech_root_group.help', """The OCI Speech Service harnesses the power of spoken language by allowing developers to easily convert file-based data containing human speech into highly accurate text transcriptions."""), short_help=cli_util.override('speech.speech_root_group.short_help', """Speech API"""))
@cli_util.help_option_group
def speech_root_group():
    pass


@click.command(cli_util.override('speech.transcription_task_group.command_name', 'transcription-task'), cls=CommandGroupWithAlias, help="""Description of Transcription Task.""")
@cli_util.help_option_group
def transcription_task_group():
    pass


@click.command(cli_util.override('speech.transcription_job_group.command_name', 'transcription-job'), cls=CommandGroupWithAlias, help="""Description of Transcription Job.""")
@cli_util.help_option_group
def transcription_job_group():
    pass


speech_root_group.add_command(transcription_task_group)
speech_root_group.add_command(transcription_job_group)


@transcription_job_group.command(name=cli_util.override('speech.cancel_transcription_job.command_name', 'cancel'), help=u"""Canceling the job cancels all the tasks under it. \n[Command Reference](cancelTranscriptionJob)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_transcription_job(ctx, from_json, transcription_job_id, if_match):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.cancel_transcription_job(
        transcription_job_id=transcription_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transcription_task_group.command(name=cli_util.override('speech.cancel_transcription_task.command_name', 'cancel'), help=u"""Cancel Transcription Task \n[Command Reference](cancelTranscriptionTask)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--transcription-task-id', required=True, help=u"""Unique Transcription Task identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_transcription_task(ctx, from_json, transcription_job_id, transcription_task_id, if_match):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    if isinstance(transcription_task_id, six.string_types) and len(transcription_task_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-task-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.cancel_transcription_task(
        transcription_job_id=transcription_job_id,
        transcription_task_id=transcription_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transcription_job_group.command(name=cli_util.override('speech.change_transcription_job_compartment.command_name', 'change-compartment'), help=u"""Moves a transcription Job resource into a different compartment. \n[Command Reference](changeTranscriptionJobCompartment)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_transcription_job_compartment(ctx, from_json, transcription_job_id, compartment_id, if_match):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.change_transcription_job_compartment(
        transcription_job_id=transcription_job_id,
        change_transcription_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transcription_job_group.command(name=cli_util.override('speech.create_transcription_job.command_name', 'create'), help=u"""Creates a new Transcription Job. \n[Command Reference](createTranscriptionJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--input-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the job.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--additional-transcription-formats', type=custom_types.CliCaseInsensitiveChoice(["SRT"]), help=u"""Transcription Format. By default JSON format will be considered.""")
@cli_util.option('--model-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--normalization', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'input-location': {'module': 'ai_speech', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'input-location': {'module': 'ai_speech', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJob'})
@cli_util.wrap_exceptions
def create_transcription_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, input_location, output_location, display_name, description, additional_transcription_formats, model_details, normalization, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['inputLocation'] = cli_util.parse_json_parameter("input_location", input_location)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if additional_transcription_formats is not None:
        _details['additionalTranscriptionFormats'] = cli_util.parse_json_parameter("additional_transcription_formats", additional_transcription_formats)

    if model_details is not None:
        _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)

    if normalization is not None:
        _details['normalization'] = cli_util.parse_json_parameter("normalization", normalization)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.create_transcription_job(
        create_transcription_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transcription_job') and callable(getattr(client, 'get_transcription_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transcription_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@transcription_job_group.command(name=cli_util.override('speech.create_transcription_job_object_list_file_input_location.command_name', 'create-transcription-job-object-list-file-input-location'), help=u"""Creates a new Transcription Job. \n[Command Reference](createTranscriptionJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-object-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the job.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--additional-transcription-formats', type=custom_types.CliCaseInsensitiveChoice(["SRT"]), help=u"""Transcription Format. By default JSON format will be considered.""")
@cli_util.option('--model-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--normalization', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}, 'input-location-object-location': {'module': 'ai_speech', 'class': 'ObjectLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}, 'input-location-object-location': {'module': 'ai_speech', 'class': 'ObjectLocation'}}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJob'})
@cli_util.wrap_exceptions
def create_transcription_job_object_list_file_input_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, output_location, input_location_object_location, display_name, description, additional_transcription_formats, model_details, normalization, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['compartmentId'] = compartment_id
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['inputLocation']['objectLocation'] = cli_util.parse_json_parameter("input_location_object_location", input_location_object_location)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if additional_transcription_formats is not None:
        _details['additionalTranscriptionFormats'] = cli_util.parse_json_parameter("additional_transcription_formats", additional_transcription_formats)

    if model_details is not None:
        _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)

    if normalization is not None:
        _details['normalization'] = cli_util.parse_json_parameter("normalization", normalization)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['inputLocation']['locationType'] = 'OBJECT_LIST_FILE_INPUT_LOCATION'

    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.create_transcription_job(
        create_transcription_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transcription_job') and callable(getattr(client, 'get_transcription_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transcription_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@transcription_job_group.command(name=cli_util.override('speech.create_transcription_job_object_list_inline_input_location.command_name', 'create-transcription-job-object-list-inline-input-location'), help=u"""Creates a new Transcription Job. \n[Command Reference](createTranscriptionJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the job.""")
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-object-locations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of ObjectLocations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the job.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--additional-transcription-formats', type=custom_types.CliCaseInsensitiveChoice(["SRT"]), help=u"""Transcription Format. By default JSON format will be considered.""")
@cli_util.option('--model-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--normalization', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}, 'input-location-object-locations': {'module': 'ai_speech', 'class': 'list[ObjectLocation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'model-details': {'module': 'ai_speech', 'class': 'TranscriptionModelDetails'}, 'normalization': {'module': 'ai_speech', 'class': 'TranscriptionNormalization'}, 'output-location': {'module': 'ai_speech', 'class': 'OutputLocation'}, 'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}, 'input-location-object-locations': {'module': 'ai_speech', 'class': 'list[ObjectLocation]'}}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJob'})
@cli_util.wrap_exceptions
def create_transcription_job_object_list_inline_input_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, output_location, input_location_object_locations, display_name, description, additional_transcription_formats, model_details, normalization, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['compartmentId'] = compartment_id
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['inputLocation']['objectLocations'] = cli_util.parse_json_parameter("input_location_object_locations", input_location_object_locations)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if additional_transcription_formats is not None:
        _details['additionalTranscriptionFormats'] = cli_util.parse_json_parameter("additional_transcription_formats", additional_transcription_formats)

    if model_details is not None:
        _details['modelDetails'] = cli_util.parse_json_parameter("model_details", model_details)

    if normalization is not None:
        _details['normalization'] = cli_util.parse_json_parameter("normalization", normalization)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['inputLocation']['locationType'] = 'OBJECT_LIST_INLINE_INPUT_LOCATION'

    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.create_transcription_job(
        create_transcription_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transcription_job') and callable(getattr(client, 'get_transcription_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transcription_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@transcription_job_group.command(name=cli_util.override('speech.get_transcription_job.command_name', 'get'), help=u"""Gets a Transcription Job by identifier \n[Command Reference](getTranscriptionJob)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJob'})
@cli_util.wrap_exceptions
def get_transcription_job(ctx, from_json, transcription_job_id):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.get_transcription_job(
        transcription_job_id=transcription_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transcription_task_group.command(name=cli_util.override('speech.get_transcription_task.command_name', 'get'), help=u"""Gets a Transcription Task by identifier \n[Command Reference](getTranscriptionTask)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--transcription-task-id', required=True, help=u"""Unique Transcription Task identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_speech', 'class': 'TranscriptionTask'})
@cli_util.wrap_exceptions
def get_transcription_task(ctx, from_json, transcription_job_id, transcription_task_id):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    if isinstance(transcription_task_id, six.string_types) and len(transcription_task_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-task-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.get_transcription_task(
        transcription_job_id=transcription_job_id,
        transcription_task_id=transcription_task_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@transcription_job_group.command(name=cli_util.override('speech.list_transcription_jobs.command_name', 'list'), help=u"""Returns a list of Transcription Jobs. \n[Command Reference](listTranscriptionJobs)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Unique identifier(OCID).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJobCollection'})
@cli_util.wrap_exceptions
def list_transcription_jobs(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
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
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_transcription_jobs,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_transcription_jobs,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_transcription_jobs(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@transcription_task_group.command(name=cli_util.override('speech.list_transcription_tasks.command_name', 'list'), help=u"""Returns a list of Transcription Tasks. \n[Command Reference](listTranscriptionTasks)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Unique identifier(OCID).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_speech', 'class': 'TranscriptionTaskCollection'})
@cli_util.wrap_exceptions
def list_transcription_tasks(ctx, from_json, all_pages, page_size, transcription_job_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')

    kwargs = {}
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
    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_transcription_tasks,
            transcription_job_id=transcription_job_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_transcription_tasks,
            limit,
            page_size,
            transcription_job_id=transcription_job_id,
            **kwargs
        )
    else:
        result = client.list_transcription_tasks(
            transcription_job_id=transcription_job_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@transcription_job_group.command(name=cli_util.override('speech.update_transcription_job.command_name', 'update'), help=u"""Updates the Transcription Job \n[Command Reference](updateTranscriptionJob)""")
@cli_util.option('--transcription-job-id', required=True, help=u"""Unique Transcription Job identifier.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the job.""")
@cli_util.option('--description', help=u"""A short description of the job.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_speech', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_speech', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_speech', 'class': 'TranscriptionJob'})
@cli_util.wrap_exceptions
def update_transcription_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, transcription_job_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(transcription_job_id, six.string_types) and len(transcription_job_id.strip()) == 0:
        raise click.UsageError('Parameter --transcription-job-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('ai_speech', 'ai_service_speech', ctx)
    result = client.update_transcription_job(
        transcription_job_id=transcription_job_id,
        update_transcription_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_transcription_job') and callable(getattr(client, 'get_transcription_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_transcription_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
