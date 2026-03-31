# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.self.src.oci_cli_partner_integeration.generated import partnerintegeration_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci self partner-integeration listing-subscriptions-collection -> oci self partner-integeration listing-subs-collection
cli_util.rename_command(partnerintegeration_cli, partnerintegeration_cli.partner_integeration_root_group, partnerintegeration_cli.listing_subscriptions_collection_group, "listing-subs-collection")


# Remove product from oci self partner-integeration
# partnerintegeration_cli.partner_integeration_root_group.commands.pop(partnerintegeration_cli.product_group.name)
