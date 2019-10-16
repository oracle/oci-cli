# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.oda.src.oci_cli_oda.generated import oda_cli
from oci_cli import cli_util

# Rename sub-command oda-instance to instance.
cli_util.rename_command(oda_cli, oda_cli.oda_root_group, oda_cli.oda_instance_group, 'instance')
cli_util.rename_command(oda_cli, oda_cli.work_request_log_entry_group, oda_cli.list_work_request_logs, 'list')
