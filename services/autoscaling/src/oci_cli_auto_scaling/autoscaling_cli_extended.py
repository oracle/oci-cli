# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci_cli import cli_util
from services.autoscaling.src.oci_cli_auto_scaling.generated import autoscaling_cli

autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.create_auto_scaling_policy_create_threshold_policy_details.name)
autoscaling_cli.auto_scaling_policy_group.commands.pop(autoscaling_cli.update_auto_scaling_policy_update_threshold_policy_details.name)
autoscaling_cli.auto_scaling_configuration_group.commands.pop(autoscaling_cli.create_auto_scaling_configuration_instance_pool_resource.name)

cli_util.rename_command(autoscaling_cli, autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_configuration_group, "configuration")
cli_util.rename_command(autoscaling_cli, autoscaling_cli.autoscaling_root_group, autoscaling_cli.auto_scaling_policy_group, "policy")
