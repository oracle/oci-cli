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


@cli.command(cli_util.override('data_labeling_service_dataplane.data_labeling_service_dataplane_root_group.command_name', 'data-labeling-service-dataplane'), cls=CommandGroupWithAlias, help=cli_util.override('data_labeling_service_dataplane.data_labeling_service_dataplane_root_group.help', """Use Data Labeling API to create Annotations on Images, Texts & Documents, and generate snapshots."""), short_help=cli_util.override('data_labeling_service_dataplane.data_labeling_service_dataplane_root_group.short_help', """Data Labeling API"""))
@cli_util.help_option_group
def data_labeling_service_dataplane_root_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.annotation_group.command_name', 'annotation'), cls=CommandGroupWithAlias, help="""An annotation represents a user- or machine-generated annotation for a given record.  The details of the annotation are captured in the RecordAnnotationDetails.""")
@cli_util.help_option_group
def annotation_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.record_analytics_aggregation_collection_group.command_name', 'record-analytics-aggregation-collection'), cls=CommandGroupWithAlias, help="""Collection of records aggregated.""")
@cli_util.help_option_group
def record_analytics_aggregation_collection_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.record_group.command_name', 'record'), cls=CommandGroupWithAlias, help="""A record represents an entry in a dataset that needs labeling.""")
@cli_util.help_option_group
def record_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.annotation_analytics_aggregation_collection_group.command_name', 'annotation-analytics-aggregation-collection'), cls=CommandGroupWithAlias, help="""Aggregation entities are required by the API consistency guidelines for API Consistency Guidelines#AnalyticsAPIs.  These are used to summarize annotations for a given dataset and will be used to populate UI elements.  Aggregations need to have the fields that identify the exact scope that they're summarizing.  Any filters applied to the list API, have to show up in the aggregation.""")
@cli_util.help_option_group
def annotation_analytics_aggregation_collection_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.record_collection_group.command_name', 'record-collection'), cls=CommandGroupWithAlias, help="""The results of a record search. It contains RecordSummary items and other data.""")
@cli_util.help_option_group
def record_collection_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.dataset_group.command_name', 'dataset'), cls=CommandGroupWithAlias, help="""A dataset is a logical collection of records. The dataset contains all the information necessary to describe a record's source, format, the type of annotations allowed for the record, and the labels allowed on annotations.""")
@cli_util.help_option_group
def dataset_group():
    pass


