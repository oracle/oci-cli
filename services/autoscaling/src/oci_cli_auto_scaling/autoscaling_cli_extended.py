# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci_cli import cli_util
from oci_cli_auto_scaling.generated import autoscaling_cli

autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.create_auto_scaling_policy_create_threshold_policy_details.name)
autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.update_auto_scaling_policy_update_threshold_policy_details.name)

cli_util.rename_command(autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_configuration_group, "configuration")
cli_util.rename_command(autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_policy_group, "policy")
