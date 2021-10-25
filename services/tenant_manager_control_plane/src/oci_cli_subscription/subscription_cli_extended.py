# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.tenant_manager_control_plane.src.oci_cli_subscription.generated import subscription_cli
from services.tenant_manager_control_plane.src.oci_cli_tenant_manager_control_plane.generated import organizations_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# Move commands under 'oci organizations subscription' -> 'oci organizations'
organizations_service_cli.organizations_service_group.commands.pop(subscription_cli.subscription_root_group.name)
organizations_service_cli.organizations_service_group.add_command(subscription_cli.subscription_mapping_group)
organizations_service_cli.organizations_service_group.add_command(subscription_cli.assigned_subscription_group)
organizations_service_cli.organizations_service_group.add_command(subscription_cli.subscription_group)
