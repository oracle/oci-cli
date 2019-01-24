# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function

from oci_cli.generated import computemanagement_cli

from oci_cli.cli_root import cli


cli.add_command(computemanagement_cli.compute_management_root_group)
