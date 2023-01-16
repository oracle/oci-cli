# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('adm.adm_root_group.command_name', 'adm'), cls=CommandGroupWithAlias, help=cli_util.override('adm.adm_root_group.help', """Use the Application Dependency Management API to create knowledge bases and vulnerability audits.  For more information, see [ADM]."""), short_help=cli_util.override('adm.adm_root_group.short_help', """Application Dependency Management API"""))
@cli_util.help_option_group
def adm_root_group():
    pass


@click.command(cli_util.override('adm.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('adm.knowledge_base_group.command_name', 'knowledge-base'), cls=CommandGroupWithAlias, help="""A Knowledge Base is a component of Application Dependency Management that contains vulnerability audits.""")
@cli_util.help_option_group
def knowledge_base_group():
    pass


@click.command(cli_util.override('adm.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('adm.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('adm.vulnerability_audit_group.command_name', 'vulnerability-audit'), cls=CommandGroupWithAlias, help="""A Vulnerability Audit associates the Application Dependencies of a project with their associated Vulnerabilities. Each Vulnerability is associated with a score (Common Vulnerability Scoring System V2 or V3). A vulnerable Application Dependency can be ignored based on the configuration of the Vulnerability Audit. maxObservedCvssV2Score, maxObservedCvssV3Score and vulnerableArtifactsCount do not take into account non-vulnerable Application Dependency.""")
@cli_util.help_option_group
def vulnerability_audit_group():
    pass


adm_root_group.add_command(work_request_error_group)
adm_root_group.add_command(knowledge_base_group)
adm_root_group.add_command(work_request_log_entry_group)
adm_root_group.add_command(work_request_group)
adm_root_group.add_command(vulnerability_audit_group)


@work_request_group.command(name=cli_util.override('adm.cancel_work_request.command_name', 'cancel'), help=u"""Cancel work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@knowledge_base_group.command(name=cli_util.override('adm.change_knowledge_base_compartment.command_name', 'change-compartment'), help=u"""Moves a Knowledge Base from one compartment to another. \n[Command Reference](changeKnowledgeBaseCompartment)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of a Knowledge Base, as a URL path parameter.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which the resource must be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_knowledge_base_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, compartment_id, if_match):

    if isinstance(knowledge_base_id, six.string_types) and len(knowledge_base_id.strip()) == 0:
        raise click.UsageError('Parameter --knowledge-base-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.change_knowledge_base_compartment(
        knowledge_base_id=knowledge_base_id,
        change_knowledge_base_compartment_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.change_vulnerability_audit_compartment.command_name', 'change-compartment'), help=u"""Moves a Vulnerability Audit from one compartment to another. \n[Command Reference](changeVulnerabilityAuditCompartment)""")
@cli_util.option('--vulnerability-audit-id', required=True, help=u"""Unique Vulnerability Audit identifier path parameter.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to which the resource must be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_vulnerability_audit_compartment(ctx, from_json, vulnerability_audit_id, compartment_id, if_match):

    if isinstance(vulnerability_audit_id, six.string_types) and len(vulnerability_audit_id.strip()) == 0:
        raise click.UsageError('Parameter --vulnerability-audit-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.change_vulnerability_audit_compartment(
        vulnerability_audit_id=vulnerability_audit_id,
        change_vulnerability_audit_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@knowledge_base_group.command(name=cli_util.override('adm.create_knowledge_base.command_name', 'create'), help=u"""Creates a new Knowledge Base. \n[Command Reference](createKnowledgeBase)""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of the Knowledge Base's compartment.""")
@cli_util.option('--display-name', help=u"""The name of the Knowledge Base.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_knowledge_base(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_knowledge_base(
        create_knowledge_base_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.create_vulnerability_audit.command_name', 'create'), help=u"""Creates a new Vulnerability Audit by providing a tree of Application Dependencies. \n[Command Reference](createVulnerabilityAudit)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud identifier ([OCID]) of the Knowledge Base.""")
@cli_util.option('--build-type', required=True, help=u"""The type of the build tool.""")
@cli_util.option('--compartment-id', help=u"""The Oracle Cloud identifier ([OCID]) of the compartment associated with the Vulnerability Audit. If compartment identifier is not provided the compartment of the associated Knowledge Base will be used instead.""")
@cli_util.option('--application-dependencies', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Application Dependencies (without vulnerabilities).

This option is a JSON list with items of type ApplicationDependency.  For documentation on ApplicationDependency please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationdependencymanagement/20220421/datatypes/ApplicationDependency.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the Vulnerability Audit.""")
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'source': {'module': 'adm', 'class': 'VulnerabilityAuditSource'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'source': {'module': 'adm', 'class': 'VulnerabilityAuditSource'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, display_name, source, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.create_vulnerability_audit_unknown_source_vulnerability_audit_source.command_name', 'create-vulnerability-audit-unknown-source-vulnerability-audit-source'), help=u"""Creates a new Vulnerability Audit by providing a tree of Application Dependencies. \n[Command Reference](createVulnerabilityAudit)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud identifier ([OCID]) of the Knowledge Base.""")
@cli_util.option('--build-type', required=True, help=u"""The type of the build tool.""")
@cli_util.option('--compartment-id', help=u"""The Oracle Cloud identifier ([OCID]) of the compartment associated with the Vulnerability Audit. If compartment identifier is not provided the compartment of the associated Knowledge Base will be used instead.""")
@cli_util.option('--application-dependencies', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Application Dependencies (without vulnerabilities).

This option is a JSON list with items of type ApplicationDependency.  For documentation on ApplicationDependency please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationdependencymanagement/20220421/datatypes/ApplicationDependency.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the Vulnerability Audit.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_unknown_source_vulnerability_audit_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, display_name, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['type'] = 'UNKNOWN'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.create_vulnerability_audit_oci_resource_vulnerability_audit_source.command_name', 'create-vulnerability-audit-oci-resource-vulnerability-audit-source'), help=u"""Creates a new Vulnerability Audit by providing a tree of Application Dependencies. \n[Command Reference](createVulnerabilityAudit)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud identifier ([OCID]) of the Knowledge Base.""")
@cli_util.option('--build-type', required=True, help=u"""The type of the build tool.""")
@cli_util.option('--source-oci-resource-id', required=True, help=u"""The Oracle Cloud identifier ([OCID]) of the OCI resource that triggered the Vulnerability Audit.""")
@cli_util.option('--compartment-id', help=u"""The Oracle Cloud identifier ([OCID]) of the compartment associated with the Vulnerability Audit. If compartment identifier is not provided the compartment of the associated Knowledge Base will be used instead.""")
@cli_util.option('--application-dependencies', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Application Dependencies (without vulnerabilities).

This option is a JSON list with items of type ApplicationDependency.  For documentation on ApplicationDependency please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationdependencymanagement/20220421/datatypes/ApplicationDependency.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the Vulnerability Audit.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_oci_resource_vulnerability_audit_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, source_oci_resource_id, compartment_id, application_dependencies, configuration, display_name, freeform_tags, defined_tags, if_match):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type
    _details['source']['ociResourceId'] = source_oci_resource_id

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['type'] = 'OCI_RESOURCE'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.create_vulnerability_audit_external_resource_vulnerability_audit_source.command_name', 'create-vulnerability-audit-external-resource-vulnerability-audit-source'), help=u"""Creates a new Vulnerability Audit by providing a tree of Application Dependencies. \n[Command Reference](createVulnerabilityAudit)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud identifier ([OCID]) of the Knowledge Base.""")
@cli_util.option('--build-type', required=True, help=u"""The type of the build tool.""")
@cli_util.option('--compartment-id', help=u"""The Oracle Cloud identifier ([OCID]) of the compartment associated with the Vulnerability Audit. If compartment identifier is not provided the compartment of the associated Knowledge Base will be used instead.""")
@cli_util.option('--application-dependencies', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Application Dependencies (without vulnerabilities).

This option is a JSON list with items of type ApplicationDependency.  For documentation on ApplicationDependency please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationdependencymanagement/20220421/datatypes/ApplicationDependency.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the Vulnerability Audit.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--source-description', help=u"""Description of the external resource source.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'application-dependencies': {'module': 'adm', 'class': 'list[ApplicationDependency]'}, 'configuration': {'module': 'adm', 'class': 'VulnerabilityAuditConfiguration'}, 'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def create_vulnerability_audit_external_resource_vulnerability_audit_source(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, build_type, compartment_id, application_dependencies, configuration, display_name, freeform_tags, defined_tags, if_match, source_description):

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['knowledgeBaseId'] = knowledge_base_id
    _details['buildType'] = build_type

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if application_dependencies is not None:
        _details['applicationDependencies'] = cli_util.parse_json_parameter("application_dependencies", application_dependencies)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if source_description is not None:
        _details['source']['description'] = source_description

    _details['source']['type'] = 'EXTERNAL_RESOURCE'

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.create_vulnerability_audit(
        create_vulnerability_audit_details=_details,
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


@knowledge_base_group.command(name=cli_util.override('adm.delete_knowledge_base.command_name', 'delete'), help=u"""Deletes the specified Knowledge Base. \n[Command Reference](deleteKnowledgeBase)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of a Knowledge Base, as a URL path parameter.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_knowledge_base(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, if_match):

    if isinstance(knowledge_base_id, six.string_types) and len(knowledge_base_id.strip()) == 0:
        raise click.UsageError('Parameter --knowledge-base-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.delete_knowledge_base(
        knowledge_base_id=knowledge_base_id,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.delete_vulnerability_audit.command_name', 'delete'), help=u"""Deletes the specified Vulnerability Audit. \n[Command Reference](deleteVulnerabilityAudit)""")
@cli_util.option('--vulnerability-audit-id', required=True, help=u"""Unique Vulnerability Audit identifier path parameter.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vulnerability_audit(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, vulnerability_audit_id, if_match):

    if isinstance(vulnerability_audit_id, six.string_types) and len(vulnerability_audit_id.strip()) == 0:
        raise click.UsageError('Parameter --vulnerability-audit-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.delete_vulnerability_audit(
        vulnerability_audit_id=vulnerability_audit_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_vulnerability_audit(vulnerability_audit_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@knowledge_base_group.command(name=cli_util.override('adm.get_knowledge_base.command_name', 'get'), help=u"""Returns the details of the specified Knowledge Base. \n[Command Reference](getKnowledgeBase)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of a Knowledge Base, as a URL path parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'KnowledgeBase'})
@cli_util.wrap_exceptions
def get_knowledge_base(ctx, from_json, knowledge_base_id):

    if isinstance(knowledge_base_id, six.string_types) and len(knowledge_base_id.strip()) == 0:
        raise click.UsageError('Parameter --knowledge-base-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.get_knowledge_base(
        knowledge_base_id=knowledge_base_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vulnerability_audit_group.command(name=cli_util.override('adm.get_vulnerability_audit.command_name', 'get'), help=u"""Returns the details of the specified Vulnerability Audit. \n[Command Reference](getVulnerabilityAudit)""")
@cli_util.option('--vulnerability-audit-id', required=True, help=u"""Unique Vulnerability Audit identifier path parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def get_vulnerability_audit(ctx, from_json, vulnerability_audit_id):

    if isinstance(vulnerability_audit_id, six.string_types) and len(vulnerability_audit_id.strip()) == 0:
        raise click.UsageError('Parameter --vulnerability-audit-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.get_vulnerability_audit(
        vulnerability_audit_id=vulnerability_audit_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('adm.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@vulnerability_audit_group.command(name=cli_util.override('adm.list_application_dependency_vulnerabilities.command_name', 'list-application-dependency-vulnerabilities'), help=u"""Returns a list of Application Dependencies with their associated vulnerabilities. \n[Command Reference](listApplicationDependencyVulnerabilities)""")
@cli_util.option('--vulnerability-audit-id', required=True, help=u"""Unique Vulnerability Audit identifier path parameter.""")
@cli_util.option('--vulnerability-id', help=u"""A filter to return only Vulnerability Audits that match the specified id.""")
@cli_util.option('--cvss-v3-greater-than-or-equal', type=click.FLOAT, help=u"""A filter that returns only Vulnerability Audits that have a Common Vulnerability Scoring System Version 3 (CVSS V3) greater or equal than the specified value.""")
@cli_util.option('--cvss-v2-greater-than-or-equal', type=click.FLOAT, help=u"""A filter that returns only Vulnerability Audits that have a Common Vulnerability Scoring System Version 2 (CVSS V2) greater or equal than the specified value.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["gav", "nodeId", "dfs", "bfs"]), help=u"""The field to sort by. Only one sort order may be provided. If sort order is dfs, the nodes are returned by going through the application dependency tree in a depth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. If sort order is bfs, the nodes are returned by going through the application dependency tree in a breadth-first manner. Children are sorted based on their GAV property alphabetically (either ascending or descending, depending on the order parameter). Default order is ascending. Default order for gav is ascending where ascending corresponds to alphanumerical order. Default order for nodeId is ascending where ascending corresponds to alphanumerical order. Sorting by DFS or BFS cannot be used in conjunction with the following query parameters: \"gav\", \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\" and \"vulnerabilityId\".""")
@cli_util.option('--root-node-id', help=u"""A filter to override the top level root identifier with the new given value. The application dependency tree will only be traversed from the given node. Query parameters \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\", \"gav\" and \"vulnerabilityId\" cannot be used in conjunction with this parameter.""")
@cli_util.option('--depth', type=click.INT, help=u"""A filter to limit depth of the application dependencies tree traversal. Additionally query parameters such as \"cvssV2GreaterThanOrEqual\", \"cvssV3GreaterThanOrEqual\", \"gav\" and \"vulnerabilityId\" can't be used in conjunction with this latter.""")
@cli_util.option('--gav', help=u"""A filter to return only resources that match the entire GAV (Group Artifact Version) identifier given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'ApplicationDependencyVulnerabilityCollection'})
@cli_util.wrap_exceptions
def list_application_dependency_vulnerabilities(ctx, from_json, all_pages, page_size, vulnerability_audit_id, vulnerability_id, cvss_v3_greater_than_or_equal, cvss_v2_greater_than_or_equal, limit, page, sort_order, sort_by, root_node_id, depth, gav):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(vulnerability_audit_id, six.string_types) and len(vulnerability_audit_id.strip()) == 0:
        raise click.UsageError('Parameter --vulnerability-audit-id cannot be whitespace or empty string')

    kwargs = {}
    if vulnerability_id is not None:
        kwargs['vulnerability_id'] = vulnerability_id
    if cvss_v3_greater_than_or_equal is not None:
        kwargs['cvss_v3_greater_than_or_equal'] = cvss_v3_greater_than_or_equal
    if cvss_v2_greater_than_or_equal is not None:
        kwargs['cvss_v2_greater_than_or_equal'] = cvss_v2_greater_than_or_equal
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if root_node_id is not None:
        kwargs['root_node_id'] = root_node_id
    if depth is not None:
        kwargs['depth'] = depth
    if gav is not None:
        kwargs['gav'] = gav
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_application_dependency_vulnerabilities,
            vulnerability_audit_id=vulnerability_audit_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_application_dependency_vulnerabilities,
            limit,
            page_size,
            vulnerability_audit_id=vulnerability_audit_id,
            **kwargs
        )
    else:
        result = client.list_application_dependency_vulnerabilities(
            vulnerability_audit_id=vulnerability_audit_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@knowledge_base_group.command(name=cli_util.override('adm.list_knowledge_bases.command_name', 'list'), help=u"""Returns a list of KnowledgeBases based on the specified query parameters. At least id or compartmentId query parameter must be provided. \n[Command Reference](listKnowledgeBases)""")
@cli_util.option('--id', help=u"""A filter to return only resources that match the specified identifier.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DISPLAY_NAME", "LIFECYCLE_STATE", "TIME_CREATED", "TIME_UPDATED"]), help=u"""The field used to sort Knowledge Bases. Only one sort order is allowed. Default order for _displayName_ is **ascending alphabetical order**. Default order for _lifecyleState_ is the following sequence: **CREATING, ACTIVE, UPDATING, FAILED, DELETING, and DELETED**.Default order for _timeCreated_ is **descending**. Default order for _timeUpdated_ is **descending**.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "FAILED", "DELETING", "DELETED"]), help=u"""A filter to return only Knowledge Bases that match the specified lifecycleState.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that belong to the specified compartment identifier.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'KnowledgeBaseCollection'})
@cli_util.wrap_exceptions
def list_knowledge_bases(ctx, from_json, all_pages, page_size, id, sort_by, lifecycle_state, sort_order, display_name, limit, page, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_knowledge_bases,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_knowledge_bases,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_knowledge_bases(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@vulnerability_audit_group.command(name=cli_util.override('adm.list_vulnerability_audits.command_name', 'list'), help=u"""Returns a list of Vulnerability Audits based on the specified query parameters. At least one of id, compartmentId or knowledgeBaseId query parameter must be provided. \n[Command Reference](listVulnerabilityAudits)""")
@cli_util.option('--id', help=u"""A filter to return only resources that match the specified identifier.""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that belong to the specified compartment identifier.""")
@cli_util.option('--knowledge-base-id', help=u"""A filter to return only Vulnerability Audits that were created against the specified knowledge base.""")
@cli_util.option('--is-success', type=click.BOOL, help=u"""A filter to return only successful or failed Vulnerability Audits.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), help=u"""A filter to return only Vulnerability Audits that match the specified lifecycleState.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["maxObservedCvssV2Score", "maxObservedCvssV3Score", "timeCreated", "vulnerableArtifactsCount", "maxObservedCvssV2ScoreWithIgnored", "maxObservedCvssV3ScoreWithIgnored", "vulnerableArtifactsCountWithIgnored"]), help=u"""The field used to sort Vulnerability Audits. Only one sort order is allowed. Default order for _maxObservedCvssV2Score_ is **ascending**. Default order for _maxObservedCvssV3Score_ is **ascending**. Default order for _maxObservedCvssV2ScoreWithIgnored_ is **ascending**. Default order for _maxObservedCvssV3ScoreWithIgnored_ is **ascending**. Default order for _timeCreated_ is **descending**. Default order for _vulnerableArtifactsCount_ is **ascending**. Default order for _vulnerableArtifactsCountWithIgnored_ is **ascending**.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'VulnerabilityAuditCollection'})
@cli_util.wrap_exceptions
def list_vulnerability_audits(ctx, from_json, all_pages, page_size, id, compartment_id, knowledge_base_id, is_success, lifecycle_state, sort_order, limit, page, sort_by, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if knowledge_base_id is not None:
        kwargs['knowledge_base_id'] = knowledge_base_id
    if is_success is not None:
        kwargs['is_success'] = is_success
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_vulnerability_audits,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_vulnerability_audits,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_vulnerability_audits(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('adm.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('adm.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
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


@work_request_group.command(name=cli_util.override('adm.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', help=u"""A filter to return only resources that belong to the specified compartment identifier.""")
@cli_util.option('--work-request-id', help=u"""The identifier of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources that match the specified OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The Oracle Cloud Identifier ([OCID]) of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field used to sort WorkRequests. Only one sort order is allowed. Default order for _timeAccepted_ is **descending**.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'adm', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@knowledge_base_group.command(name=cli_util.override('adm.update_knowledge_base.command_name', 'update'), help=u"""Updates one or more attributes of the specified Knowledge Base. \n[Command Reference](updateKnowledgeBase)""")
@cli_util.option('--knowledge-base-id', required=True, help=u"""The Oracle Cloud Identifier ([OCID]) of a Knowledge Base, as a URL path parameter.""")
@cli_util.option('--display-name', help=u"""The name of the Knowledge Base.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_knowledge_base(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, knowledge_base_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(knowledge_base_id, six.string_types) and len(knowledge_base_id.strip()) == 0:
        raise click.UsageError('Parameter --knowledge-base-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.update_knowledge_base(
        knowledge_base_id=knowledge_base_id,
        update_knowledge_base_details=_details,
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


@vulnerability_audit_group.command(name=cli_util.override('adm.update_vulnerability_audit.command_name', 'update'), help=u"""Updates one or more attributes of the specified Vulnerability Audit. \n[Command Reference](updateVulnerabilityAudit)""")
@cli_util.option('--vulnerability-audit-id', required=True, help=u"""Unique Vulnerability Audit identifier path parameter.""")
@cli_util.option('--display-name', help=u"""The name of the Vulnerability Audit.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'adm', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'adm', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'adm', 'class': 'VulnerabilityAudit'})
@cli_util.wrap_exceptions
def update_vulnerability_audit(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, vulnerability_audit_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(vulnerability_audit_id, six.string_types) and len(vulnerability_audit_id.strip()) == 0:
        raise click.UsageError('Parameter --vulnerability-audit-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('adm', 'application_dependency_management', ctx)
    result = client.update_vulnerability_audit(
        vulnerability_audit_id=vulnerability_audit_id,
        update_vulnerability_audit_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_vulnerability_audit') and callable(getattr(client, 'get_vulnerability_audit')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_vulnerability_audit(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
