# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli
from services.apigateway.src.oci_cli_usage_plans.generated import usageplans_cli

# Changing from the following:
# oci api-gateway usage-plans usage-plan [OPTIONS] COMMAND [ARGS]...

# To:
# oci api-gateway usage-plan [OPTIONS] COMMAND [ARGS]...

api_gateway_service_cli.api_gateway_service_group.commands.pop(usageplans_cli.usage_plans_root_group.name)
api_gateway_service_cli.api_gateway_service_group.add_command(usageplans_cli.usage_plan_group)
