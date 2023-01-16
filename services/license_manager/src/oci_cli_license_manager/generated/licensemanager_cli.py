# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('license_manager.license_manager_root_group.command_name', 'license-manager'), cls=CommandGroupWithAlias, help=cli_util.override('license_manager.license_manager_root_group.help', """Use the License Manager API to manage product licenses and license records. For more information, see [License Manager Overview]."""), short_help=cli_util.override('license_manager.license_manager_root_group.short_help', """License Manager API"""))
@cli_util.help_option_group
def license_manager_root_group():
    pass


@click.command(cli_util.override('license_manager.product_license_collection_group.command_name', 'product-license-collection'), cls=CommandGroupWithAlias, help="""The product license summary collection.""")
@cli_util.help_option_group
def product_license_collection_group():
    pass


@click.command(cli_util.override('license_manager.product_license_group.command_name', 'product-license'), cls=CommandGroupWithAlias, help="""The product license details.""")
@cli_util.help_option_group
def product_license_group():
    pass


@click.command(cli_util.override('license_manager.top_utilized_resource_collection_group.command_name', 'top-utilized-resource-collection'), cls=CommandGroupWithAlias, help="""The collection of top utilized resources.""")
@cli_util.help_option_group
def top_utilized_resource_collection_group():
    pass


