# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.oda.src.oci_cli_oda.generated import oda_cli, oda_service_cli
from oci_cli import cli_util

# Rename sub-command oda-instance to instance.
cli_util.rename_command(oda_service_cli, oda_service_cli.oda_service_group, oda_cli.oda_instance_group, 'instance')
cli_util.rename_command(oda_cli, oda_cli.work_request_log_entry_group, oda_cli.list_work_request_logs, 'list')
