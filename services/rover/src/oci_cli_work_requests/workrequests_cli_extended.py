# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_work_requests.generated import workrequests_cli

rover_service_cli.rover_service_group.commands.pop(workrequests_cli.work_requests_root_group.name)