@click.command(cli_util.override('license_manager.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""Details of the compartment-specific configuration.""")
@cli_util.help_option_group
def configuration_group():
    pass


@click.command(cli_util.override('license_manager.bulk_upload_license_records_details_group.command_name', 'bulk-upload-license-records-details'), cls=CommandGroupWithAlias, help="""Details required for bulk uploading of license records.""")
@cli_util.help_option_group
def bulk_upload_license_records_details_group():
    pass


@click.command(cli_util.override('license_manager.license_record_collection_group.command_name', 'license-record-collection'), cls=CommandGroupWithAlias, help="""The license record summary collection.""")
@cli_util.help_option_group
def license_record_collection_group():
    pass


@click.command(cli_util.override('license_manager.license_record_group.command_name', 'license-record'), cls=CommandGroupWithAlias, help="""License record summary.""")
@cli_util.help_option_group
def license_record_group():
    pass


@click.command(cli_util.override('license_manager.license_metric_group.command_name', 'license-metric'), cls=CommandGroupWithAlias, help="""Overview of product license and resources usage.""")
@cli_util.help_option_group
def license_metric_group():
    pass


@click.command(cli_util.override('license_manager.product_license_consumer_collection_group.command_name', 'product-license-consumer-collection'), cls=CommandGroupWithAlias, help="""Collection of resources which have consumed licenses.""")
@cli_util.help_option_group
def product_license_consumer_collection_group():
    pass


@click.command(cli_util.override('license_manager.top_utilized_product_license_collection_group.command_name', 'top-utilized-product-license-collection'), cls=CommandGroupWithAlias, help="""A collection of top utilized product licenses.""")
@cli_util.help_option_group
def top_utilized_product_license_collection_group():
    pass


@click.command(cli_util.override('license_manager.bulk_upload_template_group.command_name', 'bulk-upload-template'), cls=CommandGroupWithAlias, help="""The bulk upload template file.""")
@cli_util.help_option_group
def bulk_upload_template_group():
    pass


license_manager_root_group.add_command(product_license_collection_group)
license_manager_root_group.add_command(product_license_group)
license_manager_root_group.add_command(top_utilized_resource_collection_group)
license_manager_root_group.add_command(configuration_group)
license_manager_root_group.add_command(bulk_upload_license_records_details_group)
license_manager_root_group.add_command(license_record_collection_group)
license_manager_root_group.add_command(license_record_group)
license_manager_root_group.add_command(license_metric_group)
license_manager_root_group.add_command(product_license_consumer_collection_group)
license_manager_root_group.add_command(top_utilized_product_license_collection_group)
license_manager_root_group.add_command(bulk_upload_template_group)


@bulk_upload_license_records_details_group.command(name=cli_util.override('license_manager.bulk_upload_license_records.command_name', 'bulk-upload-license-records'), help=u"""Bulk upload the product licenses and license records for a given compartment. \n[Command Reference](bulkUploadLicenseRecords)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] where license records are created.""")
@cli_util.option('--file-name', required=True, help=u"""Name of the file that is being uploaded.""")
@cli_util.option('--file-content', required=True, help=u"""The file to be uploaded.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'BulkUploadResponse'})
@cli_util.wrap_exceptions
def bulk_upload_license_records(ctx, from_json, compartment_id, file_name, file_content):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['fileName'] = file_name
    _details['fileContent'] = file_content

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.bulk_upload_license_records(
        bulk_upload_license_records_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@license_record_group.command(name=cli_util.override('license_manager.create_license_record.command_name', 'create'), help=u"""Creates a new license record for the given product license ID. \n[Command Reference](createLicenseRecord)""")
@cli_util.option('--display-name', required=True, help=u"""License record name.""")
@cli_util.option('--is-perpetual', required=True, type=click.BOOL, help=u"""Specifies if the license record term is perpertual.""")
@cli_util.option('--is-unlimited', required=True, type=click.BOOL, help=u"""Specifies if the license count is unlimited.""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@cli_util.option('--expiration-date', type=custom_types.CLI_DATETIME, help=u"""The license record end date in [RFC 3339] date format. Example: `2018-09-12`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--support-end-date', type=custom_types.CLI_DATETIME, help=u"""The license record support end date in [RFC 3339] date format. Example: `2018-09-12`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--license-count', type=click.INT, help=u"""The number of license units added by a user in a license record. Default 1""")
@cli_util.option('--product-id', help=u"""The license record product ID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'license_manager', 'class': 'LicenseRecord'})
@cli_util.wrap_exceptions
def create_license_record(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, is_perpetual, is_unlimited, product_license_id, expiration_date, support_end_date, license_count, product_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['isPerpetual'] = is_perpetual
    _details['isUnlimited'] = is_unlimited

    if expiration_date is not None:
        _details['expirationDate'] = expiration_date

    if support_end_date is not None:
        _details['supportEndDate'] = support_end_date

    if license_count is not None:
        _details['licenseCount'] = license_count

    if product_id is not None:
        _details['productId'] = product_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.create_license_record(
        product_license_id=product_license_id,
        create_license_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_license_record') and callable(getattr(client, 'get_license_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_license_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@product_license_group.command(name=cli_util.override('license_manager.create_product_license.command_name', 'create'), help=u"""Creates a new product license. \n[Command Reference](createProductLicense)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] where product licenses are created.""")
@cli_util.option('--is-vendor-oracle', required=True, type=click.BOOL, help=u"""Specifies if the product license vendor is Oracle or a third party.""")
@cli_util.option('--display-name', required=True, help=u"""Name of the product license.""")
@cli_util.option('--license-unit', required=True, type=custom_types.CliCaseInsensitiveChoice(["OCPU", "NAMED_USER_PLUS", "PROCESSORS"]), help=u"""The product license unit.""")
@cli_util.option('--vendor-name', help=u"""The product license vendor name, for example: Microsoft, RHEL, and so on.""")
@cli_util.option('--images', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The image details associated with the product license.

This option is a JSON list with items of type ImageDetails.  For documentation on ImageDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/licensemanager/20220430/datatypes/ImageDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'images': {'module': 'license_manager', 'class': 'list[ImageDetails]'}, 'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'images': {'module': 'license_manager', 'class': 'list[ImageDetails]'}, 'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'license_manager', 'class': 'ProductLicense'})
@cli_util.wrap_exceptions
def create_product_license(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, is_vendor_oracle, display_name, license_unit, vendor_name, images, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['isVendorOracle'] = is_vendor_oracle
    _details['displayName'] = display_name
    _details['licenseUnit'] = license_unit

    if vendor_name is not None:
        _details['vendorName'] = vendor_name

    if images is not None:
        _details['images'] = cli_util.parse_json_parameter("images", images)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.create_product_license(
        create_product_license_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_product_license') and callable(getattr(client, 'get_product_license')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_product_license(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@license_record_group.command(name=cli_util.override('license_manager.delete_license_record.command_name', 'delete'), help=u"""Removes a license record. \n[Command Reference](deleteLicenseRecord)""")
@cli_util.option('--license-record-id', required=True, help=u"""Unique license record identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_license_record(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, license_record_id, if_match):

    if isinstance(license_record_id, six.string_types) and len(license_record_id.strip()) == 0:
        raise click.UsageError('Parameter --license-record-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.delete_license_record(
        license_record_id=license_record_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_license_record') and callable(getattr(client, 'get_license_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_license_record(license_record_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@product_license_group.command(name=cli_util.override('license_manager.delete_product_license.command_name', 'delete'), help=u"""Removes a product license. \n[Command Reference](deleteProductLicense)""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_product_license(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, product_license_id, if_match):

    if isinstance(product_license_id, six.string_types) and len(product_license_id.strip()) == 0:
        raise click.UsageError('Parameter --product-license-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.delete_product_license(
        product_license_id=product_license_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_product_license') and callable(getattr(client, 'get_product_license')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_product_license(product_license_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@bulk_upload_template_group.command(name=cli_util.override('license_manager.get_bulk_upload_template.command_name', 'get'), help=u"""Provides the bulk upload file template. \n[Command Reference](getBulkUploadTemplate)""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'BulkUploadTemplate'})
@cli_util.wrap_exceptions
def get_bulk_upload_template(ctx, from_json, ):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.get_bulk_upload_template(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('license_manager.get_configuration.command_name', 'get'), help=u"""Retrieves configuration for a compartment. \n[Command Reference](getConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def get_configuration(ctx, from_json, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.get_configuration(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@license_metric_group.command(name=cli_util.override('license_manager.get_license_metric.command_name', 'get'), help=u"""Retrieves the license metrics for a given compartment. \n[Command Reference](getLicenseMetric)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Indicates if the given compartment is the root compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'LicenseMetric'})
@cli_util.wrap_exceptions
def get_license_metric(ctx, from_json, compartment_id, is_compartment_id_in_subtree):

    kwargs = {}
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.get_license_metric(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@license_record_group.command(name=cli_util.override('license_manager.get_license_record.command_name', 'get'), help=u"""Retrieves license record details by the license record ID in a given compartment. \n[Command Reference](getLicenseRecord)""")
@cli_util.option('--license-record-id', required=True, help=u"""Unique license record identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'LicenseRecord'})
@cli_util.wrap_exceptions
def get_license_record(ctx, from_json, license_record_id):

    if isinstance(license_record_id, six.string_types) and len(license_record_id.strip()) == 0:
        raise click.UsageError('Parameter --license-record-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.get_license_record(
        license_record_id=license_record_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@product_license_group.command(name=cli_util.override('license_manager.get_product_license.command_name', 'get'), help=u"""Retrieves product license details by product license ID in a given compartment. \n[Command Reference](getProductLicense)""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'ProductLicense'})
@cli_util.wrap_exceptions
def get_product_license(ctx, from_json, product_license_id):

    if isinstance(product_license_id, six.string_types) and len(product_license_id.strip()) == 0:
        raise click.UsageError('Parameter --product-license-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.get_product_license(
        product_license_id=product_license_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@license_record_collection_group.command(name=cli_util.override('license_manager.list_license_records.command_name', 'list-license-records'), help=u"""Retrieves all license records for a given product license ID. \n[Command Reference](listLicenseRecords)""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether `ASC` or `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["expirationDate"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `expirationDate`

* **expirationDate:** Sorts by expiration date of the license record.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'LicenseRecordCollection'})
@cli_util.wrap_exceptions
def list_license_records(ctx, from_json, all_pages, page_size, product_license_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_license_records,
            product_license_id=product_license_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_license_records,
            limit,
            page_size,
            product_license_id=product_license_id,
            **kwargs
        )
    else:
        result = client.list_license_records(
            product_license_id=product_license_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@product_license_consumer_collection_group.command(name=cli_util.override('license_manager.list_product_license_consumers.command_name', 'list-product-license-consumers'), help=u"""Retrieves the product license consumers for a particular product license ID. \n[Command Reference](listProductLicenseConsumers)""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Indicates if the given compartment is the root compartment.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether `ASC` or `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["licenseUnitsRequired"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `licenseUnitsRequired`

* **licenseUnitsRequired:** Sorts by licenseUnitsRequired of the Resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'ProductLicenseConsumerCollection'})
@cli_util.wrap_exceptions
def list_product_license_consumers(ctx, from_json, all_pages, page_size, product_license_id, compartment_id, limit, page, is_compartment_id_in_subtree, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_product_license_consumers,
            product_license_id=product_license_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_product_license_consumers,
            limit,
            page_size,
            product_license_id=product_license_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_product_license_consumers(
            product_license_id=product_license_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@product_license_collection_group.command(name=cli_util.override('license_manager.list_product_licenses.command_name', 'list-product-licenses'), help=u"""Retrieves all the product licenses from a given compartment. \n[Command Reference](listProductLicenses)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Indicates if the given compartment is the root compartment.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether `ASC` or `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["totalLicenseUnitsConsumed"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `totalLicenseUnitsConsumed`

* **totalLicenseUnitsConsumed:** Sorts by totalLicenseUnitsConsumed of ProductLicense.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'ProductLicenseCollection'})
@cli_util.wrap_exceptions
def list_product_licenses(ctx, from_json, all_pages, page_size, compartment_id, limit, page, is_compartment_id_in_subtree, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_product_licenses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_product_licenses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_product_licenses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@top_utilized_product_license_collection_group.command(name=cli_util.override('license_manager.list_top_utilized_product_licenses.command_name', 'list-top-utilized-product-licenses'), help=u"""Retrieves the top utilized product licenses for a given compartment. \n[Command Reference](listTopUtilizedProductLicenses)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Indicates if the given compartment is the root compartment.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether `ASC` or `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["totalLicenseUnitsConsumed"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `totalLicenseUnitsConsumed`

* **totalLicenseUnitsConsumed:** Sorts by totalLicenseUnitsConsumed of ProductLicense.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'TopUtilizedProductLicenseCollection'})
@cli_util.wrap_exceptions
def list_top_utilized_product_licenses(ctx, from_json, all_pages, page_size, compartment_id, limit, page, is_compartment_id_in_subtree, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_top_utilized_product_licenses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_top_utilized_product_licenses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_top_utilized_product_licenses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@top_utilized_resource_collection_group.command(name=cli_util.override('license_manager.list_top_utilized_resources.command_name', 'list-top-utilized-resources'), help=u"""Retrieves the top utilized resources for a given compartment. \n[Command Reference](listTopUtilizedResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--is-compartment-id-in-subtree', type=click.BOOL, help=u"""Indicates if the given compartment is the root compartment.""")
@cli_util.option('--resource-unit-type', type=custom_types.CliCaseInsensitiveChoice(["OCPU"]), help=u"""A filter to return only resources whose unit matches the given resource unit.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, whether `ASC` or `DESC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["totalUnits"]), help=u"""Specifies the attribute with which to sort the rules.

Default: `totalUnits`

* **totalUnits:** Sorts by totalUnits consumed by resource.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'license_manager', 'class': 'TopUtilizedResourceCollection'})
@cli_util.wrap_exceptions
def list_top_utilized_resources(ctx, from_json, all_pages, page_size, compartment_id, limit, page, is_compartment_id_in_subtree, resource_unit_type, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if is_compartment_id_in_subtree is not None:
        kwargs['is_compartment_id_in_subtree'] = is_compartment_id_in_subtree
    if resource_unit_type is not None:
        kwargs['resource_unit_type'] = resource_unit_type
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_top_utilized_resources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_top_utilized_resources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_top_utilized_resources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('license_manager.update_configuration.command_name', 'update'), help=u"""Updates the configuration for the compartment. \n[Command Reference](updateConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID] used for the license record, product license, and configuration.""")
@cli_util.option('--email-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of email IDs associated with the configuration.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'email-ids': {'module': 'license_manager', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'email-ids': {'module': 'license_manager', 'class': 'list[string]'}}, output_type={'module': 'license_manager', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def update_configuration(ctx, from_json, force, compartment_id, email_ids, if_match):
    if not force:
        if email_ids:
            if not click.confirm("WARNING: Updates to email-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['emailIds'] = cli_util.parse_json_parameter("email_ids", email_ids)

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.update_configuration(
        compartment_id=compartment_id,
        update_configuration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@license_record_group.command(name=cli_util.override('license_manager.update_license_record.command_name', 'update'), help=u"""Updates license record entity details. \n[Command Reference](updateLicenseRecord)""")
@cli_util.option('--license-record-id', required=True, help=u"""Unique license record identifier.""")
@cli_util.option('--display-name', required=True, help=u"""License record name.""")
@cli_util.option('--is-perpetual', required=True, type=click.BOOL, help=u"""Specifies if the license record term is perpertual.""")
@cli_util.option('--is-unlimited', required=True, type=click.BOOL, help=u"""Specifies if the license count is unlimited.""")
@cli_util.option('--expiration-date', type=custom_types.CLI_DATETIME, help=u"""The license record end date in [RFC 3339] date format. Example: `2018-09-12`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--support-end-date', type=custom_types.CLI_DATETIME, help=u"""The license record support end date in [RFC 3339] date format. Example: `2018-09-12`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--license-count', type=click.INT, help=u"""The number of license units added by a user in a license record. Default 1""")
@cli_util.option('--product-id', help=u"""The license record product ID.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'license_manager', 'class': 'LicenseRecord'})
@cli_util.wrap_exceptions
def update_license_record(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, license_record_id, display_name, is_perpetual, is_unlimited, expiration_date, support_end_date, license_count, product_id, freeform_tags, defined_tags, if_match):

    if isinstance(license_record_id, six.string_types) and len(license_record_id.strip()) == 0:
        raise click.UsageError('Parameter --license-record-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['isPerpetual'] = is_perpetual
    _details['isUnlimited'] = is_unlimited

    if expiration_date is not None:
        _details['expirationDate'] = expiration_date

    if support_end_date is not None:
        _details['supportEndDate'] = support_end_date

    if license_count is not None:
        _details['licenseCount'] = license_count

    if product_id is not None:
        _details['productId'] = product_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.update_license_record(
        license_record_id=license_record_id,
        update_license_record_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_license_record') and callable(getattr(client, 'get_license_record')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_license_record(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@product_license_group.command(name=cli_util.override('license_manager.update_product_license.command_name', 'update'), help=u"""Updates the list of images for a product license. \n[Command Reference](updateProductLicense)""")
@cli_util.option('--product-license-id', required=True, help=u"""Unique product license identifier.""")
@cli_util.option('--images', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The image details associated with the product license.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'images': {'module': 'license_manager', 'class': 'list[ImageDetails]'}, 'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'images': {'module': 'license_manager', 'class': 'list[ImageDetails]'}, 'freeform-tags': {'module': 'license_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'license_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'license_manager', 'class': 'ProductLicense'})
@cli_util.wrap_exceptions
def update_product_license(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, product_license_id, images, freeform_tags, defined_tags, if_match):

    if isinstance(product_license_id, six.string_types) and len(product_license_id.strip()) == 0:
        raise click.UsageError('Parameter --product-license-id cannot be whitespace or empty string')
    if not force:
        if images or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to images and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['images'] = cli_util.parse_json_parameter("images", images)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('license_manager', 'license_manager', ctx)
    result = client.update_product_license(
        product_license_id=product_license_id,
        update_product_license_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_product_license') and callable(getattr(client, 'get_product_license')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_product_license(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
