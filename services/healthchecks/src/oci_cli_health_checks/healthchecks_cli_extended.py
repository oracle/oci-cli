# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli_health_checks.generated import healthchecks_cli
from oci_cli.cli_root import cli
from oci_cli import cli_util

cli_util.rename_command(cli, healthchecks_cli.healthchecks_root_group, "health-checks")
cli_util.rename_command(healthchecks_cli.healthchecks_root_group, healthchecks_cli.health_checks_vantage_point_group, "vantage-point")
