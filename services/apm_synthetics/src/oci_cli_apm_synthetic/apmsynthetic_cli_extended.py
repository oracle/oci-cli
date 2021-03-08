# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apm_synthetics.src.oci_cli_apm_synthetic.generated import apmsynthetic_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci apm-synthetics monitor create-monitor-scripted-rest-monitor-configuration -> oci apm-synthetics monitor create-scripted-rest-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration, "create-scripted-rest-monitor")


# oci apm-synthetics monitor update-monitor-scripted-rest-monitor-configuration -> oci apm-synthetics monitor update-scripted-rest-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration, "update-scripted-rest-monitor")


# oci apm-synthetics monitor create-monitor-scripted-browser-monitor-configuration -> oci apm-synthetics monitor create-scripted-browser-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration, "create-scripted-browser-monitor")


# oci apm-synthetics monitor update-monitor-scripted-browser-monitor-configuration -> oci apm-synthetics monitor update-scripted-browser-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration, "update-scripted-browser-monitor")


# Remove create from oci apm-synthetics monitor
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.create_monitor.name)


# Remove update from oci apm-synthetics monitor
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.update_monitor.name)


# oci apm-synthetics monitor create-monitor-browser-monitor-configuration -> oci apm-synthetics monitor create-browser-monitor
# oci apm-synthetics monitor update-monitor-browser-monitor-configuration -> oci apm-synthetics monitor update-browser-monitor
# oci apm-synthetics monitor create-monitor-rest-monitor-configuration -> oci apm-synthetics monitor create-rest-monitor
# oci apm-synthetics monitor update-monitor-rest-monitor-configuration -> oci apm-synthetics monitor update-rest-monitor
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.create_monitor_browser_monitor_configuration.name)
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.update_monitor_browser_monitor_configuration.name)
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.create_monitor_rest_monitor_configuration.name)
apmsynthetic_cli.monitor_group.commands.pop(apmsynthetic_cli.update_monitor_rest_monitor_configuration.name)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_verify_texts'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_browser_monitor_configuration.command_name', 'create-browser-monitor'), help=apmsynthetic_cli.create_monitor_browser_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verify all the search strings present in response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_browser_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'verify_texts' in kwargs:
        kwargs['configuration_verify_texts'] = kwargs['verify_texts']
        kwargs.pop('verify_texts')

    ctx.invoke(apmsynthetic_cli.create_monitor_browser_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_verify_texts'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_browser_monitor_configuration.command_name', 'update-browser-monitor'), help=apmsynthetic_cli.update_monitor_browser_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verify all the search strings present in response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_browser_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'verify_texts' in kwargs:
        kwargs['configuration_verify_texts'] = kwargs['verify_texts']
        kwargs.pop('verify_texts')

    ctx.invoke(apmsynthetic_cli.update_monitor_browser_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_rest_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_is_redirection_enabled', 'configuration_req_authentication_details', 'configuration_req_authentication_scheme', 'configuration_request_headers', 'configuration_request_method', 'configuration_request_post_body', 'configuration_request_query_params', 'configuration_verify_response_codes', 'configuration_verify_response_content'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_rest_monitor_configuration.command_name', 'create-rest-monitor'), help=apmsynthetic_cli.create_monitor_rest_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--is-redirection-enabled', type=click.BOOL, help=u"""If redirection enabled, then redirects will be allowed while accessing target URL.""")
