# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.pss.src.oci_cli_instance.generated import instance_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci pss work-request-log-entry list-work-request-logs -> oci pss work-request-log-entry list
cli_util.rename_command(instance_cli, instance_cli.work_request_log_entry_group, instance_cli.list_work_request_logs, "list")


# oci pss work-request-log-entry -> oci pss work-request-log
cli_util.rename_command(instance_cli, instance_cli.pss_root_group, instance_cli.work_request_log_entry_group, "work-request-log")


@cli_util.copy_params_from_generated_command(instance_cli.create_instance, params_to_exclude=['admin_identity_domain_user_id'])
@instance_cli.instance_group.command(name=instance_cli.create_instance.name, help=instance_cli.create_instance.help)
@cli_util.option('--admin-user-id', required=True, help=u"""The [OCID] of the identity-domain user that initially administers the PSS instance. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'pss', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'pss', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'pss', 'class': 'Instance'})
@cli_util.wrap_exceptions
def create_instance_extended(ctx, **kwargs):

    if 'admin_user_id' in kwargs:
        kwargs['admin_identity_domain_user_id'] = kwargs['admin_user_id']
        kwargs.pop('admin_user_id')

    ctx.invoke(instance_cli.create_instance, **kwargs)
