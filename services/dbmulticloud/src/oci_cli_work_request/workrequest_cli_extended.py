# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_work_request.generated import workrequest_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci dbmulticloud work-request work-request' -> 'oci dbmulticloud work-request'
workrequest_cli.work_request_root_group.commands.pop(workrequest_cli.work_request_group.name)
workrequest_cli.work_request_root_group.add_command(workrequest_cli.cancel_work_request)
workrequest_cli.work_request_root_group.add_command(workrequest_cli.get_work_request)
workrequest_cli.work_request_root_group.add_command(workrequest_cli.list_work_requests)
