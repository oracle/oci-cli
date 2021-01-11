# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from services.apigateway.src.oci_cli_apigateway.generated import api_gateway_service_cli
from services.apigateway.src.oci_cli_work_requests.generated import workrequests_cli
from oci_cli import cli_util

# Changing from the following:
# oci api-gateway work-requests work-request get --work-request-id
# oci api-gateway work-requests work-request cancel --work-request-id
# oci api-gateway work-requests work-request-error list --work-request-id, --all-pages
# oci api-gateway work-requests work-request-log list --work-request-id, --all-pages
# oci api-gateway work-requests work-request-summary list-work-requests --compartment-id, --all-pages

# To:
# oci api-gateway work-request get --work-request-id
# oci api-gateway work-request cancel --work-request-id
# oci api-gateway work-request-error list --work-request-id, --all-pages
# oci api-gateway work-request-log list --work-request-id, --all-pages
# oci api-gateway work-request list --compartment-id, --all-pages

cli_util.rename_command(api_gateway_service_cli, workrequests_cli.work_request_group, workrequests_cli.list_work_requests, "list")
api_gateway_service_cli.api_gateway_service_group.commands.pop(workrequests_cli.work_requests_root_group.name)
api_gateway_service_cli.api_gateway_service_group.add_command(workrequests_cli.work_request_log_group)
api_gateway_service_cli.api_gateway_service_group.add_command(workrequests_cli.work_request_error_group)
api_gateway_service_cli.api_gateway_service_group.add_command(workrequests_cli.work_request_group)
