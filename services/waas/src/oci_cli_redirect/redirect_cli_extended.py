# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.waas.src.oci_cli_waas.generated import waas_service_cli
from .generated import redirect_cli

waas_service_cli.waas_service_group.commands.pop(redirect_cli.redirect_root_group.name)
waas_service_cli.waas_service_group.add_command(redirect_cli.http_redirect_group)
