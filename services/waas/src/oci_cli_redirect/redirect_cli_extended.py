# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.waas.src.oci_cli_waas.generated import waas_service_cli
from .generated import redirect_cli

waas_service_cli.waas_service_group.commands.pop(redirect_cli.redirect_root_group.name)
waas_service_cli.waas_service_group.add_command(redirect_cli.http_redirect_group)
