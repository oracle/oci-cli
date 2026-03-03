# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

# Packaged here are all data-sync CLI related functions
import click
import json
import time
import oci
from oci_cli import cli_util, json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias
from services.rover.src.oci_cli_rover.rover_utils import dispatch_datasync_request

RESOURCE_TYPE = "TASK"


@click.command('task', cls=CommandGroupWithAlias, help="""Data Sync Task Execution.""")
@cli_util.help_option_group
def rover_datasync_task_group():
    pass


@rover_datasync_task_group.command(name="start", help=u"""Start Task""")
@click.pass_context
@cli_util.option('--task-definition-id', type=str, required=True,
                 help=u"""The OCID of the Task Definition that is to be executed.""")
@cli_util.option('--threads', type=int, required=False,
                 help=u"""Number of threads to copy files concurrently. Default to 1.""")
@cli_util.option('--multipart-threads', type=int, required=False,
                 help=u"""Number of threads to process multiparts per file. Default to 1.""")
@cli_util.option('--edge-type', type=str, required=False,
                 help=u"""If provided, it sets the target path to either a Rover RED or PCA device. (red/pca)""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, expose_value=True,
              callback=json_skeleton_utils.generate_json_skeleton_click_callback,
              help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
@cli_util.help_option
def start_task(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    threads = kwargs.get("threads")
    if threads is None or threads < 1:
        threads = 1

    multipart_threads = kwargs.get("multipart_threads")
    if multipart_threads is None or multipart_threads < 1:
        multipart_threads = 1

    start_task_details = {
        "taskDefinitionId": kwargs.get("task_definition_id"),
        "numThreads": threads,
        "numMultipartThreads": multipart_threads
    }

    edge_type = "red" if kwargs.get("edge_type") is None else kwargs.get("edge_type")

    dispatch_datasync_request(ctx,
                              RESOURCE_TYPE,
                              edge_type=edge_type,
                              http_method="POST",
                              data=start_task_details
                              )


@rover_datasync_task_group.command(name="list", help=u"""List Task""")
@click.pass_context
@cli_util.option('--task-definition-id', type=str, required=True,
                 help=u"""Get the Task list executed from Task Definition specified by its ocid.""")
@cli_util.option('--limit', type=int, required=False,
                 help=u"""Specify the number of tasks to be retrieved. Default to 10 if not provided.""")
@cli_util.option('--page', type=str, required=False,
                 help=u"""If provided, this specifies the ocid of the first task returned in the list.
                 This Id is returned along with the list if there are more items to fetch.""")
@cli_util.option('--sort-order', type=str, required=False,
                 help=u"""Specifies how the returned list is sorted, ASC | DESC. The default sort is ASC and it's always on start time.""")
@cli_util.option('--edge-type', type=str, required=False,
                 help=u"""If provided, it sets the target path to either a Rover RED or PCA device. (red/pca)""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, expose_value=True,
              callback=json_skeleton_utils.generate_json_skeleton_click_callback,
              help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
@cli_util.help_option
def list_tasks(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    # get all tasks by not passing "limit" and "page"
    params = {"taskDefinitionId": kwargs.get("task_definition_id")}

    limit = kwargs.get("limit")
    if limit is None or limit == 0:
        limit = 10

    next_page = None
    page = kwargs.get("page")

    # sort order
    reverse = False
    sort_order = kwargs.get("sort_order")
    if sort_order and sort_order.upper() == 'DESC':
        reverse = True

    edge_type = "red" if kwargs.get("edge_type") is None else kwargs.get("edge_type")

    # get all 10 items
    all_items = dispatch_datasync_request(ctx,
                                          RESOURCE_TYPE,
                                          edge_type=edge_type,
                                          http_method="GET",
                                          params=params,
                                          print_response=False
                                          )

    # OTEC-18415: do local sorting in mem and pagination
    sorted_list = sorted(all_items, key=lambda x: x['startTime'], reverse=reverse)

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


@rover_datasync_task_group.command(name="get", help=u"""Get/Monitor task execution progress""")
@click.pass_context
@cli_util.option('--task-id', type=str, required=True, help=u"""Task ocid.""")
@cli_util.option('--no-wait', type=bool, required=False,
                 help=u"""By default, this command monitors the task execution progress continuously till the task
                 completes.""")
@cli_util.option('--edge-type', type=str, required=False,
                 help=u"""If provided, it sets the target path to either a Rover RED or PCA device. (red/pca)""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, expose_value=True,
              callback=json_skeleton_utils.generate_json_skeleton_click_callback,
              help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
@cli_util.help_option
def get_task(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    params = {"taskId": kwargs.get("task_id")}
    continue_monitor = not kwargs.get("no_wait")
    edge_type = "red" if kwargs.get("edge_type") is None else kwargs.get("edge_type")

    # note ctx cannot be passed in recursion
    # add logic to determine query and path param
    while continue_monitor:
        if edge_type == "pca":
            response = dispatch_datasync_request(ctx,
                                                 RESOURCE_TYPE,
                                                 edge_type=edge_type,
                                                 http_method="GET",
                                                 additional_url_path=kwargs.get("task_id"),
                                                 print_response=False
                                                 )
        else:
            response = dispatch_datasync_request(ctx,
                                                 RESOURCE_TYPE,
                                                 edge_type=edge_type,
                                                 http_method="GET",
                                                 params=params,
                                                 print_response=False
                                                 )

        if response:
            status = response[0]['status']

            completion_status = status['completionStatus']
            progress = status['progress']
            summary = status['summary']

            # display progress
            display_progress(progress, completion_status)

            if status['completionStatus']['lifecycleState'] in ['WAITING_TO_START', 'RUNNING']:
                # continue monitoring every 20 seconds
                sleep_sec = 20
                print(f"Auto refresh in {sleep_sec} sec...")
                time.sleep(sleep_sec)
            else:
                # display completionStatus and summary
                display_summary(summary, completion_status)
                break


@rover_datasync_task_group.command(name="get-snapshot",
                                   help=u"""Get task snapshot - the snapshot of the Task Definition at the time of
                                   execution and the execution status""")
@click.pass_context
@cli_util.option('--task-id', type=str, required=True, help=u"""Task ocid.""")
@cli_util.option('--edge-type', type=str, required=False,
                 help=u"""If provided, it sets the target path to either a Rover RED or PCA device. (red/pca)""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, expose_value=True,
              callback=json_skeleton_utils.generate_json_skeleton_click_callback,
              help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
@cli_util.help_option
def get_task_snapshot(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    params = {"taskId": kwargs.get("task_id")}
    edge_type = "red" if kwargs.get("edge_type") is None else kwargs.get("edge_type")

    dispatch_datasync_request(ctx,
                              RESOURCE_TYPE,
                              edge_type=edge_type,
                              http_method="GET",
                              params=params
                              )


@rover_datasync_task_group.command(name="cancel", help=u"""Cancel Task""")
@click.pass_context
@cli_util.option('--task-id', type=str, required=True,
                 help=u"""Cancel a running Task by its ocid.""")
@cli_util.option('--edge-type', type=str, required=False,
                 help=u"""If provided, it sets the target path to either a Rover RED or PCA device. (red/pca)""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, expose_value=True,
              callback=json_skeleton_utils.generate_json_skeleton_click_callback,
              help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")
@json_skeleton_utils.json_skeleton_generation_handler()
@cli_util.wrap_exceptions
@cli_util.help_option
def cancel_task(ctx, **kwargs):
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    ctx.obj['config'] = config

    edge_type = "red" if kwargs.get("edge_type") is None else kwargs.get("edge_type")

    dispatch_datasync_request(ctx,
                              RESOURCE_TYPE,
                              edge_type=edge_type,
                              additional_url_path=kwargs.get("task_id"),
                              http_method="DELETE"
                              )


def display_progress(progress, completion_status):
    # column length, excluding "|", is 14 for every one
    total_count = progress['numFilesToSync']
    bytes_to_sync = progress['bytesToSync']
    bytes_sync_synced = progress['bytesSynced']
    progress_percentage = int(100 * bytes_sync_synced / bytes_to_sync)
    throughput = progress['syncThroughput']

    copied = 0
    prev_copied = 0
    failed = 0

    end_time = get_end_time(completion_status)

    time_elapsed = int((end_time - completion_status['startTimeInMs']) / 1000.0)

    for stats_per_state in progress['statsPerStateList']:
        if stats_per_state['state'] == 'COMPLETED':
            copied = stats_per_state['numFiles']
        elif stats_per_state['state'] == 'PREV_COPIED':
            prev_copied = stats_per_state['numFiles']
        elif stats_per_state['state'] == 'FAILED':
            failed = stats_per_state['numFiles']

    first_row = '| {:^12s} | {:^12d} | {:^12d} | {:^12d} | {:^12d} | {:^12s} | {:^12d}'.format(
        convert_bytes(bytes_to_sync), total_count, copied, prev_copied, failed, convert_bytes(bytes_sync_synced), progress_percentage)
    second_row = '| {:<49s} | {:>50s}'.format(
        f"Time Elapsed: {time_elapsed} sec", f"Throughput: {convert_bytes(throughput)}ps")

    text = f"+--------------------------------------------------------------------------------------------------------+\n" \
           f"| Total Bytes  |  Total Count |    Copied    |  Prev Copied |    Failed    | Bytes Copied |  Progress %  |\n" \
           f"+--------------------------------------------------------------------------------------------------------+\n" \
           f"{first_row} |\n" \
           f"+--------------------------------------------------------------------------------------------------------+\n" \
           f"{second_row} |\n" \
           f"+--------------------------------------------------------------------------------------------------------+\n"

    print(f"\n{text}")


def get_end_time(completion_status):
    end_time = completion_status['endTimeInMs']
    if end_time is None or end_time == 0:
        end_time = round(time.time() * 1000)
    return end_time


def display_summary(summary, completion_status):
    text = f"Summary:\n" \
           f"\tFinal Status:   {completion_status['lifecycleState']}\n"

    # show the reason if the task failed
    if completion_status['lifecycleState'] == 'FAILED':
        text += f"\tFailure Reason: {completion_status['failureReason']}\n"

    # Summary is available only for certain completion state
    if summary:
        text += f"\tTotal Count:    {summary['totalCnt']}\n" \
                f"\tCopied Count:   {summary['copiedCnt']}\n" \
                f"\tFailed Count:   {summary['nameCollisionCnt'] + summary['errorCnt']}\n"
    print(text)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    step_unit = 1024

    for x in ['bytes', 'Kb', 'Mb', 'Gb', 'Tb']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit
