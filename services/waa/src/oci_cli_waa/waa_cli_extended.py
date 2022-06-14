# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.waa.src.oci_cli_waa.generated import waa_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci waa web-app-acceleration create-web-app-acceleration-create-web-app-acceleration-load-balancer-details -> oci waa web-app-acceleration create-for-load-balancer
cli_util.rename_command(waa_cli, waa_cli.web_app_acceleration_group, waa_cli.create_web_app_acceleration_create_web_app_acceleration_load_balancer_details, "create-for-load-balancer")


# oci waa web-app-acceleration purge-web-app-acceleration-cache-purge-entire-web-app-acceleration-cache-details -> oci waa web-app-acceleration purge-entire-cache
cli_util.rename_command(waa_cli, waa_cli.web_app_acceleration_group, waa_cli.purge_web_app_acceleration_cache_purge_entire_web_app_acceleration_cache_details, "purge-entire-cache")


# Remove create from oci waa web-app-acceleration
waa_cli.web_app_acceleration_group.commands.pop(waa_cli.create_web_app_acceleration.name)


# Remove purge-web-app-acceleration-cache from oci waa web-app-acceleration
waa_cli.web_app_acceleration_group.commands.pop(waa_cli.purge_web_app_acceleration_cache.name)
