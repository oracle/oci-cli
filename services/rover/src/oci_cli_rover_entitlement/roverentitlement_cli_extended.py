# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_rover_entitlement.generated import roverentitlement_cli

rover_service_cli.rover_service_group.commands.pop(roverentitlement_cli.rover_entitlement_root_group.name)
