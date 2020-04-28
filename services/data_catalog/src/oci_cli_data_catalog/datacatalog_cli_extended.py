# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.data_catalog.src.oci_cli_data_catalog.generated import datacatalog_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import click
from oci_cli.aliasing import CommandGroupWithAlias

'''
In the generated docs we appear as "DataCatalog" by default.
'''

datacatalog_cli.data_catalog_root_group.short_help = "Data Catalog"

'''
We have spurious commands, resulting from our use of returned Collection object
in list calls. Each contains a "list" command but that has been misnamed.

Do the following for each:
1. Remove misnamed list subcommand from the command.
2. Add it to the correct command.
3. Rename it to the intended "list".
4. Remove the command.
'''

# oci data-catalog attribute-collection list-attributes -->
# oci data-catalog attribute list
datacatalog_cli.attribute_collection_group.commands.pop(datacatalog_cli.list_attributes.name)
datacatalog_cli.attribute_group.add_command(datacatalog_cli.list_attributes)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.attribute_group, datacatalog_cli.list_attributes, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.attribute_collection_group.name)

# oci data-catalog attribute-tag-collection list-attribute-tags -->
# oci data-catalog attribute-tag list
datacatalog_cli.attribute_tag_collection_group.commands.pop(datacatalog_cli.list_attribute_tags.name)
datacatalog_cli.attribute_tag_group.add_command(datacatalog_cli.list_attribute_tags)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.attribute_tag_group, datacatalog_cli.list_attribute_tags, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.attribute_tag_collection_group.name)

# oci data-catalog connection-collection list-connections -->
# oci data-catalog connection list
datacatalog_cli.connection_collection_group.commands.pop(datacatalog_cli.list_connections.name)
datacatalog_cli.connection_group.add_command(datacatalog_cli.list_connections)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.connection_group, datacatalog_cli.list_connections, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.connection_collection_group.name)

# oci data-catalog data-asset-collection list-data-assets -->
# oci data-catalog data-asset list
datacatalog_cli.data_asset_collection_group.commands.pop(datacatalog_cli.list_data_assets.name)
datacatalog_cli.data_asset_group.add_command(datacatalog_cli.list_data_assets)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.data_asset_group, datacatalog_cli.list_data_assets, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.data_asset_collection_group.name)

# oci data-catalog data-asset-tag-collection list-data-asset-tags -->
# oci data-catalog data-asset-tag list
datacatalog_cli.data_asset_tag_collection_group.commands.pop(datacatalog_cli.list_data_asset_tags.name)
datacatalog_cli.data_asset_tag_group.add_command(datacatalog_cli.list_data_asset_tags)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.data_asset_tag_group, datacatalog_cli.list_data_asset_tags, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.data_asset_tag_collection_group.name)

# oci data-catalog oci data-catalog entity-tag-collection list-entity-tags -->
# oci data-catalog entity-tag list
datacatalog_cli.entity_tag_collection_group.commands.pop(datacatalog_cli.list_entity_tags.name)
datacatalog_cli.entity_tag_group.add_command(datacatalog_cli.list_entity_tags)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.entity_tag_group, datacatalog_cli.list_entity_tags, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.entity_tag_collection_group.name)

# oci data-catalog folder-collection list-folders -->
# oci data-catalog folder list
datacatalog_cli.folder_collection_group.commands.pop(datacatalog_cli.list_folders.name)
datacatalog_cli.folder_group.add_command(datacatalog_cli.list_folders)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.folder_group, datacatalog_cli.list_folders, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.folder_collection_group.name)

# oci data-catalog folder-tag-collection list-folder-tags -->
# oci data-catalog folder-tag list
datacatalog_cli.folder_tag_collection_group.commands.pop(datacatalog_cli.list_folder_tags.name)
datacatalog_cli.folder_tag_group.add_command(datacatalog_cli.list_folder_tags)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.folder_tag_group, datacatalog_cli.list_folder_tags, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.folder_tag_collection_group.name)

