# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates. All rights reserved.

from oci_cli import cli_util

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_shape.generated import shape_cli

cli_util.rename_command(rover_service_cli, rover_service_cli.rover_service_group, shape_cli.shape_root_group, 'shape')
cli_util.rename_command(rover_service_cli, shape_cli.shape_root_group, shape_cli.list_shapes, 'list')
shape_cli.shape_root_group.commands.pop(shape_cli.shape_summary_group.name)
