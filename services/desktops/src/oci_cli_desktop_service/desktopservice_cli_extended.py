# Copyright (c) 2016, 2024, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click  # noqa: F401
import json  # noqa: F401
from services.desktops.src.oci_cli_desktop_service.generated import desktopservice_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# Shorten 'oci desktops desktop-pool list-desktop-pool-desktops' to 'oci desktops desktop-pool list-desktops'
cli_util.rename_command(desktopservice_cli, desktopservice_cli.desktop_pool_group, desktopservice_cli.list_desktop_pool_desktops, 'list-desktops')

# Shorten 'oci desktops desktop-pool list-desktop-pool-volumes' to 'oci desktops desktop-pool list-volumes'
cli_util.rename_command(desktopservice_cli, desktopservice_cli.desktop_pool_group, desktopservice_cli.list_desktop_pool_volumes, 'list-volumes')

# Move 'oci desktops work-request-error list' to 'oci desktops work-request list-errors'
desktopservice_cli.desktops_root_group.commands.pop(desktopservice_cli.work_request_error_group.name)
desktopservice_cli.work_request_group.add_command(desktopservice_cli.list_work_request_errors, 'list-errors')

# Move 'oci desktops work-request-log-entry list-work-request-logs' to 'oci desktops work-request list-logs'
desktopservice_cli.desktops_root_group.commands.pop(desktopservice_cli.work_request_log_entry_group.name)
desktopservice_cli.work_request_group.add_command(desktopservice_cli.list_work_request_logs, 'list-logs')
