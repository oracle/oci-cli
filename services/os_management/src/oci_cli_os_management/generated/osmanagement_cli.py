# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('os_management.os_management_root_group.command_name', 'os-management'), cls=CommandGroupWithAlias, help=cli_util.override('os_management.os_management_root_group.help', """API for the OS Management service. Use these API operations for working
with Managed instances and Managed instance groups."""), short_help=cli_util.override('os_management.os_management_root_group.short_help', """OS Management API"""))
@cli_util.help_option_group
def os_management_root_group():
    pass


@click.command(cli_util.override('os_management.software_source_group.command_name', 'software-source'), cls=CommandGroupWithAlias, help="""A software source contains a collection of packages""")
@cli_util.help_option_group
def software_source_group():
    pass


@click.command(cli_util.override('os_management.erratum_group.command_name', 'erratum'), cls=CommandGroupWithAlias, help="""Details about the erratum.""")
@cli_util.help_option_group
def erratum_group():
    pass


@click.command(cli_util.override('os_management.managed_instance_group_group.command_name', 'managed-instance-group'), cls=CommandGroupWithAlias, help="""Detail information for a managed instance group""")
@cli_util.help_option_group
def managed_instance_group_group():
    pass


@click.command(cli_util.override('os_management.managed_instance_group.command_name', 'managed-instance'), cls=CommandGroupWithAlias, help="""Detail information for an OCI Compute instance that is being managed""")
@cli_util.help_option_group
def managed_instance_group():
    pass


@click.command(cli_util.override('os_management.scheduled_job_group.command_name', 'scheduled-job'), cls=CommandGroupWithAlias, help="""Detailed information about a Scheduled Job""")
@cli_util.help_option_group
def scheduled_job_group():
    pass


@click.command(cli_util.override('os_management.windows_update_group.command_name', 'windows-update'), cls=CommandGroupWithAlias, help="""An update available for a Windows managed instance.""")
@cli_util.help_option_group
def windows_update_group():
    pass


@click.command(cli_util.override('os_management.work_request_summary_group.command_name', 'work-request-summary'), cls=CommandGroupWithAlias, help="""A work request summary""")
@cli_util.help_option_group
def work_request_summary_group():
    pass


@click.command(cli_util.override('os_management.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('os_management.erratum_summary_group.command_name', 'erratum-summary'), cls=CommandGroupWithAlias, help="""Important changes for software. This can include security | advisories, bug fixes, or enhancements.""")
@cli_util.help_option_group
def erratum_summary_group():
    pass


os_management_root_group.add_command(software_source_group)
os_management_root_group.add_command(erratum_group)
os_management_root_group.add_command(managed_instance_group_group)
os_management_root_group.add_command(managed_instance_group)
os_management_root_group.add_command(scheduled_job_group)
os_management_root_group.add_command(windows_update_group)
os_management_root_group.add_command(work_request_summary_group)
os_management_root_group.add_command(work_request_group)
os_management_root_group.add_command(erratum_summary_group)


@software_source_group.command(name=cli_util.override('os_management.add_packages_to_software_source.command_name', 'add'), help=u"""Adds a given list of Software Packages to a specific Software Source. \n[Command Reference](addPackagesToSoftwareSource)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--package-names', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""the list of package names""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'package-names': {'module': 'os_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-names': {'module': 'os_management', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def add_packages_to_software_source(ctx, from_json, software_source_id, package_names):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['packageNames'] = cli_util.parse_json_parameter("package_names", package_names)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.add_packages_to_software_source(
        software_source_id=software_source_id,
        add_packages_to_software_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.attach_child_software_source_to_managed_instance.command_name', 'attach'), help=u"""Adds a child software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance. \n[Command Reference](attachChildSoftwareSourceToManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-source-id', required=True, help=u"""OCID for the Software Source""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_child_software_source_to_managed_instance(ctx, from_json, managed_instance_id, software_source_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['softwareSourceId'] = software_source_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.attach_child_software_source_to_managed_instance(
        managed_instance_id=managed_instance_id,
        attach_child_software_source_to_managed_instance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.attach_managed_instance_to_managed_instance_group.command_name', 'attach'), help=u"""Adds a Managed Instance to a Managed Instance Group. After the Managed Instance has been added, then operations can be performed on the Managed Instance Group which will then apply to all Managed Instances in the group. \n[Command Reference](attachManagedInstanceToManagedInstanceGroup)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_managed_instance_to_managed_instance_group(ctx, from_json, managed_instance_group_id, managed_instance_id):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.attach_managed_instance_to_managed_instance_group(
        managed_instance_group_id=managed_instance_group_id,
        managed_instance_id=managed_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.attach_parent_software_source_to_managed_instance.command_name', 'attach'), help=u"""Adds a parent software source to a managed instance. After the software source has been added, then packages from that software source can be installed on the managed instance. Software sources that have this software source as a parent will be able to be added to this managed instance. \n[Command Reference](attachParentSoftwareSourceToManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-source-id', required=True, help=u"""OCID for the Software Source""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_parent_software_source_to_managed_instance(ctx, from_json, managed_instance_id, software_source_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['softwareSourceId'] = software_source_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.attach_parent_software_source_to_managed_instance(
        managed_instance_id=managed_instance_id,
        attach_parent_software_source_to_managed_instance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.change_managed_instance_group_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeManagedInstanceGroupCompartment)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_managed_instance_group_compartment(ctx, from_json, managed_instance_group_id, compartment_id, if_match):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.change_managed_instance_group_compartment(
        managed_instance_group_id=managed_instance_group_id,
        change_managed_instance_group_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.change_scheduled_job_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeScheduledJobCompartment)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_scheduled_job_compartment(ctx, from_json, scheduled_job_id, compartment_id, if_match):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.change_scheduled_job_compartment(
        scheduled_job_id=scheduled_job_id,
        change_scheduled_job_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.change_software_source_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeSoftwareSourceCompartment)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_software_source_compartment(ctx, from_json, software_source_id, compartment_id, if_match):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.change_software_source_compartment(
        software_source_id=software_source_id,
        change_software_source_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.create_managed_instance_group.command_name', 'create'), help=u"""Creates a new Managed Instance Group on the management system. This will not contain any managed instances after it is first created, and they must be added later. \n[Command Reference](createManagedInstanceGroup)""")
@cli_util.option('--display-name', required=True, help=u"""Managed Instance Group identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID for the Compartment""")
@cli_util.option('--description', help=u"""Information specified by the user about the managed instance group""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The Operating System type of the managed instance(s) on which this scheduled job will operate. If not specified, this defaults to Linux.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'ManagedInstanceGroup'})
@cli_util.wrap_exceptions
def create_managed_instance_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, description, freeform_tags, defined_tags, os_family):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if os_family is not None:
        _details['osFamily'] = os_family

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.create_managed_instance_group(
        create_managed_instance_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_instance_group') and callable(getattr(client, 'get_managed_instance_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_instance_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@scheduled_job_group.command(name=cli_util.override('os_management.create_scheduled_job.command_name', 'create'), help=u"""Creates a new Scheduled Job to perform a specific package operation on a set of managed instances or managed instance groups.  Can be created as a one-time execution in the future, or as a recurring execution that repeats on a defined interval. \n[Command Reference](createScheduledJob)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID for the Compartment""")
@cli_util.option('--display-name', required=True, help=u"""Scheduled Job name""")
@cli_util.option('--schedule-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ONETIME", "RECURRING"]), help=u"""the type of scheduling this Scheduled Job follows""")
@cli_util.option('--time-next-execution', required=True, type=custom_types.CLI_DATETIME, help=u"""the desired time for the next execution of this Scheduled Job""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--operation-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]), help=u"""the type of operation this Scheduled Job performs""")
@cli_util.option('--description', help=u"""Details describing the Scheduled Job.""")
@cli_util.option('--interval-type', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "DAY", "WEEK", "MONTH"]), help=u"""the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)""")
@cli_util.option('--interval-value', help=u"""the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)""")
@cli_util.option('--managed-instances', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of managed instances this scheduled job operates on (mutually exclusive with managedInstanceGroups). Either this or the managedInstanceGroups must be supplied.

This option is a JSON list with items of type Id.  For documentation on Id please see our API reference: https://docs.cloud.oracle.com/api/#/en/osmanagement/20190801/datatypes/Id.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--managed-instance-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of managed instance groups this scheduled job operates on (mutually exclusive with managedInstances). Either this or managedInstances must be supplied.

This option is a JSON list with items of type Id.  For documentation on Id please see our API reference: https://docs.cloud.oracle.com/api/#/en/osmanagement/20190801/datatypes/Id.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--update-type', type=custom_types.CliCaseInsensitiveChoice(["SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"]), help=u"""Type of the update (only if operation type is UPDATEALL)""")
@cli_util.option('--package-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)

This option is a JSON list with items of type PackageName.  For documentation on PackageName please see our API reference: https://docs.cloud.oracle.com/api/#/en/osmanagement/20190801/datatypes/PackageName.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--update-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The unique names of the Windows Updates (only if operation type is INSTALL). This is only applicable when the osFamily is for Windows managed instances.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The Operating System type of the managed instance(s) on which this scheduled job will operate. If not specified, this defaults to Linux.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'managed-instances': {'module': 'os_management', 'class': 'list[Id]'}, 'managed-instance-groups': {'module': 'os_management', 'class': 'list[Id]'}, 'package-names': {'module': 'os_management', 'class': 'list[PackageName]'}, 'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}, 'update-names': {'module': 'os_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instances': {'module': 'os_management', 'class': 'list[Id]'}, 'managed-instance-groups': {'module': 'os_management', 'class': 'list[Id]'}, 'package-names': {'module': 'os_management', 'class': 'list[PackageName]'}, 'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}, 'update-names': {'module': 'os_management', 'class': 'list[string]'}}, output_type={'module': 'os_management', 'class': 'ScheduledJob'})
@cli_util.wrap_exceptions
def create_scheduled_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, schedule_type, time_next_execution, operation_type, description, interval_type, interval_value, managed_instances, managed_instance_groups, update_type, package_names, freeform_tags, defined_tags, update_names, os_family):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['scheduleType'] = schedule_type
    _details['timeNextExecution'] = time_next_execution
    _details['operationType'] = operation_type

    if description is not None:
        _details['description'] = description

    if interval_type is not None:
        _details['intervalType'] = interval_type

    if interval_value is not None:
        _details['intervalValue'] = interval_value

    if managed_instances is not None:
        _details['managedInstances'] = cli_util.parse_json_parameter("managed_instances", managed_instances)

    if managed_instance_groups is not None:
        _details['managedInstanceGroups'] = cli_util.parse_json_parameter("managed_instance_groups", managed_instance_groups)

    if update_type is not None:
        _details['updateType'] = update_type

    if package_names is not None:
        _details['packageNames'] = cli_util.parse_json_parameter("package_names", package_names)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if update_names is not None:
        _details['updateNames'] = cli_util.parse_json_parameter("update_names", update_names)

    if os_family is not None:
        _details['osFamily'] = os_family

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.create_scheduled_job(
        create_scheduled_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_job') and callable(getattr(client, 'get_scheduled_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@software_source_group.command(name=cli_util.override('os_management.create_software_source.command_name', 'create'), help=u"""Creates a new custom Software Source on the management system. This will not contain any packages after it is first created, and they must be added later. \n[Command Reference](createSoftwareSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID for the Compartment""")
@cli_util.option('--display-name', required=True, help=u"""User friendly name for the software source""")
@cli_util.option('--arch-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"]), help=u"""The architecture type supported by the Software Source""")
@cli_util.option('--description', help=u"""Information specified by the user about the software source""")
@cli_util.option('--maintainer-name', help=u"""Name of the person maintaining this software source""")
@cli_util.option('--maintainer-email', help=u"""Email address of the person maintaining this software source""")
@cli_util.option('--maintainer-phone', help=u"""Phone number of the person maintaining this software source""")
@cli_util.option('--checksum-type', type=custom_types.CliCaseInsensitiveChoice(["SHA1", "SHA256", "SHA384", "SHA512"]), help=u"""The yum repository checksum type used by this software source""")
@cli_util.option('--parent-id', help=u"""OCID for the parent software source, if there is one""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def create_software_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, arch_type, description, maintainer_name, maintainer_email, maintainer_phone, checksum_type, parent_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['archType'] = arch_type

    if description is not None:
        _details['description'] = description

    if maintainer_name is not None:
        _details['maintainerName'] = maintainer_name

    if maintainer_email is not None:
        _details['maintainerEmail'] = maintainer_email

    if maintainer_phone is not None:
        _details['maintainerPhone'] = maintainer_phone

    if checksum_type is not None:
        _details['checksumType'] = checksum_type

    if parent_id is not None:
        _details['parentId'] = parent_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.create_software_source(
        create_software_source_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_software_source') and callable(getattr(client, 'get_software_source')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_software_source(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@managed_instance_group_group.command(name=cli_util.override('os_management.delete_managed_instance_group.command_name', 'delete'), help=u"""Deletes a Managed Instance Group from the management system \n[Command Reference](deleteManagedInstanceGroup)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_managed_instance_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_group_id, if_match):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.delete_managed_instance_group(
        managed_instance_group_id=managed_instance_group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_instance_group') and callable(getattr(client, 'get_managed_instance_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_managed_instance_group(managed_instance_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@scheduled_job_group.command(name=cli_util.override('os_management.delete_scheduled_job.command_name', 'delete'), help=u"""Cancels an existing Scheduled Job on the management system \n[Command Reference](deleteScheduledJob)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_scheduled_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, scheduled_job_id, if_match):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.delete_scheduled_job(
        scheduled_job_id=scheduled_job_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_job') and callable(getattr(client, 'get_scheduled_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_scheduled_job(scheduled_job_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@software_source_group.command(name=cli_util.override('os_management.delete_software_source.command_name', 'delete'), help=u"""Deletes a custom Software Source on the management system \n[Command Reference](deleteSoftwareSource)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_software_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, software_source_id, if_match):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.delete_software_source(
        software_source_id=software_source_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_software_source') and callable(getattr(client, 'get_software_source')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_software_source(software_source_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@managed_instance_group.command(name=cli_util.override('os_management.detach_child_software_source_from_managed_instance.command_name', 'detach'), help=u"""Removes a child software source from a managed instance. Packages will no longer be able to be installed from these software sources. \n[Command Reference](detachChildSoftwareSourceFromManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-source-id', required=True, help=u"""OCID for the Software Source""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_child_software_source_from_managed_instance(ctx, from_json, managed_instance_id, software_source_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['softwareSourceId'] = software_source_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.detach_child_software_source_from_managed_instance(
        managed_instance_id=managed_instance_id,
        detach_child_software_source_from_managed_instance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.detach_managed_instance_from_managed_instance_group.command_name', 'detach'), help=u"""Removes a Managed Instance from a Managed Instance Group. \n[Command Reference](detachManagedInstanceFromManagedInstanceGroup)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_managed_instance_from_managed_instance_group(ctx, from_json, managed_instance_group_id, managed_instance_id):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.detach_managed_instance_from_managed_instance_group(
        managed_instance_group_id=managed_instance_group_id,
        managed_instance_id=managed_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.detach_parent_software_source_from_managed_instance.command_name', 'detach'), help=u"""Removes a software source from a managed instance. All child software sources will also be removed from the managed instance. Packages will no longer be able to be installed from these software sources. \n[Command Reference](detachParentSoftwareSourceFromManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-source-id', required=True, help=u"""OCID for the Software Source""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_parent_software_source_from_managed_instance(ctx, from_json, managed_instance_id, software_source_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['softwareSourceId'] = software_source_id

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.detach_parent_software_source_from_managed_instance(
        managed_instance_id=managed_instance_id,
        detach_parent_software_source_from_managed_instance_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@erratum_group.command(name=cli_util.override('os_management.get_erratum.command_name', 'get'), help=u"""Returns a specific erratum. \n[Command Reference](getErratum)""")
@cli_util.option('--erratum-id', required=True, help=u"""The OCID of the erratum.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'Erratum'})
@cli_util.wrap_exceptions
def get_erratum(ctx, from_json, erratum_id):

    if isinstance(erratum_id, six.string_types) and len(erratum_id.strip()) == 0:
        raise click.UsageError('Parameter --erratum-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_erratum(
        erratum_id=erratum_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.get_managed_instance.command_name', 'get'), help=u"""Returns a specific Managed Instance. \n[Command Reference](getManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'ManagedInstance'})
@cli_util.wrap_exceptions
def get_managed_instance(ctx, from_json, managed_instance_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_managed_instance(
        managed_instance_id=managed_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.get_managed_instance_group.command_name', 'get'), help=u"""Returns a specific Managed Instance Group. \n[Command Reference](getManagedInstanceGroup)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'ManagedInstanceGroup'})
@cli_util.wrap_exceptions
def get_managed_instance_group(ctx, from_json, managed_instance_group_id):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_managed_instance_group(
        managed_instance_group_id=managed_instance_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.get_scheduled_job.command_name', 'get'), help=u"""Gets the detailed information for the Scheduled Job with the given ID. \n[Command Reference](getScheduledJob)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'ScheduledJob'})
@cli_util.wrap_exceptions
def get_scheduled_job(ctx, from_json, scheduled_job_id):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_scheduled_job(
        scheduled_job_id=scheduled_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.get_software_package.command_name', 'get-software-package'), help=u"""Returns a specific Software Package. \n[Command Reference](getSoftwarePackage)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--software-package-name', required=True, help=u"""The id of the software package.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'SoftwarePackage'})
@cli_util.wrap_exceptions
def get_software_package(ctx, from_json, software_source_id, software_package_name):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    if isinstance(software_package_name, six.string_types) and len(software_package_name.strip()) == 0:
        raise click.UsageError('Parameter --software-package-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_software_package(
        software_source_id=software_source_id,
        software_package_name=software_package_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.get_software_source.command_name', 'get'), help=u"""Returns a specific Software Source. \n[Command Reference](getSoftwareSource)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def get_software_source(ctx, from_json, software_source_id):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_software_source(
        software_source_id=software_source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@windows_update_group.command(name=cli_util.override('os_management.get_windows_update.command_name', 'get'), help=u"""Returns a Windows Update object. \n[Command Reference](getWindowsUpdate)""")
@cli_util.option('--windows-update', required=True, help=u"""The Windows Update""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'WindowsUpdate'})
@cli_util.wrap_exceptions
def get_windows_update(ctx, from_json, windows_update):

    if isinstance(windows_update, six.string_types) and len(windows_update.strip()) == 0:
        raise click.UsageError('Parameter --windows-update cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_windows_update(
        windows_update=windows_update,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('os_management.get_work_request.command_name', 'get'), help=u"""Gets the detailed information for the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.install_all_package_updates_on_managed_instance.command_name', 'install-all-package-updates'), help=u"""Install all of the available package updates for the managed instance. \n[Command Reference](installAllPackageUpdatesOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_all_package_updates_on_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.install_all_package_updates_on_managed_instance(
        managed_instance_id=managed_instance_id,
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


@managed_instance_group.command(name=cli_util.override('os_management.install_all_windows_updates_on_managed_instance.command_name', 'install-all-windows-updates'), help=u"""Install all of the available Windows updates for the managed instance. \n[Command Reference](installAllWindowsUpdatesOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_all_windows_updates_on_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.install_all_windows_updates_on_managed_instance(
        managed_instance_id=managed_instance_id,
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


@managed_instance_group.command(name=cli_util.override('os_management.install_package_on_managed_instance.command_name', 'install-package'), help=u"""Installs a package on a managed instance. \n[Command Reference](installPackageOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-package-name', required=True, help=u"""Package name""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_package_on_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id, software_package_name):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.install_package_on_managed_instance(
        managed_instance_id=managed_instance_id,
        software_package_name=software_package_name,
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


@managed_instance_group.command(name=cli_util.override('os_management.install_package_update_on_managed_instance.command_name', 'install-package-update'), help=u"""Updates a package on a managed instance. \n[Command Reference](installPackageUpdateOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-package-name', required=True, help=u"""Package name""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_package_update_on_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id, software_package_name):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.install_package_update_on_managed_instance(
        managed_instance_id=managed_instance_id,
        software_package_name=software_package_name,
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


@managed_instance_group.command(name=cli_util.override('os_management.install_windows_update_on_managed_instance.command_name', 'install-windows-update'), help=u"""Installs a Windows update on a managed instance. \n[Command Reference](installWindowsUpdateOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--windows-update-name', required=True, help=u"""Unique identifier for the Windows update. NOTE - This is not an OCID, but is a unique identifier assigned by Microsoft. Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_windows_update_on_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id, windows_update_name):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.install_windows_update_on_managed_instance(
        managed_instance_id=managed_instance_id,
        windows_update_name=windows_update_name,
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


@managed_instance_group.command(name=cli_util.override('os_management.list_available_packages_for_managed_instance.command_name', 'list-available-packages-for'), help=u"""Returns a list of packages available for install on the Managed Instance. \n[Command Reference](listAvailablePackagesForManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[InstallablePackageSummary]'})
@cli_util.wrap_exceptions
def list_available_packages_for_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_available_packages_for_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_available_packages_for_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_available_packages_for_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_available_software_sources_for_managed_instance.command_name', 'list-available-software-sources-for'), help=u"""Returns a list of available software sources for a Managed Instance. \n[Command Reference](listAvailableSoftwareSourcesForManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[AvailableSoftwareSourceSummary]'})
@cli_util.wrap_exceptions
def list_available_software_sources_for_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_available_software_sources_for_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_available_software_sources_for_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_available_software_sources_for_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_available_updates_for_managed_instance.command_name', 'list-available-updates-for'), help=u"""Returns a list of available updates for a Managed Instance. \n[Command Reference](listAvailableUpdatesForManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[AvailableUpdateSummary]'})
@cli_util.wrap_exceptions
def list_available_updates_for_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_available_updates_for_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_available_updates_for_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_available_updates_for_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_available_windows_updates_for_managed_instance.command_name', 'list-available-windows-updates-for'), help=u"""Returns a list of available Windows updates for a Managed Instance. This is only applicable to Windows instances. \n[Command Reference](listAvailableWindowsUpdatesForManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--is-eligible-for-installation', type=custom_types.CliCaseInsensitiveChoice(["INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN"]), help=u"""Indicator of whether the update can be installed using OSMS.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[AvailableWindowsUpdateSummary]'})
@cli_util.wrap_exceptions
def list_available_windows_updates_for_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by, is_eligible_for_installation):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if is_eligible_for_installation is not None:
        kwargs['is_eligible_for_installation'] = is_eligible_for_installation
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_available_windows_updates_for_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_available_windows_updates_for_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_available_windows_updates_for_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@erratum_summary_group.command(name=cli_util.override('os_management.list_errata.command_name', 'list-errata'), help=u"""Returns a list of all of the currently available Errata in the system \n[Command Reference](listErrata)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--erratum-id', help=u"""The OCID of the erratum.""")
@cli_util.option('--advisory-name', help=u"""The assigned erratum name. It's unique and not changeable.

Example: `ELSA-2020-5804`""")
@cli_util.option('--time-issue-date-start', type=custom_types.CLI_DATETIME, help=u"""The issue date after which to list all errata, in ISO 8601 format

Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-issue-date-end', type=custom_types.CLI_DATETIME, help=u"""The issue date before which to list all errata, in ISO 8601 format

Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ISSUEDATE", "ADVISORYNAME"]), help=u"""The field to sort errata by. Only one sort order may be provided. Default order for ISSUEDATE is descending. Default order for ADVISORYNAME is ascending. If no value is specified ISSUEDATE is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ErratumSummary]'})
@cli_util.wrap_exceptions
def list_errata(ctx, from_json, all_pages, page_size, compartment_id, erratum_id, advisory_name, time_issue_date_start, time_issue_date_end, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if erratum_id is not None:
        kwargs['erratum_id'] = erratum_id
    if advisory_name is not None:
        kwargs['advisory_name'] = advisory_name
    if time_issue_date_start is not None:
        kwargs['time_issue_date_start'] = time_issue_date_start
    if time_issue_date_end is not None:
        kwargs['time_issue_date_end'] = time_issue_date_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_errata,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_errata,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_errata(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_managed_instance_errata.command_name', 'list-managed-instance-errata'), help=u"""Returns a list of errata relevant to the Managed Instance. \n[Command Reference](listManagedInstanceErrata)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ErratumSummary]'})
@cli_util.wrap_exceptions
def list_managed_instance_errata(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_instance_errata,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_instance_errata,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_managed_instance_errata(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.list_managed_instance_groups.command_name', 'list'), help=u"""Returns a list of all Managed Instance Groups. \n[Command Reference](listManagedInstanceGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current lifecycle state for the object.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The OS family for which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ManagedInstanceGroupSummary]'})
@cli_util.wrap_exceptions
def list_managed_instance_groups(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by, lifecycle_state, os_family):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if os_family is not None:
        kwargs['os_family'] = os_family
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_instance_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_instance_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_instance_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_managed_instances.command_name', 'list'), help=u"""Returns a list of all Managed Instances. \n[Command Reference](listManagedInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The OS family for which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ManagedInstanceSummary]'})
@cli_util.wrap_exceptions
def list_managed_instances(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by, os_family):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if os_family is not None:
        kwargs['os_family'] = os_family
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_managed_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_managed_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_managed_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_packages_installed_on_managed_instance.command_name', 'list-packages-installed'), help=u"""Returns a list of installed packages on the Managed Instance. \n[Command Reference](listPackagesInstalledOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[InstalledPackageSummary]'})
@cli_util.wrap_exceptions
def list_packages_installed_on_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_packages_installed_on_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_packages_installed_on_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_packages_installed_on_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.list_scheduled_jobs.command_name', 'list'), help=u"""Returns a list of all of the currently active Scheduled Jobs in the system \n[Command Reference](listScheduledJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--managed-instance-id', help=u"""The ID of the managed instance for which to list resources.""")
@cli_util.option('--managed-instance-group-id', help=u"""The ID of the managed instace group for which to list resources.""")
@cli_util.option('--operation-type', type=custom_types.CliCaseInsensitiveChoice(["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]), help=u"""The operation type for which to list resources""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current lifecycle state for the object.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The OS family for which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ScheduledJobSummary]'})
@cli_util.wrap_exceptions
def list_scheduled_jobs(ctx, from_json, all_pages, page_size, compartment_id, display_name, managed_instance_id, managed_instance_group_id, operation_type, limit, page, sort_order, sort_by, lifecycle_state, os_family):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if managed_instance_group_id is not None:
        kwargs['managed_instance_group_id'] = managed_instance_group_id
    if operation_type is not None:
        kwargs['operation_type'] = operation_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if os_family is not None:
        kwargs['os_family'] = os_family
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scheduled_jobs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scheduled_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_scheduled_jobs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.list_software_source_packages.command_name', 'list-software-source-packages'), help=u"""Lists Software Packages in a Software Source \n[Command Reference](listSoftwareSourcePackages)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[SoftwarePackageSummary]'})
@cli_util.wrap_exceptions
def list_software_source_packages(ctx, from_json, all_pages, page_size, software_source_id, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_software_source_packages,
            software_source_id=software_source_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_software_source_packages,
            limit,
            page_size,
            software_source_id=software_source_id,
            **kwargs
        )
    else:
        result = client.list_software_source_packages(
            software_source_id=software_source_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.list_software_sources.command_name', 'list'), help=u"""Returns a list of all Software Sources. \n[Command Reference](listSoftwareSources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current lifecycle state for the object.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[SoftwareSourceSummary]'})
@cli_util.wrap_exceptions
def list_software_sources(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_software_sources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_software_sources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_software_sources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.list_upcoming_scheduled_jobs.command_name', 'list-upcoming'), help=u"""Returns a list of all of the Scheduled Jobs whose next execution time is at or before the specified time. \n[Command Reference](listUpcomingScheduledJobs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--time-end', required=True, type=custom_types.CLI_DATETIME, help=u"""The cut-off time before which to list all upcoming schedules, in ISO 8601 format

Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--tag-name', help=u"""The name of the tag.""")
@cli_util.option('--tag-value', help=u"""The value for the tag.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The current lifecycle state for the object.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The OS family for which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[ScheduledJobSummary]'})
@cli_util.wrap_exceptions
def list_upcoming_scheduled_jobs(ctx, from_json, all_pages, page_size, compartment_id, time_end, display_name, limit, page, sort_order, sort_by, tag_name, tag_value, lifecycle_state, os_family):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if tag_name is not None:
        kwargs['tag_name'] = tag_name
    if tag_value is not None:
        kwargs['tag_value'] = tag_value
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if os_family is not None:
        kwargs['os_family'] = os_family
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_upcoming_scheduled_jobs,
            compartment_id=compartment_id,
            time_end=time_end,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_upcoming_scheduled_jobs,
            limit,
            page_size,
            compartment_id=compartment_id,
            time_end=time_end,
            **kwargs
        )
    else:
        result = client.list_upcoming_scheduled_jobs(
            compartment_id=compartment_id,
            time_end=time_end,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@windows_update_group.command(name=cli_util.override('os_management.list_windows_updates.command_name', 'list'), help=u"""Returns a list of Windows Updates. \n[Command Reference](listWindowsUpdates)""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[WindowsUpdateSummary]'})
@cli_util.wrap_exceptions
def list_windows_updates(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_windows_updates,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_windows_updates,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_windows_updates(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.list_windows_updates_installed_on_managed_instance.command_name', 'list-windows-updates-installed'), help=u"""Returns a list of installed Windows updates for a Managed Instance. This is only applicable to Windows instances. \n[Command Reference](listWindowsUpdatesInstalledOnManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--compartment-id', help=u"""The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[InstalledWindowsUpdateSummary]'})
@cli_util.wrap_exceptions
def list_windows_updates_installed_on_managed_instance(ctx, from_json, all_pages, page_size, managed_instance_id, display_name, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_windows_updates_installed_on_managed_instance,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_windows_updates_installed_on_managed_instance,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    else:
        result = client.list_windows_updates_installed_on_managed_instance(
            managed_instance_id=managed_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('os_management.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Gets the errors for the work request with the given ID. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

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
    client = cli_util.build_client('os_management', 'os_management', ctx)
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


@work_request_group.command(name=cli_util.override('os_management.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Lists the log entries for the work request with the given ID. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

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
    client = cli_util.build_client('os_management', 'os_management', ctx)
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


@work_request_summary_group.command(name=cli_util.override('os_management.list_work_requests.command_name', 'list-work-requests'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--managed-instance-id', help=u"""The ID of the managed instance for which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--os-family', type=custom_types.CliCaseInsensitiveChoice(["LINUX", "WINDOWS", "ALL"]), help=u"""The OS family for which to list resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, display_name, managed_instance_id, limit, page, sort_order, sort_by, os_family):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if managed_instance_id is not None:
        kwargs['managed_instance_id'] = managed_instance_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if os_family is not None:
        kwargs['os_family'] = os_family
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@managed_instance_group.command(name=cli_util.override('os_management.remove_package_from_managed_instance.command_name', 'remove'), help=u"""Removes an installed package from a managed instance. \n[Command Reference](removePackageFromManagedInstance)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""OCID for the managed instance""")
@cli_util.option('--software-package-name', required=True, help=u"""Package name""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELLING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_package_from_managed_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_id, software_package_name):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.remove_package_from_managed_instance(
        managed_instance_id=managed_instance_id,
        software_package_name=software_package_name,
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


@software_source_group.command(name=cli_util.override('os_management.remove_packages_from_software_source.command_name', 'remove'), help=u"""Removes a given list of Software Packages from a specific Software Source. \n[Command Reference](removePackagesFromSoftwareSource)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--package-names', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""the list of package names""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'package-names': {'module': 'os_management', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-names': {'module': 'os_management', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def remove_packages_from_software_source(ctx, from_json, software_source_id, package_names):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['packageNames'] = cli_util.parse_json_parameter("package_names", package_names)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.remove_packages_from_software_source(
        software_source_id=software_source_id,
        remove_packages_from_software_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.run_scheduled_job_now.command_name', 'run-scheduled-job-now'), help=u"""This will trigger an already created Scheduled Job to being executing immediately instead of waiting for its next regularly scheduled time. \n[Command Reference](runScheduledJobNow)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def run_scheduled_job_now(ctx, from_json, scheduled_job_id, if_match):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.run_scheduled_job_now(
        scheduled_job_id=scheduled_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@software_source_group.command(name=cli_util.override('os_management.search_software_packages.command_name', 'search-software-packages'), help=u"""Searches all of the available Software Sources and returns any/all Software Packages matching the search criteria. \n[Command Reference](searchSoftwarePackages)""")
@cli_util.option('--software-package-name', help=u"""the identifier for the software package (not an OCID)""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable.

Example: `My new resource`""")
@cli_util.option('--cve-name', help=u"""The name of the CVE as published. Example: `CVE-2006-4535`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'list[SoftwarePackageSearchSummary]'})
@cli_util.wrap_exceptions
def search_software_packages(ctx, from_json, software_package_name, display_name, cve_name, limit, page, sort_order, sort_by):

    kwargs = {}
    if software_package_name is not None:
        kwargs['software_package_name'] = software_package_name
    if display_name is not None:
        kwargs['display_name'] = display_name
    if cve_name is not None:
        kwargs['cve_name'] = cve_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.search_software_packages(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scheduled_job_group.command(name=cli_util.override('os_management.skip_next_scheduled_job_execution.command_name', 'skip-next-scheduled-job-execution'), help=u"""This will force an already created Scheduled Job to skip its next regularly scheduled execution \n[Command Reference](skipNextScheduledJobExecution)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def skip_next_scheduled_job_execution(ctx, from_json, scheduled_job_id, if_match):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.skip_next_scheduled_job_execution(
        scheduled_job_id=scheduled_job_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@managed_instance_group_group.command(name=cli_util.override('os_management.update_managed_instance_group.command_name', 'update'), help=u"""Updates a specific Managed Instance Group. \n[Command Reference](updateManagedInstanceGroup)""")
@cli_util.option('--managed-instance-group-id', required=True, help=u"""OCID for the managed instance group""")
@cli_util.option('--display-name', help=u"""Managed Instance Group identifier""")
@cli_util.option('--description', help=u"""Information specified by the user about the managed instance group""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'ManagedInstanceGroup'})
@cli_util.wrap_exceptions
def update_managed_instance_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, managed_instance_group_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(managed_instance_group_id, six.string_types) and len(managed_instance_group_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-group-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.update_managed_instance_group(
        managed_instance_group_id=managed_instance_group_id,
        update_managed_instance_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_managed_instance_group') and callable(getattr(client, 'get_managed_instance_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_managed_instance_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@scheduled_job_group.command(name=cli_util.override('os_management.update_scheduled_job.command_name', 'update'), help=u"""Updates an existing Scheduled Job on the management system. \n[Command Reference](updateScheduledJob)""")
@cli_util.option('--scheduled-job-id', required=True, help=u"""The ID of the scheduled job.""")
@cli_util.option('--display-name', help=u"""Scheduled Job name""")
@cli_util.option('--description', help=u"""Details describing the Scheduled Job.""")
@cli_util.option('--schedule-type', type=custom_types.CliCaseInsensitiveChoice(["ONETIME", "RECURRING"]), help=u"""the type of scheduling this Scheduled Job follows""")
@cli_util.option('--time-next-execution', type=custom_types.CLI_DATETIME, help=u"""the desired time for the next execution of this Scheduled Job""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--interval-type', type=custom_types.CliCaseInsensitiveChoice(["HOUR", "DAY", "WEEK", "MONTH"]), help=u"""the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)""")
@cli_util.option('--interval-value', help=u"""the value for the interval period for a recurring Scheduled Job (only if schedule type is RECURRING)""")
@cli_util.option('--operation-type', type=custom_types.CliCaseInsensitiveChoice(["INSTALL", "UPDATE", "REMOVE", "UPDATEALL"]), help=u"""the type of operation this Scheduled Job performs""")
@cli_util.option('--update-type', type=custom_types.CliCaseInsensitiveChoice(["SECURITY", "BUGFIX", "ENHANCEMENT", "ALL"]), help=u"""Type of the update (only if operation type is UPDATEALL)""")
@cli_util.option('--package-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the id of the package (only if operation type is INSTALL/UPDATE/REMOVE)

This option is a JSON list with items of type PackageName.  For documentation on PackageName please see our API reference: https://docs.cloud.oracle.com/api/#/en/osmanagement/20190801/datatypes/PackageName.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--update-names', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The unique names of the Windows Updates (only if operation type is INSTALL). This is only applicable when the osFamily is for Windows managed instances.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'package-names': {'module': 'os_management', 'class': 'list[PackageName]'}, 'update-names': {'module': 'os_management', 'class': 'list[string]'}, 'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'package-names': {'module': 'os_management', 'class': 'list[PackageName]'}, 'update-names': {'module': 'os_management', 'class': 'list[string]'}, 'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'ScheduledJob'})
@cli_util.wrap_exceptions
def update_scheduled_job(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, scheduled_job_id, display_name, description, schedule_type, time_next_execution, interval_type, interval_value, operation_type, update_type, package_names, update_names, freeform_tags, defined_tags, if_match):

    if isinstance(scheduled_job_id, six.string_types) and len(scheduled_job_id.strip()) == 0:
        raise click.UsageError('Parameter --scheduled-job-id cannot be whitespace or empty string')
    if not force:
        if package_names or update_names or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to package-names and update-names and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if schedule_type is not None:
        _details['scheduleType'] = schedule_type

    if time_next_execution is not None:
        _details['timeNextExecution'] = time_next_execution

    if interval_type is not None:
        _details['intervalType'] = interval_type

    if interval_value is not None:
        _details['intervalValue'] = interval_value

    if operation_type is not None:
        _details['operationType'] = operation_type

    if update_type is not None:
        _details['updateType'] = update_type

    if package_names is not None:
        _details['packageNames'] = cli_util.parse_json_parameter("package_names", package_names)

    if update_names is not None:
        _details['updateNames'] = cli_util.parse_json_parameter("update_names", update_names)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.update_scheduled_job(
        scheduled_job_id=scheduled_job_id,
        update_scheduled_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_scheduled_job') and callable(getattr(client, 'get_scheduled_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_scheduled_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@software_source_group.command(name=cli_util.override('os_management.update_software_source.command_name', 'update'), help=u"""Updates an existing custom Software Source on the management system. \n[Command Reference](updateSoftwareSource)""")
@cli_util.option('--software-source-id', required=True, help=u"""The OCID of the software source.""")
@cli_util.option('--display-name', help=u"""User friendly name for the software source""")
@cli_util.option('--description', help=u"""Information specified by the user about the software source""")
@cli_util.option('--maintainer-name', help=u"""Name of the person maintaining this software source""")
@cli_util.option('--maintainer-email', help=u"""Email address of the person maintaining this software source""")
@cli_util.option('--maintainer-phone', help=u"""Phone number of the person maintaining this software source""")
@cli_util.option('--checksum-type', type=custom_types.CliCaseInsensitiveChoice(["SHA1", "SHA256", "SHA384", "SHA512"]), help=u"""The yum repository checksum type used by this software source""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'SoftwareSource'})
@cli_util.wrap_exceptions
def update_software_source(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, software_source_id, display_name, description, maintainer_name, maintainer_email, maintainer_phone, checksum_type, freeform_tags, defined_tags, if_match):

    if isinstance(software_source_id, six.string_types) and len(software_source_id.strip()) == 0:
        raise click.UsageError('Parameter --software-source-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if maintainer_name is not None:
        _details['maintainerName'] = maintainer_name

    if maintainer_email is not None:
        _details['maintainerEmail'] = maintainer_email

    if maintainer_phone is not None:
        _details['maintainerPhone'] = maintainer_phone

    if checksum_type is not None:
        _details['checksumType'] = checksum_type

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('os_management', 'os_management', ctx)
    result = client.update_software_source(
        software_source_id=software_source_id,
        update_software_source_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_software_source') and callable(getattr(client, 'get_software_source')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_software_source(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
