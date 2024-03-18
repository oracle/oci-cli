# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
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
import click  # noqa: F401
import json  # noqa: F401
from services.apm_traces.src.oci_cli_attributes.generated import attributes_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci apm-traces attributes bulk-activation-status bulk-activate-attribute -> oci apm-traces attributes bulk-activation-status activate
cli_util.rename_command(attributes_cli, attributes_cli.bulk_activation_status_group, attributes_cli.bulk_activate_attribute, "activate")


# oci apm-traces attributes bulk-de-activation-status bulk-de-activate-attribute -> oci apm-traces attributes bulk-de-activation-status deactivate
cli_util.rename_command(attributes_cli, attributes_cli.bulk_de_activation_status_group, attributes_cli.bulk_de_activate_attribute, "deactivate")


# oci apm-traces attributes bulk-pin-status bulk-pin-attribute -> oci apm-traces attributes bulk-pin-status pin
cli_util.rename_command(attributes_cli, attributes_cli.bulk_pin_status_group, attributes_cli.bulk_pin_attribute, "pin")


# oci apm-traces attributes bulk-unpin-status bulk-unpin-attribute -> oci apm-traces attributes bulk-unpin-status unpin
cli_util.rename_command(attributes_cli, attributes_cli.bulk_unpin_status_group, attributes_cli.bulk_unpin_attribute, "unpin")


# oci apm-traces attributes bulk-update-notes-status bulk-update-attribute-notes -> oci apm-traces attributes bulk-update-notes-status update-notes
cli_util.rename_command(attributes_cli, attributes_cli.bulk_update_notes_status_group, attributes_cli.bulk_update_attribute_notes, "update-notes")


# oci apm-traces attributes auto-activate-status get-status-auto-activate -> oci apm-traces attributes auto-activate-status auto-activate-status
cli_util.rename_command(attributes_cli, attributes_cli.auto_activate_status_group, attributes_cli.get_status_auto_activate, "auto-activate-status")


# oci apm-traces attributes auto-activate-toggle-status put-toggle-auto-activate -> oci apm-traces attributes auto-activate-toggle-status update-auto-activate
cli_util.rename_command(attributes_cli, attributes_cli.auto_activate_toggle_status_group, attributes_cli.put_toggle_auto_activate, "update-auto-activate")

# oci apm-traces attributes bulk-update-attribute-status bulk-update-attribute -> oci apm-traces attributes update-attribute
cli_util.rename_command(attributes_cli, attributes_cli.bulk_update_attribute_status_group, attributes_cli.bulk_update_attribute, "update-attribute")


# Move commands under 'oci apm-traces attributes auto-activate-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.auto_activate_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.get_status_auto_activate)


# Move commands under 'oci apm-traces attributes auto-activate-toggle-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.auto_activate_toggle_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.put_toggle_auto_activate)


# Move commands under 'oci apm-traces attributes bulk-activation-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_activation_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_activate_attribute)


# Move commands under 'oci apm-traces attributes bulk-de-activation-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_de_activation_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_de_activate_attribute)


# Move commands under 'oci apm-traces attributes bulk-pin-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_pin_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_pin_attribute)


# Move commands under 'oci apm-traces attributes bulk-unpin-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_unpin_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_unpin_attribute)


# Move commands under 'oci apm-traces attributes bulk-update-notes-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_update_notes_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_update_attribute_notes)

# Move commands under 'oci apm-traces attributes bulk-update-attribute-status' -> 'oci apm-traces attributes'
attributes_cli.attributes_root_group.commands.pop(attributes_cli.bulk_update_attribute_status_group.name)
attributes_cli.attributes_root_group.add_command(attributes_cli.bulk_update_attribute)


