# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function

from oci_cli_compute_management.generated import computemanagement_cli

from oci_cli.cli_root import cli
from oci_cli import cli_util

cli.add_command(computemanagement_cli.compute_management_root_group)
cli_util.rename_command(computemanagement_cli.instance_pool_group, computemanagement_cli.list_instance_pool_instances, "list-instances")
cli_util.rename_command(computemanagement_cli.instance_configuration_group, computemanagement_cli.launch_instance_configuration_compute_instance_details, "launch-compute-instance")

# hide compute management 'instances' group, commands belong under other groups
computemanagement_cli.compute_management_root_group.commands.pop(computemanagement_cli.instance_group.name)
computemanagement_cli.instance_pool_group.add_command(computemanagement_cli.list_instance_pool_instances)
computemanagement_cli.instance_configuration_group.add_command(computemanagement_cli.launch_instance_configuration_compute_instance_details)

cli_util.rename_command(computemanagement_cli.instance_configuration_group, computemanagement_cli.launch_instance_configuration_compute_instance_details, "launch-compute-instance")
computemanagement_cli.compute_management_root_group.help = "Compute Management Service CLI"
computemanagement_cli.compute_management_root_group.short_help = "Compute Management Service"

cli_util.rename_command(computemanagement_cli.instance_pool_group, computemanagement_cli.attach_load_balancer, "attach-lb")
cli_util.rename_command(computemanagement_cli.instance_pool_group, computemanagement_cli.detach_load_balancer, "detach-lb")
