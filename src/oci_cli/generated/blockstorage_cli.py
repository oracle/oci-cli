# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import six  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('blockstorage_group.command_name', 'blockstorage'), cls=CommandGroupWithAlias, help=cli_util.override('blockstorage_group.help', """APIs for Networking Service, Compute Service, and Block Volume Service."""))
@cli_util.help_option_group
def blockstorage_group():
    pass


@click.command(cli_util.override('volume_group.command_name', 'volume'), cls=CommandGroupWithAlias, help="""A detachable block volume device that allows you to dynamically expand
the storage capacity of an instance. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_group():
    pass


@click.command(cli_util.override('volume_backup_group.command_name', 'volume-backup'), cls=CommandGroupWithAlias, help="""A point-in-time copy of a volume that can then be used to create a new block volume
or recover a block volume. For more information, see
[Overview of Cloud Volume Storage].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access, see
[Getting Started with Policies].""")
@cli_util.help_option_group
def volume_backup_group():
    pass


@volume_group.command(name=cli_util.override('create_volume.command_name', 'create'), help="""Creates a new volume in the specified compartment. Volumes can be created in sizes ranging from 50 GB (51200 MB) to 16 TB (16777216 MB), in 1 GB (1024 MB) increments. By default, volumes are 1 TB (1048576 MB). For general information about block volumes, see [Overview of Block Volume Service].

A volume and instance can be in separate compartments but must be in the same Availability Domain. For information about access control and compartments, see [Overview of the IAM Service]. For information about Availability Domains, see [Regions and Availability Domains]. To get a list of Availability Domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

You may optionally specify a *display name* for the volume, which is simply a friendly name or description. It does not have to be unique, and you can change it. Avoid entering confidential information.""")
@click.option('--availability-domain', help="""The Availability Domain of the volume.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', help="""The OCID of the compartment that contains the volume. [required]""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--size-in-gbs', type=click.INT, help="""The size of the volume in GBs.""")
@click.option('--size-in-mbs', type=click.INT, help="""The size of the volume in MBs. The value must be a multiple of 1024. This field is deprecated. Use sizeInGBs instead.""")
@click.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help="""Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup. This is an optional field. If not specified or set to null, the new Block volume will be empty. When specified, the new Block volume will contain data from the source volume or backup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--volume-backup-id', help="""The OCID of the volume backup from which the data should be restored on the newly created volume. This field is deprecated. Use the sourceDetails field instead to specify the backup for the volume.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'source-details': {'module': 'core', 'class': 'VolumeSourceDetails'}}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def create_volume(ctx, generate_full_command_json_input, generate_param_json_input, from_json, availability_domain, compartment_id, display_name, size_in_gbs, size_in_mbs, source_details, volume_backup_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    availability_domain = cli_util.coalesce_provided_and_default_value(ctx, 'availability-domain', availability_domain, True)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    size_in_gbs = cli_util.coalesce_provided_and_default_value(ctx, 'size-in-gbs', size_in_gbs, False)
    size_in_mbs = cli_util.coalesce_provided_and_default_value(ctx, 'size-in-mbs', size_in_mbs, False)
    source_details = cli_util.coalesce_provided_and_default_value(ctx, 'source-details', source_details, False)
    volume_backup_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-backup-id', volume_backup_id, False)

    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    if size_in_gbs is not None:
        details['sizeInGBs'] = size_in_gbs

    if size_in_mbs is not None:
        details['sizeInMBs'] = size_in_mbs

    if source_details is not None:
        details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if volume_backup_id is not None:
        details['volumeBackupId'] = volume_backup_id

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume(
        create_volume_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('create_volume_backup.command_name', 'create'), help="""Creates a new backup of the specified volume. For general information about volume backups, see [Overview of Block Volume Service Backups]

When the request is received, the backup object is in a REQUEST_RECEIVED state. When the data is imaged, it goes into a CREATING state. After the backup is fully uploaded to the cloud, it goes into an AVAILABLE state.""")
@click.option('--volume-id', help="""The OCID of the volume that needs to be backed up. [required]""")
@click.option('--display-name', help="""A user-friendly name for the volume backup. Does not have to be unique and it's changeable. Avoid entering confidential information.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def create_volume_backup(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_id, display_name):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-id', volume_id, True)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)

    kwargs = {}

    details = {}
    details['volumeId'] = volume_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.create_volume_backup(
        create_volume_backup_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('delete_volume.command_name', 'delete'), help="""Deletes the specified volume. The volume cannot have an active connection to an instance. To disconnect the volume from a connected instance, see [Disconnecting From a Volume]. **Warning:** All data on the volume will be permanently lost when the volume is deleted.""")
@click.option('--volume-id', help="""The OCID of the volume. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-id', volume_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('delete_volume_backup.command_name', 'delete'), help="""Deletes a volume backup.""")
@click.option('--volume-backup-id', help="""The OCID of the volume backup. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_volume_backup(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_backup_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_backup_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-backup-id', volume_backup_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('blockstorage', ctx)
    result = client.delete_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('get_volume.command_name', 'get'), help="""Gets information for the specified volume.""")
@click.option('--volume-id', help="""The OCID of the volume. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def get_volume(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-id', volume_id, True)

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume(
        volume_id=volume_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('get_volume_backup.command_name', 'get'), help="""Gets information for the specified volume backup.""")
@click.option('--volume-backup-id', help="""The OCID of the volume backup. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def get_volume_backup(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_backup_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_backup_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-backup-id', volume_backup_id, True)

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('blockstorage', ctx)
    result = client.get_volume_backup(
        volume_backup_id=volume_backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('list_volume_backups.command_name', 'list'), help="""Lists the volume backups in the specified compartment. You can filter the results by volume.""")
@click.option('--compartment-id', help="""The OCID of the compartment. [required]""")
@click.option('--volume-id', help="""The OCID of the volume.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[VolumeBackup]'})
@cli_util.wrap_exceptions
def list_volume_backups(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, volume_id, limit, page, display_name, sort_by, sort_order, lifecycle_state):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    volume_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-id', volume_id, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    sort_by = cli_util.coalesce_provided_and_default_value(ctx, 'sort-by', sort_by, False)
    sort_order = cli_util.coalesce_provided_and_default_value(ctx, 'sort-order', sort_order, False)
    lifecycle_state = cli_util.coalesce_provided_and_default_value(ctx, 'lifecycle-state', lifecycle_state, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if volume_id is not None:
        kwargs['volume_id'] = volume_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volume_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_volume_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volume_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('list_volumes.command_name', 'list'), help="""Lists the volumes in the specified compartment and Availability Domain.""")
@click.option('--compartment-id', help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', help="""The name of the Availability Domain.

Example: `Uocm:PHX-AD-1`""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', help="""A filter to return only resources that match the given display name exactly.""")
@click.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@click.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order is case sensitive.""")
@click.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]), help="""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'list[Volume]'})
@cli_util.wrap_exceptions
def list_volumes(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, sort_by, sort_order, lifecycle_state):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    availability_domain = cli_util.coalesce_provided_and_default_value(ctx, 'availability-domain', availability_domain, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    sort_by = cli_util.coalesce_provided_and_default_value(ctx, 'sort-by', sort_by, False)
    sort_order = cli_util.coalesce_provided_and_default_value(ctx, 'sort-order', sort_order, False)
    lifecycle_state = cli_util.coalesce_provided_and_default_value(ctx, 'lifecycle-state', lifecycle_state, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('blockstorage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_volumes,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_volumes,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_volumes(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@volume_group.command(name=cli_util.override('update_volume.command_name', 'update'), help="""Updates the specified volume's display name. Avoid entering confidential information.""")
@click.option('--volume-id', help="""The OCID of the volume. [required]""")
@click.option('--display-name', help="""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'Volume'})
@cli_util.wrap_exceptions
def update_volume(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_id, display_name, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-id', volume_id, True)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(volume_id, six.string_types) and len(volume_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume(
        volume_id=volume_id,
        update_volume_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@volume_backup_group.command(name=cli_util.override('update_volume_backup.command_name', 'update'), help="""Updates the display name for the specified volume backup. Avoid entering confidential information.""")
@click.option('--volume-backup-id', help="""The OCID of the volume backup. [required]""")
@click.option('--display-name', help="""A friendly user-specified name for the volume backup. Avoid entering confidential information.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'core', 'class': 'VolumeBackup'})
@cli_util.wrap_exceptions
def update_volume_backup(ctx, generate_full_command_json_input, generate_param_json_input, from_json, volume_backup_id, display_name, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    volume_backup_id = cli_util.coalesce_provided_and_default_value(ctx, 'volume-backup-id', volume_backup_id, True)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(volume_backup_id, six.string_types) and len(volume_backup_id.strip()) == 0:
        raise click.UsageError('Parameter --volume-backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('blockstorage', ctx)
    result = client.update_volume_backup(
        volume_backup_id=volume_backup_id,
        update_volume_backup_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
