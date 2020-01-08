# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_root import cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('work_requests.api_gateway_service_group.command_name', 'api-gateway'), cls=CommandGroupWithAlias, help=cli_util.override('work_requests.api_gateway_service_group.help', """API for the API Gateway service. Use this API to manage gateways, deployments, and related items.
For more information, see
[Overview of API Gateway]."""), short_help=cli_util.override('work_requests.api_gateway_service_group.short_help', """API Gateway API"""))
@cli_util.help_option_group
def api_gateway_service_group():
    pass
