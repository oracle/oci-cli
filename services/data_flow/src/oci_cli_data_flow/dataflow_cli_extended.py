# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import re
import json
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.data_flow.src.oci_cli_data_flow.generated import dataflow_cli

# Rename "oci data-flow run get-run-log --file, --name, --run-id"
# to     "oci data-flow run get-log     --file, --name, --run-id"
cli_util.rename_command(dataflow_cli, dataflow_cli.run_group, dataflow_cli.get_run_log, "get-log")

# Rename "oci data-flow run-log-summary list-run-logs --run-id, --all-pages"
# to     "oci data-flow run             list-logs     --run-id"
# Step #1. Rename "list-run-logs" to "list-logs"
cli_util.rename_command(dataflow_cli, dataflow_cli.run_log_summary_group, dataflow_cli.list_run_logs, "list-logs")

# Step #2. Remove the "list-run-log" command from the "run-log-summary" group and add it to the "run" group
dataflow_cli.run_log_summary_group.commands.pop(dataflow_cli.list_run_logs.name)
dataflow_cli.run_group.add_command(dataflow_cli.list_run_logs)

# Step #3. Remove the "run_log_summary_group" group
dataflow_cli.data_flow_root_group.commands.pop(dataflow_cli.run_log_summary_group.name)


# Step #4. Remove "--all-pages" (and all paging-related options) because the list has a maximimum of 5 items
@cli_util.copy_params_from_generated_command(dataflow_cli.list_run_logs, params_to_exclude=['limit', 'page', 'all', 'all_pages', 'page_size'])
@dataflow_cli.run_group.command(name=cli_util.override('data_flow.list_logs.command_name', 'list-logs'), help=dataflow_cli.list_run_logs.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_flow', 'class': 'list[ConsumptionSummary]'})
@cli_util.wrap_exceptions
def list_run_logs(ctx, **kwargs):
    ctx.invoke(dataflow_cli.list_run_logs, **kwargs)


# convert a string into a json array by splitting the string by spaces and preserving quoted substrings
# eg.: "--input ${input} --output ${output} 10 'This is one arg'" -> ["--input", "${input}", "--output", "${output}", "10", "This is one arg"]
def convertArgumentStringToJson(s):
    # split the string by spaces - preserving single or double quoted substrings
    # eg: This is "a "test" -> ['This', 'is', '"a test"']
    # or: This is "a 'test' -> ['This', 'is', "'a test'"]
    args = [arg for arg in re.split("( |\\\".*?\\\"|'.*?')", str(s)) if arg.strip()]

    # strip the quotation marks from the args
    # ['This', 'is', '"a test"'] -> ['This', 'is', 'a test']
    # ['This', 'is', "'a test'"] -> ['This', 'is', 'a test']
    args = [arg.strip("'").strip('"') for arg in args]

    return json.dumps(args, sort_keys=True)


# convert a string of name=value pairs into a json array of { name: "...", value: "..."} objects
# eg.: "input='~/myInput.txt' output='~/myOutput.txt'" ->  [{"name": "input", "value": "~/myInput.txt"}, {"name": "output", "value": "~/myOutput.txt"}]
def convertParameterStringToJson(s):
    # split the string by spaces and equal signs - preserving single or double quoted substrings
    # eg: This is "a "test" -> ['This', 'is', '"a test"']
    # or: This is "a 'test' -> ['This', 'is', "'a test'"]
    args = [arg for arg in re.split("( |=|\\\".*?\\\"|'.*?')", str(s)) if arg.strip()]

    # strip the spaces and quotation marks from the args
    # ['This', 'is', '"a test"'] -> ['This', 'is', 'a test']
    # ['This', 'is', "'a test'"] -> ['This', 'is', 'a test']
    args = [arg.strip().strip("'").strip('"') for arg in args]

    paramsErrorMessage = "Incorrect 'parameters' value, cannot proceed. Parameters should be either in a plain text format of 'param_name_1=value_1 param_name_2=value_2 ...' or a json format of '[ { \"name\": \"param_name_1\", \"value\": \"value_1\"}, { \"name\": \"param_name_2\", \"value\": \"value_2\"}, ...]'"

    # check if there are even numer of tokens
    if (len(args) % 3 != 0):
        raise Exception(paramsErrorMessage)

    paramArray = []
    for i, token in enumerate(args):
        if (i % 3 == 0):
            data = {}
            data['name'] = token
        elif (i % 3 == 1):
            if token != "=":
                raise Exception(paramsErrorMessage)
        else:
            data['value'] = token
            paramArray.append(data)

    return json.dumps(paramArray, sort_keys=True)


# convert a string of name=value pairs into a json object (where each name will becaome a field of the object)
# eg.: 'spark.app.name="My App Name" spark.shuffle.io.maxRetries=4' -> '{ "spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4" }
def convertConfigurationStringToJson(s):
    # split the string by spaces and equal signs - preserving single or double quoted substrings
    # eg: This is "a "test" -> ['This', 'is', '"a test"']
    # or: This is "a 'test' -> ['This', 'is', "'a test'"]
    args = [arg for arg in re.split("( |=|\\\".*?\\\"|'.*?')", str(s)) if arg.strip()]

    # strip the quotation marks from the args
    # ['This', 'is', '"a test"'] -> ['This', 'is', 'a test']
    # ['This', 'is', "'a test'"] -> ['This', 'is', 'a test']
    args = [arg.strip("'").strip('"') for arg in args]

    configErrorMessage = "Incorrect 'configuration' value, cannot proceed. Configuration should be either in a plain text format of 'param_name_1=value_1 param_name_2=value_2 ...' or a json format of '{ \"param_name_1\": \"value_1\", \"param_name_2\": \"value_2\", }, ...'"

    # check if there are even numer of tokens
    if (len(args) % 3 != 0):
        raise Exception(configErrorMessage)

    obj = {}
    for i, token in enumerate(args):
        if (i % 3 == 0):
            fieldName = token
        elif (i % 3 == 1):
            if token != "=":
                raise Exception(configErrorMessage)
        else:
            obj[fieldName] = token

    return json.dumps(obj, sort_keys=True)


# Modify the the 'arguments', 'parameters' and 'configuration' command line params if needed.
# If these parameters are supplied as a simple string instead of a complex json, this function converts the string into the appropriate json format
# If the parameters are supplied in json format, they are returned unchanged.
# For example, for parameters:
#  'input="~/myInput.txt" output="~/myOutput.txt"'  ->  '[{"name": "input", "value": "~/myInput.txt"}, {"name": "output", "value": "~/myOutput.txt"}]'
# For arguments:
#   '--input ${input} --output ${output} 10 "This is one arg"'  -> '["--input", "${input}", "--output", "${output}", "10", "This is one arg"]'
# For configuration:
#   'spark.app.name="My App Name" spark.shuffle.io.maxRetries=4' -> '{"spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4"}'
# See SSS-2321 (https://jira.oci.oraclecorp.com/browse/SSS-2321)
def updateKwargs(kwargs):
    # Convert the "arguments" param from string to json if needed
    if 'arguments' in kwargs and kwargs['arguments']:
        arguments = kwargs['arguments']
        if not (arguments[0] == "[" and arguments[len(arguments) - 1] == "]"):
            kwargs['arguments'] = convertArgumentStringToJson(arguments)

    # Convert the "parameters" param from string to json if needed
    if 'parameters' in kwargs and kwargs['parameters']:
        parameters = kwargs['parameters']
        if not (parameters[0] == "[" and parameters[len(parameters) - 1] == "]"):
            kwargs['parameters'] = convertParameterStringToJson(parameters)

    # Convert the "configuration" parameter from string to json if needed
    if 'configuration' in kwargs and kwargs['configuration']:
        configuration = kwargs['configuration']
        if not (configuration[0] == "{" and configuration[len(configuration) - 1] == "}"):
            kwargs['configuration'] = convertConfigurationStringToJson(configuration)


# Modify the create_application command to accept the 'arguments', 'parameters' and 'configuration' params as a simple string as well as a json array.
# Paremeters can be in either of the following formats:
#   - a plaint text, eg:    'input="~/myInput.txt" output="~/myOutput.txt"'
#   - or a json array, eg:  '[{"name": "input", "value": "~/myInput.txt"}, {"name": "output", "value": "~/myOutput.txt"}]'
# Arguments can be in either of the following formats:
#   - a plaint text, eg.:    '--input ${input} --output ${output} 10 "This is one arg"'
#   - or a json array, eg.:  '["--input", "${input}", "--output", "${output}", "10", "This is one arg"]'
# Configuration can be in either of the following formats:
#   - a plaint text, eg.:    'spark.app.name="My App Name" spark.shuffle.io.maxRetries=4'
#   - or a json object, eg.: '{"spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4"}'
# See SSS-2321 (https://jira.oci.oraclecorp.com/browse/SSS-2321)
@cli_util.copy_params_from_generated_command(dataflow_cli.create_application, params_to_exclude=['arguments', 'parameters', 'configuration', 'execute'])
@dataflow_cli.application_group.command(name=cli_util.override('data_flow.create_application.command_name', 'create'), help=dataflow_cli.create_application.help)
@cli_util.option('--arguments', help=u"""The arguments passed to the running application as command line arguments. Arguments may contain zero or more placeholders that are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request will fail with a HTTP 400 status code. Placeholders are specified as `${name}`, where `name` is the name of the parameter. Example:  '--input ${input_file} --name \"John Doe\"'  Alternatively, the arguments can be specified as a JSON array of strings where each string represent an argument. Example:  [ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]  If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`""")
@cli_util.option('--parameters', help=u"""A string of name=value pairs used to supply SQL parameters or fill placeholders found in the arguments parameter. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of zero or more characters of any kind. Example:  'iterations=10 input_file=mydata.xml variable_x=${x}'  Alternatively, the arguments can be specified as a JSON array of objects. Example:  [ { name : \"iterations\", value : \"10\" }, { name : \"input_file\", value : \"mydata.xml\" }, { name : \"variable_x\", value : \"${x}\" } ]""")
@cli_util.option('--configuration', help=u"""The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties Example: 'spark.app.name=\"My App Name\" spark.shuffle.io.maxRetries=4'  Alternatively, the configuration can be specified as a JSON objects. Example:  { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }  Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'driver-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'executor-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Application'})
@cli_util.wrap_exceptions
def create_application(ctx, **kwargs):
    updateKwargs(kwargs)
    ctx.invoke(dataflow_cli.create_application, **kwargs)


# Modify the update_application command to accept the 'arguments', 'parameters' and 'configuration' params as a simple string as well as a json array.
# Paremeters can be in either of the following formats:
#   - a plaint text, eg:    'input="~/myInput.txt" output="~/myOutput.txt"'
#   - or a json array, eg:  '[{"name": "input", "value": "~/myInput.txt"}, {"name": "output", "value": "~/myOutput.txt"}]'
# Arguments can be in either of the following formats:
#   - a plaint text, eg.:    '--input ${input} --output ${output} 10 "This is one arg"'
#   - or a json array, eg.:  '["--input", "${input}", "--output", "${output}", "10", "This is one arg"]'
# Configuration can be in either of the following formats:
#   - a plaint text, eg.:    'spark.app.name="My App Name" spark.shuffle.io.maxRetries=4'
#   - or a json object, eg.: '{"spark.app.name": "My App Name", "spark.shuffle.io.maxRetries": "4"}'
# See SSS-2321 (https://jira.oci.oraclecorp.com/browse/SSS-2321)
@cli_util.copy_params_from_generated_command(dataflow_cli.update_application, params_to_exclude=['arguments', 'parameters', 'configuration', 'execute'])
@dataflow_cli.application_group.command(name=cli_util.override('data_flow.update_application.command_name', 'update'), help=dataflow_cli.update_application.help)
@cli_util.option('--arguments', help=u"""The arguments passed to the running application as command line arguments. Arguments may contain zero or more placeholders that are replaced using values from the parameters map. Each placeholder specified must be represented in the parameters map else the request will fail with a HTTP 400 status code. Placeholders are specified as `${name}`, where `name` is the name of the parameter. Example:  '--input ${input_file} --name \"John Doe\"'  Alternatively, the arguments can be specified as a JSON array of strings where each string represent an argument. Example:  [ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]  If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to `--input mydata.xml --name \"John Doe\"`""")
@cli_util.option('--parameters', help=u"""A string of name=value pairs used to supply SQL parameters or fill placeholders found in the arguments parameter. The name must be a string of one or more word characters (a-z, A-Z, 0-9, _). The value can be a string of zero or more characters of any kind. Example:  'iterations=10 input_file=mydata.xml variable_x=${x}'  Alternatively, the arguments can be specified as a JSON array of objects. Example:  [ { name : \"iterations\", value : \"10\" }, { name : \"input_file\", value : \"mydata.xml\" }, { name : \"variable_x\", value : \"${x}\" } ]""")
@cli_util.option('--configuration', help=u"""The Spark configuration passed to the running process. See https://spark.apache.org/docs/latest/configuration.html#available-properties Example: 'spark.app.name=\"My App Name\" spark.shuffle.io.maxRetries=4'  Alternatively, the configuration can be specified as a JSON objects. Example:  { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }  Note: Not all Spark properties are permitted to be set. Attempting to set a property that is not allowed to be overwritten will cause a 400 status to be returned.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'driver-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'executor-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Application'})
@cli_util.wrap_exceptions
def update_application(ctx, **kwargs):
    updateKwargs(kwargs)
    ctx.invoke(dataflow_cli.update_application, **kwargs)


# Add command submit to run group, using create command with --execute input, which is compatible with spark-submit syntax
# See https://jira.oci.oraclecorp.com/browse/SSS-3694
@cli_util.copy_params_from_generated_command(dataflow_cli.create_run, params_to_exclude=['execute', 'application_id', 'arguments', 'parameters'])
@dataflow_cli.run_group.command(name=cli_util.override('data_flow.submit_run.command_name', 'submit'), help=u"""Submit a run using spark-submit like syntax""")
@cli_util.option('--execute', required=True, help=u"""The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit. Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments. Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10`` Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit, Data Flow service will use derived information from execute input only.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'driver-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'executor-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Run'})
@cli_util.wrap_exceptions
def submit_run(ctx, **kwargs):
    updateKwargs(kwargs)
    ctx.invoke(dataflow_cli.create_run, **kwargs)


# For normal run create, application-id and display-name are required, execute is excluded.
@cli_util.copy_params_from_generated_command(dataflow_cli.create_run, params_to_exclude=['execute', 'application_id', 'display_name', 'archive_uri'])
@dataflow_cli.run_group.command(name=cli_util.override('data_flow.create_run_extended.command_name', 'create'), help=u"""Creates a run for an application. \n[Command Reference](createRun)""")
@cli_util.option('--application-id', required=True, help=u"""The OCID of the associated application. If this value is set, then no value for the execute parameter is required. If this value is not set, then a value for the execute parameter is required, and a new application is created and associated with the new run.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name that does not have to be unique. Avoid entering confidential information. If this value is not specified, it will be derived from the associated application's displayName or set by API using fileUri's application file name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'arguments': {'module': 'data_flow', 'class': 'list[string]'}, 'configuration': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_flow', 'class': 'dict(str, dict(str, object))'}, 'driver-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'executor-shape-config': {'module': 'data_flow', 'class': 'ShapeConfig'}, 'freeform-tags': {'module': 'data_flow', 'class': 'dict(str, string)'}, 'parameters': {'module': 'data_flow', 'class': 'list[ApplicationParameter]'}}, output_type={'module': 'data_flow', 'class': 'Run'})
@cli_util.wrap_exceptions
def create_run_extended(ctx, **kwargs):
    updateKwargs(kwargs)
    ctx.invoke(dataflow_cli.create_run, **kwargs)


# oci data-flow statement-collection list-statements -> oci data-flow statement-collection list
cli_util.rename_command(dataflow_cli, dataflow_cli.statement_collection_group, dataflow_cli.list_statements, "list")


# oci data-flow statement-collection -> oci data-flow statement
dataflow_cli.data_flow_root_group.commands.pop(dataflow_cli.statement_collection_group.name)
dataflow_cli.statement_group.add_command(dataflow_cli.list_statements)
