# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('service_catalog.service_catalog_root_group.command_name', 'service-catalog'), cls=CommandGroupWithAlias, help=cli_util.override('service_catalog.service_catalog_root_group.help', """Manage solutions in Oracle Cloud Infrastructure Service Catalog."""), short_help=cli_util.override('service_catalog.service_catalog_root_group.short_help', """Service Catalog API"""))
@cli_util.help_option_group
def service_catalog_root_group():
    pass


@click.command(cli_util.override('service_catalog.service_catalog_group.command_name', 'service-catalog'), cls=CommandGroupWithAlias, help="""The model for an Oracle Cloud Infrastructure Service Catalog.""")
@cli_util.help_option_group
def service_catalog_group():
    pass


@click.command(cli_util.override('service_catalog.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('service_catalog.service_catalog_association_group.command_name', 'service-catalog-association'), cls=CommandGroupWithAlias, help="""The detailed model for service catalog association.""")
@cli_util.help_option_group
def service_catalog_association_group():
    pass


@click.command(cli_util.override('service_catalog.private_application_group.command_name', 'private-application'), cls=CommandGroupWithAlias, help="""Full details of an application or a solution, which lives inside the tenancy and may be included into service catalogs.""")
@cli_util.help_option_group
def private_application_group():
    pass


@click.command(cli_util.override('service_catalog.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('service_catalog.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('service_catalog.private_application_package_group.command_name', 'private-application-package'), cls=CommandGroupWithAlias, help="""A base object for all types of private application packages.""")
@cli_util.help_option_group
def private_application_package_group():
    pass


@click.command(cli_util.override('service_catalog.application_summary_group.command_name', 'application-summary'), cls=CommandGroupWithAlias, help="""The model for summary of an application in service catalog.""")
@cli_util.help_option_group
def application_summary_group():
    pass


service_catalog_root_group.add_command(service_catalog_group)
service_catalog_root_group.add_command(work_request_error_group)
service_catalog_root_group.add_command(service_catalog_association_group)
service_catalog_root_group.add_command(private_application_group)
service_catalog_root_group.add_command(work_request_log_entry_group)
service_catalog_root_group.add_command(work_request_group)
service_catalog_root_group.add_command(private_application_package_group)
service_catalog_root_group.add_command(application_summary_group)


@service_catalog_association_group.command(name=cli_util.override('service_catalog.bulk_replace_service_catalog_associations.command_name', 'bulk-replace'), help=u"""Replace all associations of a given service catalog in one bulk transaction. \n[Command Reference](bulkReplaceServiceCatalogAssociations)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of CreateServiceCatalogAssociationDetails for bulk operation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'service_catalog', 'class': 'list[CreateServiceCatalogAssociationDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'service_catalog', 'class': 'list[CreateServiceCatalogAssociationDetails]'}})
@cli_util.wrap_exceptions
def bulk_replace_service_catalog_associations(ctx, from_json, force, service_catalog_id, items, if_match):

    if isinstance(service_catalog_id, six.string_types) and len(service_catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-id cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.bulk_replace_service_catalog_associations(
        service_catalog_id=service_catalog_id,
        bulk_replace_service_catalog_associations_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.change_private_application_compartment.command_name', 'change-compartment'), help=u"""Moves the specified private application from one compartment to another. \n[Command Reference](changePrivateApplicationCompartment)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to move the private application.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_private_application_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_application_id, compartment_id, if_match):

    if isinstance(private_application_id, six.string_types) and len(private_application_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.change_private_application_compartment(
        private_application_id=private_application_id,
        change_private_application_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_catalog_group.command(name=cli_util.override('service_catalog.change_service_catalog_compartment.command_name', 'change-compartment'), help=u"""Moves the specified service catalog from one compartment to another. \n[Command Reference](changeServiceCatalogCompartment)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to move the service catalog.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_service_catalog_compartment(ctx, from_json, service_catalog_id, compartment_id, if_match):

    if isinstance(service_catalog_id, six.string_types) and len(service_catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.change_service_catalog_compartment(
        service_catalog_id=service_catalog_id,
        change_service_catalog_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.create_private_application.command_name', 'create'), help=u"""Creates a private application along with a single package to be hosted. \n[Command Reference](createPrivateApplication)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the private application.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the private application.""")
@cli_util.option('--short-description', required=True, help=u"""A short description of the private application.""")
@cli_util.option('--package-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--long-description', help=u"""A long description of the private application.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo to use as the private application icon. Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'package-details': {'module': 'service_catalog', 'class': 'CreatePrivateApplicationPackage'}, 'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-details': {'module': 'service_catalog', 'class': 'CreatePrivateApplicationPackage'}, 'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}}, output_type={'module': 'service_catalog', 'class': 'PrivateApplication'})
@cli_util.wrap_exceptions
def create_private_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, short_description, package_details, long_description, logo_file_base64_encoded, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['shortDescription'] = short_description
    _details['packageDetails'] = cli_util.parse_json_parameter("package_details", package_details)

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.create_private_application(
        create_private_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.create_private_application_create_private_application_stack_package.command_name', 'create-private-application-create-private-application-stack-package'), help=u"""Creates a private application along with a single package to be hosted. \n[Command Reference](createPrivateApplication)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the private application.""")
@cli_util.option('--display-name', required=True, help=u"""The name of the private application.""")
@cli_util.option('--short-description', required=True, help=u"""A short description of the private application.""")
@cli_util.option('--package-details-version', required=True, help=u"""The package version.""")
@cli_util.option('--long-description', help=u"""A long description of the private application.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo to use as the private application icon. Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--package-details-zip-file-base64-encoded', help=u"""Base-64 payload of the Terraform zip package.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}}, output_type={'module': 'service_catalog', 'class': 'PrivateApplication'})
@cli_util.wrap_exceptions
def create_private_application_create_private_application_stack_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, short_description, package_details_version, long_description, logo_file_base64_encoded, defined_tags, freeform_tags, package_details_zip_file_base64_encoded):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['packageDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['shortDescription'] = short_description
    _details['packageDetails']['version'] = package_details_version

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if package_details_zip_file_base64_encoded is not None:
        _details['packageDetails']['zipFileBase64Encoded'] = package_details_zip_file_base64_encoded

    _details['packageDetails']['packageType'] = 'STACK'

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.create_private_application(
        create_private_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_catalog_group.command(name=cli_util.override('service_catalog.create_service_catalog.command_name', 'create'), help=u"""Creates a brand new service catalog in a given compartment. \n[Command Reference](createServiceCatalog)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment where the service catalog will be created.""")
@cli_util.option('--display-name', required=True, help=u"""The display name of the service catalog.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalog'})
@cli_util.wrap_exceptions
def create_service_catalog(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.create_service_catalog(
        create_service_catalog_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_service_catalog') and callable(getattr(client, 'get_service_catalog')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_catalog(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@service_catalog_association_group.command(name=cli_util.override('service_catalog.create_service_catalog_association.command_name', 'create'), help=u"""Creates an association between service catalog and a resource. \n[Command Reference](createServiceCatalogAssociation)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""Identifier of the service catalog.""")
@cli_util.option('--entity-id', required=True, help=u"""Identifier of the entity being associated with service catalog.""")
@cli_util.option('--entity-type', help=u"""The type of the entity that is associated with the service catalog.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogAssociation'})
@cli_util.wrap_exceptions
def create_service_catalog_association(ctx, from_json, service_catalog_id, entity_id, entity_type):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['serviceCatalogId'] = service_catalog_id
    _details['entityId'] = entity_id

    if entity_type is not None:
        _details['entityType'] = entity_type

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.create_service_catalog_association(
        create_service_catalog_association_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.delete_private_application.command_name', 'delete'), help=u"""Deletes an existing private application. \n[Command Reference](deletePrivateApplication)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_private_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_application_id, if_match):

    if isinstance(private_application_id, six.string_types) and len(private_application_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.delete_private_application(
        private_application_id=private_application_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_catalog_group.command(name=cli_util.override('service_catalog.delete_service_catalog.command_name', 'delete'), help=u"""Deletes the specified service catalog from the compartment. \n[Command Reference](deleteServiceCatalog)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_service_catalog(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, service_catalog_id, if_match):

    if isinstance(service_catalog_id, six.string_types) and len(service_catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.delete_service_catalog(
        service_catalog_id=service_catalog_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_service_catalog') and callable(getattr(client, 'get_service_catalog')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_service_catalog(service_catalog_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@service_catalog_association_group.command(name=cli_util.override('service_catalog.delete_service_catalog_association.command_name', 'delete'), help=u"""Removes an association between service catalog and a resource. \n[Command Reference](deleteServiceCatalogAssociation)""")
@cli_util.option('--service-catalog-association-id', required=True, help=u"""The unique identifier of the service catalog association.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_service_catalog_association(ctx, from_json, service_catalog_association_id, if_match):

    if isinstance(service_catalog_association_id, six.string_types) and len(service_catalog_association_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-association-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.delete_service_catalog_association(
        service_catalog_association_id=service_catalog_association_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.get_private_application.command_name', 'get'), help=u"""Gets the details of the specified private application. \n[Command Reference](getPrivateApplication)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplication'})
@cli_util.wrap_exceptions
def get_private_application(ctx, from_json, private_application_id):

    if isinstance(private_application_id, six.string_types) and len(private_application_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_private_application(
        private_application_id=private_application_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.get_private_application_action_download_logo.command_name', 'get-private-application-action-download-logo'), help=u"""Downloads the binary payload of the logo image of the private application. \n[Command Reference](getPrivateApplicationActionDownloadLogo)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_private_application_action_download_logo(ctx, from_json, file, private_application_id):

    if isinstance(private_application_id, six.string_types) and len(private_application_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_private_application_action_download_logo(
        private_application_id=private_application_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@private_application_package_group.command(name=cli_util.override('service_catalog.get_private_application_package.command_name', 'get'), help=u"""Gets the details of a specific package within a given private application. \n[Command Reference](getPrivateApplicationPackage)""")
@cli_util.option('--private-application-package-id', required=True, help=u"""The unique identifier for the private application package.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplicationPackage'})
@cli_util.wrap_exceptions
def get_private_application_package(ctx, from_json, private_application_package_id):

    if isinstance(private_application_package_id, six.string_types) and len(private_application_package_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-package-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_private_application_package(
        private_application_package_id=private_application_package_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_application_package_group.command(name=cli_util.override('service_catalog.get_private_application_package_action_download_config.command_name', 'get-private-application-package-action-download-config'), help=u"""Downloads the configuration that was used to create the private application package. \n[Command Reference](getPrivateApplicationPackageActionDownloadConfig)""")
@cli_util.option('--private-application-package-id', required=True, help=u"""The unique identifier for the private application package.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_private_application_package_action_download_config(ctx, from_json, file, private_application_package_id):

    if isinstance(private_application_package_id, six.string_types) and len(private_application_package_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-package-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_private_application_package_action_download_config(
        private_application_package_id=private_application_package_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@service_catalog_group.command(name=cli_util.override('service_catalog.get_service_catalog.command_name', 'get'), help=u"""Gets detailed information about the service catalog including name, compartmentId \n[Command Reference](getServiceCatalog)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""The unique identifier for the service catalog.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalog'})
@cli_util.wrap_exceptions
def get_service_catalog(ctx, from_json, service_catalog_id):

    if isinstance(service_catalog_id, six.string_types) and len(service_catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_service_catalog(
        service_catalog_id=service_catalog_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_catalog_association_group.command(name=cli_util.override('service_catalog.get_service_catalog_association.command_name', 'get'), help=u"""Gets detailed information about specific service catalog association. \n[Command Reference](getServiceCatalogAssociation)""")
@cli_util.option('--service-catalog-association-id', required=True, help=u"""The unique identifier of the service catalog association.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogAssociation'})
@cli_util.wrap_exceptions
def get_service_catalog_association(ctx, from_json, service_catalog_association_id):

    if isinstance(service_catalog_association_id, six.string_types) and len(service_catalog_association_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-association-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_service_catalog_association(
        service_catalog_association_id=service_catalog_association_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_catalog.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_summary_group.command(name=cli_util.override('service_catalog.list_applications.command_name', 'list-applications'), help=u"""Lists all the applications in a service catalog or a tenancy. If no parameter is specified, all catalogs from all compartments in the tenancy will be scanned for any type of content. \n[Command Reference](listApplications)""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--service-catalog-id', help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--entity-type', help=u"""The type of the application in the service catalog.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--display-name', help=u"""Exact match name filter.""")
@cli_util.option('--entity-id', help=u"""The unique identifier of the entity associated with service catalog.""")
@cli_util.option('--publisher-id', multiple=True, help=u"""Limit results to just this publisher.""")
@cli_util.option('--package-type', type=custom_types.CliCaseInsensitiveChoice(["STACK"]), multiple=True, help=u"""Name of the package type. If multiple package types are provided, then any resource with one or more matching package types will be returned.""")
@cli_util.option('--pricing', type=custom_types.CliCaseInsensitiveChoice(["FREE", "BYOL", "PAYGO"]), multiple=True, help=u"""Name of the pricing type. If multiple pricing types are provided, then any resource with one or more matching pricing models will be returned.""")
@cli_util.option('--is-featured', type=click.BOOL, help=u"""Indicates whether to show only featured resources. If this is set to `false` or is omitted, then all resources will be returned.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'publisher-id': {'module': 'service_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'publisher-id': {'module': 'service_catalog', 'class': 'list[string]'}}, output_type={'module': 'service_catalog', 'class': 'ApplicationCollection'})
@cli_util.wrap_exceptions
def list_applications(ctx, from_json, all_pages, page_size, compartment_id, service_catalog_id, entity_type, limit, page, display_name, entity_id, publisher_id, package_type, pricing, is_featured, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if service_catalog_id is not None:
        kwargs['service_catalog_id'] = service_catalog_id
    if entity_type is not None:
        kwargs['entity_type'] = entity_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if publisher_id is not None and len(publisher_id) > 0:
        kwargs['publisher_id'] = publisher_id
    if package_type is not None and len(package_type) > 0:
        kwargs['package_type'] = package_type
    if pricing is not None and len(pricing) > 0:
        kwargs['pricing'] = pricing
    if is_featured is not None:
        kwargs['is_featured'] = is_featured
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_applications,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_applications,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_applications(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_application_package_group.command(name=cli_util.override('service_catalog.list_private_application_packages.command_name', 'list'), help=u"""Lists the packages in the specified private application. \n[Command Reference](listPrivateApplicationPackages)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@cli_util.option('--private-application-package-id', help=u"""The unique identifier for the private application package.""")
@cli_util.option('--package-type', type=custom_types.CliCaseInsensitiveChoice(["STACK"]), multiple=True, help=u"""Name of the package type. If multiple package types are provided, then any resource with one or more matching package types will be returned.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "VERSION"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMECREATED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--display-name', help=u"""Exact match name filter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplicationPackageCollection'})
@cli_util.wrap_exceptions
def list_private_application_packages(ctx, from_json, all_pages, page_size, private_application_id, private_application_package_id, package_type, limit, page, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if private_application_package_id is not None:
        kwargs['private_application_package_id'] = private_application_package_id
    if package_type is not None and len(package_type) > 0:
        kwargs['package_type'] = package_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_private_application_packages,
            private_application_id=private_application_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_private_application_packages,
            limit,
            page_size,
            private_application_id=private_application_id,
            **kwargs
        )
    else:
        result = client.list_private_application_packages(
            private_application_id=private_application_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.list_private_applications.command_name', 'list'), help=u"""Lists all the private applications in a given compartment. \n[Command Reference](listPrivateApplications)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--private-application-id', help=u"""The unique identifier for the private application.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "LIFECYCLESTATE"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. Default is `TIMECREATED`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--display-name', help=u"""Exact match name filter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplicationCollection'})
@cli_util.wrap_exceptions
def list_private_applications(ctx, from_json, all_pages, page_size, compartment_id, private_application_id, limit, page, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if private_application_id is not None:
        kwargs['private_application_id'] = private_application_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_private_applications,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_private_applications,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_private_applications(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_catalog_association_group.command(name=cli_util.override('service_catalog.list_service_catalog_associations.command_name', 'list'), help=u"""Lists all the resource associations for a specific service catalog. \n[Command Reference](listServiceCatalogAssociations)""")
@cli_util.option('--service-catalog-association-id', help=u"""The unique identifier for the service catalog association.""")
@cli_util.option('--service-catalog-id', help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--entity-id', help=u"""The unique identifier of the entity associated with service catalog.""")
@cli_util.option('--entity-type', help=u"""The type of the application in the service catalog.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""Default is `TIMECREATED`""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogAssociationCollection'})
@cli_util.wrap_exceptions
def list_service_catalog_associations(ctx, from_json, all_pages, page_size, service_catalog_association_id, service_catalog_id, entity_id, entity_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if service_catalog_association_id is not None:
        kwargs['service_catalog_association_id'] = service_catalog_association_id
    if service_catalog_id is not None:
        kwargs['service_catalog_id'] = service_catalog_id
    if entity_id is not None:
        kwargs['entity_id'] = entity_id
    if entity_type is not None:
        kwargs['entity_type'] = entity_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_catalog_associations,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_catalog_associations,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_service_catalog_associations(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@service_catalog_group.command(name=cli_util.override('service_catalog.list_service_catalogs.command_name', 'list'), help=u"""Lists all the service catalogs in the given compartment. \n[Command Reference](listServiceCatalogs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--service-catalog-id', help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""Default is `TIMECREATED`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--display-name', help=u"""Exact match name filter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogCollection'})
@cli_util.wrap_exceptions
def list_service_catalogs(ctx, from_json, all_pages, page_size, compartment_id, service_catalog_id, limit, page, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if service_catalog_id is not None:
        kwargs['service_catalog_id'] = service_catalog_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_catalogs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_catalogs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_service_catalogs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('service_catalog.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('service_catalog.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('service_catalog.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_application_group.command(name=cli_util.override('service_catalog.update_private_application.command_name', 'update'), help=u"""Updates the details of an existing private application. \n[Command Reference](updatePrivateApplication)""")
@cli_util.option('--private-application-id', required=True, help=u"""The unique identifier for the private application.""")
@cli_util.option('--display-name', help=u"""The name of the private application.""")
@cli_util.option('--short-description', help=u"""A short description of the private application.""")
@cli_util.option('--long-description', help=u"""A long description of the private application.""")
@cli_util.option('--logo-file-base64-encoded', help=u"""Base64-encoded logo to use as the private application icon. Template icon file requirements: PNG format, 50 KB maximum, 130 x 130 pixels.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}}, output_type={'module': 'service_catalog', 'class': 'PrivateApplication'})
@cli_util.wrap_exceptions
def update_private_application(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, private_application_id, display_name, short_description, long_description, logo_file_base64_encoded, defined_tags, freeform_tags, if_match):

    if isinstance(private_application_id, six.string_types) and len(private_application_id.strip()) == 0:
        raise click.UsageError('Parameter --private-application-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if short_description is not None:
        _details['shortDescription'] = short_description

    if long_description is not None:
        _details['longDescription'] = long_description

    if logo_file_base64_encoded is not None:
        _details['logoFileBase64Encoded'] = logo_file_base64_encoded

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.update_private_application(
        private_application_id=private_application_id,
        update_private_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@service_catalog_group.command(name=cli_util.override('service_catalog.update_service_catalog.command_name', 'update'), help=u"""Updates the details of a previously created service catalog. \n[Command Reference](updateServiceCatalog)""")
@cli_util.option('--service-catalog-id', required=True, help=u"""The unique identifier for the service catalog.""")
@cli_util.option('--display-name', required=True, help=u"""A display name of the service catalog.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'service_catalog', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'service_catalog', 'class': 'dict(str, string)'}}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalog'})
@cli_util.wrap_exceptions
def update_service_catalog(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, service_catalog_id, display_name, defined_tags, freeform_tags, if_match):

    if isinstance(service_catalog_id, six.string_types) and len(service_catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --service-catalog-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('service_catalog', 'service_catalog', ctx)
    result = client.update_service_catalog(
        service_catalog_id=service_catalog_id,
        update_service_catalog_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_service_catalog') and callable(getattr(client, 'get_service_catalog')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_service_catalog(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
