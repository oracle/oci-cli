# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.limits.src.oci_cli_limits.generated import limits_service_cli
from services.limits.src.oci_cli_limits.generated import limits_cli
from oci_cli import cli_util

# rename limit-definition command to definition
cli_util.rename_command(limits_cli, limits_service_cli.limits_service_group, limits_cli.limit_definition_group, "definition")

# rename limit-value command to value
cli_util.rename_command(limits_cli, limits_service_cli.limits_service_group, limits_cli.limit_value_group, "value")
