# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli
from services.apigateway.src.oci_cli_deployment.generated import deployment_cli
from oci_cli import cli_util

# Changing from the following:
# oci api-gateway deployment deployment create --compartment-id, --display-name, --gateway-id, --path-prefix, --specification, --defined-tags, --freeform-tags
# oci api-gateway deployment deployment delete --deployment-id, --force
# oci api-gateway deployment deployment get --deployment-id
# oci api-gateway deployment deployment update --deployment-id, --defined-tags, --display-name, --force, --freeform-tags, --specification
# oci api-gateway deployment deployment-summary list-deployments --compartment-id, --all-pages, --display-name, --gateway-id
# oci api-gateway deployment deployment change-compartment --deployment-id, --compartment-id

# To:
# oci api-gateway deployment create --compartment-id, --display-name, --gateway-id, --path-prefix, --specification, --defined-tags, --freeform-tags
# oci api-gateway deployment delete --deployment-id, --force
# oci api-gateway deployment get --deployment-id
# oci api-gateway deployment update --deployment-id, --defined-tags, --display-name, --force, --freeform-tags, --specification
# oci api-gateway deployment list --compartment-id, --all-pages, --display-name, --gateway-id
# oci api-gateway deployment change-compartment --deployment-id, --compartment-id

cli_util.rename_command(deployment_cli, deployment_cli.deployment_group, deployment_cli.list_deployments, "list")
api_gateway_service_cli.api_gateway_service_group.commands.pop(deployment_cli.deployment_root_group.name)
api_gateway_service_cli.api_gateway_service_group.add_command(deployment_cli.deployment_group)
