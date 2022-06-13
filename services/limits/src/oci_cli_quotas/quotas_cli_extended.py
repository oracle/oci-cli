# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.limits.src.oci_cli_limits.generated import limits_service_cli
from services.limits.src.oci_cli_quotas.generated import quotas_cli
from oci_cli import cli_util


# remove quotas token from commands
limits_service_cli.limits_service_group.commands.pop(quotas_cli.quotas_root_group.name)
limits_service_cli.limits_service_group.add_command(quotas_cli.quota_group)

# oci limits quota add -> oci limits quota addlock
cli_util.rename_command(quotas_cli, quotas_cli.quota_group, quotas_cli.add_quota_lock, "addlock")

# oci limits quota remove -> oci limits quota removelock
cli_util.rename_command(quotas_cli, quotas_cli.quota_group, quotas_cli.remove_quota_lock, "removelock")
