# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('data_flow.data_flow_root_group.command_name', 'data-flow'), cls=CommandGroupWithAlias, help=cli_util.override('data_flow.data_flow_root_group.help', """Use the Data Flow APIs to run any Apache Spark application at any scale without deploying or managing any infrastructure."""), short_help=cli_util.override('data_flow.data_flow_root_group.short_help', """Data Flow API"""))
@cli_util.help_option_group
def data_flow_root_group():
    pass


@click.command(cli_util.override('data_flow.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""A Data Flow work request log object.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('data_flow.application_group.command_name', 'application'), cls=CommandGroupWithAlias, help="""A Data Flow application object.""")
@cli_util.help_option_group
def application_group():
    pass


@click.command(cli_util.override('data_flow.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""A Data Flow work request error object.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('data_flow.private_endpoint_group.command_name', 'private-endpoint'), cls=CommandGroupWithAlias, help="""A Data Flow private endpoint object.""")
@cli_util.help_option_group
def private_endpoint_group():
    pass


@click.command(cli_util.override('data_flow.run_log_summary_group.command_name', 'run-log-summary'), cls=CommandGroupWithAlias, help="""A summary of a log associated with a particular run.""")
@cli_util.help_option_group
def run_log_summary_group():
    pass


@click.command(cli_util.override('data_flow.run_group.command_name', 'run'), cls=CommandGroupWithAlias, help="""A run object.""")
@cli_util.help_option_group
def run_group():
    pass


@click.command(cli_util.override('data_flow.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A Data Flow work request object.""")
@cli_util.help_option_group
def work_request_group():
    pass


data_flow_root_group.add_command(work_request_log_group)
data_flow_root_group.add_command(application_group)
data_flow_root_group.add_command(work_request_error_group)
data_flow_root_group.add_command(private_endpoint_group)
data_flow_root_group.add_command(run_log_summary_group)
data_flow_root_group.add_command(run_group)
data_flow_root_group.add_command(work_request_group)


@application_group.command(name=cli_util.override('data_flow.change_application_compartment.command_name', 'change-compartment'), help=u"""Moves an application into a different compartment. When provided, If-Match is checked against ETag values of the resource. Associated resources, like runs, will not be automatically moved.""")
@cli_util.option('--application-id', required=True, help=u"""The unique ID for an application.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_application_compartment(ctx, from_json, application_id, compartment_id, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.change_application_compartment(
        application_id=application_id,
        change_application_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_endpoint_group.command(name=cli_util.override('data_flow.change_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a private endpoint into a different compartment. When provided, If-Match is checked against ETag values of the resource.""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The unique ID for a private endpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELLED", "CANCELLING", "FAILED", "INPROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_endpoint_id, compartment_id, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.change_private_endpoint_compartment(
        private_endpoint_id=private_endpoint_id,
        change_private_endpoint_compartment_details=_details,
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


@run_group.command(name=cli_util.override('data_flow.change_run_compartment.command_name', 'change-compartment'), help=u"""Moves a run into a different compartment. When provided, If-Match is checked against ETag values of the resource. Associated resources, like historical metrics, will not be automatically moved. The run must be in a terminal state (CANCELED, FAILED, SUCCEEDED) in order for it to be moved to a different compartment""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_run_compartment(ctx, from_json, run_id, compartment_id, if_match):

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.change_run_compartment(
        run_id=run_id,
        change_run_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_flow.create_application.command_name', 'create'), help=u"""Creates an application.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--driver-shape', required=True, help=u"""The VM shape for the driver. Sets the driver cores and memory.""")
@cli_util.option('--executor-shape', required=True, help=u"""The VM shape for the executors. Sets the executor cores and memory.""")
@cli_util.option('--file-uri', required=True, help=u"""An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--language', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCALA", "JAVA", "PYTHON", "SQL"]), help=u"""The Spark language.""")
@cli_util.option('--num-executors', required=True, type=click.INT, help=u"""The number of executor VMs requested.""")
@cli_util.option('--spark-version', required=True, help=u"""The Spark version utilized to run the application.""")
@cli_util.option('--archive-uri', help=u"""An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The arguments passed to the running application as command line arguments.  An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map.  Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--class-name', help=u"""The class for the application.""")
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A user-friendly description. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--logs-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`.  The name must be a string of one or more word characters (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind. Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

This option is a JSON list with items of type ApplicationParameter.  For documentation on ApplicationParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataflow/20200129/datatypes/ApplicationParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint-id', help=u"""The OCID of a private endpoint.""")
@cli_util.option('--warehouse-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Application'})
@cli_util.wrap_exceptions
def create_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, driver_shape, executor_shape, file_uri, language, num_executors, spark_version, archive_uri, arguments, class_name, configuration, defined_tags, description, freeform_tags, logs_bucket_uri, parameters, private_endpoint_id, warehouse_bucket_uri):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['driverShape'] = driver_shape
    _details['executorShape'] = executor_shape
    _details['fileUri'] = file_uri
    _details['language'] = language
    _details['numExecutors'] = num_executors
    _details['sparkVersion'] = spark_version

    if archive_uri is not None:
        _details['archiveUri'] = archive_uri

    if arguments is not None:
        _details['arguments'] = cli_util.parse_json_parameter("arguments", arguments)

    if class_name is not None:
        _details['className'] = class_name

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if logs_bucket_uri is not None:
        _details['logsBucketUri'] = logs_bucket_uri

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if warehouse_bucket_uri is not None:
        _details['warehouseBucketUri'] = warehouse_bucket_uri

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.create_application(
        create_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_application(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('data_flow.create_private_endpoint.command_name', 'create'), help=u"""Creates a private endpoint to be used by an application.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--dns-zones', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of a subnet.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A user-friendly description. Avoid entering confidential information.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-host-count', type=click.INT, help=u"""The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security group OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELLED", "CANCELLING", "FAILED", "INPROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'dns-zones': {'module': 'data_flow', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'data_flow', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'dns-zones': {'module': 'data_flow', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'data_flow', 'class': 'list[string]'}}, output_type={'module': 'data_flow', 'class': 'PrivateEndpoint'})
@cli_util.wrap_exceptions
def create_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, dns_zones, subnet_id, defined_tags, description, display_name, freeform_tags, max_host_count, nsg_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)
    _details['subnetId'] = subnet_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if max_host_count is not None:
        _details['maxHostCount'] = max_host_count

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.create_private_endpoint(
        create_private_endpoint_details=_details,
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


@run_group.command(name=cli_util.override('data_flow.create_run.command_name', 'create'), help=u"""Creates a run for an application.""")
@cli_util.option('--application-id', required=True, help=u"""The application ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of a compartment.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. It does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The arguments passed to the running application as command line arguments.  An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map.  Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--driver-shape', help=u"""The VM shape for the driver. Sets the driver cores and memory.""")
@cli_util.option('--executor-shape', help=u"""The VM shape for the executors. Sets the executor cores and memory.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--logs-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--num-executors', type=click.INT, help=u"""The number of executor VMs requested.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`.  The name must be a string of one or more word characters (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind. Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

This option is a JSON list with items of type ApplicationParameter.  For documentation on ApplicationParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataflow/20200129/datatypes/ApplicationParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--warehouse-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Run'})
@cli_util.wrap_exceptions
def create_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, application_id, compartment_id, display_name, arguments, configuration, defined_tags, driver_shape, executor_shape, freeform_tags, logs_bucket_uri, num_executors, parameters, warehouse_bucket_uri):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['applicationId'] = application_id
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name

    if arguments is not None:
        _details['arguments'] = cli_util.parse_json_parameter("arguments", arguments)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if driver_shape is not None:
        _details['driverShape'] = driver_shape

    if executor_shape is not None:
        _details['executorShape'] = executor_shape

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if logs_bucket_uri is not None:
        _details['logsBucketUri'] = logs_bucket_uri

    if num_executors is not None:
        _details['numExecutors'] = num_executors

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if warehouse_bucket_uri is not None:
        _details['warehouseBucketUri'] = warehouse_bucket_uri

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.create_run(
        create_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_run') and callable(getattr(client, 'get_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@application_group.command(name=cli_util.override('data_flow.delete_application.command_name', 'delete'), help=u"""Deletes an application using an `applicationId`.""")
@cli_util.option('--application-id', required=True, help=u"""The unique ID for an application.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_application(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, application_id, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.delete_application(
        application_id=application_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_application(application_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('data_flow.delete_private_endpoint.command_name', 'delete'), help=u"""Deletes a private endpoint using a `privateEndpointId`.""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The unique ID for a private endpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELLED", "CANCELLING", "FAILED", "INPROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, private_endpoint_id, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.delete_private_endpoint(
        private_endpoint_id=private_endpoint_id,
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


@run_group.command(name=cli_util.override('data_flow.delete_run.command_name', 'delete'), help=u"""Cancels the specified run if it has not already completed or was previously cancelled. If a run is in progress, the executing job will be killed.""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_run(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, run_id, if_match):

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.delete_run(
        run_id=run_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_run') and callable(getattr(client, 'get_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_run(run_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@application_group.command(name=cli_util.override('data_flow.get_application.command_name', 'get'), help=u"""Retrieves an application using an `applicationId`.""")
@cli_util.option('--application-id', required=True, help=u"""The unique ID for an application.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'Application'})
@cli_util.wrap_exceptions
def get_application(ctx, from_json, application_id):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.get_application(
        application_id=application_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@private_endpoint_group.command(name=cli_util.override('data_flow.get_private_endpoint.command_name', 'get'), help=u"""Retrieves an private endpoint using a `privateEndpointId`.""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The unique ID for a private endpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'PrivateEndpoint'})
@cli_util.wrap_exceptions
def get_private_endpoint(ctx, from_json, private_endpoint_id):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.get_private_endpoint(
        private_endpoint_id=private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@run_group.command(name=cli_util.override('data_flow.get_run.command_name', 'get'), help=u"""Retrieves the run for the specified `runId`.""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'Run'})
@cli_util.wrap_exceptions
def get_run(ctx, from_json, run_id):

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.get_run(
        run_id=run_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@run_group.command(name=cli_util.override('data_flow.get_run_log.command_name', 'get-run-log'), help=u"""Retrieves the content of an run log.""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@cli_util.option('--name', required=True, help=u"""The name of the log. Avoid entering confidential information.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_run_log(ctx, from_json, file, run_id, name):

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')

    if isinstance(name, six.string_types) and len(name.strip()) == 0:
        raise click.UsageError('Parameter --name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.get_run_log(
        run_id=run_id,
        name=name,
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


@work_request_group.command(name=cli_util.override('data_flow.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given OCID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique ID for a work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_flow.list_applications.command_name', 'list'), help=u"""Lists all applications in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "language"]), help=u"""The field used to sort the results. Multiple fields are not supported.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The ordering of results in ascending or descending order.""")
@cli_util.option('--display-name', help=u"""The query parameter for the Spark application name.""")
@cli_util.option('--owner-principal-id', help=u"""The OCID of the user who created the resource.""")
@cli_util.option('--display-name-starts-with', help=u"""The displayName prefix.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'list[ApplicationSummary]'})
@cli_util.wrap_exceptions
def list_applications(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, display_name, owner_principal_id, display_name_starts_with):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
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
    if owner_principal_id is not None:
        kwargs['owner_principal_id'] = owner_principal_id
    if display_name_starts_with is not None:
        kwargs['display_name_starts_with'] = display_name_starts_with
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_applications,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_applications,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_applications(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@private_endpoint_group.command(name=cli_util.override('data_flow.list_private_endpoints.command_name', 'list'), help=u"""Lists all private endpoints in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""The LifecycleState of the private endpoint.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated"]), help=u"""The field used to sort the results. Multiple fields are not supported.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The ordering of results in ascending or descending order.""")
@cli_util.option('--display-name', help=u"""The query parameter for the Spark application name.""")
@cli_util.option('--owner-principal-id', help=u"""The OCID of the user who created the resource.""")
@cli_util.option('--display-name-starts-with', help=u"""The displayName prefix.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'PrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, limit, page, lifecycle_state, sort_by, sort_order, display_name, owner_principal_id, display_name_starts_with):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if owner_principal_id is not None:
        kwargs['owner_principal_id'] = owner_principal_id
    if display_name_starts_with is not None:
        kwargs['display_name_starts_with'] = display_name_starts_with
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@run_log_summary_group.command(name=cli_util.override('data_flow.list_run_logs.command_name', 'list-run-logs'), help=u"""Retrieves summaries of the run's logs.""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'list[RunLogSummary]'})
@cli_util.wrap_exceptions
def list_run_logs(ctx, from_json, all_pages, page_size, run_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_run_logs,
            run_id=run_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_run_logs,
            limit,
            page_size,
            run_id=run_id,
            **kwargs
        )
    else:
        result = client.list_run_logs(
            run_id=run_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@run_group.command(name=cli_util.override('data_flow.list_runs.command_name', 'list'), help=u"""Lists all runs of an application in the specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--application-id', help=u"""The ID of the application.""")
@cli_util.option('--owner-principal-id', help=u"""The OCID of the user who created the resource.""")
@cli_util.option('--display-name-starts-with', help=u"""The displayName prefix.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED"]), help=u"""The LifecycleState of the run.""")
@cli_util.option('--time-created-greater-than', type=custom_types.CLI_DATETIME, help=u"""The epoch time that the resource was created.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName", "language", "runDurationInMilliseconds", "lifecycleState", "totalOCpu", "dataReadInBytes", "dataWrittenInBytes"]), help=u"""The field used to sort the results. Multiple fields are not supported.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The ordering of results in ascending or descending order.""")
@cli_util.option('--display-name', help=u"""The query parameter for the Spark application name.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'list[RunSummary]'})
@cli_util.wrap_exceptions
def list_runs(ctx, from_json, all_pages, page_size, compartment_id, application_id, owner_principal_id, display_name_starts_with, lifecycle_state, time_created_greater_than, limit, page, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if application_id is not None:
        kwargs['application_id'] = application_id
    if owner_principal_id is not None:
        kwargs['owner_principal_id'] = owner_principal_id
    if display_name_starts_with is not None:
        kwargs['display_name_starts_with'] = display_name_starts_with
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than is not None:
        kwargs['time_created_greater_than'] = time_created_greater_than
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
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_runs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_runs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_runs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('data_flow.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique ID for a work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
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


@work_request_log_group.command(name=cli_util.override('data_flow.list_work_request_logs.command_name', 'list'), help=u"""Return a paginated list of logs for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique ID for a work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'WorkRequestLogCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
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


@work_request_group.command(name=cli_util.override('data_flow.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of results to return in a paginated `List` call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the last `List` call to sent back to server for getting the next page of results.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_flow', 'data_flow', ctx)
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


@application_group.command(name=cli_util.override('data_flow.update_application.command_name', 'update'), help=u"""Updates an application using an `applicationId`.""")
@cli_util.option('--application-id', required=True, help=u"""The unique ID for an application.""")
@cli_util.option('--class-name', help=u"""The class for the application.""")
@cli_util.option('--file-uri', help=u"""An Oracle Cloud Infrastructure URI of the file containing the application to execute. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--spark-version', help=u"""The Spark version utilized to run the application.""")
@cli_util.option('--language', type=custom_types.CliCaseInsensitiveChoice(["SCALA", "JAVA", "PYTHON", "SQL"]), help=u"""The Spark language.""")
@cli_util.option('--archive-uri', help=u"""An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python, Java, or Scala application. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--arguments', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The arguments passed to the running application as command line arguments.  An argument is either a plain text or a placeholder. Placeholders are replaced using values from the parameters map.  Each placeholder specified must be represented in the parameters map else the request (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as `Service Api Spec`, where `name` is the name of the parameter. Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]` If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties. Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" } Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A user-friendly description. Avoid entering confidential information.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--driver-shape', help=u"""The VM shape for the driver. Sets the driver cores and memory.""")
@cli_util.option('--executor-shape', help=u"""The VM shape for the executors. Sets the executor cores and memory.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--logs-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--num-executors', type=click.INT, help=u"""The number of executor VMs requested.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of name/value pairs used to fill placeholders found in properties like `Application.arguments`.  The name must be a string of one or more word characters (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind. Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]

This option is a JSON list with items of type ApplicationParameter.  For documentation on ApplicationParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataflow/20200129/datatypes/ApplicationParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint-id', help=u"""The OCID of a private endpoint.""")
@cli_util.option('--warehouse-bucket-uri', help=u"""An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory for BATCH SQL runs. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "INACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Application'})
@cli_util.wrap_exceptions
def update_application(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, application_id, class_name, file_uri, spark_version, language, archive_uri, arguments, configuration, defined_tags, description, display_name, driver_shape, executor_shape, freeform_tags, logs_bucket_uri, num_executors, parameters, private_endpoint_id, warehouse_bucket_uri, if_match):

    if isinstance(application_id, six.string_types) and len(application_id.strip()) == 0:
        raise click.UsageError('Parameter --application-id cannot be whitespace or empty string')
    if not force:
        if arguments or configuration or defined_tags or freeform_tags or parameters:
            if not click.confirm("WARNING: Updates to arguments and configuration and defined-tags and freeform-tags and parameters will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if class_name is not None:
        _details['className'] = class_name

    if file_uri is not None:
        _details['fileUri'] = file_uri

    if spark_version is not None:
        _details['sparkVersion'] = spark_version

    if language is not None:
        _details['language'] = language

    if archive_uri is not None:
        _details['archiveUri'] = archive_uri

    if arguments is not None:
        _details['arguments'] = cli_util.parse_json_parameter("arguments", arguments)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if driver_shape is not None:
        _details['driverShape'] = driver_shape

    if executor_shape is not None:
        _details['executorShape'] = executor_shape

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if logs_bucket_uri is not None:
        _details['logsBucketUri'] = logs_bucket_uri

    if num_executors is not None:
        _details['numExecutors'] = num_executors

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    if warehouse_bucket_uri is not None:
        _details['warehouseBucketUri'] = warehouse_bucket_uri

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.update_application(
        application_id=application_id,
        update_application_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_application') and callable(getattr(client, 'get_application')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_application(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@private_endpoint_group.command(name=cli_util.override('data_flow.update_private_endpoint.command_name', 'update'), help=u"""Updates a private endpoint using a `privateEndpointId`.  If changes to a private endpoint match a previously defined private endpoint, then a 409 status code will be returned.  This indicates that a conflict has been detected.""")
@cli_util.option('--private-endpoint-id', required=True, help=u"""The unique ID for a private endpoint.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A user-friendly description. Avoid entering confidential information.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. It does not have to be unique. Avoid entering confidential information.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of DNS zone names. Example: `[ \"app.examplecorp.com\", \"app.examplecorp2.com\" ]`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-host-count', type=click.INT, help=u"""The maximum number of hosts to be accessed through the private endpoint. This value is used to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up to 512.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security group OCIDs.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "CANCELLED", "CANCELLING", "FAILED", "INPROGRESS", "SUCCEEDED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'dns-zones': {'module': 'data_flow', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'data_flow', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'dns-zones': {'module': 'data_flow', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'data_flow', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, private_endpoint_id, defined_tags, description, display_name, dns_zones, freeform_tags, max_host_count, nsg_ids, if_match):

    if isinstance(private_endpoint_id, six.string_types) and len(private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or dns_zones or freeform_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to defined-tags and dns-zones and freeform-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if max_host_count is not None:
        _details['maxHostCount'] = max_host_count

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.update_private_endpoint(
        private_endpoint_id=private_endpoint_id,
        update_private_endpoint_details=_details,
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


@run_group.command(name=cli_util.override('data_flow.update_run.command_name', 'update'), help=u"""Updates a run using a `runId`.""")
@cli_util.option('--run-id', required=True, help=u"""The unique ID for the run""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "CANCELING", "CANCELED", "FAILED", "SUCCEEDED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}}, output_type={'module': 'data_flow', 'class': 'Run'})
@cli_util.wrap_exceptions
def update_run(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, run_id, defined_tags, freeform_tags, if_match):

    if isinstance(run_id, six.string_types) and len(run_id.strip()) == 0:
        raise click.UsageError('Parameter --run-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('data_flow', 'data_flow', ctx)
    result = client.update_run(
        run_id=run_id,
        update_run_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_run') and callable(getattr(client, 'get_run')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_run(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
