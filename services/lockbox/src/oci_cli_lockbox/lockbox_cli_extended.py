# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from services.lockbox.src.oci_cli_lockbox.generated import lockbox_cli

from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils


# oci oma approval-template-collection --> oci oma approval-template
cli_util.rename_command(lockbox_cli, lockbox_cli.oma_root_group, lockbox_cli.approval_template_collection_group, "approval-templates")

# oci oma approval-template-collection list-approval-templates --> oci oma approval-templates list
cli_util.rename_command(lockbox_cli, lockbox_cli.approval_template_collection_group, lockbox_cli.list_approval_templates, "list")

# oci oma lockbox-collection --> oci oma lockbox
cli_util.rename_command(lockbox_cli, lockbox_cli.oma_root_group, lockbox_cli.lockbox_collection_group, "lockboxes")

# oci oma lockbox-collection list-lockboxes --> oci oma lockboxes list
cli_util.rename_command(lockbox_cli, lockbox_cli.lockbox_collection_group, lockbox_cli.list_lockboxes, "list")

# oci oma access-request-collection --> oci oma access-requests
cli_util.rename_command(lockbox_cli, lockbox_cli.oma_root_group, lockbox_cli.access_request_collection_group, "access-requests")

# oci oma access-request-collection list-access-requests --> oci oma access-requests list
cli_util.rename_command(lockbox_cli, lockbox_cli.access_request_collection_group, lockbox_cli.list_access_requests, "list")

# oci oma work-request-log-entry --> oci oma work-request-log
cli_util.rename_command(lockbox_cli, lockbox_cli.oma_root_group, lockbox_cli.work_request_log_entry_group, "work-request-log")

# oci oma work-request-log-entry list-work-request-logs --> oci oma work-request-log list
cli_util.rename_command(lockbox_cli, lockbox_cli.work_request_log_entry_group, lockbox_cli.list_work_request_logs, "list")


@cli_util.copy_params_from_generated_command(lockbox_cli.create_lockbox,
                                             params_to_exclude=['access_context_attributes'])
@lockbox_cli.lockbox_group.command(name='create', help=lockbox_cli.create_lockbox.help)
@cli_util.option('--context-attributes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'context-attributes': {'module': 'lockbox', 'class': 'AccessContextAttributeCollection'}, 'freeform-tags': {'module': 'lockbox', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'lockbox', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'lockbox', 'class': 'Lockbox'})
@cli_util.wrap_exceptions
def create_lockbox(ctx, **kwargs):
    if 'context_attributes' in kwargs:
        kwargs['access_context_attributes'] = kwargs['context_attributes']
        kwargs.pop('context_attributes')
    # Invoke base method "create_lockbox"
    ctx.invoke(lockbox_cli.create_lockbox, **kwargs)
