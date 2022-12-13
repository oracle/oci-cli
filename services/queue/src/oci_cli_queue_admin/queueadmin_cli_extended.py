# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.queue.src.oci_cli_queue_admin.generated import queueadmin_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci queue queue-admin work-request-error-collection list-work-request-errors -> oci queue queue-admin work-request-error-collection list
cli_util.rename_command(queueadmin_cli, queueadmin_cli.work_request_error_collection_group, queueadmin_cli.list_work_request_errors, "list")


# oci queue queue-admin work-request-log-entry-collection list-work-request-logs -> oci queue queue-admin work-request-log-entry-collection list
cli_util.rename_command(queueadmin_cli, queueadmin_cli.work_request_log_entry_collection_group, queueadmin_cli.list_work_request_logs, "list")


# oci queue queue-admin work-request-error-collection -> oci queue queue-admin work-request-error
cli_util.rename_command(queueadmin_cli, queueadmin_cli.queue_admin_root_group, queueadmin_cli.work_request_error_collection_group, "work-request-error")


# oci queue queue-admin work-request-log-entry-collection -> oci queue queue-admin work-request-log
cli_util.rename_command(queueadmin_cli, queueadmin_cli.queue_admin_root_group, queueadmin_cli.work_request_log_entry_collection_group, "work-request-log")


# oci queue queue-admin queue-collection list-queues -> oci queue queue-admin queue-collection list
cli_util.rename_command(queueadmin_cli, queueadmin_cli.queue_collection_group, queueadmin_cli.list_queues, "list")


# oci queue queue-admin work-request-summary-collection list-work-requests -> oci queue queue-admin work-request-summary-collection list
cli_util.rename_command(queueadmin_cli, queueadmin_cli.work_request_summary_collection_group, queueadmin_cli.list_work_requests, "list")


# Remove queue-collection from oci queue queue-admin
queueadmin_cli.queue_admin_root_group.commands.pop(queueadmin_cli.queue_collection_group.name)


# Remove work-request-summary-collection from oci queue queue-admin
queueadmin_cli.queue_admin_root_group.commands.pop(queueadmin_cli.work_request_summary_collection_group.name)


# oci queue queue-admin queue-collection list-queues -> oci queue queue-admin queue
queueadmin_cli.queue_collection_group.commands.pop(queueadmin_cli.list_queues.name)
queueadmin_cli.queue_group.add_command(queueadmin_cli.list_queues)


# oci queue queue-admin work-request-summary-collection list-work-requests -> oci queue queue-admin work-request
queueadmin_cli.work_request_summary_collection_group.commands.pop(queueadmin_cli.list_work_requests.name)
queueadmin_cli.work_request_group.add_command(queueadmin_cli.list_work_requests)


@cli_util.copy_params_from_generated_command(queueadmin_cli.create_queue, params_to_exclude=['dead_letter_queue_delivery_count', 'custom_encryption_key_id'])
@queueadmin_cli.queue_group.command(name=queueadmin_cli.create_queue.name, help=queueadmin_cli.create_queue.help)
@cli_util.option('--custom-key', help="""Id of the custom master encryption key which will be used to encrypt messages content""")
@cli_util.option('--dlq-delivery-count', type=click.INT, help=u"""The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'queue', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'queue', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_queue_extended(ctx, **kwargs):

    if 'custom_key' in kwargs:
        kwargs['custom_encryption_key_id'] = kwargs['custom_key']
        kwargs.pop('custom_key')

    if 'dlq_delivery_count' in kwargs:
        kwargs['dead_letter_queue_delivery_count'] = kwargs['dlq_delivery_count']
        kwargs.pop('dlq_delivery_count')

    ctx.invoke(queueadmin_cli.create_queue, **kwargs)


@cli_util.copy_params_from_generated_command(queueadmin_cli.update_queue, params_to_exclude=['dead_letter_queue_delivery_count', 'custom_encryption_key_id'])
@queueadmin_cli.queue_group.command(name=queueadmin_cli.update_queue.name, help=queueadmin_cli.update_queue.help)
@cli_util.option('--custom-key', help="""Id of the custom master encryption key which will be used to encrypt messages content. String of length 0 means the custom key should be removed from queue""")
@cli_util.option('--dlq-delivery-count', type=click.INT, help=u"""The number of times a message can be delivered to a consumer before being moved to the dead letter queue. A value of 0 indicates that the DLQ is not used. Changing that value to a lower threshold does not retro-actively move in-flight messages in the dead letter queue.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'queue', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'queue', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_queue_extended(ctx, **kwargs):

    if 'custom_key' in kwargs:
        kwargs['custom_encryption_key_id'] = kwargs['custom_key']
        kwargs.pop('custom_key')

    if 'dlq_delivery_count' in kwargs:
        kwargs['dead_letter_queue_delivery_count'] = kwargs['dlq_delivery_count']
        kwargs.pop('dlq_delivery_count')

    ctx.invoke(queueadmin_cli.update_queue, **kwargs)
