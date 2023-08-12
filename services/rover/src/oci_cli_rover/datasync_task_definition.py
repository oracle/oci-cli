# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

# Packaged here are all data-sync task-definition" functions
import click
import json
import oci
from oci_cli import cli_util, json_skeleton_utils, custom_types
from oci_cli.aliasing import CommandGroupWithAlias
from services.rover.src.oci_cli_rover.rover_utils import read_json_file, read_json_string, dispatch_datasync_request

ROVER_DATASYNC_TASK_DEF_API_BASE_PATH = "/20201030/taskDefinitions"
DATA_STORE_TYPE = ["OCI", "RED"]


@click.command('task-definition', cls=CommandGroupWithAlias, help="""Data Sync TaskDefinition CRUD operations.""")
@cli_util.help_option_group
def rover_datasync_task_definition_group():
    pass


def parse_definition_input(**kwargs):
    data = {
        "name": kwargs.get("name"),
        "rateLimit": kwargs.get("rate_limit"),
        "syncOnCreate": kwargs.get("sync_on_create")
    }

    src_datastore_type = None
    dest_datastore_type = None

    # --source
    source = kwargs.get('source')
    if source:
        if source.startswith("file://"):
            # parse the file
            data["dataSyncSource"] = read_json_file(source[7:])
        else:
            # parse the json string directly
            data["dataSyncSource"] = read_json_string(source)

        # validate src_datastore_type
        src_datastore_type = data["dataSyncSource"]["dataStore"]
        if src_datastore_type not in DATA_STORE_TYPE:
            raise Exception(f"Unknown source dataStore type: {src_datastore_type}")

    # --destination
    destination = kwargs.get('destination')
    if destination:
        if destination.startswith("file://"):
            # parse the file
            data["dataSyncDestination"] = read_json_file(destination[7:])
        else:
            # parse the json string directly
            data["dataSyncDestination"] = read_json_string(destination)

        # validate dest_datastore_type
        dest_datastore_type = data["dataSyncDestination"]["dataStore"]
        if dest_datastore_type not in DATA_STORE_TYPE:
            raise Exception(f"Unknown destination dataStore type: {dest_datastore_type}")

    # make sure source and destination are of different datastore types
    if src_datastore_type and dest_datastore_type and src_datastore_type == dest_datastore_type:
        raise Exception("DataStore type for both source and destination must not be the same")

    # --schedule
    schedule = kwargs.get('schedule')
    if schedule:
        if schedule.startswith("file://"):
            schedule_object = read_json_file(schedule[7:])
        else:
            schedule_object = read_json_string(schedule)

        # if "priority" exists in schedule_object map, convert/replace it with integer value
        priority = "priority"
        if priority in schedule_object:
            # consistent with UI
            priority_mapping = {
                "LOW": 0,
                "MEDIUM": 5,
                "HIGH": 10
            }

            priority_value = schedule_object[priority]
            schedule_object[priority] = priority_mapping[priority_value.upper()]

        data["dataSyncSchedule"] = schedule_object

    # fully populated CreateTaskDefinitionDetails object
    # print(f"Posting TaskDefinitionDetails: \n{json.dumps(data, indent=2)}")
    return data


@rover_datasync_task_definition_group.command(name="create", help=u"""Create TaskDefinition""")
@click.pass_context
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, required=True,
                 help=u"""Provide the details about the source datastore in JSON structure either in-line or
                 via a local file, file://path-to/data-sync-source-json-file.""")
@cli_util.option('--destination', type=custom_types.CLI_COMPLEX_TYPE, required=True,
                 help=u"""Provide the details about the destination datastore in JSON structure either in-line or
                 via a local file, file://path-to/data-sync-destination-json-file.""")
@cli_util.option('--schedule', type=custom_types.CLI_COMPLEX_TYPE, required=False,
                 help=u"""Provide the details about how the task execution is scheduled in JSON structure either in-line
                 or via a local file, file://path-to/schedule-json-file.""")
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'source': {'module': 'rover', 'class': 'DataStore'},
        'destination': {'module': 'rover', 'class': 'DataStore'},
        'schedule': {'module': 'rover', 'class': 'DataSyncSchedule'}}
)
@cli_util.option('--name', type=str, required=True, help=u"""Short description of the Task Definition""")
@cli_util.option('--rate-limit', type=str, required=False,
                 help=u"""If provided, it sets the data transfer rate limit for this task. Allowed values
                 are 50M, 100M, 250M, 500M, 1G, 2G, or 5G. Default to unlimited if not provided.""")
@cli_util.option('--sync-on-create', type=bool, required=False,
                 help=u"""If present, the task will started right after its creation regardless if it's a scheduled task or not.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.wrap_exceptions
@cli_util.help_option
def create_task_definition(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    data = parse_definition_input(**kwargs)

    # make API call
    dispatch_datasync_request(ctx,
                              ROVER_DATASYNC_TASK_DEF_API_BASE_PATH,
                              http_method="POST",
                              data=data
                              )


@rover_datasync_task_definition_group.command(name="update", help=u"""Update TaskDefinition""")
@click.pass_context
@cli_util.option('--id', type=str, required=True,
                 help=u"""The ocid of the Task Definition to be updated.""")
@cli_util.option('--name', type=str, required=False, help=u"""Short description of the Task Definition""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, required=False,
                 help=u"""Provide the details about the source datastore in JSON structure either in-line or
                 via a local file, file://path-to/data-sync-source-json-file.""")
