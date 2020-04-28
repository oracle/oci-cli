# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.resource_search.src.oci_cli_resource_search.generated import resourcesearch_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click

cli_util.rename_command(resourcesearch_cli, resourcesearch_cli.search_root_group, resourcesearch_cli.resource_summary_group, "resource")
cli_util.rename_command(resourcesearch_cli, resourcesearch_cli.resource_summary_group, resourcesearch_cli.search_resources_free_text_search_details, "free-text-search")
cli_util.rename_command(resourcesearch_cli, resourcesearch_cli.resource_summary_group, resourcesearch_cli.search_resources_structured_search_details, "structured-search")

cli_util.override_command_short_help_and_help(resourcesearch_cli.search_resources_free_text_search_details, "Queries any and all compartments in the tenancy to find resources that match the specified criteria. A free text search includes a request containing arbitrary text that must be present in the resource. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute.")

resourcesearch_cli.resource_summary_group.commands.pop(resourcesearch_cli.search_resources.name)
resourcesearch_cli.resource_summary_group.commands.pop(resourcesearch_cli.search_resources_structured_search_details.name)


@cli_util.copy_params_from_generated_command(resourcesearch_cli.search_resources_structured_search_details,
                                             params_to_exclude=['query_parameterconflict'])
@resourcesearch_cli.resource_summary_group.command(name='structured-search', help="""Queries any and all compartments in the tenancy to find resources that match the specified criteria. A structured search includes a request that uses Search's structured query language to specify query conditions that the resource must meet. For information about using structured queries, see Search Language Syntax in the Oracle Cloud Infrastructure User Guide. Results include resources that you have permission to view and can span different resource types. You can also sort results based on a specified resource attribute.""")
@cli_util.option('--query-text', required=True, help="""The structured query describing which resources to search for.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceSummaryCollection'})
@cli_util.wrap_exceptions
def search_resources_structured_search_details(ctx, query_text, **kwargs):
    kwargs['query_parameterconflict'] = query_text
    ctx.invoke(resourcesearch_cli.search_resources_structured_search_details, **kwargs)