@click.command(cli_util.override('data_labeling_service_dataplane.annotation_collection_group.command_name', 'annotation-collection'), cls=CommandGroupWithAlias, help="""The results of an annotations search. It contains AnnotationSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def annotation_collection_group():
    pass


data_labeling_service_dataplane_root_group.add_command(annotation_group)
data_labeling_service_dataplane_root_group.add_command(record_analytics_aggregation_collection_group)
data_labeling_service_dataplane_root_group.add_command(record_group)
data_labeling_service_dataplane_root_group.add_command(annotation_analytics_aggregation_collection_group)
data_labeling_service_dataplane_root_group.add_command(record_collection_group)
data_labeling_service_dataplane_root_group.add_command(dataset_group)
data_labeling_service_dataplane_root_group.add_command(annotation_collection_group)


@annotation_group.command(name=cli_util.override('data_labeling_service_dataplane.create_annotation.command_name', 'create'), help=u"""Creates an annotation. \n[Command Reference](createAnnotation)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the annotation.""")
@cli_util.option('--entities', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The entity types are validated against the dataset to ensure consistency.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'entities': {'module': 'data_labeling_service_dataplane', 'class': 'list[Entity]'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entities': {'module': 'data_labeling_service_dataplane', 'class': 'list[Entity]'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Annotation'})
@cli_util.wrap_exceptions
def create_annotation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, compartment_id, entities, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordId'] = record_id
    _details['compartmentId'] = compartment_id
    _details['entities'] = cli_util.parse_json_parameter("entities", entities)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_annotation(
        create_annotation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_annotation') and callable(getattr(client, 'get_annotation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_annotation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.create_record.command_name', 'create'), help=u"""Creates a record. \n[Command Reference](createRecord)""")
@cli_util.option('--name', required=True, help=u"""The name is automatically assigned by the service. It is unique and immutable.""")
@cli_util.option('--dataset-id', required=True, help=u"""The OCID of the dataset to associate the record with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--record-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def create_record(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, dataset_id, compartment_id, source_details, record_metadata, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['datasetId'] = dataset_id
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if record_metadata is not None:
        _details['recordMetadata'] = cli_util.parse_json_parameter("record_metadata", record_metadata)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_record(
        create_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.create_record_create_object_storage_source_details.command_name', 'create-record-create-object-storage-source-details'), help=u"""Creates a record. \n[Command Reference](createRecord)""")
@cli_util.option('--name', required=True, help=u"""The name is automatically assigned by the service. It is unique and immutable.""")
@cli_util.option('--dataset-id', required=True, help=u"""The OCID of the dataset to associate the record with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.""")
@cli_util.option('--source-details-relative-path', required=True, help=u"""The path relative to the prefix specified in the dataset source details (file name).""")
@cli_util.option('--record-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source-details-offset', type=click.FLOAT, help=u"""The offset into the file containing the content.""")
@cli_util.option('--source-details-length', type=click.FLOAT, help=u"""The length from offset into the file containing the content.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def create_record_create_object_storage_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, dataset_id, compartment_id, source_details_relative_path, record_metadata, freeform_tags, defined_tags, source_details_offset, source_details_length):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['name'] = name
    _details['datasetId'] = dataset_id
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['relativePath'] = source_details_relative_path

    if record_metadata is not None:
        _details['recordMetadata'] = cli_util.parse_json_parameter("record_metadata", record_metadata)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if source_details_offset is not None:
        _details['sourceDetails']['offset'] = source_details_offset

    if source_details_length is not None:
        _details['sourceDetails']['length'] = source_details_length

    _details['sourceDetails']['sourceType'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_record(
        create_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.create_record_document_metadata.command_name', 'create-record-document-metadata'), help=u"""Creates a record. \n[Command Reference](createRecord)""")
@cli_util.option('--name', required=True, help=u"""The name is automatically assigned by the service. It is unique and immutable.""")
@cli_util.option('--dataset-id', required=True, help=u"""The OCID of the dataset to associate the record with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def create_record_document_metadata(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, dataset_id, compartment_id, source_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}
    _details['name'] = name
    _details['datasetId'] = dataset_id
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['recordMetadata']['recordType'] = 'DOCUMENT_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_record(
        create_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.create_record_image_metadata.command_name', 'create-record-image-metadata'), help=u"""Creates a record. \n[Command Reference](createRecord)""")
@cli_util.option('--name', required=True, help=u"""The name is automatically assigned by the service. It is unique and immutable.""")
@cli_util.option('--dataset-id', required=True, help=u"""The OCID of the dataset to associate the record with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--record-metadata-height', type=click.INT, help=u"""Height of the image record.""")
@cli_util.option('--record-metadata-width', type=click.INT, help=u"""Width of the image record.""")
@cli_util.option('--record-metadata-depth', type=click.INT, help=u"""Depth of the image record.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def create_record_image_metadata(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, dataset_id, compartment_id, source_details, freeform_tags, defined_tags, record_metadata_height, record_metadata_width, record_metadata_depth):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}
    _details['name'] = name
    _details['datasetId'] = dataset_id
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if record_metadata_height is not None:
        _details['recordMetadata']['height'] = record_metadata_height

    if record_metadata_width is not None:
        _details['recordMetadata']['width'] = record_metadata_width

    if record_metadata_depth is not None:
        _details['recordMetadata']['depth'] = record_metadata_depth

    _details['recordMetadata']['recordType'] = 'IMAGE_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_record(
        create_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.create_record_text_metadata.command_name', 'create-record-text-metadata'), help=u"""Creates a record. \n[Command Reference](createRecord)""")
@cli_util.option('--name', required=True, help=u"""The name is automatically assigned by the service. It is unique and immutable.""")
@cli_util.option('--dataset-id', required=True, help=u"""The OCID of the dataset to associate the record with.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment for the record. This is tied to the dataset. It is not changeable on the record itself.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'data_labeling_service_dataplane', 'class': 'CreateSourceDetails'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def create_record_text_metadata(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, dataset_id, compartment_id, source_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}
    _details['name'] = name
    _details['datasetId'] = dataset_id
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['recordMetadata']['recordType'] = 'TEXT_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.create_record(
        create_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@annotation_group.command(name=cli_util.override('data_labeling_service_dataplane.delete_annotation.command_name', 'delete'), help=u"""It deletes an annotation resource by identifier. \n[Command Reference](deleteAnnotation)""")
@cli_util.option('--annotation-id', required=True, help=u"""A unique annotation identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_annotation(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, annotation_id, if_match):

    if isinstance(annotation_id, six.string_types) and len(annotation_id.strip()) == 0:
        raise click.UsageError('Parameter --annotation-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.delete_annotation(
        annotation_id=annotation_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_annotation') and callable(getattr(client, 'get_annotation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_annotation(annotation_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.delete_record.command_name', 'delete'), help=u"""Deletes a record resource by identifier. \n[Command Reference](deleteRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_record(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, if_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.delete_record(
        record_id=record_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_record(record_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@annotation_group.command(name=cli_util.override('data_labeling_service_dataplane.get_annotation.command_name', 'get'), help=u"""Gets an annotation. \n[Command Reference](getAnnotation)""")
@cli_util.option('--annotation-id', required=True, help=u"""A unique annotation identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Annotation'})
@cli_util.wrap_exceptions
def get_annotation(ctx, from_json, annotation_id):

    if isinstance(annotation_id, six.string_types) and len(annotation_id.strip()) == 0:
        raise click.UsageError('Parameter --annotation-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.get_annotation(
        annotation_id=annotation_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service_dataplane.get_dataset.command_name', 'get'), help=u"""Gets a dataset by identifier. \n[Command Reference](getDataset)""")
@cli_util.option('--dataset-id', required=True, help=u"""A unique dataset OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def get_dataset(ctx, from_json, dataset_id):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.get_dataset(
        dataset_id=dataset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.get_record.command_name', 'get'), help=u"""Gets a record. \n[Command Reference](getRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def get_record(ctx, from_json, record_id):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.get_record(
        record_id=record_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.get_record_content.command_name', 'get-record-content'), help=u"""Retrieves the content of the record from the dataset source. \n[Command Reference](getRecordContent)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-none-match', help=u"""For optimistic concurrency control. In the GET call for a resource, set the `if-none-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be fetched only if the etag you provide does not match the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_record_content(ctx, from_json, file, record_id, if_none_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.get_record_content(
        record_id=record_id,
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.get_record_preview_content.command_name', 'get-record-preview-content'), help=u"""Retrieves the preview of the record content from the dataset source. \n[Command Reference](getRecordPreviewContent)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-none-match', help=u"""For optimistic concurrency control. In the GET call for a resource, set the `if-none-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be fetched only if the etag you provide does not match the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_record_preview_content(ctx, from_json, file, record_id, if_none_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.get_record_preview_content(
        record_id=record_id,
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


@annotation_collection_group.command(name=cli_util.override('data_labeling_service_dataplane.list_annotations.command_name', 'list-annotations'), help=u"""Returns a list of annotations. \n[Command Reference](listAnnotations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--dataset-id', required=True, help=u"""Filter the results by the OCID of the dataset.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--id', help=u"""The unique OCID identifier.""")
@cli_util.option('--updated-by', help=u"""The OCID of the principal which updated the annotation.""")
@cli_util.option('--record-id', help=u"""The OCID of the record annotated.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The date and time the resource was created, in the timestamp format defined by RFC3339.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The date and time the resource was created, in the timestamp format defined by RFC3339.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "label"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. If no value is specified timeCreated is used by default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'AnnotationCollection'})
@cli_util.wrap_exceptions
def list_annotations(ctx, from_json, all_pages, page_size, compartment_id, dataset_id, lifecycle_state, id, updated_by, record_id, time_created_greater_than_or_equal_to, time_created_less_than_or_equal_to, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if updated_by is not None:
        kwargs['updated_by'] = updated_by
    if record_id is not None:
        kwargs['record_id'] = record_id
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than_or_equal_to is not None:
        kwargs['time_created_less_than_or_equal_to'] = time_created_less_than_or_equal_to
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_annotations,
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_annotations,
            limit,
            page_size,
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    else:
        result = client.list_annotations(
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@record_collection_group.command(name=cli_util.override('data_labeling_service_dataplane.list_records.command_name', 'list-records'), help=u"""The list of records in the specified compartment. \n[Command Reference](listRecords)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--dataset-id', required=True, help=u"""Filter the results by the OCID of the dataset.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--name', help=u"""The name of the record.""")
@cli_util.option('--id', help=u"""The unique OCID identifier.""")
@cli_util.option('--is-labeled', type=click.BOOL, help=u"""Whether the record has been labeled and has associated annotations.""")
@cli_util.option('--annotation-labels-contains', multiple=True, help=u"""Lets the user filter records based on the related annotations.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. The default order for timeCreated is descending. The default order for name is ascending. If no value is specified, timeCreated is used by default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'annotation-labels-contains': {'module': 'data_labeling_service_dataplane', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'annotation-labels-contains': {'module': 'data_labeling_service_dataplane', 'class': 'list[string]'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def list_records(ctx, from_json, all_pages, page_size, compartment_id, dataset_id, lifecycle_state, name, id, is_labeled, annotation_labels_contains, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if id is not None:
        kwargs['id'] = id
    if is_labeled is not None:
        kwargs['is_labeled'] = is_labeled
    if annotation_labels_contains is not None and len(annotation_labels_contains) > 0:
        kwargs['annotation_labels_contains'] = annotation_labels_contains
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_records,
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_records,
            limit,
            page_size,
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    else:
        result = client.list_records(
            compartment_id=compartment_id,
            dataset_id=dataset_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@annotation_analytics_aggregation_collection_group.command(name=cli_util.override('data_labeling_service_dataplane.summarize_annotation_analytics.command_name', 'summarize-annotation-analytics'), help=u"""Summarize the annotations created for a given dataset. \n[Command Reference](summarizeAnnotationAnalytics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--dataset-id', required=True, help=u"""Filter the results by the OCID of the dataset.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--label', help=u"""It summarizes annotations with the specified label.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["count", "label", "updatedBy"]), help=u"""The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, updatedBy is used by default.""")
@cli_util.option('--annotation-group-by', type=custom_types.CliCaseInsensitiveChoice(["updatedBy", "label"]), help=u"""The field to group by. If no value is specified, updatedBy is used by default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'AnnotationAnalyticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_annotation_analytics(ctx, from_json, compartment_id, dataset_id, lifecycle_state, label, limit, page, sort_order, sort_by, annotation_group_by):

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if label is not None:
        kwargs['label'] = label
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if annotation_group_by is not None:
        kwargs['annotation_group_by'] = annotation_group_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.summarize_annotation_analytics(
        compartment_id=compartment_id,
        dataset_id=dataset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@record_analytics_aggregation_collection_group.command(name=cli_util.override('data_labeling_service_dataplane.summarize_record_analytics.command_name', 'summarize-record-analytics'), help=u"""Summarize the records created for a given dataset. \n[Command Reference](summarizeRecordAnalytics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--dataset-id', required=True, help=u"""Filter the results by the OCID of the dataset.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), help=u"""A filter to return only resources whose lifecycleState matches the given lifecycleState.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--record-group-by', type=custom_types.CliCaseInsensitiveChoice(["isLabeled", "annotationLabelContains"]), help=u"""The field to group by. If no value is specified isLabeled is used by default.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["count", "isLabeled"]), help=u"""The field to sort by. Only one sort order may be provided. The default order is descending. If no value is specified, count is used by default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'RecordAnalyticsAggregationCollection'})
@cli_util.wrap_exceptions
def summarize_record_analytics(ctx, from_json, compartment_id, dataset_id, lifecycle_state, limit, page, sort_order, record_group_by, sort_by):

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if record_group_by is not None:
        kwargs['record_group_by'] = record_group_by
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.summarize_record_analytics(
        compartment_id=compartment_id,
        dataset_id=dataset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@annotation_group.command(name=cli_util.override('data_labeling_service_dataplane.update_annotation.command_name', 'update'), help=u"""Updates an annotation. \n[Command Reference](updateAnnotation)""")
@cli_util.option('--annotation-id', required=True, help=u"""A unique annotation identifier.""")
@cli_util.option('--entities', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The entity types are validated against the dataset to ensure consistency.

This option is a JSON list with items of type Entity.  For documentation on Entity please see our API reference: https://docs.cloud.oracle.com/api/#/en/datalabeling/20211001/datatypes/Entity.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'entities': {'module': 'data_labeling_service_dataplane', 'class': 'list[Entity]'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'entities': {'module': 'data_labeling_service_dataplane', 'class': 'list[Entity]'}, 'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Annotation'})
@cli_util.wrap_exceptions
def update_annotation(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, annotation_id, entities, freeform_tags, defined_tags, if_match):

    if isinstance(annotation_id, six.string_types) and len(annotation_id.strip()) == 0:
        raise click.UsageError('Parameter --annotation-id cannot be whitespace or empty string')
    if not force:
        if entities or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to entities and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if entities is not None:
        _details['entities'] = cli_util.parse_json_parameter("entities", entities)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.update_annotation(
        annotation_id=annotation_id,
        update_annotation_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_annotation') and callable(getattr(client, 'get_annotation')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_annotation(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.update_record.command_name', 'update'), help=u"""Updates a record. \n[Command Reference](updateRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--record-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}, 'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}, 'record-metadata': {'module': 'data_labeling_service_dataplane', 'class': 'RecordMetadata'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def update_record(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, freeform_tags, defined_tags, record_metadata, if_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or record_metadata:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and record-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if record_metadata is not None:
        _details['recordMetadata'] = cli_util.parse_json_parameter("record_metadata", record_metadata)

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.update_record(
        record_id=record_id,
        update_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.update_record_document_metadata.command_name', 'update-record-document-metadata'), help=u"""Updates a record. \n[Command Reference](updateRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def update_record_document_metadata(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, freeform_tags, defined_tags, if_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['recordMetadata']['recordType'] = 'DOCUMENT_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.update_record(
        record_id=record_id,
        update_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.update_record_image_metadata.command_name', 'update-record-image-metadata'), help=u"""Updates a record. \n[Command Reference](updateRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--record-metadata-height', type=click.INT, help=u"""Height of the image record.""")
@cli_util.option('--record-metadata-width', type=click.INT, help=u"""Width of the image record.""")
@cli_util.option('--record-metadata-depth', type=click.INT, help=u"""Depth of the image record.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def update_record_image_metadata(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, freeform_tags, defined_tags, if_match, record_metadata_height, record_metadata_width, record_metadata_depth):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if record_metadata_height is not None:
        _details['recordMetadata']['height'] = record_metadata_height

    if record_metadata_width is not None:
        _details['recordMetadata']['width'] = record_metadata_width

    if record_metadata_depth is not None:
        _details['recordMetadata']['depth'] = record_metadata_depth

    _details['recordMetadata']['recordType'] = 'IMAGE_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.update_record(
        record_id=record_id,
        update_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@record_group.command(name=cli_util.override('data_labeling_service_dataplane.update_record_text_metadata.command_name', 'update-record-text-metadata'), help=u"""Updates a record. \n[Command Reference](updateRecord)""")
@cli_util.option('--record-id', required=True, help=u"""The OCID of the record annotated.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair that is applied without any predefined name, type, or scope. It exists for cross-compatibility only. For example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags for this resource. Each key is predefined and scoped to a namespace. For example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource is updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service_dataplane', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service_dataplane', 'class': 'Record'})
@cli_util.wrap_exceptions
def update_record_text_metadata(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, record_id, freeform_tags, defined_tags, if_match):

    if isinstance(record_id, six.string_types) and len(record_id.strip()) == 0:
        raise click.UsageError('Parameter --record-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recordMetadata'] = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['recordMetadata']['recordType'] = 'TEXT_METADATA'

    client = cli_util.build_client('data_labeling_service_dataplane', 'data_labeling', ctx)
    result = client.update_record(
        record_id=record_id,
        update_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_record') and callable(getattr(client, 'get_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
