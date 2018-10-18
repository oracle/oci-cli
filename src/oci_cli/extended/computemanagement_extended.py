# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from ..generated import computemanagement_cli


# hide compute management 'instances' group, commands belong under other groups
computemanagement_cli.compute_management_root_group.commands.pop(computemanagement_cli.instance_group.name)

computemanagement_cli.instance_pool_group.add_command(computemanagement_cli.list_instance_pool_instances)
computemanagement_cli.instance_configuration_group.add_command(computemanagement_cli.launch_instance_configuration_compute_instance_details)