@cli_util.copy_params_from_generated_command(attributes_cli.put_toggle_auto_activate, params_to_exclude=['apm_domain_id', 'data_key_type', 'is_auto_activate_on'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.put_toggle_auto_activate.name, help=attributes_cli.put_toggle_auto_activate.help)
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM Domain ID for the intended request. [required]""")
@cli_util.option('--data-key-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PRIVATE_DATA_KEY", "PUBLIC_DATA_KEY"]), help=u"""Data key type for which auto-activate needs to be turned on or off. [required]""")
@cli_util.option('--auto-activate-value', required=True, type=click.BOOL, help=u"""Auto activate toggle switch.  Set to true to turn on auto-activate.  Set to false to turn off auto-activate. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_traces', 'class': 'AutoActivateToggleStatus'})
@cli_util.wrap_exceptions
def put_toggle_auto_activate_extended(ctx, **kwargs):

    if 'auto_activate_value' in kwargs:
        kwargs['is_auto_activate_on'] = kwargs['auto_activate_value']
        kwargs.pop('auto_activate_value')

    ctx.invoke(attributes_cli.put_toggle_auto_activate, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_activate_attribute, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_activate_attribute.name, help=attributes_cli.bulk_activate_attribute.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute to be activated.

This option is a JSON list with items of type BulkActivateAttributeDetail.  For documentation on BulkActivateAttributeDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkActivateAttributeDetail.
[
    {
      "attributeName": "<Name of the attribute to be activated>",
      "attributeType": "<Data type of attribute, NUMERIC or STRING>",
      "attributeNamespace": "<TRACES|SYNTHETIC>",
      "unit":"<NONE | EPOCH_TIME_MS | BYTES | COUNT | DURATION_MS | TRACE_STATUS | PERCENTAGE>"
    }
]
""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkActivateAttributeDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkActivationStatus'})
@cli_util.wrap_exceptions
def bulk_activate_attribute_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_activate_attribute, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_de_activate_attribute, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_de_activate_attribute.name, help=attributes_cli.bulk_de_activate_attribute.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute to be de-activated.

This option is a JSON list with items of type BulkDeActivateAttributeDetail.  For documentation on BulkDeActivateAttributeDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkDeActivateAttributeDetail.
[
    {
      "attributeName": "<Name of the attribute to be de-activated>",
      "attributeNamespace": "<TRACES|SYNTHETIC>"
    }
]
""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkDeActivateAttributeDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkDeActivationStatus'})
@cli_util.wrap_exceptions
def bulk_de_activate_attribute_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_de_activate_attribute, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_pin_attribute, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_pin_attribute.name, help=attributes_cli.bulk_pin_attribute.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute to be pinned.

This option is a JSON list with items of type BulkPinAttributeDetail.  For documentation on BulkPinAttributeDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkPinAttributeDetail.
[
    {
      "attributeName": "<Name of the attribute to be pinned>",
      "attributeNamespace": "<TRACES|SYNTHETIC>"
    }
]
.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkPinAttributeDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkPinStatus'})
@cli_util.wrap_exceptions
def bulk_pin_attribute_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_pin_attribute, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_unpin_attribute, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_unpin_attribute.name, help=attributes_cli.bulk_unpin_attribute.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute to be un-pinned.

This option is a JSON list with items of type BulkUnpinAttributeDetail.  For documentation on BulkUnpinAttributeDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkUnpinAttributeDetail.
[
    {
      "attributeName": "<Name of the attribute to be un-pinned>",
      "attributeNamespace": "<TRACES|SYNTHETIC>"
    }
]
.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkUnpinAttributeDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkUnpinStatus'})
@cli_util.wrap_exceptions
def bulk_unpin_attribute_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_unpin_attribute, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_update_attribute_notes, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_update_attribute_notes.name, help=attributes_cli.bulk_update_attribute_notes.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute for which notes are to be updated.

This option is a JSON list with items of type BulkUpdateAttributeNotesDetail.  For documentation on BulkUpdateAttributeNotesDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkUpdateAttributeNotesDetail.
[
    {
      "attributeName": "<Name of the attribute for which notes are to be updated>",
      "notes" : "<Sample notes>",
      "attributeNamespace": "<TRACES|SYNTHETIC>"
    }
]
.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkUpdateAttributeNotesDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkUpdateNotesStatus'})
@cli_util.wrap_exceptions
def bulk_update_attribute_notes_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_update_attribute_notes, **kwargs)


@cli_util.copy_params_from_generated_command(attributes_cli.bulk_update_attribute, params_to_exclude=['attribute_details'])
@attributes_cli.attributes_root_group.command(name=attributes_cli.bulk_update_attribute.name, help=attributes_cli.bulk_update_attribute.help)
@cli_util.option('--attribute-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of objects containing the details about individual attribute for which unit is to be updated.

This option is a JSON list with items of type BulkUpdateAttributeDetail.  For documentation on BulkUpdateAttributeDetail please see our API reference: https://docs.cloud.oracle.com/api/#/en/attributes/20200630/datatypes/BulkUpdateAttributeDetail.
[
    {
      "attributeName": "<Name of the attribute for which unit is to be updated>",
      "unit":"<NONE | EPOCH_TIME_MS | BYTES | COUNT | DURATION_MS | TRACE_STATUS | PERCENTAGE>",
      "attributeNamespace": "<TRACES|SYNTHETIC>"
    }
]
.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'attribute-details': {'module': 'apm_traces', 'class': 'list[BulkUpdateAttributeDetail]'}}, output_type={'module': 'apm_traces', 'class': 'BulkUpdateAttributeStatus'})
@cli_util.wrap_exceptions
def bulk_update_attribute_extended(ctx, **kwargs):
    ctx.invoke(attributes_cli.bulk_update_attribute, **kwargs)
