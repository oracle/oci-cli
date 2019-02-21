# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function

from .generated import core_service_cli

from oci_cli.cli_root import cli


cli.commands.pop(core_service_cli.core_service_group.name)
