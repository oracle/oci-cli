# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.

from __future__ import print_function
import click
import oci
import sys
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
from services.generative_ai_data.src.oci_cli_enrichment_job.generated import enrichmentjob_cli
from services.generative_ai_data.src.oci_cli_generative_ai_data.generated import generative_ai_data_service_cli


cli_util.rename_command(
    enrichmentjob_cli,
    generative_ai_data_service_cli.generative_ai_data_service_group,
    enrichmentjob_cli.enrichment_job_root_group,
    "enrichment-jobs"
)

enrichmentjob_cli.enrichment_job_root_group.commands.pop(enrichmentjob_cli.enrichment_job_group.name)
enrichmentjob_cli.enrichment_job_root_group.commands.pop(enrichmentjob_cli.enrichment_job_collection_group.name)

enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.cancel_enrichment_job)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.generate_enrichment_job)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.get_enrichment_job)
enrichmentjob_cli.enrichment_job_root_group.add_command(enrichmentjob_cli.list_enrichment_jobs)

cli_util.rename_command(enrichmentjob_cli, enrichmentjob_cli.enrichment_job_root_group, enrichmentjob_cli.list_enrichment_jobs, "list")
cli_util.rename_command(enrichmentjob_cli, enrichmentjob_cli.enrichment_job_root_group, enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration, "generate-full-build")
cli_util.rename_command(enrichmentjob_cli, enrichmentjob_cli.enrichment_job_root_group, enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration, "generate-partial-build")
cli_util.rename_command(enrichmentjob_cli, enrichmentjob_cli.enrichment_job_root_group, enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration, "generate-delta-refresh")


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.cancel_enrichment_job, params_to_exclude=['enrichment_job_id'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.cancel_enrichment_job.name, help=enrichmentjob_cli.cancel_enrichment_job.help)
@cli_util.option('--job-id', required=True, help=u"""The OCID of the enrichment job.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def cancel_enrichment_job_extended(ctx, **kwargs):
    enrichment_job_id = kwargs.pop('job_id')
    semantic_store_id = kwargs.pop('semantic_store_id')
    if_match = kwargs.pop('if_match', None)
    wait_for_state = kwargs.pop('wait_for_state', None)
    max_wait_seconds = kwargs.pop('max_wait_seconds', None)
    wait_interval_seconds = kwargs.pop('wait_interval_seconds', None)
    kwargs.pop('from_json', None)

    if isinstance(semantic_store_id, str) and len(semantic_store_id.strip()) == 0:
        raise click.UsageError('Parameter --semantic-store-id cannot be whitespace or empty string')

    if isinstance(enrichment_job_id, str) and len(enrichment_job_id.strip()) == 0:
        raise click.UsageError('Parameter --job-id cannot be whitespace or empty string')

    operation_kwargs = {}
    if if_match is not None:
        operation_kwargs['if_match'] = if_match
    operation_kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    client = cli_util.build_client('generative_ai_data', 'enrichment_job', ctx)
    result = client.cancel_enrichment_job(
        semantic_store_id=semantic_store_id,
        enrichment_job_id=enrichment_job_id,
        **operation_kwargs
    )

    if wait_for_state:
        try:
            wait_period_kwargs = {}
            if max_wait_seconds is not None:
                wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
            if wait_interval_seconds is not None:
                wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

            click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
            result = oci.wait_until(
                client,
                client.get_enrichment_job(semantic_store_id, enrichment_job_id),
                'lifecycle_state',
                wait_for_state,
                **wait_period_kwargs
            )
        except oci.exceptions.MaximumWaitTimeExceeded:
            click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
            cli_util.render_response(result, ctx)
            sys.exit(2)
        except Exception:
            click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
            cli_util.render_response(result, ctx)
            raise

    cli_util.render_response(result, ctx)


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.generate_enrichment_job, params_to_exclude=['enrichment_job_configuration'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.generate_enrichment_job.name, help=enrichmentjob_cli.generate_enrichment_job.help)
@cli_util.option('--configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration': {'module': 'generative_ai_data', 'class': 'EnrichmentJobConfiguration'}, 'freeform-tags': {'module': 'generative_ai_data', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai_data', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def generate_enrichment_job_extended(ctx, **kwargs):
    kwargs['enrichment_job_configuration'] = kwargs.pop('configuration')
    ctx.invoke(enrichmentjob_cli.generate_enrichment_job, **kwargs)


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration, params_to_exclude=['enrichment_job_configuration_schema_name', 'enrichment_job_type'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration.name, help=enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration.help)
@cli_util.option('--schema-name', required=True, help=u"""Name of the DB Schema to be enriched.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'generative_ai_data', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai_data', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def generate_enrichment_job_full_build_extended(ctx, **kwargs):
    kwargs['enrichment_job_configuration_schema_name'] = kwargs.pop('schema_name')
    ctx.invoke(enrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration, params_to_exclude=['enrichment_job_configuration_schema_name', 'enrichment_job_configuration_database_objects', 'enrichment_job_type'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration.name, help=enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration.help)
@cli_util.option('--database-objects', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of the DatabaseObjects to be enriched for the given schema.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--schema-name', required=True, help=u"""Name of the DB Schema to be enriched.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'database-objects': {'module': 'generative_ai_data', 'class': 'list[DatabaseObject]'}, 'freeform-tags': {'module': 'generative_ai_data', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai_data', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def generate_enrichment_job_partial_build_extended(ctx, **kwargs):
    kwargs['enrichment_job_configuration_schema_name'] = kwargs.pop('schema_name')
    kwargs['enrichment_job_configuration_database_objects'] = kwargs.pop('database_objects')
    ctx.invoke(enrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration, params_to_exclude=['enrichment_job_configuration_schema_name', 'enrichment_job_configuration_delta_refresh_schedule', 'enrichment_job_type'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration.name, help=enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration.help)
@cli_util.option('--schema-name', required=True, help=u"""Name of the DB Schema to be enriched.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'generative_ai_data', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai_data', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def generate_enrichment_job_delta_refresh_extended(ctx, **kwargs):
    kwargs['enrichment_job_configuration_schema_name'] = kwargs.pop('schema_name')
    ctx.invoke(enrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(enrichmentjob_cli.get_enrichment_job, params_to_exclude=['enrichment_job_id'])
@enrichmentjob_cli.enrichment_job_root_group.command(name=enrichmentjob_cli.get_enrichment_job.name, help=enrichmentjob_cli.get_enrichment_job.help)
@cli_util.option('--job-id', required=True, help=u"""The OCID of the enrichment job.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'generative_ai_data', 'class': 'EnrichmentJob'})
@cli_util.wrap_exceptions
def get_enrichment_job_extended(ctx, **kwargs):
    kwargs['enrichment_job_id'] = kwargs.pop('job_id')
    ctx.invoke(enrichmentjob_cli.get_enrichment_job, **kwargs)


def _normalize_choice_params(command):
    for param in getattr(command, 'params', []):
        choices = getattr(getattr(param, 'type', None), 'choices', None)
        if isinstance(choices, tuple):
            param.type.choices = list(choices)

    for child in getattr(command, 'commands', {}).values():
        _normalize_choice_params(child)


_normalize_choice_params(enrichmentjob_cli.enrichment_job_root_group)
