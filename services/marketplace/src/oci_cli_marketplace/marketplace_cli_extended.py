# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click  # noqa: F401
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_cli
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# marketplace category-summary list-categories -> marketplace category list
cli_util.rename_command(marketplace_service_cli, marketplace_service_cli.marketplace_service_group, marketplace_cli.category_summary_group, "category")
cli_util.rename_command(marketplace_cli, marketplace_cli.category_summary_group, marketplace_cli.list_categories, "list")

marketplace_service_cli.marketplace_service_group.commands.pop(marketplace_cli.listing_package_summary_group.name)

# marketplace listing-package list-packages -> marketplace package list
# marketplace listing-package get-package -> marketplace package get
cli_util.rename_command(marketplace_service_cli, marketplace_service_cli.marketplace_service_group, marketplace_cli.listing_package_group, "package")
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_summary_group, marketplace_cli.list_packages, "list")
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_group, marketplace_cli.get_package, "get")

marketplace_cli.listing_package_group.add_command(marketplace_cli.list_packages)

# oci marketplace listing-summary search-listings-structured-search-details -> oci marketplace listing-summary search-listings-structured
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_summary_group, marketplace_cli.search_listings_structured_search_details, "search-listings-structured")

# oci marketplace listing-summary search-listings-free-text-search-details -> oci marketplace listing-summary search-listings-free-text
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_summary_group, marketplace_cli.search_listings_free_text_search_details, "search-listings-free-text")


@cli_util.copy_params_from_generated_command(marketplace_cli.search_listings_structured_search_details, params_to_exclude=['query_parameterconflict'])
@marketplace_cli.listing_summary_group.command(name=marketplace_cli.search_listings_structured_search_details.name, help=marketplace_cli.search_listings_structured_search_details.help)
@cli_util.option('---search-query', required=True, help=u"""The structured query describing which resources to search for. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def search_listings_structured_search_details_extended(ctx, **kwargs):
    if '_search_query' in kwargs:
        kwargs['query_parameterconflict'] = kwargs['_search_query']
        kwargs.pop('_search_query')

    ctx.invoke(marketplace_cli.search_listings_structured_search_details, **kwargs)


@cli_util.copy_params_from_generated_command(marketplace_cli.search_listings_free_text_search_details, params_to_exclude=['text'])
@marketplace_cli.listing_summary_group.command(name=marketplace_cli.search_listings_free_text_search_details.name, help=marketplace_cli.search_listings_free_text_search_details.help)
@cli_util.option('---search-text', required=True, help=u"""The text to search for. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def search_listings_free_text_search_details_extended(ctx, **kwargs):
    if '_search_text' in kwargs:
        kwargs['text'] = kwargs['_search_text']
        kwargs.pop('_search_text')

    ctx.invoke(marketplace_cli.search_listings_free_text_search_details, **kwargs)
