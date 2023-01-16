# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('ai_document.ai_document_root_group.command_name', 'ai-document'), cls=CommandGroupWithAlias, help=cli_util.override('ai_document.ai_document_root_group.help', """Document AI helps customers perform various analysis on their documents. If a customer has lots of documents, they can process them in batch using asynchronous API endpoints."""), short_help=cli_util.override('ai_document.ai_document_root_group.short_help', """Document Understanding API"""))
@cli_util.help_option_group
def ai_document_root_group():
    pass


@click.command(cli_util.override('ai_document.processor_job_group.command_name', 'processor-job'), cls=CommandGroupWithAlias, help="""Details of a processor job.""")
@cli_util.help_option_group
def processor_job_group():
    pass


ai_document_root_group.add_command(processor_job_group)


@processor_job_group.command(name=cli_util.override('ai_document.cancel_processor_job.command_name', 'cancel'), help=u"""Cancel a processor job. \n[Command Reference](cancelProcessorJob)""")
@cli_util.option('--processor-job-id', required=True, help=u"""Processor job id.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_processor_job(ctx, from_json, processor_job_id, if_match):

    if isinstance(processor_job_id, six.string_types) and len(processor_job_id.strip()) == 0:
        raise click.UsageError('Parameter --processor-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.cancel_processor_job(
        processor_job_id=processor_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@processor_job_group.command(name=cli_util.override('ai_document.create_processor_job.command_name', 'create'), help=u"""Create a processor job for document analysis. \n[Command Reference](createProcessorJob)""")
@cli_util.option('--input-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--processor-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the processor job.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'input-location': {'module': 'ai_document', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'input-location': {'module': 'ai_document', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}}, output_type={'module': 'ai_document', 'class': 'ProcessorJob'})
@cli_util.wrap_exceptions
def create_processor_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, input_location, output_location, compartment_id, processor_config, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = cli_util.parse_json_parameter("input_location", input_location)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['compartmentId'] = compartment_id
    _details['processorConfig'] = cli_util.parse_json_parameter("processor_config", processor_config)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.create_processor_job(
        create_processor_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_processor_job') and callable(getattr(client, 'get_processor_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_processor_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@processor_job_group.command(name=cli_util.override('ai_document.create_processor_job_inline_document_content.command_name', 'create-processor-job-inline-document-content'), help=u"""Create a processor job for document analysis. \n[Command Reference](createProcessorJob)""")
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--processor-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-data', required=True, help=u"""Raw document data with Base64 encoding.""")
@cli_util.option('--display-name', help=u"""The display name of the processor job.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}}, output_type={'module': 'ai_document', 'class': 'ProcessorJob'})
@cli_util.wrap_exceptions
def create_processor_job_inline_document_content(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, output_location, compartment_id, processor_config, input_location_data, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['compartmentId'] = compartment_id
    _details['processorConfig'] = cli_util.parse_json_parameter("processor_config", processor_config)
    _details['inputLocation']['data'] = input_location_data

    if display_name is not None:
        _details['displayName'] = display_name

    _details['inputLocation']['sourceType'] = 'INLINE_DOCUMENT_CONTENT'

    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.create_processor_job(
        create_processor_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_processor_job') and callable(getattr(client, 'get_processor_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_processor_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@processor_job_group.command(name=cli_util.override('ai_document.create_processor_job_object_storage_locations.command_name', 'create-processor-job-object-storage-locations'), help=u"""Create a processor job for document analysis. \n[Command Reference](createProcessorJob)""")
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--processor-config', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-object-locations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of ObjectLocations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the processor job.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}, 'input-location-object-locations': {'module': 'ai_document', 'class': 'list[ObjectLocation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config': {'module': 'ai_document', 'class': 'ProcessorConfig'}, 'input-location-object-locations': {'module': 'ai_document', 'class': 'list[ObjectLocation]'}}, output_type={'module': 'ai_document', 'class': 'ProcessorJob'})
@cli_util.wrap_exceptions
def create_processor_job_object_storage_locations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, output_location, compartment_id, processor_config, input_location_object_locations, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['compartmentId'] = compartment_id
    _details['processorConfig'] = cli_util.parse_json_parameter("processor_config", processor_config)
    _details['inputLocation']['objectLocations'] = cli_util.parse_json_parameter("input_location_object_locations", input_location_object_locations)

    if display_name is not None:
        _details['displayName'] = display_name

    _details['inputLocation']['sourceType'] = 'OBJECT_STORAGE_LOCATIONS'

    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.create_processor_job(
        create_processor_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_processor_job') and callable(getattr(client, 'get_processor_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_processor_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@processor_job_group.command(name=cli_util.override('ai_document.create_processor_job_general_processor_config.command_name', 'create-processor-job-general-processor-config'), help=u"""Create a processor job for document analysis. \n[Command Reference](createProcessorJob)""")
@cli_util.option('--input-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--processor-config-features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of document analysis requested.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The display name of the processor job.""")
@cli_util.option('--processor-config-document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The document type.""")
@cli_util.option('--processor-config-is-zip-output-enabled', type=click.BOOL, help=u"""Whether or not to generate a ZIP file containing the results.""")
@cli_util.option('--processor-config-language', help=u"""The document language, abbreviated according to the BCP 47 Language-Tag syntax.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'input-location': {'module': 'ai_document', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config-features': {'module': 'ai_document', 'class': 'list[DocumentFeature]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'input-location': {'module': 'ai_document', 'class': 'InputLocation'}, 'output-location': {'module': 'ai_document', 'class': 'OutputLocation'}, 'processor-config-features': {'module': 'ai_document', 'class': 'list[DocumentFeature]'}}, output_type={'module': 'ai_document', 'class': 'ProcessorJob'})
@cli_util.wrap_exceptions
def create_processor_job_general_processor_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, input_location, output_location, compartment_id, processor_config_features, display_name, processor_config_document_type, processor_config_is_zip_output_enabled, processor_config_language):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['processorConfig'] = {}
    _details['inputLocation'] = cli_util.parse_json_parameter("input_location", input_location)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['compartmentId'] = compartment_id
    _details['processorConfig']['features'] = cli_util.parse_json_parameter("processor_config_features", processor_config_features)

    if display_name is not None:
        _details['displayName'] = display_name

    if processor_config_document_type is not None:
        _details['processorConfig']['documentType'] = processor_config_document_type

    if processor_config_is_zip_output_enabled is not None:
        _details['processorConfig']['isZipOutputEnabled'] = processor_config_is_zip_output_enabled

    if processor_config_language is not None:
        _details['processorConfig']['language'] = processor_config_language

    _details['processorConfig']['processorType'] = 'GENERAL'

    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.create_processor_job(
        create_processor_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_processor_job') and callable(getattr(client, 'get_processor_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_processor_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@processor_job_group.command(name=cli_util.override('ai_document.get_processor_job.command_name', 'get'), help=u"""Get the details of a processor job. \n[Command Reference](getProcessorJob)""")
@cli_util.option('--processor-job-id', required=True, help=u"""Processor job id.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_document', 'class': 'ProcessorJob'})
@cli_util.wrap_exceptions
def get_processor_job(ctx, from_json, processor_job_id):

    if isinstance(processor_job_id, six.string_types) and len(processor_job_id.strip()) == 0:
        raise click.UsageError('Parameter --processor-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_document', 'ai_service_document', ctx)
    result = client.get_processor_job(
        processor_job_id=processor_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
