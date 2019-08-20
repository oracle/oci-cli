# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.limits.src.oci_cli_limits.generated import limits_service_cli
from services.limits.src.oci_cli_quotas.generated import quotas_cli

# remove quotas token from commands
limits_service_cli.limits_service_group.commands.pop(quotas_cli.quotas_root_group.name)
limits_service_cli.limits_service_group.add_command(quotas_cli.quota_group)