# oci data-catalog job-collection list-jobs -->
# oci data-catalog job list
datacatalog_cli.job_collection_group.commands.pop(datacatalog_cli.list_jobs.name)
datacatalog_cli.job_group.add_command(datacatalog_cli.list_jobs)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.job_group, datacatalog_cli.list_jobs, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.job_collection_group.name)

# oci data-catalog job-definition-collection list-job-definitions -->
# oci data-catalog job-definition list
datacatalog_cli.job_definition_collection_group.commands.pop(datacatalog_cli.list_job_definitions.name)
datacatalog_cli.job_definition_group.add_command(datacatalog_cli.list_job_definitions)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.job_definition_group, datacatalog_cli.list_job_definitions, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.job_definition_collection_group.name)

# oci data-catalog job-execution-collection list-job-executions  -->
# oci data-catalog job-execution list
datacatalog_cli.job_execution_collection_group.commands.pop(datacatalog_cli.list_job_executions.name)
datacatalog_cli.job_execution_group.add_command(datacatalog_cli.list_job_executions)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.job_execution_group, datacatalog_cli.list_job_executions, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.job_execution_collection_group.name)

# oci data-catalog job-log-collection list-job-logs  -->
# oci data-catalog job-log list
datacatalog_cli.job_log_collection_group.commands.pop(datacatalog_cli.list_job_logs.name)
datacatalog_cli.job_log_group.add_command(datacatalog_cli.list_job_logs)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.job_log_group, datacatalog_cli.list_job_logs, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.job_log_collection_group.name)

# oci data-catalog job-metric-collection list-job-metrics  -->
# oci data-catalog job-metric list
datacatalog_cli.job_metric_collection_group.commands.pop(datacatalog_cli.list_job_metrics.name)
datacatalog_cli.job_metric_group.add_command(datacatalog_cli.list_job_metrics)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.job_metric_group, datacatalog_cli.list_job_metrics, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.job_metric_collection_group.name)

# oci data-catalog type-collection list-types  -->
# oci data-catalog type list
datacatalog_cli.type_collection_group.commands.pop(datacatalog_cli.list_types.name)
datacatalog_cli.type_group.add_command(datacatalog_cli.list_types)
cli_util.rename_command(datacatalog_cli, datacatalog_cli.type_group, datacatalog_cli.list_types, "list")

datacatalog_cli.data_catalog_root_group.commands.pop(datacatalog_cli.type_collection_group.name)

'''
Additional changes.
- Add a new tag command.
- Move the term list-tags subcommand under tag.
- Rename the search command/subcommand to make more sense as exposed via the CLI.
'''

# oci data-catalog term list-tags  -->
# oci data-catalog tags list
datacatalog_cli.term_group.commands.pop(datacatalog_cli.list_tags.name)


@click.command('tag', cls=CommandGroupWithAlias, help="""A free-form label or keyword you create to be able to logically group data objects.""")
@cli_util.help_option_group
def tag_group():
    pass


datacatalog_cli.data_catalog_root_group.add_command(tag_group)
cli_util.rename_command(datacatalog_cli, tag_group, datacatalog_cli.list_tags, "list")

# oci data-catalog search-result search-criteria  -->
# oci data-catalog search query
cli_util.rename_command(datacatalog_cli, datacatalog_cli.data_catalog_root_group, datacatalog_cli.search_result_group, "search")
datacatalog_cli.search_result_group.commands.pop(datacatalog_cli.search_criteria.name)


@cli_util.copy_params_from_generated_command(datacatalog_cli.search_criteria, params_to_exclude=['query_parameterconflict'])
@datacatalog_cli.search_result_group.command(name='query', help=u"""Returns a list of search results within a data catalog.""")
@cli_util.option('--query-text', help=u"""Search query dsl that defines the query components including fields and predicates.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'SearchResultCollection'})
@cli_util.wrap_exceptions
def search_criteria_extended(ctx, **kwargs):
    if 'query_text' in kwargs and kwargs['query_text']:
        kwargs['query_parameterconflict'] = kwargs['query_text']
    kwargs.pop('query_text')
    ctx.invoke(datacatalog_cli.search_criteria, **kwargs)
