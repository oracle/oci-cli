# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.dts.src.oci_cli_dts.generated import dts_service_cli


@click.command(cli_util.override('appliance_export_job.appliance_export_job_root_group.command_name', 'appliance-export-job'), cls=CommandGroupWithAlias, help=cli_util.override('appliance_export_job.appliance_export_job_root_group.help', """Data Transfer Service API Specification"""), short_help=cli_util.override('appliance_export_job.appliance_export_job_root_group.short_help', """Data Transfer Service API"""))
@cli_util.help_option_group
def appliance_export_job_root_group():
    pass


@click.command(cli_util.override('appliance_export_job.appliance_export_job_group.command_name', 'appliance-export-job'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def appliance_export_job_group():
    pass


dts_service_cli.dts_service_group.add_command(appliance_export_job_root_group)
appliance_export_job_root_group.add_command(appliance_export_job_group)


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.change_appliance_export_job_compartment.command_name', 'change-compartment'), help=u"""Moves a ApplianceExportJob into a different compartment. \n[Command Reference](changeApplianceExportJobCompartment)""")
@cli_util.option('--appliance-export-job-id', required=True, help=u"""ID of the Appliance Export Job""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID]  of the compartment into which the resources should be moved.""")
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_appliance_export_job_compartment(ctx, from_json, appliance_export_job_id, compartment_id, if_match):

    if isinstance(appliance_export_job_id, six.string_types) and len(appliance_export_job_id.strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.change_appliance_export_job_compartment(
        appliance_export_job_id=appliance_export_job_id,
        change_appliance_export_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.create_appliance_export_job.command_name', 'create'), help=u"""Creates a new Appliance Export Job that corresponds with customer's logical dataset \n[Command Reference](createApplianceExportJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""""")
@cli_util.option('--bucket-name', required=True, help=u"""""")
@cli_util.option('--display-name', required=True, help=u"""""")
@cli_util.option('--customer-shipping-address', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--prefix', help=u"""List of objects with names matching this prefix would be part of this export job.""")
@cli_util.option('--range-start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--range-end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}, 'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}, 'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def create_appliance_export_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, bucket_name, display_name, customer_shipping_address, prefix, range_start, range_end, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['bucketName'] = bucket_name
    _details['displayName'] = display_name
    _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if prefix is not None:
        _details['prefix'] = prefix

    if range_start is not None:
        _details['rangeStart'] = range_start

    if range_end is not None:
        _details['rangeEnd'] = range_end

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.create_appliance_export_job(
        create_appliance_export_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_appliance_export_job') and callable(getattr(client, 'get_appliance_export_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_appliance_export_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.delete_appliance_export_job.command_name', 'delete'), help=u"""deletes a Appliance Export Job \n[Command Reference](deleteApplianceExportJob)""")
@cli_util.option('--appliance-export-job-id', required=True, help=u"""ID of the Appliance Export Job""")
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_appliance_export_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, appliance_export_job_id, if_match):

    if isinstance(appliance_export_job_id, six.string_types) and len(appliance_export_job_id.strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.delete_appliance_export_job(
        appliance_export_job_id=appliance_export_job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_appliance_export_job') and callable(getattr(client, 'get_appliance_export_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_appliance_export_job(appliance_export_job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.get_appliance_export_job.command_name', 'get'), help=u"""Describes a Appliance Export Job in detail \n[Command Reference](getApplianceExportJob)""")
@cli_util.option('--appliance-export-job-id', required=True, help=u"""OCID of the Appliance Export Job""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def get_appliance_export_job(ctx, from_json, appliance_export_job_id):

    if isinstance(appliance_export_job_id, six.string_types) and len(appliance_export_job_id.strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.get_appliance_export_job(
        appliance_export_job_id=appliance_export_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.list_appliance_export_jobs.command_name', 'list'), help=u"""Lists Appliance Export Jobs in a given compartment \n[Command Reference](listApplianceExportJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""compartment id""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]), help=u"""filtering by lifecycleState""")
@cli_util.option('--display-name', help=u"""filtering by displayName""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dts', 'class': 'list[ApplianceExportJobSummary]'})
@cli_util.wrap_exceptions
def list_appliance_export_jobs(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_appliance_export_jobs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_appliance_export_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_appliance_export_jobs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@appliance_export_job_group.command(name=cli_util.override('appliance_export_job.update_appliance_export_job.command_name', 'update'), help=u"""Updates a Appliance Export Job that corresponds with customer's logical dataset. \n[Command Reference](updateApplianceExportJob)""")
@cli_util.option('--appliance-export-job-id', required=True, help=u"""ID of the Appliance Export Job""")
@cli_util.option('--bucket-name', help=u"""""")
@cli_util.option('--prefix', help=u"""List of objects with names matching this prefix would be part of this export job.""")
@cli_util.option('--range-start', help=u"""Object names returned by a list query must be greater or equal to this parameter.""")
@cli_util.option('--range-end', help=u"""Object names returned by a list query must be strictly less than this parameter.""")
@cli_util.option('--display-name', help=u"""""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]), help=u"""""")
@cli_util.option('--lifecycle-state-details', help=u"""A property that can contain details on the lifecycle.""")
@cli_util.option('--manifest-file', help=u"""Manifest File associated with this export job.""")
@cli_util.option('--manifest-md5', help=u"""md5 digest of the manifest file.""")
@cli_util.option('--number-of-objects', help=u"""Total number of objects that are exported in this job.""")
@cli_util.option('--total-size-in-bytes', help=u"""Total size of objects in Bytes that are exported in this job.""")
@cli_util.option('--first-object', help=u"""First object in the list of objects that are exported in this job.""")
@cli_util.option('--last-object', help=u"""Last object in the list of objects that are exported in this job.""")
@cli_util.option('--next-object', help=u"""First object from which the next potential export job could start.""")
@cli_util.option('--customer-shipping-address', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The entity tag to match. Optional, if set, the update will be successful only if the object's tag matches the tag specified in the request.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INPROGRESS", "SUCCEEDED", "FAILED", "CANCELLED", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}, 'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'customer-shipping-address': {'module': 'dts', 'class': 'ShippingAddress'}, 'freeform-tags': {'module': 'dts', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dts', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dts', 'class': 'ApplianceExportJob'})
@cli_util.wrap_exceptions
def update_appliance_export_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, appliance_export_job_id, bucket_name, prefix, range_start, range_end, display_name, lifecycle_state, lifecycle_state_details, manifest_file, manifest_md5, number_of_objects, total_size_in_bytes, first_object, last_object, next_object, customer_shipping_address, freeform_tags, defined_tags, if_match):

    if isinstance(appliance_export_job_id, six.string_types) and len(appliance_export_job_id.strip()) == 0:
        raise click.UsageError('Parameter --appliance-export-job-id cannot be whitespace or empty string')
    if not force:
        if customer_shipping_address or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to customer-shipping-address and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if bucket_name is not None:
        _details['bucketName'] = bucket_name

    if prefix is not None:
        _details['prefix'] = prefix

    if range_start is not None:
        _details['rangeStart'] = range_start

    if range_end is not None:
        _details['rangeEnd'] = range_end

    if display_name is not None:
        _details['displayName'] = display_name

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if lifecycle_state_details is not None:
        _details['lifecycleStateDetails'] = lifecycle_state_details

    if manifest_file is not None:
        _details['manifestFile'] = manifest_file

    if manifest_md5 is not None:
        _details['manifestMd5'] = manifest_md5

    if number_of_objects is not None:
        _details['numberOfObjects'] = number_of_objects

    if total_size_in_bytes is not None:
        _details['totalSizeInBytes'] = total_size_in_bytes

    if first_object is not None:
        _details['firstObject'] = first_object

    if last_object is not None:
        _details['lastObject'] = last_object

    if next_object is not None:
        _details['nextObject'] = next_object

    if customer_shipping_address is not None:
        _details['customerShippingAddress'] = cli_util.parse_json_parameter("customer_shipping_address", customer_shipping_address)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dts', 'appliance_export_job', ctx)
    result = client.update_appliance_export_job(
        appliance_export_job_id=appliance_export_job_id,
        update_appliance_export_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_appliance_export_job') and callable(getattr(client, 'get_appliance_export_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_appliance_export_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
