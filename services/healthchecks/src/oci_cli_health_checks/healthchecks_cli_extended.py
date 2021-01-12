# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.healthchecks.src.oci_cli_health_checks.generated import healthchecks_cli
from oci_cli import cli_util

cli_util.rename_command(healthchecks_cli, healthchecks_cli.health_checks_root_group, healthchecks_cli.health_checks_vantage_point_group, "vantage-point")
