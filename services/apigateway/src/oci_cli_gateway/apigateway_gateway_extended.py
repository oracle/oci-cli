# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from oci_cli import cli_util

from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli
from services.apigateway.src.oci_cli_gateway.generated import gateway_cli

# Changing from the following:
# oci api-gateway gateway gateway create --compartment-id, --display-name, --endpoint-type, --subnet-id, --defined-tags, --freeform-tags
# oci api-gateway gateway gateway delete --gateway-id, --force
# oci api-gateway gateway gateway get --gateway-id
# oci api-gateway gateway gateway update --gateway-id, --defined-tags, --display-name, --force, --freeform-tags
# oci api-gateway gateway gateway-summary list-gateways --compartment-id, --all-pages, --display-name
# oci api-gateway gateway gateway change-compartment --gateway-id, --compartment-id

# To:
# oci api-gateway gateway create --compartment-id, --display-name, --endpoint-type, --subnet-id, --defined-tags, --freeform-tags
# oci api-gateway gateway delete --gateway-id, --force
# oci api-gateway gateway get --gateway-id
# oci api-gateway gateway update --gateway-id, --defined-tags, --display-name, --force, --freeform-tags
# oci api-gateway gateway list --compartment-id, --all-pages, --display-name
# oci api-gateway gateway change-compartment --gateway-id, --compartment-id

cli_util.rename_command(gateway_cli, gateway_cli.gateway_group, gateway_cli.list_gateways, "list")
api_gateway_service_cli.api_gateway_service_group.commands.pop(gateway_cli.gateway_root_group.name)
api_gateway_service_cli.api_gateway_service_group.add_command(gateway_cli.gateway_group)


# Remove create-gateway-external-resp-cache from oci api-gateway gateway
gateway_cli.gateway_group.commands.pop(gateway_cli.create_gateway_external_resp_cache.name)


# Remove create-gateway-no-cache from oci api-gateway gateway
gateway_cli.gateway_group.commands.pop(gateway_cli.create_gateway_no_cache.name)


# Remove update-gateway-external-resp-cache from oci api-gateway gateway
gateway_cli.gateway_group.commands.pop(gateway_cli.update_gateway_external_resp_cache.name)


# Remove update-gateway-no-cache from oci api-gateway gateway
gateway_cli.gateway_group.commands.pop(gateway_cli.update_gateway_no_cache.name)


# oci api-gateway gateway add -> oci api-gateway gateway add-lock
cli_util.rename_command(gateway_cli, gateway_cli.gateway_group, gateway_cli.add_gateway_lock, "add-lock")


# oci api-gateway gateway remove -> oci api-gateway gateway remove-lock
cli_util.rename_command(gateway_cli, gateway_cli.gateway_group, gateway_cli.remove_gateway_lock, "remove-lock")
