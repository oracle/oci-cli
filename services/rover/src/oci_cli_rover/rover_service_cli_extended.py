# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
import oci
from oci_cli import cli_util, json_skeleton_utils, custom_types
from oci_cli.aliasing import CommandGroupWithAlias
from oci_cli.cli_util import create_config_and_signer_based_on_click_context

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_rover.rover_utils import setup_master_key_policy, \
    validate_policy_parameters, upload_bundle_for_upgrade, check_import_history, import_bundle_for_upgrade, \
    check_status, dispatch_diag_request, bundle_decrypt
from services.rover.src.oci_cli_rover.datasync_task import rover_datasync_task_group
from services.rover.src.oci_cli_rover.datasync_task_definition import rover_datasync_task_definition_group


@click.command('device', cls=CommandGroupWithAlias, help="""Rover Physical Device.""")
@cli_util.help_option_group
def rover_device_group():
    pass


rover_service_cli.rover_service_group.add_command(rover_device_group)


@click.command('system-upgrade', cls=CommandGroupWithAlias, help="""System Upgrade of Rover Physical Device.""")
@cli_util.help_option_group
def rover_system_upgrade_group():
    pass


@click.command('diagnostics', cls=CommandGroupWithAlias, help="""Rover Diagnostic Service.""")
@cli_util.help_option_group
def rover_diagnostics_group():
    pass


@click.command('bundle', cls=CommandGroupWithAlias, help="""Rover Diagnostic Service Bundle.""")
@cli_util.help_option_group
def rover_diagnostics_bundle_group():
    pass


@click.command('data-sync', cls=CommandGroupWithAlias, help="""Data Sync Service CLI.""")
@cli_util.help_option_group
def rover_datasync_group():
    pass


rover_device_group.add_command(rover_system_upgrade_group)

# add all data-sync CLIs
rover_device_group.add_command(rover_datasync_group)
rover_datasync_group.add_command(rover_datasync_task_definition_group)
rover_datasync_group.add_command(rover_datasync_task_group)
# end of data-sync CLIs

rover_device_group.add_command(rover_diagnostics_group)
rover_diagnostics_group.add_command(rover_diagnostics_bundle_group)


@rover_service_cli.rover_service_group.command(name="create-master-key-policy",
                                               help=u"""Create Policy for Master key""")
