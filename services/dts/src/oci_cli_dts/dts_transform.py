# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from oci_cli import cli_util
from services.dts.src.oci_cli_dts.generated import dts_service_cli


class DTS_Transform(object):
    def __init__(self):
        pass

    @staticmethod
    def transform(command_help_override_list=[],
                  group_help_override_list=[],
                  rename_command_list=[],
                  relocate_command_list=[],
                  pop_command_list=[]):
        for item in command_help_override_list:
            cli_util.override_command_short_help_and_help(item["command"], item["help_text"])
        for item in group_help_override_list:
            item["group"].help = item["help_text"]
            item["group"].short_help = item["short_help_text"]
        for item in rename_command_list:
            cli_util.rename_command(dts_service_cli, item["group"], item["old"], item["new"])
        for item in relocate_command_list:
            item["group"].add_command(item["command"])
        for item in pop_command_list:
            item["group"].commands.pop(item["command"])