@cli_util.option('--req-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["OAUTH", "NONE", "BASIC", "BEARER"]), help=u"""Request http authentication scheme.""")
@cli_util.option('--request-headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request headers. Example: `[{"headerName": "content-type", "headerValue":"json"}]`

This option is a JSON list with items of type Header.  For documentation on Header please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/Header.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--request-method', type=custom_types.CliCaseInsensitiveChoice(["GET", "POST"]), help=u"""Request HTTP method.""")
@cli_util.option('--request-post-body', help=u"""Request post body content.""")
@cli_util.option('--request-query-params', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request query params. Example: `[{"paramName": "sortOrder", "paramValue": "asc"}]`

This option is a JSON list with items of type RequestQueryParam.  For documentation on RequestQueryParam please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/RequestQueryParam.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected HTTP response codes. For status code range, please set values like 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match with the verifyResponseContent, then it will be considered as failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_rest_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'is_redirection_enabled' in kwargs:
        kwargs['configuration_is_redirection_enabled'] = kwargs['is_redirection_enabled']
        kwargs.pop('is_redirection_enabled')

    if 'req_authentication_details' in kwargs:
        kwargs['configuration_req_authentication_details'] = kwargs['req_authentication_details']
        kwargs.pop('req_authentication_details')

    if 'req_authentication_scheme' in kwargs:
        kwargs['configuration_req_authentication_scheme'] = kwargs['req_authentication_scheme']
        kwargs.pop('req_authentication_scheme')

    if 'request_headers' in kwargs:
        kwargs['configuration_request_headers'] = kwargs['request_headers']
        kwargs.pop('request_headers')

    if 'request_method' in kwargs:
        kwargs['configuration_request_method'] = kwargs['request_method']
        kwargs.pop('request_method')

    if 'request_post_body' in kwargs:
        kwargs['configuration_request_post_body'] = kwargs['request_post_body']
        kwargs.pop('request_post_body')

    if 'request_query_params' in kwargs:
        kwargs['configuration_request_query_params'] = kwargs['request_query_params']
        kwargs.pop('request_query_params')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.create_monitor_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_rest_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_is_redirection_enabled', 'configuration_req_authentication_details', 'configuration_req_authentication_scheme', 'configuration_request_headers', 'configuration_request_method', 'configuration_request_post_body', 'configuration_request_query_params', 'configuration_verify_response_codes', 'configuration_verify_response_content'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_rest_monitor_configuration.command_name', 'update-rest-monitor'), help=apmsynthetic_cli.update_monitor_rest_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--is-redirection-enabled', type=click.BOOL, help=u"""If redirection enabled, then redirects will be allowed while accessing target URL.""")
@cli_util.option('--req-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["OAUTH", "NONE", "BASIC", "BEARER"]), help=u"""Request http authentication scheme.""")
@cli_util.option('--request-headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request headers. Example: `[{"headerName": "content-type", "headerValue":"json"}]`

This option is a JSON list with items of type Header.  For documentation on Header please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/Header.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--request-method', type=custom_types.CliCaseInsensitiveChoice(["GET", "POST"]), help=u"""Request HTTP method.""")
@cli_util.option('--request-post-body', help=u"""Request post body content.""")
@cli_util.option('--request-query-params', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request query params. Example: `[{"paramName": "sortOrder", "paramValue": "asc"}]`

This option is a JSON list with items of type RequestQueryParam.  For documentation on RequestQueryParam please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/RequestQueryParam.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected HTTP response codes. For status code range, please set values like 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match with the verifyResponseContent, then it will be considered as failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_rest_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'is_redirection_enabled' in kwargs:
        kwargs['configuration_is_redirection_enabled'] = kwargs['is_redirection_enabled']
        kwargs.pop('is_redirection_enabled')

    if 'req_authentication_details' in kwargs:
        kwargs['configuration_req_authentication_details'] = kwargs['req_authentication_details']
        kwargs.pop('req_authentication_details')

    if 'req_authentication_scheme' in kwargs:
        kwargs['configuration_req_authentication_scheme'] = kwargs['req_authentication_scheme']
        kwargs.pop('req_authentication_scheme')

    if 'request_headers' in kwargs:
        kwargs['configuration_request_headers'] = kwargs['request_headers']
        kwargs.pop('request_headers')

    if 'request_method' in kwargs:
        kwargs['configuration_request_method'] = kwargs['request_method']
        kwargs.pop('request_method')

    if 'request_post_body' in kwargs:
        kwargs['configuration_request_post_body'] = kwargs['request_post_body']
        kwargs.pop('request_post_body')

    if 'request_query_params' in kwargs:
        kwargs['configuration_request_query_params'] = kwargs['request_query_params']
        kwargs.pop('request_query_params')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.update_monitor_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration, params_to_exclude=['configuration_is_failure_retried'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration.help)
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_rest_monitor_configuration_extended(ctx, **kwargs):
    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration, params_to_exclude=['configuration_is_failure_retried'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration.help)
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_rest_monitor_configuration_extended(ctx, **kwargs):
    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_browser_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration.help)
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_browser_monitor_configuration_extended(ctx, **kwargs):
    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration, **kwargs)