@cli_util.option('--master-key-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--policy-compartment-id', help=u"""Compartment ID where the policy should be created""")
@cli_util.option('--policy-name', help=u"""Display name for the policy to be created""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def create_master_key_policy_extended(ctx, **kwargs):
    validate_policy_parameters(**kwargs)
    result = setup_master_key_policy(ctx, **kwargs)
    cli_util.render_response(result, ctx)


@rover_system_upgrade_group.command(name="upload-bundle", help=u"""Uploads the system bundle to Object Storage bucket 'rover-system-upgrade-staging'""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--file', type=click.File(mode='rb'), required=True, help=u"""File path of the bundle to be uploaded""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.wrap_exceptions
def upload_bundle(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    bundle_file_path = kwargs['file']
    confirm_file_name = "The upgrade would only process if the bundle file name is of the format " \
                        "'X.Y.Z.YYYYMMDDHHmmSS.rover_disconnected_release.tar'. " \
                        "Do you want to proceed with the upload?(Y/N)"
    value_file_name = click.confirm(click.style(confirm_file_name, fg="yellow"))
    if value_file_name:
        upload_bundle_for_upgrade(ctx, bundle_file_path)
    else:
        click.echo("Exiting the upload!")


@rover_system_upgrade_group.command(name="import-bundle", help=u"""Starts Validation and imports the upgrade bundle""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--object-name', required=True, help=u"""Name of the upgrade bundle which has to be imported""")
@cli_util.option('--wait', type=click.BOOL, default="true", help=u"""Whether or not the call should poll until the import is successful. By default, `wait` is set to `true`. Set `wait` to `false` to return immediately once the import has started.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.wrap_exceptions
def import_bundle(ctx, wait, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    bundle_file_path = kwargs['object_name']
    create_config_and_signer_based_on_click_context(ctx)
    should_wait = True
    if wait is not None:
        should_wait = wait
    import_bundle_for_upgrade(ctx, bundle_file_path, should_wait)


@rover_system_upgrade_group.command(name="get-import-status", help=u"""Checks the import progress status""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--task-id', required=True, help=u"""Task-ID for which the status needs to be checked""")
@cli_util.option('--wait', type=click.BOOL, default="true", help=u"""Whether or not the call should poll until the import is successful. By default, `wait` is set to `true`. Set `wait` to `false` to return immediately once the import has started.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
def check_import_status(ctx, wait, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    task_id = kwargs['task_id']
    should_wait = False
    if wait is not None:
        should_wait = wait
    check_status(ctx, task_id, should_wait)


@rover_system_upgrade_group.command(name="get-import-history", help=u"""Shows history of all import tasks""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
def check_imports(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    check_import_history(ctx)


@rover_diagnostics_bundle_group.command(name="create", help=u"""Create a diag bundle""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--display-name', type=str, help=u"""Displayed name of diagnostic bundle""")
@cli_util.option('--node-name', type=str, help=u"""Rover Node Name""")
@cli_util.option('--wait-for-state', type=click.Choice(["ACCEPTED", "IN_PROGRESS", "COMPLETED", "FAILED"],
                 case_sensitive=True), multiple=True,
                 help=u"""Wait for a diagnostic bundle to reach a
                          specific state Specify this option to perform the
                          action and then wait until the resource
                          reaches a given lifecycle state. Multiple
                          states can be specified, returning on the
                          first state. For example, --wait-for-state
                          COMPLETED --wait-for-state FAILED would
                          return on whichever lifecycle state is
                          reached first.""")
@cli_util.option('--wait-interval-seconds', default=5, type=int, help=u"""Frequency to poll the state of a diagnostic bundle (seconds)""")
@cli_util.option('--max-wait-seconds', default=1800, type=int, help=u"""Wait for a diagnostic bundle to reach a specific state (seconds)""")
@cli_util.option('--use-basic-auth', is_flag=True, type=click.BOOL, default=False, help=u"""Use Basic Authentication for Diagnostic Requets - Retrieved from Serial Console""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.wrap_exceptions
@cli_util.help_option
def create_diag_bundle(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    data = {}
    wait = None
    if "display_name" in kwargs and kwargs.get("display_name") is not None:
        data["displayName"] = kwargs.get("display_name")
    if "node_name" in kwargs and kwargs.get("node_name") is not None:
        data["nodeName"] = kwargs.get("node_name")
    state = kwargs.get("wait_for_state")
    if state is not None:
        wait = {}
        wait["state"] = state
        wait["interval_seconds"] = kwargs.get("wait_interval_seconds")
        wait["max_wait_seconds"] = kwargs.get("max_wait_seconds")

    dispatch_diag_request(ctx, basic_auth=kwargs.get("use_basic_auth"), data=data,
                          http_method="POST", wait=wait)


@rover_diagnostics_bundle_group.command(name="view-summary", help=u"""View diagnostic bundle status""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--bundle-id', type=str, required=True, help=u""""Bundle Identifier (OCID)""")
@cli_util.option('--node-name', type=str, help=u"""Rover Node Name""")
@cli_util.option('--use-basic-auth', is_flag=True, type=click.BOOL, default=False, help=u"""Use Basic Authentication for Diagnostic Requets - Retrieved from Serial Console""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.wrap_exceptions
def view_diag_bundle(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    data = {}
    if "node_name" in kwargs and kwargs["node_name"] is not None:
        data["nodeName"] = kwargs.get("node_name")
    addtional_url = kwargs.get("bundle_id") + "/actions/viewSummary"
    dispatch_diag_request(ctx, basic_auth=kwargs.get("use_basic_auth"), data=data,
                          http_method="POST", additional_url_path=addtional_url)


@rover_diagnostics_bundle_group.command(name="cancel", help=u"""Cancel a diagnostic bundle execution""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--bundle-id', type=str, required=True, help=u""""Bundle Identifier (OCID)""")
@cli_util.option('--node-name', type=str, help=u"""Rover Node Name""")
@cli_util.option('--use-basic-auth', is_flag=True, type=click.BOOL, default=False, help=u"""Use Basic Authentication for Diagnostic Requets - Retrieved from Serial Console""")
@cli_util.option('--wait-for-state', type=click.Choice(["CANCELED"], case_sensitive=False), help=u"""Wait for a diagnostic bundle to reach canceled state""")
@cli_util.option('--wait-interval-seconds', default=5, type=int, help=u"""Frequency to poll the state of a diagnostic bundle (seconds)""")
@cli_util.option('--max-wait-seconds', default=120, type=int, help=u"""Wait for a diagnostic bundle to reach a specific state (seconds)""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.wrap_exceptions
def cancel_diag_bundle(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    data = {}
    params = {}
    wait = None
    state = kwargs.get("wait_for_state")
    if "node_name" in kwargs and kwargs["node_name"] is not None:
        params["nodeName"] = kwargs.get("node_name")
        data["nodeName"] = kwargs.get("node_name")
    additional_url = kwargs.get("bundle_id")
    if state:
        wait = {}
        wait["state"] = state
        wait["interval_seconds"] = kwargs.get("wait_interval_seconds")
        wait["max_wait_seconds"] = kwargs.get("max_wait_seconds")

    dispatch_diag_request(ctx, basic_auth=kwargs.get("use_basic_auth"), params=params, wait=wait,
                          data=data, http_method="DELETE", additional_url_path=additional_url)
    # the delete call doesn't return the for JSON back,
    # an additional call is needed so the user knows its in the correct state
    if kwargs.get("wait_for_state") is None:
        dispatch_diag_request(ctx, basic_auth=kwargs.get("use_basic_auth"), data=data,
                              http_method="POST", additional_url_path=additional_url + "/actions/viewSummary")


@rover_diagnostics_bundle_group.command(name="get", help=u"""Downloads a Specific Diag Bundle""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--bundle-id', required=True, help=u"""Bundle Identifier (OCID)""")
@cli_util.option('--file', required=True, help=u"""Filename for the downloaded diagnostics bundle archive""")
@cli_util.option('--encryption-key-file', help=u"""Encryption Key File for the Bundle. Encryption Key must be retrieved from Serial Console, then stored in this file""")
@cli_util.option('--node-name', type=str, help=u"""Rover Node Name""")
@cli_util.option('--use-basic-auth', is_flag=True, type=click.BOOL, default=False, help=u"""Use Basic Authentication for Diagnostic Requets - Retrieved from Serial Console""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.wrap_exceptions
def get_bundle(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    data = {}
    data["nodeName"] = kwargs.get("node_name")
    filename = kwargs.get("file")
    temp_file = '/tmp/diag_encrypted_' + filename
    encryption_key_file = kwargs.get("encryption_key_file")
    dispatch_diag_request(ctx, additional_url_path=kwargs.get('bundle_id'), basic_auth=kwargs.get("use_basic_auth"), data=data, http_method="GET", stream=True, stream_file_location=temp_file)
    if "encryption_key_file" in kwargs and kwargs["encryption_key_file"] is not None:
        with open(encryption_key_file) as f:
            bundle_key = f.readline().strip('\n')
        bundle_decrypt(temp_file, filename, bundle_key)
    else:
        click.echo("Diagnostic Bundle has been downloaded successfully. Refer to serial console Diagnostics->Help menu to decrypt the downloaded bundle")


@rover_diagnostics_bundle_group.command(name="list", help=u"""Returns a list of DiagBundles""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.option('--node-name', help=u"""Node Hostname""")
@cli_util.option('--lifecycle-state', help=u"""Filter Bundle Requests according to one of the Lifecycle States: ACCEPTED, IN_PROGRESS, COMPLETED, FAILED, CANCELING, CANCELED""")
@cli_util.option('--use-basic-auth', is_flag=True, type=click.BOOL, default=False, help=u"""Use Basic Authentication for Diagnostic Requets - Retrieved from Serial Console""")
@cli_util.option('--sort-by', help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'""")
@cli_util.option('--limit', default=10, type=int, help=u"""The maximum number of items to return. Range: 1 to 100, default is 10""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@cli_util.help_option
@cli_util.wrap_exceptions
def list_bundles(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config
    params = {}
    params["nodeName"] = kwargs.get("node_name")
    params["lifecycleState"] = kwargs.get("lifecycle_state")
    params["limit"] = kwargs.get("limit")
    params["page"] = kwargs.get("page")
    params["sortByField"] = kwargs.get("sort_by")
    params["sortOrder"] = kwargs.get("sort_order")
    dispatch_diag_request(ctx, basic_auth=kwargs.get("use_basic_auth"), params=params, http_method="GET")
