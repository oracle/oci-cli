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


@cli.command(cli_util.override('ai_vision.ai_vision_root_group.command_name', 'ai-vision'), cls=CommandGroupWithAlias, help=cli_util.override('ai_vision.ai_vision_root_group.help', """Using Vision, you can upload images to detect and classify objects in them. If you have lots of images, you can process them in batch using asynchronous API endpoints. Vision's features are thematically split between Document AI for document-centric images, and Image Analysis for object and scene-based images. Pretrained models and custom models are supported."""), short_help=cli_util.override('ai_vision.ai_vision_root_group.short_help', """Vision API"""))
@cli_util.help_option_group
def ai_vision_root_group():
    pass


@click.command(cli_util.override('ai_vision.image_job_group.command_name', 'image-job'), cls=CommandGroupWithAlias, help="""The job details for a batch image analysis.""")
@cli_util.help_option_group
def image_job_group():
    pass


@click.command(cli_util.override('ai_vision.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('ai_vision.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""A Vision Project containing models.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('ai_vision.analyze_document_result_group.command_name', 'analyze-document-result'), cls=CommandGroupWithAlias, help="""The document analysis results.""")
@cli_util.help_option_group
def analyze_document_result_group():
    pass


@click.command(cli_util.override('ai_vision.model_group.command_name', 'model'), cls=CommandGroupWithAlias, help="""Machine-learned Model.""")
@cli_util.help_option_group
def model_group():
    pass


@click.command(cli_util.override('ai_vision.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('ai_vision.project_collection_group.command_name', 'project-collection'), cls=CommandGroupWithAlias, help="""The results of a project search.""")
@cli_util.help_option_group
def project_collection_group():
    pass


@click.command(cli_util.override('ai_vision.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The workrequest status details.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('ai_vision.analyze_image_result_group.command_name', 'analyze-image-result'), cls=CommandGroupWithAlias, help="""The image analysis results.""")
@cli_util.help_option_group
def analyze_image_result_group():
    pass


@click.command(cli_util.override('ai_vision.document_job_group.command_name', 'document-job'), cls=CommandGroupWithAlias, help="""The job details for a batch document analysis.""")
@cli_util.help_option_group
def document_job_group():
    pass


@click.command(cli_util.override('ai_vision.model_collection_group.command_name', 'model-collection'), cls=CommandGroupWithAlias, help="""The results of a model search.""")
@cli_util.help_option_group
def model_collection_group():
    pass


ai_vision_root_group.add_command(image_job_group)
ai_vision_root_group.add_command(work_request_error_group)
ai_vision_root_group.add_command(project_group)
ai_vision_root_group.add_command(analyze_document_result_group)
ai_vision_root_group.add_command(model_group)
ai_vision_root_group.add_command(work_request_log_entry_group)
ai_vision_root_group.add_command(project_collection_group)
ai_vision_root_group.add_command(work_request_group)
ai_vision_root_group.add_command(analyze_image_result_group)
ai_vision_root_group.add_command(document_job_group)
ai_vision_root_group.add_command(model_collection_group)


@analyze_document_result_group.command(name=cli_util.override('ai_vision.analyze_document.command_name', 'analyze-document'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeDocument)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of document analysis requested.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--document', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@cli_util.option('--output-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]), help=u"""The document language, abbreviated according to ISO 639-2.""")
@cli_util.option('--document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The document type.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'document': {'module': 'ai_vision', 'class': 'DocumentDetails'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'document': {'module': 'ai_vision', 'class': 'DocumentDetails'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeDocumentResult'})
@cli_util.wrap_exceptions
def analyze_document(ctx, from_json, features, document, compartment_id, output_location, language, document_type):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['document'] = cli_util.parse_json_parameter("document", document)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if output_location is not None:
        _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if language is not None:
        _details['language'] = language

    if document_type is not None:
        _details['documentType'] = document_type

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_document(
        analyze_document_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analyze_document_result_group.command(name=cli_util.override('ai_vision.analyze_document_object_storage_document_details.command_name', 'analyze-document-object-storage-document-details'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeDocument)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of document analysis requested.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--document-namespace-name', required=True, help=u"""The Object Storage namespace.""")
@cli_util.option('--document-bucket-name', required=True, help=u"""The Object Storage bucket name.""")
@cli_util.option('--document-object-name', required=True, help=u"""The Object Storage object name.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@cli_util.option('--output-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]), help=u"""The document language, abbreviated according to ISO 639-2.""")
@cli_util.option('--document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The document type.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeDocumentResult'})
@cli_util.wrap_exceptions
def analyze_document_object_storage_document_details(ctx, from_json, features, document_namespace_name, document_bucket_name, document_object_name, compartment_id, output_location, language, document_type):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['document'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['document']['namespaceName'] = document_namespace_name
    _details['document']['bucketName'] = document_bucket_name
    _details['document']['objectName'] = document_object_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if output_location is not None:
        _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if language is not None:
        _details['language'] = language

    if document_type is not None:
        _details['documentType'] = document_type

    _details['document']['source'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_document(
        analyze_document_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analyze_document_result_group.command(name=cli_util.override('ai_vision.analyze_document_inline_document_details.command_name', 'analyze-document-inline-document-details'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeDocument)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of document analysis requested.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--document-data', required=True, help=u"""Raw document data.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@cli_util.option('--output-location', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]), help=u"""The document language, abbreviated according to ISO 639-2.""")
@cli_util.option('--document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The document type.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeDocumentResult'})
@cli_util.wrap_exceptions
def analyze_document_inline_document_details(ctx, from_json, features, document_data, compartment_id, output_location, language, document_type):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['document'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['document']['data'] = document_data

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if output_location is not None:
        _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if language is not None:
        _details['language'] = language

    if document_type is not None:
        _details['documentType'] = document_type

    _details['document']['source'] = 'INLINE'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_document(
        analyze_document_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analyze_image_result_group.command(name=cli_util.override('ai_vision.analyze_image.command_name', 'analyze-image'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeImage)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of image analysis.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'image': {'module': 'ai_vision', 'class': 'ImageDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'image': {'module': 'ai_vision', 'class': 'ImageDetails'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeImageResult'})
@cli_util.wrap_exceptions
def analyze_image(ctx, from_json, features, image, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['image'] = cli_util.parse_json_parameter("image", image)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_image(
        analyze_image_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analyze_image_result_group.command(name=cli_util.override('ai_vision.analyze_image_object_storage_image_details.command_name', 'analyze-image-object-storage-image-details'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeImage)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of image analysis.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image-namespace-name', required=True, help=u"""The Object Storage namespace.""")
@cli_util.option('--image-bucket-name', required=True, help=u"""The Object Storage bucket name.""")
@cli_util.option('--image-object-name', required=True, help=u"""The Object Storage object name.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeImageResult'})
@cli_util.wrap_exceptions
def analyze_image_object_storage_image_details(ctx, from_json, features, image_namespace_name, image_bucket_name, image_object_name, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['image'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['image']['namespaceName'] = image_namespace_name
    _details['image']['bucketName'] = image_bucket_name
    _details['image']['objectName'] = image_object_name

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    _details['image']['source'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_image(
        analyze_image_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@analyze_image_result_group.command(name=cli_util.override('ai_vision.analyze_image_inline_image_details.command_name', 'analyze-image-inline-image-details'), help=u"""Perform different types of image analysis. \n[Command Reference](analyzeImage)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of image analysis.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--image-data', required=True, help=u"""Raw image data.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that calls the API.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}}, output_type={'module': 'ai_vision', 'class': 'AnalyzeImageResult'})
@cli_util.wrap_exceptions
def analyze_image_inline_image_details(ctx, from_json, features, image_data, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['image'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['image']['data'] = image_data

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    _details['image']['source'] = 'INLINE'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.analyze_image(
        analyze_image_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@document_job_group.command(name=cli_util.override('ai_vision.cancel_document_job.command_name', 'cancel'), help=u"""Cancel a document batch job. \n[Command Reference](cancelDocumentJob)""")
@cli_util.option('--document-job-id', required=True, help=u"""Document job id.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_document_job(ctx, from_json, document_job_id, if_match):

    if isinstance(document_job_id, six.string_types) and len(document_job_id.strip()) == 0:
        raise click.UsageError('Parameter --document-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.cancel_document_job(
        document_job_id=document_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@image_job_group.command(name=cli_util.override('ai_vision.cancel_image_job.command_name', 'cancel'), help=u"""Cancel an image batch job. \n[Command Reference](cancelImageJob)""")
@cli_util.option('--image-job-id', required=True, help=u"""Image job id.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_image_job(ctx, from_json, image_job_id, if_match):

    if isinstance(image_job_id, six.string_types) and len(image_job_id.strip()) == 0:
        raise click.UsageError('Parameter --image-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.cancel_image_job(
        image_job_id=image_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('ai_vision.cancel_work_request.command_name', 'cancel'), help=u"""Cancel the work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai_vision.change_model_compartment.command_name', 'change-compartment'), help=u"""Moves a model from one compartment to another. When provided, If-Match is checked against the ETag values of the resource. \n[Command Reference](changeModelCompartment)""")
@cli_util.option('--model-id', required=True, help=u"""A unique model identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the model should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.change_model_compartment(
        model_id=model_id,
        change_model_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai_vision.change_project_compartment.command_name', 'change-compartment'), help=u"""Move a project from one compartment to another. When provided, If-Match is checked against the ETag values of the resource. \n[Command Reference](changeProjectCompartment)""")
@cli_util.option('--project-id', required=True, help=u"""A unique project identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the project should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.change_project_compartment(
        project_id=project_id,
        change_project_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@document_job_group.command(name=cli_util.override('ai_vision.create_document_job.command_name', 'create'), help=u"""Create a document analysis batch job. \n[Command Reference](createDocumentJob)""")
@cli_util.option('--input-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of requested document analysis types.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The compartment identifier from the requester.""")
@cli_util.option('--display-name', help=u"""The document job display name.""")
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]), help=u"""The language of the document, abbreviated according to ISO 639-2.""")
@cli_util.option('--document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The type of documents.""")
@cli_util.option('--is-zip-output-enabled', type=click.BOOL, help=u"""Whether or not to generate a ZIP file containing the results.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'input-location': {'module': 'ai_vision', 'class': 'InputLocation'}, 'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'input-location': {'module': 'ai_vision', 'class': 'InputLocation'}, 'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}}, output_type={'module': 'ai_vision', 'class': 'DocumentJob'})
@cli_util.wrap_exceptions
def create_document_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, input_location, features, output_location, compartment_id, display_name, language, document_type, is_zip_output_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = cli_util.parse_json_parameter("input_location", input_location)
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if language is not None:
        _details['language'] = language

    if document_type is not None:
        _details['documentType'] = document_type

    if is_zip_output_enabled is not None:
        _details['isZipOutputEnabled'] = is_zip_output_enabled

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.create_document_job(
        create_document_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_document_job') and callable(getattr(client, 'get_document_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_document_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@document_job_group.command(name=cli_util.override('ai_vision.create_document_job_object_list_inline_input_location.command_name', 'create-document-job-object-list-inline-input-location'), help=u"""Create a document analysis batch job. \n[Command Reference](createDocumentJob)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of requested document analysis types.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-object-locations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of ObjectLocations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The compartment identifier from the requester.""")
@cli_util.option('--display-name', help=u"""The document job display name.""")
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]), help=u"""The language of the document, abbreviated according to ISO 639-2.""")
@cli_util.option('--document-type', type=custom_types.CliCaseInsensitiveChoice(["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]), help=u"""The type of documents.""")
@cli_util.option('--is-zip-output-enabled', type=click.BOOL, help=u"""Whether or not to generate a ZIP file containing the results.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}, 'input-location-object-locations': {'module': 'ai_vision', 'class': 'list[ObjectLocation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[DocumentFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}, 'input-location-object-locations': {'module': 'ai_vision', 'class': 'list[ObjectLocation]'}}, output_type={'module': 'ai_vision', 'class': 'DocumentJob'})
@cli_util.wrap_exceptions
def create_document_job_object_list_inline_input_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, features, output_location, input_location_object_locations, compartment_id, display_name, language, document_type, is_zip_output_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['inputLocation']['objectLocations'] = cli_util.parse_json_parameter("input_location_object_locations", input_location_object_locations)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if language is not None:
        _details['language'] = language

    if document_type is not None:
        _details['documentType'] = document_type

    if is_zip_output_enabled is not None:
        _details['isZipOutputEnabled'] = is_zip_output_enabled

    _details['inputLocation']['sourceType'] = 'OBJECT_LIST_INLINE_INPUT_LOCATION'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.create_document_job(
        create_document_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_document_job') and callable(getattr(client, 'get_document_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_document_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_job_group.command(name=cli_util.override('ai_vision.create_image_job.command_name', 'create'), help=u"""Create an image analysis batch job. \n[Command Reference](createImageJob)""")
@cli_util.option('--input-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of requested image analysis types.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The compartment identifier from the requester.""")
@cli_util.option('--display-name', help=u"""The image job display name.""")
@cli_util.option('--is-zip-output-enabled', type=click.BOOL, help=u"""Whether or not to generate a ZIP file containing the results.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'input-location': {'module': 'ai_vision', 'class': 'InputLocation'}, 'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'input-location': {'module': 'ai_vision', 'class': 'InputLocation'}, 'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}}, output_type={'module': 'ai_vision', 'class': 'ImageJob'})
@cli_util.wrap_exceptions
def create_image_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, input_location, features, output_location, compartment_id, display_name, is_zip_output_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = cli_util.parse_json_parameter("input_location", input_location)
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if is_zip_output_enabled is not None:
        _details['isZipOutputEnabled'] = is_zip_output_enabled

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.create_image_job(
        create_image_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image_job') and callable(getattr(client, 'get_image_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@image_job_group.command(name=cli_util.override('ai_vision.create_image_job_object_list_inline_input_location.command_name', 'create-image-job-object-list-inline-input-location'), help=u"""Create an image analysis batch job. \n[Command Reference](createImageJob)""")
@cli_util.option('--features', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of requested image analysis types.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-location', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--input-location-object-locations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of ObjectLocations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The compartment identifier from the requester.""")
@cli_util.option('--display-name', help=u"""The image job display name.""")
@cli_util.option('--is-zip-output-enabled', type=click.BOOL, help=u"""Whether or not to generate a ZIP file containing the results.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["SUCCEEDED", "FAILED", "ACCEPTED", "CANCELED", "IN_PROGRESS", "CANCELING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}, 'input-location-object-locations': {'module': 'ai_vision', 'class': 'list[ObjectLocation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'features': {'module': 'ai_vision', 'class': 'list[ImageFeature]'}, 'output-location': {'module': 'ai_vision', 'class': 'OutputLocation'}, 'input-location-object-locations': {'module': 'ai_vision', 'class': 'list[ObjectLocation]'}}, output_type={'module': 'ai_vision', 'class': 'ImageJob'})
@cli_util.wrap_exceptions
def create_image_job_object_list_inline_input_location(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, features, output_location, input_location_object_locations, compartment_id, display_name, is_zip_output_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['inputLocation'] = {}
    _details['features'] = cli_util.parse_json_parameter("features", features)
    _details['outputLocation'] = cli_util.parse_json_parameter("output_location", output_location)
    _details['inputLocation']['objectLocations'] = cli_util.parse_json_parameter("input_location_object_locations", input_location_object_locations)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if is_zip_output_enabled is not None:
        _details['isZipOutputEnabled'] = is_zip_output_enabled

    _details['inputLocation']['sourceType'] = 'OBJECT_LIST_INLINE_INPUT_LOCATION'

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.create_image_job(
        create_image_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_image_job') and callable(getattr(client, 'get_image_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_image_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@model_group.command(name=cli_util.override('ai_vision.create_model.command_name', 'create'), help=u"""Create a new model. \n[Command Reference](createModel)""")
@cli_util.option('--model-type', required=True, help=u"""Which type of Vision model this is.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--training-dataset', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--project-id', required=True, help=u"""The [OCID] of the project that contains the model.""")
@cli_util.option('--display-name', help=u"""A human-friendly name for the model, which can be changed.""")
@cli_util.option('--description', help=u"""An optional description of the model.""")
@cli_util.option('--model-version', help=u"""The model version""")
@cli_util.option('--is-quick-mode', type=click.BOOL, help=u"""Set to true when experimenting with a new model type or dataset, so the model training is quick, with a predefined low number of passes through the training data.""")
@cli_util.option('--max-training-duration-in-hours', help=u"""The maximum model training duration in hours, expressed as a decimal fraction.""")
@cli_util.option('--testing-dataset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--validation-dataset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'training-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'testing-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'validation-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'training-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'testing-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'validation-dataset': {'module': 'ai_vision', 'class': 'Dataset'}, 'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_vision', 'class': 'Model'})
@cli_util.wrap_exceptions
def create_model(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, model_type, compartment_id, training_dataset, project_id, display_name, description, model_version, is_quick_mode, max_training_duration_in_hours, testing_dataset, validation_dataset, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['compartmentId'] = compartment_id
    _details['trainingDataset'] = cli_util.parse_json_parameter("training_dataset", training_dataset)
    _details['projectId'] = project_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if model_version is not None:
        _details['modelVersion'] = model_version

    if is_quick_mode is not None:
        _details['isQuickMode'] = is_quick_mode

    if max_training_duration_in_hours is not None:
        _details['maxTrainingDurationInHours'] = max_training_duration_in_hours

    if testing_dataset is not None:
        _details['testingDataset'] = cli_util.parse_json_parameter("testing_dataset", testing_dataset)

    if validation_dataset is not None:
        _details['validationDataset'] = cli_util.parse_json_parameter("validation_dataset", validation_dataset)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.create_model(
        create_model_details=_details,
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


@project_group.command(name=cli_util.override('ai_vision.create_project.command_name', 'create'), help=u"""Create a new project. \n[Command Reference](createProject)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment identifier.""")
@cli_util.option('--display-name', help=u"""A human-friendly name for the project, that can be changed.""")
@cli_util.option('--description', help=u"""An optional description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ai_vision', 'class': 'Project'})
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

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
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


@model_group.command(name=cli_util.override('ai_vision.delete_model.command_name', 'delete'), help=u"""Delete a model by identifier. \n[Command Reference](deleteModel)""")
@cli_util.option('--model-id', required=True, help=u"""A unique model identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.delete_model(
        model_id=model_id,
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


@project_group.command(name=cli_util.override('ai_vision.delete_project.command_name', 'delete'), help=u"""Delete a project by identifier. \n[Command Reference](deleteProject)""")
@cli_util.option('--project-id', required=True, help=u"""A unique project identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
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


@document_job_group.command(name=cli_util.override('ai_vision.get_document_job.command_name', 'get'), help=u"""Get details of a document batch job. \n[Command Reference](getDocumentJob)""")
@cli_util.option('--document-job-id', required=True, help=u"""Document job id.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'DocumentJob'})
@cli_util.wrap_exceptions
def get_document_job(ctx, from_json, document_job_id):

    if isinstance(document_job_id, six.string_types) and len(document_job_id.strip()) == 0:
        raise click.UsageError('Parameter --document-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.get_document_job(
        document_job_id=document_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@image_job_group.command(name=cli_util.override('ai_vision.get_image_job.command_name', 'get'), help=u"""Get details of an image batch job. \n[Command Reference](getImageJob)""")
@cli_util.option('--image-job-id', required=True, help=u"""Image job id.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'ImageJob'})
@cli_util.wrap_exceptions
def get_image_job(ctx, from_json, image_job_id):

    if isinstance(image_job_id, six.string_types) and len(image_job_id.strip()) == 0:
        raise click.UsageError('Parameter --image-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.get_image_job(
        image_job_id=image_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai_vision.get_model.command_name', 'get'), help=u"""Get a model by identifier. \n[Command Reference](getModel)""")
@cli_util.option('--model-id', required=True, help=u"""A unique model identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'Model'})
@cli_util.wrap_exceptions
def get_model(ctx, from_json, model_id):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.get_model(
        model_id=model_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('ai_vision.get_project.command_name', 'get'), help=u"""Get a project by identifier. \n[Command Reference](getProject)""")
@cli_util.option('--project-id', required=True, help=u"""A unique project identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, project_id):

    if isinstance(project_id, six.string_types) and len(project_id.strip()) == 0:
        raise click.UsageError('Parameter --project-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.get_project(
        project_id=project_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('ai_vision.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@model_collection_group.command(name=cli_util.override('ai_vision.list_models.command_name', 'list-models'), help=u"""Returns a list of models in a compartment. \n[Command Reference](listModels)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--project-id', help=u"""The ID of the project for which to list the objects.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The filter to match models with the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""The filter to find the model with the given identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'ModelCollection'})
@cli_util.wrap_exceptions
def list_models(ctx, from_json, all_pages, page_size, compartment_id, project_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_models,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_models,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_models(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_collection_group.command(name=cli_util.override('ai_vision.list_projects.command_name', 'list-projects'), help=u"""Returns a list of projects. \n[Command Reference](listProjects)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The filter to match projects with the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""The filter to find the project with the given identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'ProjectCollection'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_projects,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_projects,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_projects(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('ai_vision.list_work_request_errors.command_name', 'list'), help=u"""Returns a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('ai_vision.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
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


@work_request_group.command(name=cli_util.override('ai_vision.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources whose lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""The position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_vision', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
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
    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@model_group.command(name=cli_util.override('ai_vision.update_model.command_name', 'update'), help=u"""Updates the model metadata. \n[Command Reference](updateModel)""")
@cli_util.option('--model-id', required=True, help=u"""A unique model identifier.""")
@cli_util.option('--display-name', help=u"""A human-friendly name of the model, which can be changed.""")
@cli_util.option('--description', help=u"""An optional description of the model.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_model(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, model_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(model_id, six.string_types) and len(model_id.strip()) == 0:
        raise click.UsageError('Parameter --model-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
    result = client.update_model(
        model_id=model_id,
        update_model_details=_details,
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


@project_group.command(name=cli_util.override('ai_vision.update_project.command_name', 'update'), help=u"""Update the project metadata. \n[Command Reference](updateProject)""")
@cli_util.option('--project-id', required=True, help=u"""A unique project identifier.""")
@cli_util.option('--display-name', help=u"""A human-friendly name for the project, that can be changed.""")
@cli_util.option('--description', help=u"""An optional description of the project.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ai_vision', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ai_vision', 'class': 'dict(str, dict(str, object))'}})
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

    client = cli_util.build_client('ai_vision', 'ai_service_vision', ctx)
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
