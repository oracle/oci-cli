# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
import base64
import os
import sys
import zipfile

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


# oci apm-synthetics dedicated-vantage-point create-dedicated-vantage-point-oracle-rm-stack -> oci apm-synthetics dedicated-vantage-point create-with-oracle-rm-stack
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.dedicated_vantage_point_group, apmsynthetic_cli.create_dedicated_vantage_point_oracle_rm_stack, "create-with-oracle-rm-stack")

# oci apm-synthetics dedicated-vantage-point update-dedicated-vantage-point-oracle-rm-stack -> oci apm-synthetics dedicated-vantage-point update-with-oracle-rm-stack
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.dedicated_vantage_point_group, apmsynthetic_cli.update_dedicated_vantage_point_oracle_rm_stack, "update-with-oracle-rm-stack")


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_verify_texts', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_default_snapshot_enabled', 'configuration_verify_response_codes', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_browser_monitor_configuration.command_name', 'create-browser-monitor'), help=apmsynthetic_cli.create_monitor_browser_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--is-default-snapshot-enabled', type=click.BOOL, help="""If disabled then auto snapshots are not collected.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help="""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verify all the search strings present in response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_browser_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'is_default_snapshot_enabled' in kwargs:
        kwargs['configuration_is_default_snapshot_enabled'] = kwargs['is_default_snapshot_enabled']
        kwargs.pop('is_default_snapshot_enabled')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

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


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_verify_texts', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_default_snapshot_enabled', 'configuration_verify_response_codes', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_browser_monitor_configuration.command_name', 'update-browser-monitor'), help=apmsynthetic_cli.update_monitor_browser_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--is-default-snapshot-enabled', type=click.BOOL, help="""If disabled then auto snapshots are not collected.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help="""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@cli_util.option('--verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verify all the search strings present in response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_browser_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'is_default_snapshot_enabled' in kwargs:
        kwargs['configuration_is_default_snapshot_enabled'] = kwargs['is_default_snapshot_enabled']
        kwargs.pop('is_default_snapshot_enabled')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

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


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_rest_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_is_redirection_enabled', 'configuration_req_authentication_details', 'configuration_req_authentication_scheme', 'configuration_request_headers', 'configuration_request_method', 'configuration_request_post_body', 'configuration_request_query_params', 'configuration_verify_response_codes', 'configuration_verify_response_content', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_client_certificate_details', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_rest_monitor_configuration.command_name', 'create-rest-monitor'), help=apmsynthetic_cli.create_monitor_rest_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--client-certificate-details', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'client-certificate-details': {'module': 'apm_synthetics', 'class': 'ClientCertificateDetails'}, 'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_rest_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'client_certificate_details' in kwargs:
        kwargs['configuration_client_certificate_details'] = kwargs['client_certificate_details']
        kwargs.pop('client_certificate_details')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

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


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_rest_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_is_redirection_enabled', 'configuration_req_authentication_details', 'configuration_req_authentication_scheme', 'configuration_request_headers', 'configuration_request_method', 'configuration_request_post_body', 'configuration_request_query_params', 'configuration_verify_response_codes', 'configuration_verify_response_content', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_client_certificate_details', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_rest_monitor_configuration.command_name', 'update-rest-monitor'), help=apmsynthetic_cli.update_monitor_rest_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--client-certificate-details', type=custom_types.CLI_COMPLEX_TYPE, help="""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
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
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'client-certificate-details': {'module': 'apm_synthetics', 'class': 'ClientCertificateDetails'}, 'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_rest_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'client_certificate_details' in kwargs:
        kwargs['configuration_client_certificate_details'] = kwargs['client_certificate_details']
        kwargs.pop('client_certificate_details')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

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


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration, params_to_exclude=['configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_req_authentication_scheme', 'configuration_verify_response_codes', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["NONE", "RESOURCE_PRINCIPAL"]), help="""Request HTTP authentication scheme.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help="""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_rest_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'req_authentication_scheme' in kwargs:
        kwargs['configuration_req_authentication_scheme'] = kwargs['req_authentication_scheme']
        kwargs.pop('req_authentication_scheme')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.create_monitor_scripted_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration, params_to_exclude=['configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_req_authentication_scheme', 'configuration_verify_response_codes', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["NONE", "RESOURCE_PRINCIPAL"]), help="""Request HTTP authentication scheme.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help="""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_rest_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'req_authentication_scheme' in kwargs:
        kwargs['configuration_req_authentication_scheme'] = kwargs['req_authentication_scheme']
        kwargs.pop('req_authentication_scheme')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.update_monitor_scripted_rest_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_default_snapshot_enabled', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--is-default-snapshot-enabled', type=click.BOOL, help="""If disabled then auto snapshots are not collected.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_browser_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'is_default_snapshot_enabled' in kwargs:
        kwargs['configuration_is_default_snapshot_enabled'] = kwargs['is_default_snapshot_enabled']
        kwargs.pop('is_default_snapshot_enabled')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.create_monitor_scripted_browser_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration, params_to_exclude=['configuration_is_certificate_validation_enabled', 'configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_default_snapshot_enabled', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--is-default-snapshot-enabled', type=click.BOOL, help="""If disabled then auto snapshots are not collected.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Dns settings. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help="""Details of the network configuration. This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried enabled, then if call is failed then it will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_browser_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'is_default_snapshot_enabled' in kwargs:
        kwargs['configuration_is_default_snapshot_enabled'] = kwargs['is_default_snapshot_enabled']
        kwargs.pop('is_default_snapshot_enabled')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'is_certificate_validation_enabled' in kwargs:
        kwargs['configuration_is_certificate_validation_enabled'] = kwargs['is_certificate_validation_enabled']
        kwargs.pop('is_certificate_validation_enabled')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.update_monitor_scripted_browser_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_dedicated_vantage_point, params_to_exclude=['endpoint_parameterconflict', 'region_parameterconflict'])
@apmsynthetic_cli.dedicated_vantage_point_group.command(name=apmsynthetic_cli.create_dedicated_vantage_point.name, help=apmsynthetic_cli.create_dedicated_vantage_point.help)
@cli_util.option('--dvp-endpoint', required=True, help=u"""Upload endpoint. It will be a stream ocid for OCI OSS stream. [required]""")
@cli_util.option('--dvp-region', required=True, help=u"""Region name. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def create_dedicated_vantage_point_extended(ctx, **kwargs):
    if 'dvp_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['dvp_endpoint']
        kwargs.pop('dvp_endpoint')

    if 'dvp_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['dvp_region']
        kwargs.pop('dvp_region')

    ctx.invoke(apmsynthetic_cli.create_dedicated_vantage_point, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_dedicated_vantage_point, params_to_exclude=['endpoint_parameterconflict', 'region_parameterconflict'])
@apmsynthetic_cli.dedicated_vantage_point_group.command(name=apmsynthetic_cli.update_dedicated_vantage_point.name, help=apmsynthetic_cli.update_dedicated_vantage_point.help)
@cli_util.option('--dvp-endpoint', help=u"""Upload endpoint. It will be a stream ocid for OCI OSS stream.""")
@cli_util.option('--dvp-region', help=u"""Region name.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def update_dedicated_vantage_point_extended(ctx, **kwargs):
    if 'dvp_endpoint' in kwargs:
        kwargs['endpoint_parameterconflict'] = kwargs['dvp_endpoint']
        kwargs.pop('dvp_endpoint')

    if 'dvp_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['dvp_region']
        kwargs.pop('dvp_region')

    ctx.invoke(apmsynthetic_cli.update_dedicated_vantage_point, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_dedicated_vantage_point_oracle_rm_stack, params_to_exclude=['region_parameterconflict'])
@apmsynthetic_cli.dedicated_vantage_point_group.command(name=apmsynthetic_cli.create_dedicated_vantage_point_oracle_rm_stack.name, help=apmsynthetic_cli.create_dedicated_vantage_point_oracle_rm_stack.help)
@cli_util.option('--dvp-region', required=True, help=u"""Name of the region. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def create_dedicated_vantage_point_oracle_rm_stack_extended(ctx, **kwargs):
    if 'dvp_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['dvp_region']
        kwargs.pop('dvp_region')

    ctx.invoke(apmsynthetic_cli.create_dedicated_vantage_point_oracle_rm_stack, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_dedicated_vantage_point_oracle_rm_stack, params_to_exclude=['region_parameterconflict'])
@apmsynthetic_cli.dedicated_vantage_point_group.command(name=apmsynthetic_cli.update_dedicated_vantage_point_oracle_rm_stack.name, help=apmsynthetic_cli.update_dedicated_vantage_point_oracle_rm_stack.help)
@cli_util.option('--dvp-region', help=u"""Name of the region.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def update_dedicated_vantage_point_oracle_rm_stack_extended(ctx, **kwargs):
    if 'dvp_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['dvp_region']
        kwargs.pop('dvp_region')

    ctx.invoke(apmsynthetic_cli.update_dedicated_vantage_point_oracle_rm_stack, **kwargs)


# Remove create from oci apm-synthetics dedicated-vantage-point
apmsynthetic_cli.dedicated_vantage_point_group.commands.pop(apmsynthetic_cli.create_dedicated_vantage_point.name)

# Remove update from oci apm-synthetics dedicated-vantage-point
apmsynthetic_cli.dedicated_vantage_point_group.commands.pop(apmsynthetic_cli.update_dedicated_vantage_point.name)


# oci apm-synthetics monitor create-monitor-network-monitor-configuration -> oci apm-synthetics monitor create-network-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_network_monitor_configuration, "create-network-monitor")


# oci apm-synthetics monitor update-monitor-network-monitor-configuration -> oci apm-synthetics monitor update-network-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_network_monitor_configuration, "update-network-monitor")


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_network_monitor_configuration, params_to_exclude=['configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_failure_retried', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_network_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_network_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--network-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_network_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.create_monitor_network_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_network_monitor_configuration, params_to_exclude=['configuration_network_configuration', 'configuration_dns_configuration', 'configuration_is_failure_retried', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_network_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_network_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--network-configuration', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
 [required]""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_network_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    ctx.invoke(apmsynthetic_cli.update_monitor_network_monitor_configuration, **kwargs)


# oci apm-synthetics monitor create-monitor-dns-sec-monitor-configuration -> oci apm-synthetics monitor create-dns-sec-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_dns_sec_monitor_configuration, "create-dns-sec-monitor")


# oci apm-synthetics monitor create-monitor-dns-server-monitor-configuration -> oci apm-synthetics monitor create-dns-server-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_dns_server_monitor_configuration, "create-dns-server-monitor")


# oci apm-synthetics monitor create-monitor-dns-trace-monitor-configuration -> oci apm-synthetics monitor create-dns-trace-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_dns_trace_monitor_configuration, "create-dns-trace-monitor")


# oci apm-synthetics monitor update-monitor-dns-sec-monitor-configuration -> oci apm-synthetics monitor update-dns-sec-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_dns_sec_monitor_configuration, "update-dns-sec-monitor")


# oci apm-synthetics monitor update-monitor-dns-server-monitor-configuration -> oci apm-synthetics monitor update-dns-server-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_dns_server_monitor_configuration, "update-dns-server-monitor")


# oci apm-synthetics monitor update-monitor-dns-trace-monitor-configuration -> oci apm-synthetics monitor update-dns-trace-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_dns_trace_monitor_configuration, "update-dns-trace-monitor")


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_dns_sec_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_dns_sec_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_dns_sec_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_dns_sec_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.create_monitor_dns_sec_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_dns_server_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_is_query_recursive', 'configuration_name_server', 'configuration_network_configuration', 'configuration_protocol', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_dns_server_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_dns_server_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--is-query-recursive', type=click.BOOL, help=u"""If isQueryRecursive is enabled, then queries will be sent recursively to the target server.""")
@cli_util.option('--name-server', help=u"""Name of the server that will be used to perform DNS lookup.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["TCP", "UDP"]), help=u"""Type of protocol.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_dns_server_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'is_query_recursive' in kwargs:
        kwargs['configuration_is_query_recursive'] = kwargs['is_query_recursive']
        kwargs.pop('is_query_recursive')

    if 'name_server' in kwargs:
        kwargs['configuration_name_server'] = kwargs['name_server']
        kwargs.pop('name_server')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'protocol' in kwargs:
        kwargs['configuration_protocol'] = kwargs['protocol']
        kwargs.pop('protocol')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.create_monitor_dns_server_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_dns_trace_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_protocol', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_dns_trace_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_dns_trace_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["TCP", "UDP"]), help=u"""Type of protocol.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_dns_trace_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'protocol' in kwargs:
        kwargs['configuration_protocol'] = kwargs['protocol']
        kwargs.pop('protocol')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.create_monitor_dns_trace_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_dns_sec_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_dns_sec_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_dns_sec_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_dns_sec_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.update_monitor_dns_sec_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_dns_server_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_is_query_recursive', 'configuration_name_server', 'configuration_network_configuration', 'configuration_protocol', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_dns_server_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_dns_server_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--is-query-recursive', type=click.BOOL, help=u"""If isQueryRecursive is enabled, then queries will be sent recursively to the target server.""")
@cli_util.option('--name-server', help=u"""Name of the server that will be used to perform DNS lookup.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["TCP", "UDP"]), help=u"""Type of protocol.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_dns_server_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'is_query_recursive' in kwargs:
        kwargs['configuration_is_query_recursive'] = kwargs['is_query_recursive']
        kwargs.pop('is_query_recursive')

    if 'name_server' in kwargs:
        kwargs['configuration_name_server'] = kwargs['name_server']
        kwargs.pop('name_server')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'protocol' in kwargs:
        kwargs['configuration_protocol'] = kwargs['protocol']
        kwargs.pop('protocol')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.update_monitor_dns_server_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_dns_trace_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_protocol', 'configuration_record_type', 'configuration_verify_response_content', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_dns_trace_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_dns_trace_monitor_configuration.help)
@cli_util.option('--is-ipv6', type=click.BOOL, help="""If enabled, domain name will resolve to an IPv6 address.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["TCP", "UDP"]), help=u"""Type of protocol.""")
@cli_util.option('--record-type', type=custom_types.CliCaseInsensitiveChoice(["A", "AAAA", "ANY", "CNAME", "DNSKEY", "DS", "MX", "NS", "NSEC", "NULL_REC", "PTR", "RRSIG", "SOA", "TXT"]), help=u"""DNS record type.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_dns_trace_monitor_configuration_extended(ctx, **kwargs):

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'protocol' in kwargs:
        kwargs['configuration_protocol'] = kwargs['protocol']
        kwargs.pop('protocol')

    if 'record_type' in kwargs:
        kwargs['configuration_record_type'] = kwargs['record_type']
        kwargs.pop('record_type')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    ctx.invoke(apmsynthetic_cli.update_monitor_dns_trace_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_worker, params_to_exclude=['version_parameterconflict'])
@apmsynthetic_cli.worker_group.command(name=apmsynthetic_cli.create_worker.name, help=apmsynthetic_cli.create_worker.help)
@cli_util.option('--worker-version', required=True, help=u"""Image version of the On-premise VP worker. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'configuration-details': {'module': 'apm_synthetics', 'class': 'object'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Worker'})
@cli_util.wrap_exceptions
def create_worker_extended(ctx, **kwargs):

    if 'worker_version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['worker_version']
        kwargs.pop('worker_version')

    ctx.invoke(apmsynthetic_cli.create_worker, **kwargs)


# oci apm-synthetics monitor create-monitor-ftp-monitor-configuration -> oci apm-synthetics monitor create-ftp-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_ftp_monitor_configuration, "create-ftp-monitor")


# oci apm-synthetics monitor create-monitor-sql-monitor-configuration -> oci apm-synthetics monitor create-sql-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.create_monitor_sql_monitor_configuration, "create-sql-monitor")


# oci apm-synthetics monitor update-monitor-ftp-monitor-configuration -> oci apm-synthetics monitor update-ftp-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_ftp_monitor_configuration, "update-ftp-monitor")


# oci apm-synthetics monitor update-monitor-sql-monitor-configuration -> oci apm-synthetics monitor update-sql-monitor
cli_util.rename_command(apmsynthetic_cli, apmsynthetic_cli.monitor_group, apmsynthetic_cli.update_monitor_sql_monitor_configuration, "update-sql-monitor")


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_ftp_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_download_size_limit_in_bytes', 'configuration_ftp_basic_authentication_details', 'configuration_ftp_protocol', 'configuration_ftp_request_type', 'configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_upload_file_size_in_bytes', 'configuration_verify_response_codes', 'configuration_verify_response_content', 'configuration_is_active_mode', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_ftp_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_ftp_monitor_configuration.help)
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--download-size-limit-in-bytes', type=click.INT, help=u"""Download size limit in Bytes, at which to stop the transfer. Maximum download size limit is 5 MiB.""")
@cli_util.option('--ftp-basic-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ftp-protocol', type=custom_types.CliCaseInsensitiveChoice(["FTP", "FTPS", "SFTP"]), help=u"""FTP protocol type.""")
@cli_util.option('--ftp-request-type', type=custom_types.CliCaseInsensitiveChoice(["LIST", "UPLOAD", "DOWNLOAD"]), help=u"""FTP monitor request type.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--upload-file-size-in-bytes', type=click.INT, help=u"""File upload size in Bytes, at which to stop the transfer. Maximum upload size is 5 MiB.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected FTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@cli_util.option('--is-active-mode', type=click.BOOL, help=u"""If enabled, Active mode will be used for the FTP connection.""")
@cli_util.option('--is-ipv6', type=click.BOOL, help=u"""If enabled, domain name will resolve to an IPv6 address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'ftp-basic-authentication-details': {'module': 'apm_synthetics', 'class': 'BasicAuthenticationDetails'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_ftp_monitor_configuration_extended(ctx, **kwargs):

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'download_size_limit_in_bytes' in kwargs:
        kwargs['configuration_download_size_limit_in_bytes'] = kwargs['download_size_limit_in_bytes']
        kwargs.pop('download_size_limit_in_bytes')

    if 'ftp_basic_authentication_details' in kwargs:
        kwargs['configuration_ftp_basic_authentication_details'] = kwargs['ftp_basic_authentication_details']
        kwargs.pop('ftp_basic_authentication_details')

    if 'ftp_protocol' in kwargs:
        kwargs['configuration_ftp_protocol'] = kwargs['ftp_protocol']
        kwargs.pop('ftp_protocol')

    if 'ftp_request_type' in kwargs:
        kwargs['configuration_ftp_request_type'] = kwargs['ftp_request_type']
        kwargs.pop('ftp_request_type')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'upload_file_size_in_bytes' in kwargs:
        kwargs['configuration_upload_file_size_in_bytes'] = kwargs['upload_file_size_in_bytes']
        kwargs.pop('upload_file_size_in_bytes')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    if 'is_active_mode' in kwargs:
        kwargs['configuration_is_active_mode'] = kwargs['is_active_mode']
        kwargs.pop('is_active_mode')

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    ctx.invoke(apmsynthetic_cli.create_monitor_ftp_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.create_monitor_sql_monitor_configuration, params_to_exclude=['configuration_database_wallet_details', 'configuration_connection_string', 'configuration_database_authentication_details', 'configuration_database_connection_type', 'configuration_database_role', 'configuration_database_type', 'configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_query', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.create_monitor_sql_monitor_configuration.name, help=apmsynthetic_cli.create_monitor_sql_monitor_configuration.help)
@cli_util.option('--database-service-name', help="""Service name of the database. Required for database-connection-type CLOUD_WALLET""")
@cli_util.option('--database-wallet', help="""The database wallet configuration zip file path. Required for database-connection-type CLOUD_WALLET""")
@cli_util.option('--connection-string', help=u"""Database connection string. Required for database-connection-type CUSTOM_JDBC""")
@cli_util.option('--database-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--database-connection-type', type=custom_types.CliCaseInsensitiveChoice(["CLOUD_WALLET", "CUSTOM_JDBC"]), help=u"""Database connection type.""")
@cli_util.option('--database-role', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT", "SYSDBA", "SYSOPER", "SYSBACKUP", "SYSDG", "SYSKM", "SYSASM"]), help=u"""Database role.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE", "MYSQL"]), help=u"""Database type.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--database-query', help=u"""SQL query to be executed.""")
@cli_util.option('--is-ipv6', type=click.BOOL, help=u"""If enabled, domain name will resolve to an IPv6 address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'database-authentication-details': {'module': 'apm_synthetics', 'class': 'BasicAuthenticationDetails'}, 'database-wallet-details': {'module': 'apm_synthetics', 'class': 'DatabaseWalletDetails'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_sql_monitor_configuration_extended(ctx, **kwargs):
    database_wallet_details = {}
    if 'database_service_name' in kwargs and kwargs['database_service_name'] is not None:
        database_wallet_details['serviceName'] = kwargs['database_service_name']
        kwargs.pop('database_service_name')

    if 'database_wallet' in kwargs and kwargs['database_wallet'] is not None:
        database_wallet = os.path.expandvars(os.path.expanduser(kwargs['database_wallet']))
        if not os.path.exists(database_wallet):
            click.echo('Config source does not exist', file=sys.stderr)
            ctx.abort()

        if not (database_wallet.endswith(".zip") and os.path.isfile(database_wallet) and zipfile.is_zipfile(database_wallet)):
            click.echo('Database wallet must be a .zip file.', file=sys.stderr)
            ctx.abort()

        send_value = create_base64encoded_zip(database_wallet)
        if not send_value:
            click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
            ctx.abort()

        database_wallet_details['databaseWallet'] = send_value
        kwargs.pop('database_wallet')

    if len(database_wallet_details) > 0:
        kwargs['configuration_database_wallet_details'] = json.dumps(database_wallet_details)

    if 'connection_string' in kwargs:
        kwargs['configuration_connection_string'] = kwargs['connection_string']
        kwargs.pop('connection_string')

    if 'database_authentication_details' in kwargs:
        kwargs['configuration_database_authentication_details'] = kwargs['database_authentication_details']
        kwargs.pop('database_authentication_details')

    if 'database_connection_type' in kwargs:
        kwargs['configuration_database_connection_type'] = kwargs['database_connection_type']
        kwargs.pop('database_connection_type')

    if 'database_role' in kwargs:
        kwargs['configuration_database_role'] = kwargs['database_role']
        kwargs.pop('database_role')

    if 'database_type' in kwargs:
        kwargs['configuration_database_type'] = kwargs['database_type']
        kwargs.pop('database_type')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'database_query' in kwargs:
        kwargs['configuration_query'] = kwargs['database_query']
        kwargs.pop('database_query')

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'database_wallet' in kwargs:
        kwargs.pop('database_wallet')

    if 'database_service_name' in kwargs:
        kwargs.pop('database_service_name')

    ctx.invoke(apmsynthetic_cli.create_monitor_sql_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_ftp_monitor_configuration, params_to_exclude=['configuration_dns_configuration', 'configuration_download_size_limit_in_bytes', 'configuration_ftp_basic_authentication_details', 'configuration_ftp_protocol', 'configuration_ftp_request_type', 'configuration_is_failure_retried', 'configuration_network_configuration', 'configuration_upload_file_size_in_bytes', 'configuration_verify_response_codes', 'configuration_verify_response_content', 'configuration_is_active_mode', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_ftp_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_ftp_monitor_configuration.help)
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--download-size-limit-in-bytes', type=click.INT, help=u"""Download size limit in Bytes, at which to stop the transfer. Maximum download size limit is 5 MiB.""")
@cli_util.option('--ftp-basic-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--ftp-request-type', type=custom_types.CliCaseInsensitiveChoice(["LIST", "UPLOAD", "DOWNLOAD"]), help=u"""FTP monitor request type.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--upload-file-size-in-bytes', type=click.INT, help=u"""File upload size in Bytes, at which to stop the transfer. Maximum upload size is 5 MiB.""")
@cli_util.option('--verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected FTP response codes. For status code range, set values such as 2xx, 3xx.
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@cli_util.option('--is-active-mode', type=click.BOOL, help=u"""If enabled, Active mode will be used for the FTP connection.""")
@cli_util.option('--is-ipv6', type=click.BOOL, help=u"""If enabled, domain name will resolve to an IPv6 address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'ftp-basic-authentication-details': {'module': 'apm_synthetics', 'class': 'BasicAuthenticationDetails'}, 'network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}, 'verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_ftp_monitor_configuration_extended(ctx, **kwargs):

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'download_size_limit_in_bytes' in kwargs:
        kwargs['configuration_download_size_limit_in_bytes'] = kwargs['download_size_limit_in_bytes']
        kwargs.pop('download_size_limit_in_bytes')

    if 'ftp_basic_authentication_details' in kwargs:
        kwargs['configuration_ftp_basic_authentication_details'] = kwargs['ftp_basic_authentication_details']
        kwargs.pop('ftp_basic_authentication_details')

    if 'ftp_protocol' in kwargs:
        kwargs.pop('ftp_protocol')

    if 'ftp_request_type' in kwargs:
        kwargs['configuration_ftp_request_type'] = kwargs['ftp_request_type']
        kwargs.pop('ftp_request_type')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'network_configuration' in kwargs:
        kwargs['configuration_network_configuration'] = kwargs['network_configuration']
        kwargs.pop('network_configuration')

    if 'upload_file_size_in_bytes' in kwargs:
        kwargs['configuration_upload_file_size_in_bytes'] = kwargs['upload_file_size_in_bytes']
        kwargs.pop('upload_file_size_in_bytes')

    if 'verify_response_codes' in kwargs:
        kwargs['configuration_verify_response_codes'] = kwargs['verify_response_codes']
        kwargs.pop('verify_response_codes')

    if 'verify_response_content' in kwargs:
        kwargs['configuration_verify_response_content'] = kwargs['verify_response_content']
        kwargs.pop('verify_response_content')

    if 'is_active_mode' in kwargs:
        kwargs['configuration_is_active_mode'] = kwargs['is_active_mode']
        kwargs.pop('is_active_mode')

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    ctx.invoke(apmsynthetic_cli.update_monitor_ftp_monitor_configuration, **kwargs)


@cli_util.copy_params_from_generated_command(apmsynthetic_cli.update_monitor_sql_monitor_configuration, params_to_exclude=['configuration_database_wallet_details', 'configuration_connection_string', 'configuration_database_authentication_details', 'configuration_database_connection_type', 'configuration_database_role', 'configuration_database_type', 'configuration_dns_configuration', 'configuration_is_failure_retried', 'configuration_query', 'is_i_pv6'])
@apmsynthetic_cli.monitor_group.command(name=apmsynthetic_cli.update_monitor_sql_monitor_configuration.name, help=apmsynthetic_cli.update_monitor_sql_monitor_configuration.help)
@cli_util.option('--database-service-name', help="""Service name of the database. Required for database-connection-type CLOUD_WALLET""")
@cli_util.option('--database-wallet', help="""The database wallet configuration zip file path. Required for database-connection-type CLOUD_WALLET""")
@cli_util.option('--connection-string', help=u"""Database connection string. Required for database-connection-type CUSTOM_JDBC""")
@cli_util.option('--database-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--database-connection-type', type=custom_types.CliCaseInsensitiveChoice(["CLOUD_WALLET", "CUSTOM_JDBC"]), help=u"""Database connection type.""")
@cli_util.option('--database-role', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT", "SYSDBA", "SYSOPER", "SYSBACKUP", "SYSDG", "SYSKM", "SYSASM"]), help=u"""Database role.""")
@cli_util.option('--database-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE", "MYSQL"]), help=u"""Database type.""")
@cli_util.option('--dns-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.""")
@cli_util.option('--is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--database-query', help=u"""SQL query to be executed.""")
@cli_util.option('--is-ipv6', type=click.BOOL, help=u"""If enabled, domain name will resolve to an IPv6 address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'availability-configuration': {'module': 'apm_synthetics', 'class': 'AvailabilityConfiguration'}, 'maintenance-window-schedule': {'module': 'apm_synthetics', 'class': 'MaintenanceWindowSchedule'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'dns-configuration': {'module': 'apm_synthetics', 'class': 'DnsConfiguration'}, 'database-authentication-details': {'module': 'apm_synthetics', 'class': 'BasicAuthenticationDetails'}, 'database-wallet-details': {'module': 'apm_synthetics', 'class': 'DatabaseWalletDetails'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_sql_monitor_configuration_extended(ctx, **kwargs):
    database_wallet_details = {}
    if 'database_service_name' in kwargs and kwargs['database_service_name'] is not None:
        database_wallet_details['serviceName'] = kwargs['database_service_name']
        kwargs.pop('database_service_name')

    if 'database_wallet' in kwargs and kwargs['database_wallet'] is not None:
        database_wallet = os.path.expandvars(os.path.expanduser(kwargs['database_wallet']))
        if not os.path.exists(database_wallet):
            click.echo('Config source does not exist', file=sys.stderr)
            ctx.abort()

        if not (database_wallet.endswith(".zip") and os.path.isfile(database_wallet) and zipfile.is_zipfile(database_wallet)):
            click.echo('Database wallet must be a .zip file.', file=sys.stderr)
            ctx.abort()

        send_value = create_base64encoded_zip(database_wallet)
        if not send_value:
            click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
            ctx.abort()

        database_wallet_details['databaseWallet'] = send_value
        kwargs.pop('database_wallet')

    if len(database_wallet_details) > 0:
        kwargs['configuration_database_wallet_details'] = json.dumps(database_wallet_details)

    if 'connection_string' in kwargs:
        kwargs['configuration_connection_string'] = kwargs['connection_string']
        kwargs.pop('connection_string')

    if 'database_authentication_details' in kwargs:
        kwargs['configuration_database_authentication_details'] = kwargs['database_authentication_details']
        kwargs.pop('database_authentication_details')

    if 'database_connection_type' in kwargs:
        kwargs['configuration_database_connection_type'] = kwargs['database_connection_type']
        kwargs.pop('database_connection_type')

    if 'database_role' in kwargs:
        kwargs['configuration_database_role'] = kwargs['database_role']
        kwargs.pop('database_role')

    if 'database_type' in kwargs:
        kwargs['configuration_database_type'] = kwargs['database_type']
        kwargs.pop('database_type')

    if 'dns_configuration' in kwargs:
        kwargs['configuration_dns_configuration'] = kwargs['dns_configuration']
        kwargs.pop('dns_configuration')

    if 'is_failure_retried' in kwargs:
        kwargs['configuration_is_failure_retried'] = kwargs['is_failure_retried']
        kwargs.pop('is_failure_retried')

    if 'database_query' in kwargs:
        kwargs['configuration_query'] = kwargs['database_query']
        kwargs.pop('database_query')

    if 'is_ipv6' in kwargs:
        kwargs['is_i_pv6'] = kwargs['is_ipv6']
        kwargs.pop('is_ipv6')

    if 'database_wallet' in kwargs:
        kwargs.pop('database_wallet')

    if 'database_service_name' in kwargs:
        kwargs.pop('database_service_name')

    ctx.invoke(apmsynthetic_cli.update_monitor_sql_monitor_configuration, **kwargs)


def create_base64encoded_zip(database_wallet):
    if database_wallet.endswith(".zip") and os.path.isfile(database_wallet) and zipfile.is_zipfile(database_wallet):
        with open(database_wallet, mode='rb') as zip_file:
            return base64.b64encode(zip_file.read()).decode('utf-8')
