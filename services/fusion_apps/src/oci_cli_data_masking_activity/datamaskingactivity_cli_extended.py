# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_data_masking_activity.generated import datamaskingactivity_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps data-masking-activity data-masking-activity' -> 'oci fusion-apps data-masking-activity'
datamaskingactivity_cli.data_masking_activity_root_group.commands.pop(datamaskingactivity_cli.data_masking_activity_group.name)
datamaskingactivity_cli.data_masking_activity_root_group.add_command(datamaskingactivity_cli.create_data_masking_activity)
datamaskingactivity_cli.data_masking_activity_root_group.add_command(datamaskingactivity_cli.get_data_masking_activity)
datamaskingactivity_cli.data_masking_activity_root_group.add_command(datamaskingactivity_cli.list_data_masking_activities)
