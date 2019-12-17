# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_cli
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_util

# marketplace category-summary list-categories -> marketplace category list
cli_util.rename_command(marketplace_cli, marketplace_cli.marketplace_root_group, marketplace_cli.category_summary_group, "category")
cli_util.rename_command(marketplace_cli, marketplace_cli.category_summary_group, marketplace_cli.list_categories, "list")

# marketplace listing-package list-packages -> marketplace package list
# marketplace listing-package get-package -> marketplace package get
cli_util.rename_command(marketplace_cli, marketplace_cli.marketplace_root_group, marketplace_cli.listing_package_group, "package")
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_group, marketplace_cli.list_packages, "list")
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_group, marketplace_cli.get_package, "get")