@cli_util.option('--destination', type=custom_types.CLI_COMPLEX_TYPE, required=False,
                 help=u"""Provide the details about the destination datastore in JSON structure either in-line or
                 via a local file, file://path-to/data-sync-destination-json-file.""")
@cli_util.option('--schedule', type=custom_types.CLI_COMPLEX_TYPE, required=False,
                 help=u"""Provide the details about how the task execution is scheduled in JSON structure either
                 in-line or via a local file, file://path-to/schedule-json-file.""")
@cli_util.option('--rate-limit', type=str, required=False,
                 help=u"""If provided, it sets the data transfer rate limit for this task. Allowed values
                 are 50M, 100M, 250M, 500M, 1G, 2G, or 5G. Default to unlimited if not provided.""")
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'source': {'module': 'rover', 'class': 'DataStore'},
        'destination': {'module': 'rover', 'class': 'DataStore'},
        'schedule': {'module': 'rover', 'class': 'DataSyncSchedule'}}
)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.wrap_exceptions
@cli_util.help_option
def update_task_definition(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    data = parse_definition_input(**kwargs)

    # make API call
    dispatch_datasync_request(ctx,
                              ROVER_DATASYNC_TASK_DEF_API_BASE_PATH,
                              additional_url_path=kwargs.get("id"),
                              http_method="PUT",
                              data=data
                              )


@rover_datasync_task_definition_group.command(name="get", help=u"""Get TaskDefinition""")
@cli_util.option('--id', type=str, required=True,
                 help=u"""Get the Task Definition specified by its ocid.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_task_definition(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    dispatch_datasync_request(ctx,
                              ROVER_DATASYNC_TASK_DEF_API_BASE_PATH,
                              additional_url_path=kwargs.get("id"),
                              http_method="GET",
                              )


@rover_datasync_task_definition_group.command(name="list", help=u"""List TaskDefinitions""")
@cli_util.option('--limit', type=int, required=False,
                 help=u"""Specify the number of task definitions to be retrieved. Default to 10 if not provided.""")
@cli_util.option('--page', type=str, required=False,
                 help=u"""If provided, this specifies the ocid of the first task definition returned in the list.
                 This Id is returned along with the list if there are more items to fetch.""")
@cli_util.option('--sort-by', type=str, required=False,
                 help=u"""One of the supported sort-by columns: name | timeCreated | sourceDataStore | sourceBucket | destinationBucket.""")
@cli_util.option('--sort-order', type=str, required=False,
                 help=u"""Specifies how the returned list is sorted, ASC | DESC. The default sort is ASC and it's always on creation time.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def list_task_definitions(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    limit = kwargs.get("limit")
    if limit is None or limit == 0:
        limit = 10

    next_page = None
    page = kwargs.get("page")

    # sort by column
    sort_by = kwargs.get("sort_by")
    if sort_by is None:
        sort_by = 'timeCreated'

    # sort order
    reverse = False
    sort_order = kwargs.get("sort_order")
    if sort_order and sort_order.upper() == 'DESC':
        reverse = True

    # get all 10 items
    all_items = dispatch_datasync_request(ctx,
                                          ROVER_DATASYNC_TASK_DEF_API_BASE_PATH,
                                          http_method="GET",
                                          print_response=False
                                          )

    # OTEC-18416: do local sorting in mem and pagination
    sort_by_lower = sort_by.lower()
    if sort_by_lower == 'name':
        sorted_list = sorted(all_items, key=lambda x: x[sort_by], reverse=reverse)
    elif sort_by_lower == 'timeCreated'.lower():
        sorted_list = sorted(all_items, key=lambda x: x[sort_by], reverse=reverse)
    elif sort_by_lower == 'sourceDataStore'.lower():
        sorted_list = sorted(all_items, key=lambda x: x['dataSyncSource']['dataStore'], reverse=reverse)
    elif sort_by_lower == 'sourceBucket'.lower():
        sorted_list = sorted(all_items, key=lambda x: x['dataSyncSource']['bucketName'], reverse=reverse)
    elif sort_by_lower == 'destinationBucket'.lower():
        sorted_list = sorted(all_items, key=lambda x: x['dataSyncDestination']['bucketName'], reverse=reverse)
    else:
        raise Exception(f"Unknown short-by column: {sort_by}")

    # create paged list to return
    paged_list = []
    item_count = 0
    found_matched_item = False
    for item in sorted_list:
        if not found_matched_item and page is not None:
            if item['id'] == page:
                found_matched_item = True
            else:
                continue

        item_count += 1
        if item_count > limit:
            next_page = item['id']
            item_count -= 1
            break

        paged_list.append(item)

    # create JSON object to print
    data = {}
    data['data'] = paged_list
    data['opc-next-page'] = next_page
    data['opc-total-items'] = item_count

    print(f"\n{json.dumps(data, indent=2)}")


@rover_datasync_task_definition_group.command(name="delete", help=u"""Delete TaskDefinition""")
@cli_util.option('--id', type=str, required=True,
                 help=u"""Delete the Task Definition specified by its ocid.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_task_definition(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    dispatch_datasync_request(ctx,
                              ROVER_DATASYNC_TASK_DEF_API_BASE_PATH,
                              additional_url_path=kwargs.get("id"),
                              http_method="DELETE",
                              )
