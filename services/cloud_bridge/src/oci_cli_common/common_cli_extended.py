# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.cloud_bridge.src.oci_cli_common.generated import common_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci cloud-bridge common work-request-log-entry list-work-request-logs -> oci cloud-bridge common work-request-log-entry list
cli_util.rename_command(common_cli, common_cli.work_request_log_entry_group, common_cli.list_work_request_logs, "list")
