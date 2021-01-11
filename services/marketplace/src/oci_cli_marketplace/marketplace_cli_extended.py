# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_cli
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_util

# marketplace category-summary list-categories -> marketplace category list
cli_util.rename_command(marketplace_cli, marketplace_cli.marketplace_root_group, marketplace_cli.category_summary_group, "category")
cli_util.rename_command(marketplace_cli, marketplace_cli.category_summary_group, marketplace_cli.list_categories, "list")

marketplace_cli.marketplace_root_group.commands.pop(marketplace_cli.listing_package_summary_group.name)

# marketplace listing-package list-packages -> marketplace package list
# marketplace listing-package get-package -> marketplace package get
cli_util.rename_command(marketplace_cli, marketplace_cli.marketplace_root_group, marketplace_cli.listing_package_group, "package")
cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_group, marketplace_cli.get_package, "get")

cli_util.rename_command(marketplace_cli, marketplace_cli.listing_package_summary_group, marketplace_cli.list_packages, "list")
marketplace_cli.listing_package_group.add_command(marketplace_cli.list_packages)
